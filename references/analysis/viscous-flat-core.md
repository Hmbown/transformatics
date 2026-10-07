# Exact viscous affine profiles and heat-rounded flat cores

Independent analytic check, 8 September 2026. **Verdict: the proposed exact affine solution and exponential interior rounding estimate are correct with the qualifications below.** This is a direct calculation, not a finite-energy periodic NS theorem, a localization theorem, or a formal certificate. No flow simulation was run.

## 1. Hypotheses and exact solution

Fix a circle of period L, 0<a<L/2, k>0, and constant viscosity epsilon>=0. Assume A(t) is smooth, trace A=0 and A'+A^2 is symmetric on the time interval. Let xi(0) != 0 and real b solve

    xi' = -A^T xi,
    b' = -A b + 2 xi c,
    c = (xi . A b)/|xi|^2,
    xi(0) . b(0) = 0.

The linear fundamental matrix keeps xi nonzero. Direct differentiation gives (xi.b)'=-xi.Ab-xi.Ab+2xi.Ab=0.

Let F be real, smooth, odd and L-periodic, with F(s)=s on (-a,a). Oddness supplies zero mean; zero mean itself is all that is needed for a periodic primitive Q with Q'=F. Define

    tau(t) = epsilon/k^2 integral_0^t |xi(r)|^2 dr,
    f(t,s) = exp(tau(t) partial_s^2) F(s),
    q(t,s) = exp(tau(t) partial_s^2) Q(s),
    s(t,x) = xi(t).x/k.

Then q_s=f. On R3 set

    u(t,x) = A(t)x + b(t) f(t,s(t,x)),
    p(t,x) = -x.(A'+A^2)x/2 - 2 k c(t) q(t,s(t,x)).

This solves exactly

    partial_t u + (u.grad)u + grad p = epsilon Delta u,
    div u = 0.

Here is the complete cancellation. For U=Ax and D_U=partial_t+U.grad,

    D_U s=0,       Delta U=0,
    div(b f)= (xi.b) f_s/k = 0,
    (b f.grad)(b f) = b (xi.b) f f_s/k = 0,
    (b f.grad)U = A b f,
    D_U(b f) = b' f + b tau' f_ss,
    epsilon Delta(b f) = epsilon |xi|^2 b f_ss/k^2.

The last two second-derivative terms cancel by tau'. The remaining perturbation acceleration is (b'+Ab)f=2c xi f; the perturbation pressure gradient is exactly -2c xi f. Finally the base acceleration is (A'+A^2)x, canceled by its displayed quadratic pressure because that matrix is symmetric. No time derivative of the pressure appears in NS, so time variation of c, xi and q creates no omitted pressure term. Adding a time-only constant to q changes only the pressure gauge.

**Scope:** A nonzero affine background has infinite energy on R3 and is not spatially periodic. Even when A=0, a nonzero plane-wave profile generally has infinite energy on R3. A commensurate plane wave can descend to a torus only in compatible special cases; the affine calculation does not construct a general periodic finite-energy solution. No assumption of an arbitrary realizable time-dependent affine strain is implicit: the symmetry condition is essential.

## 2. Quantitative rounding, including the function itself

Write H_tau=exp(tau partial_s^2). For every integer m>=0 and |s|<=a/2, the exact Duhamel identity is

    partial_s^m(H_tau F(s)-s)
        = integral_0^tau H_r F^(m+2)(s) dr.                 (1)

The initial term partial_s^m(F-s) vanishes throughout this core. Equation (1) for m=0 is an identity for F itself; it does not try to apply a periodic heat operator to the nonperiodic function s.

Each periodic G=F^(m+2) vanishes on (-a,a). Use the periodized Gaussian, or equivalently the Gaussian convolution with the periodic extension of G:

    H_r G(s) = integral_R (4 pi r)^(-1/2)
                         exp(-y^2/(4r)) G(s-y) dy.

If |s|<=a/2, then G(s-y)=0 for |y|<a/2. This implication is enough even though more distant translates also vanish. The two Gaussian tails, each bounded by Chernoff's estimate, give

    |H_r G(s)| <= 2 ||G||_infinity exp(-a^2/(16r)).

Integrating (1), for every 0<tau<=tau0,

    sup_|s|<=a/2 |partial_s^m(H_tau F(s)-s)|
      <= 2 tau ||F^(m+2)||_infinity exp(-a^2/(16tau))
      <= 2 tau0 ||F^(m+2)||_infinity exp(-a^2/(16tau)).     (2)

Thus one can take c=1/16 and C=2 tau0 ||F^(m+2)||_infinity. Dependence on the fixed profile/core parameters and tau0 should be included if abbreviated as C_{m,F}. This proof treats periodic image contributions and m=0 explicitly; there is no hidden algebraic heat-kernel prefactor to absorb. At tau=0 the error is zero by the initial core identity.

For tau>0, H_tau F is real analytic and periodic. It cannot equal s on any nonempty open interval: analytic continuation of (H_tau F)'=1 would force its derivative to be identically 1, contradicting periodicity. Heat therefore destroys an exact nonempty linear core, while (2) gives exponentially accurate interior linearity.

Spatial jet errors inherit the chain-rule factors: for frozen t, an order-m spatial derivative of b(f-s) is bounded by |b| (|xi|/k)^m times (2). These factors must still be counted in any scale-dependent application.

## 3. The primitive has an additional pressure-gauge term

There is a useful distinction between F and its primitive. On the original core, Q(s)=Q(0)+s^2/2. Since Q''=F',

    H_tau Q-Q-tau = integral_0^tau H_r(F'-1) dr.

Here F'-1 is periodic and zero on (-a,a). The same tail proof shows

    sup_|s|<=a/2 |H_tau Q(s)-Q(0)-s^2/2-tau|
      <= 2 tau ||F'-1||_infinity exp(-a^2/(16tau)).        (3)

Thus q is close to Q(0)+s^2/2+tau, not simply to its initial quadratic primitive with exponential error. For the globally constant-in-space coefficient c(t), the extra tau changes only the pressure gauge. One may replace q by q-tau in the exact affine pressure. This innocent global gauge becomes significant if the primitive is used inside a spatially varying vector potential.

## 4. Exact curl localization identity and its boundary

Now let S(x) be smooth with xi=grad S nonzero and let b(x) be smooth with xi.b=0. Define

    C(x) = -(xi cross b)/|xi|^2.

For any scalar primitive q with derivative f and constant k, the exact identity is

    k curl[C q(S/k)] = b f(S/k) + k (curl C) q(S/k).      (4)

Indeed grad q(S/k)=xi f/k and xi cross C=b by the triple-product identity. If b is not transverse, the leading term is instead its projection b-xi(xi.b)/|xi|^2. If xi is not grad S, even that leading identity requires replacing xi by grad S in the cross product.

For a cutoff chi and frozen xi,b, (4) reads

    k curl[chi C q(S/k)]
       = chi b f(S/k) + k (grad chi cross C) q(S/k).      (5)

In the fully varying case add k chi (curl C) q. These terms are part of the velocity, not optional pressure corrections. The curl construction guarantees divergence freedom; it does not guarantee the momentum equation. Their transport, viscous Laplacian, cross-interactions with the leading wave, envelope self-interactions and pressure response must be computed and bounded. The cancellation (b f.grad)(b f)=0 used in section 1 is no longer a complete account of the localized nonlinearity. The time-varying phase must also satisfy its transport equation; merely freezing its central value does not cancel ambient drift.

For example, changing the primitive q to q-tau leaves the global affine velocity b f unchanged, but changes the localized curl velocity by

    -k tau curl(chi C).

Hence one cannot discard the tau in (3) as an irrelevant gauge inside a localized vector potential. Either primitive convention can be chosen, but its resulting velocity and time derivative must be retained consistently. Likewise an arbitrary primitive constant is harmless for the global pressure yet can change a localized velocity.

**Conclusion of this check:** the exact affine viscous extension is valid and the interior heat-rounding estimate is exponentially small. Compact localization preserves solenoidality through (4), while introducing explicit velocity and residual terms. Nothing in this calculation removes those terms or establishes an exact localized, finite-energy NS extension.


## 5. The existing central matrix satisfies the affine compatibility identity

This is an additional exact calculation by the coordinating agent, checked
independently by the packet reviewer. Use Cartesian matrices along the
reference Euler particle, rather than rotating-frame entries without their
frame correction. Let A0 be its gradient and set

    Abar=A0-r beta tensor N, r=1/ell,
    N'=-A0^T N, beta'=-A0 beta+2c N,
    c=(N.A0 beta)/|N|^2, N.beta=0.

Differentiating the rank-one term and using its square zero gives exactly

    Abar'+Abar^2=A0'+A0^2-2r c N tensor N.

The Euler gradient equation on the reference particle says
A0'+A0^2=-Hess P, which is symmetric. Thus Abar meets section 1's affine
NS compatibility condition. This makes the heat-profile model relevant
to the central matching calculation. It does not make the actual q or
Q_h spatially affine on any neighborhood, and does not identify an actual
NS jet with an arbitrary prescribed affine history.

For the existing receiving ray, the central model's accumulated diffusion
parameter is at most C_nu h ell^2 log ell, which tends to zero. Section 2
therefore yields exponentially small interior rounding in that affine
model, with its explicit chain-rule factors. Transferring this estimate to
the full localized flow, its mean/pressure tails, mixed time derivatives
and infinite descendants remains a separate PDE calculation.

Changing the profile also changes the correction algebra and the locations
of large initial higher derivatives. In particular a profile linear at the
center has vanishing third phase derivative there: the old sinusoidal
center-based C3 obstruction cannot be copied without rechecking the new
profile and its full support. No smooth infinite seed supply is thereby
established or ruled out.

## Source and review

The affine formula, periodic heat-kernel estimate, primitive correction and
localization identity were independently checked by the coordinating agent
and two separate agents. The source was a bounded derivation motivated by
the released [Boussinesq flat-core construction](https://cims.nyu.edu/~tristanb/boussinesq.pdf);
no claim of novelty is made. These are written calculations, not a formal
certificate or a finite-energy full-NS construction. 

Original reviewed source: `nse-flat-core-viscous-check-20260908.md`; SHA-256 `47219fdef448380d7467246961c9cb523a3d9d27df1464c5160325928aad61ed`. The central-matrix corollary was independently reviewed separately before archival addition.
