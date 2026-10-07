# Finite supplied-seed amplification in the full unforced NS equation

**8 September 2026. PROVED at the restricted analytic scope below.
ROOT and `(E′)` remain OPEN.** This is a family of finite-time smooth
solutions with supplied seeds and different initial data at each scale.
It is not an infinite cascade, a singularity, or a global regularity proof.
No novelty claim is made.

For each sufficiently large L, one frozen compact Euler profile and an
explicitly scaled smooth oscillatory seed yield a full unforced NS
solution at the original fixed viscosity. Its absolute Fourier high-pass
norm grows by a factor at least `a₁ ε^(-μc)`, which tends to infinity.
The same proof keeps that norm below the earlier prescribed activation
threshold throughout its time window. The seed's rescaled C¹ size stays
negligible relative to the background. These conclusions must be cited
together.

Inputs: [the oblique ODE theorem](gavrilov-oblique.md) and
[the steady-background comparison](steady-background.md).
Pins: [exact residual and scaling controls](../../experiments/nse_viscous_packet.py),
[independent tests](../../tests/test_nse_viscous_packet.py), and
[receipt](../../artifacts/enstrophy_sup/nse_viscous_packet.json).
Node `nse-viscous-packet-amplification`, outside the critical path into ROOT.

Two agents independently reviewed the linear derivation and nonlinear
corollary, with a separate parent review. The new code has 53 exact
controls and 11 passing focused tests, including missing-pressure,
missing-curl, normalization and exponent negative controls. These checks
validate local algebra and conditional bounds, not the full analytic PDE
estimates. The written proof has no Lean certificate. The existing Lean
certificate covers only earlier cone algebra.

## Reading order

Part I derives the finite-wavelength linearized NS bridge, including its
pressure residual and Fourier estimate. Part II supplies the separate
strong nonlinear continuation argument and high-pass gain. Part III
records the independent review and the stronger activation exclusion.

## Part I. Localized linearized NS amplification

### 1. Result and exact scope

The previously proved principal-ODE multiplier does permit a quantitative
finite-wavelength **linearized** NS realization on a sufficiently short
logarithmic interval. A direct curl construction avoids invoking a
pseudodifferential expansion with untracked time constants.

Fix one of the sufficiently large integers j in
`references/navier-stokes/gavrilov-oblique.md` once and for all. If desired, perform
the fixed L2 normalization used in the steady-background note. Denote the
resulting fixed smooth compact steady Euler field by V. Do not let j depend
on L, h, or epsilon. All constants below may depend on this V, its selected
orbit, and its selected expanding polarization.

Write phi_tau for the flow of V. Choose an initial point x0 on the selected
closed orbit, a returning nonzero physical covector xi0, and a real unit
expanding Floquet polarization b0 perpendicular to xi0. Let

    N(tau) = xi(tau,x0),    b_*(tau) = B(tau,x0,xi0)b0.

Here B is the exact, pressure-corrected amplitude cocycle. For some fixed
mu > 0 and a_* > 0,

    |b_*(tau)| >= a_* exp(mu tau),     tau >= 0.                 (1)

This follows from the positive expanding full-orbit multiplier: mu is its
logarithm divided by the full period, and the remaining Floquet factor is a
nonvanishing continuous periodic vector. The covector N is periodic. Scale
xi0, which does not change the amplitude equation, so that

    min_tau |N(tau)| = 2.                                     (2)

Let v_epsilon be the actual unforced NS background on the expanding torus
T_L, initialized at V, from the steady-background note. Fix its bootstrap
radius and a background rate kappa > 0 so that, throughout its strong
comparison interval,

    ||v_epsilon(tau)-V||_{W^{1,infinity}}
       <= C_b epsilon exp(kappa tau),
    ||S(v_epsilon(tau))||_{L^infinity,op} <= G.                (3)

The constants C_b, kappa, G are independent of L and epsilon. For example,
(3) follows from that note's H^s estimate with s >= 3 and its fixed bootstrap
radius. No perturbed nonlinear solution is assumed here.

For all sufficiently small 0 < h <= delta <= delta0, the construction below
gives a smooth, mean-zero, solenoidal complex datum w^a(0), localized in a
ball of radius delta, with

    1 <= ||w^a(0)||_2 <= 1 + C(h/delta)^2.                    (4)

All L2 norms in this note are unnormalized on T_L. Let w solve the exact
homogeneous linearization about v_epsilon:

    w_tau - epsilon Delta w
      + P_L[(v_epsilon.grad)w + (w.grad)v_epsilon] = 0,
    div w = 0,             w(0) = w^a(0).                   (5)

There are fixed constants C and Gamma > max(G,mu), independent of
L,epsilon,h,delta, such that throughout the background comparison interval

    ||w(tau)-w^a(tau)||_2
      <= C[(h/delta + epsilon/h^2)exp(Gamma tau)
                + (epsilon/h)exp((Gamma+kappa)tau)],         (6)

and

    ||P_{|D_y|>1/h} w(tau)||_2
      >= a_* exp(mu tau)
          - C[(delta+h/delta+epsilon/h^2)exp(Gamma tau)
                   + (epsilon/h)exp((Gamma+kappa)tau)].      (7)

The high-pass in (7) is the actual periodic Fourier projector, with
frequencies k/L. The amplitude is not merely evaluated on one particle:
(7) concerns the norm of an actual solution of (5).

The constants are existential/profile-dependent, as is the already frozen
choice j. A numerical value of Gamma or an effective minimum L is not
supplied. Section 4 explains why a single finite Gamma exists, rather than
silently using a fixed-time remainder at a growing time.

### 2. Local phase, amplitude, and exactly solenoidal packet

Choose a fixed small ball B(x0,delta0) within a compact interior action
annulus. Its images under phi_tau remain in that annulus. The entire annulus
is contained in a fixed Euclidean ball, embedded with a collar in T_L for
all sufficiently large L. The Euclidean flow and all local constructions
therefore agree with their periodic versions.

Take real chi in C_c^infinity(B(0,1)), with ||chi||_2=1, and put

    chi_delta(a) = delta^(-3/2) chi((a-x0)/delta).

On the moving image of the fixed initial ball define the exact transported
phase and its covector by

    S(tau,phi_tau(a)) = xi0.(a-x0),       xi = grad_y S,
    D = partial_tau + V.grad,             A = grad V.

Thus DS=0 and Dxi=-A^T xi. The gradient never vanishes on this patch,
because the particle flow is a diffeomorphism. Let b solve

    Db = -Ab + 2xi (xi.Ab)/|xi|^2,
    b(0,a) = chi_delta(a)b0.                               (8)

The constraint xi.b=0 is preserved exactly. Equivalently,
b(tau,phi_tau(a))=chi_delta(a)B(tau,a,xi0)b0.

Set

    F = (xi cross b)/|xi|^2,
    c = i curl F,
    w^a = h curl(i F exp(iS/h))
        = (b+h c) exp(iS/h).                               (9)

The leading identity in (9) uses xi.b=0. This packet is exactly
divergence-free and has exactly zero periodic mean, because it is the curl
of a smooth periodic vector potential. It is not just projected to leading
order. The bump vanishes smoothly before the boundary of the phase patch;
the vector potential and packet extend by zero. No globally defined linear
phase, integer carrier frequency, or global choice of angle coordinates is
required. Although the packet has compact physical support, it has a
nontrivial smooth Fourier tail.

At time zero, xi0 and b0 are constant, so

    w^a(0) = [chi_delta b0
              + i h curl(xi0 cross (chi_delta b0)/|xi0|^2)]
                exp(i xi0.(y-x0)/h).

The first vector in brackets is real and the correction is purely
imaginary. Therefore its squared complex norm is exactly

    ||w^a(0)||_2^2 = 1
       + h^2 ||curl(xi0 cross (chi_delta b0)/|xi0|^2)||_2^2
       = 1 + O((h/delta)^2),                               (10)

which proves (4). The volume factor delta^(-3/2) is essential here.

### 3. Exact pressure and residual identity

Define the real scalar p and the complex approximate pressure q^a by

    p = 2(xi.Ab)/|xi|^2,          q^a = i h p exp(iS/h).

Equation (8) says Db+Ab=xi p. Also

    grad q^a = (-xi p + i h grad p)exp(iS/h).

Since DS=0, direct differentiation gives the exact Euler residual

    (partial_tau+V.grad)w^a + (w^a.grad)V + grad q^a
       = h exp(iS/h)[(D+A)c + i grad p].                    (11)

In particular there is no uncancelled O(1) pressure term and no hidden
1/h transport term. The factor 2 in p is indispensable. Nor does the
solenoidal correction force a second envelope derivative into the Euler
residual: commuting D past one spatial derivative gives

    D(partial_j F_k)
        = partial_j(DF_k) - (partial_j V_m)partial_m F_k.

The expression DF is algebraic in A,xi,b and |xi|^{-1}; differentiating it
once introduces only first derivatives of b and xi, and one derivative of
A. Thus the Euler residual costs h/delta, not h/delta^2.

Write d=v_epsilon-V. The full linearized-NS residual about the actual
time-dependent background is exactly

    R = h exp(iS/h)[(D+A)c+i grad p] - epsilon Delta w^a
          + (d.grad)w^a + (w^a.grad)d.                      (12)

Its last two terms include the change of the transport phase caused by the
actual NS background. Hence this proof does not assume that Eulerian C1
closeness already proves particle, covector, or polarization shadowing.
It pays for that change directly as a PDE residual, at cost epsilon/h.

Applying P_L to (12) removes the displayed approximate pressure. P_L is an
L2 contraction, uniformly on expanding tori. This accounts for the exact
nonlocal pressure in (5); no locality assumption on the true pressure is
made. The residual is an error of the approximation, not a forcing applied
to the underlying NS background or to (5).

### 4. Uniform-in-time derivative ledger

For a fixed smooth V, the derivatives needed below have at most exponential
growth in tau. Here is a way to verify this without a dangerous estimate
that inserts a growing coefficient into another exponential.

Write n=xi/|xi|. Along a particle,

    X'=V(X),
    n'=-A(X)^T n + (n.A(X)^T n)n,
    b'=[-A(X)+2n tensor n A(X)]b.

The (X,n) system is smooth on the fixed compact annulus times S^2. Its
derivatives through the required finite order have bounded coefficients.
Differentiate its flow with respect to the initial point up to order four;
induction and the variation-of-constants formula give exponential bounds
at each order. Differentiate the linear b equation in the same way. The
coefficient multiplying the highest b derivative stays bounded by a fixed
multiple of ||A||_infinity; lower derivatives supply exponentially bounded
inhomogeneous terms. The magnitude rho=|xi| obeys

    rho'=-(n.A n)rho.

Its reciprocal and the required spatial derivatives likewise have
exponential bounds. Finally compose with the inverse particle flow to
pass from initial coordinates to physical y derivatives. Its finite-order
derivatives also have exponential bounds. These observations produce
constants C_m,gamma_m before h and delta are chosen; only finitely many
derivatives of V, for example a C^5 bound, are required.

Factoring out chi_delta and using det Dphi_tau=1 gives, for m<=3,

    ||grad^m b(tau)||_2 <= C_m delta^(-m)exp(gamma_m tau).

Derivatives of xi/|xi|^2 have similar pointwise exponential bounds without
delta factors. Consequently, after choosing one larger finite gamma,

    ||c||_2 <= C delta^(-1)exp(gamma tau),
    ||(D+A)c||_2 + ||grad p||_2
                    <= C delta^(-1)exp(gamma tau),
    ||w^a||_{H^1} <= C h^(-1)exp(gamma tau),
    ||w^a||_{H^2} <= C h^(-2)exp(gamma tau).                 (13)

For the last bound the raw terms are bounded by fixed exponentials times

    h^(-2), h^(-1)delta^(-1), delta^(-2), h delta^(-3).

All are at most h^(-2) because h<=delta. The normalization by
delta^(-3/2) creates no further L2 loss. The rates can be generated from
finite derivative suprema of the fixed ODE vector fields above; the point
is that none depend on h, delta, epsilon, L, or tau.

Equations (3), (12), and (13) imply

    ||R(tau)||_2 <= C[(h/delta+epsilon/h^2)exp(gamma tau)
                      +(epsilon/h)exp((gamma+kappa)tau)].  (14)

Choose Gamma at least one larger than G and large enough to dominate every
finite geometric rate used here and below. If e=w-w^a, the exact L2 energy
estimate for (5) gives

    d/dtau ||e||_2 <= G||e||_2 + ||R||_2,       e(0)=0.

Convolution with exp(G(tau-s)) in (14) proves (6), with no time-dependent
constant or unrecorded polynomial-in-tau factor.

### 5. From one growing orbit to packet and Fourier high-pass norms

The initial-point derivative of the amplitude cocycle has an exponential
bound. Volume preservation and the L2 normalization of chi_delta therefore
give

    ||b(tau)||_2 >= |b_*(tau)| - C delta exp(gamma_1 tau)
                 >= a_* exp(mu tau)-C delta exp(gamma_1 tau). (15)

This is the spatial localization loss. It explicitly controls the fact
that nearby points and their covectors are not exactly on the selected
periodic carrier. Adding the curl correction costs at most
C(h/delta)exp(gamma tau).

The same initial-point derivative estimates give on the packet support

    |xi(tau,y)-N(tau)| <= C delta exp(gamma_2 tau).

Writing B_a=b+h c, direct differentiation yields

    (-ih grad_y-N(tau))w^a
       = [(xi-N(tau))B_a - i h grad B_a]exp(iS/h).

The previous bounds, with Gamma enlarged once more if necessary, imply

    ||(-ih grad_y-N(tau))w^a||_2
                   <= C(delta+h/delta)exp(Gamma tau).       (16)

This elementary Fourier moment also controls the low frequencies. On a
periodic Fourier mode k/L with |k/L|<=1/h, (2) implies

    |h k/L-N(tau)| >= 1.

Parseval therefore gives

    ||P_{|D_y|<=1/h} w^a||_2
        <= ||(-ih grad_y-N(tau))w^a||_2.                    (17)

Combining (1), (6), and (15)-(17) proves (7). In particular, physical
compactness has not been used to assert spectral compactness. The
high-pass statement follows from an explicit Fourier estimate for this
oscillatory packet.

### 6. Real data and exact normalization

Equations (5), the pressure/Leray projector, and the radial Fourier
high-pass all have real coefficients. Write w=w_R+i w_I. At any prescribed
observation time T,

    ||P_high w(T)||_2^2
       = ||P_high w_R(T)||_2^2 + ||P_high w_I(T)||_2^2,
    ||w(0)||_2^2 = ||w_R(0)||_2^2 + ||w_I(0)||_2^2.

At least one nonzero real initial component consequently has a high-pass
gain ratio at least the complex ratio. Select it and divide by its own
initial L2 norm. This produces a real, smooth, mean-zero, solenoidal datum
of norm exactly one, with the gain asserted below at T. Its initial support
is still in B(x0,delta).

This selection is made for the one prescribed observation time T; the
energy-sum argument alone is not a claim that a single chosen real
quadrature has the complex lower bound at every intermediate time. Also,
a real packet has both positive and negative carrier lobes. It cannot be
described as having only the complex packet's one signed Fourier lobe.
Both lobes have magnitude comparable to 1/h, and the radial high-pass
statement is unaffected.

### 7. The actual exponents at the proposed scales

Fix the physical viscosity nu>0, and take

    h=L^(-1/10),       epsilon=nu L^(-2/5)=nu h^4,
    delta=h^theta,     0<theta<1,
    T_epsilon=c log(1/epsilon).

The four error terms in (7), evaluated at T_epsilon, are bounded by a
constant depending on nu times

    epsilon^[theta/4-c Gamma],
    epsilon^[(1-theta)/4-c Gamma],
    epsilon^[1/2-c Gamma],
    epsilon^[3/4-c(Gamma+kappa)].                           (18)

The desired signal is a_* epsilon^(-mu c). Thus a less restrictive
relative-error condition replaces Gamma by Gamma-mu in the first three
exponents, and Gamma+kappa by Gamma+kappa-mu in the last, together with
c<1/kappa for the background comparison. In either version the admissible
c interval is nonempty because theta and 1-theta are positive and every
rate is finite for the frozen profile.

A simple explicit conservative choice is

    theta=1/2,        c=1/[16(Gamma+kappa)].                 (19)

Then c<1/kappa; the first two exponents in (18) are at least 1/16, the
third is at least 7/16, and the fourth is 11/16. For sufficiently small
epsilon the background strong estimate applies on the full interval, and
the absolute error in (7) is at most C_nu epsilon^(1/16). Therefore

    ||P_{|D_y|>1/h} w(T_epsilon)||_2
         >= a_* epsilon^(-mu c)-C_nu epsilon^(1/16).        (20)

After division by the initial norm in (4), the same holds up to a fixed
constant. Section 6 supplies a real unit datum with

    ||P_{|D_y|>1/h} w_real(T_epsilon)||_2
                            >= c_* epsilon^(-mu c)         (21)

for some fixed c_*>0 and all sufficiently large L. This is a real,
finite-wavelength, high-pass amplification statement for the exact
linearization about the time-dependent unforced NS background.

With the background scaling A_L=L^(7/5), tau=L^(12/5)t, y=Lx, the
physical carrier scale and observation time are

    H=L/h=L^(11/10),
    t_L=c L^(-12/5) log(L^(2/5)/nu).

The gain in physical and rescaled L2 ratios is the same:

    epsilon^(-mu c)=nu^(-mu c)L^((2/5)mu c).

If the rescaled real seed is multiplied by eta_L, its physical averaged
L2 size is eta_L a_L/(2pi)^(3/2), where a_L=L^(-1/10), and the lower bound
is multiplied by that same factor. The argument does not choose eta_L or
provide a nonlinear solution realizing that lower bound.

### 8. What the losses mean, and what remains unproved

* The two leading losses of this first-order construction are delta
  (coherence with the selected orbit) and h/delta (envelope differentiation
  and the exact solenoidal correction). Their balance explains theta=1/2.
  These are proved costs of this construction, not universal lower bounds
  against higher-order or more adapted constructions.
* The viscosity scale epsilon/h^2 is the genuine principal damping scale.
  Along a bounded returning covector its exponent over this window is
  O((epsilon/h^2)log(1/epsilon))=O(nu h^2 log(1/h)), which tends to zero.
  Our residual estimate additionally prices its propagated error.
* The epsilon/h background term pays for using the Euler-transported phase
  instead of an actual-NS-transported phase. It is a valid sufficient loss,
  not a theorem that every possible comparison must lose exactly h^-1.
* Gamma can be much larger than the Floquet rate mu, especially for a thin
  cutoff. The construction proves the existence of a positive gain power;
  it does not prove a useful numerical power for a specified seed ledger.
  Freezing j before sending L to infinity is indispensable.
* The packet is an externally selected initial perturbation. It is not
  generated from the background's tail by this argument. A fixed power of
  L cannot amplify a superpolynomially small smooth tail to a prescribed
  polynomial size. No one-datum infinite-stage conclusion follows.
* Equation (5) omits the perturbation's quadratic self-interaction by its
  definition as a linearization. The exact background is strong, and the
  linear equation is well-posed on its interval, but smoothness or growth
  of a nonlinear solution with this seed has not been proved here.
  The normalized envelope has L-infinity size proportional to
  delta^(-3/2); amplitude and derivative losses must be included when
  selecting eta_L for any nonlinear comparison.
* Neither (20) nor (21) is an autonomous viscous eigenvalue claim or an
  infinite-time instability theorem for one fixed viscous background.
  This is a family of finite-time propagator estimates around different
  concentrated NS backgrounds.

### 9. Primary-source cross-check and why it is not the proof here

Shvydkoy--Friedlander, *The unstable spectrum of the Navier-Stokes operator
in the limit of vanishing viscosity*,
https://arxiv.org/html/math/0509538v1, equations (2.3), (2.5)-(2.7), gives
the same principal pressure-corrected symbol and short-wave cocycle.
Theorem 3.1, especially (3.7), includes the principal viscous attenuation
factor. This is consistent with the scaling above.

Their displayed uniformity is for a fixed bounded time interval; it does
not by itself provide the logarithmic-time constants needed here. Their
Theorem 2.1 concerns eigenvalues beyond the inviscid essential-spectrum
threshold. The present orbit multiplier is not a supplied eigenvalue in
that region. Moreover, their fixed steady viscous comparison may use a
balancing force, while our actual v_epsilon is time-dependent and unforced.
Thus none of those spectral conclusions is imported. Equations (9)-(18)
above provide the direct residual and time-constant accounting instead.

The sole geometric input for a growing orbit remains the internally
reviewed oblique-carrier note, which uses Gavrilov's original construction
and Baldi's Theorem 1.1:
https://arxiv.org/html/1810.08020v1 and
https://arxiv.org/html/2302.02982v1. No new geometric assertion about those
papers is needed for the present finite-wavelength step.

### 10. Suggested independent proof audit

Before promoting this scratch derivation, independently check (i) the
signs in the curl and pressure identity (11); (ii) the single envelope
derivative, rather than two, in its Euler residual; (iii) the finite-order
exponential derivative induction and uniform expanding-torus constants;
(iv) the phase patch's smooth periodic zero extension; (v) the Fourier
moment estimate (16)-(17); and (vi) the real-data selection and its
observation-time quantifier. These are the load-bearing analytic steps.
Exact exponent pins are useful checks but do not replace these arguments.

## Part II. Supplied-seed nonlinear realization

### 1. Precisely what can follow from the linear estimate

For one frozen compact Gavrilov profile with the proved unstable carrier,
there is a family of smooth, mean-zero, **unforced full NS solutions** at
the original fixed viscosity whose supplied high-frequency seeds undergo
an unbounded relative high-pass amplification factor at one prescribed
short physical time. The initial datum changes with L. The high-pass norm
itself remains small under the construction's conservative parameters.

This result does not generate the seed, inherit it from a previous stage,
reach the original activation threshold, or build an infinite cascade. It
also does not imply norm inflation or failure of continuous dependence:
the rescaled perturbation stays small in H3 throughout the interval.

All norms below are unnormalized on the expanding torus T_L until the
physical rescaling is explicitly applied. The Leray projector is the exact
periodic one. All constants depend on one frozen profile and orbit but are
independent of L and its associated h and epsilon.

### 2. Fix all orders and amplitudes before the logarithmic coefficient

Fix physical nu>0 and put

    h=L^(-1/10),     epsilon=nu h^4,
    delta=h^(1/2),   eta=h^6.                                (1)

Use s=3 for the nonlinear perturbation bootstrap. Apply the background
comparison theorem at the fixed index 9, not only at index 3. Because V is
smooth and compact, its H9 and H11 norms are finite. That theorem supplies
a rate kappa9 and a fixed bootstrap bound B such that

    ||v_epsilon(tau)-V||_{H9}
                     <= C epsilon exp(kappa9 tau),
    ||v_epsilon(tau)||_{H9} <= B                            (2)

on tau<=c log(1/epsilon), for all sufficiently small epsilon whenever
c<1/kappa9. The H3, H4, and W^{2,infinity} bounds used below follow uniformly
from (2); so does a fixed strain bound G.

Take the linear packet proof with this higher-index background comparison
rate. This changes constants but none of its powers. Let Gamma and mu>0 be
its fixed remainder and Floquet rates. The exact linearized equation then
has a real, unit L2 initial datum f_h with

    ||P_{|D_y|>1/h} w(T)||_2 >= a epsilon^(-mu c),
    w(0)=f_h,                    T=c log(1/epsilon),          (3)

for a fixed a>0 and all sufficiently large L, provided c is suitably
small. The real initial component may be chosen for this observation time
T, as in the linear note. Its sign and phase are therefore part of the
chosen initial-data family.

We now check the uniform Sobolev normalization needed to use (3).

### 3. Real quadratures have uniformly nonvanishing initial mass

At tau=0 the complex curl datum has the form

    f_complex = [chi_delta b0 + i h d0] exp(iS0/h),
    d0 = curl(xi0 cross (chi_delta b0)/|xi0|^2),
    S0 = xi0.(y-x0),       ||chi_delta||_2=1, |b0|=1.

Consequently

    Re f_complex = chi_delta b0 cos(S0/h)-h d0 sin(S0/h),
    Im f_complex = chi_delta b0 sin(S0/h)+h d0 cos(S0/h).

One integration by parts in the constant xi0 direction gives

    |integral chi_delta^2 exp(2iS0/h)|
       <= C h ||grad(chi_delta^2)||_1 <= C h/delta.           (4)

The cross terms in either squared norm are bounded by
C h||chi_delta||_2||d0||_2<=C h/delta, and the correction squares by
C(h/delta)^2. It follows that

    ||Re f_complex||_2^2 = 1/2+O(h/delta),
    ||Im f_complex||_2^2 = 1/2+O(h/delta).                   (5)

Each is at least 1/4 for small h. Thus normalizing whichever real component
was selected in (3) loses at most a fixed factor. Leibniz differentiation
of the initial linear phase and bump, using h<=delta, gives

    ||f_h||_2=1,    ||f_h||_{H1}<=C h^(-1),
    ||f_h||_{H3}<=C h^(-3).                                (6)

For example a differentiated correction term has size bounded by
h^{1-a}delta^{-(m+1-a)}<=h^{-m} for 0<=a<=m. The L2 normalization of the
bump already accounts for its delta^(-3/2) pointwise factor. There is no
additional delta^(-3/2) loss in (6).

The datum is real, smooth, divergence-free, mean-zero, and initially
supported in the same radius-delta ball. It has two signed Fourier lobes.
The linear note's Fourier-moment argument at time zero, or direct
integration by parts, also gives

    ||P_{|D_y|<=1/h} f_h||_2 <= C h/delta = C h^(1/2).        (7)

### 4. Exact linear Sobolev estimates

The exact real w in (3) solves the homogeneous linearization about the
actual v_epsilon. The uniform H4 bound for v_epsilon in (2), transport
cancellation, and uniform expanding-torus Sobolev estimates give finite
rates K3,K1>=1 such that

    ||w(tau)||_{H3} <= C h^(-3)exp(K3 tau),
    ||w(tau)||_{H1} <= C h^(-1)exp(K1 tau).                 (8)

For H1 the differentiated transport terms require only fixed W2,infinity
coefficient bounds, supplied by H4. For H3, the term (w.grad)v is bounded
using the fixed H4 background norm. There is no h-dependent coefficient in
either energy inequality. The viscous terms are dissipative and may be
dropped for these upper bounds.

In particular, H3 embeds into W1,infinity, and

    ||grad w||_infinity <= C h^(-3)exp(K3 tau),
    ||(w.grad)w||_2
       <= ||w||_infinity ||grad w||_2
       <= C h^(-4)exp((K3+K1)tau).                          (9)

These estimates concern the exact all-mode linear solution, not just its
localized WKB approximation.

### 5. Strong full NS existence through the same time

Let q_epsilon be the local strong solution of the full unforced NS
equation with initial data

    q_epsilon(0)=V+eta f_h.                                 (10)

Write r=q_epsilon-v_epsilon. Its exact equation is

    r_tau-epsilon Delta r
       +P[(v.grad)r+(r.grad)v+(r.grad)r]=0,
    r(0)=eta f_h.                                          (11)

The standard differentiated energy calculation, using (2) and the uniform
Sobolev constants, yields for z=||r||_{H3}

    z' <= K_r z+C_3 z^2,
    z(0)<=C eta h^(-3)=C h^3.                              (12)

Fix K_n>=K_r+C_3, K_n>=1. On the bootstrap z<=1,

    z(tau)<=C h^3 exp(K_n tau).                             (13)

If c<3/(8K_n), its upper bound at T is

    C_nu h^(3-4cK_n)=o(1),

with exponent greater than 3/2. For sufficiently large L it remains below
1/2, closing the bootstrap strictly. The H3 continuation alternative then
proves existence of q_epsilon on the entire [0,T]. This is the required
strong-solution argument; nonlinear smoothness has not been inferred from
the L2 residual comparison. Smooth initial data and standard persistence
of regularity give smoothness on this finite interval.

### 6. Nonlinear error relative to the exact linear evolution

Define

    e=q_epsilon-v_epsilon-eta w = r-eta w,       e(0)=0.

Subtracting the background and linear equations gives the exact identity

    e_tau-epsilon Delta e
       +P[(v.grad)e+(e.grad)v
           +eta(w.grad)e+eta(e.grad)w+(e.grad)e]
          =-eta^2 P[(w.grad)w].                             (14)

All three transporting velocities v,w,e are divergence-free. Thus the
v.grad e, w.grad e, and e.grad e terms cancel in the L2 energy pairing.
The remaining estimate is

    d/dtau ||e||_2
       <= [G+eta||S(w)||_infinity]||e||_2
                +eta^2 ||(w.grad)w||_2.                    (15)

By (9), eta||grad w||_infinity<=C h^3 exp(K3 tau)=o(1) on
[0,T] if c<3/(8K3). It is therefore <=1 for sufficiently large L.
Choose a fixed K_e>=G+K3+K1+2. Applying (9) in (15) gives

    ||e(tau)||_2 <= C eta^2 h^(-4)exp(K_e tau).              (16)

At the observation time, division by eta=h6 gives

    ||e(T)||_2/eta <= C_nu h^(2-4cK_e)=o(1)                 (17)

if c<1/(4K_e), with exponent greater than one. This error estimate is
derived after the independent H3 bootstrap has guaranteed the true
nonlinear solution exists throughout the comparison interval.

### 7. Absolute high-pass amplitude and its initial value

The fixed H9 background comparison also supplies a uniform H8 bound. By
the actual Fourier multiplier, at every tau in [0,T],

    ||P_{|D_y|>1/h} v_epsilon(tau)||_2
                    <= C h^8 ||v_epsilon(tau)||_{H8}
                    <= C h^8 = o(eta).                     (18)

This is a finite-order Sobolev tail bound for the evolving background. It
does not assert inherited compact spectral support. All orders (3,6,8,9)
were fixed before choosing c, so there is no circular choice of a tail
order after its growth constant has already fixed the time interval.

Combining (3), (17), and (18) yields for the full nonlinear solution

    ||P_{|D_y|>1/h} q_epsilon(T)||_2
       >= a eta epsilon^(-mu c)
                  -C h^8-C_nu eta h^(2-4cK_e).              (19)

At time zero, (7) and the H8 bound for V give

    eta(1-o(1))
       <= ||P_{|D_y|>1/h} q_epsilon(0)||_2
       <= eta+C h^8.                                       (20)

Therefore, for sufficiently large L, there is a fixed a1>0 such that

    ||P_{|D_y|>1/h} q_epsilon(T)||_2
      /||P_{|D_y|>1/h} q_epsilon(0)||_2
                    >= a1 epsilon^(-mu c) -> infinity.     (21)

This is a supplied-seed amplification result for the absolute high-pass
norm of the full unforced solution. It is not merely growth of its
difference from the background. The actual perturbation difference has
the same gain lower bound even without using (18).

### 8. One nonempty choice of the logarithmic coefficient

All rates are fixed once the profile and the fixed Sobolev orders above
are fixed. Choose

    0<c<min{1/[16(Gamma+kappa9)],
             3/(8K_n), 3/(8K3), 1/(4K_e)}.                 (22)

Every entry is positive. The first term supplies the linear proof's
absolute-error margin and the H9 background comparison lifetime. The
other three supply respectively the nonlinear H3 bootstrap, the small
eta grad w coefficient, and the nonlinear remainder bound. No numerical
claim about the size of c is made.

On the fixed physical torus define

    u_L(t,x)=A_L q_epsilon(tau,Lx),
    A_L=L^(7/5),          tau=L^(12/5)t.

This solves the full unforced NS equation with the original fixed nu.
The physical high-pass threshold and observation time are

    H=L/h=L^(11/10),
    t_L=c L^(-12/5)log(L^(2/5)/nu).

The physical averaged L2 high-pass norms acquire the common factor

    A_L L^(-3/2)/(2pi)^(3/2)
             =L^(-1/10)/(2pi)^(3/2).

Thus their ratio still satisfies (21). The initial high-pass norm is
comparable to L^(-1/10)h6=L^(-7/10), and the proved final lower bound is
comparable to

    L^(-7/10) epsilon^(-mu c)
             =nu^(-mu c)L^(-7/10+(2/5)mu c).                (23)

Because the conservative first restriction in (22) has Gamma>mu,
mu c<1/16. In particular the lower bound in (23) still tends to zero.
It is far below the earlier prescribed threshold H^(-1/10)=L^(-11/100).
The theorem asserts an increasing amplification factor, not completion of
that stronger activation target. Also, (13) supplies an upper bound
tending to zero for the rescaled perturbation in H3 throughout [0,T].

### 9. Remaining scope and review coverage

This argument uses an explicitly supplied polynomially small seed, a
profile-dependent positive c, and different smooth initial data for each
L. It does not show an NS trajectory creates that seed, maintains it from
an earlier scale, or reaches an order-one background-relative amplitude.
It does not overcome the smooth-tail/infinite-stage obstruction or prove
singularity, global regularity, or ROOT.

The independent analytic reviews verified the actual linear H1 and H3 estimates
under the fixed H9 background bound; the real quadrature normalization;
the exact cancellations in (14)-(15); the separate continuation argument
in (12)-(13); and the fixed-order tail bookkeeping in (18)-(22). The
linear packet theorem was independently checked; its principal-ODE input
alone does not suffice for this corollary.

## Part III. Independent review and the actual activation exclusion

The independent review checked the exact curl/pressure cancellation,
one-envelope-derivative residual cost, normalized-direction exponential
jet estimates, local phase zero extension, and uniform Fourier moment
bound on expanding tori. The nonlinear review checked the uniform real
quadrature norms, fixed H⁹ background, differentiated H¹/H³ estimates,
strong continuation bootstrap, all three transport cancellations, and the
fixed-order background tail. No must-fix gap was found at the stated
finite supplied-seed scope. These reviews do not provide formal kernel
coverage of the PDE argument.

There is a stronger conclusion than observing that the displayed lower
bound is below the old target. Write q=v+r as in Part II. Uniformly over
0≤τ≤T, the actual Fourier multiplier and the H³ bootstrap give

\[
\|P_{>1/h}q(\tau)\|_2
\le C h^8+h^3\|r(\tau)\|_{H^3}
\le C h^8+C_\nu h^{6-4cK_n}.
\]

The common physical averaged-L² scaling factor is a constant times
L^(-1/10)=h. Therefore the full nonlinear physical solution satisfies

\[
\|P_{>H}u_L(t)\|_{2,\mathrm{av}}
\le C_\nu\bigl(h^9+h^{7-4cK_n}\bigr),
\qquad 0\le t\le t_L.
\]

The chosen coefficient has c<3/(8K_n), so `7−4cK_n>11/2`.
The original target is `H^(-1/10)=h^(11/10)`. Their ratio tends to zero.
Thus the target is actually excluded throughout this construction's
window. Its unbounded relative gain is compatible with that exclusion
because the initial high-pass mass is much smaller still.

Moreover, `||r||C¹≤C||r||H³=o(1)` in rescaled coordinates. The seed's strain
cannot take over the fixed background's order-one strain in this regime.
This is an obstruction for the specified construction and estimates,
not for every NS trajectory or every wave-packet method.

### Next execution

The independent exact pins and joint registration of amplification and
activation exclusion are complete. Next, identify a mechanism that
creates/inherits a sufficiently large seed
and controls feedback through an actual transfer of dominant strain.
The small-H³ bootstrap above cannot certify that handover. The
[wave-handover note](wave-handover.md) identifies the exact
self-interaction cancellation, its failed generic stability extension,
and pressure-generated normal mean flow. Do not improve the tiny-gain
constants or repeat this construction as a cascade.

Keep one physical viscosity and one smooth initial datum as the eventual
infinite-stage requirement. Different solutions indexed by L do not meet
that requirement. No new DNS is authorized or needed by this draft.
