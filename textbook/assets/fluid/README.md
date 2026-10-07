# Periodic incompressible fluid lab

Browser entry: `lab.js`; dedicated module worker: `worker.js`; numerical core: `solver.js`; request identity gate: `protocol.js`. The textbook chapter provides the accessible controls and includes `lab.css`. Serve over HTTP(S); no network service or remote compute is used by the lab itself.

Run local checks with `node textbook/assets/fluid/checks.js` (Node 18+). No npm dependencies. Checks compare FFT against direct DFT, recover a 3D transform, check exact spectral projection and mask, verify ABC energy decay at N=16 and N=32, compare Taylor–Green step refinements, and exercise periodic sampling and the worker protocol.

The grid spans [0,2π)^3; all diagnostics are volume-averaged. Kinetic energy and enstrophy include the factor 1/2. The forward transform is unnormalized and the inverse divides by N per axis. Fields are mean-zero; the componentwise cutoff is strict 3|k_i|<N, removing Nyquist planes. This avoids quadratic aliasing into the retained band. Pressure is accounted for by the Fourier Leray projector. Viscosity is exact for the linear heat part; nonlinear time integration remains approximate.

The worker emits actual field diagnostics and advected tracer positions. It never sends decorative synthetic velocity to the renderer. Tracer trajectories use old-field prediction and a new-field correction with periodic trilinear interpolation. Tracer density is not a quantitative fluid observable.

The time step is min(0.025, 0.22 Δx/max|u|). Non-finite results and a coarse large-growth guard stop the run and require reset; neither condition detects a PDE singularity. No adaptive spatial refinement or rigorous error estimator is provided. The tutorial presets are not the specialized Gavrilov/packet construction, and no theorem-specific or global NS claim follows from these finite grids.

Worker requests carry a generation and request ID. Settings changes/reset invalidate old generations; stale replies cannot update diagnostics or clear a current request. The protocol checks include reset-over-step races, repeated resets, duplicate responses, and tagged numerical errors. Pause and tab hiding stop future scheduling while allowing an already-running step to finish visibly as paused.
