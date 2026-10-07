# Notation and glossary

A symbol has a meaning within a stated problem. The research chapters sometimes
use conventions inherited from their source papers; those chapters identify
the change. In particular, $S$ can denote a model evolution, a strain matrix,
or a wave phase. These are different objects. Use the surrounding definition,
not the letter alone, to identify them.

## State and evolution

**State space $X$.** The set of allowed configurations. A particle state
may be a point of $\mathbb R^d$; a fluid state is a velocity field satisfying
specified regularity, divergence and boundary conditions.

**Transformation $T$.** A map taking an allowed input state to an output
state. Its domain matters: a formula need not define a map on every state.
See [finite changes](transformations.md).

**Flow $\Phi_t$.** Evolution through time $t$ for an autonomous system,
on the interval where the solution exists. The composition law is
$\Phi_{t+s}=\Phi_t\circ\Phi_s$ whenever both sides are defined.
A general time-dependent evolution uses two times, $T_{t,s}$.

**Generator $L_v$.** The instantaneous action of a smooth vector field
$v$ on an observable: $L_vf=v\cdot\nabla f$. This is the derivative
of the pulled-back observable at time zero. See [generators](generators.md).

**Observable $f$.** A quantity read from a state. Examples include a particle
coordinate, total fluid energy and a Fourier coefficient. Different observables
can behave differently along the same evolution.

**Pullback $U_T$.** The map on observables defined by $U_Tf=f\circ T$.
With this convention, $U_TU_S=U_{S\circ T}$.

**Finite difference $\Delta_T$.** The change of an observable under a
specified transformation: $\Delta_Tf=f\circ T-f$. It is not the
operator-theoretic resolvent $(zI-A)^{-1}$.

## Representation and approximation

**Representation $R:X\to Y$.** A way of describing a full state by a
model state. A projection onto a few coordinates can lose information.
A change of coordinates may preserve all of it.

**Fiber of $R$.** The set of states with the same represented value:
$R^{-1}(y)=\{x:R(x)=y\}$. Exact closed model evolution requires that
evolving states in the same fiber gives the same represented output.
See [transfer systems](transfer-systems.md).

**Exact transfer; semiconjugacy.** Exact transfer means $RT=SR$, with all domains specified.
Following the foundations, a semiconjugacy additionally requires $R$ onto
$Y$; the topological version also requires continuity. If $R$ is
invertible with an inverse of the required regularity, this becomes a conjugacy. In a continuous
problem the corresponding relation must hold at each relevant time.

**Defect $D_R$.** For a normed model space, $D_R(x)=R(Tx)-S(Rx)$.
It measures a one-step failure of the transfer relation, not the entire
accumulated error.

**Stability.** A bound on how changes in data or forcing affect an output.
For a Lipschitz map, $\|Sx-Sy\|\le L\|x-y\|$. Stability constants
enter every [composition of errors](composition.md).

**Residual.** The discrepancy left when a proposed field is inserted into an
equation. For prescribed $u,p$,
$\mathcal R_\nu(u,p)=u_t+(u\cdot\nabla)u-\nu\Delta u+\nabla p$.
The forced equation requires $\mathcal R_\nu(u,p)=f$. See [residuals](residuals.md).

**Consistency.** Agreement of an approximation rule with the target equation
in an appropriate limit. A small residual is a consistency estimate;
turning it into small solution error also requires stability and initial-data
control.

## Norms, scales and fluid quantities

**$L^p$ norm.** For finite $p$,
$\|u\|_p=(\int|u|^p)^{1/p}$, using the stated measure.
The $L^\infty$ norm is the essential supremum; for a continuous periodic
field it is the maximum. A normalized torus integral differs from an
unnormalized integral by a volume factor.

**$H^s$ and $C^m$.** For nonnegative integers, $H^s$ measures
square-integrable derivatives through order $s$; $C^m$ denotes continuous derivatives through order $m$.
On a noncompact domain, boundedness requires $C_b^m$ or an explicitly
finite $C^m$ norm; each estimate specifies its convention.
Small $L^2$ error alone does not imply small gradient error.

**Viscosity $\nu$.** The positive coefficient of diffusion in ordinary
Navier–Stokes. A Fourier mode of wavevector $k$ under the heat equation
decays by $e^{-\nu|k|^2t}$.

**Pressure $p$; Leray projection $\mathbb P$.** Pressure enforces
incompressibility. On a nonzero periodic Fourier mode,
$\mathbb P_k=I-k\otimes k/|k|^2$. The zero mode is handled separately.
See [the fluid equation](equation.md).

**Strain $S$; vorticity $\omega$.**
$S=(\nabla u+\nabla u^T)/2$ and $\omega=\nabla\times u$.
The research notation $Q=\int|S|_F^2$ measures integrated squared strain.
Under periodic incompressibility, $\int|\omega|^2=2Q$; conventions for
the factor in the word *enstrophy* vary.

**Packet, phase and polarization.** A packet is an oscillation with an envelope.
In $a(x)e^{i\varphi(x)/h}$, $\varphi$ is phase and the vector
$a$ includes polarization. The covector $\nabla\varphi$ records local
oscillation direction. Localization contributes additional derivatives.

**Mean stress.** An average of the tensor $w\otimes w$. A wave with zero
mean can have nonzero mean stress because averaging does not commute with
multiplication. See [the published-proof examples](published-proof.md).

**$O(h^a)$, $o(1)$, and $h^{a-o(1)}$.** The first means a bound
by $Ch^a$ with the permitted parameter dependence of $C$ specified.
The second tends to zero in the stated limit. The third allows an exponent
loss tending to zero; it is not a uniform bound by $Ch^a$.

## Limits and proof scope

**Fixed depth versus an infinite construction.** A theorem for every fixed
integer depth may have a scale threshold depending on that depth. It does not
automatically yield infinitely many stages for one fixed datum. See [iteration](iteration.md).

**Flatness.** A smooth function is flat at a point if every derivative vanishes
there. Smoothness alone does not imply flatness. A force can extend smoothly
through a terminal time with nonzero terminal values.

**ROOT and FORCED-D.** Local research identifiers. ROOT asks for global
regularity of the unforced periodic equation. FORCED-D refers to Clay's forced
periodic breakdown alternative and is recorded here as an external imported
result. They have different quantifiers and forcing assumptions.

**Written, imported and kernel-checked results.** These identify different
evidence records, explained in [reading a claim](evidence.md). Consult the
[claim register](../claims.md) for exact scope and source versions.
