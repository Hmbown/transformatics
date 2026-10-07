# Viscous return attempt: exact normalization, spatial commutators, and the axis

8 September 2026. Bounded analytic attempt on the ordinary-viscosity forced
track. **No complete insertion/return stage is established here.** The new
results are an exact normalization of the two diffusion operators, a precise
spatial commutator, and a solved reduced-system example showing that identical
diffusion does not imply a complete return. Full velocity recovery and finite
physical derivative costs are stated in nonsingular Cartesian coordinates.
These calculations do not construct a singular NS solution or an all-order
force schedule. ROOT and FORCED-D remain OPEN. No DNS was run.

## 1. The apparent unequal drift can be removed exactly

Use the ordinary axisymmetric NS convention

    u = u_r e_r + u_phi e_phi + u_z e_z,
    omega_phi = partial_z u_r - partial_r u_z,
    Gamma = r u_phi, Xi = omega_phi/r,
    D = partial_t + u_r partial_r + u_z partial_z.

The previous note correctly gives

    D Gamma = nu L_Gamma Gamma + r f_phi,
    D Xi = nu L_Xi Xi + r^(-4) partial_z(Gamma^2)
                              + (curl f)_phi/r,
    L_Gamma = partial_z^2 + partial_r^2 - r^(-1)partial_r,
    L_Xi = partial_z^2 + partial_r^2 + 3r^(-1)partial_r.

However, their difference is not an invariant obstruction to a return. Put

    theta = Gamma/r^2 = u_phi/r,
    L = partial_z^2 + partial_r^2 + 3r^(-1)partial_r.

Direct product differentiation gives the exact conjugation

    L_Gamma(r^2 theta) = r^2 L theta.                       (1)

Since D(r^2)=2r u_r, the complete equations become

    D theta = nu L theta - 2(u_r/r)theta + f_phi/r,
    D Xi = nu L Xi + partial_z(theta^2) + (curl f)_phi/r.   (2)

Thus the **full scalar diffusion operator**, including its radial drift,
is common to both channels. The price is the explicit stretching term
`-2(u_r/r)theta` and the changed normalization of the circulation amplitude.
A central zero value of Xi is unaffected by this change of variables;
physical circulation and velocity gains must still be converted separately.

This is a classical reformulation, not a new Navier--Stokes identity claimed
as original to this project. [Hou--Lei--Li, equations (13)--(17), printed
p. 5](https://users.cms.caltech.edu/~hou/papers/NSE_anisotropic_revise1.pdf)
give these unforced variables, common operator, and streamfunction recovery
at viscosity one. Equation (2) follows directly with general fixed viscosity
and the displayed physical forcing. Their regularity theorem has its own
hypotheses; it is not being imported as unrestricted global regularity.

In volume coordinates y=(z,r^2/2), the same L is

    L = partial_1^2 + 2y2 partial_2^2 + 4partial_2.

The `4nu partial_2 Xi` term in the old coordinates has not been thrown away:
it is now present identically in both theta and Xi equations. Treating it
alone as an unavoidable differential damping of the two normalized channels
would therefore be misleading. Variable metric, spatially dependent
coupling, the nonlinear transport, and elliptic recovery remain.

## 2. The equal operator does not commute with a spatial return map

A useful exact calculation can be made before attempting the full nonlinear
system. On a smooth annular chart consider a vector equation

    D W = nu L W + B(t,y) W.                               (3)

Here D is a fixed supplied transport, L is the scalar operator just above,
and B is a smooth matrix. This is a reduced linear equation; the complete
linearization of (2) also contains the nonlocal velocity recovery and is not
asserted to have this local form.

Let M solve D M=B M with M(0,y)=I. Let H solve D H=nu L H, with the desired
vector incoming profile. Write a^{ij}=diag(1,2y2). Applying (3) to the
proposed common-heat evolution W_app=M H gives the exact residual

    (D-nu L-B)(M H)
       = -nu[(L M)H + 2 a^{ij}(partial_i M)(partial_j H)].  (4)

All terms in (4) are matrix-vector products. In particular, the drift part
of L contributes to LM, while the derivative cross term comes from its
second-order part. There is no missing first-order drift cross term.
The formula remains valid for time-dependent metric coefficients because
it is an instantaneous product rule.

Equivalently, where M is invertible, an exact solution W=M Z satisfies

    D Z = nu L Z
        + 2nu M^(-1) a^{ij}(partial_i M)(partial_j Z)
        + nu M^(-1)(L M)Z.                                (5)

The new terms are matrix-valued. They need not preserve the returning
one-dimensional subspace. A spatially constant M would eliminate them;
a material-center return alone does not.

For completeness, suppose the chart is a bounded smooth domain lying in
`y2>=c>0`, the true and approximate solutions have equal initial and
boundary data, and the coefficients are smooth. Set

    b(t)=sup_y ||sym B(t,y)||op,
    R(t)=sup_y |(D-nu L-B)W_app(t,y)|.

The scalar maximum principle applied to the Euclidean norm of the error
(or a positive regularization of it) gives

    ||W-W_app||(T)_infinity
      <= integral_0^T exp(integral_s^T b(t)dt) R(s)ds.     (6)

The transport and scalar diffusion satisfy the norm inequality; the matrix
contribution is bounded by b. Equal boundary data are essential to this
stated estimate. It is not a cutoff-free estimate for an embedded packet.

If `||LM||<=M2`, `sum ||a^{ij} partial_i M||<=M1`,
`||H||<=H0` and `||grad H||<=H1`, equation (4) yields the concrete bound

    R <= nu (M2 H0 + 2 M1 H1).                             (7)

For a phase with derivative scale N and fixed envelope scale, H1 typically
contains N H0. This is an actual `nu N` commutator cost before propagation,
not a proved `N^(-1)` correction gain. Shortening the flight and absorbing
heat can change the cost, but the same chosen flight must retain the
claimed amplification. No improvement with arbitrary correction depth J
follows from (4) alone.

## 3. Exact counterexample to a common-heat whole-envelope return

The following completely solved model shows why (4) matters. It is a
counterexample to a factorization inference, **not an NS counterexample**.
Use a one-dimensional periodic coordinate z, integer N>=2, and

    J = [[0,0],[1,0]], J^2=0,
    B(t,z)=g'(t) I + phi'(t) cos(z) J,
    g(0)=0, g(T)=G,

where phi is a nonnegative nonzero smooth bump supported inside (0,T).
Consider

    partial_t W=nu partial_z^2 W+B(t,z)W,
    W(0,z)=(cos(Nz),0).

For nu=0 the exact matrix propagator is

    M(t,z)=exp(g(t))[I+phi(t)cos(z)J].

Thus M(T,z)=exp(G)I at every point: the inviscid second channel returns
exactly to zero across the whole profile, with amplification exp(G) in the
first channel if G>0. This is stronger than a return only at one center.

For nu>0, remove exp(g(t)). The first component is exactly
`exp(-nu N^2 t)cos(Nz)`. The second component at T equals

    W2(T,z)=exp(G)[c_plus cos((N+1)z)+c_minus cos((N-1)z)],

    c_plus/minus = (1/2) integral_0^T phi'(s)
        exp(-nu[(N+/-1)^2(T-s)+N^2 s]) ds
      = -(nu/2)(+/-2N+1) integral_0^T phi(s)
        exp(-nu[(N+/-1)^2(T-s)+N^2 s]) ds.                 (8)

The second equality is integration by parts; phi vanishes at both ends.
Both integrals are strictly positive. Therefore c_plus<0 and c_minus>0,
and the second channel is not identically zero. Orthogonality of the two
cosines rules out cancellation of the complete returned profile.

The first component still has precisely the scalar heat attenuation
`exp(G-nu N^2 T)`. Equal diffusion of the two channels has not preserved
the return because multiplication by cos(z) mixes adjacent frequencies,
which then accumulate different heat histories. This identifies the
mechanism in elementary terms, rather than appealing to an unspecified
lower-order error. At a specially selected point the two terms could
cancel; equation (8) makes no universal assertion about every central
point. It definitively excludes the whole-envelope factorization.

## 4. Exact velocity recovery and full force without a singular coordinate

Write the azimuthal streamfunction as `psi_phi=r psi`. Then

    u_r=-r partial_z psi,
    u_z=2psi+r partial_r psi,
    Xi=-L psi.                                            (9)

With (9), equations (2) retain both nonlinear couplings:

    D theta=nu L theta+2theta partial_z psi+f_phi/r,
    D Xi=nu L Xi+partial_z(theta^2)+(curl f)_phi/r.          (10)

In particular, solving the common heat equation for both scalar fields
while freezing psi does not solve (10). The recovered meridional velocity
changes D, feeds back into theta, and is itself coupled to Xi by (9).
The complete increment equations make the missing feedback explicit. Write
`theta=theta0+alpha`, `Xi=Xi0+beta`, `psi=psi0+zeta`, where
`beta=-L zeta`, and let `w=(-r zeta_z, 2zeta+r zeta_r)` be the meridional
velocity increment. With `D0=partial_t+u0_r partial_r+u0_z partial_z`,
subtracting the older equations gives exactly

    (D0-nu L)alpha
       = -w.grad theta0 + 2alpha psi0_z + 2theta0 zeta_z
         -w.grad alpha + 2alpha zeta_z + delta f_phi/r,
    (D0-nu L)beta
       = -w.grad Xi0 + 2partial_z(theta0 alpha)
         -w.grad beta + partial_z(alpha^2)
         + (curl delta f)_phi/r.                           (10a)

The first line retains stretching of both the old and new circulation;
the second retains the old-vorticity transport and both source products.
Already the linear terms involve the recovered zeta, so a local matrix B
alone is not the exact linearization. A full stage must estimate those
terms and their physical force reconstruction on its actual support.

Prescribing an arbitrary compact Xi also does not prove compact recovery
of psi: an elliptic inverse generally has tails. A compact construction can
instead prescribe compact psi and retain the exact Xi=-Lpsi it generates,
or provide a separate compact recovery argument.

There is a useful Cartesian form which has no powers of 1/r. For smooth
axisymmetric functions theta(x1,x2,z) and psi(x1,x2,z), set

    u1=-x1 psi_z-x2 theta,
    u2=-x2 psi_z+x1 theta,
    u3=2psi+x1 psi_x1+x2 psi_x2.                            (11)

Direct differentiation gives div u=0, including on the axis. If theta and
psi are smooth functions of `(x1^2+x2^2,z)`, this is a smooth Cartesian
field. If they have compact support strictly inside one fundamental cube,
periodic extension gives a smooth solenoidal field on one fixed torus.
This is a local embedded axisymmetric construction, not a claim that the
flat torus possesses global cylindrical coordinates.

For any such smooth time-dependent pair and any chosen smooth periodic
pressure p, define the **complete vector** force by

    f=partial_t u+(u.grad)u-nu Delta u+grad p.              (12)

Then the full periodic NS equation is exact; no pressure or force component
is inferred merely from its curl. Choosing p=0 keeps f compact in the same
spatial set as u, and also satisfies periodic pressure compatibility. It
may be a poor small-force gauge. A chosen pressure cancellation must be
retained in (12) and estimated, rather than discarded from the norm.

For a specified finite older state, one example is psi_old=0 and
`theta_old=Omega chi(r^2,z)`, with a fixed smooth compact cutoff chi. It is
a time-independent divergence-free swirl on the same torus, with p_old=0
and exactly

    f_old=-(r theta_old^2)e_r-nu r(L theta_old)e_phi.

This is a smooth prescribed forced NS state, including its entire cutoff
region. It is not an unforced host, not a low-force host uniformly in its
parameters, and not by itself an amplifying/returning older history.
Superposing a compact pair in (11) adds all old/new interactions to (12).
Thus the older state can be specified concretely without pretending that
its full residual is small. What remains absent is a compatible return
with a quantitative gain/force margin on this or another specified host.

For reference, in cylindrical variables the full force corresponding to
(12) is

    f_r=D u_r-u_phi^2/r
             -nu(partial_r^2+r^(-1)partial_r+partial_z^2-r^(-2))u_r+p_r,
    f_z=D u_z-nu(partial_r^2+r^(-1)partial_r+partial_z^2)u_z+p_z,
    f_phi=r[D theta-nu L theta+2(u_r/r)theta].             (13)

The quotient terms in (13) are evaluated by the smooth Cartesian lift at
the axis. Equation (11), not separate division of noisy radial profiles,
is the convenient way to keep this compatibility exact.

## 5. Finite derivative costs when a construction reaches the axis

For a packet supported in a physical ball of radius rho centered on the
axis, let X=(x1,x2,z-z0)/rho and sigma=(t-t0)/tau. Take fixed smooth
axis-compatible profiles Theta(X,sigma), Psi(X,sigma), P(X,sigma), and set

    theta=(a/rho)Theta, psi=a Psi, p=a^2 P.

Equation (11) gives `u=a U(X,sigma)`. Its exact full force is

    f=(a/tau) U_sigma+(a^2/rho)[(U.grad_X)U+grad_X P]
                              -(nu a/rho^2)Delta_X U.     (14)

For each fixed spatial multiindex alpha and time order m,

    ||partial_x^alpha partial_t^m f||infinity
      <=rho^(-|alpha|)tau^(-m) [
          (a/tau)||partial_X^alpha partial_sigma^(m+1)U||infinity
        +(a^2/rho)||partial_X^alpha partial_sigma^m
                         ((U.grad_X)U+grad_X P)||infinity
        +(nu a/rho^2)||partial_X^alpha partial_sigma^m
                                             Delta_X U||infinity]. (15)

This is an exact finite-order upper bound with explicit profile norms.
If the profile includes a phase frequency N, those norms include its
powers of N; they are not constants uniform in N. Cutoffs and activation
ramps belong to the profiles in (15). For a nonzero older state V, replace
(14) by the incremental defect with `V.grad u+u.grad V`; differentiating
those products retains every old-state spatial and time jet.

Unlike repeated estimates with r^(-1) coefficients, (14)--(15) do not have
spurious coordinate singularities as rho tends to zero. They still have
real physical derivative and diffusion costs. Also, the velocity scale is
a, whereas theta has scale a/rho and Xi has scale a/rho^2. Growth of the
normalized scalar fields alone does not establish growing velocity.

Smooth axisymmetry requires theta and psi to be even smooth radial
profiles, equivalently smooth functions of r^2 locally. In particular
Gamma=r^2 theta, u_phi=r theta, and omega_phi=r Xi have the appropriate
vanishing at the axis. The radial part of L at r=0 is `4partial_r^2` on
these even profiles, not zero. Neglecting this contribution changes the
viscosity exactly where the new construction would have to work.

As a scale check, suppose an off-axis packet is centered at radius R,
has envelope rho<=c R, physical carrier K=N/rho, and a host gradient
bounded by a rate lambda. Suppose additionally that its actual central
covector stays uniformly nonzero, its chosen flight is tau=c0/lambda,
and its selected inviscid velocity gain is at most exp(C lambda tau).
Its damping necessarily satisfies

    D=nu integral |K xi(t)|^2 dt >= c1 nu N^2 tau/rho^2.

Define the strain-based local Reynolds number `Re=lambda rho^2/nu`.
Then a positive principal gain within these assumptions requires a
margin of the form `Re>c2 N^2`; a large output from a tiny activation
requires the stronger logarithmic margins already present in the force
budget. Merely sending R to zero provides no such margin. If, in addition,
this particular host family has `lambda<=C a_old/rho`, then
`Re<=C a_old rho/nu`, which tends to zero for bounded a_old and rho->0.
That last host inequality is an explicit extra assumption, not a bound on
all highly oscillatory NS fields with bounded velocity. Anisotropic
geometries and nonuniform covector histories must be charged by their
actual scales and full damping integral instead.

### A restricted swirl-dominated axis-approach obstruction

Suppose a full smooth axisymmetric velocity and force are supported in one
fixed bounded spatial region for `0<=t<T<infinity`, with radius at most
R_max and the usual smooth axis compatibility. The circulation equation
and scalar maximum principle give

    ||Gamma(t)||infinity
      <=||Gamma(0)||infinity+integral_0^t ||r f_phi(s)||infinity ds
      <=||Gamma(0)||infinity+R_max integral_0^T ||f(s)||infinity ds
      =: M_Gamma < infinity.                              (16)

This conclusion needs no annular separation from the axis. To justify it
without treating the singular-looking coefficient as harmless by assertion,
observe that Gamma=0 on the axis and outside the fixed support. Any strictly
positive spatial maximum or strictly negative spatial minimum is attained
at r>0, where the equation has its ordinary uniformly elliptic local
maximum-principle sign. Apply the argument to Gamma minus the integrated
source bound and to its negative, with the usual strict time barrier.
Smoothness and compact support permit passage to the endpoint supremum.
This proves (16) on every preterminal interval with one common bound.

Now add the following **geometric stage assumptions**, none of which is
claimed to follow for every axisymmetric flow:

- The jth packet is centered at radius R_j and has envelope
  `rho_j<=c R_j`, with phase K_j=N_j/rho_j.
- A host rate lambda_j>0 bounds the gradient relevant to its selected
  inviscid velocity propagator, and
  `lambda_j<=C_s M_Gamma/R_j^2`. This is the swirl-dominated, controlled
  fixed-shape hypothesis; it places an extra restriction on meridional
  strain as well as on derivatives of the swirl profile.
- The selected exponent satisfies `G_j<=C_g lambda_j tau_j`, the flight
  is `tau_j=c0/lambda_j`, and `|xi_j(t)|>=c_xi>0` throughout it, with
  c,c0,C_s,C_g,c_xi independent of j.

Then

    Re_j=lambda_j rho_j^2/nu<=C_s c^2 M_Gamma/nu,             (17)
    G_j-D_j<=tau_j[ C_g lambda_j
                              -c_xi^2 nu N_j^2/rho_j^2 ].  (18)

Consequently a positive exponential growth margin in this particular
principal amplifier requires

    N_j^2 < (C_g/c_xi^2) Re_j
           <=(C_g C_s c^2/c_xi^2) M_Gamma/nu.               (19)

The right side is fixed. Thus moving a swirl-dominated ring toward the
axis does not by itself permit the **dimensionless** wave number N_j to
grow without bound while retaining this gain margin. Its physical wave
number K_j can still grow as rho_j shrinks with bounded N_j; the statement
does not exclude that distinct limit or establish its force budget.

In particular, (16) does not bound arbitrary meridional strain by the
circulation. A concentrating meridional field, uncontrolled profile
shapes, an anisotropic geometry, or a covector whose norm changes outside
the assumed bounds requires a new calculation. Equations (17)--(19)
exclude only the specified dimensionless fixed-shape swirl-ring shortcut.
They are not a proof of full axisymmetric regularity or an obstruction to
all axis-approaching forced cascades.

## 6. What this attempt changes

The [released Euler theorem, Theorem 1.1, printed p. 2](https://cims.nyu.edu/~tristanb/euler.pdf)
uses a fixed solid torus with `0<R<r0/2`. Its section 13.2, printed p. 107,
explicitly puts the complete velocity, circulation and azimuthal vorticity
in that fixed region, with a neighborhood of the axis identically empty.
These source facts concern the released Euler construction. A fixed-annulus
ordinary-NS continuation obstruction is investigated separately; no such
new theorem is inferred merely from the source's support statement here.

The finite viscous stage does **not** need to treat the unequal radial
operators as a fundamental unmatched diffusion effect: (1)--(2) remove that
problem exactly. It does need to control spatial diffusion/coupling
commutators, and (8) proves that a shared heat operator alone cannot provide
that control. A viable axis-approaching variant must preserve the smooth
axis conditions, nonlocal meridional recovery, full vector force, and actual
velocity gain simultaneously. The Cartesian formulation supplies exact
starting identities and derivative budgets for that task. It does not
supply the missing gain/force parameter range or an infinite stage schedule.

The proposed complete finite stage remains unproved at a precise point:
no selected older NS history and incoming profile have yet been shown to
retain the required return and velocity gain after the terms in (4)--(5),
nonlinear feedback in (10), full recovery and cutoffs, while satisfying
(15) with a useful small complete force. Increasing a formal correction
index J without a proved remainder estimate does not discharge that gap.
