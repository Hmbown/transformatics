# A fixed axisymmetric annulus cannot contain a smooth-forced NS breakdown

8 September 2026. Restricted analytic exclusion of a proposed architecture;
ROOT and FORCED-D remain OPEN. This is a classical regularity argument applied
to the released Euler geometry, not a new global regularity theorem. The
derivation below includes smooth forcing and an embedded periodic chart.
Independent AI review by the force/gain audit agent passes the stated
whole-velocity/support claim. Two clarifications from that review are
incorporated below: the full force norm in the final H1 estimate, and zero
extension before applying the annular maximum principle. This is not an
external expert review or a formal PDE certificate.

## 1. The geometric condition that matters

Let a classical solution of ordinary NS with fixed viscosity nu>0 exist on
[0,T), T finite, on one fixed flat three-torus. Suppose its entire velocity
has support in a fixed compact set K inside one Euclidean coordinate chart.
Assume the chart contains complete circles about one fixed z-axis and

    K subset {r_* <= r <= R, |z| <= Z}, r_*>0.

The cylindrical components u_r,u_theta,u_z are independent of theta, and
the zero extension of u outside the chart is smooth and axisymmetric. The
data are smooth and the prescribed periodic force is smooth through T.
The pressure is periodic. These assumptions concern the **whole velocity**,
not just a core or the newest packet. One can equivalently work on R3 with
the same compact support and the usual finite-energy/pressure conditions.

**Claim.** Such a solution continues smoothly beyond T. Consequently an
infinite forced construction retaining all these conditions cannot prove
FORCED-D. Finite gain inside this geometry is not excluded.

The fixed support and axis are substantive. Different axes for successive
packets, a nonsymmetric older flow, noncompact velocity tails, or support
approaching r=0 are outside this particular theorem. Merely writing one
packet in cylindrical coordinates does not impose its hypotheses.

This conclusion is consistent with the classical fact that singularities
of axisymmetric suitable NS flows can occur only on the axis. For primary
context see [Seregin, *A Note on Local Regularity of Axisymmetric Solutions
to the Navier–Stokes Equations* (2022), section 2, step 1](https://link.springer.com/article/10.1007/s00021-022-00667-6).
We give a direct energy proof for our stronger support assumptions instead
of importing that local theorem with unstated forcing conditions.

## 2. Circulation stays bounded

Put v=u_r e_r+u_z e_z, Gamma=r u_theta, and Xi=omega_theta/r.
Let F0=sup_[0,T] ||f||infinity, F1=sup_[0,T] ||curl f||infinity,
and V=|K|. These are finite. The axisymmetric circulation equation is

    (partial_t+v.grad)Gamma
       =nu(partial_r^2-r^(-1)partial_r+partial_z^2)Gamma
          +r fbar_theta.                                      (1)

Here fbar_theta is the angular average of the cylindrical force component.
This formula does not require the given pressure to be axisymmetric: its
theta derivative averages to zero on each complete circle in the chart.
All remaining terms already have no theta dependence. Where u is zero
in an open set, the original equation gives f=grad p, so this averaged
swirl forcing is zero there. Thus its support is in K and
||r fbar_theta||infinity<=R F0.

Apply the scalar parabolic maximum principle on a fixed larger annular
cylinder, where Gamma is identically zero near its boundary. To do this,
one may first extend Gamma, v and their already compact
averaged source by zero out of the chart; no torus-wide rotation symmetry
is being assumed. On every closed preterminal interval the drift is smooth,
and the resulting bound
does not depend on its size. For 0<=t<T,

    ||Gamma(t)||infinity <= M := ||Gamma(0)||infinity+R T F0,
    ||u_theta(t)||infinity <= M/r_*.                           (2)

The coefficient 1/r is harmless on this fixed annulus. This step is where
uniform distance from the axis begins to enter the quantitative bound.

## 3. Weighted meridional vorticity has a dissipative energy estimate

The exact second equation is

    (partial_t+v.grad)Xi
       =nu(partial_r^2+3r^(-1)partial_r+partial_z^2)Xi
          +partial_z(Gamma^2/r^4)+g,
    g=(curl f)_theta/r.                                       (3)

Its forcing can also be angular averaged. In fact curl f equals the curl
of the NS velocity residual, which is axisymmetric under the hypotheses.
It vanishes outside K. Hence ||g||2<=V^(1/2) F1/r_*.
Every norm and integral below uses the ordinary three-dimensional measure
dx=2pi r dr dz, not the unweighted meridional measure.

Set Y=||Xi||2^2 and W=||grad Xi||2^2. The velocity v is solenoidal in
three dimensions, so transport drops out of the pairing with Xi. The
extra radial diffusion has zero pairing:

    integral Xi (2/r) partial_r Xi dx
       =2pi integral partial_r(Xi^2) dr dz=0.

The boundary values vanish because the support avoids the axis and the
outer boundary. Integrating the swirl source in z gives exactly

    (1/2)Y' + nu W
      = - integral partial_z Xi (Gamma^2/r^4) dx
          + integral Xi g dx.                                (4)

By (2), ||Gamma^2/r^4||2^2<=V M^4/r_*^8. Young's inequality yields

    Y' + nu W <= Y+B,
    B=V M^4/(nu r_*^8)+V F1^2/r_*^2.                          (5)

In particular, with Y_*=exp(T)(Y(0)+BT),

    sup_[0,T) Y <= Y_*,
    integral_0^T W dt <= [Y(0)+T Y_*+BT]/nu.                  (6)

No assumed bound on the meridional velocity or on its accumulated strain
was used to obtain these estimates.

## 4. Recover velocity before using a continuation criterion

The ordinary energy inequality gives

    sup ||u(t)||2^2 <= E_* := (||u(0)||2+T V^(1/2)F0)^2.      (7)

The meridional field v is a smooth, compactly supported solenoidal vector
field in the chart, and therefore a periodic solenoidal field on the torus.
Its curl is

    curl v=omega_theta e_theta=Xi(-x2,x1,0).

The full Cartesian derivative, including differentiation of e_theta, must
be retained. Direct integration gives the useful exact identity

    ||grad curl v||2^2 = integral r^2 |grad Xi|^2 dx.          (8)

For clarity, before integrating in r the difference of the two radial
integrands is partial_r(r^2 Xi^2); its boundary values vanish. Dropping
the derivative of e_theta would give an incorrect expression.
The periodic Fourier div-curl identity and (8) imply

    ||D^2 v||2^2=||grad curl v||2^2 <= R^2 W.                 (9)

The fixed-domain H2-to-Linfinity embedding consequently gives

    integral_0^T ||v||infinity^2 dt
       <=C_domain [T E_*+R^2 integral_0^T W dt].             (10)

Combining (2), (6) and (10) proves the finite quantitative bound

    integral_0^T ||u||infinity^2 dt
      <=2C_domain {T E_*+(R^2/nu)[Y(0)+T Y_*+BT]}
            +2T M^2/r_*^2 < infinity.                       (11)

The same H2 embedding with its L2 term holds on R3. We have recovered the
full velocity norm needed for continuation; a bound on Xi alone was not
silently treated as such a criterion.

Finally, pairing the full NS equation with -Delta u gives, for X=||grad u||2^2,

    X' + nu ||Delta u||2^2
      <= (2/nu)||u||infinity^2 X+(2/nu)||f||2^2.             (12)

Gronwall, (11), and the smooth force bound give a uniform H1 bound. The
force norm in (12) is the full-domain norm, bounded on the torus by
|T3|^(1/2) F0; the smaller volume V in (7) was allowed only because the
energy pairing there is supported on K. On R3 the force is assumed to have
the usual finite L2 bound, as supplied by the Clay spatial decay condition.
The usual strong H1 continuation theorem with the prescribed smooth force
then extends u beyond T. Smooth initial data and smooth forcing propagate
higher regularity on that extension. This proves the restricted claim.

## 5. Apply the test to the actual released construction

The current [Alpöge–Buckmaster Euler manuscript](https://cims.nyu.edu/~tristanb/euler.pdf),
Theorem 1.1 on printed p. 2, chooses a toroidal region around a meridional
center (z0,r0), of radius R0 with 0<R0<r0/2. Section 13.2 on p. 107
explicitly places the complete velocity, circulation and meridional
vorticity in that fixed region and away from the axis. The inspected
PDF has SHA-256
`97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8`.

These geometry facts mean that the following proposed modification is
excluded: retain a fixed-axis annular velocity with the same compact
support, absorb heat into the wave profiles, and try to obtain NS
breakdown with a smooth complete force. The proof above does not require
retaining the Euler velocity amplitudes, its bounded-velocity conclusion,
its profile, or its specific recursion. Even a different amplitude
schedule in that same global geometry is regular under these hypotheses.

This is stronger than the earlier failure of f_NS=f_E-nu Delta u, which
only excluded reusing the exact Euler velocity. It is not an objection to
the Euler theorem: the proof uses positive viscosity in (5), (6) and (12).

## 6. Consequence for the next construction

A finite annular viscous stage can still be useful for calculating return
maps. It cannot be the sole geometry of an infinite singular construction.
Before spending effort on arbitrary correction depth, choose and quantify
how the proposed full flow leaves this excluded class:

- A stage sequence may approach the axis. Then r_* is not fixed, and the
  factors r_*^(-8), r_*^(-2), cylindrical regularity, force recovery and
  the actual diffusion clock must all be reanalysed together.
- The full velocity may break axisymmetry. Then the two scalar equations
  above no longer close; every new angular interaction and pressure term
  belongs to the stage estimate.
- A local axisymmetric core may live in a more general older flow. Then
  that older flow and its nonlocal recovery cannot be discarded from the
  proof or from the force budget.

These are open alternatives, not constructions established here. A
time-dependent coordinate change does not by itself supply one: the
physical equation and its new transport/force terms must be derived.

## 7. Exact controls and review scope

[The exact-control script](checks/check-annular-geometry.py)
verifies the weighted diffusion flux identity, the full Cartesian
vorticity-gradient identity with a negative control omitting the angular
basis derivative, and the complete radial-operator conjugation used by the
companion stage analysis. These are algebra checks. Maximum principles,
Sobolev embedding and strong continuation are the analytic inputs to this
written proof; the script is not a substitute for them.
