# Exact shear stability budget and its transfer boundary

**Research appendix — 8 September 2026.** **Review status:** an independent algebra read checked the exact affine Kelvin map and its uniform all-orientation bound. The background is a prescribed affine drift, with the domain and infinite-energy limitations stated below. No improved propagator estimate for the actual spatially varying periodic q follows from this calculation. The numerical diagnostic in section 8 is a recorded sign/implementation check, not an analytic or formal certificate.

All four appended derivations remain outside the registered proof graph; full formalization and ROOT / `(E′)` remain open. See the [next-transfer review index](../navier-stokes/next-transfer-review.md) for the common scope and remaining estimates.

The original derivation follows, with local references relocated. Its original drafting-status sentences are retained as historical text. Source artifact: `nse-shear-stability-budget-20260908.md`; SHA-256 `085b4246a3957ad28a910f0703af23a4a7de64337f3f821e4d30f02095a19260`.

---

8 September 2026. Independent bounded audit. No repository changes, DNS, UI work, or publication. ROOT remains OPEN. The exact formulas and uniform bounds in §§1–4 below are direct derivations; §5 distinguishes proved bounded-operator perturbation estimates from the missing variable-background PDE theorem.

## 1. Equation and domain: what is actually being solved

Consider the prescribed affine drift U(t,x)=sigma(t) x_3 e_1, with locally integrable real sigma, and the full incompressible linear equation

    v_t + U.grad v + (v.grad)U + grad pi = epsilon Delta v + f,
    div v=0,                       epsilon>=0.

This is naturally an equation on R^3, or on a domain periodic in the two directions parallel to the shear and unbounded in x_3. The perturbation can have finite L2 norm. The affine background itself has infinite energy and is NOT a well-defined periodic background on a fixed three-torus. Time-dependent sigma is a prescribed nonautonomous drift: unless sigma is constant, this affine field is generally not an unforced NS solution (sigma'(t)x_3 e_1 cannot be canceled by a scalar pressure). These distinctions remain even though the linear equation is well-defined.

The following is an exact Fourier solution of that equation, not only a principal geometric-optics approximation. A local affine jet of an admissible background does not inherit this global propagator automatically.

## 2. Full viscous Kelvin propagator, with no singular division by streamwise frequency

Fix initial time s and Fourier label eta=(p,q,r). Set

    theta(t,s)=integral_s^t sigma(u)du,
    xi(t)=(p,q,r-p theta(t,s)),
    K(t)=|xi(t)|^2,
    D_epsilon(t,s,eta)=exp[-epsilon integral_s^t K(u)du].

For the homogeneous equation f=0 and v=b(t)exp(i xi(t).x), pressure amplitude and polarization obey exactly

    pi_hat=2i sigma(t) p b_3/K,
    b'=-sigma b_3 e_1 + 2sigma p b_3 xi/K -epsilon K b.

Thus b=D_epsilon times the inviscid polarization. The factor two follows by differentiating xi.b=0; it includes the entire pressure contribution. The scalar viscous factor commutes with the polarization evolution.

Here is a representation uniform through p=0. For kappa=sqrt(p^2+q^2)>0 define orthonormal horizontal vectors

    E_H=(p,q,0)/kappa,        E_T=(-q,p,0)/kappa,
    E_P(t)=(-(r-p theta)E_H+kappa e_3)/sqrt(K(t)).

Write the initial solenoidal amplitude as b(s)=a_s E_P(s)+c_s E_T. Then

    [a_t]                [ R   0 ] [a_s]
    [c_t] = D_epsilon *  [ J   1 ] [c_s],

    R=sqrt(K(s)/K(t)),
    J=q sqrt(K(s)) integral_0^theta
          du/[kappa^2+(r-pu)^2].                         (A)

The output basis is (E_P(t),E_T), so the displayed Euclidean matrix norm is the physical velocity-amplitude norm. To derive it, remove damping, observe b_3 K is constant, and take the E_T component of the ODE: c'=sigma(q/kappa)b_3. This avoids the appendix's reconstruction formula dividing by p.

Formula (A) remains continuous at p=0: R=1 and J=q theta/sqrt(q^2+r^2). When kappa=0 but eta is nonzero, transversality gives b_3=0 and the polarization is constant, with ordinary heat damping. The zero Fourier mode, when the domain admits it, solves b'=-sigma b_3 e_1 and has the same linear shear bound.

For p nonzero one may evaluate the integral by arctangents, but that expression should not be bounded by a constant proportional to 1/|p|. Keeping the integral or using the following uniform estimate resolves the near-zero streamwise-frequency issue.

Time dependence and sign changes of sigma cause no inviscid loss beyond its NET integral theta. The inviscid coefficient ODE can be parametrized by theta; its primitive makes (A) valid even when theta reverses direction. Viscous damping retains the full path integral of K, not merely the endpoint theta.

## 3. Uniform polynomial bound for every Fourier orientation

Put P=p/kappa, Q=q/kappa and rho=r/kappa. Then

    J=Q sqrt(1+rho^2) integral_0^theta
                           du/[1+(rho-Pu)^2].

For either sign of theta, use

    sqrt(1+rho^2) <= sqrt(1+(rho-Pu)^2)+|P||u|.

The first resulting integral is at most |theta|. The second is at most pi|theta|, because |u|<=|theta| and the arctangent integral satisfies

    |P| integral_segment du/[1+(rho-Pu)^2] <= pi.

For P=0 the second term is zero. Hence, without any orientation restriction,

    |J| <= (1+pi)|theta|.

Also xi(s)=xi(t)+p theta e_3 and |p|<=|xi(t)|, so

    R <=1+|theta|.

Consequently, for every nonzero label on its transverse plane,

    ||M(t,s,eta)|| <= 1+(2+pi)|theta(t,s)|.                (B)

The constant is deliberately unoptimized. This is LINEAR polynomial growth, not a bound with a hidden 1/p or initial-orientation constant. The reverse inviscid map satisfies the same bound with -theta. The p=0,q nonzero,r=0 lift-up map has norm comparable to |theta|, so a uniform O(1) bound is false; the linear order is sharp.

The Kelvin frequency relabeling eta -> xi(t) has determinant one. Plancherel and D_epsilon<=1 therefore give, for arbitrary solenoidal finite-energy errors,

    ||S_epsilon(t,s)v_s||_2
          <=[1+(2+pi)|theta(t,s)|]||v_s||_2.              (C)

No Fourier support restriction, prepared transversality relative to one chosen carrier, or excluded near-zero streamwise frequency is needed. With solenoidal forcing, Duhamel yields the same kernel multiplying ||f(s)||_2. For non-solenoidal forcing apply the exact orthogonal Leray projection; its L2 norm is at most one.

The usual exp(C integral |sigma|) energy bound is therefore genuinely replaceable by (C) for this exact affine-shear equation. Oscillatory sigma can make the improvement even larger, since net shear, rather than total variation, controls the inviscid factor.

## 4. Viscosity and norm weights

For constant sigma over an interval of length tau,

    integral K = (p^2+q^2)tau
       +tau(r-sigma p tau/2)^2 +sigma^2 p^2 tau^3/12.

This is the exact enhanced-dissipation quadratic form. Its cubic term disappears at p=0 and is not uniform as p tends to zero. Thus enhanced dissipation cannot supply a direction-uniform replacement for lift-up growth. The all-orientation estimate (C) does not need it.

Define a transported Fourier Sobolev norm by weighting the initial label eta, equivalently pull back the velocity components by the volume-preserving shear map before taking H^s. Since the weight is fixed for each Kelvin label, (C) holds in that norm with the same linear factor. More general nonnegative scalar weights of eta have the same property whenever the norm is finite.

For ordinary physical inhomogeneous H^s, s>=0,

    <xi(t)> <= (1+|theta|)<eta>,
    ||S_epsilon(t,s)||_{Hs -> Hs}
                  <= C_s(1+|theta|)^(s+1).               (D)

One can also use the exact inviscid inverse polarization to define a Fourier symmetrizer with no inviscid growth, but its equivalence with physical L2 deteriorates polynomially with theta. Calling that an invariant norm does not remove the cost when converting back to physical errors. These statements concern Fourier/co-moving weights, not arbitrary spatially weighted norms: multiplication by x and spatial cutoffs introduces additional commutators.

On the proposed terminal interval, |sigma|<=C lambda and

    Delta=lambda^(-3/4),       lambda Delta=lambda^(1/4).

Thus the exact affine-shear L2 propagation cost is O(lambda^(1/4)), rather than exp(C lambda^(1/4)). The physical H^s cost from (D) is O(lambda^((s+1)/4)); the transported H^s cost remains O(lambda^(1/4)). This would be materially sharper if transferred to the actual background. It is not yet such a transfer theorem.

## 5. What a perturbation costs—and which hypothesis is insufficient

### 5a. A genuinely L2-bounded perturbation: a useful precise lemma

Suppose an additional linear operator K(t) acts on the same solenoidal Hilbert space with ||K(t)||_{2->2}<=beta. This is stronger and different from saying that a velocity-gradient perturbation is bounded. Duhamel with (C) gives

    y(t)<=C(1+lambda t)y(0)
          +C beta integral_0^t (1+lambda(t-r))y(r)dr.

The scalar Volterra resolvent, equivalently the roots of
z^2-C beta z-C beta lambda=0, yields

    y(t)<=C(1+lambda t)
               exp[C(beta+sqrt(beta lambda))t] y(0).     (E)

Constants can be enlarged without depending on lambda. This follows also by summing convolution powers of the affine kernel; no eigenvector assumption is needed. The same resolvent controls external forcing.

At Delta=lambda^(-3/4), fixed beta costs
exp[O(beta lambda^(-3/4)+sqrt(beta)lambda^(-1/4))], tending to one. Hence a bounded-operator perturbation preserves the useful polynomial bound on this short interval. For multiplication by a bounded matrix followed by the exact Leray projector, the operator hypothesis does hold.

### 5b. Why a bounded matrix B(t) in the GRADIENT is not automatically 5a

If the actual affine gradient is A(t)=sigma(t)e_1 tensor e_3+B(t), its drift includes B(t)x. The extra linear PDE operator contains BOTH

    (B(t)x).grad v       and       B(t)v,

as well as the corresponding pressure projection. The first operator is unbounded on L2, despite trace B=0 making its direct energy pairing skew. Treating the whole perturbation as K of size ||B|| in (E) is invalid. In Kelvin variables it changes the covector itself:

    xi'=-(sigma e_1 tensor e_3+B)^T xi.

An adapted Fourier energy would have to price the B-driven change of its symbol as well as Bv. No such all-orientation symmetrizer-commutator bound for the actual q is proved here.

There is a concrete long-time obstruction to a bound depending only polynomially on total shear and uniformly bounded B. Take constant B=beta e_3 tensor e_1, beta>0, and returning xi=e_2. Pressure vanishes for this covector on the e_1/e_3 plane and

    [b_1]'= -lambda b_3,    [b_3]'= -beta b_1.

The exact matrix has eigenvalues +/-sqrt(lambda beta), so exponential growth is real. This is an affine-jet control, not a finite-energy periodic NS example. Viscosity multiplies it by exp(-epsilon |xi|^2 t).

On the short Delta interval this example does NOT obstruct a polynomial bound: writing omega=sqrt(lambda beta), the off-diagonal propagator is (lambda/omega)sinh(omega Delta)=lambda Delta[1+O(lambda beta Delta^2)], and omega Delta=sqrt(beta)lambda^(-1/4). Its gain is O(lambda^(1/4)) with a vanishing relative correction for fixed beta. This is consistent with a sharper short-time theorem but does not prove that theorem for all affine B or every Fourier orientation. The appendix's robust selected-carrier estimate supplies a restricted lower bound; it is not an all-mode upper propagator bound.

A basic covector check illustrates the missing uniformity. If F_0=I+theta e_1 tensor e_3 and zeta=F_0^T xi, then

    zeta'=-F_0^T B^T F_0^(-T) zeta.

Its coefficient is bounded by C beta(1+lambda t)^2, with integrated cost O(beta[Delta+lambda Delta^2+lambda^2 Delta^3])=O(beta lambda^(-1/4)). This gives a useful small perturbation in shear coordinates. It does not alone control pressure polarization in physical coordinates: the shear coordinate condition number and angular derivatives of the polarization multiplier must also be tracked. Omitting those conversions would be another unproved step.

### 5c. Spatial localization and shear variation

For a true perturbing velocity R(t,x), the terms are

    R.grad v + v.grad R,

with nonlocal pressure. A C1 bound on R does not make R.grad an L2-bounded perturbation. On H^s it also introduces derivative/commutator requirements. A frequency-dependent bound ||R.grad v||_2<=||R||_infinity||grad v||_2 loses a wavelength; at secondary wavelength k this costs ||R||/k, not merely ||grad R||.

For the actual outgoing wave, a small packet of width d=h^(5/4) sees approximately affine coefficients on the cell scale h; geometric coherence pays d/h=h^(1/4) times the established propagation factors. That is precisely a localized construction estimate, not an arbitrary-error propagator estimate. The residual and its exact Leray projection can have nonlocal tails, and an arbitrary solenoidal error need not stay inside the small patch. There is no global decomposition of the actual periodic q into an admissible affine shear plus an L2-bounded operator of size O(1).

Even an exact spatially varying parallel shear U=F(z)e_1 does not have the affine Fourier decoupling. The two-dimensional perturbation vorticity equation contains

    omega_t+F(z)partial_x omega - F''(z)partial_x psi
                     =epsilon Delta omega,   Delta psi=omega

Here the planar perturbation is (v_x,v_z)=(-partial_z psi,partial_x psi), and omega=partial_x v_z-partial_z v_x=Delta psi. The F'' term is zero in Couette and nonzero for the outgoing oscillatory shear. It couples wall-normal Fourier modes through the inverse Laplacian. A local value of F' and its nilpotence does not bound this global operator by the affine multiplier. In cell variables the outgoing wave has order-one shear curvature, not a globally small Couette perturbation. A conclusion of polynomial arbitrary-error growth for it therefore needs a new proof with exact pressure and spatial localization retained.

## 6. Concrete conclusion for repeated transfer

The exact all-orientation affine estimate is a genuine sharper reference bound: linear L2 growth, including near-zero streamwise modes and arbitrary time-dependent shear, with exact viscosity. Its bounded-operator robustness lemma also has an explicit favorable short-window budget. These are useful targets for an adapted norm construction.

What is not supplied is the load-bearing transfer estimate

    ||S_q(t,s)||_{L2_sigma -> L2_sigma}
                       <=C(1+lambda(t-s))^m

for the actual spatially localized outgoing NS solution, or an invariant error class with a comparably controlled norm. One must construct and estimate a shear-adapted pseudodifferential/Fourier energy (including advection and pressure commutators), or prove a prepared packet/tail decomposition closed under the exact error equation. Initial support and a selected-characteristic lower bound do not supply that closure.

Accordingly no exponential-to-polynomial replacement may yet be inserted into the canonical outgoing-wave nonlinear or repeated-stage budget. The exact affine calculation does demonstrate that the generic Gronwall factor is not sharp for the reference shear; the precise open point is stability of that improved norm under the actual varying geometry and its nonlocal errors.

## 7. Primary-source context (not an imported theorem for q)

Bedrossian–Germain–Masmoudi, *On the stability threshold for the 3D Couette flow in Sobolev regularity*, Annals of Mathematics 185 (2017): https://annals.math.princeton.edu/wp-content/uploads/annals-v185-n2-p04-p.pdf . Section 1.4.2 isolates the streamwise-zero heat/lift-up formula. Its broader linear and nonlinear analysis treats Couette geometry, mixing, and viscosity; the nonlinear smallness and regularity hypotheses are not a theorem for our localized outgoing background.

Their *Dynamics near the subcritical transition of the 3D Couette flow I: Below threshold case*, https://arxiv.org/abs/1506.03720 , distinguishes algebraic transient growth from nonlinear instability/global behavior. The uniform estimate (B) above is derived here rather than inferred from their nonlinear theorem. No literature theorem has been used to turn the local affine model into an admissible periodic NS background.


## 8. Bounded verification performed

The endpoint formula (A), including the scalar viscous damping, was compared against independent direct integration of the full three-component pressure-corrected ODE for five orientations: generic, p=0, p=10^(-10), q=0, and p=q=0. The test used sign-changing sigma(t)=3cos(4t)-0.6, epsilon=0.07, and T=1.3. Maximum endpoint discrepancy was 1.74e-12. Scratch diagnostic: [the archived shear diagnostic](checks/check-shear-propagator.py). This checks implementation/sign consistency only; the uniform bound is the analytic argument in §3, not a sampling inference. The official Annals source was also opened and its equation/domain/hypothesis scope checked.
