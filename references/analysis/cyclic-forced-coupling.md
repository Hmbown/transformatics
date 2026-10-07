# A three-direction cycle: the exact feedback that supplied Kelvin waves omit

8 September 2026. Bounded written calculation; the separate AI-agent
[coupled-stage review](coupled-stages-review.md) passed.
That record pins the mathematical source before this introductory label
changed. Equations and estimates are unchanged. This is not external
expert acceptance or a formal PDE certificate.
This note adds a genuinely three-direction interior dependence to the
[finite forced stage](threed-forced-stage.md). Its conclusions
concern the displayed full finite forced fields. They neither exclude a
velocity-corrected construction nor establish any infinite trajectory.
ROOT, E-prime and FORCED-D remain OPEN. No research DNS is used.

## 1. Three supplied waves and their ordinary-viscosity histories

Keep physical viscosity nu>0 and the same compact periodic host H, which
equals Ax in its core, with A=diag(lambda,2lambda,-3lambda). There take

    v=a sin(kappa x1)e3+b sin(ell x3)e2+c sin(m x2)e1,       (1)

with nonzero real initial amplitudes and positive frequencies. Each wave
is divergence free. The dependence follows the closed cycle
x1 -> velocity3 -> x3 -> velocity2 -> x2 -> velocity1 -> x1.
It is not a two-coordinate interior ansatz.

The exact homogeneous viscous linearization about Ax gives

    kappa=K exp(-lambda t), ell=L exp(3lambda t),
    m=M exp(-2lambda t),
    a=a0 exp(3lambda t-D_a),
    b=b0 exp(-2lambda t-D_b), c=c0 exp(-lambda t-D_c),
    D_a=nu K²(1-exp(-2lambda t))/(2lambda),
    D_b=nu L²(exp(6lambda t)-1)/(6lambda),
    D_c=nu M²(1-exp(-4lambda t))/(4lambda).                 (2)

These identities retain the rapid diffusion of the reverse, x3-dependent
wave. All three waves are supplied at the initial time; no generation of
b0 or c0 is asserted.

## 2. Full interior nonlinear residual, including pressure

Use the quadratic core pressure -x.A²x/2. Direct substitution of Ax+v
and (2) into the full NS momentum equation leaves exactly

    f_cycle=
      bc m sin(ell x3)cos(m x2)e1
     +ab ell sin(kappa x1)cos(ell x3)e2
     +ac kappa sin(m x2)cos(kappa x1)e3.                    (3)

There are no additional self-interactions: every original wave is
independent of its own velocity coordinate. Each component of (3) is
also independent of its own coordinate, so div f_cycle=0. Equivalently,
tr[(grad v)²]=0 everywhere. The quadratic interaction therefore has no
interior Poisson source and is already transverse to each of its Fourier
covectors. Pressure cannot remove it by a Fourier projection. The local
circulation argument below avoids treating this interior computation as
a global periodic pressure calculation.

At the origin put

    s_a=a kappa, s_b=b ell, s_c=c m,
    S=s_a E31+s_b E23+s_c E12, B=A+S.

Unlike the preceding one-way extension, the characteristic polynomial is

    det(zI-B)=(z-lambda)(z-2lambda)(z+3lambda)-P,
    P=s_a s_b s_c.                                         (4)

The three-cycle does change the spectrum. It has not thereby created an
increasing new host: (2) gives the exact laws

    kappa ell m=KLM,
    abc=a0 b0 c0 exp(-D_a-D_b-D_c),
    P'=-nu(kappa²+ell²+m²)P.                                (5)

Thus g=|P|^(1/3) decreases in this specified family. For completeness,
a positive diagonal similarity balances all three off-diagonal
magnitudes to g. The resulting off-diagonal matrix is g times a signed
permutation matrix, of operator norm g. Consequently every instantaneous
eigenvalue satisfies Re z<=2lambda+g. This is an eigenvalue bound only:
the similarity changes with time and can be ill-conditioned. It is not
an arbitrary-error propagator bound or an exclusion of nonnormal gain.

The exact omitted strain source is particularly simple:

    grad f_cycle(0)=S²
      =s_b s_c E13+s_a s_b E21+s_a s_c E32.                 (6)

These are the three reverse edges, absent from the original ansatz. A
nonlinear velocity completion must evolve these modes, their further
interactions and the associated full pressure. Keeping (2) while calling
the waves an autonomous nonlinear amplifier omits precisely (3) and (6).
Neither a closed matrix ODE nor a pressure-Hessian closure has been proved
for the completed periodic flow.

## 3. Complete finite periodic realization and force budget

Use the existing smooth transported bump chi, supported strictly inside
the affine core. Form the three compact curls

    W_a=curl[-chi(a/kappa)cos(kappa x1)e2],
    W_b=curl[-chi(b/ell)cos(ell x3)e1],
    W_c=curl[-chi(c/m)cos(m x2)e3].                          (7)

On the plateau they equal (1); globally they include every curl correction
and are smooth, mean zero and periodic. Keep the existing actual old
velocity u_old=H+W_a, pressure p_old and force f_old from the finite stage.
Put V=W_b+W_c, u=u_old+V and p=p_old. The prescribed force is exactly

    f=f_old+(partial_t-nu Delta)V
                  +(u_old.grad)V+(V.grad)u_old+(V.grad)V.  (8)

This preserves the original pressure and force when b=c=0. Every new
term is computed from compact fields; no global pressure tail is dropped.
On the plateau f_old=0 and (8) reduces to (3).

Here are sufficient finite mixed-derivative bounds, including activation.
On a fixed finite window write r_i=r exp(A_ii t), rho=min_(i,t) r_i,

    omega_*=min_(t) min(kappa,ell,m),
    Omega=max_(t) max(kappa,ell,m), e=1/(omega_*rho)<=1,
    a_*=sup_t |a|, Z_*=sup_t(|b|+|c|),
    M_x=Omega+rho^(-1),
    M_t=lambda[1+(K+L+M)r]+nu Omega²+Delta^(-1).

The complete supports must remain in the host core throughout that window.
Eulerian phase differentiation costs lambda(K+L+M)r, in addition to
the amplitude and envelope rates; the material rate alone is insufficient.
For nonnegative fixed integers p,m_t, differentiating (2),(7) gives

    ||D_x^p partial_t^m_t V||infinity
       <=C_(p,m_t) Z_*(1+e) M_x^p M_t^m_t.                (9)

Constants depend on the fixed bump and the bounded base window. If V is
multiplied by a smooth activation alpha with derivative cost Delta^(-j),
the linear terms in (8) acquire alpha, the quadratic term alpha², and
alpha'V is added. The new force increment is bounded by

    C_(p,m_t) M_x^p M_t^m_t {
      Z_*(1+e)[M_t+lambda R M_x+lambda+nu M_x²]
      +(2a_*Z_*+Z_*²)(1+e)² M_x }.                        (10)

This follows directly from the product rule, ||H||infinity<=C lambda R,
||grad H||infinity<=C lambda, and the analogous curl bound for W_a.
Add the old full force and its separately priced host ramps. These bounds
construct a finite smooth forced stage; they do not give one parameter
sequence with a smooth terminal force. Smoothly turning off V simply
returns the old state and pays its activation cost.

## 4. Three local loops give pressure-independent costs

Assume the common plateau contains the following three rectangles at the
time of measurement, with the specified vertical side lengths:

- Fix x1=0; vary x2 from -pi/(2m) to pi/(2m), and x3 over length h3,
  with m h3>=pi. On the x2 sides the e2 component of (3) is zero.
- Fix x3=0; vary x1 from -pi/(2kappa) to pi/(2kappa), and x2 over
  length h2, with kappa h2>=pi. On the x1 sides its e1 component is zero.
- Fix x2=0; vary x3 from -pi/(2ell) to pi/(2ell), and x1 over length
  h1, with ell h1>=pi. On the x3 sides its e3 component is zero.

The circulations have magnitudes 2|ac kappa|h3, 2|ab ell|h2, and
2|bc m|h1. Dividing by the respective perimeters gives, for every smooth
pressure choice and the same unchanged velocity,

    F=||f||infinity >= (1/2) max(|ac kappa|,|ab ell|,|bc m|).
                                                               (11)

All old host and cutoff forces vanish on these loops. Exterior corrections
cannot change their circulations. Taking the geometric mean in (11), with
V_g=|abc|^(1/3), yields

    F >= (1/2) V_g g.                                      (12)

The factor V_g is the geometric mean of the three supplied wave amplitudes,
not the full velocity norm. A highly unbalanced triple can have a small
V_g and a large largest amplitude; (12) does not exclude that case or
prove a general force-versus-velocity theorem. If a required rectangle does
not fit, its particular lower bound is unavailable. The upper bounds in
(10) are not being used as evidence for these lower bounds.

## 5. What this changes in the next attempt

The smallest genuine three-direction Kelvin cycle has a nonzero cubic
spectral invariant, but that invariant is supplied and dissipates rather
than growing. Its full quadratic force is already solenoidal, and its
gradient creates the missing reverse cycle (6). A useful next construction
must include that nonlinear feedback in the velocity and recover pressure
and localization for the resulting complete flow. It cannot keep the
three independent Kelvin histories and discard their cross force.

This result complements the [reverse-pair calculation](twoway-forced-coupling.md),
whose planar interior can have a moment of pressure cancellation. There
is no analogous cancellation of (3) merely by choosing equal frequencies.
Neither calculation rules out a redesigned nonlinear stage, and neither
solves ROOT or FORCED-D.
