# Response to the supplied agent report

8 September 2026. **Research advice audited; no new Navier–Stokes theorem.**

The report's useful recommendation is to examine continuation beyond the
present postfocus window while following the packet's changing frequencies
and spatial envelope. Its claimed ceiling and universal generation barrier
do not follow. Several load-bearing calculations are incorrect. We retain
the proposed longer window as a model target and require a new stability
estimate before drawing conclusions about the actual solution.

This assessment uses two separate AI-agent audits and root checks:
[cap arithmetic and stability](../analysis/external-cap-report-audit.md)
and [source statements and quantifiers](../analysis/external-report-source-audit.md).
These are independent model reviews, not external expert acceptance.
The supplied attachment is identified by SHA-256
489bb315142dec6839d3e313e05cdf3b7d5f1b2fa79de14e672dbc991d2f4e02.

## What survives the audit

The gradient-time clock is invariant under the program's physical rescaling.
The supplied carrier laws reproduce the order of the proved endpoint strain.
If those laws could be extended, balancing viscous damping against growth
would locate a cap at rescaled frequency of order h^(-2) and time of order
ell²/(2 mu), with ell=sqrt(log(1/h)). This calculation identifies a useful
question; it neither extends the actual solution nor establishes its cap.

The emphasis on seed preparation, all mixed force derivatives and one
admissible datum is sound. The repository already excludes particular
noncancelling preparations and forced geometries. Those restrictions are
not universal impossibility theorems.

## Corrections that change the recommendation

| Report claim | Audit finding |
|---|---|
| Relative error is preserved when its growth operator is controlled by packet strain. | False as an inference. A scalar error growing at that rate can outrun the packet by an exponential of its accumulated strain. |
| The cap strain has logarithmic factor ell^(-13/8). | Its displayed model gives ell^(-9/8). The leading h^(-1/2+o(1)) power survives conditionally. |
| The next-seed deficit is h^(-1+o(1)). | The displayed amplitude powers yield h^(-3/4+o(1)); logarithms cannot change that limiting power. Neither the supplied amplitude nor the receiving threshold is an actual cap-time theorem. |
| A Sobolev ceiling at derivative order 9/4 follows from the shrinking core. | The small region where a gradient is approximately affine is not the whole packet envelope. Substituting its volume does not give the global norm. |
| Core radius times frequency reaching one demonstrates geometric destruction at cap. | With the report's radius definition, that product equals one at every time. It does not diagnose the whole envelope. |
| Pressure and nonlinear feedback are already harmless at the proposed cap. | The necessary full stress, frequency support, propagated residual and derivative estimates have not been supplied on that interval. |
| The supplied-seed architecture is therefore ruled out generally. | The current preparation obstruction assumes a specified profile and disjoint or quantitatively noncancelling copies. It does not cover every inherited or generated state. |

There is also an exact error in the proposed Lean target. For the symmetric
trace-free matrix S=diag(2,-1,-1), tr(S³)=6 and |S|_F³=6 sqrt(6).
The report's coefficient 2/(3 sqrt(6)) gives the false inequality 6<=4.
The sharp cubic coefficient is 1/sqrt(6). The distinct Betchov prefactor
produces the repository's rate constant 4/(3 sqrt(6)).

The report's status table predates the reviewed postfocus and full-flow
band results. The finer-tail result uses the order: fix eta, beta and
desired power; choose finite proof indices; then take h sufficiently
small. It is not an infinite correction argument. All these results
retain their finite scope.

## The first estimate to attempt

Before targeting the entire conjectured cap interval, test a modest
scale-dependent extension. A fixed extra doubling is already covered by
the finite-depth theorem with a larger fixed eta; repeating it would not
resolve this gap. A concrete new candidate is

    eta_h=ell^(1/16),
    T_h=t_f+(1/8+1/16) log(ell)/mu.

The formal reference-background clock is then of order ell^(19/16),
still o(ell²), whereas the formal receiver clock has order ell^(33/16).
The latter produces a generic Grönwall factor h^(-C ell^(1/16)), which
no fixed residual-power budget can absorb. These are extrapolated
reference calculations, not estimates proved for the longer actual flow.

Keep the original datum. Specify the complete approximate velocity,
actual background, deformed envelope and a norm controlling the desired
velocity-gradient observable. Include pressure, viscosity, mean
corrections and every residual term. Uniformity in eta_h and the actual
lifespan are part of the new task; the fixed-eta theorem supplies neither.

The decisive object is the full linearized propagator in that changing
norm. If Sigma(t) is the proposed carrier-strain scale, one needs a
justified bound for the propagator divided by Sigma(t)/Sigma(s), together
with the correspondingly weighted residual integral. Commutators from
the changing norm and the nonlinear error must be included.

The elementary negative control is already decisive against the report's
shortcut: Sigma(t)=Sigma(0) exp(mu t) and e'=C Sigma(t)e imply

    e(t)=e(0) exp(C [Sigma(t)-Sigma(0)]/mu).

This does not preserve e(t)/Sigma(t). A successful estimate must identify
which polarization, cancellation or structure controls this growth, or
exhibit the actual growing error mode that prevents the extension.
An a priori estimate must be paired with a separate continuation argument.

It does not replace the second task: actual nonlinear feedback with full
pressure, followed by incoming-state and all-orders force accounting for
any proposed iteration. No route is promoted or killed by the supplied
report alone. ROOT, E-prime and FORCED-D remain OPEN.

## Teaching and public presentation

The textbook keeps its classical mathematical lineage explicit. Transformatics
is the name of this course and research program; the report does not establish
it as a new mathematical discipline. A corrected carrier-cap model could
become a worked example once its assumptions and transfer gap are taught
alongside the calculation.

The user's plain-web direction is implemented with ordinary typography,
links and controls, an exact 2D map animation, and the existing 3D numerical
fluid laboratory. Neither animation is evidence for the research claims.
The publication condition is unmet. Clay's
[current Navier–Stokes page](https://www.claymath.org/millennium/navier-stokes-equation/)
still lists the problem as unsolved, checked on 8 September 2026.
