# Global strain cost of the completed external reference

8 September 2026. Restricted written consequence of the released
construction. All modes, mean corrections, diagonal tails and physical
cutoffs are included. This is a bound for the actual forced reference,
not an arbitrary-error cancellation theorem or an unforced solution.

The external source is [OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538)
and its [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
SHA-256 `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
We use its unit torus, viscosity one, terminal time one, and one fixed
choice of the construction with \(0<h<1/100\).

## 1. The bound and its quantifiers

There are constants \(C,\tau_*>0\), depending on that fixed construction,
such that, for \(0<\tau<\tau_*\),
\[
 \sup_{1-\tau\le t\le1-\tau/2}
 \left(\|U(t)\|_\infty+\|\nabla U(t)\|_\infty\right)
 \le C\tau^{-1-h}\sqrt{1+\log(1/\tau)}.
 \tag{1}
\]
In particular, the exact coefficient in the linear \(L^2\) energy
inequality obeys
\[
 a_2(t):=\left\|\max\{0,\lambda_{\max}(-S(U(t)))\}\right\|_\infty
 \le C\tau^{-1-h}\sqrt{1+\log(1/\tau)},
 \qquad S(U)=\tfrac12(\nabla U+\nabla U^T).
 \tag{2}
\]
The explicit remaining-time power is \(1+h\); the logarithmic power
in this upper bound is \(1/2\). We do not assert optimality of that
logarithm. The already reviewed heat-exterior calculation gives the
lower bound \(a_2(t)\ge c(1-t)^{-1-h}\), so the power cannot be
improved in an unrestricted global supremum estimate of this kind.

The proof below does not use Lemma 9.8's deliberately coarse combined
space/time derivative loss to estimate the finite prefix. It uses the
cumulative velocity classes (9.9), and uses the diagonal derivative
estimate only to bound the remaining infinite tail.

## 2. Spatial differentiation in one physical chart

The paper's (6.1)–(6.6) set
\[
 Q=2^{-n},\qquad \varepsilon=Q^h,\qquad S_*=n^2,
 \qquad A=\tfrac12+h,
 \qquad k=\lceil\varepsilon^{-1/2}\rceil,
 \qquad \kappa_s=10^{-5}.
 \tag{3}
\]
On an active band, \(Q\asymp q\), and
\(n\asymp1+|\log q|\). The band scale is held fixed while
differentiating. The physical velocity is \(Q^{-A}\) times its
normalized chart representative. Evaluation at the actual auxiliary
phase map is already included in the differential operators.

The normalized radial derivative of an amplitude loses at most
\(\varepsilon^{-\kappa_s}\), with a fixed polynomial in \(S_*\);
the axial amplitude derivative is smaller. Thus a coefficient of class
\(\mathcal W^\alpha\) or \(\mathcal M^\alpha\) has a first
physical amplitude derivative bounded by
\[
 C Q^{-1/2}\varepsilon^{\alpha-\kappa_s}S_*^P.
 \tag{4}
\]
This is (6.32), including the actual radial evaluation derivative,
followed by the physical scale conversion. Frame derivatives cost
\(C Q^{-1/2}\) on the annulus and fit (4). The flat shell-edge
weights absorb their fixed inverse edge powers, so these estimates
hold uniformly through smooth zero extensions.

For the actual selected phase, Lemma 7.1 and (7.9) give a stronger
zeroth-order bound than an unspecified polynomial:
\[
 |n_\Phi|\le C,\qquad
 \nabla_x\Phi=Q^{-1/2}n_\Phi
 \quad\text{in the orthonormal cylindrical frame}.
 \tag{5}
\]
Here \(s(v)\), the reference normal and its coefficient \(B_s\) stay
in fixed bounded ranges. The radial, angular and axial entries of the
physical gradient are all retained. In particular,
\[
 |\nabla_x e^{ikm\Phi}|\le C_m Q^{-1/2}\varepsilon^{-1/2}
 \tag{6}
\]
for every harmonic in a fixed finite stage. Such a stage has only
finitely many harmonics, independently of the band.

Equations (4) and (6) imply, for a wave in \(\mathcal W^\alpha\),
\[
 |\nabla_x(Q^{-A}w)|
 \le C Q^{-1-(3/2-\alpha)h}S_*^P,
 \tag{7}
\]
because \(\kappa_s<1/2\), so the carrier derivative is the larger
power. For a mean in \(\mathcal M^\alpha\), there is no angular
carrier, and
\[
 |\nabla_x(Q^{-A}m)|
 \le C Q^{-1-(1-\alpha+\kappa_s)h}S_*^P.
 \tag{8}
\]
These are spatial estimates, not estimates on physical time derivatives.

## 3. The primary wave fixes the logarithmic cost

Write one leading transverse primary summand as in (7.24) and (7.35):
\[
 W_{0,\gamma}^{\rm phys}
 =Q^{-A}\eta_\beta\sqrt\varepsilon\,
   a_\sigma\chi_g\psi\,t^h_\sigma\cos(k\Phi_\sigma).
 \tag{9}
\]
The covariance estimate (7.29) gives
\[
 y_\sigma=a_\sigma^2\le C\sqrt{S_*}|T_{0,*}|,
 \qquad |a_\sigma|\le C S_*^{1/4},
 \tag{10}
\]
since the fixed normalized target is bounded on the closed active
rectangle. Lemma 7.4, specifically (7.21), gives
\(|t^h_\sigma|\le C P(v)\le C\). The cutoffs in (9) are uniformly
bounded. Therefore the portion of its derivative falling on the carrier
has the bound
\[
 C Q^{-A-1/2}\sqrt\varepsilon\,k S_*^{1/4}
 \le C Q^{-1-h}S_*^{1/4}.
 \tag{11}
\]
The product \(\sqrt\varepsilon\,k\) is between one and two for
small \(Q\). Since \(S_*=n^2\), its fourth root is proportional
to \(\sqrt{1+|\log q|}\).

Derivatives of the amplitude, pulse, slow cutoff, auxiliary cutoff and
cylindrical frame are included separately using the fixed first-order
coefficient estimates and (4). They are bounded by
\[
 C Q^{-1-(1/2+\kappa_s)h}S_*^{P_0}.
 \tag{12}
\]
The gap \((1/2-\kappa_s)h>0\) makes this smaller than (11) for
all sufficiently small \(Q\), regardless of the finite exponent
\(P_0\). No numerical value of \(P_0\) is required.

Lemma 6.3 gives bounded pointwise overlap of wave labels, including
their fixed support enlargements. Thus summing the actual primary
labels does not introduce a further power of \(S_*\) into (11).
This uses pointwise overlap; the polynomial count of labels met during
radial integration is a different estimate and is not used here.

The finite construction uses exact curls. The field (9) is only their
transverse leading part. Their curl corrections are included in the
remainder in the next section, rather than omitted from the velocity.

## 4. One finite state contains every earlier correction

At every fixed stage \(J\), Definition 9.4 and Proposition 9.6 retain
the cumulative bounds (9.9):
\[
 w-w_0^{\rm tan}\in\mathcal W^{17/25},\qquad
 v,\gamma,p_m\in\mathcal M^{9/10},\qquad
 \beta\in\mathcal M^{19/10}.
 \tag{13}
\]
They apply to the complete current fields, including primary curl
corrections, all subsequent harmonics, signed stress corrections and
mean updates. Constants and logarithmic powers may depend on \(J\).
Applying (7)–(8) gives the following complete first-derivative budget:

| Contribution | Physical derivative bound before absorbing logarithms |
|---|---|
| Primary carrier | \(Cq^{-1-h}(1+|\log q|)^{1/2}\) |
| Primary coefficient derivatives | \(Cq^{-1-(1/2+\kappa_s)h}(1+|\log q|)^{P_0}\) |
| All remaining waves | \(C_Jq^{-1-(41/50)h}(1+|\log q|)^{P_J}\) |
| Tangential means | \(C_Jq^{-1-(1/10+\kappa_s)h}(1+|\log q|)^{P_J}\) |
| Radial mean | \(C_Jq^{-1+(9/10-\kappa_s)h}(1+|\log q|)^{P_J}\) |

Every nonprimary row has a strictly smaller remaining-scale power
than \(1+h\). In particular, the smallest relevant wave margin is
\((9/50)h>0\). Every fixed polynomial logarithm can be absorbed in
these margins after fixing \(J\). Radial aggregation of mean labels
may increase \(P_J\), which is harmless here.

The realized axisymmetric base obeys the normalized derivative bounds
(5.42), with the cutoff-tail refinement (5.46); its first physical
derivative is bounded by \(Cq^{-1-h}\). These estimates extend to
the axis using the smooth Cartesian profile factors described in
Proposition 5.5. The axial scale \(q^{1/2-h}\) is larger than the
radial scale \(q^{1/2}\), so it causes no worse spatial power.

Hence each fixed finite state has
\[
 |\nabla u^{[J]}(x,t)|+|u^{[J]}(x,t)|
 \le C_J q^{-1-h}\sqrt{1+|\log q|}
 \tag{14}
\]
for sufficiently small \(q\). This step is why summing Lemma 9.8's
coarse individual stage bounds is unnecessary and would lose the
useful exponent.

## 5. The infinite tail and global localization

Apply the actual summation estimate (5.35) at derivative order one.
Its bound on the velocity includes the extra curl derivative and
all cutoff commutators. Since \(g_J\to\infty\), first choose one
fixed \(J\) large enough that \(g_{J+1}/2-\ell'_1\ge0\). Then,
for \(q<(2a_J)^{-1}\),
\[
 \|u_{\rm loc}-u^{[J]}\|_{C^1\text{ at }(x,t)}\le 2^{-J}.
 \tag{15}
\]
The notation denotes the sum of the pointwise norms of derivatives
through order one. The first \(J\) cutoffs equal one in this region.
The estimate controls the entire later infinite tail, not its
individual norms without their cutoff factors. Combining (14) and
(15) proves the same bound for the completed local field.

Outside the fixed active profile rectangle the field is exactly the
heat exterior, by Theorem 3.1(iii). There
\(r^2\ge2X_{\rm ext}q\), \(q\ge1-t\), and its explicit formula
\(K=\kappa r^{-1-2h}H(4(1-t)/r^2)\) gives
\(|\nabla(Ke_\theta)|\le Cr^{-2-2h}\le C(1-t)^{-1-h}\).
The fixed spatial localization region is away from the singular
origin; its field and cutoff derivatives have bounded terminal
limits. This follows from the one-sided extension in Theorem 3.1(ii)
together with the exact exterior formula where \(q\downarrow0\).
The late temporal cutoff is one. Periodization preserves these
local bounds and introduces no new small-scale derivatives.

Finally \(q\ge1-t\ge\tau/2\) on the requested time interval.
Equations (14)–(15), the exterior and the fixed localization region
therefore prove (1). All thresholds and constants are for one fixed
construction; there is no uniformity over new profile choices or
growing correction orders.

The formal source provides matching structural checks:
[ActualPrimaryBounds.chart_normal_range](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualPrimaryBounds.lean#L1253)
retains a uniform bound on the actual selected phase normal;
[PrimaryCovarianceBounds](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PrimaryCovarianceBounds.lean#L245)
retains the \(S_*^{-1/2}\) covariance-column mass;
[CorrectionStep's cumulative wave update](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CorrectionStep.lean#L2693)
preserves the \(17/25\) remainder class; and
[DiagonalJetBounds.potential_tail_jet_bound](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalJetBounds.lean#L196)
controls actual differentiated cutoff tails. The assembled global
bound (1) is the written consequence proved here, not a claim that
an identically stated Lean theorem has been exported or replayed.

## 6. Cost for the actual linear force response

For the full solenoidal linearized evolution, transport and pressure
cancel in the exact energy identity:
\[
 \frac12\frac d{dt}\|z\|_2^2+\nu\|\nabla z\|_2^2
 =-\int z\cdot S(U)z\,dx+\langle F,z\rangle.
 \tag{16}
\]
Consequently (2) gives, for \(s\le t\) in this time interval,
\[
 \|\mathcal S_U(t,s)\|_{2\to2}
 \le\exp\!\left(C(t-s)\tau^{-1-h}\sqrt{L_\tau}\right),
 \qquad L_\tau=1+\log(1/\tau).
 \tag{17}
\]
On any window of length
\(\Delta_\tau\le C_0\tau^{1+h}L_\tau\), this is
\[
 \|\mathcal S_U(t,s)\|_{2\to2}\le\exp(C_1 L_\tau^{3/2}).
 \tag{18}
\]
It is an upper bound on the actual full propagator, compatible with
the earlier lower bound on its norm. If
\(\sup\|\mathbb P f\|_2\le F_*\), the zero-data linear response
has the elementary bound
\[
 \left\|\int_{t_0}^{t_0+\Delta_\tau}
 \mathcal S_U(t_0+\Delta_\tau,s)\mathbb P f(s)\,ds\right\|_2
 \le F_*\Delta_\tau\exp(C_1L_\tau^{3/2}).
 \tag{19}
\]
This bound alone does not tend to zero and is not a force-removal
estimate. Its useful content is the explicit cost: for every fixed
\(c,\alpha>0\),
\(\exp(C_1L_\tau^{3/2}-c\tau^{-\alpha})\to0\).
Any proposed spatial attenuation must still be proved for the actual
response, with compatible constants and domains, before this comparison
can be used.

No additional cancellation from rapid oscillation has been assumed.
The exact transport cancellation is already present in (16). A
transverse carrier's leading gradient is a rank-one matrix whose
symmetric part generally remains nonzero, so the oscillation alone
does not remove its pointwise strain. The bound above uses its actual
amplitude and phase geometry rather than replacing the signed energy
integral by an unsupported angular average.

## 7. Fixed Sobolev orders retain the same exponential cost

Let \(z\) be the zero-data linear response on this same window:
\[
 z_t-\nu\Delta z+(U\cdot\nabla)z+(z\cdot\nabla)U+\nabla p=F,
 \qquad \operatorname{div}z=0,\qquad z(t_0)=0.
 \tag{20}
\]
Assume \(F\) is a fixed smooth periodic force extending through time
one; \(F=\pm f\) and \(F=\pm\mathbb P f\) are included. Normalize
the pressure to have zero spatial mean. The same conclusion holds if
each fixed Sobolev norm of \(F\) has a polynomial bound in \(\tau^{-1}\).

For every fixed nonnegative integer \(m\), there are finite constants
\(C_m,P_m\), independent of \(\tau\), such that
\[
 \sup_{t_0\le t\le t_0+\Delta_\tau}
 \big(\|z(t)\|_{H^m}+\|z_t(t)\|_{H^m}+\|p(t)\|_{H^m}\big)
 \le C_m\tau^{-P_m}\exp(C_mL_\tau^{3/2}).
 \tag{21}
\]
There is no bound here on how \(C_m,P_m\) grow with \(m\).

To prove this, write \(Z_m=\|z\|_{H^m}\) and
\(g_\tau=C\tau^{-1-h}\sqrt{L_\tau}\). Differentiating (20),
pairing with the differentiated solenoidal field and discarding only
nonnegative viscous dissipation gives, in the usual regularized-norm
or upper-Dini sense,
\[
 D^+ Z_m\le C_m g_\tau Z_m+
 C_m\sum_{j=2}^{m+1}\|\nabla^jU\|_\infty Z_{m+1-j}
 +\|F\|_{H^m}.
 \tag{22}
\]
The sum is empty when \(m=0\). In the transport commutator, one
derivative on \(U\) multiplies derivatives of \(z\) of order at
most \(m\), giving the first term. Every higher derivative of
\(U\) multiplies a strictly lower derivative of \(z\). The term
\((z\cdot\nabla)U\) has the same triangular structure, including
\(\nabla^{m+1}U\) multiplying \(z\). Pressure drops from each
differentiated energy pairing. No high Sobolev norm of \(U\) has
been placed in the coefficient of \(Z_m\).

The source's fixed-order jet and cutoff-tail estimates imply, for
every fixed \(j\),
\[
 \sup_{1-\tau\le t\le1-\tau/2}\|\nabla^jU(t)\|_\infty
 \le C_j\tau^{-N_j}
 \tag{23}
\]
for some finite \(N_j\). This is the fixed-prefix plus diagonal-tail
argument from Lemma 9.8 and Proposition 9.9, with logarithms absorbed
into one additional power; the exact exterior and localization region
are included as in §5. It is also the source input detailed in
[the fixed response-jets note](force-response-jets.md#1-the-two-different-kinds-of-regularity-used).
There is no assertion that \(N_j\) grows linearly with \(j\).

At order zero, (17) bounds \(Z_0\). Suppose all lower orders have
the form in (21). Each term of the sum in (22) is then a polynomial
in \(\tau^{-1}\) times \(\exp(C_mL_\tau^{3/2})\). Integrating
(22) multiplies these by at most
\(\exp(C_m g_\tau\Delta_\tau)\), of the same form by (18).
The time interval has length at most one. Induction proves the bound
for \(Z_m\) at every fixed order. The constants may increase with
the finite number of induction steps, while the exponential remains
a fixed constant times \(L_\tau^{3/2}\).

For the other terms in (21), incompressibility gives the complete
pressure equation
\[
 \Delta p=\operatorname{div}F-
 \partial_i\partial_j(U_i z_j+z_i U_j).
 \tag{24}
\]
The periodic Riesz operators \(\Delta^{-1}\partial_i\partial_j\)
are bounded on every \(H^m\). Thus \(p\) is bounded by fixed
Sobolev norms of the products \(Uz\), and by
\(\Delta^{-1}\operatorname{div}F\). Leibniz' rule, (23) and the
already obtained \(Z_m\) estimate give the claimed pressure bound.
Finally use the projected equation
\[
 z_t=\nu\Delta z-
 \mathbb P\operatorname{div}(U\otimes z+z\otimes U)+\mathbb P F.
 \tag{25}
\]
Its \(H^m\) bound uses the proved solution estimate through order
\(m+2\), and fixed derivatives of \(U\) through order \(m+1\).
This explicitly charges the two derivatives needed for viscosity.
All factors again have the form (21). These are linear-response
upper bounds; no estimate on the nonlinear force-removal error is
asserted by this corollary.

## Verification scope

The integration reviewer and a separate analysis agent independently read the
load-bearing paper estimates and passed the primary amplitude/phase
normalization, cumulative finite-state bounds, fixed diagonal-tail
comparison and global localization. Both also checked the triangular
Sobolev energy inequality, the full pressure equation and the derivative
cost for \(z_t\). Exact rational arithmetic reproduced all four
nonprimary power margins and the logarithmic exponents. No correction
was required. These are independent AI reviews and elementary algebra
checks of a written source-derived estimate, not a new Lean replay.
No complete nonlinear force-removal estimate is asserted.
