// Frame renderer for "Motion, measurement, acceleration".
// window.renderFrame(T) draws the frame at film time T (seconds). Every
// picture is computed from the exact solutions named on screen:
//   Taylor–Green cells  u = (sin x cos y, −cos x sin y, 0) e^{−2νt},
//                       p = ¼(cos 2x + cos 2y) e^{−4νt};
//   sliding layers      u = a(0) e^{−νN²t} sin(Ny) e₁,  p = 0.
// Part two adds pictures computed from further formulas, each labelled on
// screen: the published scaling laws (OpenAI, "Finite time blowup for
// Navier–Stokes", §2.1 and §3.5), a hand-squeezed Lamb–Oseen vortex and its
// residual force, plane waves and their mean flux, an exact shearing wave on
// U = (Sy, 0), and determinant-one box maps. Schematics are marked as such.
// The numerical readouts are evaluated live from those formulas.
'use strict';

const W = 1920, H = 1080, TAU = 2 * Math.PI;
const C = {
  bg: '#f6f4ee', ink: '#1c1d21', muted: '#77757a', faint: '#d8d3c6', paper: '#fffdf8',
  blue: '#2b59c3', red: '#c8462b', gold: '#c08f12', teal: '#17876f', purple: '#6c4bb8',
};
const SERIF = '"Bitstream Charter", "Charter", "DejaVu Serif", "Songti SC", serif';
const SANS = '"Inter", "DejaVu Sans", "PingFang SC", sans-serif';

const cv = document.getElementById('c');
const g = cv.getContext('2d');
let TL = null; // timeline.json, injected by render.mjs
let FILM_LANG = 'en';
function tr(s) {
  s = String(s);
  if (FILM_LANG !== 'zh') return s;
  if (Object.hasOwn(window.FILM_ZH, s)) return window.FILM_ZH[s];
  for (const [pattern, replacement] of window.FILM_ZH_DYNAMIC) s = s.replace(pattern, replacement);
  return s;
}

// ---------- small utilities ----------
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const smooth = x => { x = clamp(x); return x * x * (3 - 2 * x); };
const ramp = (t, a, d = 0.8) => smooth((t - a) / d);
const lerp = (a, b, s) => a + (b - a) * s;
function rgba(hex, a) {
  const n = parseInt(hex.slice(1), 16);
  return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`;
}
function text(s, x, y, { size = 30, font = SERIF, color = C.ink, align = 'left', alpha = 1, weight = '', base = 'alphabetic', italic = false } = {}) {
  if (alpha <= 0) return;
  s = tr(s);
  g.save();
  g.globalAlpha *= alpha;
  g.font = `${italic ? 'italic ' : ''}${weight} ${size}px ${font}`;
  g.fillStyle = color; g.textAlign = align; g.textBaseline = base;
  g.fillText(s, x, y);
  g.restore();
}
function arrow(x0, y0, x1, y1, { color = C.ink, width = 4, head = 16, alpha = 1, dash = null } = {}) {
  const dx = x1 - x0, dy = y1 - y0, L = Math.hypot(dx, dy);
  if (alpha <= 0 || L < 0.5) return;
  const ux = dx / L, uy = dy / L, h = Math.min(head, L * 0.6);
  g.save();
  g.globalAlpha *= alpha;
  g.strokeStyle = color; g.fillStyle = color; g.lineWidth = width; g.lineCap = 'round';
  if (dash) g.setLineDash(dash);
  g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1 - ux * h * 0.7, y1 - uy * h * 0.7); g.stroke();
  g.setLineDash([]);
  g.beginPath();
  g.moveTo(x1, y1);
  g.lineTo(x1 - ux * h - uy * h * 0.45, y1 - uy * h + ux * h * 0.45);
  g.lineTo(x1 - ux * h + uy * h * 0.45, y1 - uy * h - ux * h * 0.45);
  g.closePath(); g.fill();
  g.restore();
}
function sci(v, digits = 1) {
  if (v === 0) return '0';
  const e = Math.floor(Math.log10(Math.abs(v)));
  const m = (v / 10 ** e).toFixed(digits);
  const sup = String(e).replace('-', '⁻').replace(/\d/g, d => '⁰¹²³⁴⁵⁶⁷⁸⁹'[d]);
  return `${m}×10${sup}`;
}
const fx = (v, d = 3) => (v >= 0 ? '+' : '−') + Math.abs(v).toFixed(d);

// ---------- equation overlays (KaTeX) ----------
const EQ = {
  tg_field: String.raw`u=\big(\sin x\cos y,\;-\cos x\sin y,\;0\big)\,e^{-2\nu t}`,
  ode: String.raw`X'(t)=u\big(t,X(t)\big)`,
  phi: String.raw`\Phi_t:\;X(0)\longmapsto X(t)`,
  tg_p: String.raw`p=\tfrac14(\cos 2x+\cos 2y)\,e^{-4\nu t}`,
  chain: String.raw`\frac{d}{dt}\,u\big(t,X(t)\big)=\textcolor{#c08f12}{\partial_t u}+\textcolor{#c8462b}{(u\cdot\nabla)u}`,
  ns: String.raw`\underbrace{\textcolor{#c08f12}{\partial_t u}+\textcolor{#c8462b}{(u\cdot\nabla)u}}_{\text{acceleration}}=\underbrace{\textcolor{#6c4bb8}{-\nabla p}}_{\text{pressure}}+\underbrace{\textcolor{#17876f}{\nu\Delta u}}_{\text{viscosity}}`,
  match1: String.raw`\textcolor{#c8462b}{(u\cdot\nabla)u}=\textcolor{#6c4bb8}{-\nabla p}=\tfrac12(\sin 2x,\ \sin 2y,\ 0)\,e^{-4\nu t}`,
  match2: String.raw`\textcolor{#c08f12}{\partial_t u}=\textcolor{#17876f}{\nu\Delta u}=-2\nu\,u`,
  lay_u: String.raw`u=a(t)\,\sin(Ny)\,e_1`,
  lay_adv: String.raw`(u\cdot\nabla)u=a\sin(Ny)\,\partial_x u=0,\qquad p=0`,
  lay_ode: String.raw`a'=-\nu N^2a\;\Longrightarrow\;a(t)=a(0)\,e^{-\nu N^2t}`,
  lay_X: String.raw`X_1(t)=X_1(0)+\frac{a(0)}{\nu N^2}\big(1-e^{-\nu N^2t}\big)\sin\big(NX_2(0)\big)`,
  en_def: String.raw`E=\tfrac12\int_{\mathbb T^3}|u|^2\,dx`,
  en_val: String.raw`E(0)=2\pi^3a^2\ \text{ for both}`,
  en_t: String.raw`E(t)=E(0)\,e^{-2\nu N^2t}`,
  en_id: String.raw`\frac{dE}{dt}=-\nu\!\int_{\mathbb T^3}\!|\nabla u|^2\,dx=-2\nu N^2E`,
  gr_pts: String.raw`y_j=\tfrac{2\pi j}{8},\quad j=0,1,\dots,7`,
  gr_alias: String.raw`-\sin(7y_j)=\sin(y_j)\ \text{ at every } y_j`,
  gr_decay1: String.raw`\textcolor{#2b59c3}{u_1=e^{-\nu t}\sin y}`,
  gr_decay2: String.raw`\textcolor{#c8462b}{u_1=-e^{-49\nu t}\sin 7y}`,
  q_crit: String.raw`R(x)=R(x')\ \Longrightarrow\ R(\Phi_t x)=R(\Phi_t x')`,
  q_x: String.raw`x`, q_xt: String.raw`\Phi_t x`, q_r: String.raw`R(x)`, q_rt: String.raw`R(\Phi_t x)`,
  q_phi: String.raw`\Phi_t`, q_R1: String.raw`R`, q_R2: String.raw`R`, q_S: String.raw`?`,
  ab_U: String.raw`U_Tf=f\circ T,\qquad \Delta_Tf=U_Tf-f`,
  ab_ex: String.raw`x\in\mathbb R,\qquad T(x)=x+1,\qquad f(x)=x^2`,
  pk_l: String.raw`\ell_r\asymp\tau^{1/2},\qquad \ell_z\asymp\tau^{1/2-h}`,
  pk_u: String.raw`|u_\theta|,\,|u_z|\asymp\tau^{-1/2-h},\qquad 0<h<\tfrac{1}{100}`,
  pk_E: String.raw`E_{\text{core}}\asymp\underbrace{\tau^{3/2-h}}_{\text{volume}}\cdot\underbrace{\tau^{-1-2h}}_{\text{speed}^2}=\tau^{1/2-3h}\to0`,
  rs_def: String.raw`f:=\partial_t u+(u\cdot\nabla)u-\nu\Delta u+\nabla p`,
  rs_lo: String.raw`u_\theta=\frac{\Gamma}{2\pi r}\Big(1-e^{-r^2/(4\nu\tau)}\Big)`,
  rs_R: String.raw`f_\theta=\frac{\Gamma\,r}{4\pi\nu\tau^2}\,e^{-r^2/(4\nu\tau)},\qquad \max_r f_\theta\propto\tau^{-3/2}`,
  wv_w: String.raw`w=a\cos(\xi\cdot x),\qquad a\cdot\xi=0`,
  wv_avg: String.raw`\langle w\rangle=0,\qquad \langle w\otimes w\rangle=\tfrac12\,a\otimes a`,
  wv_cone: String.raw`T=c_1v_1+c_2v_2,\qquad c_1,\,c_2>0`,
  wv_k: String.raw`k(t)=\big(k_x,\;k_y(0)-Sk_xt\big)`,
  wv_A: String.raw`A(t)=A_0\,\frac{|k(0)|}{|k(t)|}\,\exp\Big(-\nu\!\int_0^t\!|k|^2\Big)`,
  wv_E: String.raw`\frac{d}{dt}\,\tfrac12\!\int\!|w|^2=-S\!\int\! w_1w_2\;-\;\nu\!\int\!|\nabla w|^2`,
  pr_lim: String.raw`\sup_{0\le t<1}\|u(t)\|_{L^2}<\infty,\qquad \limsup_{t\uparrow1}\|u(t)\|_{L^\infty}=\infty`,
  pr_en: String.raw`\|u(t)\|_{L^2}\le\int_0^t\|f(s)\|_{L^2}\,ds`,
  cp_sq: String.raw`\Phi_{t_{n+1},t_n}\big(E(c)\big)=E(Tc)`,
  cp_halt: String.raw`\big(\exists\,t\ge0:\ X(t;a_*)\in(-1,2)^3\big)\iff\text{the machine halts}`,
  cp_vol: String.raw`\lambda_1^{\,s}\lambda_2^{\,s}\lambda_3^{\,s}=1`,
  cp_c: String.raw`c`, cp_Tc: String.raw`Tc`, cp_Ec: String.raw`E(c)`, cp_ETc: String.raw`E(Tc)`,
  cp_T: String.raw`T`, cp_Phi: String.raw`\Phi`, cp_E1: String.raw`E`, cp_E2: String.raw`E`,
};
const eqEl = {};
let eqShown = new Set();
function buildEquations() {
  const host = document.getElementById('eqs');
  host.replaceChildren();
  for (const [id, tex] of Object.entries(EQ)) {
    const d = document.createElement('div');
    d.className = 'eq';
    const localized = FILM_LANG === 'zh' ? tex.replace(/\\text\{([^}]+)\}/g, (m, label) => `\\text{${window.FILM_ZH_MATH[label] ?? label}}`) : tex;
    katex.render(localized, d, { displayMode: false, throwOnError: true, output: 'html' });
    host.appendChild(d);
    eqEl[id] = d;
  }
}
// Show equation `id` centred at (x, y) with font size `size`; anchor 'l' left-aligns at x.
function eq(id, x, y, { alpha = 1, size = 40, anchor = 'c', color = null } = {}) {
  const d = eqEl[id];
  if (alpha <= 0.001) return;
  d.style.fontSize = size + 'px';
  if (color) d.style.color = color;
  const w = d.offsetWidth, h = d.offsetHeight;
  const left = anchor === 'l' ? x : x - w / 2;
  d.style.transform = `translate(${left}px, ${y - h / 2}px)`;
  d.style.opacity = alpha;
  eqShown.add(id);
}
function hideUnusedEquations(used) {
  for (const id of Object.keys(eqEl)) if (!used.has(id)) eqEl[id].style.opacity = 0;
}

// ---------- the box ----------
const BOX = { x: 150, y: 165, s: 810 };
let VIEW = { x0: 0, y0: 0, span: TAU }; // part of the periodic box shown in BOX
const px = (x, b = BOX) => b === BOX ? BOX.x + (x - VIEW.x0) / VIEW.span * BOX.s : b.x + (x / TAU) * b.s;
const py = (y, b = BOX) => b === BOX ? BOX.y + BOX.s - (y - VIEW.y0) / VIEW.span * BOX.s : b.y + b.s - (y / TAU) * (b.h ?? b.s);
function drawBox(alpha = 1, b = BOX, { marks = 0 } = {}) {
  if (alpha <= 0) return;
  const h = b.h ?? b.s;
  g.save();
  g.globalAlpha *= alpha;
  g.fillStyle = C.paper; g.fillRect(b.x, b.y + b.s - h, b.s, h);
  g.strokeStyle = C.ink; g.lineWidth = 2; g.strokeRect(b.x, b.y + b.s - h, b.s, h);
  if (marks > 0) { // identification marks: single chevrons left/right, double top/bottom
    g.globalAlpha *= marks;
    const chev = (x, y, dir, n) => {
      for (let k = 0; k < n; k++) {
        const o = (k - (n - 1) / 2) * 16;
        g.beginPath();
        if (dir === 'up') { g.moveTo(x - 12 + o * 0, y + 8 + o); g.lineTo(x, y - 6 + o); g.lineTo(x + 12, y + 8 + o); }
        else { g.moveTo(x - 8 + o, y - 12); g.lineTo(x + 6 + o, y); g.lineTo(x - 8 + o, y + 12); }
        g.stroke();
      }
    };
    g.lineWidth = 3; g.strokeStyle = C.blue;
    chev(b.x, b.y + b.s - h / 2, 'up', 1); chev(b.x + b.s, b.y + b.s - h / 2, 'up', 1);
    g.strokeStyle = C.red;
    chev(b.x + b.s / 2, b.y + b.s - h, 'right', 2); chev(b.x + b.s / 2, b.y + b.s, 'right', 2);
  }
  g.restore();
}

// ---------- Taylor–Green cells ----------
const NU_TG = 0.01;
const tgU = (x, y) => [Math.sin(x) * Math.cos(y), -Math.cos(x) * Math.sin(y)]; // steady shape
const tgF = t => Math.exp(-2 * NU_TG * t);
const tgS = t => (1 - Math.exp(-2 * NU_TG * t)) / (2 * NU_TG); // reparametrised time ∫F
function rk4Steady(x, y, ds) {
  const [a1, b1] = tgU(x, y);
  const [a2, b2] = tgU(x + 0.5 * ds * a1, y + 0.5 * ds * b1);
  const [a3, b3] = tgU(x + 0.5 * ds * a2, y + 0.5 * ds * b2);
  const [a4, b4] = tgU(x + ds * a3, y + ds * b3);
  return [x + ds / 6 * (a1 + 2 * a2 + 2 * a3 + a4), y + ds / 6 * (b1 + 2 * b2 + 2 * b3 + b4)];
}
// Precomputed particle paths on a grid of reparametrised time s.
const TG = { ds: 0.02, steps: 0, n: 0, pos: null, col: [], lines: [] };
function buildTG(sMax) {
  const pts = [];
  const M = 46;
  for (let i = 0; i < M; i++) for (let j = 0; j < M; j++) {
    const x = (i + 0.5) / M * TAU, y = (j + 0.5) / M * TAU;
    pts.push([x, y]);
    const hue = (x / TAU) * 300 + 200, light = 34 + 30 * (y / TAU);
    TG.col.push(`hsl(${hue % 360},58%,${light}%)`);
  }
  const nDots = pts.length, P = 900;
  // dye blobs: material circles carried by the flow (one straddles a cell boundary)
  for (const [cx, cy, r, hue] of [[1.05, 2.05, 0.42, 222], [Math.PI + 0.02, 4.45, 0.36, 12], [4.55, 1.35, 0.4, 150], [2.2, 4.9, 0.34, 280]]) {
    TG.lines.push({ start: pts.length, n: P, c0: [cx, cy], r, hue });
    for (let q = 0; q < P; q++) pts.push([cx + r * Math.cos(TAU * q / P), cy + r * Math.sin(TAU * q / P)]);
  }
  TG.nDots = nDots; TG.n = pts.length; TG.steps = Math.ceil(sMax / TG.ds) + 2;
  TG.pos = new Float32Array(TG.steps * TG.n * 2);
  const cur = pts.map(p => p.slice());
  for (let s = 0; s < TG.steps; s++) {
    for (let i = 0; i < TG.n; i++) {
      TG.pos[(s * TG.n + i) * 2] = cur[i][0];
      TG.pos[(s * TG.n + i) * 2 + 1] = cur[i][1];
      cur[i] = rk4Steady(cur[i][0], cur[i][1], TG.ds);
    }
  }
}
function tgPos(i, t) {
  const f = clamp(tgS(t) / TG.ds, 0, TG.steps - 1.001), k = Math.floor(f), r = f - k;
  const a = (k * TG.n + i) * 2, b = ((k + 1) * TG.n + i) * 2;
  return [lerp(TG.pos[a], TG.pos[b], r), lerp(TG.pos[a + 1], TG.pos[b + 1], r)];
}
function drawTGDots(t, alpha, { radius = 4.2, b = BOX } = {}) {
  if (alpha <= 0) return;
  g.save(); g.globalAlpha *= alpha;
  g.beginPath(); g.rect(b.x, b.y, b.s, b.s); g.clip();
  for (let i = 0; i < TG.nDots; i++) {
    const [x, y] = tgPos(i, t);
    g.fillStyle = TG.col[i];
    g.beginPath(); g.arc(px(x, b), py(y, b), radius, 0, TAU); g.fill();
  }
  g.restore();
}
function drawBlobs(t, alpha, ghost = 0) {
  if (alpha <= 0) return;
  g.save(); g.globalAlpha *= alpha;
  g.beginPath(); g.rect(BOX.x, BOX.y, BOX.s, BOX.s); g.clip();
  g.lineJoin = 'round';
  for (const L of TG.lines) {
    if (ghost > 0) { // where the blob started: X(0)
      g.save(); g.globalAlpha *= ghost; g.setLineDash([7, 7]); g.lineWidth = 2; g.strokeStyle = `hsl(${L.hue},45%,35%)`;
      g.beginPath(); g.arc(px(L.c0[0]), py(L.c0[1]), L.r / VIEW.span * BOX.s, 0, TAU); g.stroke(); g.restore();
    }
    g.beginPath();
    for (let q = 0; q < L.n; q++) {
      const [x, y] = tgPos(L.start + q, t);
      q ? g.lineTo(px(x), py(y)) : g.moveTo(px(x), py(y));
    }
    g.closePath();
    g.fillStyle = `hsla(${L.hue},60%,50%,0.55)`; g.fill();
    g.lineWidth = 2.5; g.strokeStyle = `hsl(${L.hue},55%,30%)`; g.stroke();
  }
  g.restore();
}
function drawStreamlines(alpha, b = BOX) { // level sets of ψ = sin x sin y
  if (alpha <= 0) return;
  g.save(); g.globalAlpha *= alpha;
  g.beginPath(); g.rect(BOX.x, BOX.y, BOX.s, BOX.s); g.clip();
  g.strokeStyle = rgba(C.ink, 0.28); g.lineWidth = 1.5;
  for (const c of [0.15, 0.35, 0.55, 0.75, 0.92]) {
    for (const [cx, cy] of [[1, 1], [3, 1], [1, 3], [3, 3]]) {
      const sgn = ((cx === 1) === (cy === 1)) ? 1 : -1;
      g.beginPath();
      // ψ = c on the cell: solve sin y = c / sin x along x, both branches
      const xs = [], N = 160;
      const x0 = (cx - 1) * Math.PI / 2, y0 = (cy - 1) * Math.PI / 2;
      const top = [], bot = [];
      for (let k = 0; k <= N; k++) {
        const x = x0 + Math.asin(c) + (Math.PI - 2 * Math.asin(c)) * k / N;
        const sx = Math.sin(x - x0);
        const r = clamp(c / sx, -1, 1);
        const yy = Math.asin(r);
        bot.push([x, y0 + yy]); top.push([x, y0 + Math.PI - yy]);
      }
      const ring = bot.concat(top.reverse());
      ring.forEach(([x, y], k) => k ? g.lineTo(px(x, b), py(y, b)) : g.moveTo(px(x, b), py(y, b)));
      g.closePath(); g.stroke();
      void sgn; void xs;
    }
  }
  g.restore();
}
let pressureImg = null;
function buildPressure() {
  const n = 270, off = document.createElement('canvas');
  off.width = off.height = n;
  const c2 = off.getContext('2d'), im = c2.createImageData(n, n);
  const lo = [196, 222, 236], mid = [252, 250, 244], hi = [244, 205, 168];
  for (let j = 0; j < n; j++) for (let i = 0; i < n; i++) {
    const x = (i + 0.5) / n * TAU, y = (1 - (j + 0.5) / n) * TAU;
    const p = 0.5 * (Math.cos(2 * x) + Math.cos(2 * y)); // in [−1, 1]
    const s = Math.abs(p), base = p < 0 ? lo : hi;
    const k = (j * n + i) * 4;
    for (let q = 0; q < 3; q++) im.data[k + q] = lerp(mid[q], base[q], s);
    im.data[k + 3] = 255;
  }
  c2.putImageData(im, 0, 0);
  pressureImg = off;
}

// Exact fields for the tracked particle (full time dependence).
function tgField(t, x, y) {
  const F = tgF(t), [a, b] = tgU(x, y);
  return [F * a, F * b];
}
function tgTerms(t, x, y) {
  const F = tgF(t), [u1, u2] = tgU(x, y);
  const dtu = [-2 * NU_TG * F * u1, -2 * NU_TG * F * u2];
  // (u·∇)u, written out from the derivatives of u (not from the pressure)
  const U1 = F * u1, U2 = F * u2;
  const du1dx = F * Math.cos(x) * Math.cos(y), du1dy = -F * Math.sin(x) * Math.sin(y);
  const du2dx = F * Math.sin(x) * Math.sin(y), du2dy = -F * Math.cos(x) * Math.cos(y);
  const adv = [U1 * du1dx + U2 * du1dy, U1 * du2dx + U2 * du2dy];
  const gp = [-0.5 * Math.sin(2 * x) * F * F, -0.5 * Math.sin(2 * y) * F * F]; // ∇p
  const lap = [-2 * U1, -2 * U2]; // Δu
  return { u: [U1, U2], dtu, adv, mgp: [-gp[0], -gp[1]], visc: [NU_TG * lap[0], NU_TG * lap[1]] };
}
function rk4Field(t, x, y, h) {
  const k1 = tgField(t, x, y);
  const k2 = tgField(t + h / 2, x + h / 2 * k1[0], y + h / 2 * k1[1]);
  const k3 = tgField(t + h / 2, x + h / 2 * k2[0], y + h / 2 * k2[1]);
  const k4 = tgField(t + h, x + h * k3[0], y + h * k3[1]);
  return [x + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), y + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])];
}
const TRACK0 = [Math.PI / 2 - 0.95, Math.PI / 2 + 0.25];
function trackedPath(t, every = 0.04) { // returns final state plus a sampled trace
  const h = 0.004;
  let x = TRACK0[0], y = TRACK0[1], s = 0;
  const trace = [[0, x, y]];
  let next = every;
  while (s < t - 1e-12) {
    const step = Math.min(h, t - s);
    [x, y] = rk4Field(s, x, y, step); s += step;
    if (s >= next - 1e-9) { trace.push([s, x, y]); next += every; }
  }
  return { x, y, trace };
}
function measuredAcceleration(t, x, y) { // central difference of u along the computed path
  const h = 1e-3, sub = 10;
  let [xa, ya] = [x, y], [xb, yb] = [x, y];
  for (let k = 0; k < sub; k++) { [xa, ya] = rk4Field(t + k * h / sub, xa, ya, h / sub); }
  for (let k = 0; k < sub; k++) { [xb, yb] = rk4Field(t - k * h / sub, xb, yb, -h / sub); }
  const ua = tgField(t + h, xa, ya), ub = tgField(t - h, xb, yb);
  return [(ua[0] - ub[0]) / (2 * h), (ua[1] - ub[1]) / (2 * h)];
}

// ---------- sliding layers ----------
const LAY = { nu: 0.25, a0: 0.5 };
const layA = (t, N, a0 = LAY.a0, nu = LAY.nu) => a0 * Math.exp(-nu * N * N * t);
const layX = (x0, y0, t, N, a0 = LAY.a0, nu = LAY.nu) =>
  x0 + a0 / (nu * N * N) * (1 - Math.exp(-nu * N * N * t)) * Math.sin(N * y0);
const wrap = x => ((x % TAU) + TAU) % TAU;

// ---------- chapter bar ----------
const CHAPTERS = [
  ['Motion', ['motion']], ['Measurement', ['measure']], ['Acceleration', ['balance', 'layers']],
  ['Summaries', ['energy', 'grid']], ['The question', ['question']],
  ['Forced breakdown', ['peak', 'residual', 'waves', 'proof']], ['Forced computation', ['compute']],
  ['Standing', ['standing']],
];
function chapterBar(id, alpha) {
  if (alpha <= 0) return;
  const x0 = 150, x1 = 1770, y = 70, n = CHAPTERS.length;
  const cur = CHAPTERS.findIndex(c => c[1].includes(id));
  g.save(); g.globalAlpha *= alpha;
  g.strokeStyle = C.faint; g.lineWidth = 2;
  g.beginPath(); g.moveTo(x0, y); g.lineTo(x1, y); g.stroke();
  for (let i = 0; i < n; i++) {
    const x = lerp(x0, x1, i / (n - 1));
    const on = i === cur, done = i < cur;
    g.fillStyle = on ? C.ink : done ? C.muted : C.faint;
    g.beginPath(); g.arc(x, y, on ? 8 : 5.5, 0, TAU); g.fill();
    text(CHAPTERS[i][0], x, y - 22, { size: 22, font: SANS, align: i === 0 ? 'left' : i === n - 1 ? 'right' : 'center', color: on ? C.ink : C.muted, weight: on ? '600' : '400' });
  }
  if (cur > 0) {
    g.strokeStyle = C.muted; g.lineWidth = 2;
    g.beginPath(); g.moveTo(x0, y); g.lineTo(lerp(x0, x1, cur / (n - 1)), y); g.stroke();
  }
  g.restore();
}

// ---------- panels ----------
function panel(x, y, w, h, alpha = 1) {
  if (alpha <= 0) return;
  g.save(); g.globalAlpha *= alpha;
  g.fillStyle = C.paper; g.strokeStyle = C.faint; g.lineWidth = 2;
  g.beginPath(); g.roundRect(x, y, w, h, 10); g.fill(); g.stroke();
  g.restore();
}
function plotAxes(P, { xl = 't', yl = '', alpha = 1, yticks = [0, 1] } = {}) {
  g.save(); g.globalAlpha *= alpha;
  g.strokeStyle = C.ink; g.lineWidth = 2;
  g.beginPath(); g.moveTo(P.x, P.y); g.lineTo(P.x, P.y + P.h); g.lineTo(P.x + P.w, P.y + P.h); g.stroke();
  for (const v of yticks) {
    const yy = P.y + P.h - v * P.h;
    g.strokeStyle = C.faint; g.lineWidth = 1;
    g.beginPath(); g.moveTo(P.x, yy); g.lineTo(P.x + P.w, yy); g.stroke();
    text(String(v), P.x - 12, yy + 8, { size: 22, font: SANS, align: 'right', color: C.muted });
  }
  text(xl, P.x + P.w + 14, P.y + P.h + 8, { size: 26, italic: true });
  text(yl, P.x, P.y - 18, { size: 24, font: SANS, color: C.muted });
  g.restore();
}
function plotCurve(P, f, tMax, { color = C.blue, width = 4, alpha = 1, upto = tMax, dash = null } = {}) {
  if (alpha <= 0) return;
  g.save(); g.globalAlpha *= alpha;
  g.strokeStyle = color; g.lineWidth = width; g.lineJoin = 'round';
  if (dash) g.setLineDash(dash);
  g.beginPath();
  const n = 240;
  for (let k = 0; k <= n; k++) {
    const t = upto * k / n;
    const X = P.x + t / tMax * P.w, Y = P.y + P.h - f(t) * P.h;
    k ? g.lineTo(X, Y) : g.moveTo(X, Y);
  }
  g.stroke();
  g.fillStyle = color;
  g.beginPath(); g.arc(P.x + upto / tMax * P.w, P.y + P.h - f(upto) * P.h, 7, 0, TAU); g.fill();
  g.restore();
}

// ---------- scenes ----------
// Each scene gets local time τ (seconds from its start) and b(i), the local
// start time of narration beat i.
const S = {};

S.title = (τ, b, D) => {
  // drifting cells behind the title
  const t = 3 + τ * 0.5;
  const B2 = { x: 0, y: -420, s: 1920 };
  g.save(); g.globalAlpha = 0.16 * ramp(τ, 0, 2) * (1 - ramp(τ, D - 1.2, 1.2));
  for (let i = 0; i < TG.nDots; i += 1) {
    const [x, y] = tgPos(i, t);
    g.fillStyle = TG.col[i];
    g.beginPath(); g.arc(px(x, B2), py(y, B2), 5, 0, TAU); g.fill();
  }
  g.restore();
  const out = 1 - ramp(τ, D - 1.0, 0.9);
  const words = ['Motion', 'Measurement', 'Acceleration'].map(tr), size = 80, gap = 130;
  g.font = ` ${size}px ${SERIF}`;
  const ws = words.map(w => g.measureText(w).width);
  let x = 960 - (ws.reduce((a, c) => a + c, 0) + 2 * gap) / 2;
  const w0 = b(0), step = (b(1) - w0 - 0.4) / 3;
  words.forEach((w, i) => {
    const a = ramp(τ, w0 + i * step - 0.1, 0.6) * out;
    text(w, x, 470 + 20 * (1 - a), { size, alpha: a });
    if (i < 2) arrow(x + ws[i] + 28, 445, x + ws[i] + gap - 28, 445, { color: C.muted, width: 3, head: 14, alpha: ramp(τ, w0 + (i + 1) * step - 0.2, 0.5) * out });
    x += ws[i] + gap;
  });
  text('What the equation measures, what was just proved, and what is still open', 960, 585, { size: 38, align: 'center', italic: true, color: C.muted, alpha: ramp(τ, b(1), 1) * out });
  text('A TRANSFORMATICS TEACHING FILM', 960, 690, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: ramp(τ, b(1) + 1.5, 1) * out, weight: '500' });
};

S.motion = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  VIEW = { x0: 0, y0: 0, span: TAU };
  chapterBar('motion', ramp(τ, 0, 0.8));
  drawBox(ramp(τ, 0.2, 0.8), BOX, { marks: ramp(τ, b(0) + 2.0, 0.8) * (1 - ramp(τ, b(2), 1)) });
  // wrap demonstration: a tracer leaving right re-enters left
  const wa = ramp(τ, b(0) + 3.0, 0.4) * (1 - ramp(τ, b(1), 0.6));
  if (wa > 0) {
    const s = clamp((τ - b(0) - 3.0) / 3.5);
    const x = wrap(TAU * (0.62 + 0.75 * s)), y = TAU * 0.78;
    g.save(); g.globalAlpha = wa;
    g.fillStyle = C.ink; g.beginPath(); g.arc(px(x), py(y), 9, 0, TAU); g.fill();
    g.restore();
    text('leaves on the right, re-enters on the left', 555, 1025, { size: 26, align: 'center', italic: true, color: C.muted, alpha: wa });
  }
  const tm = Math.max(0, τ - b(2) - 0.6) * 0.6; // physical time
  drawStreamlines(ramp(τ, b(4), 1.2) * 0.9);
  drawTGDots(tm, ramp(τ, b(1), 1.0) * (1 - 0.55 * ramp(τ, b(3) + 0.2, 0.8)));
  drawBlobs(tm, ramp(τ, b(3) + 0.2, 1.0), ramp(τ, b(3) + 1.0, 0.8) * 0.9);
  // a sparse quiver while the ODE is introduced
  const qa = ramp(τ, b(2), 0.8) * (1 - ramp(τ, b(3), 1.0));
  if (qa > 0) for (let i = 0; i < 12; i++) for (let j = 0; j < 12; j++) {
    const x = (i + 0.5) / 12 * TAU, y = (j + 0.5) / 12 * TAU, [u, v] = tgField(tm, x, y);
    arrow(px(x), py(y), px(x) + u * 38, py(y) - v * 38, { width: 2.5, head: 10, alpha: qa * 0.85 });
  }
  const R = 1080;
  text('A flow moves every particle at once', R, 230, { size: 42, alpha: ramp(τ, b(0), 1) * out });
  text('Periodic box: opposite sides are the same place.', R, 285, { size: 28, color: C.muted, alpha: ramp(τ, b(0) + 0.5, 1) * out });
  text('Colour records each particle’s starting position.', R, 335, { size: 28, color: C.muted, alpha: ramp(τ, b(1), 1) * out });
  eq('ode', R, 430, { anchor: 'l', size: 46, alpha: ramp(τ, b(2) + 1.2, 0.8) * out });
  text('velocity field u, particle position X', R, 495, { size: 26, color: C.muted, alpha: ramp(τ, b(2) + 1.6, 0.8) * out });
  eq('phi', R, 590, { anchor: 'l', size: 46, alpha: ramp(τ, b(3) + 0.8, 0.8) * out });
  text('the flow map is the transformation', R, 650, { size: 26, color: C.muted, alpha: ramp(τ, b(3) + 1.2, 0.8) * out });
  text('Dashed circles: dye at t = 0.  Filled: the same dye now.', R, 692, { size: 26, color: C.muted, alpha: ramp(τ, b(3) + 2.5, 0.8) * out });
  const ea = ramp(τ, b(4), 0.8) * out;
  text('EXACT SOLUTION · TAYLOR–GREEN CELLS', R, 790, { size: 22, font: SANS, weight: '600', color: C.teal, alpha: ea });
  eq('tg_field', R, 845, { anchor: 'l', size: 36, alpha: ea });
  eq('tg_p', R, 910, { anchor: 'l', size: 36, alpha: ramp(τ, b(4) + 0.8, 0.8) * out });
  text(`ν = ${NU_TG}     t = ${tm.toFixed(1)}     amplitude exp(−2νt) = ${tgF(tm).toFixed(3)}`, R, 975, { size: 25, color: C.muted, alpha: ea });
};

// ---- one particle, measured (scenes "measure" and "balance") ----
const MEAS_K = 0.9, VS = 260, AS = 760; // physical time per second; px per unit velocity / acceleration
const SCENE_T0 = { balance: 0 };
function zoomView(z) { VIEW = { x0: 0, y0: 0, span: lerp(TAU, Math.PI, smooth(z)) }; }
function trackedScene(τ, b, id) {
  const tm = id === 'measure' ? Math.max(0, τ - b(0) - 1.0) * MEAS_K : SCENE_T0.balance + τ * MEAS_K;
  const P = trackedPath(tm);
  return { tm, P, terms: tgTerms(tm, P.x, P.y) };
}
function drawTracked(st, { trailA = 1, velA = 1, advA = 0, dtA = 0, sumA = 0 } = {}) {
  const { P, terms } = st;
  g.save(); g.beginPath(); g.rect(BOX.x, BOX.y, BOX.s, BOX.s); g.clip();
  g.globalAlpha = trailA; g.strokeStyle = rgba(C.ink, 0.45); g.lineWidth = 3; g.lineJoin = 'round';
  g.beginPath();
  P.trace.forEach(([, x, y], k) => k ? g.lineTo(px(x), py(y)) : g.moveTo(px(x), py(y)));
  g.lineTo(px(P.x), py(P.y)); g.stroke();
  g.restore();
  const X = px(P.x), Y = py(P.y);
  const acc = [terms.dtu[0] + terms.adv[0], terms.dtu[1] + terms.adv[1]];
  arrow(X, Y, X + terms.u[0] * VS, Y - terms.u[1] * VS, { color: C.blue, width: 7, head: 24, alpha: velA });
  arrow(X, Y, X + terms.adv[0] * AS, Y - terms.adv[1] * AS, { color: C.red, width: 7, head: 22, alpha: advA });
  arrow(X, Y, X + acc[0] * AS, Y - acc[1] * AS, { color: C.ink, width: 3, head: 18, alpha: sumA, dash: [9, 8] });
  arrow(X, Y, X + terms.dtu[0] * AS, Y - terms.dtu[1] * AS, { color: C.gold, width: 8, head: 8, alpha: dtA });
  g.fillStyle = C.ink; g.beginPath(); g.arc(X, Y, 12, 0, TAU); g.fill();
  g.fillStyle = C.paper; g.beginPath(); g.arc(X, Y, 5, 0, TAU); g.fill();
  return { X, Y, acc };
}
function hodograph(st, a, { box = { x: 1110, y: 175, w: 300, h: 300 } } = {}) {
  if (a <= 0) return;
  const cx = box.x + box.w / 2, cy = box.y + box.h / 2, k = 140;
  panel(box.x - 20, box.y - 20, box.w + 40, box.h + 70, a);
  g.save(); g.globalAlpha *= a;
  g.strokeStyle = C.faint; g.lineWidth = 1.5;
  g.beginPath(); g.moveTo(box.x, cy); g.lineTo(box.x + box.w, cy); g.moveTo(cx, box.y); g.lineTo(cx, box.y + box.h); g.stroke();
  g.strokeStyle = rgba(C.blue, 0.55); g.lineWidth = 3;
  g.beginPath();
  st.P.trace.forEach(([t, x, y], i) => {
    const [u, v] = tgField(t, x, y);
    i ? g.lineTo(cx + u * k, cy - v * k) : g.moveTo(cx + u * k, cy - v * k);
  });
  g.stroke();
  g.restore();
  const [u, v] = st.terms.u;
  arrow(cx, cy, cx + u * k, cy - v * k, { color: C.blue, width: 5, head: 18, alpha: a });
  text('velocity the particle records', box.x + box.w / 2, box.y + box.h + 38, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: a });
  text('u₁', box.x + box.w - 4, cy - 10, { size: 22, italic: true, align: 'right', color: C.muted, alpha: a });
  text('u₂', cx + 10, box.y + 18, { size: 22, italic: true, color: C.muted, alpha: a });
}

S.measure = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  zoomView(ramp(τ, 0.2, 2.2));
  chapterBar('measure', 1);
  drawBox(1);
  drawStreamlines(1 - 0.35 * ramp(τ, b(0), 1));
  drawTGDots(0, 0.3 * (1 - ramp(τ, 0, 1.2)));
  const st = trackedScene(τ, b, 'measure');
  const vis = ramp(τ, b(0) + 0.4, 0.8);
  const { X, Y } = drawTracked(st, { trailA: vis, velA: vis, advA: ramp(τ, b(4), 0.8), dtA: ramp(τ, b(3), 0.8), sumA: ramp(τ, b(5), 0.8) });
  const ring = ramp(τ, b(3), 0.6) * (1 - ramp(τ, b(4) + 1, 1));
  if (ring > 0) {
    g.save(); g.globalAlpha = ring; g.strokeStyle = C.gold; g.lineWidth = 3;
    g.beginPath(); g.arc(X, Y, 34, 0, TAU); g.stroke(); g.restore();
    text('∂ₜu, drawn to scale', X + 44, Y + 64, { size: 24, font: SANS, color: C.gold, weight: '600', alpha: ring });
  }
  if (vis > 0) text('one cell of the box, enlarged', BOX.x, BOX.y + BOX.s + 48, { size: 24, font: SANS, color: C.muted, alpha: vis * out });
  hodograph(st, ramp(τ, b(1), 1) * out);
  const R = 1490;
  text('Its velocity keeps turning:', R, 225, { size: 30, alpha: ramp(τ, b(1) + 1, 1) * out });
  text('the particle accelerates.', R, 266, { size: 30, alpha: ramp(τ, b(1) + 1.5, 1) * out });
  text('Meanwhile the field’s', R, 340, { size: 26, color: C.muted, alpha: ramp(τ, b(1) + 3, 1) * out });
  text('pattern only fades:', R, 374, { size: 26, color: C.muted, alpha: ramp(τ, b(1) + 3, 1) * out });
  text(`exp(−2νt) = ${tgF(st.tm).toFixed(3)}`, R, 410, { size: 26, color: C.muted, alpha: ramp(τ, b(1) + 3, 1) * out });
  text('chain rule along X(t)', 1460, 580, { size: 24, font: SANS, align: 'center', color: C.muted, alpha: ramp(τ, b(2) + 0.6, 0.8) * out });
  eq('chain', 1460, 645, { size: 52, alpha: ramp(τ, b(2) + 0.3, 0.8) * out });
  text('∂ₜu   change at one fixed point', 1130, 730, { size: 25, font: SANS, color: C.gold, weight: '600', alpha: ramp(τ, b(3), 0.8) * out });
  text('(u·∇)u   moving to where velocity differs: advection', 1130, 768, { size: 25, font: SANS, color: C.red, weight: '600', alpha: ramp(τ, b(4), 0.8) * out });
  text('dashed   their sum, the acceleration', 1130, 806, { size: 25, font: SANS, color: C.ink, weight: '600', alpha: ramp(τ, b(5), 0.8) * out });
  const ca = ramp(τ, b(5) + 0.2, 0.8) * out;
  if (ca > 0) {
    const m = measuredAcceleration(st.tm, st.P.x, st.P.y);
    const f = [st.terms.dtu[0] + st.terms.adv[0], st.terms.dtu[1] + st.terms.adv[1]];
    panel(1100, 840, 720, 170, ca);
    text('LIVE CHECK', 1130, 878, { size: 20, font: SANS, weight: '600', color: C.muted, alpha: ca });
    text(`velocity change measured along the path   (${fx(m[0], 4)}, ${fx(m[1], 4)})`, 1130, 920, { size: 23, font: SANS, alpha: ca });
    text(`∂ₜu + (u·∇)u from the formula                   (${fx(f[0], 4)}, ${fx(f[1], 4)})`, 1130, 958, { size: 23, font: SANS, alpha: ca });
    text(`difference ${sci(Math.hypot(m[0] - f[0], m[1] - f[1]))}  (finite-difference error)`, 1130, 993, { size: 21, font: SANS, color: C.muted, alpha: ca });
  }
};

S.balance = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  zoomView(1);
  chapterBar('balance', 1);
  drawBox(1);
  const pa = ramp(τ, b(1), 1.2);
  if (pa > 0) {
    const n = pressureImg.width, sw = n * VIEW.span / TAU;
    g.save(); g.globalAlpha = pa;
    g.drawImage(pressureImg, 0, n - sw, sw, sw, BOX.x, BOX.y, BOX.s, BOX.s);
    g.restore();
    const la = pa * (1 - ramp(τ, b(2) + 3, 1));
    for (const [x, y] of [[0, 0], [Math.PI, 0], [0, Math.PI], [Math.PI, Math.PI]])
      text('high p', clamp(px(x), BOX.x + 70, BOX.x + BOX.s - 70), clamp(py(y), BOX.y + 45, BOX.y + BOX.s - 25), { size: 26, font: SANS, weight: '600', color: '#9a5a22', align: 'center', alpha: la });
    text('low p', px(Math.PI / 2), py(Math.PI / 2) + 9, { size: 26, font: SANS, weight: '600', color: '#2c6683', align: 'center', alpha: la });
  }
  drawStreamlines(0.6);
  const st = trackedScene(τ, b, 'balance');
  const { X, Y } = drawTracked(st, { trailA: 1, velA: 1 - 0.65 * ramp(τ, b(2), 1), advA: 1, dtA: 1, sumA: 1 });
  const T = st.terms;
  const ga = ramp(τ, b(2), 0.8);
  if (ga > 0) { // −∇p laid over (u·∇)u
    g.save(); g.strokeStyle = C.purple; g.lineWidth = 20; g.lineCap = 'round'; g.globalAlpha = 0.3 * ga;
    g.beginPath(); g.moveTo(X, Y); g.lineTo(X + T.mgp[0] * AS, Y - T.mgp[1] * AS); g.stroke(); g.restore();
  }
  const va = ramp(τ, b(3), 0.8);
  if (va > 0) { // νΔu laid over ∂ₜu
    g.save(); g.strokeStyle = C.teal; g.lineWidth = 22; g.lineCap = 'round'; g.globalAlpha = 0.4 * va;
    g.beginPath(); g.moveTo(X, Y); g.lineTo(X + T.visc[0] * AS, Y - T.visc[1] * AS); g.stroke(); g.restore();
  }
  const R = 1060;
  text('What causes the acceleration?', R, 220, { size: 40, alpha: ramp(τ, b(0), 1) * out });
  eq('ns', 1450, 345, { size: 50, alpha: ramp(τ, b(0) + 0.8, 1) * out });
  const pl = ramp(τ, b(1), 1) * out;
  text('Pressure: high where streams meet between cells,', R, 490, { size: 27, color: C.muted, alpha: pl });
  text('low at the cell centres.', R, 526, { size: 27, color: C.muted, alpha: pl });
  eq('match1', R, 605, { anchor: 'l', size: 34, alpha: ramp(τ, b(2), 0.8) * out });
  text('the pressure force bends the path around the cell', R, 660, { size: 25, font: SANS, color: C.purple, alpha: ramp(τ, b(2) + 0.8, 0.8) * out });
  eq('match2', R, 735, { anchor: 'l', size: 36, alpha: ramp(τ, b(3), 0.8) * out });
  text(`viscosity accounts for the slow fade (size here ${Math.hypot(...T.visc).toFixed(4)})`, R, 790, { size: 25, font: SANS, color: C.teal, alpha: ramp(τ, b(3) + 0.8, 0.8) * out });
  const ca = ramp(τ, b(4) + 0.5, 0.8) * out;
  if (ca > 0) {
    const r = Math.hypot(T.dtu[0] + T.adv[0] - T.mgp[0] - T.visc[0], T.dtu[1] + T.adv[1] - T.mgp[1] - T.visc[1]);
    panel(R, 845, 760, 130, ca);
    text('LIVE CHECK AT THE PARTICLE', R + 30, 885, { size: 20, font: SANS, weight: '600', color: C.muted, alpha: ca });
    text(`| acceleration − (−∇p + νΔu) | = ${r === 0 ? '0' : sci(r)}   (rounding)`, R + 30, 935, { size: 26, alpha: ca });
  }
};

S.layers = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('layers', 1);
  drawBox(1);
  const tm = Math.max(0, τ - b(0) - 3.0) * 0.6, N = 1;
  const a = layA(tm, N);
  const ia = ramp(τ, 0.2, 1.0);
  // particles in rows; colour bands by layer
  g.save(); g.beginPath(); g.rect(BOX.x, BOX.y, BOX.s, BOX.s); g.clip();
  g.globalAlpha = ia;
  const rows = 30, cols = 34;
  for (let j = 0; j < rows; j++) {
    const y = (j + 0.5) / rows * TAU, s = Math.sin(N * y);
    g.fillStyle = s >= 0 ? `hsl(220,55%,${62 - 22 * s}%)` : `hsl(14,60%,${62 + 22 * s}%)`;
    for (let i = 0; i < cols; i++) {
      const x = wrap(layX((i + 0.5) / cols * TAU, y, tm, N));
      g.beginPath(); g.arc(px(x), py(y), 4.4, 0, TAU); g.fill();
    }
  }
  // dye lines
  const da = ramp(τ, b(3) - 0.5, 1.0);
  g.globalAlpha = Math.max(ia * 0.0, da);
  g.strokeStyle = C.ink; g.lineWidth = 4;
  for (const x0 of [TAU * 0.25, TAU * 0.75]) {
    for (const off of [-TAU, 0, TAU]) {
      g.beginPath();
      for (let k = 0; k <= 200; k++) {
        const y = k / 200 * TAU, x = layX(x0, y, tm, N) + off;
        k ? g.lineTo(px(x), py(y)) : g.moveTo(px(x), py(y));
      }
      g.stroke();
    }
  }
  g.restore();
  // velocity profile arrows on the left edge
  const qa = ramp(τ, b(0) + 0.8, 0.8);
  profileArrows(px(Math.PI), j => py(j), y => a * Math.sin(N * y) * 300, 15, qa);
  // highlighted particle on one layer
  const ha = ramp(τ, b(1), 0.8) * (1 - ramp(τ, b(3), 0.8));
  if (ha > 0) {
    const y0 = TAU * 0.3, x = wrap(layX(TAU * 0.1, y0, tm, N));
    g.save(); g.globalAlpha = ha; g.strokeStyle = C.ink; g.setLineDash([6, 8]); g.lineWidth = 2;
    g.beginPath(); g.moveTo(px(0), py(y0)); g.lineTo(px(TAU), py(y0)); g.stroke(); g.restore();
    g.save(); g.globalAlpha = ha; g.fillStyle = C.ink; g.beginPath(); g.arc(px(x), py(y0), 11, 0, TAU); g.fill(); g.restore();
    arrow(px(x), py(y0), px(x) + a * Math.sin(y0) * 300, py(y0), { color: C.blue, width: 6, head: 20, alpha: ha });
    g.save(); g.globalAlpha = ha * 0.92; g.fillStyle = C.paper; g.fillRect(px(TAU / 2) - 200, py(y0) - 52, 400, 40); g.restore();
    text('same speed all along its layer', px(TAU / 2), py(y0) - 22, { size: 24, font: SANS, align: 'center', alpha: ha, weight: '600' });
  }
  const R = 1060;
  text('Sliding layers', R, 220, { size: 40, alpha: ramp(τ, b(0), 1) * out });
  eq('lay_u', R, 300, { anchor: 'l', size: 44, alpha: ramp(τ, b(0) + 0.6, 0.8) * out });
  eq('lay_adv', R, 385, { anchor: 'l', size: 36, alpha: ramp(τ, b(1) + 0.6, 0.8) * out });
  text('advection vanishes; no pressure is needed', R, 440, { size: 25, font: SANS, color: C.red, alpha: ramp(τ, b(1) + 1.4, 0.8) * out });
  eq('lay_ode', R, 515, { anchor: 'l', size: 36, alpha: ramp(τ, b(2) + 0.4, 0.8) * out });
  eq('lay_X', R, 605, { anchor: 'l', size: 33, alpha: ramp(τ, b(3) + 0.3, 0.8) * out });
  // amplitude plot
  const P = { x: 1130, y: 700, w: 560, h: 230 };
  const pA = ramp(τ, b(2) + 1.0, 0.8) * out, tMax = 14;
  if (pA > 0) {
    plotAxes(P, { yl: 'a(t) / a(0)', alpha: pA });
    const upto = clamp(tm, 0, tMax);
    plotCurve(P, t => Math.exp(-LAY.nu * t), tMax, { color: C.blue, upto, alpha: pA });
    text('N = 1:  exp(−νt)', P.x + P.w - 10, P.y + 40, { size: 26, align: 'right', color: C.blue, alpha: pA });
    const a2 = ramp(τ, b(4), 0.8) * out;
    plotCurve(P, t => Math.exp(-4 * LAY.nu * t), tMax, { color: C.red, upto: clamp((τ - b(4)) * 2.2, 0, tMax), alpha: a2 });
    text('N = 2:  exp(−4νt),  four times the rate', P.x + P.w - 10, P.y + 80, { size: 26, align: 'right', color: C.red, alpha: a2 });
  }
  text(`N = 1     ν = ${LAY.nu}     t = ${tm.toFixed(1)}     a(t)/a(0) = ${(a / LAY.a0).toFixed(3)}`, BOX.x, BOX.y + BOX.s + 50, { size: 25, color: C.muted, alpha: ia * out });
};

function profileArrows(x0, Y, len, n, alpha) { // u₁(y) drawn from a vertical axis
  if (alpha <= 0) return;
  g.save(); g.globalAlpha = alpha * 0.7; g.strokeStyle = C.ink; g.lineWidth = 2; g.setLineDash([5, 6]);
  g.beginPath(); g.moveTo(x0, Y(0)); g.lineTo(x0, Y(TAU)); g.stroke(); g.restore();
  for (let j = 0; j < n; j++) {
    const y = (j + 0.5) / n * TAU, L = len(y);
    arrow(x0, Y(y), x0 + L, Y(y), { color: '#ffffff', width: 10, head: 20, alpha: alpha * 0.9 });
    arrow(x0, Y(y), x0 + L, Y(y), { color: C.ink, width: 4, head: 15, alpha });
  }
}
function layerStrip(B, N, tm, alpha) {
  drawBox(alpha, B);
  if (alpha <= 0) return;
  const h = B.h;
  g.save(); g.globalAlpha *= alpha;
  g.beginPath(); g.rect(B.x, B.y + B.s - h, B.s, h); g.clip();
  const rows = 22, cols = 40;
  for (let j = 0; j < rows; j++) {
    const y = (j + 0.5) / rows * TAU, s = Math.sin(N * y);
    g.fillStyle = s >= 0 ? `hsl(220,55%,${62 - 22 * s}%)` : `hsl(14,60%,${62 + 22 * s}%)`;
    for (let i = 0; i < cols; i++) {
      const x = wrap(layX((i + 0.5) / cols * TAU, y, tm, N, 0.5, ENERGY_NU));
      g.beginPath(); g.arc(px(x, B), py(y, B), 3.6, 0, TAU); g.fill();
    }
  }
  g.restore();
  profileArrows(B.x + B.s / 2, y => py(y, B), y => layA(tm, N, 0.5, ENERGY_NU) * Math.sin(N * y) * 300, 12, alpha);
}
const ENERGY_NU = 0.06;

S.energy = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('energy', 1);
  const tm = Math.max(0, τ - b(2) - 0.3) * 0.75;
  const B1 = { x: 150, y: 175, s: 760, h: 340 }, B2 = { x: 150, y: 600, s: 760, h: 340 };
  // B.y + B.s - h is the top edge; set so the strips sit where intended
  B1.y = 175 + 340 - 760; B2.y = 615 + 340 - 760;
  const sa = ramp(τ, b(1), 0.9);
  layerStrip(B1, 1, tm, sa);
  layerStrip(B2, 2, tm, ramp(τ, b(1) + 1.2, 0.9));
  text('N = 1', 150, 165, { size: 26, font: SANS, weight: '600', color: C.blue, alpha: sa * out });
  text('N = 2', 150, 605, { size: 26, font: SANS, weight: '600', color: C.red, alpha: ramp(τ, b(1) + 1.2, 0.9) * out });
  const R = 1010;
  text('Keep one number', R, 210, { size: 40, alpha: ramp(τ, b(0), 1) * out });
  eq('en_def', R, 290, { anchor: 'l', size: 42, alpha: ramp(τ, b(0) + 1.0, 0.8) * out });
  eq('en_val', R, 370, { anchor: 'l', size: 36, alpha: ramp(τ, b(1) + 2.6, 0.8) * out });
  // energy meters
  const ma = ramp(τ, b(1) + 2.0, 0.8) * out;
  const e1 = Math.exp(-2 * ENERGY_NU * tm), e2 = Math.exp(-8 * ENERGY_NU * tm);
  if (ma > 0) {
    const mx = 1560, my = 430, mh = 250, mw = 70;
    for (const [k, e, c, lab] of [[0, e1, C.blue, 'N = 1'], [1, e2, C.red, 'N = 2']]) {
      const x = mx + k * 130;
      g.save(); g.globalAlpha = ma;
      g.strokeStyle = C.ink; g.lineWidth = 2; g.strokeRect(x, my, mw, mh);
      g.fillStyle = rgba(c, 0.85); g.fillRect(x, my + mh * (1 - e), mw, mh * e);
      g.restore();
      text(lab, x + mw / 2, my + mh + 34, { size: 22, font: SANS, align: 'center', color: c, weight: '600', alpha: ma });
      text(e.toFixed(3), x + mw / 2, my - 14, { size: 22, font: SANS, align: 'center', alpha: ma });
    }
    text('E(t) / E(0)', mx + 100, my - 52, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: ma });
  }
  const P = { x: 1060, y: 450, w: 400, h: 230 };
  const pa = ramp(τ, b(2), 0.8) * out, tMax = 18;
  if (pa > 0) {
    plotAxes(P, { yl: 'E(t) / E(0)', alpha: pa });
    const upto = clamp(tm, 0, tMax);
    plotCurve(P, t => Math.exp(-2 * ENERGY_NU * t), tMax, { color: C.blue, upto, alpha: pa });
    plotCurve(P, t => Math.exp(-8 * ENERGY_NU * t), tMax, { color: C.red, upto, alpha: pa });
    text('exp(−2νt)  N = 1', P.x + P.w - 6, P.y + 70, { size: 26, align: 'right', color: C.blue, alpha: pa });
    text('exp(−8νt)  N = 2', P.x + 120, P.y + P.h - 26, { size: 26, color: C.red, alpha: pa });
    eq('en_t', R, 770, { anchor: 'l', size: 34, alpha: ramp(τ, b(2) + 1.5, 0.8) * out * (1 - ramp(τ, b(4), 0.6)) });
  }
  const fa = ramp(τ, b(3), 0.7) * out * (1 - ramp(τ, b(4), 0.6));
  text('Equal energy at t = 0; unequal energy later.', R, 860, { size: 34, alpha: fa });
  const ia = ramp(τ, b(4), 0.8) * out;
  eq('en_id', R, 790, { anchor: 'l', size: 40, alpha: ia });
  text('Dissipation depends on the gradient; E alone does not record it.', R, 870, { size: 26, color: C.muted, alpha: ramp(τ, b(4) + 1.5, 0.8) * out });
  text(`same amplitude a(0) = 0.5     ν = ${ENERGY_NU}     t = ${tm.toFixed(1)}`, 150, 1010, { size: 25, color: C.muted, alpha: sa * out });
};

S.grid = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('grid', 1);
  const P = { x: 200, y: 230, w: 1100, h: 420 };
  const cy = P.y + P.h / 2, ky = P.h / 2 * 0.85;
  const X = y => P.x + y / TAU * P.w, Y = v => cy - v * ky;
  const NU = 0.02;
  const tm = Math.max(0, τ - b(2) - 0.5) * 1.1;
  const fa = Math.exp(-NU * tm), fb = Math.exp(-49 * NU * tm);
  const aa = ramp(τ, 0.2, 0.8);
  g.save(); g.globalAlpha = aa;
  g.strokeStyle = C.ink; g.lineWidth = 2;
  g.beginPath(); g.moveTo(P.x, cy); g.lineTo(P.x + P.w, cy); g.stroke();
  g.restore();
  text('y', P.x + P.w + 20, cy + 9, { size: 30, italic: true, alpha: aa });
  text('2π', X(TAU), cy + 40, { size: 24, align: 'center', color: C.muted, alpha: aa });
  text('0', X(0), cy + 40, { size: 24, align: 'center', color: C.muted, alpha: aa });
  text('velocity u₁ across the layers', P.x, P.y - 10, { size: 24, font: SANS, color: C.muted, alpha: aa });
  // grid lines + samples
  const ga = ramp(τ, b(0) + 1.5, 0.8);
  for (let j = 0; j < 8; j++) {
    const y = TAU * j / 8;
    g.save(); g.globalAlpha = ga * 0.6; g.strokeStyle = C.faint; g.lineWidth = 2;
    g.beginPath(); g.moveTo(X(y), P.y); g.lineTo(X(y), P.y + P.h); g.stroke(); g.restore();
  }
  const curve = (f, color, upto, alpha, w = 5) => {
    if (alpha <= 0) return;
    g.save(); g.globalAlpha = alpha; g.strokeStyle = color; g.lineWidth = w; g.lineJoin = 'round';
    g.beginPath();
    const n = 700;
    for (let k = 0; k <= n * upto; k++) { const y = TAU * k / n; k ? g.lineTo(X(y), Y(f(y))) : g.moveTo(X(y), Y(f(y))); }
    g.stroke(); g.restore();
  };
  const ba = ramp(τ, b(1), 0.5), ra = ramp(τ, b(1) + 3.0, 0.5);
  curve(y => fa * Math.sin(y), C.blue, ramp(τ, b(1), 2.2), ba);
  curve(y => -fb * Math.sin(7 * y), C.red, ramp(τ, b(1) + 3.0, 2.6), ra, 3.5);
  // samples
  const split = ramp(τ, b(2) + 0.5, 0.6);
  for (let j = 0; j < 8; j++) {
    const y = TAU * j / 8, va = fa * Math.sin(y), vb = -fb * Math.sin(7 * y);
    const pulse = 1 + 0.5 * Math.max(0, Math.sin((τ - b(1) - 6) * 4)) * ramp(τ, b(1) + 5.8, 0.3) * (1 - ramp(τ, b(2), 0.5));
    g.save(); g.globalAlpha = ga;
    if (split < 0.01) {
      g.fillStyle = C.ink; g.beginPath(); g.arc(X(y), Y(va), 10 * pulse, 0, TAU); g.fill();
    } else {
      g.lineWidth = 4;
      g.strokeStyle = C.blue; g.fillStyle = C.paper; g.beginPath(); g.arc(X(y), Y(va), 10, 0, TAU); g.fill(); g.stroke();
      g.strokeStyle = C.red; g.beginPath(); g.arc(X(y), Y(vb), 10, 0, TAU); g.fill(); g.stroke();
    }
    g.restore();
  }
  // table of the eight numbers
  const ta = ramp(τ, b(1) + 5, 0.8) * out;
  if (ta > 0) {
    const tx = 200, ty = 745, cw = 120;
    panel(tx - 30, ty - 55, 8 * cw + 290, 180, ta);
    text('j', tx, ty, { size: 24, italic: true, color: C.muted, alpha: ta });
    text('sin yⱼ', tx, ty + 45, { size: 24, font: SANS, color: C.blue, weight: '600', alpha: ta });
    text('−sin 7yⱼ', tx, ty + 90, { size: 24, font: SANS, color: C.red, weight: '600', alpha: ta });
    for (let j = 0; j < 8; j++) {
      const y = TAU * j / 8, x = tx + 190 + j * cw;
      const v1 = Math.sin(y) * fa, v2 = -Math.sin(7 * y) * fb;
      const z = v => (Math.abs(v) < 5e-4 ? 0 : v);
      text(String(j), x, ty, { size: 24, font: SANS, align: 'right', color: C.muted, alpha: ta });
      text(z(v1).toFixed(3), x, ty + 45, { size: 24, font: SANS, align: 'right', alpha: ta });
      text(z(v2).toFixed(3), x, ty + 90, { size: 24, font: SANS, align: 'right', alpha: ta });
    }
  }
  const R = 1400;
  text('A grid of eight values', R, 250, { size: 36, alpha: ramp(τ, b(0), 1) * out });
  eq('gr_pts', R, 320, { anchor: 'l', size: 32, alpha: ramp(τ, b(0) + 1.5, 0.8) * out });
  eq('gr_alias', R, 395, { anchor: 'l', size: 30, alpha: ramp(τ, b(1) + 5.5, 0.8) * out });
  eq('gr_decay1', R, 470, { anchor: 'l', size: 32, alpha: ramp(τ, b(2), 0.8) * out });
  eq('gr_decay2', R, 520, { anchor: 'l', size: 32, alpha: ramp(τ, b(2) + 0.6, 0.8) * out });
  text(`ν = ${NU}     t = ${tm.toFixed(1)}`, R, 585, { size: 25, color: C.muted, alpha: ramp(τ, b(2), 0.8) * out });
  text('The eight values cannot', R, 660, { size: 32, italic: true, alpha: ramp(τ, b(3) + 2.5, 0.8) * out });
  text('distinguish the two waves.', R, 702, { size: 32, italic: true, alpha: ramp(τ, b(3) + 3.2, 0.8) * out });
};

S.question = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('question', 1 - ramp(τ, D - 0.9, 0.8));
  // commutative square
  const L = 330, Rx = 830, T = 260, Bt = 560;
  const da = ramp(τ, b(0), 0.8) * out;
  eq('q_x', L, T, { size: 48, alpha: da });
  eq('q_xt', Rx, T, { size: 48, alpha: ramp(τ, b(0) + 1.0, 0.8) * da / Math.max(da, 1e-9) * da });
  arrow(L + 50, T, Rx - 80, T, { width: 3, alpha: ramp(τ, b(0) + 0.6, 0.8) * da });
  eq('q_phi', (L + Rx) / 2, T - 38, { size: 36, alpha: ramp(τ, b(0) + 0.6, 0.8) * da });
  const ra = ramp(τ, b(0) + 2.5, 0.8) * da;
  arrow(L, T + 40, L, Bt - 40, { width: 3, alpha: ra });
  arrow(Rx, T + 40, Rx, Bt - 40, { width: 3, alpha: ra });
  eq('q_R1', L - 30, (T + Bt) / 2, { size: 36, alpha: ra });
  eq('q_R2', Rx + 30, (T + Bt) / 2, { size: 36, alpha: ra });
  eq('q_r', L, Bt, { size: 44, alpha: ra });
  eq('q_rt', Rx, Bt, { size: 44, alpha: ra });
  const sa = ramp(τ, b(1), 0.8) * da;
  arrow(L + 90, Bt, Rx - 120, Bt, { width: 3, alpha: sa, dash: [10, 9], color: C.muted });
  eq('q_S', (L + Rx) / 2, Bt - 36, { size: 40, alpha: sa });
  text('state', L, T - 70, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: da });
  text('summary', L, Bt + 60, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: ra });
  eq('q_crit', 580, 700, { size: 40, alpha: ramp(τ, b(1) + 3.0, 0.8) * da });
  text('the factor criterion: States, models, and exact transfer, §3', 580, 765, { size: 24, font: SANS, align: 'center', color: C.muted, alpha: ramp(τ, b(1) + 4.0, 0.8) * da });
  // test results
  const tx = 1090, rows = [
    ['Energy E', 'fails', 'N = 1 and N = 2 share E(0), not E(t)', C.red],
    ['Eight grid values', 'fails', 'N = 1 and N = 7 share samples, not futures', C.red],
    ['Energy and wavenumber (E, N)', 'passes', 'E(t) = E(0) exp(−2νN²t) for sliding layers', C.teal],
    ['Eight grid values, N ≤ 3 only', 'passes', 'the samples determine a and N', C.teal],
  ];
  rows.forEach(([name, verdict, why, col], i) => {
    const a = ramp(τ, b(2) + [0, 1.2, 3.6, 5.2][i], 0.7) * da;
    const y = 300 + i * 120;
    text(name, tx, y, { size: 30, alpha: a });
    text(verdict.toUpperCase(), 1820, y, { size: 22, font: SANS, align: 'right', color: col, weight: '700', alpha: a });
    text(why, tx, y + 40, { size: 25, color: C.muted, alpha: a });
  });
  // hand-off to part two
  const ha = ramp(τ, b(3), 1.0) * out;
  text('Next: two results, read with this test in mind.', 960, 1000, { size: 34, align: 'center', alpha: ha });
};

S.credits = (τ, b, D) => {
  const a = ramp(τ, 0.3, 1.0) * (1 - ramp(τ, D - 1.6, 1.4));
  text('Transformatics', 960, 330, { size: 64, align: 'center', alpha: a });
  text('Finite change, continuous evolution, and the passage between mathematical models', 960, 390, { size: 28, align: 'center', italic: true, color: C.muted, alpha: a });
  text('github.com/hmbown/transformatics', 960, 470, { size: 30, font: SANS, align: 'center', color: C.blue, alpha: a });
  const lines = [
    'Written and illustrated by Hunter Bown. Transformatics is his proposed way of organizing these ideas.',
    'Sources: OpenAI, “Finite time blowup for Navier–Stokes” (2026); openai/math family 376 (6 Oct 2026).',
    'Narration: Microsoft synthetic voices.',
  ];
  lines.forEach((s, i) => text(s, 960, 590 + i * 46, { size: 25, font: SANS, align: 'center', color: C.muted, alpha: a * ramp(τ, 0.8 + i * 0.4, 0.8) }));
};

// ================= Part two: the published results =================
// Shared helpers for the new scenes.
function source(s, alpha) { text(s, 150, 1040, { size: 21, font: SANS, color: C.muted, alpha }); }
function tag(s, x, y, color, alpha, align = 'left') {
  if (alpha <= 0) return;
  s = tr(s);
  g.save(); g.globalAlpha *= alpha;
  g.font = `700 19px ${SANS}`;
  const w = g.measureText(s).width + 24, x0 = align === 'right' ? x - w : x;
  g.fillStyle = rgba(color, 0.12); g.strokeStyle = color; g.lineWidth = 1.5;
  g.beginPath(); g.roundRect(x0, y - 22, w, 32, 6); g.fill(); g.stroke();
  g.fillStyle = color; g.textBaseline = 'middle'; g.textAlign = 'left';
  g.fillText(s, x0 + 12, y - 5);
  g.restore();
}
function wrapText(s, x, y, maxW, opts = {}) { // greedy word wrap; returns next y
  const size = opts.size ?? 30, lh = opts.lh ?? size * 1.32;
  g.save(); g.font = `${opts.italic ? 'italic ' : ''}${opts.weight ?? ''} ${size}px ${opts.font ?? SERIF}`;
  s = tr(s);
  const cjk = /[\u3400-\u9fff]/.test(s);
  const words = cjk ? s.match(/[A-Za-z0-9._]+|[^\s]/g) : s.split(' '); let line = '';
  const lines = [];
  for (const w of words) { const t = line ? line + (cjk ? '' : ' ') + w : w; if (g.measureText(t).width > maxW && line) { lines.push(line); line = w; } else line = t; }
  if (line) lines.push(line);
  g.restore();
  lines.forEach((l, i) => text(l, x, y + i * lh, opts));
  return y + lines.length * lh;
}
// log–log axes: P = {x, y, w, h}, x in log10 τ from lx0 to lx1 (drawn left to right), y in log10 from ly0 to ly1
function logAxes(P, lx0, lx1, ly0, ly1, alpha, { xl = 'time remaining τ', yticks = [], xticks = [] } = {}) {
  if (alpha <= 0) return;
  g.save(); g.globalAlpha *= alpha;
  g.strokeStyle = C.ink; g.lineWidth = 2;
  g.beginPath(); g.moveTo(P.x, P.y); g.lineTo(P.x, P.y + P.h); g.lineTo(P.x + P.w, P.y + P.h); g.stroke();
  for (const [v, lab] of yticks) {
    const yy = P.y + P.h - (v - ly0) / (ly1 - ly0) * P.h;
    g.strokeStyle = C.faint; g.lineWidth = 1; g.beginPath(); g.moveTo(P.x, yy); g.lineTo(P.x + P.w, yy); g.stroke();
    text(lab, P.x - 12, yy + 8, { size: 21, font: SANS, align: 'right', color: C.muted });
  }
  for (const [v, lab] of xticks) {
    const xx = P.x + (v - lx0) / (lx1 - lx0) * P.w;
    text(lab, xx, P.y + P.h + 30, { size: 21, font: SANS, align: 'center', color: C.muted });
  }
  text(xl, P.x + P.w, P.y + P.h + 62, { size: 22, font: SANS, align: 'right', color: C.muted });
  g.restore();
}
function logCurve(P, lx0, lx1, ly0, ly1, f, upto, { color, width = 4, alpha = 1, dash = null, dot = true } = {}) {
  if (alpha <= 0) return;
  const X = l => P.x + (l - lx0) / (lx1 - lx0) * P.w, Y = l => P.y + P.h - (l - ly0) / (ly1 - ly0) * P.h;
  g.save(); g.globalAlpha *= alpha; g.strokeStyle = color; g.lineWidth = width; g.lineJoin = 'round';
  g.beginPath(); g.rect(P.x, P.y - 4, P.w + 8, P.h + 8); g.clip();
  if (dash) g.setLineDash(dash);
  g.beginPath();
  const n = 200;
  for (let k = 0; k <= n; k++) { const l = lx0 + (upto - lx0) * k / n; const yy = Y(f(l)); k ? g.lineTo(X(l), yy) : g.moveTo(X(l), yy); }
  g.stroke(); g.setLineDash([]);
  if (dot) { g.fillStyle = color; g.beginPath(); g.arc(X(upto), Y(f(upto)), 7, 0, TAU); g.fill(); }
  g.restore();
}


// ---- about: what Transformatics is ----
S.about = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  text('What is Transformatics?', 150, 200, { size: 48, alpha: ramp(τ, b(0), 1) * out });
  wrapText('A way of thinking I put together while working on Navier–Stokes with AI tools.', 150, 262, 1400, { size: 30, italic: true, color: C.muted, alpha: ramp(τ, b(0) + 2, 1) * out });
  // the triple
  const cards = [['STATE', 'x ∈ X', 'what the system is'], ['TRANSFORMATION', 'T : X → X', 'how it is updated'], ['OBSERVABLE', 'f : X → ℝ', 'what we measure']];
  const ta = 1 - ramp(τ, b(4), 0.8);
  cards.forEach(([h, m, d2], i) => {
    const a = ramp(τ, b(1) + 0.8 + i * 1.6, 0.7) * out * ta, x = 150 + i * 560;
    panel(x, 340, 500, 160, a);
    text(h, x + 24, 382, { size: 19, font: SANS, weight: '700', color: [C.blue, C.purple, C.teal][i], alpha: a });
    text(m, x + 24, 438, { size: 36, alpha: a });
    text(d2, x + 24, 478, { size: 22, font: SANS, color: C.muted, alpha: a });
  });
  // the smallest example: ±2 under x ↦ x + 1, measured by x²
  const ea = ramp(τ, b(2) + 4, 0.8) * out * ta;
  if (ea > 0) {
    eq('ab_ex', 560, 580, { size: 34, alpha: ea });
    const X = v => 200 + (v + 4) / 8 * 720, y0 = 700;
    g.save(); g.globalAlpha = ea; g.strokeStyle = C.ink; g.lineWidth = 2; g.beginPath(); g.moveTo(X(-4), y0); g.lineTo(X(4), y0); g.stroke(); g.restore();
    for (let v = -4; v <= 4; v++) { g.save(); g.globalAlpha = ea; g.strokeStyle = C.ink; g.beginPath(); g.moveTo(X(v), y0 - 8); g.lineTo(X(v), y0 + 8); g.stroke(); g.restore(); text(String(v).replace('-', '−'), X(v), y0 + 38, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: ea }); }
    const st = smooth((τ - b(3) - 1.5) / 2.5);
    const pts = [[2, C.blue], [-2, C.red]];
    pts.forEach(([x0, col], i) => {
      const x = x0 + st, a = ramp(τ, b(3) + i * 1.2, 0.6) * ea;
      if (st > 0.01) arrow(X(x0), y0 - 30, X(x0 + st), y0 - 30, { color: col, width: 3, head: 11, alpha: a });
      g.save(); g.globalAlpha = a; g.fillStyle = col; g.beginPath(); g.arc(X(x), y0, 12, 0, TAU); g.fill(); g.restore();
      // the observable: bar of height x²
      const bx = 1180 + i * 260, by = 900, sc = 34, v = x * x;
      g.save(); g.globalAlpha = a; g.strokeStyle = C.ink; g.lineWidth = 2; g.strokeRect(bx, by - 9 * sc, 110, 9 * sc);
      g.fillStyle = rgba(col, 0.8); g.fillRect(bx, by - v * sc, 110, v * sc); g.restore();
      text(`start ${x0 > 0 ? '+' : '−'}2`, bx + 55, by + 36, { size: 22, font: SANS, align: 'center', color: col, weight: '600', alpha: a });
      text(`x² = ${v.toFixed(2)}`, bx + 55, by - 9 * sc - 16, { size: 24, font: SANS, align: 'center', alpha: a });
    });
    text('the measurement x²', 1370, 538, { size: 24, font: SANS, align: 'center', color: C.muted, alpha: ramp(τ, b(3), 0.8) * ea });
    text('Same square at the start, different squares after one step.', 560, 830, { size: 28, align: 'center', alpha: ramp(τ, b(3) + 5, 0.8) * ea });
  }
  // closing: the question, and where the tools come from
  const ca = ramp(τ, b(4), 0.9) * out;
  if (ca > 0) {
    text('When a full state is replaced by a summary,', 960, 450, { size: 46, align: 'center', alpha: ca });
    text('which conclusions survive?', 960, 515, { size: 46, align: 'center', alpha: ca });
    const tools = ['finite differences', 'dynamical systems', 'numerical analysis', 'PDE estimates'];
    let x = 960 - (tools.length * 300 - 40) / 2;
    tools.forEach((t, i) => { const a = ramp(τ, b(4) + 4 + i * 0.7, 0.6) * out; panel(x, 610, 260, 64, a); text(t, x + 130, 652, { size: 25, font: SANS, align: 'center', alpha: a }); x += 300; });
    text('Standard tools, organized around one question. Not a new theory of fluids.', 960, 760, { size: 30, align: 'center', color: C.muted, alpha: ramp(τ, b(4) + 8, 0.8) * out });
  }
  source('Adapted from the project’s opening chapter, “A calculus of transformations”.', ramp(τ, b(0), 1) * out);
};

// ---- news: three questions ----
S.news = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  const a0 = ramp(τ, b(0), 1) * out;
  text('Three questions about the Navier–Stokes equations', 960, 190, { size: 46, align: 'center', alpha: a0 });
  text('Short summaries tend to merge them. They have different hypotheses and different answers.', 960, 245, { size: 28, align: 'center', color: C.muted, alpha: ramp(τ, b(0) + 2, 1) * out });
  const rows = [
    ['Forced breakdown', 'A chosen smooth force', 'Smooth flow breaks down in finite time', 'PROOF RELEASED · SEPT 2026', C.red, b(1)],
    ['Forced computation', 'A chosen smooth force', 'Smooth for all time, and carries out any computation', 'NEW PAPERS · OCT 2026', C.blue, b(2)],
    ['Unforced regularity', 'No force at all', 'Do smooth solutions stay smooth forever?', 'OPEN', C.gold, b(3)],
  ];
  const y0 = 380, dy = 165;
  text('QUESTION', 200, y0 - 50, { size: 20, font: SANS, weight: '700', color: C.muted, alpha: ramp(τ, b(1), 0.8) * out });
  text('FORCE', 700, y0 - 50, { size: 20, font: SANS, weight: '700', color: C.muted, alpha: ramp(τ, b(1), 0.8) * out });
  text('WHAT IS ASKED OR SHOWN', 1060, y0 - 50, { size: 20, font: SANS, weight: '700', color: C.muted, alpha: ramp(τ, b(1), 0.8) * out });
  rows.forEach(([q, f, r, st, col, at], i) => {
    const a = ramp(τ, at, 0.8) * out, y = y0 + i * dy;
    panel(170, y - 45, 1580, 135, a);
    g.save(); g.globalAlpha = a; g.fillStyle = col; g.fillRect(170, y - 45, 8, 135); g.restore();
    text(q, 200, y + 5, { size: 34, alpha: a });
    text(f, 700, y + 5, { size: 28, alpha: a, color: i === 2 ? C.ink : C.muted, weight: i === 2 ? '600' : '' });
    text(r, 1060, y + 5, { size: 28, alpha: a });
    tag(st, 1060, y + 60, col, ramp(τ, at + 1.2, 0.6) * out);
  });
  text('First: what the equation actually measures.', 960, 930, { size: 34, italic: true, align: 'center', alpha: ramp(τ, b(4), 0.8) * out });
};

// ---- peak: speed can blow up while energy vanishes ----
const PK = { h: 0.005, hVis: 0.12, lmin: -4 };
S.peak = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('peak', 1);
  // τ sweeps from 1 down to 10⁻⁴ (log-uniform) once the core is introduced
  const sw = smooth((τ - b(2) - 1.0) / (b(6) - b(2) - 0.5));
  const lt = PK.lmin * sw, tau = 10 ** lt;
  // opening: a tall narrow bump and a low wide bump (illustrative)
  const oa = ramp(τ, b(0) + 1, 0.8) * (1 - ramp(τ, b(2), 0.8));
  if (oa > 0) {
    panel(150, 150, 780, 760, oa);
    const base = 760, X0 = 200, Wd = 680, bump = (x, c, w, hgt) => hgt * Math.exp(-(((x - c) / w) ** 2));
    const prof = [[0.3, 0.12, 120, C.blue, 'low and wide'], [0.72, 0.006, 480, C.red, 'tall and narrow']];
    for (const [c, w, hgt, col, lab] of prof) {
      g.save(); g.globalAlpha = oa;
      g.fillStyle = rgba(col, 0.15); g.strokeStyle = col; g.lineWidth = 4; g.beginPath(); g.moveTo(X0, base);
      for (let k = 0; k <= 400; k++) { const x = k / 400; g.lineTo(X0 + x * Wd, base - bump(x, c, w, hgt)); }
      g.lineTo(X0 + Wd, base); g.closePath(); g.fill(); g.stroke(); g.restore();
      text(lab, X0 + c * Wd, base + 40, { size: 24, font: SANS, align: 'center', color: col, alpha: oa });
    }
    g.save(); g.globalAlpha = oa; g.strokeStyle = C.ink; g.lineWidth = 2; g.beginPath(); g.moveTo(X0, base); g.lineTo(X0 + Wd, base); g.stroke(); g.restore();
    text('speed across space · illustration', 175, 190, { size: 21, font: SANS, color: C.muted, alpha: oa });
    // ∫u² for each bump, computed on the drawn profiles (same units)
    const e2 = prof.map(([c, w, hgt]) => { let sum = 0; for (let k = 0; k <= 20000; k++) sum += bump(k / 20000, c, w, hgt) ** 2 / 20000; return sum; });
    text('Four times the peak speed, a twentieth of the width:', 175, 840, { size: 25, alpha: ramp(τ, b(1) + 2, 0.8) * oa });
    text(`∫u² is ${(e2[1] / e2[0]).toFixed(2)} times that of the wide bump (computed).`, 175, 875, { size: 25, alpha: ramp(τ, b(1) + 2, 0.8) * oa });
  }
  // left: radial–axial section of the core (schematic, aspect exaggerated)
  const ca = ramp(τ, b(2), 1) * out;
  const cx = 540, cy = 520, R0 = 260;
  if (ca > 0) {
    panel(150, 150, 780, 760, ca);
    text('radial–axial section of the core · schematic, aspect exaggerated', 175, 190, { size: 21, font: SANS, color: C.muted, alpha: ca });
    // fixed-scale view: the core shrinks to the origin
    const r = R0 * Math.sqrt(tau), z = R0 * tau ** (0.5 - PK.hVis);
    g.save(); g.globalAlpha = ca;
    g.strokeStyle = C.faint; g.lineWidth = 1.5; g.setLineDash([6, 6]);
    g.beginPath(); g.moveTo(cx, 230); g.lineTo(cx, 820); g.moveTo(190, cy); g.lineTo(890, cy); g.stroke(); g.setLineDash([]);
    g.fillStyle = rgba(C.red, 0.18); g.strokeStyle = C.red; g.lineWidth = 2.5;
    g.beginPath(); g.ellipse(cx, cy, Math.max(r, 2.5), Math.max(z, 2.5), 0, 0, TAU); g.fill(); g.stroke();
    g.restore();
    text('axis', cx + 10, 245, { size: 20, font: SANS, color: C.muted, alpha: ca });
    text('fixed scale', 175, 860, { size: 22, font: SANS, color: C.muted, alpha: ca });
    // magnifier: zoom with the core so the shape stays visible
    const ma = ramp(τ, b(3), 0.8) * ca, mx = 760, my = 690, mr = 150;
    if (ma > 0) {
      g.save(); g.globalAlpha = ma;
      g.fillStyle = C.paper; g.strokeStyle = C.ink; g.lineWidth = 2;
      g.beginPath(); g.arc(mx, my, mr, 0, TAU); g.fill(); g.stroke(); g.clip();
      const zr = 52, zz = 52 * tau ** (-PK.hVis); // ℓz/ℓr ≍ τ^(−h), exaggerated
      g.fillStyle = rgba(C.red, 0.18); g.strokeStyle = C.red; g.lineWidth = 2.5;
      g.beginPath(); g.ellipse(mx, my, zr, zz, 0, 0, TAU); g.fill(); g.stroke();
      // inflow, axial outflow on either side of a dividing layer near z = 0
      for (const s of [-1, 1]) {
        arrow(mx + s * (zr + 70), my, mx + s * (zr + 22), my, { color: C.blue, width: 3, head: 11 });
        arrow(mx + s * 14, my - 10, mx + s * 14, my - Math.min(zz, 120) + 6, { color: C.blue, width: 3, head: 11 });
        arrow(mx + s * 14, my + 10, mx + s * 14, my + Math.min(zz, 120) - 6, { color: C.blue, width: 3, head: 11 });
      }
      g.restore();
      text('zoomed with the core', mx, my + mr + 30, { size: 21, font: SANS, align: 'center', color: C.muted, alpha: ma });
      text('in', mx - zr - 80, my - 12, { size: 20, font: SANS, color: C.blue, alpha: ma, align: 'center' });
      text('out along the axis', mx, my - mr - 14, { size: 20, font: SANS, color: C.blue, alpha: ma, align: 'center' });
    }
    // live readouts
    const ra = ramp(τ, b(4), 0.8) * out;
    text(`τ = ${tau < 0.01 ? sci(tau, 1) : tau.toFixed(3)}`, 175, 270, { size: 28, font: SANS, alpha: ca });
    text(`peak speed  ×${(tau ** (-0.5 - PK.h)).toFixed(1)}`, 175, 315, { size: 28, font: SANS, color: C.red, weight: '600', alpha: ra });
    text(`core energy ×${(tau ** (0.5 - 3 * PK.h)).toFixed(4)}`, 175, 360, { size: 28, font: SANS, color: C.blue, weight: '600', alpha: ramp(τ, b(5), 0.8) * out });
  }
  // right column
  const R = 1010;
  text('Peak speed is not energy', R, 210, { size: 42, alpha: ramp(τ, b(0), 1) * out });
  eq('en_def', R, 290, { anchor: 'l', size: 36, alpha: ramp(τ, b(1), 0.8) * out });
  text('adds speed squared over space', R + 330, 296, { size: 24, color: C.muted, alpha: ramp(τ, b(1) + 0.8, 0.8) * out });
  eq('pk_l', R, 380, { anchor: 'l', size: 34, alpha: ramp(τ, b(3), 0.8) * out });
  eq('pk_u', R, 445, { anchor: 'l', size: 34, alpha: ramp(τ, b(4), 0.8) * out });
  eq('pk_E', R, 530, { anchor: 'l', size: 32, alpha: ramp(τ, b(5), 0.8) * out });
  // log–log plot of the published scalings, h = 0.005
  const P = { x: 1090, y: 640, w: 640, h: 260 }, pa = ramp(τ, b(4), 0.8) * out;
  logAxes(P, 0, PK.lmin, -2.5, 2.5, pa, { yticks: [[-2, '10⁻²'], [0, '1'], [2, '10²']], xticks: [[0, '1'], [-2, '10⁻²'], [-4, '10⁻⁴']] });
  logCurve(P, 0, PK.lmin, -2.5, 2.5, l => (-0.5 - PK.h) * l, lt, { color: C.red, alpha: pa });
  logCurve(P, 0, PK.lmin, -2.5, 2.5, l => (0.5 - 3 * PK.h) * l, lt, { color: C.blue, alpha: ramp(τ, b(5), 0.8) * out });
  text('peak speed', P.x + 0.45 * P.w, P.y + 0.3 * P.h, { size: 24, font: SANS, color: C.red, align: 'center', alpha: pa });
  text('core energy', P.x + 0.45 * P.w, P.y + 0.84 * P.h, { size: 24, font: SANS, color: C.blue, align: 'center', alpha: ramp(τ, b(5), 0.8) * out });
  text('published exponents, plotted with h = 0.005', P.x, P.y - 22, { size: 21, font: SANS, color: C.muted, alpha: pa });
  text('Energy alone does not rule this out.', R, 990, { size: 30, alpha: ramp(τ, b(6), 0.8) * out });
  source('Scalings: OpenAI, “Finite time blowup for Navier–Stokes”, §2.1 and §3.5. Core picture: schematic.', ramp(τ, b(2), 1) * out);
};

// ---- residual: defining the force is free; keeping it smooth is not ----
const LO = { G: 1, nu: 0.05 };
const loU = (r, tau) => LO.G / (TAU * r) * (1 - Math.exp(-r * r / (4 * LO.nu * tau)));
const loF = (r, tau) => LO.G * r * Math.exp(-r * r / (4 * LO.nu * tau)) / (2 * TAU * LO.nu * tau * tau);
function loMax(f, tau) { let m = 0; for (let k = 1; k <= 400; k++) m = Math.max(m, f(Math.sqrt(LO.nu * tau) * 6 * k / 400, tau)); return m; }
S.residual = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('residual', 1);
  const R = 1010;
  // the definition and the requirements
  text('A force can be defined from any flow', R, 210, { size: 40, alpha: ramp(τ, b(0), 1) * out });
  eq('rs_def', R, 290, { anchor: 'l', size: 36, alpha: ramp(τ, b(0) + 1.5, 0.8) * out });
  text('the leftover of the equation, called the force', R, 345, { size: 24, color: C.muted, alpha: ramp(τ, b(0) + 2, 0.8) * out });
  const reqs = ['smooth in space and time', 'zero outside a bounded region of space and time', 'every derivative bounded, through the blowup time'];
  reqs.forEach((q, i) => {
    const a = ramp(τ, b(1) + 1 + i * 2.2, 0.7) * out;
    text('✓', R, 420 + i * 48, { size: 28, font: SANS, color: C.teal, weight: '700', alpha: a });
    text(q, R + 40, 420 + i * 48, { size: 28, alpha: a });
  });
  const fa0 = ramp(τ, b(0) + 1, 0.8) * (1 - ramp(τ, b(2), 0.8));
  if (fa0 > 0) {
    const boxes = [['choose any incompressible u', 300], ['compute the leftover', 520], ['call it the force f', 740]];
    boxes.forEach(([s2, y], i) => {
      const a = ramp(τ, b(0) + 1 + i * 2.2, 0.7) * fa0;
      panel(230, y - 50, 620, 90, a);
      text(s2, 540, y + 8, { size: 32, align: 'center', alpha: a });
      if (i < 2) arrow(540, y + 48, 540, y + 165, { width: 3, alpha: ramp(τ, b(0) + 2 + i * 2.2, 0.6) * fa0 });
    });
    text('the equation now holds by definition', 540, 870, { size: 26, italic: true, align: 'center', color: C.muted, alpha: ramp(τ, b(0) + 7, 0.8) * fa0 });
  }
  // squeezed vortex: log–log of peak speed and peak leftover force
  const va = ramp(τ, b(2), 0.8) * out * (1 - ramp(τ, b(4), 0.8));
  const sw = smooth((τ - b(2) - 2.0) / (b(4) - b(2) - 2.5)), lt = -4 * sw, tau = 10 ** lt;
  if (va > 0) {
    panel(150, 150, 780, 800, va);
    text('teaching example · not the paper’s flow', 175, 190, { size: 21, font: SANS, color: C.muted, alpha: va });
    text('a classical vortex, squeezed by hand', 175, 232, { size: 30, alpha: va });
    eq('rs_lo', 175, 300, { anchor: 'l', size: 30, alpha: va });
    // profile of u_θ at the current τ, rescaled to the panel
    const Pp = { x: 200, y: 360, w: 680, h: 150 };
    const rmax = 0.6, um = loMax(loU, tau);
    g.save(); g.globalAlpha = va;
    g.strokeStyle = C.ink; g.lineWidth = 2; g.beginPath(); g.moveTo(Pp.x, Pp.y + Pp.h); g.lineTo(Pp.x + Pp.w, Pp.y + Pp.h); g.stroke();
    g.strokeStyle = C.blue; g.lineWidth = 4; g.beginPath();
    for (let k = 1; k <= 300; k++) { const r = rmax * k / 300; const X = Pp.x + r / rmax * Pp.w, Y = Pp.y + Pp.h - loU(r, tau) / um * Pp.h; k > 1 ? g.lineTo(X, Y) : g.moveTo(X, Y); }
    g.stroke(); g.restore();
    text('swirl speed u_θ across radius r (rescaled to its peak)', Pp.x, Pp.y + Pp.h + 32, { size: 21, font: SANS, color: C.muted, alpha: va });
    const P = { x: 230, y: 610, w: 640, h: 250 };
    logAxes(P, 0, -4, -1, 6, va, { yticks: [[0, '1'], [2, '10²'], [4, '10⁴'], [6, '10⁶']], xticks: [[0, '1'], [-2, '10⁻²'], [-4, '10⁻⁴']] });
    const u0 = Math.log10(loMax(loU, 1)), f0 = Math.log10(loMax(loF, 1));
    logCurve(P, 0, -4, -1, 6, l => Math.log10(loMax(loU, 10 ** l)) - u0, lt, { color: C.blue, alpha: va });
    const fa = ramp(τ, b(3), 0.8) * va;
    logCurve(P, 0, -4, -1, 6, l => Math.log10(loMax(loF, 10 ** l)) - f0, lt, { color: C.red, alpha: Math.max(fa, 0.35 * va) });
    g.save(); g.globalAlpha = va * 0.8; g.strokeStyle = C.teal; g.lineWidth = 3; g.setLineDash([10, 8]);
    const yb = P.y + P.h - (0.3 + 1) / 7 * P.h; g.beginPath(); g.moveTo(P.x, yb); g.lineTo(P.x + P.w, yb); g.stroke(); g.restore();
    text('a bounded force stays near here', P.x + 10, yb - 12, { size: 21, font: SANS, color: C.teal, alpha: va });
    text('peak speed', P.x + P.w - 10, P.y + P.h - 0.62 * P.h, { size: 22, font: SANS, color: C.blue, align: 'right', alpha: va });
    text('peak leftover force', P.x + 300, P.y + 26, { size: 22, font: SANS, color: C.red, align: 'right', alpha: va });
    text(`τ = ${tau < 0.01 ? sci(tau, 1) : tau.toFixed(3)}    force ×${sci(loMax(loF, tau) / loMax(loF, 1), 1)}`, 175, 925, { size: 24, font: SANS, alpha: va });
  }
  eq('rs_R', R, 640, { anchor: 'l', size: 30, alpha: ramp(τ, b(3), 0.8) * out * (1 - ramp(τ, b(4), 0.8)) });
  text('Not allowed: this force blows up with the flow.', R, 720, { size: 30, italic: true, color: C.red, alpha: ramp(τ, b(3) + 3, 0.8) * out * (1 - ramp(τ, b(4), 0.8)) });
  // the published layout: core, ring, outer flow
  const ka = ramp(τ, b(4) + 0.3, 0.9) * out;
  if (ka > 0) {
    const cx = 540, cy = 560;
    g.save(); g.globalAlpha = ka;
    g.fillStyle = rgba(C.teal, 0.07); g.beginPath(); g.arc(cx, cy, 330, 0, TAU); g.fill();
    g.fillStyle = rgba(C.red, 0.22); g.beginPath(); g.arc(cx, cy, 200, 0, TAU); g.fill();
    g.fillStyle = rgba(C.blue, 0.16); g.beginPath(); g.arc(cx, cy, 130, 0, TAU); g.fill();
    g.strokeStyle = C.ink; g.lineWidth = 1.5; for (const r of [130, 200, 330]) { g.beginPath(); g.arc(cx, cy, r, 0, TAU); g.stroke(); }
    g.restore();
    text('core', cx, cy - 10, { size: 28, align: 'center', alpha: ka });
    text('balanced to leading order', cx, cy + 24, { size: 20, font: SANS, align: 'center', color: C.muted, alpha: ka });
    text('ring', cx, cy - 158, { size: 26, align: 'center', color: C.red, alpha: ka });
    text('outer flow', cx, cy - 262, { size: 26, align: 'center', alpha: ka });
    text('exact heat flow · no leftover', cx, cy - 232, { size: 20, font: SANS, align: 'center', color: C.muted, alpha: ka });
    text('top view · schematic', 175, 190, { size: 21, font: SANS, color: C.muted, alpha: ka });
    text('Leftover imbalance lives in the ring at the core’s edge,', R, 640, { size: 30, alpha: ramp(τ, b(4) + 3, 0.8) * out });
    text('and still blows up as τ → 0.', R, 682, { size: 30, alpha: ramp(τ, b(4) + 3, 0.8) * out });
    text('It has to be cancelled inside the fluid.', R, 750, { size: 30, color: C.red, alpha: ramp(τ, b(4) + 7, 0.8) * out });
  }
  source(ka > 0.5 ? 'Layout: OpenAI, §2.2–2.3 and §3.2 (the stress T is supported in an annulus).' : 'Lamb–Oseen profile with its width forced to shrink like √τ; pressure balances u_θ²/r, leaving only f_θ.', ramp(τ, b(2), 1) * out);
};

// ---- waves: mean flux from oscillations; growth and decay in shear ----
const SW = { S: 1, nu: 0.004, kx: 1, ky0: 6 };
const swKy = t => SW.ky0 - SW.S * SW.kx * t;
const swInt = t => SW.kx ** 2 * t + SW.ky0 ** 2 * t - SW.ky0 * SW.S * SW.kx * t * t + SW.S ** 2 * SW.kx ** 2 * t ** 3 / 3;
const swAmp = t => Math.hypot(SW.kx, SW.ky0) / Math.hypot(SW.kx, swKy(t)) * Math.exp(-SW.nu * swInt(t)); // A(t)/A0
let swImg = null;
function drawShearWave(B, t, alpha) {
  if (alpha <= 0) return;
  const n = 240;
  if (!swImg) swImg = g.createImageData(n, n);
  const amp = swAmp(t) / 4.45, d = swImg.data;
  for (let j = 0; j < n; j++) for (let i = 0; i < n; i++) {
    const x = TAU * (i + 0.5) / n, y = TAU * (1 - (j + 0.5) / n);
    const v = amp * Math.sin(SW.kx * x + swKy(t) * y);
    const k = 4 * (j * n + i), c = v > 0 ? [43, 89, 195] : [200, 70, 43], s = Math.min(1, Math.abs(v));
    d[k] = 255 - (255 - c[0]) * s; d[k + 1] = 253 - (253 - c[1]) * s; d[k + 2] = 248 - (248 - c[2]) * s; d[k + 3] = 255;
  }
  const off = new OffscreenCanvas(n, n); off.getContext('2d').putImageData(swImg, 0, 0);
  g.save(); g.globalAlpha = alpha; g.imageSmoothingEnabled = true; g.drawImage(off, B.x, B.y, B.s, B.s);
  g.strokeStyle = C.ink; g.lineWidth = 2; g.strokeRect(B.x, B.y, B.s, B.s);
  // background shear arrows U = (S y, 0), measured from the centre line
  for (let k = 0; k <= 8; k++) {
    const y = B.y + B.s * k / 8, u = (0.5 - k / 8) * 2;
    arrow(B.x + B.s + 30, y, B.x + B.s + 30 + u * 60, y, { color: C.muted, width: 3, head: 11 });
  }
  g.restore();
  // faint crest lines keep the geometry visible after the wave has faded
  g.save(); g.globalAlpha = alpha * 0.35; g.strokeStyle = C.ink; g.lineWidth = 1;
  g.beginPath(); g.rect(B.x, B.y, B.s, B.s); g.clip(); g.beginPath();
  const ky = swKy(t);
  for (let m = -40; m <= 40; m++) { // k_x x + k_y y = π/2 + 2πm
    const c = Math.PI / 2 + TAU * m;
    if (Math.abs(ky) < 1e-6) { const x = c / SW.kx; g.moveTo(B.x + x / TAU * B.s, B.y); g.lineTo(B.x + x / TAU * B.s, B.y + B.s); continue; }
    const yA = c / ky, yB = (c - SW.kx * TAU) / ky;
    g.moveTo(B.x, B.y + B.s - yA / TAU * B.s); g.lineTo(B.x + B.s, B.y + B.s - yB / TAU * B.s);
  }
  g.stroke(); g.restore();
}
S.waves = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('waves', 1);
  const R = 1060;
  // part 1: a plane wave and its averages
  const pa = ramp(τ, b(0), 0.8) * (1 - ramp(τ, b(3), 0.8));
  const B = { x: 170, y: 170, s: 740 };
  if (pa > 0) {
    const a = [0.8, -0.6], xi = [0.6, 0.8].map(v => v * 3), ph = τ * 1.2;
    panel(B.x - 20, B.y - 20, B.s + 40, B.s + 40, pa);
    let s1 = 0, s2 = 0, s12 = 0, n = 0;
    for (let i = 0; i < 15; i++) for (let j = 0; j < 15; j++) {
      const x = (i + 0.5) / 15 * TAU, y = (j + 0.5) / 15 * TAU, c = Math.cos(xi[0] * x + xi[1] * y - ph);
      arrow(B.x + x / TAU * B.s, B.y + B.s - y / TAU * B.s, B.x + x / TAU * B.s + a[0] * c * 34, B.y + B.s - y / TAU * B.s - a[1] * c * 34, { width: 2.5, head: 9, alpha: pa, color: c > 0 ? C.blue : C.red });
    }
    for (let k = 0; k < 4096; k++) { const c = Math.cos(TAU * k / 4096 - ph); s1 += a[0] * c; s2 += a[1] * c; s12 += a[0] * a[1] * c * c; n++; }
    const av = pa * (1 - ramp(τ, b(2), 0.6));
    text('Averages over one wavelength, computed live:', R, 600, { size: 24, font: SANS, color: C.muted, alpha: ramp(τ, b(0) + 3, 0.8) * av });
    text(`⟨w₁⟩ = ${fx(s1 / n)}     ⟨w₂⟩ = ${fx(s2 / n)}`, R, 645, { size: 28, font: SANS, alpha: ramp(τ, b(0) + 3, 0.8) * av });
    text(`⟨w₁w₂⟩ = ${fx(s12 / n)}  =  ½ a₁a₂`, R, 690, { size: 28, font: SANS, weight: '600', color: C.purple, alpha: ramp(τ, b(1), 0.8) * av });
  }
  text('Waves that average to zero can still push', R, 210, { size: 38, alpha: ramp(τ, b(0), 1) * out * (1 - ramp(τ, b(3), 0.8)) });
  eq('wv_w', R, 290, { anchor: 'l', size: 34, alpha: ramp(τ, b(0) + 1.5, 0.8) * pa });
  eq('wv_avg', R, 365, { anchor: 'l', size: 34, alpha: ramp(τ, b(1), 0.8) * pa });
  text('its divergence acts like a force on the background', R, 425, { size: 24, color: C.muted, alpha: ramp(τ, b(1) + 2, 0.8) * pa });
  // cone of two families
  const ca = ramp(τ, b(2), 0.8) * (1 - ramp(τ, b(3), 0.8));
  if (ca > 0) {
    const ox = 1110, oy = 990, sc = 300, v1 = [1, 0.25], v2 = [0.3, 1];
    const th = (τ - b(2)) * 0.5, T = [0.62 + 0.3 * Math.cos(th), 0.62 + 0.3 * Math.sin(1.3 * th)];
    const det = v1[0] * v2[1] - v2[0] * v1[1];
    const c1 = (T[0] * v2[1] - v2[0] * T[1]) / det, c2 = (v1[0] * T[1] - T[0] * v1[1]) / det;
    g.save(); g.globalAlpha = ca;
    g.fillStyle = rgba(C.purple, 0.12); g.beginPath(); g.moveTo(ox, oy); g.lineTo(ox + v1[0] * 2.4 * sc, oy - v1[1] * 2.4 * sc); g.lineTo(ox + v2[0] * 1.3 * sc, oy - v2[1] * 1.3 * sc); g.closePath(); g.fill();
    g.restore();
    arrow(ox, oy, ox + v1[0] * sc, oy - v1[1] * sc, { color: C.blue, width: 4, alpha: ca });
    arrow(ox, oy, ox + v2[0] * sc, oy - v2[1] * sc, { color: C.red, width: 4, alpha: ca });
    arrow(ox, oy, ox + T[0] * sc, oy - T[1] * sc, { color: C.ink, width: 5, alpha: ca });
    text('v₁', ox + v1[0] * sc + 12, oy - v1[1] * sc + 8, { size: 28, color: C.blue, alpha: ca });
    text('v₂', ox + v2[0] * sc - 10, oy - v2[1] * sc - 14, { size: 28, color: C.red, alpha: ca });
    text('T', ox + T[0] * sc + 12, oy - T[1] * sc - 6, { size: 30, weight: '700', alpha: ca });
    text(`c₁ = ${c1.toFixed(2)}    c₂ = ${c2.toFixed(2)}`, 1500, 630, { size: 28, font: SANS, weight: '600', alpha: ca, color: c1 > 0 && c2 > 0 ? C.teal : C.red });
    text('both positive: realizable', 1500, 670, { size: 21, font: SANS, color: C.muted, alpha: ca });
    eq('wv_cone', R, 500, { anchor: 'l', size: 32, alpha: ca });
  }
  // part 2: one exact wave riding a uniform shear
  const sa = ramp(τ, b(3) + 0.3, 0.9) * out;
  const tw = Math.max(0, τ - b(3) - 3.0) * 0.62; // physical time of the wave
  if (sa > 0) {
    const B2 = { x: 170, y: 190, s: 700 };
    drawShearWave(B2, tw, sa);
    text('one exact wave on the shear U = (Sy, 0)', B2.x, B2.y - 22, { size: 22, font: SANS, color: C.muted, alpha: sa });
    text(`S = ${SW.S}   ν = ${SW.nu}   t = ${tw.toFixed(1)}`, B2.x, B2.y + B2.s + 40, { size: 24, font: SANS, color: C.muted, alpha: sa });
    text('shear', B2.x + B2.s + 60, B2.y - 10, { size: 21, font: SANS, color: C.muted, alpha: sa, align: 'center' });
    text('Exact Navier–Stokes solution, with the pressure the tilting needs:', B2.x, B2.y + B2.s + 80, { size: 21, font: SANS, color: C.muted, alpha: sa });
    text('p = 2SA k_x²/|k|³ · cos(k·x).', B2.x, B2.y + B2.s + 108, { size: 21, font: SANS, color: C.muted, alpha: sa });
    text('One wave on a shear', R, 210, { size: 38, alpha: sa });
    eq('wv_k', R, 285, { anchor: 'l', size: 32, alpha: ramp(τ, b(4), 0.8) * out });
    eq('wv_A', R, 365, { anchor: 'l', size: 32, alpha: ramp(τ, b(4) + 0.8, 0.8) * out });
    eq('wv_E', R, 455, { anchor: 'l', size: 30, alpha: ramp(τ, b(4) + 3, 0.8) * out });
    const P = { x: R + 20, y: 560, w: 640, h: 240 }, ga = ramp(τ, b(4), 0.8) * out, tMax = 30;
    plotAxes(P, { yl: 'wave amplitude A(t) / A₀', alpha: ga, yticks: [] });
    for (const v of [0, 1, 2, 3, 4]) {
      const yy = P.y + P.h - v / 4.6 * P.h;
      g.save(); g.globalAlpha = ga; g.strokeStyle = C.faint; g.lineWidth = 1; g.beginPath(); g.moveTo(P.x, yy); g.lineTo(P.x + P.w, yy); g.stroke(); g.restore();
      text(String(v), P.x - 12, yy + 8, { size: 22, font: SANS, align: 'right', color: C.muted, alpha: ga });
    }
    plotCurve(P, t => swAmp(t) / 4.6, tMax, { color: C.purple, upto: clamp(tw, 0, tMax), alpha: ga });
    text(`A/A₀ = ${swAmp(tw).toFixed(2)}`, P.x + P.w - 10, P.y + 30, { size: 26, font: SANS, align: 'right', color: C.purple, weight: '600', alpha: ga });
    const leaning = swKy(tw) > 0;
    text(leaning ? 'crests lean against the shear: the wave draws energy, grows' : 'crests lean with the shear: energy goes back; viscosity finishes it',
      R, 860, { size: 26, italic: true, color: leaning ? C.teal : C.red, alpha: ramp(τ, b(4) + 1, 0.8) * out });
    const na = ramp(τ, b(5), 0.8) * out;
    text('The published pulses grow by rotation on a collapsing core:', R, 930, { size: 25, alpha: na });
    text('this Kelvin shearing wave is an analogue, not the construction.', R, 966, { size: 25, alpha: na });
  }
  source(sa > 0.5 ? 'Pulse behaviour: OpenAI, §2.2 and §3.3 (seeded, amplified by shear, then viscously damped).' : 'Two-family positive representation of the stress: OpenAI, §3.2, Figure 4, Proposition 7.5.', ramp(τ, b(0), 1) * out);
};

// ---- proof: the chain of obligations ----
S.proof = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('proof', 1);
  const steps = [
    ['Collapsing core and smooth outer heat flow', '§4, App. A–B', b(1)],
    ['Leftover imbalance written as a stress in the ring', '§4–5', b(1) + 3.8],
    ['Two pulse families cancel it, on finer and finer scales', '§6–7, App. C', b(1) + 7.6],
    ['Correct new errors until the rest vanishes to every order', '§8–9', b(2)],
    ['Cut off in space; extend the force smoothly past t = 1', '§10.1–10.2', b(2) + 6],
    ['Energy bounded, because the force is', 'Lemma 10.4', b(3)],
    ['A bounded-energy rival must agree, so blows up too', 'Lemma 10.5', b(3) + 4.5],
  ];
  text('Steps in the proof', 150, 180, { size: 40, alpha: ramp(τ, b(0), 1) * out });
  steps.forEach(([s, ref, at], i) => {
    const a = ramp(τ, at, 0.7) * out, y = 260 + i * 100;
    panel(150, y - 40, 860, 76, a);
    g.save(); g.globalAlpha = a; g.fillStyle = C.ink; g.beginPath(); g.arc(190, y - 2, 18, 0, TAU); g.fill(); g.restore();
    text(String(i + 1), 190, y + 7, { size: 22, font: SANS, align: 'center', color: C.paper, weight: '700', alpha: a });
    text(s, 225, y + 7, { size: 25, alpha: a });
    text(ref, 990, y + 7, { size: 20, font: SANS, align: 'right', color: C.muted, alpha: a });
    if (i < steps.length - 1) arrow(190, y + 20, 190, y + 56, { color: C.muted, width: 2, head: 9, alpha: ramp(τ, steps[i + 1][2], 0.6) * out });
  });
  // statement
  const R = 1080, sa = ramp(τ, b(4), 0.8) * out;
  if (sa > 0) {
    panel(R - 30, 220, 760, 470, sa);
    text('THEOREM 1.1 (OPENAI), IN WORDS', R, 265, { size: 20, font: SANS, weight: '700', color: C.muted, alpha: sa });
    let y = wrapText('For every viscosity ν > 0 there is a smooth force, zero outside a bounded region of space and time, and a smooth solution starting from rest on 0 ≤ t < 1, with', R, 315, 700, { size: 26, alpha: sa });
    eq('pr_lim', R, y + 20, { anchor: 'l', size: 28, alpha: sa });
    y = wrapText('So no smooth bounded-energy solution exists for all time, alternative (C) on ℝ³; on the periodic box, no global smooth solution at all, (D).', R, y + 85, 700, { size: 26, alpha: ramp(τ, b(4) + 3, 0.8) * out });
    text('Lean formalization: openai/NavierStokesAndEuler', R, y + 30, { size: 21, font: SANS, color: C.muted, alpha: ramp(τ, b(4) + 6, 0.8) * out });
  }
  const za = ramp(τ, b(5), 0.8) * out;
  if (za > 0) {
    panel(R - 30, 730, 760, 230, za);
    text('THE FORCE IS NOT ZERO', R, 775, { size: 20, font: SANS, weight: '700', color: C.red, alpha: za });
    eq('pr_en', R, 830, { anchor: 'l', size: 30, alpha: za });
    text('With f = 0 and a fluid at rest, this keeps u = 0.', R, 900, { size: 25, alpha: ramp(τ, b(5) + 2.5, 0.8) * out });
    text('The unforced problem is a different question.', R, 937, { size: 25, italic: true, alpha: ramp(τ, b(5) + 4.5, 0.8) * out });
  }
  source('Source: OpenAI, “Finite time blowup for Navier–Stokes” (166 pp.), Theorem 1.1, Corollary 10.6, §3 outline.', ramp(τ, b(0), 1) * out);
};

// ---- compute: smooth flows that compute ----
const CPT = { lam: [2, 0.625, 0.8] };
function isoBox(cx, cy, L, alpha, color) { // L = [lx, ly, lz] in px; simple oblique projection
  if (alpha <= 0) return;
  const ox = 0.45, oy = -0.32;
  const P = (x, y, z) => [cx + x + ox * z, cy - y + oy * z];
  const [a, b2, c] = L, v = [[0, 0, 0], [a, 0, 0], [a, b2, 0], [0, b2, 0], [0, 0, c], [a, 0, c], [a, b2, c], [0, b2, c]].map(p => P(p[0] - a / 2, p[1] - b2 / 2, p[2] - c / 2));
  const E = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]];
  g.save(); g.globalAlpha = alpha;
  g.fillStyle = rgba(color, 0.12); g.beginPath(); [4, 5, 6, 7].forEach((k, i) => i ? g.lineTo(...v[k]) : g.moveTo(...v[k])); g.closePath(); g.fill();
  g.strokeStyle = color; g.lineWidth = 2.5; for (const [i, j] of E) { g.beginPath(); g.moveTo(...v[i]); g.lineTo(...v[j]); g.stroke(); }
  g.restore();
}
// A finite program trace illustrating encoding, not a claimed PDE solution.
function drawProgramExample(P, progress, language = 'en') {
  const zh=language==='zh',fontSize=P.w<1000?29:32;
  const xs=[.15,.5,.85].map(t=>P.x+t*P.w), top=P.y+P.h*.27, bottom=P.y+P.h*.75;
  text(zh?'程序中的值':'Value in the program',P.x,P.y+30,{size:fontSize,font:SANS,color:C.muted});
  text(zh?'粒子的位置':'Particle position',P.x,bottom-95,{size:fontSize,font:SANS,color:C.muted});
  for(let i=0;i<3;i++) {
    const active=Math.min(2,Math.floor(progress+.00001))===i;
    panel(xs[i]-P.w*.11,top-58,P.w*.22,104,1);
    text(String(i),xs[i],top+16,{size:50,align:'center',color:active?C.blue:C.muted});
    if(i<2) {
      arrow(xs[i]+P.w*.12,top,xs[i+1]-P.w*.12,top,{width:3,color:C.muted,head:12});
      text('+1',(xs[i]+xs[i+1])/2,top-26,{size:28,align:'center',color:C.muted});
    }
    g.save();g.strokeStyle=C.faint;g.setLineDash([5,8]);g.beginPath();g.moveTo(xs[i],top+65);g.lineTo(xs[i],bottom-25);g.stroke();g.restore();
    g.save();g.fillStyle=C.faint;g.beginPath();g.arc(xs[i],bottom,8,0,TAU);g.fill();g.restore();
  }
  g.save();g.fillStyle=rgba(C.teal,.08);g.strokeStyle=C.teal;g.lineWidth=2;
  g.fillRect(xs[2]-55,bottom-60,110,120);g.strokeRect(xs[2]-55,bottom-60,110,120);g.restore();
  text(zh?'停止':'Stop',xs[2],bottom+106,{size:fontSize,align:'center',color:C.teal});
  const segment=Math.min(1,Math.floor(progress)), f=clamp(progress-segment);
  const x=lerp(xs[segment],xs[segment+1],f);
  g.save();g.strokeStyle=C.blue;g.lineWidth=3;g.beginPath();g.moveTo(xs[0],bottom);g.lineTo(x,bottom);g.stroke();
  g.fillStyle=C.blue;g.beginPath();g.arc(x,bottom,13,0,TAU);g.fill();g.restore();
  text(zh?'有限程序的示意图':'A finite program, shown schematically',P.x,P.y+P.h+35,{size:23,font:SANS,color:C.muted});
}
S.compute = (τ, b, D) => {
  const out = 1 - ramp(τ, D - 0.9, 0.8);
  chapterBar('compute', 1);
  const R = 1080;
  text('Smooth for all time, and computing', 150, 180, { size: 40, alpha: ramp(τ, b(0), 1) * out });
  const exampleAlpha = ramp(τ, b(0), .7) * (1 - ramp(τ, b(2), .7));
  if (exampleAlpha > 0) {
    g.save(); g.globalAlpha = exampleAlpha;
    const progress = 2 * smooth((τ - b(1) - 1.5) / Math.max(4, b(2) - b(1) - 3.5));
    drawProgramExample({x:150,y:300,w:1620,h:580}, progress, FILM_LANG);
    g.restore();
  }
  const encodingAlpha = ramp(τ, b(2), .7) * (1 - ramp(τ, b(3), .7));
  if (encodingAlpha > 0) {
    text('A complete machine state', 220, 330, {size:36,alpha:encodingAlpha});
    text('stored symbols + next instruction', 220, 390, {size:28,color:C.muted,alpha:encodingAlpha});
    const symbols = ['…','1','0','1','1','0','…'];
    symbols.forEach((symbol,i) => {
      const x=230+i*90; panel(x,470,80,90,encodingAlpha);
      text(symbol,x+40,532,{size:36,align:'center',alpha:encodingAlpha});
    });
    arrow(930,515,1170,515,{width:4,color:C.blue,alpha:encodingAlpha});
    g.save();g.globalAlpha=encodingAlpha;g.fillStyle=C.blue;g.beginPath();g.arc(1400,515,14,0,TAU);g.fill();g.restore();
    text('particle position (x, y, z)',1400,595,{size:30,align:'center',alpha:encodingAlpha});
    text('The digits of the coordinates record the symbols.',960,740,{size:34,align:'center',alpha:encodingAlpha});
    text('Encoding: schematic',150,960,{size:22,font:SANS,color:C.muted,alpha:encodingAlpha});
  }
  // 1–2: box routing with a determinant-one stretch
  const ba = ramp(τ, b(3), 0.8) * (1 - ramp(τ, b(5), 0.8));
  if (ba > 0) {
    panel(150, 230, 860, 700, ba);
    const s = smooth((τ - b(3) - 4) / 6) * (1 - 0) , s2 = smooth((τ - b(4)) / 5);
    const src = [330, 640], tgt = [790, 440];
    const cxy = [lerp(src[0], tgt[0], s), lerp(src[1], tgt[1], s)];
    const L0 = 150, L = CPT.lam.map(l => L0 * l ** s2);
    isoBox(src[0], src[1], [L0, L0, L0], ba * 0.35, C.muted);
    isoBox(tgt[0], tgt[1], CPT.lam.map(l => L0 * l), ba * 0.35 * ramp(τ, b(4), 0.8), C.muted);
    isoBox(cxy[0], cxy[1], L, ba, C.blue);
    // points = tapes sharing the prefix that the instruction reads
    g.save(); g.globalAlpha = ba;
    const rr = (() => { let q = 7; return () => (q = (q * 16807) % 2147483647) / 2147483647; })();
    for (let k = 0; k < 60; k++) { const u = rr() - 0.5, v = rr() - 0.5, w = rr() - 0.5;
      const x = cxy[0] + u * L[0] + 0.45 * w * L[2], y = cxy[1] - v * L[1] - 0.32 * w * L[2];
      g.fillStyle = C.ink; g.beginPath(); g.arc(x, y, 3.2, 0, TAU); g.fill(); }
    g.restore();
    text('source box: every tape whose prefix the rule reads', 180, 890, { size: 22, font: SANS, color: C.muted, alpha: ba });
    text('target box', tgt[0], tgt[1] + 150, { size: 22, font: SANS, color: C.muted, align: 'center', alpha: ba * ramp(τ, b(4), 0.8) });
    text('schematic route; the map on the box is the exact affine instruction', 180, 270, { size: 21, font: SANS, color: C.muted, alpha: ba });
    const vol = CPT.lam.reduce((p, l) => p * l ** s2, 1);
    eq('cp_vol', R, 330, { anchor: 'l', size: 34, alpha: ramp(τ, b(4), 0.8) * ba });
    text(`volume ratio = ${vol.toFixed(6)}`, R, 400, { size: 28, font: SANS, weight: '600', color: C.teal, alpha: ramp(τ, b(4), 0.8) * ba });
    text(`sides ×${(CPT.lam[0] ** s2).toFixed(3)}, ×${(CPT.lam[1] ** s2).toFixed(3)}, ×${(CPT.lam[2] ** s2).toFixed(3)}`, R, 445, { size: 25, font: SANS, color: C.muted, alpha: ramp(τ, b(4), 0.8) * ba });
    text('A tape is the coordinates of one point.', R, 250, { size: 28, alpha: ramp(τ, b(3), 0.8) * ba });
  }
  // 3: reversibility
  const ra = ramp(τ, b(5), 0.8) * (1 - ramp(τ, b(6), 0.8));
  if (ra > 0) {
    const L = 220, y1 = 380, y2 = 560;
    text('An ordinary program may forget', 200, 300, { size: 28, color: C.red, alpha: ra });
    for (const [lab, y] of [['input A', y1], ['input B', y2]]) { panel(L - 40, y - 35, 170, 60, ra); text(lab, L + 45, y + 5, { size: 24, font: SANS, align: 'center', alpha: ra }); arrow(L + 140, y, 560, (y1 + y2) / 2, { color: C.red, width: 3, alpha: ra }); }
    panel(570, (y1 + y2) / 2 - 35, 170, 60, ra); text('output', 655, (y1 + y2) / 2 + 5, { size: 24, font: SANS, align: 'center', alpha: ra });
    text('A smooth flow cannot merge two particles.', 200, 690, { size: 26, alpha: ramp(τ, b(5) + 3, 0.8) * ra });
    text('Keep the history, and every step is reversible:', R - 20, 300, { size: 28, color: C.teal, alpha: ramp(τ, b(5) + 5, 0.8) * ra });
    for (const [lab, o, y] of [['A', '(output, A)', y1], ['B', '(output, B)', y2]]) {
      const a = ramp(τ, b(5) + 6, 0.8) * ra;
      panel(R, y - 35, 150, 60, a); text('input ' + lab, R + 75, y + 5, { size: 24, font: SANS, align: 'center', alpha: a });
      arrow(R + 160, y, R + 330, y, { color: C.teal, width: 3, alpha: a });
      panel(R + 340, y - 35, 230, 60, a); text(o, R + 455, y + 5, { size: 24, font: SANS, align: 'center', alpha: a });
    }
    text('History records: Bennett (1973). Affine symbol updates: Moore (1990–91).', 200, 780, { size: 21, font: SANS, color: C.muted, alpha: ramp(τ, b(5) + 6, 0.8) * ra });
  }
  // 4: the commutative square
  const qa = ramp(τ, b(6), 0.8) * (1 - ramp(τ, b(7), 0.8));
  if (qa > 0) {
    const L = 360, Rx = 860, T = 360, Bt = 660;
    eq('cp_c', L, T, { size: 46, alpha: qa }); eq('cp_Tc', Rx, T, { size: 46, alpha: qa });
    arrow(L + 40, T, Rx - 60, T, { width: 3, alpha: qa }); eq('cp_T', (L + Rx) / 2, T - 36, { size: 36, alpha: qa });
    text('compute', (L + Rx) / 2, T + 40, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: qa });
    arrow(L, T + 40, L, Bt - 40, { width: 3, alpha: qa }); arrow(Rx, T + 40, Rx, Bt - 40, { width: 3, alpha: qa });
    eq('cp_E1', L - 30, (T + Bt) / 2, { size: 36, alpha: qa }); eq('cp_E2', Rx + 30, (T + Bt) / 2, { size: 36, alpha: qa });
    eq('cp_Ec', L, Bt, { size: 42, alpha: qa }); eq('cp_ETc', Rx, Bt, { size: 42, alpha: qa });
    arrow(L + 70, Bt, Rx - 90, Bt, { width: 3, alpha: qa, color: C.blue }); eq('cp_Phi', (L + Rx) / 2, Bt - 36, { size: 36, alpha: qa, color: C.blue });
    text('flow', (L + Rx) / 2, Bt + 40, { size: 22, font: SANS, align: 'center', color: C.blue, alpha: qa });
    text('encode', L - 70, (T + Bt) / 2 + 40, { size: 22, font: SANS, align: 'center', color: C.muted, alpha: qa });
    eq('cp_sq', R, 420, { anchor: 'l', size: 36, alpha: qa });
    wrapText('Encode, then flow, equals compute, then encode: the factor criterion, built in on purpose.', R, 500, 700, { size: 28, alpha: ramp(τ, b(6) + 3, 0.8) * qa });
    wrapText('Asserted for the material flow at instruction times, on each rule’s whole domain.', R, 620, 700, { size: 23, font: SANS, color: C.muted, alpha: ramp(τ, b(6) + 5, 0.8) * qa });
  }
  // 5–6: the detector
  const da = ramp(τ, b(7), 0.8) * (1 - ramp(τ, b(9), 0.8));
  if (da > 0) {
    panel(150, 230, 860, 700, da);
    g.save(); g.globalAlpha = da;
    g.fillStyle = rgba(C.teal, 0.15); g.strokeStyle = C.teal; g.lineWidth = 3; g.fillRect(780, 330, 180, 180); g.strokeRect(780, 330, 180, 180);
    g.restore();
    text('target box', 870, 545, { size: 22, font: SANS, align: 'center', color: C.teal, alpha: da });
    const pth = (k, s) => k ? [230 + 700 * s, 760 - 120 * Math.sin(5 * s) - 160 * s] : [230 + 640 * s, 700 - 300 * s + 60 * Math.sin(9 * s)];
    for (const [k, col, lab] of [[0, C.blue, 'halting run: enters'], [1, C.red, 'non-halting run: never enters']]) {
      const s = clamp((τ - b(7) - 1 - k * 0.5) / 8);
      g.save(); g.globalAlpha = da; g.strokeStyle = col; g.lineWidth = 3.5; g.beginPath();
      for (let i = 0; i <= 100 * s; i++) { const [x, y] = pth(k, i / 100); i ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke();
      const [x, y] = pth(k, s); g.fillStyle = col; g.beginPath(); g.arc(x, y, 8, 0, TAU); g.fill(); g.restore();
      text(lab, 200, 830 + k * 40, { size: 24, font: SANS, color: col, alpha: da });
    }
    text('schematic paths · the proof guards every intermediate time', 180, 270, { size: 21, font: SANS, color: C.muted, alpha: da });
    eq('cp_halt', R, 330, { anchor: 'l', size: 28, alpha: da });
    text('particle starting at a* = (4, 0, 0); balanced three-stack construction', R, 385, { size: 21, font: SANS, color: C.muted, alpha: da });
    wrapText('The marked box represents halting. Intermediate motion is arranged to avoid accidental entry.', R, 460, 720, { size: 27, alpha: ramp(τ, b(7) + 6, 0.8) * da });
    const ua = ramp(τ, b(8), 0.8) * da;
    panel(R - 20, 600, 760, 200, ua);
    text('CONSEQUENCE', R + 10, 645, { size: 20, font: SANS, weight: '700', color: C.muted, alpha: ua });
    wrapText('No algorithm decides, for every force in this family, whether the particle will ever arrive. Halting reduces to it.', R + 10, 690, 700, { size: 27, alpha: ua });
  }
  const finish = ramp(τ, b(9), .8) * out;
  if (finish > 0) {
    text('Machine rules and input',250,380,{size:38,alpha:finish});
    arrow(750,365,1060,365,{color:C.blue,width:4,alpha:finish});
    text('Prescribed force',1130,380,{size:38,color:C.blue,alpha:finish});
    text('The flow stays smooth for all time.',250,570,{size:38,alpha:finish});
    text('The particle follows the encoded computation.',250,655,{size:38,alpha:finish});
  }
  source('Source: openai/math (6 Oct 2026), family 376, nine manuscripts; balanced three-stack theorem in “Incompressible Box Transport and Finite Computation”.', ramp(τ, b(0), 1) * out);
};

// ---- standing ----
S.standing = (τ, b, D) => {
  const out=1-ramp(τ,D-.9,.8), rowsAlpha=1-ramp(τ,b(3),.7);
  chapterBar('standing',out);
  text('Two uses of a prescribed force',150,190,{size:44,alpha:ramp(τ,b(0),.8)*out*rowsAlpha});
  const rows=[
    ['Forced breakdown','A smooth force; unbounded peak speed in finite time',C.red,b(1)],
    ['Forced computation','A smooth flow; particle motion follows a program',C.blue,b(1)+5],
    ['Unforced regularity','General smooth initial data in 3D, no force: still open',C.gold,b(2)],
  ];
  rows.forEach(([title,body,col,at],i)=>{
    const a=ramp(τ,at,.7)*out*rowsAlpha,y=340+i*185;
    panel(150,y-65,1620,145,a);
    g.save();g.globalAlpha=a;g.fillStyle=col;g.fillRect(150,y-65,7,145);g.restore();
    text(title,185,y-8,{size:34,alpha:a});
    text(body,185,y+43,{size:28,color:C.muted,alpha:a});
  });
  const a=ramp(τ,b(3),.8)*out;
  text('Notes and calculations behind this film:',960,470,{size:40,align:'center',alpha:a});
  text('github.com/hmbown/transformatics',960,545,{size:44,font:SANS,align:'center',color:C.blue,alpha:a});
};

// ---------- frame dispatch ----------
function sceneAt(T) {
  for (const sc of TL.scenes) if (T < sc.end) return sc;
  return TL.scenes[TL.scenes.length - 1];
}
window.setTimeline = tl => {
  TL = tl;
  FILM_LANG = tl.language || 'en';
  document.documentElement.lang = FILM_LANG === 'zh' ? 'zh-CN' : 'en';
  buildEquations();
  buildPressure();
  buildTG(tgS(40));
  // the balance scene continues the measured particle from where "measure" left off
  // "balance" continues the measured particle from where "measure" ends
  const m = TL.scenes.find(s => s.id === 'measure');
  SCENE_T0.balance = Math.max(0, m.end - m.beats[0].start - 1.0) * MEAS_K;
};
window.renderFrame = T => {
  const sc = sceneAt(T);
  const τ = T - sc.start, D = sc.end - sc.start;
  const b = i => (sc.beats[i] ? sc.beats[i].start - sc.start : D);
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.globalAlpha = 1;
  g.fillStyle = C.bg; g.fillRect(0, 0, W, H);
  eqShown = new Set();
  VIEW = { x0: 0, y0: 0, span: TAU };
  S[sc.id](τ, b, D);
  hideUnusedEquations(eqShown);
  return sc.id;
};
