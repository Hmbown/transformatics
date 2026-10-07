# A complete three-dimensional affine-core stage and its boundary-force cost

8 September 2026. Reviewed written finite-stage construction and a restricted
incompatibility. The [independent review](threed-forced-stage-review.md)
pins mathematical source SHA-256
`2ba3b8ba2168fadfe1d7225ff59b7e538a6fca1301684a983f5118541b336b59`.
Root independently read the proof; this review-label change alters no
equation. These AI-agent reviews are not external expert acceptance or
a formal PDE certificate. Ordinary physical
viscosity nu>0 is fixed. The velocity, pressure and force below are actual
smooth periodic fields, with every localization and nonlinear term retained.
The construction gives finite **velocity** gain and a finite-order force
budget. Its simplest compact transported-wave architecture cannot accumulate
unbounded velocity with bounded force. No new DNS, infinite trajectory,
general regularity theorem, or solution of FORCED-D is claimed.

The [two-track contract](../navier-stokes/two-track-program.md),
[force admissibility](../navier-stokes/forced-admissibility.md) and
[gain audit](force-gain-audit.md) are retained. The current
[logarithmic unforced host](../navier-stokes/logarithmic-host.md) supplies
actual large finite strain but no uniform affine approximation with all jets
through an independently chosen descendant flight. It is not substituted
for the explicitly constructed older state in this note.

## 1. A specified older state outside the excluded axisymmetric class

Work on one fixed torus of side 2pi. Choose R>0 sufficiently small that the
ball of radius 3R lies inside one Euclidean chart. Put

    A=diag(lambda,2lambda,-3lambda), lambda>0,
    C_H(x)=-(1/3)x cross (Ax).

The exact identity curl C_H=Ax follows from tr A=0 and homogeneity. Choose
fixed smooth radial unit-scale cutoffs bar chi_H and bar chi_P, both equal
to one on |y|<=2 and zero on |y|>=3. Set chi_H(x)=bar chi_H(x/R) and
chi_P(x)=bar chi_P(x/R), so their derivative constants are independent
of R after the displayed rescaling, and define

    H=curl(chi_H C_H),
    P_H=-(1/2)chi_P x^T A^2 x,
    f_H=H.grad H+grad P_H-nu Delta H.                   (1)

Extend these compact fields periodically. H is exactly solenoidal, its
spatial mean is zero, and P_H is a genuine periodic pressure. On |x|<2R,

    H=Ax, H.grad H=A^2x, grad P_H=-A^2x, Delta H=0.

Thus f_H vanishes in the complete affine core and outside the cutoff ball.
There is no nonperiodic pressure hidden in the construction: its cutoff
gradient is part of f_H. The three distinct eigenvalues of A preclude
invariance under any continuous spatial rotation in a neighborhood of the
origin. In particular this complete older state is not the full
fixed-axis annular velocity excluded by the earlier theorem.

For every fixed spatial order p,

    ||D^p H||infinity <= C_p lambda R^(1-p),
    ||D^p f_H||infinity
       <= C_p[lambda^2 R^(1-p)+nu lambda R^(-1-p)].     (2)

The host is prescribed and paid for; it is not an unforced compact affine
solution. Its genuine pressure-independent force cost is

    ||f_H||infinity >= c nu lambda/R.                  (3)

Indeed pairing its stationary equation with H gives
<f_H,H>=nu||grad H||2^2. The inner ball supplies
||grad H||2^2>=c lambda^2 R^3, whereas
||H||1<=C lambda R^4. This proves (3), for any alternative periodic
pressure as well. The force in our specified pressure convention is
supported in the outer cutoff shell.

## 2. Exact viscous gain inside that core

Use physical time t with the start of the gain interval labelled zero.
Let its length be tau=Theta/lambda, Theta>0. Define

    F(t)=exp(tA), kappa(t)=K exp(-lambda t),
    phi(t,x)=kappa(t)x1+phi0,
    a(t)=a0 exp[3lambda t
             -nu K^2(1-exp(-2lambda t))/(2lambda)].      (4)

The vector a(t)sin(phi)e3 is an exact solution of the full perturbation
equation about Ax wherever no cutoff is present. Its self-advection
vanishes, and no additional interior pressure is required:

    (partial_t+Ax.grad-nu Delta)(a sin(phi)e3)
       +A(a sin(phi)e3)=0.

The physical velocity gain is exactly

    G=a(tau)/a0
      =exp[3Theta-(nu K^2/(2lambda))(1-exp(-2Theta))].   (5)

Frequency contracts from K to K exp(-Theta); the strain gain is instead
G exp(-Theta). The two quantities are not identified. For example
lambda=nu K^2 and Theta=1 give
G=exp[3-(1-exp(-2))/2]>12. This is genuine finite velocity amplification
by a compressive eigen-direction of the full anisotropic host, with
ordinary viscosity already included in its exact heat clock.

## 3. Transported compact support and the complete pressure correction

Take a fixed smooth product bump chi_0(z)=psi(z1)psi_2(z2)psi_3(z3), supported
in (-1,1)^3. Each factor equals one near zero. Later we choose psi also
exactly linear, with nonzero slope, on one fixed subinterval of its
transition region. This is compatible with a smooth nonnegative bump.
Set

    chi(t,x)=chi_0(F(t)^(-1)x/r),
    W=curl[-(a/kappa)chi cos(phi)e2]
      =( (a/kappa)chi_3 cos(phi), 0,
          a chi sin(phi)-(a/kappa)chi_1 cos(phi) ).       (6)

Here chi_i means the physical Cartesian derivative. W is an exact compact
curl and hence solenoidal and mean zero. Incompressibility of F preserves
its support volume. Its principal support half-widths are

    r1(t)=r exp(lambda t),
    r2(t)=r exp(2lambda t),
    r3(t)=r exp(-3lambda t).                            (7)

Choose sqrt(3)r exp(2Theta)<R. Then the complete packet support stays
strictly inside the affine host region throughout the gain interval. For
activation/reset intervals added below, impose the same containment on
their entire finite time window. On the bump plateau W=a sin(phi)e3,
so (5) is an actual velocity difference at suitable interior points,
not merely the coefficient of an unrealized profile.

Put

    pi_W=-8lambda(a/kappa^2)chi_3 sin(phi).              (8)

This compact periodic pressure removes the leading host/curl defect.
Define L_A=partial_t+Ax.grad-nu Delta. A direct expansion gives exactly

    (L_A+A)W+grad pi_W=R_lin,

    R_lin,1= -8lambda(a/kappa^2)chi_13 sin(phi)
              -nu(a/kappa)Delta chi_3 cos(phi)
              +2nu a chi_13 sin(phi),
    R_lin,2= -8lambda(a/kappa^2)chi_23 sin(phi),
    R_lin,3= -8lambda(a/kappa^2)chi_33 sin(phi)
              -nu a[(Delta chi+2chi_11)sin(phi)
                       +2kappa chi_1 cos(phi)
                       -(Delta chi_1/kappa)cos(phi)].   (9)

For example, before pressure correction, the non-diffusive first
component is 8lambda(a/kappa)chi_3 cos(phi); the fast x1 derivative of
(8) cancels it. The other derivatives of (8) remain in (9). The factor
8 uses all three entries of A and the evolving inverse frequency.

The full physical velocity and pressure on the gain interval are

    u=H+W, p=P_H+pi_W,
    f=f_H+R_lin+W.grad W.                              (10)

These are exact ordinary NS fields. The nonlinear term W.grad W is not
dropped, projected away, or assumed small without a bound. All quantities
in (9)-(10) have compact chart support, so there are no unpriced periodic
Leray tails. This particular force need not be divergence-free; the
prescribed pressure and force together satisfy the full momentum equation.

## 4. Upper bounds for the complete force, with Eulerian time derivatives

For a finite window containing the gain interval let

    rho=min_t min_i r_i(t),
    kappa_*=min_t kappa(t)>0,
    K_*=max_t kappa(t),
    a_*=max_t a(t), e_loc=1/(kappa_* rho),
    M_x=K_*+rho^(-1).

The fixed-window constants can depend on its total dimensionless length
Theta_bar, on the chosen bumps and on the derivative order. Assume
e_loc<=c<1 and the complete transported support stays in |x|<R.
The exact residual (9) implies

    ||R_lin||infinity <= C a_* L,
    L=lambda/(kappa_*^2 rho^2)
       +nu K_*/rho+nu/rho^2+nu/(kappa_* rho^3).          (11)

Writing W=W0+Wcorr, the sizes are
|W0|<=Ca_*, |Wcorr|<=Ca_*e_loc. Since W0 is in the e3 direction,
its fast phase derivative does not occur in W0.grad W0. The remaining
cross terms give

    ||W.grad W||infinity
         <= C a_*^2 rho^(-1)(1+e_loc)^2.               (12)

The same cancellation holds after differentiation by the product rule.
Each extra spatial derivative costs at most M_x.

To insert and remove the wave, let alpha(t) be a smooth scalar function,
zero with all derivatives at the outer endpoints, one throughout the gain
interval, with |alpha^(j)|<=C_j Delta^(-j). Use alpha W and alpha pi_W.
The **exact** force difference from the same H is

    delta f=alpha R_lin+alpha^2 W.grad W+alpha' W.     (13)

There is no missing activation term. The finite return to the older state
H is obtained when alpha returns to zero; its cost is included in (13).
The total force remains f_H+delta f.

On the entire compact transported support, |kappa x1|<=C Kr, where K is
the frequency at the chosen time label zero. At fixed Eulerian x,
phi_t=-lambda kappa x1, so the time derivative of the phase pays lambda Kr.
The amplitude pays lambda+nu K_*^2, and the envelope pays lambda. Therefore
define

    M_t=lambda(1+Kr)+nu K_*^2+Delta^(-1).

For every fixed pair of derivative orders p,m, direct differentiation of
(9) and (13) yields the complete physical bound

    ||D_x^p partial_t^m delta f||infinity
       <= C_(p,m,Theta_bar) M_x^p M_t^m
          {a_*[L+Delta^(-1)(1+e_loc)]
                    +a_*^2 rho^(-1)(1+e_loc)^2}.       (14)

The derivatives of kappa^(-1), of a, of the transported cutoff, and of
the pressure (8) are all included. For mixed derivatives the fixed bump
norms through p+m+3 suffice after increasing their finite order if needed.
This is an Eulerian derivative estimate, not merely a material one.

If a force of compact time support is wanted for this single finite
example, first remove W, then multiply H by a smooth host cutoff beta.
Choose pressure beta^2 P_H. Its exact force is

    beta' H+beta^2(H.grad H+grad P_H)-nu beta Delta H.  (15)

For a host ramp of duration Delta_H this adds the explicit mixed bound

    C_(p,m) R^(-p) Delta_H^(-m)
       [lambda R/Delta_H+lambda^2 R+nu lambda/R].      (16)

The initial host can likewise be activated with a disjoint smooth ramp.
There are no joins with incompatible time derivatives. Thus the finite
construction can start and end at rest and have smooth periodic pressure
and smooth compact-time forcing. It is then a globally smooth forced
example, not a breakdown example. The purpose of the ramps is to display
the complete finite insertion/return cost, not to claim a free reset.

## 5. A nonempty finite gain margin, and what its smallness means

Fix Theta=1 and r sufficiently small relative to R that the support and
the chosen finite ramps fit. Choose K large enough that K r exceeds all
fixed localization constants, and set lambda=nu K^2. All parameters are
finite. Then the exact plateau velocity gain in (5) is greater than 12,
and e_loc is small. Its peak amplitude is a_* comparable to its outgoing
amplitude a_out, with fixed window-dependent constants.

For any prescribed finite maximum mixed order P and increment budget
epsilon_f>0, write C_P for the maximum of the finite constants in (14),
and take

    Q_P=max(1,M_x,M_t)^P,
    L_join=L+Delta^(-1)(1+e_loc).

The nonempty choice

    0<a_* <= min{epsilon_f/[2C_P Q_P L_join],
          sqrt(epsilon_f rho/[2C_P Q_P(1+e_loc)^2])}   (17)

gives every mixed derivative of delta f through total order P bounded by
epsilon_f, while preserving the same velocity **ratio** G. The full
force budget must add (2) and, if used, (16). In particular this is a small
increment on an explicitly paid-for older state. It is not a claim that
the complete force can be made arbitrarily small at fixed large host
strain, or that a fixed positive outgoing velocity survives epsilon_f
tending to zero.

No derivative order is allowed to change secretly after these choices.
For each finite P the construction is explicit; these independent finite
choices do not supply one common infinite-order, infinite-stage schedule.

## 6. An actual pressure-independent obstruction in the cutoff strip

The upper bound (14) alone cannot prove that a force cost is necessary.
Here a genuine lower bound is available for the explicit velocity (6).
Choose the fixed factor psi in chi_0 to be linear with slope c_psi!=0
on one fixed transition subinterval I. Let psi_2,psi_3 be constant one
on sufficiently large central subintervals. In the resulting open strip,

    chi_1=c_psi/r1(t), all chi_ij=0,
    W1=W2=0, W3=a chi sin(phi)-(a/kappa)chi_1 cos(phi),
    partial_3 W=0, W.grad W=0, pi_W=0.

The complete NS residual there is consequently **exactly**

    f-f_H= -2nu a kappa [c_psi/r1(t)] cos(phi)e3.       (18)

The strip is inside the host core, so f_H=0 there. This is an ordinary
viscous envelope term. The affine stretching, all pressure terms and all
self-advection have already been accounted for in obtaining (18).

Assume kappa r1|I| is sufficiently large to contain two x1 values at
phases 0 and pi inside the linear strip. Choose a rectangular loop between
these values, at fixed x2=0, with x3 height h3 comparable to r3 in the
flat plateau. Its horizontal width is pi/kappa. The two vertical force
values have equal magnitude and opposite sign. Therefore

    |integral_loop f.dx|=4nu a kappa |c_psi| h3/r1,
    length(loop)=2h3+2pi/kappa.

If kappa h3>=pi, the actual norm obeys

    ||f(t)||infinity >= nu a(t) kappa(t)|c_psi|/r1(t). (19)

Any alternative smooth periodic pressure changes f by a gradient, whose
integral around this contractible loop is zero. Thus (19) holds for
**every pressure choice** for this particular complete velocity. It is
not a divergent upper bound or a claim based on a raw unprojected force.

The bound is present during the gain interval when alpha=1; neither
activation nor reset is used to derive it. It also yields actual
derivative lower bounds: in the strip curl f has an oscillatory component
of size 2nu a kappa^2 |c_psi|/r1. Spatial differentiation multiplies its
oscillation by further powers of kappa. In particular all-orders force
admissibility cannot be inferred by merely changing the pressure.

On one fixed torus the support widths are bounded above by a fixed
geometric constant. The localization condition kappa r3>=c>0 bounds
kappa below by another fixed positive constant. Hence (19) implies

    ||f(t)||infinity >= c_(geometry,psi) nu a(t).       (20)

An accumulating sequence of **these unchanged compact transported-wave
stages**, observed on their alpha=1 gain intervals and with the stated
strip surviving in the complete velocity, cannot have a_out tend to
infinity while its complete force stays bounded through a finite terminal
time. This remains an exclusion of a specified genuinely 3D architecture,
not of arbitrary nonsymmetric NS dynamics.

Additional older fields or full profile corrections may change the
velocity and its momentum residual in this strip. If so, (18) no longer
applies and their complete effects must be derived; they cannot be
dismissed as mere pressure changes. The lower bound does not rule out
such a redesigned construction.

## 7. What this stage settles and what must change next

This example leaves full fixed-axis annular symmetry in a precise way,
retains positive ordinary viscosity, realizes a finite interior velocity
gain, and gives a complete periodic pressure and mixed-force estimate
including finite insertion and return. The finite margin (17) is real,
but its absolute output shrinks with the allowed increment budget.

Two independent physical costs prevent promoting it directly to a
breakdown construction: the complete held affine host pays (3), and its
unchanged transported compact wave pays the circulation lower bound (19).
The [stability audit](symmetry-breaking-audit.md) also applies
to this smooth finite reference; nonzero three-dimensional dependence is
not by itself a singularity mechanism.

The next useful forced calculation must alter an actual load-bearing
piece: evolve the older host with a controlled complete force rather than
hold an ever-stronger compact affine field, and derive genuine velocity
corrections that cancel the transverse viscous cutoff residual while
retaining gain. A finite-depth correction result could address the second
cost; it would not automatically eliminate the first. Neither alteration
is assumed proved here.

## Exact calculation boundary

Symbolic checks verified the three components of (9) on transported
polynomial cutoff jets, including all mixed derivatives that occur, the
solenoidal curl identity, and the exact affine-host vector potential.
Omitting pressure (8) fails the residual check. A separate exact
linear-strip check included W.grad W and reproduced (18). These controls
are algebra checks. The cutoff support, derivative bounds and circulation
argument are the written proofs above, not numerical flow evidence.
