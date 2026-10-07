# Growing derivative orders for the first-stage background

8 September 2026. **Reviewed quantitative background lemma under the
stated fixed Gevrey-2 hypothesis.** The
[independent derivative-energy review](growing-window-background-review.md)
and root read passed. These are AI-agent reviews, not external expert
acceptance or a formal PDE certificate. The review pins the version before
these introductory and finite-stage accounting clarifications.
This supplies an order-dependent replacement for the
fixed-order background bounds used in the finite-depth recurrence. It does
not continue the full two-wave solution Q beyond its reviewed interval.
Its extra hypothesis is a fixed Gevrey-2 choice of the original profiles.
The previously stated arbitrary smooth profiles do not automatically have
that property. No datum is changed as a function of the proof order.
No DNS or canonical source edits are involved.

Inputs are the full first-stage approximation in
[the log-log theorem](../navier-stokes/loglog-handover.md), the
[logarithmic host](../navier-stokes/logarithmic-host.md), and the
[finite-depth recurrence](finite-depth-profile.md).
The argument below exposes the derivative-order constants instead of
placing all of them inside an unspecified subpower factor.

## 1. Parameters and the additional hypothesis

Set a=1/16 and

    eta_h=ell^a,
    T_h=t_f+(1/8+a)log ell/mu,
    m_h(t)=1+ell^(-1)exp(mu t),
    I_h=integral_0^T_h m_h(t)dt <= C ell^(19/16).          (1)

Here T_h=O(log ell), with the same exact t_f as before. The inequality
in (1) is presently a reference coefficient calculation. The first-stage
argument below proves that actual q has a comparable gradient clock;
it does not give such a clock for full Q. Constants may depend on the
one fixed actual Gavrilov profile and nu, but not on h or the integer N.

Assume the selected compact stationary Euler field V, pressure cutoff,
primary bump, receiving bump and periodic flat phase profile satisfy
fixed Gevrey-2 bounds. In local coordinates, a sufficient convention is

    ||D^j f||infinity + ||D^j f||2
                   <= A_0 A_1^j (j!)², j>=0,             (2)

with the L2 term used only for compact fields and one period for a
periodic profile. Tensor derivatives may be used; dimension factors are
absorbed into A_1. All coordinate maps needed to build V must have the
same fixed Gevrey property on their compact domains, or be analytic.

This is a genuine additional choice, compatible with smooth flat
cutoffs. For example e^(-1/t) for t>0, extended by zero for t<=0,
has derivative bound C^(j+1)(j!)². Cauchy's estimate on a complex disk
of radius theta t gives j!(theta t)^(-j)e^(-c/t); maximizing in t
supplies the second factorial. Forming a smooth step by dividing by
the sum of two overlapping positive copies, then composing with a
quadratic radius, constructs fixed Gevrey-2 bumps. An odd function
s chi(s), supported strictly inside (-pi,pi) and equal to s near zero,
extends periodically to a suitable flat phase profile.

An analytic local Gavrilov velocity/pressure multiplied by a Gevrey-2
function of its pressure has (2) on a fixed compact chart. Its Euler
pressure is obtained by integrating the square of that cutoff against
the local pressure variable. This describes a sufficient choice; it
does not certify (2) for an unspecified smooth profile from an earlier
construction. Fix this choice before taking h to zero.

The chart can be a fixed strictly positive pressure annulus away from the
central circle, with the cutoff vanishing near both annulus boundaries.
[Gavrilov's analytic scalar construction and localization](https://arxiv.org/html/1810.08020v1)
then supply the required local analytic ingredients; the swirl square root
is analytic on this annulus. No analyticity across the central circle or
of a nonzero compactly supported function on all of space is asserted.

The target integer N may grow, subject to N<=C_0 ell^(1/16). The
constant C_0 is fixed. Reserve a fixed multiple of N plus a fixed
number of derivatives for the constructions below. This covers a
recurrence depth J comparable to ell^(1/16), if its separate residual
and full-Q continuation estimates can be closed.

## 2. The useful finite-order energy norm

For 0<r<=1 and an integer N>=4, define the Hilbert norm

    Y_(N,r)(v)²=sum_(j=0)^N r^(2j)||D^j v||2².          (3)

Use full derivative tensors and unnormalized L2 on the expanding
torus. Its Fourier weight is sum_(j=0)^N(r|K|)^(2j). Pressure gradients
pair to zero at every order for a solenoidal v. Leray is retained and
is an L2 contraction. All domain constants below are uniform for L>=1.

Scaled Fourier Cauchy–Schwarz gives, for j<=N-2,

    ||D^j v||infinity <= C r^(-j-3/2)Y_(N,r)(v).        (4)

Consider a divergence-free comparison field U with

    ||grad U||infinity <= C m(t),
    ||D^j U||infinity
      <= C m(t) h^(1-j) K^(j-1)(j!)², 2<=j<=N+1.    (5)

Choose one time-independent weight

    r=h/(C_1 N² K),                                  (6)

with C_1 sufficiently large. Differentiated transport coefficients have
size binomial(n,j) r^(j-1)||D^j U||infinity. For j>=1,

    binomial(n,j)(j!)² <= n^j j! <= n N^(2j-2),
                                           1<=j<=n<=N,

up to an absolute adjustment at j=1. Thus their sum is at most C N m.
The differentiated stretching coefficients contain
binomial(n,j) r^j||D^(j+1)U||infinity. The same estimate, with the
additional (j+1)² factor, is summable under (6). Summing all derivative
levels by Cauchy–Schwarz gives the deliberately coarser C N² m bound.
No high derivative of U is placed in the diagonal exponent by itself.

For the nonlinear difference, the usual solenoidal Sobolev energy
calculation gives the explicit rough bound

    nonlinear energy contribution
           <= C_N r^(-5/2)Y_(N,r)(v)³,
    log C_N <= C N log(N+2).                          (7)

One way to verify this dependence is Fourier transport cancellation,
followed by the mean-value bound on the order-N multiplier. It costs
at most C N 2^N before equivalence with (3). The remaining convolution
contains ||grad v||A0, bounded by a fixed scaled H3 norm. Differentiated
tensor counting and equivalence factors are at most exp(CNlog(N+2)).
Rescaling x=r z contributes exactly r^(-1-3/2). This argument does not
require a constant polynomial in N in the ordinary tame H^N inequality.

Consequently, if v is the exact error from U with residual R and zero
initial error, its full equation obeys

    Y' <= C N² m Y + C_N r^(-5/2)Y² + Y_(N,r)(R).     (8)

The zeroth-order transports U.grad v and v.grad v cancel in the energy
pairing; their differentiated commutators are what (5)–(8) estimate.
Diffusion is nonpositive and is not replaced by a spectral cutoff.

## 3. Why the old background bound must be reorganized

The written steady-background proof uses

    C_V=C_s||V||H^(s+1)

as a diagonal growth coefficient. Under (2), a direct upper bound on
this coefficient is exp(O(s log s)). For s growing like ell^(1/16),
putting that bound into exp(C_V T_h) does not yield a subpower loss.
The fixed-order proof is correct but that substitution is insufficient.

For w=v_epsilon-V, retain higher derivatives of V as triangular
coefficients instead. With a weight r_0=h/(C N²), (2) and the argument
of section 2 give

    Y_(N,r_0)(w)' <= C N² Y_(N,r_0)(w)
             +C_N r_0^(-5/2)Y_(N,r_0)(w)²+C nu h⁴.    (9)

The forcing bound follows from the full residual epsilon Delta V:
r_0^j A_1^(j+2)((j+2)!)² is summable through N when h N^C is small.
The pressure of w remains in the differentiated solenoidal energy.

Starting from w=0, the bootstrap

    Y_(N,r_0)(w) <= h⁴ exp[C N²(1+T_h)]               (10)

closes after increasing C. Indeed the nonlinear coefficient relative
to Y is at most h^(3/2) times exp(CN²T_h+CNlog(N+2)), which tends to
zero for the stated N range. Equation (4) controls C1 and a fixed
H4 continuation alternative gives the actual v_epsilon lifetime.
For every j<=N-2 this also gives

    ||D^j(v_epsilon-V)||infinity
       <= h^(5/2-j) exp[C N²(1+T_h+log(N+2))].        (11)

The large-order bound is not used where a sharper fixed-order bound
suffices. In particular the original fixed-order estimate for
v_epsilon-V is O(h⁴ exp(C T_h)) in C1.

## 4. Quantified jets of the existing first-stage approximation

This section concerns the already explicit approximation

    U_app=v_epsilon+m+Re(C_1[b]+C_1[g_1]+C_2[g_2]),

not a new profile recurrence. Its primary wavelength is h and its
envelope width is delta=h^(1/2). All displayed mean and harmonic
equations and their longitudinal pressures in the log-log source
are retained.

Here is a deliberately nonminimal common constant through the reserved
derivative order N+8:

    K_N=exp[C(N+8)²(1+T_h+log(N+10))].               (12)

Increasing C once depends only on the fixed profiles. The following
finite jet accounting supplies (12).

In this accounting, distinguish intermediate constants
B_N^(s)=exp[C_s(N+8)²(1+T_h+log(N+10))] for geometry, mean, forced
harmonics and residual assembly. There are a fixed number of these
stages. Mean recovery at radius delta/(C N² B_N^(s)) costs
(B_N^(s))^(j+3/2); enlarge the next fixed C_s to absorb it into a
per-derivative jet bound. The final K_N is chosen after these stages,
large enough to dominate every per-derivative factor. Multiplication by
r_N^j then cancels those factors and the factorial growth in residual
jets. The independent review gives this accounting explicitly. These
finitely many stage constants are not the growing correction rounds for Q.

* Leibniz products in Gevrey-2 normalization are bounded by a fixed
  convolution constant: sum_j binomial(n,j)^(-1)<=3. Finite-dimensional
  composition and reciprocal operations on a fixed nonvanishing range
  retain a bound C^n(n!)², with their actual inverse-range cost recorded.
* The steady Euler flow and inverse flow have jets bounded by
  C^n(n!)² exp(Cn(1+t)). Differentiate their exact ODEs: only the first
  derivative of V acts on the top flow jet; the higher derivatives feed
  lower jets. The Gevrey product bound closes this finite triangular
  induction. The cotangent and normalized-direction equations give
  inverse-covector and polarization jets with the safe larger loss
  exp[C(n+1)²(1+t)]. The direction variable stays on the unit sphere;
  a loose inverse-covector bound is not placed in the top amplitude
  coefficient.
* The transported bump brings delta^(-j). Pullback by those flows and
  multiplication by the cocycle therefore give slow primary jets of
  size h delta^(-j) C^j(j!)² exp[C(j+1)²(1+t)]. All phases and potentials
  remain defined on their transported compact chart.
* The global mean equation has forcing Q0 with derivative L2 scale
  h² delta^(1/2-j) and those same finite jet losses. Estimate it in
  (3) with weight delta/(C N² K_N). Its coefficient is the fixed V,
  so its energy growth is at most exp(CN²T_h). Recovery by (4) yields
  the scale h² delta^(-1-j) times the finite constants. No compact
  support is assigned to the mean or its pressure.
* The forced g_1,g_2 equations are linear along V, with the full
  forcing including (m.xi/h)b and the full pressure numerator
  2xi.Ag+xi.H. Their top coefficient remains bounded by C||grad V||,
  and the preceding mean jets are triangular sources. They have slow
  scale h² delta^(-1-j) times the same enlarged constant. All their
  nonzero phase indices are among the fixed original harmonics.
* Evaluation at S/h, the exact curl lift, and the complete residual
  use only finitely many products and at most three additional slow
  derivatives. Chain-rule partitions through order N have count at
  most exp(CNlog(N+2)); the fast derivative scale is h^(-1), while
  delta^(-1) is smaller. These costs fit (12), after enlargement.

For j=0,1 and the residual's L2 norm, use the fixed-order versions of
these estimates. Their losses are exp(C T_h), hence fixed powers of ell.
Whole-primary-envelope comparison with its central Floquet carrier
has error delta exp(C T_h)=o(1). Consequently the same approximation
has sharp gradient and residual estimates

    ||grad U_app(t)||infinity <= C m_h(t)+o(1),
    ||R_app(t)||2 <= h^(11/4) exp[C(1+T_h)].          (13)

All high jets can be bounded in the form (5) with K=K_N. For j>=2,
the larger finite losses are absorbed into K_N^(j-1); j=1 keeps (13).
In the smaller weight r_N=h/(C N² K_N), the residual satisfies

    integral_0^T_h Y_(N,r_N)(R_app)dt
         <= h^(11/4) exp[C N²(1+T_h+log(N+2))].       (14)

The actual-base mismatch is harmless in this count: pair a derivative
of v_epsilon-V globally in L2 with a bounded packet derivative, or
its pointwise bound with the packet's actual L2 volume. Even the
coarser bound (11) leaves L2 residual powers at least 13/4 or 4,
strictly smaller terms than 11/4. There is no global-tail volume shortcut.

## 5. Actual-q comparison at growing order

Apply (8) to e=q-U_app using (12)–(14). For a sufficiently large fixed C,
put

    P_N=C[(N+8)²(I_h+1)
                   +(N+8)³(1+T_h+log(N+10))].       (15)

Then the candidate bound

    Y_(N,r_N)(e) <= h^(11/4) exp(P_N)               (16)

closes its nonlinear bootstrap. The coefficient C_N r_N^(-5/2)Y is
bounded by h^(1/4) exp(P_N+C N²(1+T_h+log(N+2))), which tends to zero.
All sources and the initial error are those of the original q datum;
no extra wave or altered initial correction is introduced.

Recovery by (4), including the weight r_N for every derivative, gives

    h^(j-1)||D^j(q-U_app)||infinity
                       <= h^(1/4)exp(C P_N),
                          1<=j<=N-2.                (17)

The corresponding velocity error is h^(5/4)exp(CP_N). Since

    N=O(ell^(1/16)), I_h=O(ell^(19/16)),
    P_N=O(ell^(21/16)+ell^(3/16)log ell)=o(ell²),     (18)

the gradient bootstrap improves to a positive power of h. The finite
H4 bound for each h supplies strong continuation of actual q through
T_h. In particular (1) becomes a proved upper bound for its actual
gradient clock under the additional Gevrey hypotheses.

Equation (17) is not obtained by differentiating a C1 error. It comes
from the full weighted derivative energy. It also avoids using the
ordinary order-N tame constant inside a leading linear Gronwall factor;
that constant multiplies the small nonlinear error in (8).

## 6. Actual-q deformation, phase and whole-envelope constants

The actual q jets now have, uniformly through the required finite order,

    ||D^j q||infinity
       <= C m_h h^(1-j)K_N^(j-1)(j!)²,
    ||grad q||infinity <= C m_h.                     (19)

The error in (17) is smaller than one in these scaled units and can
be included in the right side of (19). Apply the finite triangular
flow-jet argument to x/h and time variable integral m_h. It gives
flow and inverse-flow derivatives of scale h^(1-j), with logarithmic
constant at most C[j log(j+2)+j log K_N+j I_h]. The same argument for
the normalized cotangent and linear polarization equations, followed
by composition with the prepared original fields, has the safe common
bound

    log C_(N,h) <= C[(N+8)²(I_h+1)
                    +(N+8)^4(1+T_h+log(N+10))]
                 =o(ell²).                          (20)

This pays both forward transport and the original backwards preparation
to t_f; the latter uses a shorter part of the same actual-q history.
The initial scalar normalizations and fixed-profile Floquet constants
add only fixed powers of ell. They do not depend on the proof order.

Consequently the receiver's support diameter is bounded by
d exp(CI_h), its volume remains its transported original volume, and
its inner plateau contains a ball of radius c d exp(-CI_h). The
whole-envelope variation in the coefficient matrix has the factor

    (d/h)exp[C I_h+log C_(N,h)] = h^(1/4-o(1)).        (21)

Spatial jets of phase, inverse covector, bump and polarization can be
charged by the same explicit logarithmic budget, with their usual h
or d scale powers. This is an upper uniformity result; it does not
prove the growing-window outgoing central lower bound or a signed
full-Q transfer by itself.

For a full mean equation about q, use derivative weight
d/(C N² K_N exp(CI_h)), increasing the constant if necessary to cover
the phase jet radius. Differentiated q coefficients of order j>=2
gain (d/h)^(j-1), which absorbs the finite jet constants by (20).
Its top transport/stretching coefficient is at most C N² m_h.
Pressure remains in global differentiated L2, with pointwise recovery
only afterwards. This avoids a claim of L-infinity boundedness for
Leray or a compact-support claim for pressure-generated means.

For the fixed periodic F, integration by parts M+2 times gives

    ||F||A_M <= C^(M+3)((M+2)!)²,
    log ||F||A_M <= C(M+1)log(M+2).                  (22)

The nonnegative central heat clock is contractive on these phase norms.
Its spatial derivatives vanish. The full pressure term xi.H in every
forced profile is retained; its slow derivatives are among (20).
Neither viscosity nor the longitudinal pressure has been omitted from
the derivative ledger.

## 7. What is proved conditionally, and what remains

Under fixed quantitative Gevrey-2 profile choices, the weighted-energy
scheme above supplies an actual first-stage q with the growing-window
clock and high-order comparison needed by a depth of order ell^(1/16).
All quoted logarithmic constants are explicit polynomials of the order,
the actual-q reference clock and T_h, with exponents below ell² in this
range. Arbitrary smooth fixed profiles alone supply no such bound.

The remaining full-Q problem is separate: its receiver clock is
formally ell^(33/16), and the nonlinear recurrence must pay every
growing-depth source, residual and continuation constant against that
clock. The present note neither proves convergence of an infinite
profile series nor supplies a later seed or a Navier–Stokes breakdown.
The finite-count coefficient estimates (5)–(8) and approximation jet
ledger (12)–(14) passed the separately linked independent audit under
the stated Gevrey hypothesis. The receiver operators and final-Q
assembly require their own checks.

For context, [Kukavica–Vicol's radius estimate](https://cims.nyu.edu/~vicol/KV02.pdf)
illustrates why a quantitative radius argument can improve crude
high-Sobolev exponentiation; its theorem also records dependence on the
initial norms. It is not used as a substitute for the scaled,
expanding-torus energy estimates above, nor applied here without
checking its hypotheses to infer the full-Q continuation.
