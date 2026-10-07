# The same cycle's central strain: exact feedback with unclosed pressure

8 September 2026. Bounded continuation-facing diagnostic; the separate
[point-feedback review](cycle-point-feedback-review.md)
and a coordinating-agent read passed. The review pins the source before
this introductory label changed; equations are unchanged. These are
AI-agent reviews, not external expert acceptance or formal certification.
This continues the **same actual solution** in the
[periodic transfer calculation](periodic-cycle-transfer.md).
Its equal cyclic sine datum is a common spatial translation of the
cosine prototype in [frequency activation](../navier-stokes/frequency-activation.md),
with the added seed there set to zero. It is not a new datum or architecture.
The new observable here is the exact central pressure/strain feedback;
the already proved first-coefficient activation is an input, not a new claim.
No DNS, autonomous scalar closure, global regularity or breakdown is asserted.
ROOT, E-prime and FORCED-D remain OPEN.

## 1. Symmetry fixes the form of the gradient, not its evolution

Use the normalized variables of the transfer note: tau=Aq t,
mu=nu q/A>0, U0=(sin y,sin z,sin x), and

    C=E12+E23+E31, C^3=I.

Central inversion and cyclic coordinate permutation are symmetries of
the periodic equation and datum. Uniqueness therefore gives

    U(tau,-x)=-U(tau,x), U(tau,Cx)=C U(tau,x).

The mean-zero pressure is even and cyclically invariant. In particular
U(tau,0)=0, and B=grad U(tau,0) commutes with C. A real matrix commuting
with this three-cycle is a linear combination of I,C,C^2. Since tr B=0,

    B=s(tau)C+r(tau)C^2.                             (1)

Likewise the symmetric pressure Hessian and the velocity Laplacian jet
have the exact forms

    H=Hess Pi(tau,0)=alpha I+beta(C+C^2),
    Delta B(tau,0)=l_s C+l_r C^2.                    (2)

Here Delta B means the spatial Laplacian of grad U evaluated at zero;
it is not the Laplacian of the two time-only coefficients in (1).
The trace of that spatial matrix is zero because div U=0 everywhere.
All identities hold on the same actual smooth lifespan.

Put c=s+r and d=s-r. Then

    S(tau,0)=c(C+C^2)/2,
    omega(tau,0)=-d(1,1,1).

The symmetric strain eigenvalues are c,-c/2,-c/2, and
|S(tau,0)|_F^2=3c^2/2. Thus c and d measure different observables.

## 2. Exact point equations retain two unresolved spatial quantities

Differentiating the complete momentum equation at the stationary center
gives

    B'=-B^2-H+mu Delta B.                            (3)

The center's advective term vanishes because U(tau,0)=0; the quadratic
gradient B^2 does not vanish. The pressure Poisson equation fixes

    3alpha=Delta Pi(tau,0)=-tr B^2=-6sr,
    alpha=-2sr=(d^2-c^2)/2.                         (4)

This also cancels the diagonal part of B^2 in (3), as cyclic symmetry
and incompressibility require. The remaining two equations are

    s'=-r^2-beta+mu l_s,
    r'=-s^2-beta+mu l_r.

Equivalently, with L_c=l_s+l_r and L_d=l_s-l_r,

    c'=-(c^2+d^2)/2-2beta+mu L_c,
    d'=c d+mu L_d.                                  (5)

The second line is exactly vortex stretching at this particle, with its
full Laplacian. It does not imply d'=cd for positive viscosity. The first
line retains the off-diagonal pressure response beta. Neither quantity
is determined by the symmetry-reduced point matrix alone.

## 3. The pressure term is a full nonlocal observable

Let

    g(tau,x)=tr[(grad U(tau,x))^2].

It has spatial mean zero by periodic incompressibility. With the Fourier
convention ghat(k)=V^(-1)integral g(x)exp(-ik.x)dx, the exact mean-zero
pressure is Pi=(-Delta)^(-1)g. Consequently

    beta(tau)=partial_1 partial_2 Pi(tau,0)
      =-sum_(k in Z^3, k!=0)
                       [k1 k2/|k|^2] ghat(tau,k).   (6)

Cyclic symmetry makes the other two off-diagonal entries equal; it
does not make this sum zero. For a smooth solution the series converges
with all derivatives required here. Equivalently it is the periodic
Green-function derivative applied to the full g, interpreted as that
distributional convolution, not an unjustified ordinary kernel integral.

The Laplacian terms also retain all spatial modes. For example,

    l_s=Delta partial_2 U1(tau,0),
    l_r=Delta partial_3 U1(tau,0).                    (7)

They involve third spatial derivatives and cannot be recovered from the
first spatial derivative B at the center. A pointwise positive stretching
factor, or the scalar symmetry of the pressure trace, is not an estimate
for (6)-(7). No sign of their later values is postulated here.

## 4. How the already proved early jets fit these equations

Take U1,U2 and Pi1 from the reviewed transfer note. They give

    s(0)=1, r(0)=0, c(0)=d(0)=1,
    beta(0)=beta'(0)=0,
    l_s(0)=-1, l_r(0)=0,
    l_s'(0)=mu, l_r'(0)=2.

Equation (5) therefore reproduces

    c'(0)=-1-mu, d'(0)=1-mu,
    c''(0)=4mu+mu^2, d''(0)=mu^2-4mu.               (8)

The first pressure Hessian jet is 2I: it is required to cancel the
diagonal second gradient response even though beta'(0)=0. This is the
pressure cancellation already present in the second-order transfer
calculation, not a reason to omit later off-diagonal pressure.

One additional exact pressure jet makes that distinction concrete. Set

    F=sin x sin y cos y cos z
       +sin x sin z cos x cos y
       +sin y sin z cos x cos z.

Using the known U1,U2 in the twice-differentiated pressure Poisson
equation gives

    g''(0,x)=36mu cos x cos y cos z-8F,
    Pi2:=partial_tau^2 Pi(0,x)
                   =12mu cos x cos y cos z-(4/3)F.   (9)

Each term of F has squared Fourier frequency 6; cos x cos y cos z has
squared frequency 3. This verifies the full periodic inverse Laplacian,
not just its trace at the origin. In particular

    alpha''(0)=-12mu, beta''(0)=-4/3.                (10)

The actual off-diagonal pressure begins at
beta(tau)=-(2/3)tau^2+O(tau^3). The uniform Sobolev/time-jet bounds from
the transfer note justify this remainder: differentiating g three times
uses U through its third time derivative, whose H6 bound gives g''' in
H5; applying (-Delta)^(-1) and two spatial derivatives still controls
the value at the center uniformly on the proved local interval.

For a check at the next gradient order,

    l_s''(0)=-2-mu^2, l_r''(0)=-8mu,
    c'''(0)=2/3-2mu-12mu^2-mu^3,
    d'''(0)=-2-2mu+12mu^2-mu^3.                     (11)

These follow both from (5) and from the full third momentum jet with
Pi2 retained. Suppressing beta'' while keeping the other actual jets
changes c''' by -8/3. Thus the first previously invisible pressure term
already changes the subsequent strain feedback quantitatively. This
exact early contribution does not establish the sign of beta at later
times, the sign of c', or a closed increasing amplifier.

## 5. Continuation-facing conclusion

The symmetry reduction is exact and useful: it separates central
symmetric strain, vorticity, the determined pressure trace, the single
remaining off-diagonal pressure value and two viscous spatial jets.
The resulting system (5) is driven by the complete nonlocal solution
through (6)-(7). Closing it requires estimates for those actual terms,
not a fresh supplied wave or a scalar replacement of the full equation.

The finite global-enstrophy gain already proved for this prototype
does not supply such estimates. Nor does controlling this one point
control the maximum gradient elsewhere. A prospective next stage must
retain the actual generated modes and the full pressure/lifetime
budget. No new continuation criterion or infinite construction is
claimed by this point diagnostic.

[Exact controls](checks/check-cycle-point-feedback.py)
verify the symmetry algebra, second pressure Poisson jet, its nonzero
off-diagonal value and the complete third gradient jet. These are
finite algebra checks, not research DNS or formal PDE certification.
