# Smooth supplied-seed strain handover on a log-log interval

**8 September 2026 — PROVED at the restricted analytic scope below.**
ROOT and `(E′)` remain OPEN. This note concerns a finite family of smooth
unforced NS solutions with changing initial data. It is not an infinite
cascade, a full Lean proof, or a novelty claim. Independent analytic
review found no load-bearing defect after the explicit clarifications
recorded in section 9. Node: `nse-loglog-strain-handover`.

## The theorem and its quantifiers

Freeze one real, compact smooth steady Euler profile V and one returning
oblique polarization carrier from
[the Gavrilov theorem](gavrilov-oblique.md). Its positive
Floquet exponent mu and all profile parameters remain fixed. Fix physical
viscosity nu>0. For integers L sufficiently large (with threshold depending
on this fixed profile and nu), put

    h=L^(-1/10),    epsilon=nu h^4,    delta=sqrt(h),
    ell=sqrt(log(1/h)),    T_h=(2/mu)log ell.

On the expanding torus T_L=(R/(2pi L)Z)^3 use unnormalized Lebesgue L2
and inhomogeneous Sobolev norms. Let v_epsilon be the actual NS solution
initialized at V, supplied by the
[fixed-background comparison](steady-background.md).
There is an explicitly defined real, mean-zero, divergence-free curl
packet Z_h(0), with point amplitude h/ell and support width delta, such
that the unforced NS solution q_epsilon initialized at V+Z_h(0) is smooth
through T_h. In these rescaled coordinates,

    ||grad Z_h(0)||_infinity <= C/ell -> 0,
    ||S(q_epsilon(T_h)-v_epsilon(T_h))||_infinity
                                           >= c ell -> infinity.

The positive constants c,C do not depend on L. The final lower bound
is evaluated at a reference Euler particle location, which suffices for
the supremum; no perturbed-NS particle-trajectory statement is claimed.
The reference strain stays bounded, so the final total strain also grows
at least c ell minus a fixed constant.

The explicitly corrected approximation U_app below obeys

    sup_[0,T_h] ||q_epsilon-U_app||_2 <= h^(11/4-o(1)),
    sup_[0,T_h] ||grad(q_epsilon-U_app)||_infinity
                                                <= h^(1/24-o(1)).

Here every subpolynomial loss is a product of exp(C ell) and a fixed
finite power of ell. All derivative orders and constants are selected
before h tends to zero. The proof has a separate H12 continuation
bootstrap; L2 comparison alone would not imply its smooth conclusion.

For the original fixed torus and viscosity, set A_L=L^(7/5) and
u_L(t,x)=A_L q_epsilon(A_L L t,Lx). The common strain factor is A_L L,
and the physical time is T_h/(A_L L). The unnormalized rescaled L2 norm
converts to the physical averaged norm by h/(2pi)^(3/2). Thus these are
admissible fixed-viscosity NS solutions, but their data change with L.
The construction is not a fixed-viscosity small-data C1 instability
statement, and its global high-pass norm remains below the earlier
activation target, as explained in section 8.

## 1. Amplitude convention and exact quadratic identity

Here a means local velocity amplitude, not L2 norm. An amplitude-a packet
occupying volume comparable to delta^3 has L2 size comparable to
a delta^(3/2). In the earlier unit-L2 normalization, its scalar seed
coefficient is eta comparable to a delta^(3/2).

Let S be a real phase, xi=grad S nonzero on a transported local patch,
b a real vector field perpendicular to xi, and

    d=curl(xi cross b/|xi|^2),    g=div b=xi.d,
    phi=S/h+vartheta,
    W=Re[(b+i h d)exp(i phi)]=b cos phi-h d sin phi.          (1)

The equality g=xi.d follows from curl xi=0 and b=-xi cross
(xi cross b/|xi|^2). Thus div W=0 exactly. Its quadratic self-advection is

    (W.grad)W=Q0+Q_c cos(2phi)+Q_s sin(2phi),               (2)

where

    Q0=1/2[(b.grad)b+g b+h^2(d.grad)d]
       =1/2 div(b tensor b+h^2 d tensor d),
    Q_c=1/2[(b.grad)b-g b-h^2(d.grad)d],
    Q_s=-h/2[(d.grad)b+(b.grad)d-g d].                      (3)

Equivalently the nonzero harmonic is Re[F2 exp(2i phi)], with

    F2=1/2[(b.grad)b-g b-h^2(d.grad)d
                +i h((d.grad)b+(b.grad)d-g d)].            (4)

These formulas are exact, with arbitrary curved S. In deriving them,
W.xi=-h g sin phi. This removes the apparent 1/h self-advection. A direct
symbolic substitution with S=z and b=(xy,yz,0) checked every component of
(2)-(3) exactly; the remainder was zero.

For amplitude a and envelope derivatives delta^(-1), uniformly nonzero
xi, and h<=delta, the resulting bounds are

    ||(W.grad)W||_infinity <= C a^2/delta,
    ||(W.grad)W||_2 <= C a^2 delta^(1/2).                   (5)

Fixed-profile time-dependent factors multiply C in an evolving packet.
The true relative L2 nonlinear residual rate is a/delta, not a/h. The
pointwise strain itself can still be of size a/h.

Pressure does not destroy the L2 improvement: the exact nonlinear force
is -P[(W.grad)W], and P is an L2 contraction on every expanding torus.
Its pressure obeys Delta pi=-div((W.grad)W). However, the zero harmonic
requires the full nonlocal projection; replacing it by the pointwise
projection perpendicular to xi is incorrect.

For the factorized leading amplitude b=chi_delta beta, the dangerous
envelope derivative cancels even from Q_c's leading part:

    (b.grad)b-(div b)b
       =chi_delta^2[(beta.grad)beta-(div beta)beta].          (6)

The mean Q0 generally retains the envelope-scale forcing. It is not the
spatially constant Fourier mode: its spatial integral is zero, but it has
nontrivial slow envelope frequencies.

## 2. Why cancellation alone is insufficient

The [handover obstruction](wave-handover.md) independently
proves two exact controls. An exactly self-noninteracting heat shear has
an arbitrary-error initial growth rate comparable to a/h, even when
a/delta tends to zero. A transverse single-phase periodic datum also
generates a nonzero normal slow velocity through its exact pressure.
These are restricted initial-rate identities, not a persistence theorem.
Consequently this proof retains both the generic a/h stability cost and
the full nonlocal mean equation; it does not assume an invariant
transverse-error class.

## 3. A distinct logarithmic-amplitude regime

Freeze one previously proved Gavrilov profile, returning covector, and
real expanding Floquet polarization. All shape parameters stay fixed as
h tends to zero. Let mu>0 be the full-period Floquet exponent and let
the corresponding central polarization beta_*(t) satisfy

    c exp(mu t)<=|beta_*(t)|<=C exp(mu t).

Its central covector N(t) is periodic and bounded away from zero. Fix a
real bump chi with chi(0)=1 and support in a sufficiently small initial
ball; do not L2-normalize it. For definiteness choose

    delta=h^(1/2),       ell=sqrt(log(1/h)),
    a0=h/ell,            T_h=(2/mu)log ell.                 (13)

An O(1) adjustment of T_h to a full orbit period is harmless. Evolve

    b(0,y)=a0 chi((y-x0)/delta)b0

by the exact inviscid pressure-corrected amplitude equation about V, and
transport S exactly by V. Choose S(0,y)=N(0).(y-x0) on the initial patch
and vartheta=pi/2 in (1).
Then S(t,X_V(t,x0))=0, so the reference Euler particle stays at maximal
leading strain rather than at a zero of its sine. No identification with
a perturbed NS material trajectory is used.

At the final time the central amplitude is comparable to h ell; initially
it is h/ell. The main packet strain therefore goes from O(1/ell) to a
quantity comparable to ell. Throughout the interval h/ell<=a(t)<=C h ell,
and h ell=o(delta). The physical NS viscosity remains fixed because the
rescaled viscosity is still epsilon=nu h^4.

Here T_h=O(log log(1/h)), which is inside every fixed-order background
comparison window for sufficiently small h. Every fixed geometric-jet
factor exp(C T_h) is only a fixed power of ell. In the bounds below,
`poly(ell)` means a fixed finite power, selected before sending h to zero.

The sharper primary gradient bound is important. Initial-point continuity
of the cocycle gives on the transported support

    |b-a0 chi_delta beta_*(t)|<=C a0 delta exp(Ct),
    sup_support |xi-N(t)|<=C delta exp(Ct).

Here chi_delta means the initial bump transported by the Euler flow.
The second estimate follows by differentiating the same fixed-profile
cotangent flow with respect to its initial point. Since N(t) is periodic
and bounded away from zero, xi is uniformly bounded above and below on
the whole support through T_h. This uniform bound, rather than a loose
power of ell, is necessary for the next estimate.

Consequently

    integral_0^T ||grad W||_infinity dt
         <= C integral_0^T (a0/h)exp(mu t)dt+o(1)
         <= C ell.                                        (14)

All other terms carry h/delta or delta times a fixed power of ell and
vanish even after integration. Thus the relative-energy factor is
exp(C ell)=h^(-o(1)), despite the final large strain.

The first-order approximation already supplies full Leray-Hopf L2
tracking: its nonlinear and linear residuals have L2 size at most
C h^2 delta^(1/2)poly(ell), so their propagated error is
h^(9/4-o(1)). But that order is insufficient for the strong C1 bootstrap
below. It must not be silently promoted into a smooth handover theorem.

## 4. An explicit second correction: mean plus two harmonic amplitudes

This section specifies the correction that supplies the extra
power in the residual. Write D=partial_t+V.grad, A=grad V,

    G=-A+2(xi tensor xi)A/|xi|^2,
    Pi_xi=I-xi tensor xi/|xi|^2.

For any tangent complex amplitude g and nonzero integer n define

    C_n[g]=(g+(i h/n)curl(xi cross g/|xi|^2))exp(i n phi).
                                                               (15)

It is the curl of (i h/n)(xi cross g/|xi|^2)exp(i n phi), hence exactly
solenoidal. The phase is defined only on the transported patch; all
oscillatory vector potentials vanish smoothly before its boundary and
extend by zero on the expanding torus.

The primary real packet is Z=Re C_1[b]. Define

    p_b=2xi.Ab/|xi|^2,
    F1=i h[(D+A)d+grad p_b],                               (16)

where d is the real curl in (1). Its exact linear Euler residual, with
pressure Re(i h p_b exp(i phi)), is Re(F1 exp(i phi)). Compute Q0 and F2
from (3)-(4), including all terms displayed there.

First solve the **full forced linearized Euler PDE**, with its exact
pressure, for a real slow mean m:

    m_t+(V.grad)m+(m.grad)V+grad pi_m=-Q0,
    div m=0,             m(0)=0.                           (17)

It is equivalent to putting -P Q0 on the right after projection. The
solution is not assumed compactly supported; pressure tails are retained.

Next define two forcing amplitudes

    H1=F1+(i/h)(m.xi)b,       H2=F2,                       (18)

and solve the forced tangent amplitude equations along V:

    Dg_n=G g_n-Pi_xi Hn,     g_n(0)=0,      n=1,2.         (19)

The term (i/h)(m.xi)b is the leading mean-to-primary phase interaction.
Dropping it would leave a residual of the same order as the one being
corrected. Both g_n stay perpendicular to xi. This construction is
sequential: b determines Q0; (17) determines m; then (18)-(19) determine
g1 and g2. No invariant finite-harmonic system or nonlinear fixed point
has been presumed.

For each n the pressure correction is

    q_n=(i h/n)[2xi.Ag_n/|xi|^2+(xi.Hn)/|xi|^2]
                     exp(i n phi).                        (20)

Indeed direct differentiation gives the exact identity

    D C_n[g_n]+A C_n[g_n]+grad q_n
      =-Hn exp(i n phi)
         +(h/n)exp(i n phi)
            [(D+A)c_n+i grad(2xi.Ag_n/|xi|^2
                                      +(xi.Hn)/|xi|^2)],    (21)

with c_n=i curl(xi cross g_n/|xi|^2). This identity supplies the full
parallel pressure term as well as the tangent cancellation.

Let v_epsilon be the actual unforced NS background initialized at V,
using the comparison theorem at the fixed index H32. For the following
bookkeeping it suffices to retain slow phase and primary-amplitude
derivatives through order 24, mean Sobolev estimates through order 20,
and correction-amplitude derivatives through order 14. The H12 norm of
the lifted fields uses at most 13 amplitude derivatives; mean derivatives
through order 14 can be bounded in L-infinity using its H18 estimate.
All coefficients belong to the one fixed smooth Euler profile. The
comparison theorem's finite higher-data requirements are fixed before
h tends to zero. The corrected approximation is

    U_app=v_epsilon+m+Re(C_1[b]+C_1[g1]+C_2[g2]).            (22)

All added corrections have zero initial data. Thus the actual initial
datum is exactly V+Z(0), with no unexplained preloaded mean or second
harmonic.

## 5. Bounds including nonlocal mean tails

The amplitude and its envelope derivatives obey, up to any fixed order,

    ||grad^r b||_infinity<=C h delta^(-r)poly(ell),
    ||grad^r b||_2<=C h delta^(3/2-r)poly(ell).              (23)

These loose derivative bounds coexist with the sharper zeroth and
integrated-gradient estimate used in (14).

Products in (3) and (16) give

    ||Q0||_{H^r}<=C h^2 delta^(1/2-r)poly(ell),
    ||F1||_{H^r}+||F2||_{H^r}
                     <=C h^2 delta^(1/2-r)poly(ell).       (24)

Here and below one may first state the derivative-by-derivative versions
or use delta-weighted Sobolev norms. Transport commutators in the
delta-weighted norms have coefficients bounded independently of delta:
every differentiated V coefficient contains delta^(j-1), j>=1.
The Leray projector commutes with derivatives and is an L2 contraction.
The forced equation (17) consequently yields, for every fixed r,

    ||m||_{H^r}<=C h^2 delta^(1/2-r)poly(ell),
    ||m||_2<=C h^2 delta^(1/2)poly(ell).                    (25)

Uniform expanding-torus Fourier splitting or Gagliardo-Nirenberg then
gives

    ||grad^r m||_infinity
                  <=C h^2 delta^(-1-r)poly(ell).            (26)

For example interpolate L2 and H^k with exponent (r+3/2)/k, choosing
k>r+3/2. This is not an L-infinity boundedness claim for a Riesz transform.
It explicitly retains the nonlocal mean in global norms.

The mean term in H1 has pointwise size
(h^2/delta)*h/h=h^2/delta times poly(ell). Differentiating the tangent ODEs
(19), using (23)-(26), therefore gives

    ||grad^r g_n||_infinity
                   <=C h^2 delta^(-1-r)poly(ell),
    ||grad^r g_n||_2
                   <=C h^2 delta^(1/2-r)poly(ell).           (27)

The amplitudes g_n are supported in the transported packet because their
forcing is supported there. Equation (21) now has remainder L2 size
C h^3 delta^(-1/2)poly(ell): it differentiates g_n or Hn once more and
multiplies by h.

## 6. Every remaining nonlinear interaction

For two lifted nonzero harmonics C_n[u], C_m[v], tangent u,v satisfy

    xi.(u+(h/n)c_u)=(h/n)xi.c_u.

The fast differentiation factor i m/h is therefore reduced to the fixed
ratio i m/n times xi.c_u, an envelope derivative. For the finitely many
indices plus/minus 1, plus/minus 2 here, every such interaction has its
envelope-scale product bound. In particular primary/correction products
have pointwise size at most h^3/delta^2 times poly(ell), hence L2 size
h^3 delta^(-1/2)poly(ell). The generated third and fourth harmonics are
included in this remainder, not discarded.

The interaction m.grad Z has the leading first harmonic displayed in
(18), which has been canceled. Its remaining terms, and Z.grad m, have
the same bound h^3/delta^2. Interactions m.grad C_n[g_n] may contain a
genuine fast derivative, but m*g_n/h is already h^3/delta^2. The slow
mean self-interaction has L2 size at most

    ||m||_infinity ||grad m||_2
                   <=C h^4 delta^(-3/2)poly(ell),

which is smaller by h/delta. The correction/correction products are also
smaller. These include every interaction absent from a principal-mode-only
ansatz.

Finally, the actual-background mismatch is bounded by
||v_epsilon-V||_{W1,infinity}<=C epsilon exp(kappa t), and viscosity
contributes epsilon Delta to each added field. With epsilon=nu h^4,
all these are smaller than h^3 delta^(-1/2) on [0,T_h]. For example the
primary viscous L2 residual is bounded by
epsilon h^(-2)*h delta^(3/2)=nu h^3 delta^(3/2), and the mean's by
epsilon*h^2 delta^(-3/2)=nu h^6 delta^(-3/2).

Thus the **full NS residual**, with all pressures collected or the exact
Leray projection applied, satisfies

    ||R_app(t)||_2<=C_nu h^3 delta^(-1/2)poly(ell)
                  =C_nu h^(11/4)poly(ell).                 (28)

No spectral support invariant is used in (28).

The mean and harmonic corrections have C1 norm bounded by

    C[(h^2/delta^2)+(h/delta)]poly(ell)=o(1).               (29)

Combining (14) and (29) gives

    integral_0^T ||grad U_app||_infinity dt<=C ell.          (30)

For fixed integer s>=3 its Sobolev norm is bounded by

    ||U_app(t)||_{Hs}
              <=C[1+h^(7/4-s)poly(ell)].                  (31)

The primary wave dominates the two corrections in this bound.

## 7. Closed strong-solution bootstrap

Let q_epsilon be the local strong unforced NS solution with initial
datum U_app(0). Let e=q_epsilon-U_app, initially zero. Its exact equation
has the usual three terms U_app.grad e, e.grad U_app, e.grad e, and
forcing -P R_app. The two transport terms cancel in the L2 pairing, so

    d/dt ||e||_2<=||S(U_app)||_infinity||e||_2+||R_app||_2.

Equations (28)-(30), including the length T_h, give on its strong interval

    ||e(t)||_2<=h^(11/4-o(1)),       0<=t<=T_h.             (32)

The o(1) in an exponent denotes only fixed powers of ell and exp(C ell),
which are subpolynomial because ell=sqrt(log(1/h)).

Bootstrap ||grad e||_infinity<=1. The exact standard NS Hs energy
inequality gives

    d/dt ||q_epsilon||_{Hs}
           <=C_s||grad q_epsilon||_infinity||q_epsilon||_{Hs}.

Using (30) and the initial norm in (31) yields

    ||q_epsilon(t)||_{Hs}+||U_app(t)||_{Hs}
                     <=h^(7/4-s-o(1)).                    (33)

Uniform expanding-torus Fourier splitting gives for s>5/2

    ||grad e||_infinity
       <=C_s ||e||_2^(1-5/(2s)) ||e||_{Hs}^(5/(2s))
                    +C_s||e||_2.

Substituting (32)-(33) gives

    ||grad e||_infinity
             <=h^[1/4-5/(2s)-o(1)].                        (34)

Choose the fixed index s=12. The exponent is 1/24-o(1)>0. For sufficiently
small h, (34) is below 1/2, closing the bootstrap strictly. The H12
continuation alternative extends the strong solution through T_h.
The same interpolation gives ||e||_infinity=o(1). This is where the
second correction is essential: replacing 11/4 in (32) by the first
approximation's 9/4 gives a negative exponent for every s.

All finite derivative orders needed for (23)-(34), and the high-index
background comparison, are fixed in advance. The log-log interval fits
their comparison lifetimes for sufficiently small h. No uniformity over
increasingly thin choices of Gavrilov j is asserted.

## 8. Strain handover and its boundary

At t=0, the supplied perturbation has C1 norm O(1/ell). At the reference
Euler particle location X_V(T_h,x0), vartheta=pi/2 and the leading strain
of the primary wave
is

    -(b tensor N+N tensor b)/(2h),

whose nonzero eigenvalues have magnitude |b||N|/(2h), comparable to ell.
The slower derivatives of b, the curl correction, m, g1,g2, and the true
error in (34) contribute o(1) there. Hence the theorem gives

    ||S(q_epsilon(0)-V)||_infinity ->0,
    ||S(q_epsilon(T_h)-v_epsilon(T_h))||_infinity
                                              >=c ell ->infinity.

This is a supplied-seed local strain handover by a family of smooth
unforced NS solutions, on a log-log interval. It is not an infinite-stage
construction or a singularity result. The physical strain ratio is the
same after rescaling, since both fields acquire the common factor A_L L.

The initial rescaled packet L2 norm is comparable to
h delta^(3/2)/ell=h^(7/4)/ell; at the final time the main packet norm is
comparable to h^(7/4)ell. To see the real lower bound with the prescribed
phase, pull back by the volume-preserving Euler flow and set initial
y=x0+delta z. The phase is the linear function delta N(0).z/h.
One integration by parts bounds the oscillatory part of sin-squared
averaging by C(h/delta)poly(ell) times the nonoscillatory mass. Cocycle
continuity makes the amplitude uniformly comparable to the central
Floquet amplitude on this support. The curl correction has relative
size at most C(h/delta)poly(ell), which tends to zero.

The mean, harmonic corrections, and true error are smaller in L2 than
the final primary wave. Therefore the actual difference q_epsilon minus
v_epsilon has the same final L2 order. The physical averaged norms
multiply by h/(2pi)^(3/2), giving initial and final orders
h^(11/4)/ell and h^(11/4)ell, respectively.

For the original high-pass threshold H=L/h, the background H8 bound and
the whole-interval perturbation bound also give

    sup_[0,T_h/(A_L L)] ||P_{>=H}u_L||_{2,av}
           <= C_nu [h^9 poly(ell)+h^(11/4)ell]
            = o(h^(11/10)) = o(H^(-1/10)).

Thus the old absolute activation event is excluded throughout this
window. Local strain dominance and that global high-pass requirement
are different statements.

## 9. Literature and verification scope

Cheverry, [*Cascade of phases in turbulent flows*, BSMF 134 (2006),
33–82](https://www.numdam.org/item/BSMF_2006__134_1_33_0/), distinguishes
high-order approximate waves from a stability theorem. The published
Theorem 6.1 uses a specified modified anisotropic viscosity and a
sufficiently large coefficient. The corresponding result is numbered
Theorem 5.1 in [arXiv v1](https://arxiv.org/html/math/0402408v1).
Neither is imported here as a theorem for epsilon=nu h^4. The formulas
and continuation argument above are direct calculations for isotropic,
unforced NS.

The [exact instrument](../../experiments/nse_loglog_handover.py),
[independent tests](../../tests/test_nse_loglog_handover.py), and
[receipt](../../artifacts/enstrophy_sup/nse_loglog_handover.json) check finite
algebra and scaling. They do not certify the analytic uniform estimates,
existence theorems, or entire proof in Lean.

Validation on this revision: 63 exact controls and 20 focused tests pass.
The combined seven-result suite passes 88 tests; coverage audit is OK at
363 nodes, with three existing warnings. These are reproducibility
receipts at their stated scope, separate from the analytic review.

One independent agent reviewed the complete correction and continuation
argument. Its separate curved-phase calculation used
S=z+x^2/2+y^2/3, nonconstant tangent amplitudes, an incompressible affine
jet and nonzero longitudinal forcing at harmonics 2 and -1. It also
checked all residual powers and the uniform integrated strain estimate.
A second independently reviewed expanding-torus interpolation, the H12
bootstrap and endpoint strain inference. Their requested clarifications
are explicit above: the nearby-covector bound, fixed derivative indices,
reference Euler evaluation point, and real-mass normalization. Neither
review supplies an effective profile threshold or a formal PDE certificate.

## 10. The next transfer is still missing

At the selected point the leading outgoing gradient has the form
A_out=kappa p tensor N, with p.N=0. Thus A_out^2=0, although its symmetric
part has nonzero eigenvalues +/-|kappa||p||N|/2. This elementary calculation
explains why large instantaneous strain does not itself provide the next
expanding Floquet carrier. The outgoing wave is not asserted to be a
scaled Gavrilov steady profile.

The subsequent [outgoing-wave theorem](outgoing-wave.md)
now realizes a finer packet's gain in the exact viscous linearization
about this actual wave, retaining its phase, mean and old background.
Its seed is specified at a later time. A nonlinear second handover and
compatibility with the original initial datum remain unproved. Ultimately an infinite construction must use one
smooth initial datum, one physical viscosity, summable physical times,
compatible seed tails and controlled propagated errors. The finite family
proved here establishes none of those infinite-stage conclusions.
