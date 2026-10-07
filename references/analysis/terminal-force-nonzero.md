# A nonzero projected terminal force in the released localization

8 September 2026. Source-derived classical calculation with independent
AI-agent reviews of the source identification and the argument. This is not
a new formal certificate or external expert review.
This note identifies a nonzero part of the actual terminal force of
the pinned construction. It then excludes one coarse sufficient stability
test. It does not prove that the true error grows, or that an unforced
singularity is impossible.

## 1. The precise exterior and cutoff being used

Use the viscosity-one, terminal-time-one normalization of the released
[OpenAI source](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
Write tau=1-t, A=1/2+h, with its fixed h>0. The source and native build
have their separate [evidence record](../navier-stokes/openai-result-bridge.md).
This calculation does not extend that formal verification scope.

The spatial cutoff is explicitly a product:

\[
\chi(r,z)=\eta(r)\xi(z),\qquad
\eta(r)=c_0(16r^2),\qquad \xi(z)=c_0(4z).
\tag{1}
\]

Here c_0 is smooth, equals one on [-1/2,1/2], and vanishes outside (-1,1).
Consequently, with

\[
a=1/\sqrt{32},\qquad b=1/4,
\]

eta equals one for r<=a and zero for r>=b; xi is identically one near z=0.
These are `SpatialLocalization.cutoffProfile`, `spatialCutoff` and their
plateau/support statements, [lines 41–50 and 133–151](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/SpatialLocalization.lean#L41).

At any fixed positive r on z=0, sufficiently late times lie in the actual
pure-heat exterior. The stream potential and all annular corrections vanish
there. In an open preterminal neighborhood the full uncut fields are

\[
u=K(r,t)e_\theta,\qquad p_r=K^2/r,
\qquad K_t=K_{rr}+r^{-1}K_r-r^{-2}K.
\tag{2}
\]

This is equality of fields on an exterior region, not merely a leading
asymptotic term. The source pins are `BaseExterior.near_one_in_exterior`
and the subsequent equatorial trace theorem, the actual exterior identities
in `FinalSlowBase` and `ActualCandidateAssembly`, and the paper's §9.5,
step 4. The paper's §10 localizes this full field, retaining cutoff terms.

The heat profile has the terminal value

\[
K_0(r)=\kappa r^{-1-2h},\qquad \kappa>0.
\tag{3}
\]

Indeed, `TerminalStress.physicalHeat` is C times
\(s^{-A}H(2\tau/s)\), where s=r^2/2. `RadialHeatProfile.profile_zero`
gives H(0)=1. Thus kappa=2^A C. The source's C is positive:
`BaseExterior.nominalHeatNormalization` uses
`PhysicalHeatCoordinates.normalization`, whose positivity follows from
`normalization_pos` and `nominalHeatSwitch_pos`.
The smooth positive-radius extension supplies the radial derivatives as well.

For each fixed r in [a,b], the exterior equality applies for sufficiently
small tau; the required time need not be uniform over unrelated choices of
the construction. On this compact annulus one may also choose a common late
interval. The late temporal cutoff is one. The periodic version agrees with
the localized fields inside its fundamental cube, which contains every
circle considered below.

For the whole-space export, the additional cutoff used when extending the
force equals one on this cylinder (`R3CompactCandidate.outerCutoff_one`).
It therefore preserves every circle used in the calculation. The argument
does not replace the complete field by the leading core alone.

## 2. A circulation that pressure cannot remove

Let f be the complete localized physical force and let F_0 be its smooth
terminal trace. In the exterior, the localized velocity is chi K e_theta
and its pressure is chi p. The azimuthal component of the complete residual
is

\[
f_\theta=-K\Delta\chi-2K_r\chi_r.
\tag{4}
\]

The centrifugal and pressure terms are radial or axial. Equation (2)
cancels precisely the uncut azimuthal heat terms. Equation (4) is the
azimuthal part of the full residual calculated in the
[force source audit, §3](external-force-removal-source.md).
At z=0 the xi derivatives vanish, and (3) therefore gives

\[
(F_0)_\theta(r,0)
=-\kappa r^{-1-2h}
\left[\eta''(r)-\frac{1+4h}{r}\eta'(r)\right].
\tag{5}
\]

Put beta=1+4h and D_eta=eta''-beta eta'/r. This expression cannot vanish
identically on (a,b). Otherwise

\[
(r^{-\beta}\eta')'=0,
\]

so r^(-beta) eta' is constant. Smooth matching to eta=1 gives eta'(a)=0;
hence eta'=0 on (a,b), contradicting eta(b)=0.
Thus there exists r_* in (a,b) with (F_0)_theta(r_*,0) nonzero.

Let C_r be the circle of radius r in the plane z=0, oriented in the
positive angular direction. Then

\[
\oint_{C_r}F_0\cdot dx=2\pi r(F_0)_\theta(r,0).
\tag{6}
\]

Write the global Leray projection as P F_0=F_0-grad phi. The potential
phi is single valued, so its integral around this circle is zero. This
holds on R^3 and on the torus, where the chosen circle lies in one local
coordinate cube. Consequently (6) proves

\[
\boxed{\mathbb P F_0\ne0.}
\tag{7}
\]

The rest of the force may be non-axisymmetric. That does not change the
zero circulation of a gradient or the exact exterior value used on C_r.
No pointwise locality of the pressure projection is assumed.

A quantitative form is available without choosing a particular cutoff
formula. Define

\[
I_{a,b,\beta}=\int_a^b r^\beta
\int_a^r s^{-\beta}\,ds\,dr>0.
\]

Solving the first-order equation for eta' and integrating eta(b)-eta(a)=-1
shows ||D_eta||_infinity >= 1/I_{a,b,beta}. The maximum is attained inside
the interval, since eta is flat at both ends. From (5)–(6),

\[
\|\mathbb P F_0\|_\infty
\ge\sup_{a\le r\le b}|(F_0)_\theta(r,0)|
\ge\frac{\kappa b^{-1-2h}}{I_{a,b,\beta}}>0.
\tag{8}
\]

This lower bound concerns the fixed source's actual localization. A different
localization or construction requires a new argument. It is not a universal
lower bound for every smoothly forced singular solution.

## 3. Consequence for the previously proposed coarse stability test

The source's smooth terminal extension implies

\[
\|\mathbb P f(t)-\mathbb P F_0\|_{H^s}\longrightarrow0
\]

for every fixed integer s>=0, using compact support on R^3 or the fixed
torus. Hence for s>=3 there are t_*<1 and delta_s>0 such that

\[
F_s(t):=\|\mathbb P f(t)\|_{H^s}\ge\delta_s
\qquad(t_*<t<1).
\tag{9}
\]

The separate [inner-circle source calculation](external-modulation-source.md)
gives ||grad U(t)||_infinity >= c tau^(-1-h). In that calculation the
Cartesian derivative of the rotating basis is essential. It gives no lower
bound on symmetric strain or on the true linearized growth rate.
Sobolev embedding nevertheless implies that the particular coarse coefficient
used in [the stability note, §3](force-removal-stability.md)
satisfies

\[
a_s(t):=C_s\|U(t)\|_{H^{s+1}}\ge c_s\tau^{-1-h}.
\tag{10}
\]

Fix any t_0<1 and choose t_0<=r_1<r_2<1 after both lower bounds apply.
For t>r_2, its nonnegative Gronwall majorant obeys

\[
\begin{aligned}
\Phi_s(t)
&=\int_{t_0}^t e^{\int_r^t a_s(\sigma)\,d\sigma}F_s(r)\,dr\\
&\ge\delta_s(r_2-r_1)
\exp\!\left(\frac{c_s}{h}
[(1-t)^{-h}-(1-r_2)^{-h}]\right).
\end{aligned}
\tag{11}
\]

In particular int_(t0)^1 Phi_s(t) dt is infinite. Thus the sufficient
condition (8) of that note cannot hold for this source at any fixed late
restart. Moving the initial time closer to one does not repair this
particular estimate.

This excludes the coarse H^(s+1)-norm Gronwall test, not the true propagator.
The exact linear response includes signs, pressure and rotation that (11)
has discarded. The next useful target is therefore a structured or modulated
stability argument, with its nonlinear error space and fixed initial datum
specified. Unforced ROOT remains open.

## Review record

Two separate AI agents checked the terminal coefficient, integrating-factor
argument, circulation, quantitative bound and scalar response estimate.
One also followed the actual exterior equalities, positive heat
normalization and the larger force cutoff in the pinned formal source.
The integration reviewer checked the companion gradient and modulation arguments.
The [symbolic companion](checks/check-force-removal.py) checks
elementary identities and negative controls;
the written argument supplies the analytic and source-dependent steps.
