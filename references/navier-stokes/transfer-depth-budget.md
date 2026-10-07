# What the finite transfer estimates permit at repeated depth

**8 September 2026 — restricted estimate audit. ROOT and `(E′)` OPEN.**
This note concerns the simultaneous requirements of a proposed proof.
It does not assert that an actual Navier–Stokes trajectory must obey
the sufficient localization bounds imposed below. Failure of those bounds
is failure of that proof method, not a regularity or blow-up theorem.
Separate finite-stage derivations and their review boundaries are indexed
in the [research appendix](next-transfer-review.md).
The [original-time finite theorem](original-nonlinear-handover.md) now supplies two compatible original seeds; one smooth datum supporting infinite depth remains open.

The input is the finite-time
[outgoing-wave estimate](outgoing-wave.md). Its current
flow-derivative bound contains `exp(C lambda Delta)`, with
`lambda=ell`, `Delta=ell^(-3/4)`. This is harmless in that theorem's
varying-data limit, since `ell=sqrt(log(1/h))`. Repeating stages within
one solution requires a different, simultaneous limit.

## 1. An exponential localization certificate conflicts with weak diffusion

Fix positive constants `epsilon,C,Hmax,eta`, with `eta<1`, and a fixed
exponent `0<b<1`. Suppose `lambda_j -> infinity` and, in one fixed
coordinate system,

    Delta_j=lambda_j^(-b),
    0<k_j<=d_j<h_j<=Hmax.

Here h is a host length, d is the radius used to localize a receiving
packet, k is its wavelength parameter, and epsilon is the single fixed
viscosity in these coordinates. Consider the particular sufficient
coherence certificate

    (d_j/h_j) exp(C lambda_j^(1-b)) <= eta.             (1)

**Restricted implication.** These assumptions force

    epsilon Delta_j/k_j^2
       >= epsilon/(eta^2 Hmax^2)
          lambda_j^(-b) exp(2C lambda_j^(1-b)).          (2)

In particular, the left side divided by `log lambda_j` tends to
infinity. It cannot remain bounded, or even grow only logarithmically.

**Proof.** Equation (1) gives
`k_j<=d_j<=eta Hmax exp(-C lambda_j^(1-b))`.
Square, invert and multiply by `epsilon Delta_j`. For the last claim,
the logarithm of the ratio of the right side of (2) to `log lambda_j` is

    log(epsilon/(eta^2 Hmax^2))
       -b log lambda_j-log log lambda_j
       +2C lambda_j^(1-b),

which tends to infinity because `1-b>0`. This logarithm is that of
the ratio to `log lambda_j`, not a statement that (2) follows from
a lower bound on the actual coherence error.

For a prescribed characteristic whose covector satisfies `|xi|>=c0>0`,
the principal viscous polarization equals the inviscid polarization times

    exp[-(epsilon/k_j^2) integral |xi(t)|^2 dt].         (3)

This is an exact identity for the principal ODE: its viscous term is
a scalar multiple of the identity. If the inviscid propagator on that
characteristic is bounded by C0 lambda_j^p with C0,p independent of j, (2)-(3) suppress
its polynomial gain. In particular, a certificate using (1), uniformly
nonzero covectors, and weak viscous attenuation cannot support infinitely
many such polynomial-gain stages at fixed epsilon.

This statement does **not** rule out smaller actual coherence errors,
an anisotropic localization argument, a different error norm, covectors
with different scale histories, or a different NS mechanism. The generic
exponential bound is an upper estimate, not a dynamically necessary loss.

### The coordinates cannot reset the diffusion budget

For the NS rescaling

    u(t,x)=A q(AL t,Lx),       epsilon=nu L/A,

a rescaled interval Delta and wavelength k correspond to physical
interval `Delta/(AL)` and wavelength `k/L`. Therefore

    nu [Delta/(AL)]/(k/L)^2 = epsilon Delta/k^2.        (4)

This dimensionless attenuation is unchanged by the coordinate choice.
One may use new coordinates at a later stage, but must transform every
quantity together. The fixed-epsilon assumptions in section 1 refer to
one fixed coordinate system, not independently chosen stage normalizations.

The original first-stage family has `epsilon=nu h^4` while h tends to
zero; section 1 does not contradict its finite-time estimates. Once a
member of that family is fixed, its rescaled epsilon is positive and fixed.

## 2. A polynomial replacement still needs a joint recurrence

This section is exact algebra for a proposed recurrence, not an NS
realization. Fix `lambda_0>1`, `h_0>0`, `epsilon>0`, and constants
`r>1`, `a>0`, `b>0`. Impose

    lambda_(j+1)=lambda_j^r,
    h_(j+1)=h_j lambda_j^(-a),
    Delta_j=lambda_j^(-b).                              (5)

Treat h_(j+1) as the receiving wavelength in stage j. Direct induction
gives

    lambda_j=lambda_0^(r^j),
    h_j=h_0 lambda_0^[-a(r^j-1)/(r-1)],

and hence its stage diffusion number is exactly

    D_j=epsilon Delta_j/h_(j+1)^2
       =(epsilon/h_0^2) lambda_0^[-2a/(r-1)]
         lambda_j^[2ar/(r-1)-b].                        (6)

Thus D_j tends to zero, stays constant, or tends to infinity according
as `2ar/(r-1)-b` is negative, zero, or positive. Bounded D_j requires

    a <= b(r-1)/(2r).                                   (7)

When (7) holds, choosing the starting diffusion number sufficiently small
can make every D_j small. This closes only this scalar diffusion check.
It supplies no compatible seed, pressure estimate, nonlinear error
control, spatial realization, or singularity theorem.

The time sum is finite for all parameters above: Bernoulli's inequality
`r^j >= 1+j(r-1)` bounds Delta_j by a summable geometric sequence. A
summable time list and bounded diffusion do not establish an NS trajectory.

### A specific isotropic polynomial certificate also fails

Suppose a proposed transient stage uses `1/2<b<1` and an incoming strain
`lambda^alpha` with `b<alpha<1`. The model output exponent is

    r=alpha+1-b,        1<r<2-b.

If an isotropic certificate additionally requires a wavelength loss at
least the full shear factor, then `a>=1-b`. This is the specific extra
assumption being tested; it is **not** a universal requirement on packets.
Under it, the exponent in (6) obeys

    2ar/(r-1)-b
       >=2(1-b)r/(r-1)-b
       >2(2-b)-b=4-3b>1.                              (8)

The strict step uses the fact that `r/(r-1)` decreases for r>1 and
`r<2-b`. Thus replacing an exponential estimate by a polynomial one is
not sufficient if this particular isotropic loss remains in the
recurrence. Anisotropic geometry or a smaller wavelength cost is a
substantive change to investigate, not a constant adjustment.

For the current proposed exponents `alpha=7/8`, `b=3/4`, one has
`r=9/8`. Equation (7) permits at most `a=1/24`, whereas the full-shear
loss above demands at least `a=1/4`. These intervals are disjoint.
Neither number is an estimate already proved for the actual outgoing q.

As a control against overinterpreting (8), the abstract choice
`r=9/8`, `b=3/4`, `a=1/48` gives exponent `-3/8` in (6), so its
diffusion numbers decrease. This scalar recurrence violates the imposed
full-shear wavelength loss; it is not a constructed NS cascade.

## 3. Consequence for the next proof attempt

The original-time nonlinear handover and localized-profile extension now
have reviewed finite proofs. They cannot justify iteration merely by renaming
its current small parameters at the next stage. The next iterable
estimate must specify, in compatible physical units:

- the actual incoming seed and its earlier damping and feedback;
- the receiving phase, support geometry and wavelength loss;
- the propagator norm used for every generated error, including pressure
  tails, with constants and losses uniform across stages;
- the full recurrence for strain, length, time and viscosity.

An exact affine-shear Fourier calculation gives a promising comparison:
its linearized L2 propagator is only linear in net shear, uniformly across
Fourier orientations. It is a result for a prescribed affine drift,
which has infinite background energy. The subsequently reviewed
[Kolmogorov packet](../analysis/kolmogorov-outgoing-audit.md)
excludes an analogous uniform polynomial bound for arbitrary errors on
the actual spatially varying q family. The outgoing sinusoidal profile
has curvature and mode coupling that a gradient at one particle does not
capture. Bounds for appropriately restricted errors remain separate targets.

Separate written derivations for original-time linear preparation and a
late nonlinear second stage have since been completed. The late-data
nonlinear draft has a full independent mathematical review. Sections 4–7
of the original-time draft have also passed an independent review at the
forward linearized scope, after a correction to the initial-cost
comparison; the seed-cost identity has a separate algebra check. Its
phase-class exclusion was not newly reviewed. See the
[precise review record](next-transfer-review.md).
Neither derivation is an input to the restricted algebraic implications
here, and neither supplies an infinite compatible trajectory. No research
DNS, publication or full formal certificate is part of this audit.

## 4. The current full-solution and principal-ray restrictions

The [next-seed analysis](next-seed-analysis.md) applies the
actual H12 bound to every Fourier mode. On the current proved interval,
the gradient above frequency h^(-9/4) is at most h^(27/4-o(1)). Reaching a
fixed rescaled threshold later would require accumulated strain at least
c log(1/h)-O(ell); no corresponding later upper bound is known.

The [signed source calculation](../analysis/generated-receiver.md)
also proves the exact real principal-ray identity

    d log(|xi||b|)/dt = n.S(A)n-epsilon |xi|^2/kappa^2,
    n=(xi cross b)/(|xi||b|).

During the present window, ||S(A)|| is at most C ell^(11/8). A ray that
stays above h^(-beta), beta>2, is therefore damped: viscosity contributes
nu h^(4-2 beta), larger than this logarithmic strain. This is a homogeneous
polarization-ODE statement, not a forced full-Fourier decay theorem.
It prevents treating k_next=h^(9/4) as a cost-free repetition at the same
viscosity. A different scale must be chosen and its actual source, time
and deformation history proved. The [smoothly forced track](two-track-program.md)
may add a source, but must pay its complete smoothness budget.
