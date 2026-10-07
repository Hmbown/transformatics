# A signed coarse component of the actual nonlinear remainder survives focus

8 September 2026. **Reviewed bounded actual-flow calculation.** The
[independent source review](postfocus-normal-source-review.md)
and a separate coordinating-agent read passed at the written scope below.
The review pins the mathematical source before this introductory label was
updated. No equation or estimate changed. These are AI-agent reviews, not
external expert acceptance or formal PDE certification.
This continues the same actual unforced solution and the same original data.
It uses the full pressure, global relative-stress errors, and an affine
comparison only after estimating its error against actual q. It supplies
neither a new datum nor an infinite trajectory. ROOT, E-prime and FORCED-D
remain open. No DNS is used.

The endpoint row differs from the fixed original receiving normal used in
[the short-time result](normal-source-transport.md). Here it
is the transported primary r direction, at a coarse frequency parallel to
the primary normal N. This change of test is explicit; the remainder
being measured is unchanged.

## 1. Same remainder, new endpoint observable

Keep the data and notation of the
[logarithmic host](../navier-stokes/logarithmic-host.md):

\[
 k=h^{3/2},\quad d=h^{5/4},\quad \epsilon=\nu h^4,\quad
 L=h^{-10},\quad \ell=\sqrt{\log(1/h)},
\]
\[
 t_f={2\over\mu}\log\ell-\ell^{-3/4},\qquad
 t_\eta=t_f+L_\eta,\qquad
 L_\eta={\log\ell\over8\mu}+{\log\eta\over\mu}.
                                                        \tag{1}
\]

The exact existing receiving focus is \(t_c=t_f\): the original seed
prescribes its covector there, as in
[the original preparation](original-seed-compatibility-draft.md)
and [outer matching](outer-matching.md).
Distinguish the nominal time \(t_{\rm nom}=(2/\mu)\log\ell\).
Their difference is \(\Delta=t_{\rm nom}-t_c=\ell^{-3/4}\).
All exact focus formulas below are centered at t_c, not t_nom.
In inner units \(\Delta/e=O(\ell^{-1/4})\to0\); recentering an
asymptotic calculation would make only a vanishing translation error.
The endpoint factors obey the exact relation
\[
 e^{-\mu(t_\eta-t_{\rm nom})}
       =e^{\mu\Delta}e^{-\mu(t_\eta-t_c)}.
\]
No exact covector condition is moved from t_c to t_nom.

One sufficiently thin unscaled Gavrilov profile is fixed before h tends
to zero. The permitted eta is fixed and sufficiently small. Both original
waves remain in Q(0). Let q be the actual first-stage NS solution, let Z
solve its exact viscous linearization with the original receiver datum,
and put

\[
 W=Q-q,\qquad \mathcal N=W-Z,\qquad
 \partial_t\mathcal N+B_q\mathcal N-\epsilon\Delta\mathcal N
       =-\mathbb P\operatorname{div}(W\otimes W),\quad
 \mathcal N(0)=0,
                                                        \tag{2}
\]
\[
 B_qv=\mathbb P(q\cdot\nabla v+v\cdot\nabla q).
\]

Thus all q-times-generated-mean interactions are retained in B_q.
They are not omitted from a total Fourier stress.

Along the reference fixed-profile particle, use the exact primary frame
\[
 p=\beta/|\beta|,\qquad n=N/|N|,\qquad r=n\times p.
\]
The model central gradient is
\(\overline A=A_0-\ell^{-1}\beta\otimes N\), with
\(\beta=e^{\mu t}B_+(t)\). The primary stable Floquet vector B_- is
normalized as in the [outgoing proof](outgoing-outer.md).
In particular
\[
 d_-(s):=r(s)\cdot B_-(s)<-c,\qquad
 |N|+|N|^{-1}+|B_\pm|+|d_-|^{-1}\le C.              \tag{3}
\]

Choose a fixed growth majorant
\[
 H_h=\ell^{C_0}\exp(C_0\ell^{9/8}),
\]
large enough for the finitely many estimates below. There are fixed
positive exponents M and A, chosen in that order, for which
\[
 \delta_h=H_h^{-M},\qquad R_h=dH_h^A,\qquad
 \kappa_h=R_h^{-1}.                                  \tag{4}
\]
The packet diameter is much smaller than R_h, and
\[
 R_h\ll R_h/\delta_h\ll h.
\]
No exponent or differentiation order grows with h.

For all sufficiently small h, the actual endpoint has a cone-filtered
signed r(t_eta) component. In particular, with C fixed,
\[
 \|r(t_\eta)\cdot\mathcal N(t_\eta)\|_\infty
 \ge c\,\eta^{-1} k^2d^3\ell^{9/8}
                  \kappa_h^4\delta_h^4
 =c\,\eta^{-1}h^{7/4}\ell^{9/8}H_h^{-4A-4M},          \tag{5}
\]
\[
 \|S(\mathcal N(t_\eta))\|_\infty
 \ge c\,\eta^{-1}k^2d^3\ell^{9/8}
                  \kappa_h^5\delta_h^4
 =c\,\eta^{-1}h^{1/2}\ell^{9/8}H_h^{-5A-4M}.          \tag{6}
\]

The frequencies lie in a cone of angular width delta_h about N(t_eta),
with magnitude comparable to kappa_h. The cone and dual norm costs in
(5),(6) are explicit. The statement is not based on one Fourier ray
with a hidden expanding-volume penalty.

This is a coarse component of the generated remainder relative to Z.
It is not claimed to dominate Q, to be normal to the final receiving
phase, or to supply a new independent rapidly oscillating phase.

## 2. An exact distinguished Kelvin channel

First use the model central gradient; its comparison with actual q is
paid in sections 5--6. Since N dot beta=0,
\[
 N'=-\overline A^TN=-A_0^TN.
\]
For a coarse cotangent \(K(s)=\kappa N(s)\), the exact pressure-correct
Kelvin generator on its transverse plane is
\[
 G_N=-\overline A+
       {2N(N^T\overline A)\over|N|^2}.
\]
On N-perpendicular this is exactly
\[
 G_Nv=-A_0v+{2N(N^TA_0v)\over|N|^2}.                 \tag{7}
\]
The large rank-one primary shear vanishes in this restricted generator.
No pressure term has been dropped: its large additional numerator also
vanishes because N dot beta=0.

The solutions \(e^{\mu s}B_+(s)\) and \(e^{-\mu s}B_-(s)\) therefore
give its full transverse propagator. If b is the exact receiving
polarization, write
\[
 \mathbb P_Nb=B_+y_1+B_-y_2,\qquad
 y_2={r\cdot b\over d_-}.                            \tag{8}
\]

For an affine background with deformation F and a stress concentrated
at its particle, the real Fourier response v, defined by Fourier
remainder equal to -i v, satisfies
\[
 v'=G_Kv-\epsilon|K|^2v+
           \mathbb P_K b(K\cdot b),\quad v(0)=0,
 \qquad K'= -\overline A^TK.                         \tag{9}
\]
The stress mass multiplier is inserted below. Equation (9) follows by
differentiating K dot v=0 in the forced Fourier equation; its factor
2 in G_K is the full pressure contribution.

For K=kappa N and without the temporarily negligible coarse heat factor,
the endpoint r row is exactly
\[
 r(t_\eta)\cdot v(t_\eta)
   =\kappa e^{-\mu L_\eta}d_-(t_\eta)\,\mathcal J_h,
                                                        \tag{10}
\]
\[
 \mathcal J_h=\int_0^{t_\eta}
       e^{\mu(s-t_f)}
       {(N(s)\cdot b(s))(r(s)\cdot b(s))\over d_-(s)}\,ds.
                                                        \tag{11}
\]

The growing coefficient is annihilated because r dot B_+=0. A statement
about the norm of the propagator would not determine the sign of (11).

## 3. The largest inner coefficient cancels; the stable one is positive

Use the full inner system from
[inner matching](inner-matching.md) and
[the continued connection](longer-host-attempt.md).
Put
\[
 \Lambda={|\beta(t_f)||N(t_f)|\over\ell}\asymp\ell,
 \quad e=\Lambda^{-1/2},\quad z=(t_f-s)/e,
 \quad a=a_{21}(t_f)<0,\quad c=a_{31}(t_f)<0.
\]
The actual a,c stay in one compact negative set. Define
\[
 P=1+a^2z^4,\qquad
 v_0(z)={|a|Y_+(z)\over\sqrt P},\qquad w_0=-v_0',
 \qquad \rho_0=-2azv_0+az^2w_0,                     \tag{12}
\]
where the already selected incoming solution has
\[
 Y_+''={4a^2z^2-2cP\over P^2}Y_+,\qquad
 Y_+(+\infty)=1,\quad Y_+'(+\infty)=0.
\]
The factor |a| preserves the original incoming normalization
\(v_0(z)\sim z^{-2}\) at positive infinity. For the unnormalized
receiving branch, the leading components are
\[
 b_p=\sqrt\Lambda D_hv_0,\qquad
 b_n=D_hw_0,\qquad b_r=D_h\rho_0,\qquad
 D_h\asymp\ell^{5/2}.                               \tag{13}
\]

The coefficient which might first appear largest is zero:
\[
 \int_{\mathbb R}v_0w_0\,dz
       =-\tfrac12[v_0^2]_{-\infty}^{+\infty}=0.       \tag{14}
\]
Both ends have v_0 tending to zero. This cancels the leading focused
growing-row source, not the whole remainder.

The stable-row coefficient is instead
\[
 \mathcal I(a,c)=\int_{\mathbb R}w_0\rho_0\,dz
  =2a\int_{\mathbb R}
       \left({cz^2\over P}-{4a^2z^4\over P^2}\right)v_0^2\,dz
  >0.                                               \tag{15}
\]
Every nonzero point of the displayed integrand is positive because
a,c<0. The coefficient has uniform positive lower and upper bounds
over the fixed compact coefficient set.

Here is a direct verification. The first integration by parts gives
\[
 \int w_0\rho_0
       =a\int(z^2v_0'^2-v_0^2).
\]
Use \((Pv_0')'+(2a^2z^2+2c)v_0=0\). A second integration by parts gives
\[
 z^2{2a^2z^2+2c\over P}
        -\tfrac12\left({z^2P'\over P}\right)'
       ={2cz^2\over P}-{8a^2z^4\over P^2},
\]
which proves (15). Its boundary terms vanish: at positive infinity
\(v_0=O(z^{-2}),v_0'=O(z^{-3})\); at negative infinity
\(v_0=O(|z|^{-1}),v_0'=O(|z|^{-2})\).
The uniform lower bound follows by restricting to any fixed positive
interval away from zero, since Y_+>=1 there. Physical forward time has
ds=-e dz, so the entire passage has the positive orientation
\(e\int_{-\infty}^{+\infty}w_0\rho_0\,dz\).

## 4. Full incoming and outgoing tails are smaller

For (11) the slow factor
\[
 g(s)=e^{\mu(s-t_f)}{|N(s)|\over d_-(s)}
\]
has value \(g(t_f)<0\) and bounded relative variation on a fixed
small interval about t_f. The inner result is
\[
 \mathcal J_h
     =eD_h^2 {|N(t_f)|\over d_-(t_f)}
             [\mathcal I(a,c)+o(1)]< -ceD_h^2.       \tag{16}
\]
We now account for the rest of the interval and the uniform error in
this asymptotic; neither is assigned a favorable sign.

Take the already used incoming overlap
\(u_m=\ell^{-3/10}\), \(u=t_f-s\), and \(R_m=u_m/e\to\infty\).
The exact incoming outer bounds give, for u_m<=u<=1,
\[
 |y_1|\le C\ell^2/u^2,\quad
 |y_2|\le C\ell/u^3,\quad
 |b_r|+|b_n|\le C\ell/u^3.                           \tag{17}
\]
For b_n use the exact lift:
\(b_n=|N|(C\cdot B_+y_1+C\cdot B_-y_2)/d_f\).
Here C dot B_+=O(u), C dot B_-=O(1), and |d_f|~ell u^2.
The extra term u^(-5) is smaller than ell u^(-3) because
ell u_m^2 tends to infinity. Thus this part of (11) has absolute size
\[
 C\ell^2u_m^{-5}=C\ell^{7/2}=o(eD_h^2).
\]
For u>=1, the same lift and incoming stable bound give an absolute
integrand at most \(C\ell^2(1+u)^2e^{-3\mu u}\), hence total O(ell^2).

On the outgoing outer interval with any fixed small delta>0, the full
outgoing proof gives y_2=O(D_h e^(-mu tau)). Consequently, for tau>=1,
\[
 |b_r|\le CD_he^{-\mu\tau},\qquad
 |b_n|\le {CD_h\over\ell(1+\tau)e^{\mu\tau}}.
                                                        \tag{18}
\]
For delta<=tau<=1 the bounds are C_delta D_h and C_delta D_h/ell.
After the weight e^(mu tau) in (11), the total outgoing outer tail is
\(O_\delta(D_h^2/\ell)=o(eD_h^2)\), even up to L_eta.

The inner comparison is uniform on the growing intervals. On the
incoming side use
\[
 |W|\le {CD_h\over(1+z)^3},\qquad
 |b_r|\le {CD_h\over1+z}.
\]
On the outgoing side use
\[
 |W|\le {CD_h\over(1+|z|)^2},\qquad |b_r|\le CD_h.
\]
These products have integrable tails after division by D_h^2.
The full weighted Volterra comparison with the frozen coefficients has
error O(delta)+o(1), retaining the exact pressure and transversality.
Replacing g(s) by g(t_f) costs the same. First choose delta small, then
h small. Since delta is only an analysis partition and changes no
datum, letting delta tend to zero proves (16) uniformly in the terminal
phase. This uses the nonzero stable scattering connection; it does not
copy incoming decay to the outgoing side.

For the actual receiving normalization write
\[
 b_c=\theta_h b,\qquad
 \theta_h={k\ell^{7/8}\over N_h},\quad N_h\asymp D_h.
\]
This is the original normalization, not a choice of a new outgoing seed.
Since d_-(t_eta) and d_-(t_f) are both negative, (10),(16) yield a
positive real endpoint response with magnitude
\[
 \kappa\,d^3\langle F^2\rangle\theta_h^2 eD_h^2
                            e^{-\mu L_\eta}
 \asymp \kappa\,d^3 k^2\eta^{-1}\ell^{9/8}.           \tag{19}
\]
The fixed bump factor \(\int\chi^2>0\) is included in its constants.
The coarse heat clock is O(epsilon kappa^2 t_eta) on this ray. Restoring
it changes (19) by a positive-power h error. The central heat evolution
of F also has a vanishing clock and is treated in the same error budget.

## 5. Relative stress and actual central coefficients

The known q jets and clock are
\[
 \|D^rq(s)\|_\infty\le C_rm_h(s)h^{1-r},\qquad
 \int_0^{t_\eta}m_h(s)\,ds=O_\eta(\ell^{9/8}).
\]
The actual central matrix \(A_c(s)=\nabla q(s,Y(s))\) differs from
the fixed-profile model by \(h^\gamma H_h^C\), for a fixed gamma>0.
Finite-order cotangent and polarization comparison, with coefficient
bounded by the q clock, has the same positive-power error. This
includes the receiving b_c and the auxiliary coarse Kelvin transfer.
No long-time thin-profile approximation is used.

Let Z_a be the full primary receiving curl packet. The existing J=1
approximation, with its global mean and complete profile correction,
implies
\[
 \|W-Z_a\|_2
   \le h^{29/8}H_h^C+h^{31/8-B\eta}H_h^C,\qquad
 \|W\|_2+\|Z_a\|_2\le h^{27/8}H_h^C.
\]
For the permitted small eta, B eta<1/4, so
\[
 \|W\otimes W-Z_a\otimes Z_a\|_1
   \le [h^7+h^{29/4-B\eta}]H_h^C
   =h^{27/4+\gamma_1}H_h^C,\quad\gamma_1>0.          \tag{20}
\]
All mean-wave and mean-mean products, including their global tails,
are included by this Cauchy-Schwarz estimate. For a different fixed
accuracy, the reviewed fixed-depth recurrence can increase the second
exponent by fixing J first. No limit J(h) is used here.

Whole-envelope transport gives support diameter d H_h^C and phase-mean
stress
\[
 d^3\langle F_{\theta_c(s)}^2\rangle
       \Big(\int\chi^2\Big)b_c(s)\otimes b_c(s)
\]
after integration, with error \(h^{27/4+\gamma_2}H_h^C\) for a fixed
gamma_2>0. Curl errors have relative factor k/d times a subpower
majorant. Nonzero profile modes integrate by parts against the test:
their frequency is at least k^(-1) times a subpower, whereas the
coarse test frequencies are at most kappa_h times a subpower.
Thus this phase averaging also has a positive h-power error. It does
not identify a phase mean with a spatially evaluated field without
estimating the difference.

## 6. Full actual-q adjoint versus its affine comparison

For a terminal scalar test f and vector r(t_eta), use the actual
solenoidal adjoint with terminal value P(r f). Its exact pairing with
(2) is
\[
 \langle\mathcal N(t_\eta),\phi_{t_\eta}\rangle
   =\int_0^{t_\eta}\int(W\otimes W):\nabla\phi\,dx\,ds.
                                                        \tag{21}
\]
Use y=(x-Y(s))/R_h and backward elapsed time. The actual rescaled
adjoint generator is
\[
 \mathbb P[b_s(y)\cdot\nabla-A_s(y)^T]+\delta_\nu\Delta,
 \quad b_s={q(s,Y+R_hy)-q(s,Y)\over R_h},
 \quad A_s=\nabla q(s,Y+R_hy),\quad
 \delta_\nu=\epsilon/R_h^2.
\]
Its spatially affine comparison uses A_c(s)y and A_c(s) on Euclidean
space, with the same positive diffusion in backward elapsed time.
It is solved before being periodized.

For a Fourier test supported away from zero, the affine frequency
support is carried by its exact invertible deformation. Leray's symbol
is smooth on that transported support. Differentiating its Fourier
equations a fixed finite number of times gives
\[
 \sup_s\|\langle y\rangle^jD^\alpha\Phi_{\rm aff}(s)\|_2
       \le H_h^C\delta_h^{-C}
 \quad(j+|\alpha|\le24).                            \tag{22}
\]
The same holds for the finitely many pointwise and L1 seminorms used
below. This is an exponential bound in the finite q clock, hence
subpower in h; no arbitrary-error polynomial estimate is assumed.
The ordinary heat multiplier is retained in these equations.

Periodize the evolving Euclidean test on the torus of side
2pi H_dom, H_dom=L/R_h. The affine drift A_c y is not declared periodic.
The exact image defect contains
\[
 \sum_{j\in\mathbb Z^3\setminus\{0\}}
       A_c(2\pi H_{\rm dom}j)\cdot
                \nabla\Phi_{\rm aff}(y+2\pi H_{\rm dom}j).
                                                        \tag{23}
\]
Its H4 norm is at most \(m_hH_{\rm dom}^{-4}H_h^C\delta_h^{-C}\),
by the fixed weighted bounds (22). Leray and diffusion commute with
periodization on these tests.

On a central fundamental cube, Taylor's theorem gives
\[
 |b_s-A_cy|\le C m_h(R_h/h)|y|^2,\qquad
 |A_s-A_c|\le C m_h(R_h/h)|y|.
                                                        \tag{24}
\]
Their differentiated versions through the H4 forcing orders follow
from the actual q jets. Multiplying (24) by derivatives of the known
affine test and using (22) bounds the H4 forcing by
\[
 m_h[(R_h/h)+H_{\rm dom}^{-4}]H_h^C\delta_h^{-C}.
\]
The unknown adjoint difference uses unweighted H4 energy. Leray is
self-adjoint on solenoidal tests, divergence-free transport cancels,
and commutators use only scaled derivatives of actual q. Its energy
clock is at most C integral m_h. Therefore its C1 norm is bounded by
the same displayed positive h-power error times another H_h^C.
No weighted estimate is imposed on an unknown pressure tail.

The factor R_h/h=h^(1/4)H_h^A tends to zero for every fixed A.
Likewise H_dom^(-4) has a large positive h power. After restoring the
physical-in-rescaled-coordinates gradient factor kappa_h^4, (20) and
these adjoint errors are smaller than the signed pairing (19) times
kappa_h^3. The packet-to-point replacement costs
\((d/R_h)H_h^C\delta_h^{-C}\); choose A sufficiently large after M
so this also tends to zero relative to the polynomial coefficient.

## 7. A cone of signs, scalar duality and strain

The special ray alone is insufficient for (5). For terminal covectors
near N(t_eta), all exact affine Kelvin equations and their first
angular derivatives have bounds H_h^C. The covectors stay away from
zero by invertibility of the deformation. Their response and its
angular derivative therefore have bounds k^2 d^3 kappa_h H_h^C.
The actual central-matrix comparison has a positive h-power error.
Choose M large enough that perturbations of size delta_h cannot
change the sign in (19), including any contamination from the larger
growing Floquet component. The same choice keeps the whole nearby
cotangent history within a small relative distance of the bounded N
history. Its ordinary coarse heat clock still vanishes.

Choose a nonnegative smooth Fourier weight of unit integral on this
annular cone, obtained by rescaling a fixed smooth weight transversely
by delta_h. Its radial coordinate ranges over a fixed positive compact
interval. On the central ray the response is linear in that coordinate
up to the negligible heat factor, so the positive sign is uniform.
Use the real scalar sine kernel f_h with this weight and the terminal
vector r(t_eta); choose its sign so the positive real response in (19)
has positive pairing. Explicitly, for the convention Fourier remainder
equal to -i v, this is the positive sine kernel.

The normalized Fourier weight has derivatives through order four with
L1 norm at most C delta_h^(-4). Fourier integration by parts gives
\[
 \|f_h\|_1\le C\delta_h^{-4}.                         \tag{25}
\]
Its periodized endpoint version is
\(\kappa_h^3 f_h(\kappa_h(x-Y(t_\eta)))\).
The physical torus has unnormalized measure; periodization and this
scaling preserve (25), with no factor L^3. Its Fourier sum samples a
cone containing many lattice points since H_dom delta_h tends to
infinity. Equivalently its pairing is obtained directly by the
periodized test, with the vanishing image error already paid.

Equations (19)--(24) give a positive endpoint pairing at least
\[
 c\,\eta^{-1}d^3k^2\ell^{9/8}\kappa_h^4.
\]
At the endpoint, solenoidality gives the exact scalar identity
\[
 \langle\mathcal N,\mathbb P(r f)\rangle
        =\langle r\cdot\mathcal N,f\rangle.
\]
Dividing by (25) proves (5), even though the interior adjoint is
vector-valued.

For (6), use the exact solenoidal identity
\(\Delta\mathcal N=2\operatorname{div}S(\mathcal N)\).
Move the band-supported inverse Laplacian to the scalar test. Its
resulting tensor kernel has L1 norm at most
\(C\kappa_h^{-1}\delta_h^{-4}\), since its symbol is smooth on the
same annulus and the previous four-derivative estimate applies.
Pairing with S proves (6). This is a bounded band-filter calculation,
not a global L-infinity Korn assertion. It does not select a diagonal
strain component or locate a coherent core.

## 8. What this resolves and what remains

The exact stable projection of the focused stress has a positive
coefficient after the leading growing coefficient cancels. Outer tails,
coarse diffusion, actual-q curvature, full relative stresses, global
pressure and the shrinking cone costs all remain below that coefficient.
The resulting endpoint bounds concern the same generated remainder
through the full finite logarithmic host interval.

The witnessed frequency remains between the original primary and
receiving scales. Its central direction is the existing primary N;
the new information is a nonzero generated polarization component,
not an independent new fast phase. The r endpoint row is different
from the original fixed-normal row, and is not automatically normal
to the receiving phase at t_eta. No next-stage amplifier, full-Q
dominance, persistent affine core or infinite smooth datum is supplied.

In physical units the observation time is h^24 t_eta, the radial test
scale is h^(45/4)H_h^A, and its transverse width may be larger by
delta_h^(-1). Velocity and gradient are multiplied by h^(-14) and
h^(-24). These are still estimates for the existing varying-data
family at fixed physical viscosity, not a singular trajectory.

The next calculation must determine a usable coupling for this actual
generated component after its complete spatial shape and other
components are retained. A signed coarse norm lower bound alone does
not supply that coupling.

## Reproduction

[The bounded symbolic checks](../../experiments/nse_postfocus_normal_source_checks.py)
verify the special pressure-correct Kelvin restriction, cotangent
constraint, stable integral identity, strict integrand sign, Fourier
strain duality, and the rational scale and tail powers. They do not
certify the analytic matching, affine comparison or infinite-dimensional
PDE estimates. The independent affine calculation in
[affine-stress-transport.md](affine-stress-transport.md)
separately derives the inner identity and explains why its special
channel is needed: generic transported source positivity can fail.
