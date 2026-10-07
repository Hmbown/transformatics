# Three-dimensional fluid laboratory

Evolve a three-dimensional velocity field on the periodic cube $[0,2\pi)^3$. This finite Fourier model approximates unforced incompressible Navier–Stokes; the visible particles follow its computed velocity.

<link rel="stylesheet" href="../assets/fluid/lab.css">
<div class="fluid-lab" id="fluid-lab">
<div class="fluid-controls">
<label>Initial field<select name="preset"><option value="taylor-green">Taylor–Green vortex</option><option value="abc">ABC Beltrami field</option><option value="shear">Sinusoidal shear</option></select></label>
<label>Grid<select name="grid"><option value="16">16 × 16 × 16</option><option value="32">32 × 32 × 32</option></select></label>
<label>Viscosity ν<input name="viscosity" type="number" min="0" max="1" step="0.01" value="0.03"></label>
<button type="button" data-play aria-pressed="false">Play</button>
<button type="button" data-step>One step</button>
<button type="button" data-reset>Reset</button>
<button type="button" data-rotate>Rotate view</button>
</div>
<canvas role="img" aria-label="Projected three-dimensional periodic cube showing passive tracers of the computed velocity. Warmer colors indicate greater speed. Numerical diagnostics follow."></canvas>
<dl class="fluid-diagnostics">
<div><dt>Simulation time</dt><dd data-value="time">0</dd></div>
<div><dt>Kinetic energy</dt><dd data-value="energy">—</dd></div>
<div><dt>Enstrophy</dt><dd data-value="enstrophy">—</dd></div>
<div><dt>RMS divergence</dt><dd data-value="divergence">—</dd></div>
<div><dt>Last time step</dt><dd data-value="dt">—</dd></div>
<div><dt>Completed steps</dt><dd data-value="steps">0</dd></div>
</dl>
<p class="fluid-status" data-status role="status">Preparing the numerical field…</p>
</div>
<script type="module" src="../assets/fluid/lab.js"></script>

The run starts paused. Changed settings take effect when you select **Reset**. Select **One step** to inspect a single update, or **Play** to continue. The periodic faces identify opposite sides of the cube: a tracer crossing a face reappears at its matching face. Rotate changes only the camera. Simulation time advances independently of your device’s display speed.

## What the solver computes

For each retained nonzero Fourier wavevector $k$, the velocity is projected onto the plane perpendicular to $k$:

$$
\mathbb P_k v=v-k\frac{k\cdot v}{|k|^2}.
$$

The nonlinear term is evaluated as $\mathbb P(u\times\omega)$, where $\omega=\nabla\times u$. This equals the usual projected transport term $-\mathbb P[(u\cdot\nabla)u]$; the gradient difference is absorbed by pressure. Projection therefore retains incompressibility and the nonlocal pressure contribution rather than deleting pressure from the equation.

The Fourier transform uses double-precision arithmetic. A strict two-thirds cutoff retains modes with $3|k_i|<N$ in each coordinate; Nyquist modes and the mean are zeroed. The quadratic product is evaluated on the grid and projected back to that retained band. An integrating-factor Heun step handles viscous decay exactly in each Fourier mode and treats the nonlinear evolution to second order. Its advective time step is limited by the computed maximum speed. This is a numerical stability precaution, not a convergence theorem for every trajectory.

The reported quantities use volume averages:

$$
E=\tfrac12\langle|u|^2\rangle,\qquad
Z=\tfrac12\langle|\omega|^2\rangle,\qquad
D_{\rm div}=\langle|\nabla\cdot u|^2\rangle^{1/2}.
$$

For a smooth unforced solution, $dE/dt=-2\nu Z$. A finite time step need not satisfy that identity exactly. RMS divergence tests the supplied Fourier field after projection; it is not a test of temporal accuracy. The tracers use periodic trilinear interpolation and a predictor–corrector update, so their paths also have interpolation and time-step errors.

## An exact check you can recognize

The ABC preset is

$$
u_0=(\sin z+\cos y,\;\sin x+\cos z,\;\sin y+\cos x).
$$

Here $\nabla\times u_0=u_0$ and $\Delta u_0=-u_0$. Consequently the projected nonlinearity vanishes and the exact solution is $u(t)=e^{-\nu t}u_0$. Both energy and enstrophy start at $3/2$ and decay as $(3/2)e^{-2\nu t}$. Use this field to distinguish a numerical implementation check from an unknown turbulent evolution.

## Experiment: compare resolutions

Run Taylor–Green at viscosity $0.03$, first on the 16³ grid and then on 32³. Pause at similar simulation times and compare energy and enstrophy. Agreement at early times is useful evidence; later disagreement means the retained scales or time accuracy need investigation. Neither a busy tracer image nor an increasing enstrophy value diagnoses a singularity.

The [finite amplification chapter](viscous.md) studies specially prepared localized data and rigorously controlled errors. These presets do not instantiate that construction. This laboratory can help inspect velocity, vorticity, dissipation, and resolution dependence; it does not certify those theorems, infinite transfer, global regularity, or blow-up. Future theorem-specific experiments need their own matched initial data and quantitative error bounds.

## Connecting a proved result to the simulator

A theorem becomes a computational guarantee through an error estimate.
For example, if a proof supplies a solution bound for a specified datum,
viscosity, domain and time interval, an accompanying numerical analysis
must bound the discarded Fourier modes and accumulated time-step error.
The simulator could then report an error bound for velocity or energy
over that interval, with the assumptions and theorem reference attached.
An existence or regularity theorem alone does not choose a sufficient grid.

That is the planned theorem-backed mode. It requires a verified theorem,
a reproducible initial field satisfying its hypotheses, and a validated
numerical error bound. The current laboratory supplies the numerical
solver and exact-solution checks; those additional guarantees are open.

The [original-time handover theorem](../../references/navier-stokes/original-nonlinear-handover.md)
now provides a finite analytic example with both supplied waves in the initial
data. Its sufficiently small scale threshold is existential, and these browser
presets do not reproduce its field. Using that theorem for a guaranteed numerical
run still requires effective constants, a matching datum and a proved grid/time
error bound. The new theorem does not certify the current 16³ or 32³ runs.

The local numerical checks cover Fourier identities, divergence projection, exact Beltrami decay, and refinement of a short nonlinear step. They can be replayed from [the check source](../assets/fluid/checks.js) with Node using `node notes/assets/fluid/checks.js` in the repository.
