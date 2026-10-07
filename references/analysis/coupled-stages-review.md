# Independent review of the reverse pair and three-direction cycle

8 September 2026. Two bounded written calculations passed separate
AI-agent mathematical review. The coordinating agent reviewed the reverse
pair, written by the stage-audit agent. The stage-audit agent independently
reviewed the three-direction cycle, written by the coordinating agent.
Neither is external expert acceptance, a formal PDE certificate or a
Navier–Stokes solution. ROOT, E-prime and FORCED-D remain OPEN.

The exact mathematical sources reviewed were:

| Source | Reviewed SHA-256 |
|---|---|
| [Reverse pair](twoway-forced-coupling.md) | `476d3b1e2fe6a75f2195ca89ae620af4ad02f58a18162e01ade9feae15edc671` |
| [Three-direction cycle](cyclic-forced-coupling.md) | `dfd296914108f3c957363082e956c5106d98dabf03e68e216afdac1b2e56ee8e` |
| [Shared exact controls](checks/check-coupled-stages.py) | `097f69a2df45555ef57f57cb7eacdf877804db86c8e39c40626509a0ccf87d9b` |

Subsequent introductory review labels and links may change the current
source hashes; they do not alter the equations reviewed here. The reverse
source hash above already includes correction of a literal introductory
link/word separator typo. No mathematical correction was requested.

## Reverse-pair review

The coordinating agent independently checked the complete calculation:

- The added x3-dependent wave closes the E31/E13 gradient loop; its
  actual central eigenvalues and loop-product history are correct. The
  old and reverse wave use their different ordinary-viscosity histories.
- The full interaction pressure and both remaining force components
  give curl f in the second direction equal to
  ab(kappa^2-ell^2)sin(kappa x1)sin(ell x3). Equal frequencies cancel the
  interior force at one time, not throughout a positive-length flight.
- The coupled particle labels, sufficient material core and actual
  receiving-covector equation retain the large shear terms. Neither
  background-transported phase is called an actual transported phase
  of the complete two-wave velocity.
- The compact reverse curl and all three components of its linear
  residual have the correct signs, including the +8lambda pressure
  correction. The complete periodic force includes every old/new
  interaction and the spatial cutoff of the interaction pressure.
- The mixed-derivative bound includes Eulerian phase differentiation,
  ordinary viscosity, inverse covectors, activation, and the additional
  time-derivative factor at resonance. A small frequency mismatch
  does not multiply every time derivative.
- The specified phase rectangle proves the pressure-independent C0
  and C1 force bounds. At equal frequency q*, the exact Eulerian curl
  derivative is -8lambda ab q*^2 times the sine product, proving the
  componentwise mixed-force bound at least 4lambda P.
- The whole-flight mismatch bound and the conditional heat/loop-clock
  calculation give the constants and powers stated in equation (26).
  The latter conclusion uses all of its explicit hypotheses.

The scope is necessary: the interior perturbation is planar despite
its two-way coupling and the three-dimensional compact full field. The
reverse wave is supplied and its prescribed velocity amplitude decays.
The stated force lower bounds concern the unchanged selected velocity,
a surviving flat phase rectangle and the stated measurement/activation
conditions. A new nonlinear velocity completion can change that force.
The planar vorticity maximum principle is not used to prove a global
theorem for the compact periodic construction. No arbitrary-error
propagator bound follows from the central spectrum.

## Three-direction cycle review

The stage-audit agent independently checked the full written source:

- Substitution into ordinary NS gives all three displayed cross-force
  components. Their divergence is zero and the interaction has no
  interior Poisson source. The periodic construction retains a specified
  old pressure and its force, rather than assuming this local pressure
  observation eliminates global cutoff terms.
- The characteristic polynomial includes the cubic cycle product P.
  The exact law is P'=-nu(kappa^2+ell^2+m^2)P; the magnitudes of the
  three supplied edges therefore do not grow their product. The
  missing reverse-edge gradient is exactly S^2.
- Positive diagonal balancing yields the stated instantaneous eigenvalue
  bound. It may be ill-conditioned and time-dependent. The source
  explicitly does not turn it into an arbitrary-error or propagator bound.
- All compact curl signs are correct. The full physical force identity
  and its finite mixed-order bound include viscosity, older-state
  interactions, Eulerian phase derivatives, cutoffs and activation.
- On each of the three specified rectangles the transverse force
  component vanishes. Dividing the circulation by its actual perimeter
  gives the factor 1/2. Their geometric mean is precisely V_g g.
  V_g is the geometric mean of wave amplitudes, not the full velocity
  norm; unbalanced waves are not excluded by that bound.

The source correctly restricts every lower bound to the unchanged fields
and the actual loop geometry. It does not claim that exterior corrections
which leave those fields unchanged can remove the interior circulation,
or that velocity corrections changing the interior are forbidden. The
three supplied Kelvin profiles do not constitute an autonomous nonlinear
amplifier after their cross force is deleted.

## Exact controls and remaining limits

The stage-audit agent separately reproduced the cycle's full NS residual,
divergence, characteristic polynomial, reverse-edge gradient, product
dissipation, curl signs and all three transverse loop cancellations by
exact symbolic calculation. The reverse author separately checked its
complete NS residual, pressure, curl, resonance time derivative and all
localized reverse-residual components.

The shared script above was also executed successfully. Its two groups
check the reverse pressure/resonance calculation and the genuine cycle,
including omitted-feedback controls. This is exact finite algebra,
not research DNS. The support, product estimates, continuation scope
and pressure-independent loop arguments remain written analytic inputs.

Both calculations expose costs in concrete finite architectures. Neither
establishes a common infinite sequence, an admissible terminal force,
new original-data compatibility, a nonlinear next-host theorem, or a
general obstruction to other full three-dimensional couplings.
