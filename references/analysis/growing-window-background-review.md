# Independent review of the growing-order background estimate

8 September 2026. **PASS for sections 2--5 under the stated fixed Gevrey-2
hypothesis and the referenced exact first-stage equations.** This is a
written mathematical review, not a formal PDE certificate. It does not
review section 6's full receiver/operator package or prove continuation of
the full two-wave Q_h. ROOT, E-prime and FORCED-D remain OPEN. No DNS.

Reviewed source:
[growing-window-background.md](growing-window-background.md),
SHA-256

```text
3004a6cd9b1de908d3cf75bcb079140f7cba7de943b5ac9c2586b249096e064f
```

The exact mean/harmonic equations and residual cancellations were read
against [the log-log source](../navier-stokes/loglog-handover.md), SHA-256
`52275bebfa88f8ff626b592548511868f1cb4c8edaf56aacaa0097c29167d9d9`.
Those fixed equations, including both longitudinal pressure numerators,
are reused here. This review independently checks how their constants
depend on the growing derivative order. It does not certify the Gevrey
hypothesis for an unspecified previously selected smooth profile. The
analytic local-coordinate inputs may be restricted to one fixed support
annulus away from the central circle, with the cutoff vanishing near
both annulus boundaries. No analyticity across that circle is assumed
or needed in this audit.

## 1. Weighted energy without derivative loss

For full derivative tensors, the exact Fourier weight of Y_(N,r)² is
sum_(j=0)^N(r|K|)^(2j). It has no unrecorded exponential tensor-equivalence
factor. For j+2<=N, retain just its jth, (j+1)st and (j+2)nd terms.
Fourier Cauchy--Schwarz gives the claimed

    ||D^j v||infinity <= C r^(-j-3/2) Y_(N,r)(v).

The lattice factor L^(3/2) cancels the normalization factor
(2pi L)^(-3/2). The result is uniform for L>=1 and 0<r<=1; no
domain-independent Poincare inequality is assumed.

For the U.grad v commutator, the coefficient connecting order n to
order n-j+1 is binomial(n,j) r^(j-1)||D^j U||infinity. The elementary
bound used in the source is valid:

    binomial(n,j)(j!)² <= n^j j! <= n N^(2j-2).

For j>=2, use j!<=j^(j-1)<=N^(j-1); j=1 is exact. With
r=h/(C_1 N² K), the coefficient sum is bounded by C N m.
Stretching terms connect order n to order n-j and have coefficients
binomial(n,j)r^j||D^(j+1)U||infinity. Their extra (j+1)² factor is
summable against C_1^(-j). The j=0 term uses only ||grad U||infinity.
Summing derivative levels by Cauchy--Schwarz gives the safe C N² m
bound. All non-top derivatives of U remain off the diagonal of this
finite hierarchy.

For v.grad v, transport cancellation removes the top differentiated
advection. The remaining Fourier commutator is bounded by an
order-dependent constant times ||grad v||A0 Y_(N,r)(v)². A bound
C N 2^N, followed by at most exp(CN log(N+2)) tensor/weight accounting,
is sufficient. Scaled Fourier recovery from the first three derivative
orders gives

    ||grad v||A0 <= C r^(-5/2)Y_(N,r)(v).

Thus the nonlinear contribution is cubic in Y and yields precisely
the quadratic term in the differential inequality for Y. It loses
no derivative beyond N. This large order constant multiplies the
small nonlinear error; it is not placed in the linear Gronwall clock.
Pressure cancels in every differentiated solenoidal pairing, and the
ordinary viscous term has the correct nonpositive sign.

## 2. The actual steady background

For w=v_epsilon-V, the Gevrey derivative bound and the weight
r_0=h/(C N²) control the full epsilon Delta V forcing by C nu h⁴
in Y. Consecutive weighted factorial terms have ratio at most C h
over the reserved range after enlarging the fixed denominator.
Higher V derivatives therefore produce a C N² linear coefficient,
rather than exp(CN log N) as a diagonal growth rate.

At the proposed error size h⁴ exp(CN²(1+T_h)), the nonlinear rate is

    h^(3/2) exp(O(N²T_h+N log(N+2))),

which tends to zero uniformly for N<=C_0 ell^(1/16). The bootstrap
closes. Recovery gives h^(5/2-j) times the recorded finite losses;
the factor r_0^(-j-3/2) contributes only O(N log(N+2)) to their
logarithm when j<=N. These powers agree with (11).

For each h, Y controls a finite H4 norm and the gradient error stays
small, so the separate steady background has the required strong
lifetime. The old fixed-order C1 estimate can still be used where
it is sharper; it is not differentiated to obtain the growing-order
bound.

## 3. Closing the first-stage jet ledger

There is a useful notational refinement of (12)--(14). Intermediate
radius constants and the final K_N should be distinguished. Recovery
of a mean estimated with radius delta/(C N² B_N) costs
B_N^(j+3/2), not just B_N. This is compatible with the proposed K_N
after finitely many fixed enlargements, but the cancellation should
be made explicit. The following finite accounting supplies it.

Put M=N+8 and H=1+T_h+log(N+10). Use a sequence of constants

    B_N^(s)=exp(C_s M² H),

where s labels geometry, mean, the two forced harmonics, and residual
assembly. There are only finitely many such stages, independently of
N. Choose each C_s larger than the previous constants by a fixed
factor. These are not the growing-depth correction rounds for Q_h.

The Gevrey Leibniz convolution is uniformly bounded because
sum_j binomial(n,j)^(-1)<=3. Composition, reciprocals on the stated
nonvanishing range, flow differentiation and cotangent/polarization
jets therefore give bounds of the schematic form

    size × scale^(-j) (B_N^(s))^(j+1) (j!)²,

after fixed enlargements. The flow top jet sees only grad V; lower
jets feed triangular sources. Bounds exp(C(j+1)²(1+t)) fit this
form. Any inverse-covector range loss from the fixed Euler flow is
charged in B_N^(s); it is not used as a large top amplitude rate.

The mean forcing has unnormalized derivative L2 size
h² delta^(1/2-j), multiplied by such jet constants. Use the
intermediate weight delta/(C M² B_N^(s)). The factorial/radius factors
are summable, and the weighted forcing and mean energy estimates
cost only a fixed power of B_N^(s). The coefficients in the mean
equation are the fixed V, with linear clock C M² T_h. Pointwise
recovery then gives

    h² delta^(-1-j)
      (C M² B_N^(s))^(j+3/2) (B_N^(s))^c,

for a fixed c. This is bounded by the schematic jet form with the
next B_N^(s+1). It does not require replacing log K_N by N³H.
The mean keeps its global L2 norm and is never assigned compact support.

The equations for g_1,g_2 have bounded top polarization coefficients
along the fixed Euler flow. Their sources include the already bounded
mean, the complete fast mean-primary coupling, and the longitudinal
pressure. Gevrey products and the same triangular flow accounting
give the next finite-stage constants, with pointwise slow scale
h² delta^(-1-j). Their true compact wave support supplies their L2
volume when applicable.

Finally, each residual is a finite product or curl/pressure/viscous
expression. Its differentiated L2 bound can be written schematically as

    h^(11/4) h^(-j) B_N^(c_1 j+c_2) ((j+c_3)!)²,

with fixed c_1,c_2,c_3, plus terms carrying strictly better h powers.
Here B_N is one of the preceding finite-stage constants. Choose the
final K_N=exp(C M²H) with C large enough to dominate B_N^(c_1+1)
and all preceding stages. Multiplication by
r_N^j=[h/(C_1 N² K_N)]^j cancels the h^(-j), per-derivative B_N
and factorial factors. The fixed derivative shifts leave only a
fixed power of B_N and a fixed polynomial in N. Summing the finitely
many derivative levels and integrating over time therefore leaves

    integral Y_(N,r_N)(R_app) dt
       <= h^(11/4) exp(C N²(1+T_h+log(N+2))),

as in (14). The same final enlargement gives the required U_app
jet form K_N^(j-1)(j!)² for j>=2: the ratio (j+c)/(j-1) is bounded
by a fixed constant on this range. The first derivative instead uses
the sharp fixed-order bound in (13).

Thus recovery factors have been charged, rather than treated as a
single unspecified subpower constant. A finite chain of changes in
C_s suffices because the first-stage approximation has a mean and
two harmonic corrections, not a growing number of them.

The reserved eight derivatives are sufficient for these equations.
An order-N residual needs at most N+3 slow derivatives of a lifted
harmonic. Its mean source needs pointwise mean derivatives through
N+3, obtainable from global mean order N+5. The complete Q0/curl
forcing requires primary and covector jets through N+7; the phase
gradient adds one flow derivative. This fits N+8. The steady-base
mismatch requires no larger order. This count does not discard the
h²(d.grad)d term of Q0 or any viscous curl derivative.

## 4. Residual powers, sharp clock and actual-q bootstrap

The complete first-stage cancellation leaves L2 residual
h³ delta^(-1/2)=h^(11/4). The residual includes the generated third
and fourth harmonics; it does not assume a finite Fourier invariant
subspace. Mean self-interactions use a pointwise factor and global
L2 factor, giving h⁴ delta^(-3/2)=h^(13/4), not a fictitious mean
support volume.

For the actual-base mismatch, the coarse pointwise w bound is
h^(5/2-j) times finite constants. With a packet of amplitude h and
volume delta³, pairing w with one fast packet derivative gives
h^(5/2) delta^(3/2)=h^(13/4); pairing grad w with the packet gives
the same power. Alternatively global L2 w costs h⁴ with the
bounded packet derivative. Extra differentiated fast powers are
paid by r_N. These are the two claimed safe powers, 13/4 and 4;
neither assigns compact volume to a pressure-generated tail.

For the sharp low-order estimate, the Euler-flow envelope comparison
error is delta exp(C T_h)=o(1), with C fixed. The original central
primary wave has bounded nonzero periodic covector and amplitude
(h/ell)exp(mu t). The small mean/harmonic gradients and steady-base
error retain fixed-order losses exp(C T_h), yielding
||grad U_app||infinity<=C m_h+o(1). No K_N is substituted for this
sharp gradient coefficient.

In (15), the N² I_h term pays the weighted linear energy. The N³H
term safely covers the radius factors needed for recovery through
order N. With the residual (14), the candidate weighted error has
nonlinear rate

    h^(1/4) exp(P_N+O(N²H+N log(N+2))),

which vanishes even after multiplication by T_h=O(log ell). Recovery at
derivative j gives exactly

    h^(j-1) r_N^(-j-3/2) h^(11/4)
       = h^(1/4)(C N² K_N)^(j+3/2).

For j<=N-2 the extra logarithm is O(N³H), already in C P_N.
The corresponding zeroth-order h power is 5/4. Finally,

    N² I_h=O(ell^(21/16)),
    N³H=O(ell^(3/16) log ell),

so P_N=o(ell²) uniformly in the stated N range. This closes the
weighted nonlinear bootstrap and supplies actual q's smooth lifetime
by its finite H4 bound. Its actual gradient clock is bounded by
C integral m_h plus a vanishing error. The datum remains the same
original first-stage datum for every choice of proof order.

## 5. Controls and scope of this pass

Omitting the mean-primary fast coupling or the corresponding full
pressure cancellation can leave the earlier h^(9/4) residual. That
would give h^(-1/4), rather than h^(1/4), in the nonlinear weighted
bootstrap and would not support this proof. Taking the larger radius
h/(C N²) for U_app while ignoring its K_N jets likewise fails to
control the linear commutator sum. Placing exp(CN log N) inside the
leading linear clock reproduces the failure identified in section 3
of the source. None of these shortcuts is used in the audited scheme.

No decisive gap was found in sections 2--5 after the explicit finite-stage
radius accounting above. Distinct intermediate B_N and final K_N notation
would make (12)--(14) easier to verify; the author's finite enlargement
language can be implemented as shown without a larger loss exponent.
This pass is conditional on the stated quantitative Gevrey profiles and
the exact retained first-stage equations. It does not supply the receiver's
outgoing lower bound, a full-Q growing-depth recurrence, an infinite series,
or a global Navier--Stokes theorem.
