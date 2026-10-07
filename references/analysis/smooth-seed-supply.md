# Smooth original seed supply: a restricted obstruction to direct repetition

8 September 2026. Bounded analytic audit, with the derivative identity and scale budget
independently rederived by the coordinating agent and a separate reviewer;
see the [completed review](matching-review.md). No DNS.
This is a kinematic obstruction to assembling the newly matched prepared
packets into one smooth datum by a specified superposition. It is not an
obstruction to all Navier–Stokes cascades, to generated seeds, or to an
arbitrary rescaling or cancellation scheme. ROOT remains open.

## 1. Packet convention and the precise conclusion

Use the selected, normalized original-time receiver from the matched
outer/inner construction, in its rescaled y coordinates. Set

    ell=sqrt(log(1/h)), k=h^(3/2), d=h^(5/4),
    a_h=k ell^(-13/8).

At the central initial point y_h, the transported bump is one, the phase
is theta=S/k+pi/2=pi/2, and the real primary amplitude and covector satisfy

    |b_h(y_h)| comparable to a_h,
    |xi_h(y_h)| comparable to ell, xi_h=grad S_h,
    xi_h.b_h=0.

The initial velocity perturbation is the exact real curl

    Z_h=b_h cos(theta)-k d_b,h sin(theta),
    d_b,h=curl(xi_h cross b_h/|xi_h|^2).

Every later mean/harmonic correction has zero initial data, so it does
not change this original datum. The fixed spatial jet estimates imply

    ||D^r b_h||_infinity <=a_h d^(-r) E_h, r<=4,
    ||D^r xi_h||_infinity <=h^(-r) E_h, 1<=r<=4,
    |xi_h|+|xi_h|^(-1)<=E_h,
    E_h=exp(C ell)=h^(-o(1)),

after enlarging the fixed constant C. They also imply
||D^r d_b,h||<=a_h d^(-1-r)E_h for r<=3. Thus phase derivatives through
order five, not merely order three, cover the complete differentiated
curl remainder.

There are unit vectors e_h=xi_h(y_h)/|xi_h(y_h)| and
v_h=b_h(y_h)/|b_h(y_h)| such that

    v_h . partial_(e_h)^3 Z_h(y_h)
       = |b_h(y_h)| (|xi_h(y_h)|/k)^3 [1+o(1)]
       >= c k^(-2) ell^(11/8).                        (1)

In contrast the leading initial first derivative is only ell^(-5/8).
Consequently small initial C1 does not make this a uniformly smooth
family: its C3 norm diverges very rapidly.

If these packet profiles are embedded without coordinate or amplitude
rescaling into one compact coordinate domain, an infinite disjoint
superposition cannot be C3. The same conclusion holds for superpositions
whose third derivatives do not cancel the lower bound (1). It therefore
cannot be C-infinity. The exact meaning of these restrictions is in
sections 3 and 5.

## 2. Exact third derivative, including curl and envelope terms

Freeze e=e_h when differentiating, and write a prime for the directional
derivative at y_h. Let q=theta'=|xi_h|/k there. Since theta=pi/2,

    (b cos theta)''' = b(q^3-theta''')
                          -3b' theta''-3b''q,
    (-k d_b sin theta)'''
          =-k d_b'''+3k d_b' q^2+3k d_b q theta''.

These identities are exact at the central point; no affine-phase or
constant-envelope replacement was made. The leading scalar product with
v_h is |b_h|q^3. The remaining terms are bounded, respectively, by

    a_h h^-2 E_h/k,
    a_h d^-1 h^-1 E_h/k,
    a_h d^-2 ell E_h/k,
    k a_h d^-4 E_h,
    a_h d^-2 ell^2 E_h/k,
    a_h d^-1 ell h^-1 E_h/k.

Relative to a_h ell^3/k^3 their h-power factors are
h, h^(3/4), h^(1/2), h, h^(1/2), h^(3/4), up to harmless powers of ell
and E_h. Hence the total relative error is O(h^(1/2)E_h)=o(1).
The leading coefficient is

    a_h ell^3/k^3 = k^-2 ell^(11/8),

which verifies (1). The phase pi/2 is useful: the leading odd derivatives
are attained at the specified center, so no nearby-phase selection is
needed for this C3 obstruction.

## 3. A precise superposition obstruction

Let h_j tend to zero and place translated/rotated copies Z_j of these
profiles in a common compact smooth domain, for example a fixed torus.
Translations and orthogonal rotations preserve the derivative bound.
Suppose the closed supports are pairwise disjoint and each designated
center x_j is in its packet's interior. For any fixed smooth background
U_bg, suppose a proposed sum U=U_bg+sum_j Z_j is defined at least as a
locally integrable field and agrees with this sum on those interiors.

In a neighborhood of x_j every other packet is identically zero.
If U were C3, its third derivative at x_j would therefore obey

    ||D^3 U(x_j)|| >= c k_j^-2 ell_j^(11/8)-||D^3 U_bg||_infinity.

The right side tends to infinity, contradicting bounded continuous third
derivatives on a compact domain. This argument does not need convergence
of the series after three differentiations: assuming C3, local equality
on each individual packet interior already determines the derivative.
The varying directions e_j and v_j do not help, since each is a unit
vector and their scalar evaluation is bounded by the full D3 tensor norm.

For overlapping supports, a sufficient quantitative noncancellation
condition is that the total contribution of the other packets, interpreted
in a C3 neighborhood of x_j if necessary, has scalar third derivative
opposite to (1) of magnitude at most theta times its leading size, for a
fixed theta<1. A bounded background is harmless. Then the same lower
bound with factor 1-theta applies. An assertion that the packets are
merely 'different frequencies' is not itself this condition.

On a noncompact domain, centers escaping every compact set are different:
a locally finite disjoint sum can be C-infinity with unbounded derivatives
at infinity. Thus the argument concerns compact domains, accumulation
inside a compact region, or a specified global bounded-C3 requirement.
It does not claim that unbounded derivative norms prohibit local C-infinity
regularity on all of R3.

## 4. Attenuation repairs smoothness only by losing this handover

Allow nonnegative scalar amplitudes eta_j multiplying the prepared
packets. Equation (1) scales linearly. Under the same disjointness or
noncancellation hypothesis, bounded C3 necessarily requires

    eta_j k_j^-2 ell_j^(11/8) <= C,
    hence eta_j <= C k_j^2 ell_j^(-11/8).              (2)

This is only a necessary C3 condition, not a sufficient C-infinity
construction. A compactly accumulating C-infinity sum typically requires
control of every fixed derivative order and its limiting compatibility.
There is no need to establish that stronger condition to see the loss
already forced by (2).

For the matched finite transfer, the unattenuated terminal p strain is
comparable to ell^(11/8), and the normal strain to ell^(7/8). Applying
(2) to its linear principal packet yields

    terminal total fine strain <= C k_j^2 ->0,
    terminal normal strain <= C k_j^2 ell_j^(-1/2) ->0.

The controlled mean, harmonic, and NS tracking errors in the existing
finite-transfer approximation tend to zero. They cannot restore a
strain larger than a host of order ell_j within that proven mechanism.
By contrast even fixed-factor dominance of the host would require
eta_j >= c ell_j^(-3/8), incompatible with (2).

This does not prove that an arbitrarily tiny seed can never grow under
some later, longer, or different flow. It says that the matched time
window and polynomial-in-ell amplification do not pay for the attenuation
already needed to assemble this disjoint family in bounded C3.

## 5. Coordinates and physical scaling must not be mixed

The original finite proofs live on expanding rescaled tori and use
h-dependent rescaled viscosity epsilon=nu h^4. Their individual velocity
fields cannot simply be called one family of packets on a single
fixed-viscosity coordinate domain without specifying the coordinate map.
The obstruction in section 3 is a statement about identity-coordinate
embeddings of the packet profiles; it is kinematic and does not assert
that the separate finite amplification theorems survive such an embedding.

For the particular conversion used in the canonical log-log note,

    L=h^-10, A_L=L^(7/5)=h^-14,
    u_L(t,x)=A_L q_epsilon(A_L L t,Lx),

all three derivatives acquire the factor A_L L^3=h^-44. Thus the same
receiver alone has physical third derivative at least

    c h^-47 ell^(11/8),

and physical first derivative of order h^-24 ell^(-5/8). Its small
rescaled C1 norm is not small physical C1. This particular conversion
therefore does not evade the disjoint fixed-torus obstruction; it makes
the derivative growth stronger. The base field also changes with L.
These statements refer to that exact conversion, not every possible
physical placement or normalization.

More generally, for a spatial scaling s_j and velocity multiplier A_j,

    W_j(x)=A_j Z_j(s_j(x-x_j)),
    ||D^3 W_j|| leading size
       =A_j s_j^3 k_j^-2 ell_j^(11/8).

The terminal strain also changes by A_j s_j, and support sizes, time,
and viscosity must be transformed consistently. An NS conversion to one
fixed viscosity nu requires epsilon_j=nu s_j/A_j. One may not carry
only the derivative multiplier from one convention and the handover
threshold from another. No claim is made here that every choice of these
parameters is impossible; a proposed alternative must provide its own
common-domain, viscosity, support, time, and amplitude budget.

## 6. Cancellation and generated or inherited seeds remain separate routes

Exact mutual cancellation can defeat any lower bound derived from an
individual summand. For example adding a packet and its negative removes
it entirely, though that also removes its proposed seed. More elaborate
cancellation or conditional sums require analysis of the actual total
initial field, not independent evolutions of the summands: NS is nonlinear
and overlapping packets change the receiving background. This note does
not rule out such constructions and does not assume their success.

The obstruction therefore rules out the naive plan of preloading
infinitely many of the current unattenuated, independently prepared
receivers as disjoint or noncancelling components of one smooth compact
datum in a common coordinate convention. It identifies the additional
obligation for an iterative construction: produce the next usable seed
from the preceding solution, transport an inherited seed with a proven
common-data budget, or supply a different smooth compatible preparation
whose attenuation is paid for by a stronger transfer mechanism. The
finite supplied-seed theorem alone supplies none of these alternatives.

The exact third-derivative calculation uses only the finite jet bounds
already available for the packet. It is not an infinite-time argument,
a universal cascade obstruction, or a global NS regularity proof.


## Source and review scope

Original source: `nse-smooth-seed-supply-audit-20260908.md`; SHA-256 `a5ee0f95956a1e2e25a0f747fb63bb733a2b05ad92806431aadde980eae839b1`. Archival wording and local links have been updated. Mathematical review here means a separate AI-agent derivation audit, not independent expert acceptance or a formal proof certificate.
