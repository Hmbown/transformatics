# Proposed late nonlinear receiving handover around the actual first-stage NS solution

**Research appendix — 8 September 2026.** **Review status:** a full independent mathematical read by the author of the [original-seed note](original-seed-compatibility-draft.md#8-separate-read-only-review-of-the-late-nonlinear-candidate) found no remaining load-bearing defect at the stated finite late-data scope. The review checked the q C24 / mean H16 / harmonic order13 derivative budget, full pressure terms, residual and viscosity powers, the sharp integrated strain O(ell^(3/8)), absorption of the older H12 factor, and the gradient-error exponent 1/48. The final observation is on an actual particle of the base q, not a claimed particle of the new solution Q. This is a reviewed research derivation outside the registered proof graph, not a formal certificate or an original-time seed construction.

All four appended derivations remain outside the registered proof graph; full formalization and ROOT / `(E′)` remain open. See the [next-transfer review index](../navier-stokes/next-transfer-review.md) for the common scope and remaining estimates.

The original derivation follows, with local references relocated. Its original drafting-status sentences are retained as historical text. Source artifact: `nse-second-nonlinear-handover-20260908.md`; SHA-256 `23088facdc2f801bfe0bff9d53952d67006d96df5de77e7fe45f2213c5742d81`.

---

8 September 2026. Scratch proof for independent review. No repository
promotion, DNS, formal-kernel claim, or original-time seed construction.
This draft treats initial data supplied at the late time t0. ROOT and
(E') remain open. The underlying first-stage solution is not changed.

Inputs: the registered first log-log handover and outgoing-wave results,
and the independently reviewed full linearized second-wave proof in
[the outgoing-wave proof](../navier-stokes/outgoing-wave.md). In particular the
actual first-stage q-characteristic and its robust transient principal
system are available. No spectral instability theorem is imported.

## 1. Claimed finite late-data theorem and parameter order

Fix the first-stage smooth profile and physical viscosity nu>0. Put

    ell=sqrt(log(1/h)),       epsilon=nu h^4,
    Delta=ell^(-3/4),         t0=T_h-Delta,
    k=h^(3/2),               d=h^(5/4),
    a=k ell^(7/8).

All norms below are unnormalized on T_L, L=h^(-10), unless specified.
Let q be the actual smooth first-stage NS solution. Let Y(t) denote the
actual q-particle beginning at the original center at time zero. On
[t0,T_h], q has strain comparable to ell near this particle and bounded
above globally by C ell.

The proposed conclusion is a smooth solution Q of the same unforced NS
equation and viscosity epsilon on [t0,T_h], initialized at t0 by

    Q(t0)=q(t0)+Z(t0),

where Z(t0) is the real, compactly supported, exactly solenoidal curl
packet constructed below. Its strain satisfies

    ||S(Z(t0))||_infinity <=C ell^(7/8),
    ||S(Q(T_h)-q(T_h))||_infinity >=c ell^(9/8).          (1)

The initial added strain is small relative to q's strain ell, while
the final added strain dominates it. It is not initially small in
absolute C1 norm. The comparison will follow from an explicit approximate
solution U and error bounds

    ||Q-U||_2 <=h^(31/8-o(1)),
    ||grad(Q-U)||_infinity <=h^(1/48-o(1)).               (2)

The claim remains subject to the complete proof and independent review.
No datum at the original time zero is asserted for Q.

## 2. Fixed high-order background bounds

The finite-linear proof supplied q derivatives through order five. Higher
uniform derivative bounds needed here do not follow just from smoothness.
They can be obtained from the same first-stage estimates at fixed orders.

Choose the first-stage Sobolev order s0=128. Extend its explicit U_app
bookkeeping, without changing its fields, using primary covector and
amplitude derivatives through 160, global mean through H132, harmonic
amplitudes through 129, and background comparison through H128. These
are conservative fixed orders. The Q0 source at H132 uses amplitude
derivatives through 134 and phase derivatives through 135, within that
budget. The mean H132 bound supplies the C129 coefficients needed for
the harmonic forcing. One final curl derivative then gives U_app H128.
The profile is smooth, and every required norm is finite before h varies.

The fixed H128 comparison interval contains the log-log interval for
small h. The already closed first-stage Lipschitz bound, together with
the standard H128 NS inequality, gives

    ||q||_{H128}+||U_app||_{H128}
                        <=h^(7/4-128-o(1)).

Combining this with the first-stage L2 error h^(11/4-o(1)) gives, for
each fixed r<=24,

    ||D^r(q-U_app)||_infinity
                <=h^[5/4-r-(r+3/2)/128-o(1)].            (3)

After multiplication by h^(r-1), the worst positive exponent at r=24
is 13/256. The refined primary amplitude bound on the terminal interval,
and the positive-power cell-scale smallness of its mean/harmonic
corrections, therefore give

    ||D^r q(t)||_infinity <=C_r ell h^(1-r),
       1<=r<=24,                 t0<=t<=T_h.             (4)

The r=0 field includes an O(1) translating background. It is not claimed
to have size h ell. Each norm order and rate is fixed independently of h.

## 3. Secondary phase, primary receiving amplitude, and sharp time bound

At Y(t0), use the orthonormal first-wave frame (p,n cross p,n). Set the
new covector xi0=4(n cross p) and new unit polarization B0=n, constant
across the initial secondary packet. Transport the phase S by q, with
S(t0,y)=xi0.(y-Y(t0)). Put phi=S/k+pi/2 and xi=grad S.

Let Phi(t,z) be the q flow initialized at z at t0, and let B(t,z) be the
unweighted pressure-corrected polarization initialized at B0. Write
D=partial_t+q.grad, A=grad q, and

    G=-A+2(xi tensor xi)A/|xi|²,    Pi=I-xi tensor xi/|xi|².

Choose a fixed real smooth bump chi supported strictly inside the unit
ball, with chi(0)=1 and bounded fixed derivatives; it is not L2-normalized.
Define

    b(t,Phi(t,z))=a chi((z-Y(t0))/d) B(t,z).

Then Dxi=-A^T xi, Db=G b, and xi.b=0. The robust transient estimate gives
along Y, uniformly for 0<=tau=t-t0<=Delta,

    3<=|xi(t,Y(t))|<=5,
    |B(t,Y(t0))|<=C(1+ell tau),
    |B(T_h,Y(t0))|>=c ell^(1/4).                         (5)

The unweighted flow/cocycle derivatives have background-cell scale h:
through the fixed required orders they are bounded by h^(-r) times
exp(C_r ell^(1/4)). This follows by translating along Y and rescaling
space by h and time by ell; (4) gives uniformly bounded spatial jets.
The normalized-covector equation on S² avoids a growing coefficient in
the highest derivative equation. No time derivative of q is needed.
Across the transported radius-d packet, the unweighted B and xi differ
from their central values by at most

    C(d/h)exp(C ell^(1/4))=h^(1/4-o(1)).                 (6)

Use geometric derivatives through order 22, the mean through H16, and
the harmonic amplitudes through order 13 below. The q C24 budget suffices
for these fixed estimates. For instance Q0 H16 needs receiving amplitude
derivatives through 18 and phase derivatives through 19.

Let F_h stand for a fixed power of ell times exp(C ell^(1/4)); finite
products and finitely many different constants are absorbed by enlarging
it. Volume preservation, product differentiation, and d<h give

    ||D_y^r b||_infinity <=k d^(-r) F_h,
    ||D_y^r b||_2        <=k d^(3/2-r) F_h.              (7)

The sharper zeroth bound is retained separately:

    ||b(t)||_infinity
        <=C a(1+ell tau)+C a(d/h)exp(C ell^(1/4)).        (8)

It is (8), not the loose F_h bound, that controls accumulated strain.

## 4. Exact self-interaction and the sequential corrections

Set d_b=curl(xi cross b/|xi|²). For tangent b,
div b=xi.d_b and div d_b=0. Define the real receiving packet

    Z=Re[(b+i k d_b)exp(i phi)].

It is exactly the real part of a periodic curl, after smooth zero
extension of its vector potential from the transported phase patch.
The exact self-advection is

    (Z.grad)Z=Q0+Re[F2 exp(2i phi)],
    Q0=1/2[(b.grad)b+(div b)b+k²(d_b.grad)d_b],
    F2=1/2[(b.grad)b-(div b)b-k²(d_b.grad)d_b
         +i k((d_b.grad)b+(b.grad)d_b-(div b)d_b)].        (9)

Q0 is one half div(b tensor b+k²d_b tensor d_b). It is a slow spatial
field with zero integral, not a spatially constant Fourier mode.
The scalar pressure amplitude and exact linear residual of Z are

    p_b=2xi.A b/|xi|²,
    F1=i k[(D+A)d_b+grad p_b].                            (10)

First solve the full linearized Euler equation about time-dependent q,
with its global pressure and zero initial data,

    Dm+A m+grad pi_m=-Q0,
    div m=0,       m(t0)=0.                             (11)

The pressure tails of m are retained. Next set

    H1=F1+(i/k)(m.xi)b,       H2=F2,
    Dg_n=Gg_n-Pi Hn,         g_n(t0)=0,     n=1,2.        (12)

Both g_n are tangent to xi and supported on the transported phase patch.
The full mean-to-primary phase interaction in H1 is included before
solving the harmonic equations.

For a tangent complex g define

    C_n[g]=(g+(i k/n)curl(xi cross g/|xi|²))exp(i n phi).

It is an exact curl. Put c_n=i curl(xi cross g_n/|xi|²) and

    p_n=(2xi.A g_n+xi.Hn)/|xi|²,
    pi_n=(i k/n)p_n exp(i n phi).

Direct differentiation gives the exact identity

    (D+A)C_n[g_n]+grad pi_n
       =-Hn exp(i n phi)
          +(k/n)exp(i n phi)[(D+A)c_n+i grad p_n].       (13)

The plus sign of xi.Hn is necessary to cancel the parallel forcing.
The proposed approximation is

    U=q+m+Z+Re C_1[g1]+Re C_2[g2].                       (14)

Every mean/harmonic correction has zero initial data. The exact initial
datum is q(t0)+Z(t0), without a preloaded correcting field.

## 5. Global mean bounds and harmonic derivative bounds

Equation (7), the spatial bounds for xi/|xi|², and k<d<h imply, at every
fixed order used here,

    ||D_y^r d_b||_infinity <=k d^(-1-r)F_h,
    ||D_y^r d_b||_2        <=k d^(1/2-r)F_h.

The full sources in (9)-(10), with no terms omitted, consequently satisfy

    ||D_y^r Q0||_infinity+||D_y^r F1||_infinity
                  +||D_y^r F2||_infinity <=k²d^(-1-r)F_h,
    ||Q0||_{H^r}+||F1||_{H^r}+||F2||_{H^r}
                                      <=k²d^(1/2-r)F_h. (15)

Here factors of ell are absorbed into F_h. The term k²(d_b.grad)d_b is
bounded relative to the leading quadratic source by (k/d)². For F1,
the material derivative of the curl uses

    D(partial_j F_l)=partial_j(DF_l)-A_mj partial_m F_l,
    F=xi cross b/|xi|².

DF is algebraic in A,xi,b and |xi|^(-1), so one further spatial derivative
costs d^(-1) or h^(-1), with h^(-1)<=d^(-1). A time derivative of A, q,
or a pressure operator is not required.

For completeness, use the delta-weighted norm

    ||m||_{r,d}²=sum_{|alpha|<=r} d^(2|alpha|)||partial^alpha m||_2².

Apply partial^alpha to (11) and take its L2 pairing with that derivative
of m. The pressure pairing vanishes because each derivative is
solenoidal. The principal q transport cancels. Its commutators have
coefficients bounded by

    d^(j-1)||D^j q||_infinity
                       <=C ell(d/h)^(j-1)<=C ell.

The differentiated A m terms have coefficients
d^j||D^j A||_infinity<=C ell(d/h)^j. Thus, for every required fixed r,

    d/dt ||m||_{r,d} <=C_r ell ||m||_{r,d}+||Q0||_{r,d}.

With zero initial data, (15), and ell Delta=ell^(1/4), this proves

    ||m||_{H^r}<=k²d^(1/2-r)F_h,
    ||m||_2<=k²d^(1/2)F_h.                              (16)

Uniform expanding-torus interpolation between L2 and H^j, choosing
j>r+3/2, then gives

    ||D_y^r m||_infinity<=k²d^(-1-r)F_h.                 (17)

The additional L2 term in the torus inequality is smaller. This is a
global estimate and does not assume compact support or boundedness of
the Leray projector on L-infinity. The H16 bound suffices for r<=13.
The mean remains divergence-free and mean-zero. Its forcing has zero
integral, and both linear advective terms integrate to zero.

The source (m.xi)b/k in H1 has the same orders as (15), by (7) and (17).
The forced tangent equations (12) therefore yield

    ||D_y^r g_n||_infinity<=k²d^(-1-r)F_h,
    ||D_y^r g_n||_2<=k²d^(1/2-r)F_h,       n=1,2.        (18)

One can prove (18) either along particles or by weighted differentiated
transport equations. The coefficient on the highest g derivative is
bounded by C ell; lower derivatives are handled successively. The scaled
derivatives d^r D_y^r xi are bounded, since they are at most
(d/h)^r exp(C_r ell^(1/4)) for r>=1. Hence the weighted coefficients
are bounded by fixed multiples of ell for sufficiently small h.
No exponentially growing derivative coefficient is placed in a second
Gronwall exponential. Alternatively the triangular derivative induction
produces finitely many products of F_h, still of the same allowed form.

The forced curl identity (13) now has L2 remainder bounded by

    C k³d^(-1/2)F_h.                                    (19)

Indeed DF_g is algebraic in A,xi,g_n,Hn and inverse powers of |xi|.
The curl commutator and grad p_n require one more spatial derivative of
g_n or Hn, priced by d^(-1), and one factor k. They do not require D Hn
or any time derivative of the nonlocal mean pressure.

## 6. Full nonlinear residual and all generated interactions

The linear Euler residuals in (10)-(13) and the exact Z self-interaction
cancel as follows. The mean cancels Q0; the second harmonic cancels F2;
the first harmonic cancels F1 and the leading phase part
Re[(i/k)(m.xi)b exp(i phi)] of (m.grad)Z. Every statement here is an
identity before estimates. The NS residual is obtained by retaining all
remaining cross-products and subtracting epsilon Delta_y from every
added field. The background q cancels by its exact unforced NS equation.

For two lifted nonzero harmonics, the leading amplitudes are tangent to
xi. Contracting the transporting lift with xi supplies a factor k from
its curl correction. Thus the apparent inverse-k fast derivative is
reduced to one envelope derivative. This applies to all signed indices
plus/minus 1 and plus/minus 2, including their mixed products. The
resulting third and fourth harmonics are part of the residual.

The leading sizes of the remaining terms are listed explicitly below.
Every row includes a fixed factor F_h. Terms involving at least one
oscillatory packet are supported in the transported initial packet;
its volume is O(d³) by incompressibility. The mean self-interaction is
estimated globally instead of using such a support claim.

| Remaining term | Pointwise size when localized | L2 size |
|---|---|---|
| Each forced harmonic curl/pressure remainder | — | k³d^(-1/2) |
| Primary–harmonic-correction interactions in both orders | k³/d² | k³d^(-1/2) |
| (m.grad)Z after removing its leading phase part | k³/d² | k³d^(-1/2) |
| (Z.grad)m | k³/d² | k³d^(-1/2) |
| m advecting a harmonic correction, including its fast derivative | k³/d² | k³d^(-1/2) |
| Harmonic correction advecting m | k⁴/d³ | k⁴d^(-3/2) |
| Correction–correction products | k⁴/d³ | k⁴d^(-3/2) |
| Mean self-advection | global | k⁴d^(-3/2) |

For the potentially dangerous mean/correction term, no transversality
of m is assumed: its fast part is bounded by
(k²/d)(k²/d)/k=k³/d². For mean self-advection use
||m||_infinity ||grad m||_2, giving k⁴d^(-3/2). In (m.grad)Z the
uncancelled curl phase part has size (k²/d)(k/d)=k³/d²; it is retained.
The k⁴d^(-3/2) terms are smaller than (19) by k/d=h^(1/4).

Viscosity is also retained. The complete Laplacian of the primary curl
packet has the envelope powers k^(-2), k^(-1)d^(-1), d^(-2), k d^(-3)
times its L2 amplitude k d^(3/2). They are all bounded by k^(-2).
Spatial phase derivatives cost h^(-1)<=d^(-1). The three viscous bounds are

    epsilon||Delta Z||_2 <=epsilon k^(-1)d^(3/2)F_h =nu h^(35/8)F_h,
    epsilon||Delta Re C_n[g_n]||_2
                               <=epsilon d^(1/2)F_h =nu h^(37/8)F_h,
    epsilon||Delta m||_2 <=epsilon k²d^(-3/2)F_h =nu h^(41/8)F_h.

No actual-background mismatch term occurs, because phase, amplitudes and
the mean equation all use q. Collecting the displayed pressures, or
applying the exact periodic Leray projector, gives the full NS residual

    ||R_U(t)||_2 <=C_nu k³d^(-1/2)F_h
                 =C_nu h^(31/8)F_h.                    (20)

This is the computed extra power, not an assumption about the accuracy
of a second correction. Without these cancellations the first source
size is k²d^(1/2)=h^(29/8), which is insufficient for the C1 conclusion.

## 7. Sharp accumulated strain and the required high Sobolev norm

The leading fast derivative of Z is -(b tensor xi/k)sin phi. The
covector is uniformly bounded on the packet. All slow and curl terms
in grad Z are bounded by (k/d)F_h=o(1). From the sharp bound (8),

    integral_{t0}^{T_h} ||grad Z||_infinity dt
      <=C(a/k)(Delta+ell Delta²)+o(1)
      <=C[ell^(1/8)+ell^(3/8)]+o(1).                    (21)

The coherence error in (8) contributes only a positive power of h times
F_h after this integration. Using the loose unweighted exponential
bound in place of (8) would not prove (21).

The corrections satisfy

    ||grad m||_infinity <=k²d^(-2)F_h=h^(1/2)F_h,
    ||grad Re C_n[g_n]||_infinity
                     <=C[(k/d)+(k²/d²)]F_h=o(1).        (22)

Their integrals are o(1). The base q contributes at most C ell Delta
=C ell^(1/4). Therefore

    integral_{t0}^{T_h} ||grad U||_infinity dt
                                            <=C ell^(3/8). (23)

For a fixed s, the primary high Sobolev size is

    k^(1-s)d^(3/2)F_h =h^(27/8-3s/2)F_h.

The harmonic correction is smaller by k/d; the mean is smaller by
(k/d)^(s+1). Background q has the already known bound
h^(7/4-s-o(1)). At s=12 the new primary term dominates the background
as well. More generally that comparison holds when s>13/4; it should
not be asserted for every low Sobolev index. In particular

    ||U(t)||_{H12} <=C h^(27/8-18)F_h.                 (24)

Although the earlier bound for q may carry exp(C ell), its ratio to
the new primary h-power is h^(35/8-o(1)), which tends to zero. This
positive power absorbs that earlier factor before (24) is used. Thus
F_h in (24) really can have the new exp(C ell^(1/4)) form, rather than
silently retaining the longer first-stage growth factor.

The derivative budgets in sections 2-3 supply the one extra curl
derivative needed here. The initial datum q(t0)+Z(t0) has the same H12
bound, with no correction fields present initially.

## 8. Independent strong continuation of the late nonlinear solution

For fixed h, let Q be the local strong unforced NS solution initialized
at t0 by q(t0)+Z(t0). Let E=Q-U, initially zero. Its exact equation is

    E_t-epsilon Delta E
       +P_L[(U.grad)E+(E.grad)U+(E.grad)E]=-P_L R_U.

U and E are divergence-free. Both transport terms (U.grad)E and
(E.grad)E cancel in the L2 pairing. Consequently, on the actual strong
existence interval,

    d/dt ||E||_2 <=||S(U)||_infinity||E||_2+||R_U||_2.

Equations (20) and (23), including the interval length, yield

    ||E(t)||_2 <=h^(31/8) G_h,
    G_h=ell^K exp(C ell^(3/8))=h^(-o(1)),                (25)

for fixed K,C. This estimate does not assume small error derivatives.

Separately bootstrap ||grad E||_infinity<=1. Then (23) bounds the
integrated Lipschitz norm of Q by C ell^(3/8)+Delta. The exact NS H12
energy inequality and the initial H12 bound give

    ||Q(t)||_{H12}+||U(t)||_{H12}
                                   <=h^(27/8-18) G_h.   (26)

These norms may be large as h tends to zero; they are finite for each
fixed h. Uniform expanding-torus Fourier interpolation gives

    ||grad E||_infinity
       <=C ||E||_2^(1-5/24)||E||_{H12}^(5/24)+C||E||_2.

Substitution of (25)-(26) gives exactly

    ||grad E||_infinity
       <=h^[ (31/8)(19/24)+(27/8-18)(5/24) ] G_h
       =h^(1/48) G_h=o(1).                             (27)

For sufficiently small h this is below 1/2 throughout the provisional
interval. Continuity closes the bootstrap strictly. The H12 continuation
alternative prevents a breakdown before T_h, proving existence on the
whole interval. Smooth initial data and the finite integrated Lipschitz
norm give persistence of higher regularity. This continuation argument
is independent of the L2 residual tracking.

For comparison, replacing the residual exponent by 29/8 gives gradient
exponent -1/8-5/(8s), negative for every finite s. The second correction
is needed for this proof, rather than just improving a constant.

## 9. The actual strain observable and its exact scope

Along the base q-particle Y(t), DS=0 keeps phi=pi/2. At that point

    S(Z) =-(b tensor xi+xi tensor b)/(2k)-k S(grad d_b).

Since b is perpendicular to xi, the leading matrix has two nonzero
eigenvalues of magnitude |b||xi|/(2k). At T_h, (5) and chi(0)=1 give
|b|>=c a ell^(1/4), so that magnitude is at least c ell^(9/8).
The remaining displayed curl term is O(k²/d² F_h)=o(1). All mean and
harmonic strain corrections are o(1) by (22), and the true error has
gradient o(1) by (27). Therefore

    ||S(Q(T_h)-q(T_h))||_infinity >=c ell^(9/8).

Because ||S(q(T_h))||_infinity<=C ell, this also gives
||S(Q(T_h))||_infinity>=c' ell^(9/8) for small h. Initially the added
strain is bounded by C a/k+o(1)=C ell^(7/8), and is comparable to that
size at the central point. Thus its ratio to the background strain is
O(ell^(-1/8)) initially and at least c ell^(1/8) finally. The final
observation is at an actual base-q particle, not a claimed particle of Q.

The seed's initial L2 size is of order a d^(3/2)=h^(27/8)ell^(7/8).
Its leading final L2 size is of order h^(27/8)ell^(9/8); the usual
volume-preserving pullback and one integration by parts against the
initial affine phase justify real-packet mass comparability. None of
these small velocity norms is an old global activation threshold.

This completes a proposed analytic proof of the finite late-data
statement (1)-(2), conditional on the previously proved first-stage
and outgoing transient inputs and subject to independent review of this
draft. It does not add a seed at time zero, run NS backward, or show that
the preceding evolution creates the required fine packet. Physical
rescaling retains the original fixed viscosity and the strain ratios,
but different h still give different smooth data. No claim about an
infinite cascade, singularity, global regularity, or full formalization
is made.
