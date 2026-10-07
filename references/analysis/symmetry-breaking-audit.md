# What a quantitative departure from a regular geometry must supply

8 September 2026. Independent adversarial review and a classical perturbation
estimate for the current two-track program. The two reviewed finite lemmas
pass in their stated scope. The new estimate below excludes a **quantified
neighborhood** of any specified regular reference on a fixed finite time
interval, even when every nonzero perturbation has genuinely three-dimensional
spatial dependence. It does not establish regularity for arbitrary data,
construct a singular solution, or close ROOT or FORCED-D. No DNS is used.

## 1. Review of the two new analytic claims

### The later-flow lemma

The [later-flow note](later-flow-attempt.md) has no new analytic
gap in its stated consequence from the
[localized-profile endpoint inputs](../navier-stokes/localized-profile.md).
This review checked those displayed inputs and the new proof; it is not a
fresh certification of the entire earlier packet construction.

- The endpoint global gradient bound uses the whole-support primary
  estimate, base flow, correctors and tracking error. The central strain
  value is not used as a global upper bound.
- The periodic pressure Hessian loses the explicitly charged logarithm of
  the torus size. Dyadic annular kernels have uniform L1 bounds by
  periodization. The H11 high-frequency tail has power -19/2, and the
  source has mean zero. No L-infinity Riesz-transform estimate is assumed.
- The separate H12 energy estimate and differentiated maximum principle
  close the proposed lifetime. The Gaussian estimate compares the actual
  backward diffusion to the actual deterministic flow; it does not freeze
  the host or discard pressure. The covering-space estimate implies the
  required periodic-distance estimate.
- The endpoint leakage scale is R squared divided by epsilon times tau;
  the displayed powers give the absolute rescaled C1 error ell^(-1/4).
  The source estimate is only an upper bound. The propagated H12 bound,
  rather than its weaker Duhamel estimate, supplies the stated net tail.

The result gives neither large additional accumulated strain nor a new
signed receiving source. Small rescaled gradient error does not supply
small higher derivatives or an independently controlled material jet.

### The full fixed-annulus exclusion

The [fixed-annulus note](fixed-annulus-obstruction.md) also
passes for its **whole-velocity**, fixed-axis, compact-support assumptions.
The circle average removes the pressure's angular derivative even though
the torus pressure need not be axisymmetric. Zero extension is performed
only for already compact velocity and averaged source fields. In the Xi
energy identity the measure is the physical 2 pi r dr dz, and the radial
boundary flux vanishes because support avoids the axis and chart boundary.

The full Cartesian derivative of Xi(-x2,x1,0) includes differentiation of
the angular basis. Its extra radial integrand is exactly a boundary
derivative. This gives the H2 estimate for the meridional velocity. Together
with bounded swirl, it yields the full velocity in L2-time/L-infinity-space.
The last H1 estimate uses the **full-domain force norm**, and therefore
really closes strong continuation. There is no hidden appeal to global
rotation invariance of the torus. A local symmetric core in a nonsymmetric
or noncompact older velocity is outside the claim.

The source check is consistent with
[Seregin's paper, section 2, step 1](https://link.springer.com/article/10.1007/s00021-022-00667-6),
which locates possible singularities of the axisymmetric suitable flow on
its axis. The repository proof separately derives the needed smooth-force
version with stronger support assumptions. The inspected local copy of
the [released Alpöge–Buckmaster Euler manuscript](https://cims.nyu.edu/~tristanb/euler.pdf)
has SHA-256 `97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8`.
Its Theorem 1.1 and section 13.2 supply the stated fixed annular geometry;
they do not assert ordinary Navier–Stokes breakdown. The live PDF fetch
failed during this audit, so this geometry check refers specifically to
that existing hash-pinned copy, not an asserted newer release.

The existing [exact controls](checks/check-annular-geometry.py)
were rerun: weighted diffusion, the Cartesian basis derivative with its
negative control, full-operator conjugation, spatial-return commutator,
sideband signs and seven exponent checks pass. They certify those algebraic
identities, not the PDE continuation theorem.

## 2. Compare complete physical velocities, not symmetry labels

Fix one flat three-torus Omega, one viscosity nu>0 and T<infinity. All norms
below are its ordinary unnormalized physical norms. Constants are for this
fixed torus; they are not silently uniform under a concentration or
large-domain limit.

Let U be a specified smooth divergence-free reference velocity on [0,T],
with periodic pressure P and complete reference force F:

    U_t + U.grad U + grad P = nu Delta U + F.

The reference may be a proved regular axisymmetric solution in an embedded
chart, a regular 2D3C solution, or another explicitly controlled velocity.
It may also be a smooth approximate construction, provided F is its
**complete residual force**, including all cutoffs and pressure recovery.

Let u be the maximal strong solution for datum u0 and smooth force f on
the same torus, and set

    w=u-U, pi=p-P, g=f-F.

Then the exact difference equation is

    w_t - nu Delta w + U.grad w + w.grad U + w.grad w
        + grad pi = g,             div w=0.                 (1)

No symmetry of w or g is assumed. In particular this retains every
three-dimensional interaction and the complete prescribed force error.
The pressure cancels in the energy pairing because both w and Delta w
are divergence-free and periodic.

## 3. A finite, explicit H1 stability margin

Choose fixed valid Sobolev constants C_S and C_G for Omega such that

    ||v||6 <= C_S ||v||H1,
    ||grad v||3 <= C_G ||grad v||2^(1/2) ||Delta v||2^(1/2). (2)

The second estimate uses the zero mean of each periodic first derivative,
Sobolev embedding, interpolation and the Fourier equality
||D^2 v||2=||Delta v||2. It does not require v itself to have zero mean.
Define

    X=||w||2^2+||grad w||2^2,
    D=||grad w||2^2+||Delta w||2^2,
    c_U(t)=2||U(t)||infinity+C_S||grad U(t)||3,
    a(t)=1+(2/nu)c_U(t)^2,
    b=27(C_S C_G)^4/(2nu^3),
    q(t)=(1+2/nu)||g(t)||2^2.                              (3)

These actual coefficient norms and their viscosity costs remain in the
estimate. Pair (1) with w-Delta w. The low-order U transport and self
transport vanish. Integrate w.grad U against w by parts. The two remaining
U terms and that low-order term are bounded in total by

    c_U X^(1/2) D^(1/2) <= (nu/4)D+(c_U^2/nu)X.

The high-order self-interaction is bounded by

    ||w||6 ||grad w||3 ||Delta w||2
       <= C_S C_G X^(3/4)D^(3/4)
       <= (nu/4)D + [27(C_S C_G)^4/(4nu^3)]X^3.           (4)

For the force use

    |<g,w-Delta w>|
      <= X/2 + ||g||2^2/2 + (nu/4)D + ||g||2^2/nu.

Thus the full nonlinear perturbation obeys

    X' + (nu/2)D <= a(t)X+bX^3+q(t).                     (5)

The cubic X term is structural. It has not been replaced by a linear
coefficient or controlled by the ordinary kinetic-energy budget.

Put

    A(t)=integral_0^t a(s) ds,
    E=X(0)+integral_0^T exp(-A(s))q(s) ds,
    B(t)=b integral_0^t exp(2A(s)) ds.                     (6)

If A(T)<infinity and

    2 E^2 B(T)<1,                                        (7)

then

    X(t) <= exp(A(t)) E / sqrt(1-2E^2 B(t)),  0<=t<=T.  (8)

For E=0 the right side is zero. To prove (8), multiply (5) by exp(-A).
The new unknown y=exp(-A)X satisfies

    y(t) <= E+integral_0^t b exp(2A(s)) y(s)^3 ds.

The scalar comparison solution starting from E is exactly
E[1-2E^2 B(t)]^(-1/2), which proves the bound. Strictness in (7) keeps
X uniformly bounded through T. The usual forced H1 strong-solution
continuation theorem then extends u beyond T; smooth data and forcing
propagate smoothness. This use of continuation is for the **full** u.

Consequently any singularity at or before this specified T, relative to
this specified reference with finite A(T), must fail (7):

    2 E^2 B(T)>=1.                                       (9)

Failure of the smallness test is only a necessary condition for that
possibility, never evidence of singularity. The stability margin can be
very small when the actual host norms or nu^(-1) are large.

For the regular annular reference, finiteness of A(T) follows from the
reviewed proof itself. It gives U in L2_t L-infinity_x; the final H1
estimate, integrated in time, also gives Delta U in L2_t L2_x and U in
L-infinity_t H1_x. Therefore grad U is in L2_t L3_x by (2). No additional
assumed bound on all higher derivatives is needed to make (6) finite.

## 4. A nonzero third phase can remain inside the regular neighborhood

On the torus of side 2pi, the exact unforced shear

    U(t,x)=a0 exp(-nu N^2 t) sin(N x2) e1, N>=1,           (10)

is a smooth 2D3C reference on every finite interval. Its actual coefficient
in (3) is bounded explicitly using

    ||U||infinity=|a0| exp(-nu N^2t),
    ||grad U||3=|a0|N exp(-nu N^2t)||cos(Nx2)||3.

Writing C_N=||cos(Nx2)||3, the integral in (6) is exactly

    A(t)=t+
      [a0^2(2+C_S N C_N)^2/(nu^2 N^2)]
          [1-exp(-2nu N^2t)].                             (11)

Now perturb the datum by

    w0=eta (sin x3, sin x1, sin x2), g=0.                 (12)

This field is divergence-free. For eta!=0, the complete initial velocity
U(0)+w0 has no nonzero constant direction along which it is invariant:
its second component forces that direction's first coordinate to vanish,
its third component forces the second to vanish, and the first then
forces the third to vanish. Thus its spatial dependence is truly
three-dimensional, even for arbitrarily small eta.

Nevertheless X(0)=3|Omega|eta^2. For any prescribed finite T, (7) holds
whenever

    2(3|Omega|)^2 eta^4 B(T)<1,                            (13)

with B computed from (11). The resulting full three-dimensional NS
solution continues past T. This is a finite-horizon exclusion, not a
claim that (13) with one eta works for every T. It shows why naming a
nonzero third phase cannot itself supply the missing singular mechanism.

## 5. Exact symmetry-derivative accounting

For a periodic flow u on a torus with x3 period 2pi L3, set

    zeta=partial_3 u, h3=partial_3 f,
    sigma(t)=ess sup_x lambda_max(-S(u(t,x))),
    kappa3=1/L3.

Differentiating the full NS equation gives exactly

    zeta_t + u.grad zeta + zeta.grad u + grad(partial_3 p)
        =nu Delta zeta+h3,       div zeta=0.              (14)

Pairing with zeta gives the signed identity

    (1/2)d_t ||zeta||2^2+nu||grad zeta||2^2
        =-integral zeta^T S(u) zeta dx+<h3,zeta>.         (15)

Each x3-periodic line has zero mean for zeta, so
||grad zeta||2^2>=kappa3^2||zeta||2^2. With
Lambda(t)=integral_0^t [sigma(s)-nu kappa3^2] ds, this yields

    ||zeta(t)||2 <= exp(Lambda(t))[
      ||zeta(0)||2+integral_0^t exp(-Lambda(s))||h3(s)||2 ds]. (16)

This is an estimate with the **actual full strain**, not the reference
strain. It provides no universal control of Lambda. If f is x3-independent,
a proposed target ||zeta(t)||2>=Z requires
||zeta(0)||2>=Z exp(-Lambda(t)); a new nonzero derivative cannot appear
from exactly zero without symmetry-breaking force. This L2 derivative
budget alone is not a continuation criterion.

The analogous angular derivative in Euclidean space must differentiate
the rotating vector basis. Let Jx=(-x2,x1,0) and define

    R u=(Jx).grad u-Ju.                                   (17)

Then R u=0 is axisymmetry of the cylindrical vector components. The
operator R commutes with the vector Laplacian and acts on convection as

    R(u.grad u)=(R u).grad u+u.grad(R u),
    R(grad p)=grad[(Jx).grad p].                           (18)

Thus (14)-(15) hold with zeta=R u and h3 replaced by R f, for a decaying
whole-space velocity with justified integrations or a complete compact
chart field with no boundary flux. The forcing derivative is R f,
including -Jf. The coordinatewise derivative (Jx).grad u by itself does
**not** vanish for an axisymmetric vector field. Equation (18) is not a
global rotational symmetry of a generic flat torus. If only a local core
is rotated, boundary/localization terms must be restored before using it.

## 6. Required evidence for the next proposal

A proposed escape from the annular or 2D3C geometry should provide the
actual complete reference, the complete difference w and force mismatch g,
and the quantities A,E,B on the same stage or prospective terminal
interval. If (7) holds uniformly through the proposed singular time, the
construction is regular. If the proposal works at a different axis, scale,
or older state on successive stages, no fixed-reference estimate is
automatically uniform; all changed constants and accumulated coefficients
must be charged.

For a signed amplification claim, retain the actual stretching integral
in (15) or derive the corresponding full mode interaction, together with
diffusion and force. Crossing the upper-bound stability threshold is not
such a signed lower bound. Neither the annular exclusion nor its
perturbative neighborhood rules out the open alternatives outside its
quantitative hypotheses.

## Review and calculation boundary

The coordinating agent independently checked the three host pairings,
the exact Young constant, treatment of the velocity mean in H1, the cubic
comparison formula, the shear coefficient integral, the cyclic datum's
norm, and both symmetry-derivative signs. That review passes the stated
finite-time perturbation theorem. This is independent AI review, not an
external expert review or a formal certificate.

Additional exact symbolic checks passed for the rotation/convection,
rotation/Laplacian and rotation/pressure identities, including a negative
control using the incorrect derivative without its vector-basis term.
The Young remainder factors as
z^4-4z^3+27=(z-3)^2(z^2+2z+3), verifying its displayed optimal scalar
constant. Differentiation checks the cubic comparison formula and (11);
the cyclic datum is exactly solenoidal with constant H1 density 3 eta^2.
These finite algebra checks do not replace the energy or continuation
arguments.
