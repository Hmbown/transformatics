// Fourier convention: forward unnormalized, inverse divided by N in each axis.
export function fft(re, im, inverse = false) {
  const n = re.length;
  if (n < 1 || n & (n - 1)) throw Error("FFT length must be a power of two");
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) {
      [re[i], re[j]] = [re[j], re[i]];
      [im[i], im[j]] = [im[j], im[i]];
    }
  }
  for (let len = 2; len <= n; len <<= 1) {
    const a = ((inverse ? 2 : -2) * Math.PI) / len,
      wr0 = Math.cos(a),
      wi0 = Math.sin(a);
    for (let i = 0; i < n; i += len) {
      let wr = 1,
        wi = 0;
      for (let j = 0; j < len / 2; j++) {
        const p = i + j,
          q = p + len / 2,
          tr = wr * re[q] - wi * im[q],
          ti = wr * im[q] + wi * re[q];
        re[q] = re[p] - tr;
        im[q] = im[p] - ti;
        re[p] += tr;
        im[p] += ti;
        const t = wr * wr0 - wi * wi0;
        wi = wr * wi0 + wi * wr0;
        wr = t;
      }
    }
  }
  if (inverse)
    for (let i = 0; i < n; i++) {
      re[i] /= n;
      im[i] /= n;
    }
}
// Flattened layout: index(x,y,z)=(x*N+y)*N+z. Each pass gathers
// one axis into scratch arrays, transforms it, then scatters it back.
function lineIndex(axis, j, p, q, n) {
  if (axis === 0) return (j * n + p) * n + q;
  if (axis === 1) return (p * n + j) * n + q;
  return (p * n + q) * n + j;
}

export function fft3(re, im, n, inverse = false) {
  const r = new Float64Array(n),
    a = new Float64Array(n);
  for (let axis = 0; axis < 3; axis++)
    for (let p = 0; p < n; p++)
      for (let q = 0; q < n; q++) {
        for (let j = 0; j < n; j++) {
          const idx = lineIndex(axis, j, p, q, n);
          r[j] = re[idx];
          a[j] = im[idx];
        }
        fft(r, a, inverse);
        for (let j = 0; j < n; j++) {
          const idx = lineIndex(axis, j, p, q, n);
          re[idx] = r[j];
          im[idx] = a[j];
        }
      }
}
const complexArray = (m) => ({
  re: new Float64Array(m),
  im: new Float64Array(m),
});
const cloneSpectrum = (a) =>
  a.map((v) => ({ re: v.re.slice(), im: v.im.slice() }));
export class Fluid {
  constructor(n = 16, nu = 0.03, preset = "taylor-green") {
    if (![16, 32].includes(n)) throw Error("Supported grids: 16 and 32");
    if (!Number.isFinite(nu) || nu < 0)
      throw Error("Viscosity must be nonnegative");
    this.n = n;
    this.m = n ** 3;
    this.nu = nu;
    this.time = 0;
    this.lastDt = 0;
    this.steps = 0;
    this.k = Array.from({ length: 3 }, () => new Int16Array(this.m));
    this.k2 = new Int16Array(this.m);
    this.keep = new Uint8Array(this.m);
    for (let x = 0; x < n; x++)
      for (let y = 0; y < n; y++)
        for (let z = 0; z < n; z++) {
          const i = (x * n + y) * n + z,
            ks = [x, y, z].map((j) => (j < n / 2 ? j : j - n));
          for (let c = 0; c < 3; c++) this.k[c][i] = ks[c];
          this.k2[i] = ks.reduce((s, k) => s + k * k, 0);
          this.keep[i] = ks.every((k) => 3 * Math.abs(k) < n) ? 1 : 0;
        }
    this.u = Array.from({ length: 3 }, () => complexArray(this.m));
    for (let x = 0; x < n; x++)
      for (let y = 0; y < n; y++)
        for (let z = 0; z < n; z++) {
          const i = (x * n + y) * n + z,
            X = (2 * Math.PI * x) / n,
            Y = (2 * Math.PI * y) / n,
            Z = (2 * Math.PI * z) / n;
          let v;
          if (preset === "abc")
            v = [
              Math.sin(Z) + Math.cos(Y),
              Math.sin(X) + Math.cos(Z),
              Math.sin(Y) + Math.cos(X),
            ];
          else if (preset === "shear") v = [Math.sin(Z), 0, 0];
          else
            v = [
              Math.sin(X) * Math.cos(Y) * Math.cos(Z),
              -Math.cos(X) * Math.sin(Y) * Math.cos(Z),
              0,
            ];
          v.forEach((v, c) => (this.u[c].re[i] = v));
        }
    for (const v of this.u) fft3(v.re, v.im, n);
    this.project(this.u);
    this.physical = this.toPhysical(this.u);
  }
  // P_k = I - k⊗k/|k|². Masking precedes projection; zero mean is retained.
  project(a) {
    for (let i = 0; i < this.m; i++) {
      const k2 = this.k2[i];
      if (!this.keep[i] || !k2) {
        for (const v of a) v.re[i] = v.im[i] = 0;
        continue;
      }
      let dr = 0,
        di = 0;
      for (let c = 0; c < 3; c++) {
        dr += this.k[c][i] * a[c].re[i];
        di += this.k[c][i] * a[c].im[i];
      }
      for (let c = 0; c < 3; c++) {
        a[c].re[i] -= (this.k[c][i] * dr) / k2;
        a[c].im[i] -= (this.k[c][i] * di) / k2;
      }
    }
    return a;
  }
  toPhysical(a) {
    return a.map((v) => {
      const r = v.re.slice(),
        im = v.im.slice();
      fft3(r, im, this.n, true);
      return r;
    });
  }
  // Spectral curl is i k × û; no finite-difference derivative is used.
  curlSpectrum(a) {
    const curl = Array.from({ length: 3 }, () => complexArray(this.m));
    for (let i = 0; i < this.m; i++)
      for (let c = 0; c < 3; c++) {
        const d = (c + 1) % 3,
          e = (c + 2) % 3;
        curl[c].re[i] = -(
          this.k[d][i] * a[e].im[i] -
          this.k[e][i] * a[d].im[i]
        );
        curl[c].im[i] = this.k[d][i] * a[e].re[i] - this.k[e][i] * a[d].re[i];
      }
    return curl;
  }

  // Rotational form: -P[(u·∇)u] = P[u×ω]. Project the product
  // back to the strict two-thirds band to remove quadratic aliases.
  nonlinear(a) {
    const physical = this.toPhysical(a);
    const w = this.toPhysical(this.curlSpectrum(a)),
      out = Array.from({ length: 3 }, () => complexArray(this.m));
    for (let i = 0; i < this.m; i++)
      for (let c = 0; c < 3; c++) {
        const d = (c + 1) % 3,
          e = (c + 2) % 3;
        out[c].re[i] = physical[d][i] * w[e][i] - physical[e][i] * w[d][i];
      }
    for (const v of out) fft3(v.re, v.im, this.n);
    return this.project(out);
  }
  maxSpeed() {
    let max = 0;
    for (let i = 0; i < this.m; i++)
      max = Math.max(max, Math.hypot(...this.physical.map((v) => v[i])));
    return max;
  }
  // Integrating-factor Heun: E=exp(-ν|k|²dt),
  // predictor E(u+dt F(u)), corrector Eu+dt/2(EF(u)+F(predictor)).
  // This gives exact heat decay and second-order explicit nonlinear evolution.
  step(requestedDt = Infinity) {
    const speed = this.maxSpeed(),
      dt = Math.min(
        requestedDt,
        0.025,
        (0.22 * ((2 * Math.PI) / this.n)) / Math.max(speed, 1e-10),
      );
    if (!(dt > 0) || !Number.isFinite(dt)) throw Error("Invalid time step");
    const f0 = this.nonlinear(this.u),
      pred = cloneSpectrum(this.u);
    for (let i = 0; i < this.m; i++) {
      const E = Math.exp(-this.nu * this.k2[i] * dt);
      for (let c = 0; c < 3; c++) {
        pred[c].re[i] = E * (this.u[c].re[i] + dt * f0[c].re[i]);
        pred[c].im[i] = E * (this.u[c].im[i] + dt * f0[c].im[i]);
      }
    }
    this.project(pred);
    const f1 = this.nonlinear(pred),
      next = cloneSpectrum(this.u);
    for (let i = 0; i < this.m; i++) {
      const E = Math.exp(-this.nu * this.k2[i] * dt);
      for (let c = 0; c < 3; c++) {
        next[c].re[i] =
          E * this.u[c].re[i] + 0.5 * dt * (E * f0[c].re[i] + f1[c].re[i]);
        next[c].im[i] =
          E * this.u[c].im[i] + 0.5 * dt * (E * f0[c].im[i] + f1[c].im[i]);
        if (!Number.isFinite(next[c].re[i]) || !Number.isFinite(next[c].im[i]))
          throw Error("Non-finite velocity; reset or reduce the time step");
      }
    }
    this.project(next);
    this.u = next;
    this.physical = this.toPhysical(next);
    this.time += dt;
    this.lastDt = dt;
    this.steps++;
    const diag = this.diagnostics();
    if (diag.energy > 100 || this.maxSpeed() > 100)
      throw Error(
        "Numerical growth limit reached; this is not a singularity diagnosis",
      );
    return diag;
  }
  // Periodic trilinear interpolation of the computed physical-grid velocity.
  sample(pos) {
    const n = this.n,
      coords = pos.map((v) => ((((v / (2 * Math.PI)) * n) % n) + n) % n),
      base = coords.map(Math.floor),
      f = coords.map((v, i) => v - base[i]),
      out = [0, 0, 0];
    for (let x = 0; x < 2; x++)
      for (let y = 0; y < 2; y++)
        for (let z = 0; z < 2; z++) {
          const w =
              (x ? f[0] : 1 - f[0]) *
              (y ? f[1] : 1 - f[1]) *
              (z ? f[2] : 1 - f[2]),
            i =
              (((base[0] + x) % n) * n + ((base[1] + y) % n)) * n +
              ((base[2] + z) % n);
          for (let c = 0; c < 3; c++) out[c] += w * this.physical[c][i];
        }
    return out;
  }
  // Parseval for an unnormalized forward transform: average |u|²
  // is sum |û|² / M². For solenoidal modes, |k×û|²=|k|²|û|².
  diagnostics() {
    let energy = 0,
      enstrophy = 0,
      div2 = 0;
    const norm = this.m ** 2;
    for (let i = 0; i < this.m; i++) {
      let dr = 0,
        di = 0;
      for (let c = 0; c < 3; c++) {
        const v = this.u[c],
          power = v.re[i] ** 2 + v.im[i] ** 2;
        energy += power;
        enstrophy += this.k2[i] * power;
        dr += this.k[c][i] * v.re[i];
        di += this.k[c][i] * v.im[i];
      }
      div2 += dr * dr + di * di;
    }
    return {
      time: this.time,
      dt: this.lastDt,
      steps: this.steps,
      energy: energy / (2 * norm),
      enstrophy: enstrophy / (2 * norm),
      divergence: Math.sqrt(div2 / norm),
      n: this.n,
    };
  }
}
