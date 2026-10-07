import assert from "node:assert/strict";
import { fft, fft3, Fluid } from "./solver.js";
import { RequestGate } from "./protocol.js";
let checks = 0;
const close = (a, b, tol = 1e-10) => {
  assert.ok(Math.abs(a - b) <= tol, `${a} != ${b}`);
  checks++;
};
for (const n of [2, 8, 16]) {
  const r = Float64Array.from(
      { length: n },
      (_, i) => Math.sin(i * 1.7) + i * 0.03,
    ),
    im = Float64Array.from({ length: n }, (_, i) => Math.cos(i * 0.4) * 0.2),
    a = r.slice(),
    b = im.slice();
  fft(r, im);
  for (let k = 0; k < n; k++) {
    let R = 0,
      I = 0;
    for (let j = 0; j < n; j++) {
      const x = (-2 * Math.PI * j * k) / n;
      R += a[j] * Math.cos(x) - b[j] * Math.sin(x);
      I += a[j] * Math.sin(x) + b[j] * Math.cos(x);
    }
    close(r[k], R);
    close(im[k], I);
  }
  fft(r, im, true);
  for (let i = 0; i < n; i++) {
    close(r[i], a[i]);
    close(im[i], b[i]);
  }
}
{
  const n = 4,
    r = Float64Array.from({ length: n ** 3 }, (_, i) => Math.sin(i)),
    im = new Float64Array(n ** 3),
    orig = r.slice();
  fft3(r, im, n);
  fft3(r, im, n, true);
  for (let i = 0; i < r.length; i++) {
    close(r[i], orig[i]);
    close(im[i], 0);
  }
}
for (const n of [16, 32]) {
  const f = new Fluid(n, 0.08, "abc");
  close(f.diagnostics().energy, 1.5);
  close(f.diagnostics().enstrophy, 1.5);
  const nl = f.nonlinear(f.u);
  assert.ok(
    nl.reduce(
      (max, v) =>
        Math.max(
          max,
          v.re.reduce((m, x) => Math.max(m, Math.abs(x)), 0),
          v.im.reduce((m, x) => Math.max(m, Math.abs(x)), 0),
        ),
      0,
    ) < 1e-9,
  );
  checks++;
  for (let j = 0; j < 6; j++) f.step(0.01);
  close(f.diagnostics().energy, 1.5 * Math.exp(-2 * 0.08 * f.time), 1e-11);
  assert.ok(f.diagnostics().divergence < 1e-12);
  checks++;
}
{
  const f = new Fluid(16, 0);
  for (let c = 0; c < 3; c++)
    for (let i = 0; i < f.m; i++) {
      f.u[c].re[i] = Math.sin(i * (c + 1));
      f.u[c].im[i] = Math.cos(i * (c + 2));
    }
  f.project(f.u);
  assert.ok(f.diagnostics().divergence < 1e-13);
  checks++;
  for (let i = 0; i < f.m; i++)
    if (!f.keep[i] || f.k2[i] === 0)
      for (const v of f.u) {
        close(v.re[i], 0);
        close(v.im[i], 0);
      }
}
function advance(dt, T) {
  const f = new Fluid(16, 0.03);
  for (let t = 0; t < T - 1e-12; t += dt) f.step(dt);
  return f;
}
const difference = (a, b) =>
  Math.sqrt(
    a.u.reduce(
      (sum, v, c) =>
        sum +
        v.re.reduce(
          (s, x, i) =>
            s + (x - b.u[c].re[i]) ** 2 + (v.im[i] - b.u[c].im[i]) ** 2,
          0,
        ),
      0,
    ),
  ) / a.m;
{
  const coarse = advance(0.01, 0.04),
    fine = advance(0.005, 0.04),
    ref = advance(0.00125, 0.04);
  const ec = difference(coarse, ref),
    ef = difference(fine, ref);
  assert.ok(ec > ef * 3, `Expected second-order improvement: ${ec} / ${ef}`);
  checks++;
  assert.ok(fine.diagnostics().energy < 0.125);
  checks++;
  console.log("Taylor–Green refinement errors:", ec, ef);
}
console.log(
  `PASS: ${checks} numerical assertions (DFT/FFT, projection/dealiasing, ABC decay at both grids, nonlinear refinement).`,
);

{
  const f = new Fluid(16, 0.03, "abc"),
    point = [
      (2 * Math.PI * 3) / 16,
      (2 * Math.PI * 5) / 16,
      (2 * Math.PI * 7) / 16,
    ],
    value = f.sample(point),
    idx = (3 * 16 + 5) * 16 + 7;
  for (let c = 0; c < 3; c++) {
    close(value[c], f.physical[c][idx]);
    close(f.sample(point.map((x) => x + 2 * Math.PI))[c], value[c]);
  }
}
let reply;
globalThis.onmessage = null;
globalThis.postMessage = (data) => {
  reply = data;
};
await import("./worker.js");
globalThis.onmessage({
  data: { type: "reset", n: 16, nu: 0.03, preset: "abc" },
});
assert.equal(reply.type, "state");
const before = reply.tracers.map((p) => p.slice());
globalThis.onmessage({ data: { type: "step" } });
assert.equal(reply.type, "state");
assert.equal(reply.diagnostics.steps, 1);
assert.ok(reply.tracers.some((p, i) => p.some((x, c) => x !== before[i][c])));
assert.ok(
  reply.tracers.every((p) =>
    p.every((x) => Number.isFinite(x) && x >= 0 && x < 2 * Math.PI),
  ),
);
console.log(
  "PASS: periodic sampling and worker reset/step/tracer smoke checks.",
);

// Stale replies must neither overwrite current state nor clear its busy flag.
const gate = new RequestGate();
const oldStep = gate.issue({ type: "step" });
gate.invalidate(); // settings changed while the old worker computation runs
assert.equal(gate.accept({ ...oldStep, type: "state" }), false);
const firstReset = gate.issue({ type: "reset" });
gate.invalidate();
const latestReset = gate.issue({ type: "reset" });
assert.equal(gate.accept({ ...firstReset, type: "state" }), false);
assert.equal(gate.busy, true);
assert.equal(gate.accept({ ...latestReset, type: "state" }), true);
assert.equal(gate.busy, false);
assert.equal(gate.accept({ ...latestReset, type: "state" }), false);
const badReset = gate.issue({ type: "reset", n: 8, nu: 0.03, preset: "abc" });
globalThis.onmessage({ data: badReset });
assert.equal(reply.type, "error");
assert.equal(reply.requestId, badReset.requestId);
assert.equal(reply.generation, badReset.generation);
assert.equal(gate.accept(reply), true);
console.log(
  "PASS: request generations, stale replies, duplicate replies and tagged worker errors.",
);
