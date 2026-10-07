# Independent analytic review of the cycle's maximum-speed loss

8 September 2026. **PASS at the stated finite written scope.** This
independent review checks the actual-solution remainders, selection of
global maxima, and positive-viscosity comparison in
[the next-transfer source](cycle-next-transfer.md).
Reviewed source SHA-256:
`c8baeadaeca70f64ac482e67a9e7eb8e4ec4508c6ca758ddaeb6b9d051345864`.
Its exact control has SHA-256
`9c49093157f4889e2ffd15174f90a23265cae2651c365cf0a4ab9da59c9a0b01`.
The coordinating agent separately checked its exact Fourier algebra.
The control was read here but not rerun; this review does not substitute
its finite Fourier output for an actual PDE remainder estimate.
It is AI-agent review, not external expert acceptance or formal PDE
certification. No DNS or canonical source edits were made.

## 1. Uniform actual smooth solutions and time derivatives

The datum is one fixed trigonometric polynomial on the fixed torus.
In the H20 energy inequality, all constants depend only on that fixed
order and domain. The term mu Delta U is dissipative for every mu in
[0,1]. The resulting H20 bootstrap therefore gives one positive local
lifespan and one bound M independent of mu, including the auxiliary
Euler solution. This is standard uniform local existence, not a
consequence of the formal finite Fourier jets.

Differentiating the full projected equation j times in time gives
the stated H^(20-2j) bound through j=5. Each diffusion term loses two
spatial derivatives and has coefficient at most one. The ordered
quadratic products involve previously controlled time derivatives;
the lowest spaces used remain far above the three-dimensional Sobolev
algebra threshold. Leray is bounded in those spaces. In particular the
fifth time derivative is controlled in H10, so Taylor's integral
remainder through degree four is O(tau^5) with more than the required
two spatial derivatives. Composition with the fixed lines used in the
source preserves that uniform remainder.

## 2. All maxima are selected, and their displacement is paid

At tau=0, G=|U_E|² has exactly the eight listed maxima with value 3.
Choose disjoint small coordinate balls about them where D²G(0) is
uniformly negative definite. On their complement, compactness gives
G(0)<=3-g for some fixed g>0. The C2 continuity supplied by section 1
preserves strict concavity in each ball. The implicit-function theorem
gives one critical branch there, and no second critical point can occur
in a strictly concave ball. The branches have values tending to 3,
while the complement remains below 3-g/2 after a smaller common time
is chosen. Thus every global maximizer belongs to a listed branch.

For one branch, write x(tau)=p+tau v+tau²w+O(tau³). Substitution into
grad G(tau,x(tau))=0 gives

    tau:    -2v+grad G1(p)=0,
    tau²:   -2w+(1/2)D³G0(p)[v,v]
                    +D²G1(p)v+(1/2)grad G2(p)=0.

The three additional terms in the second line vanish by the source's
displayed initial jets. Hence w=0, proving the claimed O(tau³)
displacement error. This also independently checks why fixing p gives
the wrong quadratic conclusion: the optimized second derivative is

    G2(p)-grad G1(p)^T[D²G0(p)]^(-1)grad G1(p)
                        =-6+6=0.

At the straight-line test point p+tau v, grad G=O(tau³). Its distance
to the true branch is O(tau³); Taylor's formula in space therefore
changes G by O(tau^6), including both its linear and quadratic terms.
The reviewed line coefficient U_E=v-(4/15)tau^4 v+O(tau^5), with
|v|²=3, consequently gives branch value
3-(8/5)tau^4+O(tau^5). Taking the maximum of finitely many branches
with the same quartic coefficient preserves this expansion. There is
no untracked maximizing sequence outside these neighborhoods.

## 3. The viscosity error has the required extra time factor

Let W=U_mu-U_E. An especially direct form of the exact difference
equation is

    W_tau+P(U_mu.grad W+W.grad U_E)-mu Delta W
                                      =mu Delta U_E.

All velocities are solenoidal. In H16 the top transport cancels and
the remaining coefficient norms are bounded by the common H20 bound.
The forcing is bounded by C mu. With W(0)=0, energy therefore gives
||W||H16<=C mu tau on the common interval. This estimate already
includes the complete pressure via the exact Leray projection.

The same equation in H14 gives

    ||W_tau-mu Delta U0||H14 <= C mu tau.

Indeed both advective terms are O(mu tau), the diffusion of W is
O(mu² tau), and mu Delta(U_E-U0)=O(mu tau) since U_E-U0=O_H16(tau).
The condition mu<=1 absorbs the mu² term. Integrating once, with
Delta U0=-U0, proves the full-space bound

    U_mu=U_E-mu tau U0+O_C2(mu tau²).

This is stronger than an O(mu) comparison and remains informative when
mu is much smaller than a power of tau. Expanding the squared magnitude,
using U0-U_E=O(tau) and mu²<=mu, yields uniformly in x

    |U_mu|²=(1-2mu tau)|U_E|²+O(mu tau²).

For tau<=1/4 the scalar factor is positive. Taking maxima is then
legitimate directly: if two functions differ by at most E uniformly,
their suprema differ by at most E. No differentiability or uniqueness
of the viscous maximizing branch is required. Combining with the
Euler maximum expansion gives

    ||U_mu||infinity²=3-6mu tau-(8/5)tau^4
                                      +O(tau^5+mu tau²).

All constants are independent of mu in [0,1].

## 4. Strict finite-time margins and scope

The source's choice of T_* bounds its two errors by (4/5)tau^4 and
3mu tau, respectively. It therefore proves the asserted upper bound

    ||U_mu(tau)||infinity² <=3-3mu tau-(4/5)tau^4,
                                      0<tau<=T_*.

The same-time enstrophy comparison is also sound. Choose one positive
tau_dagger inside both proved lifespans with C_Q tau_dagger<=1/4,
and then 0<mu<=tau_dagger/16. The enstrophy quadratic term exceeds its
linear loss and remainder by at least tau_dagger²/8, while the maximum
speed is strictly below its initial value at that identical time.

For u(t,x)=A U_mu(Aqt,qx) and integer q, maximum speed squared gains
A², enstrophy gains A²q², and time is divided by Aq. Periodic spatial
averages and unnormalized integrals on the fixed physical torus have
the same q-cancellation in this change of variables. The restriction
A>=16nu q/tau_dagger retains positive fixed physical viscosity.

The result is a concrete short-time failure of a maximum-speed gain
requirement for this same cyclic datum. It is compatible with generated
Fourier modes and increasing enstrophy. It supplies no global maximum
principle, later-time exclusion, or conclusion for all localized or
altered stages. No source correction is requested.
