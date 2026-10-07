import { RequestGate } from "./protocol.js";

const root = document.getElementById("fluid-lab");
if (root) {
  const canvas = root.querySelector("canvas");
  const ctx = canvas.getContext("2d");
  const status = root.querySelector("[data-status]");
  const play = root.querySelector("[data-play]");
  const step = root.querySelector("[data-step]");
  const reset = root.querySelector("[data-reset]");
  const gate = new RequestGate();
  let worker = null;
  let running = false;
  let dirty = false;
  let failed = false;
  let state = null;
  let angle = 0.58;
  const tilt = 0.42;

  function readSettings() {
    return {
      type: "reset",
      n: Number(root.querySelector("[name=grid]").value),
      nu: Number(root.querySelector("[name=viscosity]").value),
      preset: root.querySelector("[name=preset]").value,
    };
  }
  function updateControls() {
    play.textContent = running ? "Pause" : "Play";
    play.setAttribute("aria-pressed", String(running));
    play.disabled = dirty || failed;
    step.disabled = dirty || failed || gate.busy;
  }
  function describeState() {
    if (dirty || failed) return; // Preserve the actionable settings/error text.
    const d = state?.diagnostics;
    status.textContent = d
      ? `${running ? "Running" : "Paused"} · ${d.n}³ grid · ${d.steps} steps`
      : "Preparing the numerical field…";
  }
  function pause() {
    running = false;
    updateControls();
    describeState();
  }
  function fail(message) {
    running = false;
    failed = true;
    gate.invalidate();
    updateControls();
    status.textContent = `Simulation stopped: ${message} Select Reset to start again.`;
  }
  function send(payload) {
    try {
      if (!worker) {
        worker = new Worker(new URL("./worker.js", import.meta.url), {
          type: "module",
        });
        worker.onmessage = receive;
        worker.onerror = (event) => {
          event.preventDefault();
          worker?.terminate();
          worker = null;
          fail(
            "The worker failed. Serve this chapter over HTTP if it was opened as a local file.",
          );
        };
      }
      worker.postMessage(gate.issue(payload));
      updateControls();
    } catch (error) {
      fail(error.message);
    }
  }
  function resetField() {
    running = false;
    dirty = false;
    failed = false;
    gate.invalidate();
    state = null;
    send(readSettings());
    if (!failed) status.textContent = "Resetting initial data…";
    draw();
  }
  play.onclick = () => {
    running = !running;
    updateControls();
    describeState();
    if (running && !gate.busy) send({ type: "step" });
  };
  step.onclick = () => {
    pause();
    if (!gate.busy && !dirty && !failed) send({ type: "step" });
  };
  reset.onclick = resetField;
  root.querySelectorAll("select,input").forEach((control) => {
    control.addEventListener("change", () => {
      running = false;
      dirty = true;
      gate.invalidate();
      updateControls();
      status.textContent = "Settings changed. Select Reset to apply them.";
    });
  });
  root.querySelector("[data-rotate]").onclick = () => {
    angle += Math.PI / 8;
    draw();
  };
  function project(p, w, h) {
    const x = p[0] - Math.PI,
      y = p[1] - Math.PI,
      z = p[2] - Math.PI,
      a = x * Math.cos(angle) - y * Math.sin(angle),
      b = x * Math.sin(angle) + y * Math.cos(angle),
      v = z * Math.cos(tilt) - b * Math.sin(tilt),
      depth = z * Math.sin(tilt) + b * Math.cos(tilt),
      scale = Math.min(w, h) * 0.093;
    return [w / 2 + a * scale, h / 2 - v * scale, depth];
  }
  function draw() {
    const box = canvas.getBoundingClientRect(),
      dpr = Math.min(devicePixelRatio || 1, 2),
      w = box.width,
      h = box.height;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.fillStyle = "#101e27";
    ctx.fillRect(0, 0, w, h);
    const corners = Array.from({ length: 8 }, (_, i) => [
      i & 1 ? 2 * Math.PI : 0,
      i & 2 ? 2 * Math.PI : 0,
      i & 4 ? 2 * Math.PI : 0,
    ]);
    ctx.strokeStyle = "#46606a";
    ctx.lineWidth = 1;
    for (let i = 0; i < 8; i++)
      for (let bit = 1; bit <= 4; bit *= 2)
        if (!(i & bit)) {
          const a = project(corners[i], w, h),
            b = project(corners[i | bit], w, h);
          ctx.beginPath();
          ctx.moveTo(a[0], a[1]);
          ctx.lineTo(b[0], b[1]);
          ctx.stroke();
        }
    if (!state) return;
    const dots = state.tracers
      .map((p, i) => ({ p: project(p, w, h), speed: state.speeds[i] }))
      .sort((a, b) => a.p[2] - b.p[2]);
    for (const dot of dots) {
      const brightness = Math.min(dot.speed / 3, 1);
      ctx.fillStyle = `hsl(${185 - 145 * brightness} 78% ${62 + 8 * brightness}%)`;
      ctx.globalAlpha = 0.6 + (0.35 * (dot.p[2] + 5)) / 10;
      ctx.beginPath();
      ctx.arc(dot.p[0], dot.p[1], 2.2, 0, 2 * Math.PI);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
    ctx.fillStyle = "#cbdadf";
    ctx.font = "12px system-ui";
    ctx.fillText("Warmer points = faster flow", 16, h - 16);
  }
  function receive({ data }) {
    // A late step/reset reply must not update a newly selected field or controls.
    if (!gate.accept(data)) return;
    if (data.type === "error") {
      fail(data.message);
      return;
    }
    state = data;
    for (const [key, value] of Object.entries(data.diagnostics)) {
      const element = root.querySelector(`[data-value="${key}"]`);
      if (element)
        element.textContent =
          key === "steps" || key === "n"
            ? value
            : key === "divergence"
              ? value.toExponential(2)
              : value.toFixed(key === "dt" ? 5 : 4);
    }
    updateControls();
    describeState();
    draw();
    if (running)
      setTimeout(() => {
        if (running && !gate.busy && !dirty && !failed) send({ type: "step" });
      }, 16);
  }
  new ResizeObserver(draw).observe(canvas);
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) pause();
  });
  window.addEventListener("pagehide", () => {
    pause();
    worker?.terminate();
    worker = null;
    gate.invalidate();
  });
  resetField();
}
