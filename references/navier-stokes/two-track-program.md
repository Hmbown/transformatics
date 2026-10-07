# Unforced and smoothly forced Navier–Stokes: two explicit targets

> **Source update — 8 September 2026.** OpenAI published the external forced-breakdown construction. See the [source assessment](openai-result-bridge.md). FORCED-D is **IMPORTED**; unforced ROOT and E-prime remain **OPEN**. Earlier FORCED-D labels below describe the local research before that publication.


**8 September 2026. Both tracks are authorized and OPEN.** The user has
explicitly asked to pursue both. A forced result must retain its own theorem
statement; it does not close the unforced ROOT by relabelling the equation.
The overall objective remains a complete verified Navier–Stokes result.

**Twelfth execution, 8 September (current):** the signed postfocus source
and its [full-flow band comparison](../analysis/actual-coarse-band.md)
passed independent AI-agent reviews and root reads. The same original-data
Q_h generates a measurable intermediate frequency band: endpoint velocity
and symmetric-strain lower scales are h^(7/4+o(1)) and h^(1/2+o(1)), above
its initial band tails. Exact q and linear-Z leakage are separately bounded.
The band is coarser than the supplied receiver. Its generated remainder
still has C1 norm at most C h^(1/96) and a vanishing current-window strain
clock; this supplies no automatic next host or infinite trajectory.

The [opposing/cyclic forced calculations](../analysis/coupled-stages-review.md)
retain the complete nonlinear force and all fixed mixed derivatives.
Instantaneous resonance cancellation leaves a nonzero force time jet;
the supplied cyclic-wave product dissipates and its omitted reverse
couplings are real. These restrictions allow changed interior velocities.

The [actual periodic cycle](../analysis/periodic-cycle-transfer.md)
now evolves those nonlinear interactions without forcing. Its full pressure
jets and uniform local remainder prove finite total enstrophy gain for
sufficiently small nu q/A, while kinetic energy decreases. This extends
the existing activation prototype, whose sine datum is a common translation
of the old cosine datum. No new architecture, large velocity gain or shape
return is asserted. The activation lesson teaches the pressure cancellation
and the finite-time gain inequality.

Next: useful later nonlinear feedback and an actual compatible next state,
with pressure, viscosity, localization and one-datum/terminal-force budgets.
Do not repeat the completed postfocus sign or first activation coefficient.
These are restricted written results, not formal PDE certificates or external
expert acceptance. ROOT, E-prime and FORCED-D remain OPEN. No new research
DNS or public release. The earlier checkpoints below are historical.

**Tenth execution:** the [logarithmic host](logarithmic-host.md)
now continues the same original unforced datum beyond its receiver focus,
with order-eta ell² rescaled strain and controlled nonlinear error for
small fixed eta. It supplies no next independent seed or infinite sequence.
The fixed-annulus forced exclusion below remains in force.

**Ninth execution:** the [fixed-annulus geometry](../analysis/fixed-annulus-obstruction.md)
is now excluded for a full compact axisymmetric NS breakdown with smooth
forcing. The [same unforced flow](../analysis/later-flow-attempt.md)
also has a reviewed short further lifetime and a transported almost-affine
core. These change the next tasks below; neither closes either global target.

## 1. The equations and completion conditions

In both tracks the ordinary three-dimensional incompressible equation is

    partial_t u+(u.grad)u+grad p=nu Delta u+f,
    div u=0, nu>0 fixed.

| Track | Input and target | What would establish it |
|---|---|---|
| Unforced ROOT | f=0; smooth periodic divergence-free initial data. | A complete global regularity proof, or a counterexample from one admissible smooth datum. The existing ROOT node is specifically the global regularity claim and remains OPEN. |
| FORCED-D | One smooth periodic divergence-free datum and one prescribed smooth periodic force, with every mixed derivative decaying faster than any power of time. | A proof that no global smooth periodic velocity and pressure solve that datum and force. Finite-time breakdown of the unique preterminal classical solution would suffice. |

The [official Fefferman statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf),
pp. 1–2, explicitly offers alternatives A–D. A/B use zero force; C/D permit
the specified forces in a breakdown example. Its appended erratum also
requires periodic pressure in the periodic setting. The two-pi period used
in this repository and Clay's unit period differ by a fixed consistent NS
rescaling, which preserves positive viscosity and smoothness.

We start the forced track with periodic alternative D, matching the existing
domain. Alternative C additionally requires rapid spatial decay of every
initial-data and force derivative on R3. A nonlocal pressure or Leray
projection can matter for that stronger spatial requirement; it cannot
be assumed away by copying a periodic argument.

For D it is sufficient to construct a force smooth on the entire closed
time interval through a proposed singular time, with a smooth extension
of compact support in time. Smoothness only on t<T is insufficient.
The force is prescribed data: if constructed from a candidate solution,
its complete extension and derivative bounds must be proved independently
of the candidate's singular limit.

## 2. Why forcing does not make breakdown automatic

For an explicit solenoidal velocity U and pressure P one can define

    f_U=partial_t U+(U.grad)U+grad P-nu Delta U.

That identity makes U a forced solution before any singular time. It
does not establish that f_U is admissible through that time. All its
space and time derivatives, including pressure and cutoff contributions,
belong to the proof.

For example, on the two-pi torus let U=a(t)sin(y)e1 and P=0. Its nonlinear
advection vanishes, and its exact force is

    f_U=[a'(t)+nu a(t)]sin(y)e1.

Setting a(t)=1/(T-t) makes both U and its force singular. Conversely,
if a'+nu a=g is smooth and bounded on a finite interval, then

    a(t)=exp(-nu t)a(0)+integral_0^t exp(-nu(t-s))g(s)ds

stays bounded there. This simple shear cannot furnish smooth-force
breakdown. A successful forced construction must use additional dynamics.

## 3. Work shared by the tracks

The [localized profile extension](localized-profile.md)
now supplies a finite actual NS region with nearly uniform gradient,
complete pressure, heat evolution and all Fourier correction modes.
Its error is controlled through a finite endpoint. The subsequent
[later-flow lemma](../analysis/later-flow-attempt.md)
extends that same solution by c ell^(-27/8), and preserves a transported
radius-c k core with rescaled gradient error O(ell^(-1/4)) for an additional
ell^(-5) interval. This is short persistence of existing strain, not a new
descendant or an infinite construction.

The [next-seed analysis](next-seed-analysis.md) proves that
the current full solution cannot develop dominant strain at the proposed
next scale h^(9/4) within its proved interval. The
[generated-source calculation](../analysis/generated-receiver.md)
shows that the leading cross source was already counted in the existing
handover. Fixed flat profiles also retain the full-support C3 seed cost.
Forcing may supply a different reset or seed; its cost then appears in
f and must pass the all-orders smoothness requirements.

## 4. What the forced review establishes

The three calculations have passed separate agent reviews at their stated
written scope. The [review record](../analysis/forced-stage-review.md)
includes the corrections and distinguishes them from a complete proof.

| Calculation | Established result | Remaining obligation |
|---|---|---|
| [Physical force and terminal extension](forced-admissibility.md) | The existing residual gives a small physical L1-time/L2-space force, h^(39/8-o(1)). A single sequence with summable bounds for every fixed mixed derivative has a smooth terminal extension. | The current estimates do not bound all physical force derivatives along an infinite construction. A diverging upper bound is inconclusive. |
| [Ordinary viscosity](forced-viscosity.md) | Reusing the released compact Euler velocity fails smooth NS forcing, even after a pressure change. In the fixed-background principal two-component wave equation, both channels instead undergo the same heat smoothing. | Prove the full viscous stage, including the changed older flow, lower-order drift, localization and force recovery. |
| [Finite reset](../analysis/forced-reset.md) | Smooth forcing can steer a finite solenoidal state exactly. Holding a shrinking fixed-shape compact core stationary has a genuine force lower bound proportional to nu times amplitude divided by radius squared. | A useful return must arise from evolving dynamics with its complete force controlled. Independent finite steering does not provide an infinite trajectory. |

For the promising principal identity, let n be a nonzero phase Fourier
index and D the integrated viscous clock. The two-component amplitude obeys

    R_NS,n(t)=exp(-n^2 D(t)) R_Euler,n(t).

Thus a selected central zero in the outgoing reduced-vorticity component
remains zero at principal order. For a general profile F, the retained
profile is exp(D partial_s^2)F, not a common scalar multiple of F. This
identity supplies a reason to attempt the viscous construction; it does
not prove that its complete return survives.

Ordinary NS breakdown with admissible smooth forcing must also have
unbounded velocity: a bounded velocity and finite force norms give an H1
continuation estimate. The released Euler construction's bounded-velocity
conclusion therefore cannot be retained in a successful NS adaptation.

## 5. Next work and its acceptance test

**Forced track:** choose a full flow that escapes the now-excluded compact
fixed-annulus axisymmetric geometry, then derive one complete viscous
insertion/return on a specified older state. The
[exact normalized equations and spatial commutator](../analysis/viscous-stage-attempt.md)
show that both scalar channels can use the same full diffusion operator,
but this alone does not preserve a spatial return. Axis approach requires
smooth Cartesian parity and its actual Reynolds/force budget; broken
symmetry requires the complete additional three-dimensional interactions.
Keep fixed physical viscosity, periodic pressure and every localization
term. A finite-order mixed-force estimate and nonempty velocity-gain margin
must precede any infinite common schedule. The
[gain audit](../analysis/force-gain-audit.md) prevents
double-counting inverse-frequency recovery or treating arbitrarily high
frequency on one fixed host as a free improvement.

**Unforced track:** use the proved logarithmic continuation to identify
a signed new independent receiving contribution on the full time-dependent
Q_h state. The full-solution frequency exclusion continues through this
longer interval; its small-coefficient strain clock is not an activation
theorem. The exact source still lacks a signed new-seed lower bound.
Any inherited seed requires the same original smooth datum and its full
derivative cost. Do not repeat the completed finite continuation estimate.


Neither track advances to an infinite construction by choosing a different
finite example for each derivative order.

No private internal-model proof is available as an input. Public mathematical
sources and their versioned statements remain the evidence. No publication
or complete proof claim follows from establishing this second target.
