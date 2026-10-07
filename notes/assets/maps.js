// Exact intermediate maps for the shear/translation worked example.
const demo = document.querySelector('[data-map-demo]');
if (demo) {
  const slider = demo.querySelector('input');
  const play = demo.querySelector('[data-map-play]');
  const step = demo.querySelector('[data-map-step]');
  const reset = demo.querySelector('[data-map-reset]');
  const phase = demo.querySelector('[data-map-phase]');
  const panels = [...demo.querySelectorAll('[data-map-order]')];
  const ns = 'http://www.w3.org/2000/svg';
  let progress = 0, running = false, frame = 0, previous = null;
  const point = ([x, y]) => [36 + 52 * x, 240 - 52 * y];
  const square = [[.75, 1.75], [1.25, 1.75], [1.25, 2.25], [.75, 2.25]];
  const positions = points => points.map(p => point(p).join(',')).join(' ');
  const map = (p, order) => {
    const first = Math.min(progress, 1), second = Math.max(progress - 1, 0);
    const [x, y] = p;
    return order === 'shear-first'
      ? [x + first * y, y + second]
      : [x + second * (y + first), y + first];
  };
  function element(tag, attributes, parent) {
    const node = document.createElementNS(ns, tag);
    for (const [name, value] of Object.entries(attributes)) node.setAttribute(name, value);
    parent.append(node);
    return node;
  }
  for (const panel of panels) {
    const svg = panel.querySelector('svg');
    for (let x = 0; x <= 5; x++) {
      const px = point([x, 0])[0];
      element('line', {x1:px, y1:32, x2:px, y2:240, class:'map-grid'}, svg);
      element('text', {x:px, y:260, 'text-anchor':'middle'}, svg).textContent = x;
    }
    for (let y = 1; y <= 4; y++) {
      const py = point([0, y])[1];
      element('line', {x1:36, y1:py, x2:322, y2:py, class:'map-grid'}, svg);
      element('text', {x:23, y:py + 4, 'text-anchor':'middle'}, svg).textContent = y;
    }
    element('path', {d:'M36 24 V240 H328', class:'map-axes', fill:'none'}, svg);
    element('text', {x:333,y:245}, svg).textContent = 'x';
    element('text', {x:28,y:17}, svg).textContent = 'y';
    element('polygon', {points:positions(square), class:'map-original'}, svg);
    panel.shape = element('polygon', {class:'map-shape'}, svg);
    panel.dot = element('circle', {r:4, class:'map-point'}, svg);
  }
  function draw() {
    slider.value = progress.toFixed(3);
    phase.textContent = progress === 0 ? 'Starting state' : progress < 1 ? 'Applying the first map' : progress === 1 ? 'First map complete' : progress < 2 ? 'Applying the second map' : 'Both maps complete';
    slider.setAttribute('aria-valuetext', phase.textContent + '; progress ' + progress.toFixed(2) + ' of 2');
    for (const panel of panels) {
      const order = panel.dataset.mapOrder;
      const center = map([1, 2], order), screen = point(center);
      panel.shape.setAttribute('points', positions(square.map(p => map(p, order))));
      panel.dot.setAttribute('cx', screen[0]);
      panel.dot.setAttribute('cy', screen[1]);
      const f = center[0] ** 2 + 2 * center[1];
      panel.querySelector('output').textContent = 'Point (' + center[0].toFixed(2) + ', ' + center[1].toFixed(2) + '); f = ' + f.toFixed(2) + '; change = ' + (f - 5).toFixed(2);
    }
  }
  function pause() {
    running = false;
    previous = null;
    cancelAnimationFrame(frame);
    play.textContent = progress === 2 ? 'Replay both orders' : 'Play both orders';
    play.setAttribute('aria-pressed', 'false');
  }
  function tick(now) {
    if (!running) return;
    if (previous !== null) progress = Math.min(2, progress + Math.min(now - previous, 100) / 3000);
    previous = now;
    draw();
    if (progress === 2) pause();
    else frame = requestAnimationFrame(tick);
  }
  play.addEventListener('click', () => {
    if (running) return pause();
    if (progress === 2) progress = 0;
    running = true; previous = null;
    play.textContent = 'Pause animation';
    play.setAttribute('aria-pressed', 'true');
    draw();
    frame = requestAnimationFrame(tick);
  });
  step.addEventListener('click', () => {
    pause();
    progress = progress < 1 ? 1 : 2;
    draw(); pause();
  });
  reset.addEventListener('click', () => { progress = 0; pause(); draw(); });
  slider.addEventListener('input', () => { progress = Number(slider.value); pause(); draw(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) pause(); });
  window.addEventListener('pagehide', pause);
  window.addEventListener('beforeprint', pause);
  // Leaving the example stops motion; resuming is always deliberate.
  if ('IntersectionObserver' in window) new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) pause();
  }).observe(demo);
  demo.querySelectorAll('button,input').forEach(control => { control.disabled = false; });
  draw();
}
