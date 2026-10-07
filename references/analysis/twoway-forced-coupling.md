# A reverse-wave feedback loop: resonance, viscosity and its physical force

8 September 2026. **Reviewed bounded written calculation.** The
[independent review](coupled-stages-review.md) records the
coordinating agent's complete read and exact mathematical source hash.
This is AI-agent review, not external expert acceptance or a formal PDE
certificate. Ordinary physical viscosity nu>0 is fixed. The older periodic
host and wave are exactly those of the
[finite three-dimensional stage](threed-forced-stage.md),
current source SHA-256
`a7cc608ad90dd598d0b3a2b2bd36308b80f90d879fa062b8ea886d496909cb3f`.
The [previous inheritance test](inherited-forced-host.md)
has current SHA-256
`9e39e482e374f6e27e393d434cd2b243f13a4c109563c8df7877eb07e182102b`.

A reverse wave depending on x3 closes the E31/E13 feedback loop and changes
the full central eigenvalues. It is therefore different from the earlier
triangular receiver. Its two-wave interior perturbation still depends on
only x1,x3; this calculation does **not** supply a genuinely
three-directional nonlinear interior. The compact full periodic field
does retain three-dimensional dependence through the specified host and
cutoffs. Every interaction of that actual field is included below.

The useful result is a precise resonance test. The interior nonlinear
force can vanish at equal frequencies, but the physical mixed derivative
of its curl then costs 8lambda times the two-way gradient product. A
separate finite-interval lower bound incorporates diffusion and an
explicit useful-loop-clock requirement. Neither bound rules out velocity
corrections which change the selected fields. No DNS, infinite trajectory,
universal regularity claim or solution of ROOT/FORCED-D is supplied.

## 1. Actual input, ordinary viscosity and the two-way matrix

Keep the earlier H, P_H, f_H, with H=Ax in |x|<2R and

    A=diag(lambda,2lambda,-3lambda), lambda>0.

In the common flat core, consider the completely specified velocity

    u=Ax+a(t)sin(kappa(t)x1)e3+b(t)sin(ell(t)x3)e1.    (1)

The first wave is the old state. The nonzero b0 wave is an additional
incoming datum, or must be activated by the smooth forcing charged in
section 4. It is not generated from b0=0 by the formulas below. Take
a0,b0,K,L positive; absolute values give the force bounds for other signs.

The exact Kelvin histories relative to Ax are

    kappa=K exp(-lambda t), ell=L exp(3lambda t),
    D_a=nu K^2[1-exp(-2lambda t)]/(2lambda),
    D_b=nu L^2[exp(6lambda t)-1]/(6lambda),
    a=a0 exp(3lambda t-D_a),
    b=b0 exp(-lambda t-D_b).                          (2)

Thus a'=(3lambda-nu kappa^2)a and b'=(-lambda-nu ell^2)b.
These contain the full ordinary Laplacian, not a modified dissipative
operator. The old velocity gains by exp(3Theta-D_a); the reverse
velocity **decays** by exp(-Theta-D_b). Its frequency stretches instead
of contracting. The two heat clocks cannot be identified.

At the stationary central particle, define

    s=a kappa, r=b ell, P=s r,
    B=grad u(t,0)=A+sE31+rE13.                        (3)

The eigenvalues are 2lambda and -lambda plus or minus
sqrt(4lambda^2+P). For P>0 this is a true two-way hyperbolic loop, not a
nilpotent shear. Nonnormality also remains when s and r have different
sizes. The product and relative gradient have the exact histories

    P(t)=P(0) exp(4lambda t-D_a-D_b),
    r/s=[b0 L/(a0 K)]exp(D_a-D_b).                    (4)

In particular its possible finite growth is bounded by the original
base clock, P(t)<=P(0)exp(4lambda t). No new faster host has been freely
substituted. With K=L at initial time, D_b>=D_a for t>=0, so a balanced
outgoing reverse gradient requires an at-least-comparable incoming
reverse gradient. Other K/L choices must use the actual ratio in (4).

When the plateau contains full phases in both directions, its perturbation
velocity norm is sqrt(a^2+b^2). The b contribution is already supplied;
there is no additional velocity mode or feedback-driven amplitude gain
hidden in (2). The interaction force below is what keeps this particular
two-mode velocity on its assigned Kelvin histories.

## 2. Complete interior momentum and the pressure-bearing interaction

The two self-advections vanish. The complete cross advection is

    N=ab[ell sin(kappa x1)cos(ell x3)e1
             +kappa cos(kappa x1)sin(ell x3)e3].      (5)

Its divergence is 2ab kappa ell cos(kappa x1)cos(ell x3). Set

    p_int=[2ab kappa ell/(kappa^2+ell^2)]
                             cos(kappa x1)cos(ell x3),
    delta=(ell^2-kappa^2)/(ell^2+kappa^2).

Then Delta p_int=-div N. With the background quadratic pressure,
substitution into the **full** ordinary NS momentum equation leaves
exactly the divergence-free interior force

    f_int=N+grad p_int
      =ab delta[ell sin(kappa x1)cos(ell x3)e1
                   -kappa cos(kappa x1)sin(ell x3)e3]. (6)

No phase mean or cross sideband was deleted. These are the two combined
wavevectors (kappa,0,ell) and (kappa,0,-ell). They have squared physical
frequency kappa^2+ell^2; treating their subsequent evolution as free
waves would require that full diffusion as well as their interaction
with u. Here (6) is their complete physical force, not an approximation.

The pressure-independent curl component is

    (curl f)_2=ab(kappa^2-ell^2)sin(kappa x1)sin(ell x3). (7)

At kappa=ell the interaction is purely a pressure gradient and f_int=0.
This is a genuine cancellation, so a lower bound proportional to
ab max(kappa,ell) without a frequency-mismatch factor would be false.
But ell/kappa=(L/K)exp(4lambda t); equality occurs at most once in any
positive-length flight with lambda>0.

## 3. Actual particles, physical covectors and the available core

The phases in (2) follow Ax; they are not transported phases of the
full two-way velocity. With D_u=partial_t+u.grad,

    D_u(kappa x1)=kappa b sin(ell x3),
    D_u(ell x3)=ell a sin(kappa x1).                   (8)

These are precisely the cross advections charged in (5)-(6). Treating
both left sides as zero would omit the feedback under examination.

For an actual particle remaining on the plateau, use the background
labels X1=exp(-lambda t)x1, X2=exp(-2lambda t)x2,
X3=exp(3lambda t)x3. Their exact equations are

    X1'=exp(-lambda t)b(t)sin(LX3),
    X2'=0,
    X3'=exp(3lambda t)a(t)sin(KX1).                   (9)

Thus the reverse wave also changes the support/deformation calculation.
The source's transported cutoff still has widths
r0 exp(lambda t), r0 exp(2lambda t), r0 exp(-3lambda t), but it is not
a material cutoff for (1). If its flat label box contains |Xi|<c0 r0,
a sufficient condition that every particle from a central ball of
radius b_core remains in that box is

    b_core exp(C_label(t))<c0 r0,
    C_label(t)=(1/2)integral_0^t
            [L exp(-lambda v)b(v)+K exp(3lambda v)a(v)]dv. (10)

Indeed the symmetric part of the two-by-two coefficient bound obtained
from |sin z|<=|z| has operator norm half the displayed sum. A bootstrap
up to first plateau exit proves (10). This is a sufficient shaped-core
budget, not an optimal radius. The central particle remains fixed.
The full Eulerian packet must separately satisfy the source containment
sqrt(3)r0 exp(2Theta)<R for the whole gain and activation window.

A new genuinely transported infinitesimal covector at the center obeys

    xi1'=-lambda xi1-s xi3,
    xi2'=-2lambda xi2,
    xi3'=3lambda xi3-r xi1.                          (11)

Its heat clock is nu integral |xi|^2dt. Equations (11), rather than
either scalar frequency in (2), are the covector history for a later
receiver on this actual new host. No constant-coefficient diagonalization
or polynomial arbitrary-error estimate is inferred. For example a valid
coarse norm bound is

    |xi(t)|<=|xi(0)|exp(C_xi(t)),
    C_xi(t)=3lambda t+(1/2)integral_0^t(s+r)dv
       <=3Theta+[(s(0)+r(0))/(4lambda)](exp(2Theta)-1). (12)

This explicitly retains the large shear conditioning. Useful next-wave
polarization, damping and nonlinear error bounds are not supplied by the
central eigenvalues alone.

## 4. Exact compact periodic fields and the entire force budget

Use the same product cutoff chi(t,x)=chi0(exp(-tA)x/r0) as the old wave.
The old compact curl W and pressure pi_W are already fixed. Realize the
reverse wave as

    V=curl[(b/ell)chi cos(ell x3)e2]
      =(b chi sin(ell x3)-(b/ell)chi_3 cos(ell x3),
        0, (b/ell)chi_1 cos(ell x3)).                (13)

Both waves are exactly solenoidal, compact and mean zero. Write
L_A=partial_t+Ax.grad-nu Delta and choose the compact pressure

    pi_V=8lambda(b/ell^2)chi_1 sin(ell x3).

The complete reverse linear residual is

    (L_A+A)V+grad pi_V=R_V,
    (R_V)_1=8lambda(b/ell^2)chi_11 sin(ell x3)
        -nu b[(Delta chi+2chi_33)sin(ell x3)
              +2ell chi_3 cos(ell x3)
              -(Delta chi_3/ell)cos(ell x3)],
    (R_V)_2=8lambda(b/ell^2)chi_12 sin(ell x3),
    (R_V)_3=8lambda(b/ell^2)chi_13 sin(ell x3)
          -nu(b/ell)Delta chi_1 cos(ell x3)
          +2nu b chi_13 sin(ell x3).                 (14)

Let R_W be the previously supplied complete residual for W. The actual
periodic velocity, pressure and force on the flight are

    u=H+W+V,
    p=P_H+pi_W+pi_V+chi^2 p_int,
    f=f_H+R_W+R_V+W.grad W+V.grad V
                  +W.grad V+V.grad W+grad(chi^2 p_int). (15)

Every pressure here is a smooth compact chart function extended
periodically. Thus (15) includes all cutoffs and pressure terms without
unpriced Leray tails. Its plateau restriction is exactly (6). The
complete older force f_old=f_H+R_W+W.grad W remains present.

For explicit finite-window bounds define

    rho=min_t,i r_i(t), k_*=min_t kappa, l_*=min_t ell,
    K_*=max_t kappa, L_*=max_t ell,
    a_*=max_t a, b_*=max_t b,
    e_a=1/(k_*rho), e_b=1/(l_*rho),
    M_x=K_*+L_*+rho^(-1),
    delta_*=sup_t |delta(t)|,
    L_b=lambda/(l_*^2 rho^2)+nu L_*/rho
                              +nu/rho^2+nu/(l_*rho^3).

Assume e_a,e_b are bounded by one fixed small constant and the full
support is inside the affine core. Equation (14) gives
||R_V||infinity<=C b_* L_b. The reverse self-interaction obeys
||V.grad V||infinity<=C b_*^2 rho^(-1)(1+e_b)^2.
For the complete cross interaction C_cross in (15),

    ||C_cross||infinity <= C a_*b_*
       [delta_*(K_*+L_*)+rho^(-1)
                         +(e_a+e_b+e_a e_b)M_x].     (16)

To verify (16), the two principal waves give chi^2 times (6), plus
cutoff-derivative terms of size O(ab/rho). Differentiating chi^2 p_int
adds the same cutoff scale because |p_int|<=ab. Each remaining cross
term has at least one curl correction of relative size e_a or e_b and
costs at most M_x for its derivative. The frequency-ratio losses are
therefore retained even when kappa and ell are quite different.

For activation beta(t), use beta V and pressure increment
beta(pi_V+chi^2p_int), with |beta^(j)|<=C_j Delta^(-j). The exact force
increment over the same old state is

    beta R_V+beta C_cross+beta^2 V.grad V+beta' V.     (17)

Here C_cross=W.grad V+V.grad W+grad(chi^2p_int).
This prices the additional receiver rather than relabelling it as an
inherited input. Set

    M_t=lambda[1+(K+L)r0]+nu(K_*^2+L_*^2)+Delta^(-1).

For every fixed mixed order p,m the full increment in (17) satisfies

    ||D_x^p partial_t^m delta f||infinity
      <= C_(p,m,Theta_bar) M_x^p M_t^m
       { b_*[L_b+Delta^(-1)(1+e_b)]
          +b_*^2 rho^(-1)(1+e_b)^2
          +a_*b_*[(delta_*+1_(m>=1))(K_*+L_*)
                    +rho^(-1)+(e_a+e_b+e_a e_b)M_x] }. (18)

All constants depend only on fixed bumps, orders and the bounded base
window. Spatial differentiation uses M_x. At fixed Eulerian x,
phase differentiation pays lambda(K+L)r0; amplitude differentiation
pays lambda+nu(K_*^2+L_*^2); the cutoff and inverse wavevectors pay
lambda. These facts prove (18) by the ordinary product rule. The extra
1_(m>=1) is intentional: delta can be zero while delta' is nonzero.
Multiplying every time derivative by the small zeroth-order mismatch
delta_* would miss the resonance cost.

Add the existing complete f_old budget from the finite-stage source to
(18). Any host activation or replacement also pays its separate host
ramp budget. Choosing b0 small makes this one finite increment small
at each fixed order, but simultaneously makes P small with the older
a fixed. No such finite-order choice proves one smooth terminal force.

## 5. Pressure-independent finite-time and resonance lower bounds

Assume that at the measured time the common flat core contains the
rectangle 0<=x1<=pi/kappa, 0<=x3<=pi/ell at a fixed flat x2. A sufficient
condition for this throughout the flight is Kr0 and Lr0 sufficiently
large relative to the fixed plateau constants. The rectangle has a
strict flat buffer, and beta=1 on an open neighborhood of the flight.

Stokes' theorem applied to (7) gives circulation magnitude
4ab|kappa^2-ell^2|/(kappa ell). Its perimeter is
2pi(kappa+ell)/(kappa ell). For **every** smooth pressure change,

    ||f(t)||infinity >= (2/pi)ab|kappa-ell|.           (19)

Pressure can neither change this circulation nor its curl. Also, if
||D_x f||infinity denotes the maximum of the componentwise first
derivatives, evaluation at the two sine maxima gives

    ||D_x f(t)||infinity >= (1/2)ab|kappa^2-ell^2|.   (20)

At an exact resonance time t*, put kappa(t*)=ell(t*)=q*. The bulk
force in (6) vanishes, but Eulerian differentiation of (7) gives

    partial_t(curl f)_2(t*,x)
       =-8lambda a(t*)b(t*)q*^2 sin(q*x1)sin(q*x3).  (21)

The derivatives of the sine phases and of ab multiply the zero
frequency mismatch at this time. The remaining coefficient is
(kappa^2-ell^2)'=-8lambda q*^2. Consequently

    max_(i,j)||partial_i partial_t f_j(t*)||infinity
       >=4lambda a(t*)b(t*)q*^2=4lambda P(t*).       (22)

This is an ordinary physical mixed derivative, with no conversion from
a material derivative. A time-dependent pressure change also has zero
curl derivative. Thus shrinking a resonance window cannot hide an
unbounded positive loop product P at fixed lambda under a force smooth
through one finite terminal time. This is a bound on the unchanged
specified two-wave velocity and its surviving flat core, not on all
possible nonlinear completions.

For a whole flight [0,tau], let q_min=min_t min(kappa,ell) and
F_I=sup_[0,tau]||f||infinity. Since

    (ell-kappa)'=lambda(3ell+kappa)>=4lambda q_min,

at least one endpoint has |ell-kappa|>=2lambda q_min tau. Moreover,
ab(t)>=a(tau)b(tau)exp(-2Theta) for 0<=t<=tau, because the heat clocks
are increasing. Equation (19) therefore yields the exact bound

    F_I >= (4/pi)exp(-2Theta)a(tau)b(tau)
                                           q_min lambda tau. (23)

It applies even when the equality point has been optimally placed
inside the interval. Cancellation at one instant is not cancellation
on a whole positive-length flight.

## 6. A useful-loop-clock and diffusion test near resonance

Here is a more restrictive but explicit finite-stage test, including
the possibility of tuning the stage around resonance. Suppose t* lies
in [0,tau], Theta=lambda tau<=Theta_bar, and put

    R_loop=sqrt(P(t*))=sqrt(a(t*)b(t*))q*.

Impose two **additional quantitative hypotheses** on a proposed flight:

    D_a(tau)+D_b(tau)<=D_bar,
    R_loop tau>=theta0>0.                            (24)

The first limits total diffusion of the two supplied waves. The second
requests a nonvanishing flight measured by the newly proposed loop rate.
It is not a universal necessary condition for every nonnormal transient:
highly unbalanced shears can have a different clock, which must instead
be computed from the actual propagator. We are testing the proposed
two-way eigenvalue mechanism on its own stated scale.

On this interval q_min>=q*exp(-3Theta_bar) and
min(ab)>=a(t*)b(t*)exp(-2Theta_bar-D_bar). The endpoint frequency-gap
argument above then gives

    F_I >= (4/pi)exp(-5Theta_bar-D_bar)
                          lambda R_loop^2 tau/q*.   (25)

On the other hand, the *full ordinary* heat clocks imply

    D_bar >=nu integral_0^tau(kappa^2+ell^2)dt
              >=2nu exp(-6Theta_bar)q*^2 tau.

Combining this with (24)-(25) proves

    F_I >= (4sqrt(2)/pi)exp(-8Theta_bar-D_bar)
          theta0^(3/2) D_bar^(-1/2)
                                  lambda sqrt(nu R_loop). (26)

Thus a uniformly bounded C0 force, fixed nu and lambda, bounded base
clock and heat loss, and a useful fixed loop clock cannot coexist with
R_loop tending to infinity in these selected fields. At exact
resonance (22) already imposes the stronger all-orders smooth-force
restriction without either extra hypothesis (24). If a candidate
drops a heat or clock hypothesis, the corresponding conclusion is
not retained; its new gain and diffusion budget must be computed.

## 7. What the nonlinear completion changes, and what remains open

The selected profiles permit some instantaneous pressure cancellation
unavailable to the earlier one-way mixed mode. They do not provide
new nonlinear velocity transfer for free: b is supplied and decays,
a follows its original host ODE, and (15) is the force required to
keep both assigned profiles. Equations (19)-(26) explicitly quantify
that cost, including its otherwise tempting resonance loophole.

If one instead solves for the full nonlinear perturbation w(t,x1,x3)
in the affine interior, the exact unforced equations are

    w_t+(A_2 x+w).grad_(1,3) w+A_2 w+grad_(1,3)pi
                                       =nu Delta_(1,3) w,
    div_(1,3) w=0, A_2=diag(lambda,-3lambda).

The other velocity component is still u2=2lambda x2. Its scalar
vorticity Omega=partial_3 w1-partial_1 w3 obeys

    Omega_t+(A_2 x+w).grad_(1,3)Omega
                           =2lambda Omega+nu Delta_(1,3)Omega. (27)

The nonlinear completion changes the two-mode ansatz and creates other
modes. For bounded smooth vorticity in a whole-plane setting where the
maximum principle applies, (27) gives
||Omega(t)||infinity<=exp(2lambda t)||Omega(0)||infinity.
That restricted scalar bound is not a velocity estimate for arbitrary
three-dimensional periodic flows, and the compact curl introduces
additional components and dependence outside the flat interior.

Thus this reverse pair is a useful failed intermediate architecture:
it genuinely closes a two-way gradient loop and tests pressure resonance,
but its interior still reduces to a planar vorticity equation. A
genuinely three-directional feedback, or a controlled nonlinear
completion that uses the complete localized geometry, requires a new
same-state momentum, pressure, support, covector and mixed-force
calculation. No conclusion here follows from eigenvalues alone, and
no general no-feedback or no-gain theorem is asserted.

## Verification scope

Exact symbolic substitution checked the entire interior ordinary NS
momentum equation with interaction pressure (6), its curl (7), the
Eulerian mixed derivative at resonance (21), and every component of the
localized reverse-wave residual (14). The matrices, label equations,
product history, circulation and heat-clock inequalities are written
calculations. The coefficient/product bounds price all mixed derivatives
at each fixed finite order, with the old force retained. These checks
are not numerical flow simulation or a formal PDE certificate.
