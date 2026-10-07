// Independent numerical checks of the claims the film makes on screen.
// Uses finite differences and quadrature only, not the renderer's formulas
// for derivatives. Run: node checks.mjs
const TAU = 2 * Math.PI;
let failed = 0;
const check = (name, ok, detail) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}  ${detail}`); if (!ok) failed++; };
const rnd = (() => { let s = 12345; return () => (s = (s * 16807) % 2147483647) / 2147483647; })();

// 1. Taylor–Green cells solve the unforced Navier–Stokes equations on the periodic box.
{
  const nu = 0.01;
  const u = (t, x, y) => [Math.sin(x) * Math.cos(y) * Math.exp(-2 * nu * t), -Math.cos(x) * Math.sin(y) * Math.exp(-2 * nu * t)];
  const p = (t, x, y) => 0.25 * (Math.cos(2 * x) + Math.cos(2 * y)) * Math.exp(-4 * nu * t);
  const h = 1e-4;
  let worst = 0, worstDiv = 0;
  for (let k = 0; k < 200; k++) {
    const t = 30 * rnd(), x = TAU * rnd(), y = TAU * rnd();
    const U = u(t, x, y);
    const d = (f, dt, dx, dy) => f(t + dt * h, x + dx * h, y + dy * h);
    for (let i = 0; i < 2; i++) {
      const c = (dt, dx, dy) => d(u, dt, dx, dy)[i];
      const ut = (c(1, 0, 0) - c(-1, 0, 0)) / (2 * h);
      const ux = (c(0, 1, 0) - c(0, -1, 0)) / (2 * h), uy = (c(0, 0, 1) - c(0, 0, -1)) / (2 * h);
      const lap = (c(0, 1, 0) + c(0, -1, 0) + c(0, 0, 1) + c(0, 0, -1) - 4 * U[i]) / (h * h);
      const gp = i === 0 ? (d(p, 0, 1, 0) - d(p, 0, -1, 0)) / (2 * h) : (d(p, 0, 0, 1) - d(p, 0, 0, -1)) / (2 * h);
      worst = Math.max(worst, Math.abs(ut + U[0] * ux + U[1] * uy + gp - nu * lap));
    }
    const div = (d(u, 0, 1, 0)[0] - d(u, 0, -1, 0)[0] + d(u, 0, 0, 1)[1] - d(u, 0, 0, -1)[1]) / (2 * h);
    worstDiv = Math.max(worstDiv, Math.abs(div));
  }
  check('Taylor–Green momentum residual', worst < 1e-5, `max ${worst.toExponential(1)} (finite differences)`);
  check('Taylor–Green divergence', worstDiv < 1e-8, `max ${worstDiv.toExponential(1)}`);
}

// 2. Sliding layers: the particle path formula integrates X' = u(t, X).
{
  const nu = 0.25, a0 = 0.5, N = 1, y = 1.3, x0 = 0.4, T = 12;
  const steps = 12000, dt = T / steps;
  const f = t => a0 * Math.exp(-nu * N * N * t) * Math.sin(N * y);
  let x = x0;
  for (let k = 0; k < steps; k++) { const t = k * dt; x += dt / 6 * (f(t) + 4 * f(t + dt / 2) + f(t + dt)); }
  const exact = x0 + a0 / (nu * N * N) * (1 - Math.exp(-nu * N * N * T)) * Math.sin(N * y);
  check('sliding-layer particle path', Math.abs(x - exact) < 1e-10, `error ${Math.abs(x - exact).toExponential(1)}`);
}

// 3. Equal energies 2π³a² for N = 1 and N = 2, and the energy identity dE/dt = −ν∫|∇u|².
{
  const a = 0.5, M = 512;
  const E = N => { let s = 0; for (let j = 0; j < M; j++) s += Math.sin(N * TAU * j / M) ** 2; return 0.5 * a * a * s / M * TAU ** 3; };
  const grad2 = N => { let s = 0; for (let j = 0; j < M; j++) s += (a * N * Math.cos(N * TAU * j / M)) ** 2; return s / M * TAU ** 3; };
  check('energy N = 1 equals 2π³a²', Math.abs(E(1) - 2 * Math.PI ** 3 * a * a) < 1e-9, E(1).toFixed(6));
  check('energy N = 2 equals 2π³a²', Math.abs(E(2) - 2 * Math.PI ** 3 * a * a) < 1e-9, E(2).toFixed(6));
  for (const N of [1, 2]) check(`∫|∇u|² = 2N²E for N = ${N}`, Math.abs(grad2(N) - 2 * N * N * E(N)) < 1e-9, 'so E(t) = E(0) exp(−2νN²t)');
}

// 4. Eight samples cannot tell sin y from −sin 7y; with N ≤ 3 they determine a and N.
{
  let worst = 0;
  for (let j = 0; j < 8; j++) { const y = TAU * j / 8; worst = Math.max(worst, Math.abs(Math.sin(y) + Math.sin(7 * y))); }
  check('sin(y_j) = −sin(7 y_j) on 8 points', worst < 1e-14, `max gap ${worst.toExponential(1)}`);
  const vec = N => Array.from({ length: 8 }, (_, j) => Math.sin(N * TAU * j / 8));
  const dot = (p, q) => p.reduce((s, v, i) => s + v * q[i], 0);
  let ortho = 0;
  for (const m of [1, 2, 3]) for (const n of [1, 2, 3]) ortho = Math.max(ortho, Math.abs(dot(vec(m), vec(n)) - (m === n ? 4 : 0)));
  check('N = 1, 2, 3 are orthogonal on the grid', ortho < 1e-12, 'so samples recover a and N');
}

// 0. The intro's example: T(x) = x + 1 and f(x) = x². The starts +2 and −2 share f, not f∘T.
check('±2 share x² = 4, then x² = 9 and 1', (2) ** 2 === 4 && (-2) ** 2 === 4 && (2 + 1) ** 2 === 9 && (-2 + 1) ** 2 === 1, 'the square forgets the sign');

// ---------- Part two: the published results ----------

// 5. Scaling arithmetic quoted from OpenAI, "Finite time blowup for Navier–Stokes", §2.1 and §3.5:
//    ℓr ≍ τ^½, ℓz ≍ τ^(½−h), speed ≍ τ^(−½−h), so core energy ≍ volume·speed² = τ^(½−3h)
//    and core dissipation ≍ τ^(−½−3h), integrable in τ when h < 1/6. The film uses h = 0.005 (< 1/100).
{
  const h = 0.005;
  const eVol = 2 * 0.5 + (0.5 - h), eSpeed = -0.5 - h; // volume ≍ ℓr²·ℓz
  check('core volume exponent 3/2 − h', Math.abs(eVol - (1.5 - h)) < 1e-15, `${eVol}`);
  check('core energy exponent ½ − 3h > 0', Math.abs(eVol + 2 * eSpeed - (0.5 - 3 * h)) < 1e-15 && 0.5 - 3 * h > 0, `${(eVol + 2 * eSpeed).toFixed(3)}`);
  const eDiss = eVol + 2 * (eSpeed - 0.5); // squared radial derivative ≍ (speed/ℓr)²
  check('core dissipation exponent −½ − 3h > −1 (integrable)', Math.abs(eDiss - (-0.5 - 3 * h)) < 1e-15 && eDiss > -1, `${eDiss.toFixed(3)}`);
  const tau = 1e-4;
  check('at τ = 10⁻⁴ speed ×100+, core energy → ~1%', tau ** eSpeed > 100 && tau ** (0.5 - 3 * h) < 0.02, `speed ${(tau ** eSpeed).toFixed(1)}, energy ${(tau ** (0.5 - 3 * h)).toFixed(4)}`);
}

// 6. A vortex squeezed by hand (teaching example, not the paper's flow): the Lamb–Oseen profile
//    u_θ = Γ/(2πr)·(1 − exp(−r²/(4ντ))) run with τ = 1 − t shrinking. With p balancing u_θ²/r,
//    the only residual is azimuthal: R_θ = ∂t u_θ − ν(∂rr + ∂r/r − 1/r²)u_θ = Γ r e^{−r²/(4ντ)}/(4πντ²),
//    whose maximum grows like τ^(−3/2).
{
  const G = 1, nu = 0.05;
  const uth = (r, t) => G / (TAU * r) * (1 - Math.exp(-r * r / (4 * nu * (1 - t))));
  const Rex = (r, t) => { const tau = 1 - t; return G * r * Math.exp(-r * r / (4 * nu * tau)) / (2 * TAU * nu * tau * tau); };
  let worst = 0;
  for (const t of [0, 0.5, 0.9]) for (const r of [0.05, 0.2, 0.5, 1.0]) {
    const hr = 1e-4 * Math.max(r, 0.1), ht = 1e-6;
    const ut = (uth(r, t + ht) - uth(r, t - ht)) / (2 * ht);
    const urr = (uth(r + hr, t) - 2 * uth(r, t) + uth(r - hr, t)) / (hr * hr);
    const ur = (uth(r + hr, t) - uth(r - hr, t)) / (2 * hr);
    const R = ut - nu * (urr + ur / r - uth(r, t) / (r * r));
    worst = Math.max(worst, Math.abs(R - Rex(r, t)) / (Math.abs(Rex(r, t)) + 1));
  }
  check('squeezed-vortex residual formula', worst < 1e-4, `max rel. gap ${worst.toExponential(1)} (finite differences)`);
  const peak = tau => Rex(Math.sqrt(2 * nu * tau), 1 - tau);
  const slope = Math.log(peak(1e-4) / peak(1e-2)) / Math.log(1e-4 / 1e-2);
  check('its peak grows like τ^(−3/2)', Math.abs(slope + 1.5) < 1e-12, `slope ${slope.toFixed(6)}`);
}

// 7. An exact shearing wave (Kelvin; Craik–Criminale on affine flows): background U = (S y, 0),
//    wave w = A(t)(−k_y, k_x)/|k| sin(k_x x + k_y(t) y), k_y(t) = k_y0 − S k_x t,
//    A(t) = A0 |k(0)|/|k(t)| · exp(−ν∫|k|²). U + w solves 2D Navier–Stokes with the pressure
//    p = 2 S A k_x²/|k|³ · cos(k·x) that the tilting requires (Δp = −2S ∂x w₂). The wave's
//    self-interaction (w·∇)w vanishes because its velocity is perpendicular to k.
{
  const S = 1, nu = 0.004, kx = 1, ky0 = 6, A0 = 0.05;
  const ky = t => ky0 - S * kx * t;
  const K2int = t => kx * kx * t + ky0 * ky0 * t - ky0 * S * kx * t * t + S * S * kx * kx * t ** 3 / 3;
  const amp = t => A0 * Math.hypot(kx, ky0) / Math.hypot(kx, ky(t)) * Math.exp(-nu * K2int(t));
  const vel = (t, x, y) => {
    const k = Math.hypot(kx, ky(t)), s = Math.sin(kx * x + ky(t) * y), A = amp(t);
    return [S * y - A * ky(t) / k * s, A * kx / k * s];
  };
  const pres = (t, x, y) => { const k = Math.hypot(kx, ky(t)); return 2 * S * amp(t) * kx * kx / k ** 3 * Math.cos(kx * x + ky(t) * y); };
  const h = 1e-3;
  let worst = 0, worstDiv = 0;
  for (let n = 0; n < 200; n++) {
    const t = 12 * rnd(), x = TAU * rnd(), y = TAU * rnd();
    const U = vel(t, x, y);
    for (let i = 0; i < 2; i++) {
      const c = (dt, dx, dy) => vel(t + dt * h, x + dx * h, y + dy * h)[i];
      const ut = (c(1, 0, 0) - c(-1, 0, 0)) / (2 * h), ux = (c(0, 1, 0) - c(0, -1, 0)) / (2 * h), uy = (c(0, 0, 1) - c(0, 0, -1)) / (2 * h);
      const lap = (c(0, 1, 0) + c(0, -1, 0) + c(0, 0, 1) + c(0, 0, -1) - 4 * U[i]) / (h * h);
      const gp = i === 0 ? (pres(t, x + h, y) - pres(t, x - h, y)) / (2 * h) : (pres(t, x, y + h) - pres(t, x, y - h)) / (2 * h);
      worst = Math.max(worst, Math.abs(ut + U[0] * ux + U[1] * uy + gp - nu * lap));
    }
    const div = (vel(t, x + h, y)[0] - vel(t, x - h, y)[0] + vel(t, x, y + h)[1] - vel(t, x, y - h)[1]) / (2 * h);
    worstDiv = Math.max(worstDiv, Math.abs(div));
  }
  check('shearing wave solves NS (with its pressure)', worst < 2e-5, `max residual ${worst.toExponential(1)} (finite differences)`);
  check('shearing wave is divergence-free', worstDiv < 1e-6, `max ${worstDiv.toExponential(1)}`);
  let tPeak = 0, aPeak = 0;
  for (let t = 0; t <= 40; t += 0.01) if (amp(t) > aPeak) { aPeak = amp(t); tPeak = t; }
  check('the wave grows, then decays', aPeak > 3 * A0 && amp(40) < A0, `peak ×${(aPeak / A0).toFixed(2)} at t = ${tPeak.toFixed(2)}, ×${(amp(40) / A0).toFixed(3)} at t = 40`);
  // after the peak, the tilt (|k(0)|/|k(t)|) undoes most of the growth; viscosity only finishes it
  const geo = Math.hypot(kx, ky(6)) / Math.hypot(kx, ky(12)), visc = Math.exp(-nu * (K2int(12) - K2int(6)));
  check('from t = 6 to 12 the decay is mostly the tilt, not viscosity', geo < 0.2 && visc > 0.7, `tilt factor ${geo.toFixed(3)}, viscous factor ${visc.toFixed(3)}`);
}

// 8. A wave with zero mean can carry a nonzero mean momentum flux: for w = a cos(ξ·x), a·ξ = 0,
//    ⟨w⟩ = 0 and ⟨w ⊗ w⟩ = ½ a ⊗ a. Two such families span a cone; a target inside it has c1, c2 > 0.
{
  const a = [0.8, -0.6], M = 4096;
  let m0 = 0, m11 = 0, m12 = 0, m22 = 0;
  for (let j = 0; j < M; j++) { const c = Math.cos(TAU * j / M + 0.3); m0 += c / M; m11 += a[0] * a[0] * c * c / M; m12 += a[0] * a[1] * c * c / M; m22 += a[1] * a[1] * c * c / M; }
  const ok = Math.abs(m0) < 1e-14 && Math.abs(m11 - a[0] * a[0] / 2) < 1e-14 && Math.abs(m12 - a[0] * a[1] / 2) < 1e-14 && Math.abs(m22 - a[1] * a[1] / 2) < 1e-14;
  check('⟨w⟩ = 0 and ⟨w⊗w⟩ = ½ a⊗a', ok, `⟨w₁w₂⟩ = ${m12.toFixed(4)}`);
  const v1 = [1, 0.25], v2 = [0.3, 1], T = [0.9, 0.8];
  const det = v1[0] * v2[1] - v2[0] * v1[1];
  const c1 = (T[0] * v2[1] - v2[0] * T[1]) / det, c2 = (v1[0] * T[1] - T[0] * v1[1]) / det;
  check('target stress inside the cone: c1, c2 > 0', c1 > 0 && c2 > 0 && Math.abs(c1 * v1[0] + c2 * v2[0] - T[0]) < 1e-14, `c1 = ${c1.toFixed(3)}, c2 = ${c2.toFixed(3)}`);
}

// 9. A box stretched by λ1, λ2, λ3 with λ1λ2λ3 = 1 along x(s) = diag(λᵢ^s) x0 is carried by the
//    velocity v = diag(log λᵢ) x, whose divergence Σ log λᵢ = 0: volume is preserved at every s.
{
  const lam = [2, 0.5 * 1.25, 1 / 1.25];
  const prod = lam[0] * lam[1] * lam[2];
  const div = lam.reduce((s, l) => s + Math.log(l), 0);
  let worst = 0;
  for (let s = 0; s <= 1; s += 0.05) worst = Math.max(worst, Math.abs(lam.reduce((p, l) => p * l ** s, 1) - 1));
  check('box map: determinant one along the whole path', Math.abs(prod - 1) < 1e-15 && Math.abs(div) < 1e-15 && worst < 1e-14, `max |volume − 1| ${worst.toExponential(1)}`);
}

process.exitCode = failed ? 1 : 0;
