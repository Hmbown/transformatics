# Actual first-stage seed cost: exact reduction and the remaining matching problem

**Current application:** the [original-time nonlinear theorem](../navier-stokes/original-nonlinear-handover.md) now combines this note with the completed matching and whole-envelope estimates. Its full finite supplied-seed assembly passed a separate agent review. Historical conditional and unfinished-matching statements below retain their local derivation scope; they do not describe the current finite theorem. Infinite compatibility and ROOT remain open.

8 September 2026. Independent bounded calculation by packet_estimate_review,
with the thin inner equation and its positivity argument cross-checked against
the independent root calculation. No DNS. This research appendix remains outside the registered proof graph.
ROOT and (E') remain OPEN.

This note establishes exact transfer and optimization identities and reduces
the actual-NS central cost to a particular Euler-compatible matrix model.
It also proves positivity of the limiting inner connection. It does **not**
claim that these facts alone establish the proposed powers of ell for the
full polarization transfer. The required weighted matching is identified
explicitly below.

**Later matching checkpoint, 8 September:** the [full outer estimate](outer-matching.md) and [uniform inner connection](inner-matching.md) now supply the selected central branch and its complete history. Both passed separate agent reviews recorded [here](matching-review.md). Statements below identifying weighted matching as unfinished describe this reduction in isolation; they are superseded by those appendices. The choice of an unscaled fixed profile in section 1 is essential.

## 1. Setting and the cost which must actually be calculated

Use one fixed sufficiently thin Gavrilov profile from
[the oblique-carrier proof](../navier-stokes/gavrilov-oblique.md), and the actual first-stage NS
solution q from [the log-log theorem](../navier-stokes/loglog-handover.md). Set

    h=L^(-1/10), epsilon=nu h^4, ell=sqrt(log(1/h)),
    T=(2/mu)log ell, t*=T-ell^(-3/4),
    k=h^(3/2), d=h^(5/4), a2=k ell^(7/8).

The profile, its positive Floquet exponent mu, and nu are fixed before
h tends to zero. Specifically choose the unscaled geometric V=V_j with
f_j(P_j)=1 from the oblique-carrier theorem. The thin-limit constants
below use that normalization. The older background note's separate L2
normalization is not imposed here; its comparison proof applies to this
fixed V with profile-dependent constants. The log-log theorem allows
this choice, and q denotes the corresponding first-stage solution.
Let Y be the actual q-particle starting at the first
packet's center. At t*, let p,n be its primary polarization and covector
unit directions, r=n cross p, and Q=(p,r,n). The proposed pure receiver is

    xi*=4r, b*=n.

Along Y, put A_q=grad q and let J_q be the particle deformation. The unique
initial covector reaching xi* is xi0=J_q(t*,0)^T xi*. The full
pressure-corrected polarization transfer M_h is defined by

    xi'=-A_q^T xi,
    b'=-A_q b+2xi(xi.A_q b)/|xi|^2,  xi.b=0.

It maps the initial orthogonal plane to the final orthogonal plane. With
continuously oriented orthonormal bases, its exact determinant is

    det M_h=|xi0|/|xi*|=:r_h.                           (1)

This follows either from the three-dimensional determinant and normal
quotient or directly by tracing the tangent generator. In particular the
initial/final leading-strain cost for b*=n is

    C_h=r_h |M_h^(-1)n|=|M_h^*p|.                      (2)

The second equality is the two-dimensional adjugate identity, since
r cross n=p. It is an adjoint row norm, not merely an inverse condition
number. The forward viscous realization in
[the original-time linear preparation](original-seed-compatibility-draft.md) has initial C1 size
comparable to ell^(7/8) C_h.

If a scalar factor eta_h is allowed, small original strain and the
previous pure-receiver late strain dominating the host ell require

    eta_h ell^(7/8) C_h ->0,
    eta_h ell^(1/8) ->infinity.

Such scalars exist exactly when C_h=o(ell^(-3/4)). This is a necessary
and sufficient scalar endpoint condition for this specified pure
receiver, not a nonlinear feedback theorem.

## 2. A reference matrix which retains the primary wave

On the central reference V-particle X(t), write

    A0(t)=grad V(X(t)), F(t,s)=D Phi_V(t,s),
    N'=-A0^T N,
    beta'=-A0 beta+2N(N.A0 beta)/|N|^2,
    alpha=N cross beta,
    Gamma=omega_V.N.

Here N returns periodically, beta is the chosen real expanding Floquet
solution, and Gamma is a nonzero constant. The selected thin family has
Gamma -> -1/2 under the normalization used below. The exact cross-product
identity is

    alpha'=A0 alpha+Gamma beta.                        (3)

The central leading first-stage gradient is therefore the matrix

    Abar(t)=A0(t)-ell^(-1) beta(t) tensor N(t).          (4)

It is essential to retain the second term: its integral has size ell,
despite the small velocity difference q-V.

The model also retains an Euler vorticity identity. Define

    omegabar=omega_V-ell^(-1) alpha.

Then, exactly,

    omegabar'=Abar omegabar.                            (5)

Indeed N.alpha=0 and N.omega_V=Gamma, so (3) gives (5) immediately.
Consequently omegabar.xi is constant for every model cotangent solution.
This does not solve the polarization equation, but it distinguishes (4)
from an arbitrary prescribed trace-free matrix history.

## 3. Exact deformation, without an exponential ell loss

Let F(t)=F(t,0), N0=N(0), and

    kappa(t)=ell^(-1) integral_0^t F(s)^(-1) beta(s) ds.

Since N(t)=F(t)^(-T)N0 and N.beta=0, all interaction generators have
the same right factor N0 and their products vanish. Thus the exact model
deformation is

    Jbar(t,0)=F(t)[I-kappa(t) tensor N0],
    N0.kappa(t)=0.                                    (6)

Integrating (3) after multiplying by F^(-1) gives the useful endpoint
identity

    kappa(t)=[F(t)^(-1)alpha(t)-alpha(0)]/(ell Gamma).   (7)

The inverse of the bracket in (6) is I+kappa tensor N0. No time-ordered
exponential remains in this deformation calculation.

For the reference terminal receiver xi*=4alpha(t*)/|alpha(t*)|,

    xibar0=F(t*)^T xi*
       - N0 [alpha(t*)-F(t*)alpha(0)].xi*/(ell Gamma)
       =-4|alpha(t*)|N0/(ell Gamma)+O(1+t*).            (8)

The reference deformation is at most linear in time on the fixed
action annulus. Since |alpha(t*)| is comparable to ell^2, (8) proves

    |xibar0|/|xi*| is comparable to ell.                (9)

The original direction approaches the primary direction, with the sign
specified by -Gamma, at angle O(log ell/ell). This is a logarithmic
angle, so it is not excluded by the earlier obstruction for an initial
cone of width h^beta, beta>0.

There is an exact backward formula at every intermediate time:

    xibar(t)=C(t)-f(t)N(t),  C(t)=F(t*,t)^T xi*,
    f(t)=[alpha(t*)-F(t*,t)alpha(t)].xi*/(ell Gamma),
    f'(t)=-ell^(-1) beta(t).C(t),  f(t*)=0.            (10)

Since beta(t*).xi*=0, f'(t*)=0. If u=t*-t, Taylor expansion gives

    f(t)=ell^(-1)u^2 xi*.A0(t*)beta(t*)
             +O(ell^(-1)e^(mu t*)u^3).                (11)

Thus the transition of the covector near the endpoint occurs on a
square-root scale. A linear terminal-zero approximation would be wrong.

## 4. Uniform actual-profile geometry and the thin formula

The action-angle construction gives more than a generic linear-in-time
bound. Use the canonical moving orthonormal frame E=(n_rad,t_pol,a_ax),
and put

    C_j(t)=E(t)^T [r_j Phi_I, Phi_sigma/r_j, Phi_beta].

The analytic coordinate expansion gives C_j=I+O(r_j), uniformly in
the angles. In these scaled coordinates the exact action shear is

    D_j=[[0,0,0],[r_j^2 Omega1',0,0],[r_j Omega2',0,0]],
    D_j^2=0,
    F_E(t*,t)=C_j(t*)[I+u D_j]C_j(t)^(-1).             (12)

Here F_E=E(t*)^T F(t*,t)E(t). The two nonzero entries tend to -2 and
-c, respectively, with c=1/sqrt(2). Hence both F_E and its inverse
are bounded by C(1+u), uniformly over all sufficiently large j and all
u>=0. Equation (12) does not accumulate an O(r_j) coefficient error
over the growing time interval.

In the thin limit the exact relative-frame matrices and primary vectors
are

    A0=[[0,-1,0],[-1,0,0],[-c,0,0]],
    O0=[[0,-1,0],[1,0,0],[0,0,0]],
    D0=A0-O0,
    mu=2/3, N=k0=(0,-c,2),
    beta(t)=e^(mu t) beta0, beta0=(1,1/3,c/6),
    alpha0=k0 cross beta0=(-3/4,2,c),
    |alpha0|=9/4, |k0|=3c, |beta0|=3c/2, Gamma=-1/2.

Let r0=alpha0/|alpha0| and use a unit terminal receiver xi*=r0;
constant rescaling of xi does not affect the polarization equation or
the strain ratio. With sT=e^(mu t*)/ell and st=sT e^(-mu u), (10) becomes

    xibar(t)=r0-2u e1
          +(9/2)[sT-st(1+mu u)]k0,                    (13)
    f(t)=-sT g(u),
    g(u)=(9/2)[1-(1+mu u)e^(-mu u)]
         =u^2+O(u^3),  g'(u)=2u e^(-mu u).

In particular g is positive for every u>0.

For actual sufficiently thin fixed profiles, the two-dimensional
relative Floquet coefficients are O(r_j) perturbations of a constant
hyperbolic matrix on a fixed 2pi interval in the poloidal angle. Its simple expanding
eigenvector and exponent therefore give, in the E frame, a periodic
Floquet factor beta_per,j=beta0+O(r_j), after the stated normalization;
the analogous assertion holds for alpha and N. Combining this with
(12), the normalized f in (10) is uniformly close to the expression
in (13). Near u=0 the error has an additional u^2 factor, because both
f and f' vanish exactly and the fixed time derivatives of the
coefficients converge. For u bounded away from zero, convergence is
uniform; the tail is controlled by (1+u)e^(-mu u), uniformly for mu
near 2/3. Consequently, for sufficiently large fixed j,

    c ell min(u^2,1)<=|f(t)|<=C ell min(u^2,1),         (14)

uniformly for 0<=t<=t*. Its sign is the sign of the thin expression.
For u sufficiently small, C(t) remains uniformly transverse to N(t).
For larger u, the fN term dominates the O(1+u) vector C. It follows
that, for sufficiently small h,

    |xibar(t)| is comparable to 1+ell min(u^2,1).        (15)

These are deformation and covector statements. They do not give the
polarization transfer norms.

## 5. The actual-q cost differs from the model cost by a relative o(1)

The first-stage proof and its material-particle phase check imply

    ||q-U_app||_infinity<=h^(9/8-o(1)),
    ||grad(q-U_app)||_infinity<=h^(1/24-o(1)),
    phi(Y(t),t)-pi/2=h^(1/8-o(1)).

Pulling Y back by the fixed V flow moves the initial point by
h poly(ell). The normalized primary directions at Y therefore differ
from the reference directions by a positive power of h times a fixed
power of ell. The bump remains near chi(0)=1. The slow gradients and
the mean/harmonic gradients are h^(1/2)poly(ell) or smaller. Thus

    sup_[0,t*] |A_q(t,Y(t))-Abar(t)|
                              <=h^(1/24-o(1)).         (16)

The actual and reference terminal receiving frames also differ by a
positive power of h. Both gradients have integrated norm at most C ell.

To compare their backward rays, first evolve the unit direction on
the compact sphere, then evolve log|xi|. The direction vector field
has Lipschitz constant C|A|. This yields an error h^(1/24)exp(C ell)
after enlarging C. It does not insert a small |xi| denominator into a
second exponential. Comparing the full amplitude generators and their
forward fundamental matrices gives the same type of error. Initial
planes are identified by the small orthogonal rotation between their
unit normals. The adjoint row formula (2) then gives

    |C_h-Cbar_h|<=h^(1/24)exp(C ell).                   (17)

The generic norm/inverse-norm bounds give Cbar_h>=exp(-C ell). Since
ell=sqrt(log(1/h)), (17) therefore proves

    C_h/Cbar_h ->1.                                   (18)

The same comparison transfers (9) and (15) to the actual covector.
In particular its principal viscous exponent has the improved bound

    (epsilon/k^2) integral_0^t* |xi(t)|^2 dt
                           <=C_nu h ell^2 log ell=o(1).

This scalar attenuation estimate is not a substitute for the full
finite-wave residual. The forward linearized preparation note retains
all envelope/curl Laplacians and Leray pressure. Equations (16)-(18)
show that a sharp result for the **fixed actual profile's** model (4)
will transfer to q. They do not turn the straight-column limit into
such a result.

## 6. The outer growing branch and the inner connection

In the outer region |f|>>|C|, transversality in (10) is

    N.b=C.b/f.

Using the small normal lift from N-perpendicular to xibar-perpendicular,
the leading outer tangent equation is

    v'=G_N(A0)v+[1/(ell f)] beta(C.v),
    G_N(A0)=-A0+2N tensor N A0/|N|^2.                  (19)

Its growing solution has the exact expression

    v_outer(t)=[f(0)/f(t)] beta(t),                    (20)

up to the chosen normalization of beta(0). Indeed (10) gives
-f'/f=beta.C/(ell f), so differentiating (20) verifies (19).
Equation (20) is exact for the **reduced outer equation** (19), not
for the full finite-ell pressure-corrected polarization equation.
That distinction is load-bearing.

Since f(0) is comparable to ell and f(t) to ell u^2 near the endpoint,
(20) suggests a p component ell^2/u^2. At u comparable to ell^(-1/2)
this is ell^3. Transversality suggests a normal component ell^(5/2).
These observations identify the weighted powers that a proof must use.

The limiting inner equation can be calculated independently from the
full three-component thin system, including the moving frame and
pressure. Put Q=(p0,r0,n0), Lambda=(9/4)sT, z=sqrt(Lambda)u, and
b_const=2sqrt(2)/3. Then

    (xibar)_Q=(-4sqrt(2)z/[3sqrt(Lambda)],
                   1+O(Lambda^(-1/2)), b_const z^2)+o(1)

on each fixed z interval. Write the amplitude components as
b_p=sqrt(Lambda)V and b_n=W. Transversality eliminates b_r. The limiting
system is

    V_z=-W,
    W_z=[(2b_const^2 z^2-2b_const/3)V
                     -4b_const^2 z^3 W]/P,
    P=1+b_const^2 z^4.                                (21)

Equivalently,

    (P V')'+(2b_const^2 z^2-2b_const/3)V=0.             (22)

An independent intrinsic-plane derivation with z_old=sqrt(ell)u
gives (P_old Y')'+(9z_old^2-sqrt(2))Y=0,
P_old=1+(9/2)z_old^4. Since z=(3/2+o(1))z_old, the equations agree.

The branch selected by (20) should have V proportional to z^(-2) as
z tends to infinity. The relevant connection of (22) is rigorously
nonzero. Let g=P^(-1/2), and write V=g y. Direct differentiation gives

    Lg=-[4b_const^2 z^2+(2b_const/3)P]/P^(3/2)<0,
    y''=q_inner(z)y,
    q_inner=[4b_const^2 z^2+(2b_const/3)P]/P^2>0.

Normalize y(infinity)=1 and y'(infinity)=0. The solution is the positive
Volterra series for

    y(z)=1+integral_z^infinity (s-z)q_inner(s)y(s) ds.    (23)

Its n-th iterate is bounded by M(z)^n/n!, where
M(z)=integral_z^infinity s q_inner(s)ds and

    M(0)=1+pi/6.

The series therefore converges, with 1<=y<=exp(1+pi/6). Moreover
y'(0)=-integral_0^infinity q_inner(s)y(s)ds<0. Since g(0)=1 and
g'(0)=0,

    V(0)>0, W(0)=-V'(0)>0.                            (24)

This proves the two nonzero connection coefficients for the limiting
inner boundary-value problem. It does not by itself prove that the
finite-ell solution enters that problem with the proposed nonzero
outer coefficient.

## 7. Pure and optimized terminal polarizations have different costs

There is an exact optimization available before any asymptotic claim.
If only the terminal normal component n.b*=1 is specified, the least
initial polarization norm is 1/|M_h^*n|. It is attained by

    b0_opt=M_h^*n/|M_h^*n|^2.

Thus the least initial leading-strain cost for that terminal normal
component is

    C_opt=r_h/|M_h^*n|,                               (25)

and its additional p component is exactly

    p.b*_opt=(M_h^*p).(M_h^*n)/|M_h^*n|^2.             (26)

This follows directly from Cauchy-Schwarz and its equality case. It
shows why a large pure-target inverse cost is not a universal
preparation obstruction.

For orientation only, if the proposed weighted matching establishes
the thin-model row powers

    |M^*p| comparable to ell^3,
    |M^*n| comparable to ell^(5/2),

with aligned leading rows and a nonzero common incoming functional,
then (2), (9), and (25)-(26) would give

    C_pure comparable to ell^3,
    C_opt comparable to ell^(-3/2),
    p.b*_opt comparable to ell^(1/2).

For the proposed terminal normal strain ell^(7/8), the optimized
original strain would be ell^(-5/8), while its terminal p strain
would be ell^(11/8). This is a conditional consequence of the row
asymptotics, not an established actual-q power law.

The outer profile also predicts a usable history bound. For the
optimized normalization its scalar amplitude multiplier is
ell^(7/8-5/2)=ell^(-13/8). In the outer near-terminal region the
covector ell u^2 cancels the amplitude factor ell^2/u^2, giving strain
ell^(11/8). Further back, an e^(-mu u) factor is integrable. The inner
scale gives the same order. If the necessary weighted upper bounds
hold, both the maximal strain and its time integral are therefore
O(ell^(11/8)), with fixed constants or harmless logarithmic factors.
An energy factor exp(C ell^(11/8)) is still h^(-o(1)), since
ell^2=log(1/h). This is the reason to investigate the mixed receiver.

There is a separate interpretation limit: its p strain already has
size ell^(11/8) at t*. The previously isolated terminal shear adds
only ell^(9/8) over [t*,T]. It would not yield a new ell^(1/4) relative
gain of the entire mixed packet. It could still provide an original-time
supplied-seed finite strain handover, subject to all missing matching
and nonlinear estimates.

## 8. Exact checkpoint and next decisive estimate

Established here: (1)-(18), the exact optimized cost (25)-(26), the
reduced outer solution identity (20), and the limiting inner positivity
(24). The last two statements explicitly concern their stated reduced
equations. The polynomial row powers and optimized history bound are
not established for the full model or actual q in this note.

The remaining analytic task is a weighted outer-to-inner matching for
the full pressure-corrected model, uniformly in terminal phase for one
fixed sufficiently thin actual profile. It must control the entire
two-dimensional propagator, not only one formal growing ansatz, and
prove that the incoming expanding row has a nonzero coefficient at
the inner boundary. It must also give weighted upper bounds over the
whole preceding interval for the optimized input. Ordinary unweighted
continuous dependence can lose exp(C ell) and cannot establish the
desired ell powers.

A possible overlap is u_m=ell^(-a), 1/4<a<1/3. The suggested error
balances ell^(-1+3a) and ell^(1/2-2a), both ell^(-1/10) at a=3/10,
require a proof of the corresponding weighted propagator bounds;
they are not estimates proved in this note. Equations (12)-(15)
remove the separate deformation-geometry obstacle, while (23)-(24)
provide the nonzero inner connection to which such a proof can match.

After that step, (18) transfers the fixed-profile result to actual q.
The existing forward viscous preparation can realize the chosen
linearized packet without any backward NS solve or late insertion.
A nonlinear original-time compatibility theorem would still have to
control its full earlier feedback and every generated harmonic. No
infinite composition, singularity, global regularity, or claim of
novelty follows from this checkpoint.


## 9. Reproduction and independent checks

The [exact limiting-model controls](checks/check-seed-turning.py)
check twelve identities, including the finite-parameter backward covector,
pressure-corrected inner reduction, positive Volterra transform and kernel
moment. They passed in the repository Python environment. A separate
seven-check symbolic derivation agreed. The written Volterra argument
establishes positivity for its limiting boundary-value problem; none of
these controls supplies the missing weighted matching.

The [conditional nonlinear budget](mixed-seed-nonlinear-budget.md)
states the exact history and envelope bounds to prove next. The scalar
cost criterion for the pure receiver must not be imposed on every mixed
receiver. Conversely, the optimized endpoint identity does not alone
control the earlier trajectory.

Source artifact: `nse-actual-seed-cost-20260908.md`; original SHA-256 `87b0436863f3e77e1730ae2caac979801c8579f7c21b73c5633251d8ed32b6b2`. References and archival status were updated for this copy.
