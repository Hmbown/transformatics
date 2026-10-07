# Original-time preparation of the receiving carrier: map, cost, and limits

**Research appendix — 8 September 2026.** **Review status:** an independent mathematical review accepted sections 4–7 at their forward viscous **linearized** scope, after repairing the initial-cost comparison in section 7. It checked whole-interval derivative estimates, phase preparation, forced pressure, the residual, semiclassical energy and viscous C1 tracking. The determinant/adjugate identity and endpoint interpretation also have a separate independent algebra check. The phase-class exclusion in section 3 was not newly reviewed. Section 8 reviews the separate late nonlinear draft; section 9 records the review of this preparation. Small original-time strain and nonlinear compatibility remain open.

These research appendices remain outside the registered proof graph; full formalization and ROOT / `(E′)` remain open. See the [next-transfer review index](../navier-stokes/next-transfer-review.md) for the common scope and remaining estimates.

The derivation follows, with local references relocated and the identified section 7 correction incorporated. Other original drafting-status sentences are historical. Original source artifact: `nse-original-seed-compatibility-20260908.md`; SHA-256 `e734a643b6a666a0f5c8c73627f2fbfb3a64dbcf10029f48da145a85f3a8e437`. This original hash does not describe the corrected file.

---

8 September 2026. Independent bounded derivation. No canonical files or
DNS were changed. ROOT and (E') remain open. This note distinguishes an
original-time **linearized** preparation from a compatible nonlinear
trajectory and from a claim of small initial C1 norm.

Use the actual first-stage NS solution q from the reviewed log-log note,
on T_L, with epsilon=nu h^4, ell=sqrt(log(1/h)), and

    T=T_h=(2/mu)log ell,  t*=T-ell^(-3/4),
    k=h^(3/2),  d=h^(5/4),  a2=k ell^(7/8).

The first Gavrilov profile and nu are fixed, and h is in the original
family h=L^(-1/10). All norms on the expanding torus are unnormalized.
At y*=Y(t*) use the receiving directions

    xi*=4 Q(t*)e2,  b*=Q(t*)e3,  Q=(p,n cross p,n).

## 1. Exact finite-dimensional transfer, including its inverse cost

Let Phi(t,s,a) be the actual q flow and J(t,s) its derivative along Y.
It has determinant one. The cotangent transfer is J(t,s)^(-T). To reach
xi* at t*, the unique initial central covector is therefore

    xi0=J(t*,0)^T xi*,
    xi(t)=J(t*,t)^T xi*.

Along that covector solve the full pressure-corrected amplitude equation

    b'=G(t,xi)b,
    G=-A+2 xi tensor xi A/|xi|^2,  A=grad q(t,Y(t)).

Write M(t,s) for its transfer from xi(s)-perpendicular to
xi(t)-perpendicular. Transversality is exactly preserved. The initial
polarization reaching b* is b0=M(t*,0)^(-1)b*.

For tangent b, the exact norm equation is

    (|b|^2)'=-2 b.S(q)b.

The covector satisfies (log|xi|)'=-n.S(q)n. Consequently if
J_S(s,t)=integral_s^t ||S(q)||_infinity, both the norm and inverse norm
of M(t,s) are at most exp(J_S), and the covector norm ratio lies between
exp(-J_S) and exp(J_S). The first-stage bound gives J_S(0,T)<=C ell.
These are finite ODE inverses, not backward solutions of viscous NS.

There is also an exact determinant, with continuously oriented
orthonormal bases on the two planes:

    det M(t,s)=|xi(s)|/|xi(t)|.                         (1)

Indeed trace G=2 n.A n=-2(log|xi|)'. The full three-dimensional transfer
has determinant (|xi(s)|/|xi(t)|)^2 and satisfies
xi(t)^T M_full=xi(s)^T. Its normal quotient therefore has factor
|xi(s)|/|xi(t)|, leaving (1) on the tangent plane.

Define the dimensionless initial/final leading-strain cost

    C_h=(|xi0|/|xi*|) |M(t*,0)^(-1)b*|.                (2)

For the proposed receiving amplitude, its leading initial strain is
comparable to ell^(7/8) C_h. The exact two-dimensional adjugate identity
turns (2) into

    C_h=|M(t*,0)^* p(t*)|,                            (3)

where the adjoint maps the final polarization plane to the initial one.
Here xi*/|xi*| cross b*=p(t*). Thus the cost is an adjoint amplitude gain
in the outgoing velocity direction, not an unspecified inverse constant.
The general bounds give only exp(-C ell)<=C_h<=exp(C ell), after changing C.

For fixed a2=k ell^(7/8), small initial C1 requires

    ell^(7/8) C_h ->0.                                (4)

Neither the determinant nor the generic exponential bounds prove (4).
Allowing a scalar multiplier eta_h on that amplitude, small initial
strain and final strain dominating the host ell require respectively

    eta_h ell^(7/8) C_h ->0,
    eta_h ell^(1/8) ->infinity.

Such scalar choices exist exactly when C_h=o(ell^(-3/4)). This is an
endpoint linear cost criterion, not control of nonlinear feedback during
the intervening first stage.

## 2. Reference V and actual q must not be interchanged

On the frozen Euler action annulus, the coordinate flow has constant
actions and affine angle shear. Its deformation and inverse are bounded
by C(1+t). Thus the reference-V covector preparation costs at most
C(1+T), and fixed-coefficient reference polarization bounds cost
exp(C T), a fixed power of ell.

These are not bounds for the actual-q polarization map. Although
||q-V||_infinity is small, its gradient contains the growing outgoing
rank-one wave, and its time integral is of order ell. Replacing the
actual map by the reference map is unjustified.

For the exact parallel-shear control, with covector e2 and polarization
b*=e3, the full map in the e1,e3 plane is

    M=[[1,-Theta],[0,1]],
    M^(-1)e3=Theta e1+e3,
    C_h=sqrt(1+Theta^2).

This is an exact inverse-cost obstruction for that specified shear
class. It is not proved for actual q, whose bounded background terms
can change the amplitude map substantially over a growing time interval.

## 3. A specified initial phase class cannot receive the new orientation

Let xi_p be the first primary phase gradient, transported by V. Along
the actual q particle, it obeys

    D_q xi_p+A_q^T xi_p=grad[(q-V).xi_p].                (5)

The primary oscillation has normal velocity
-h div(b_p) sin(phi_p). Its differentiated size is O(h^(1/2) poly(ell));
the mean and harmonic normal contributions are smaller. The true
first-stage C1 error is h^(1/24-o(1)), and the velocity error is
h^(9/8-o(1)). Thus the right side of (5) is h^(1/24-o(1)).

Let N_q be the exact actual-q cotangent solution with N_q(0)=xi_p(0).
Variation of constants and integral ||S(q)||<=C ell give

    N_q(t)-xi_p(t,Y(t))=h^(1/24-o(1)),  0<=t<=T.        (6)

The primary covector is uniformly nonzero. Therefore any original seed
with initial covector collinear with xi_p(0), including any harmonic of
that phase, arrives essentially parallel to n(t*), whereas the receiving
covector Q(t*)e2=n cross p is perpendicular to it. A polynomially narrow
initial cone about the primary covector has the same obstruction:
its angular width h^beta, beta>0, remains o(1) after exp(C ell) conditioning.

This excludes a specified principal-phase class. It is not an invariant
Fourier-support theorem and does not exclude new orientations generated
by general nonlinear three-dimensional interactions or independent
initial phases.

## 4. Forward finite-wave preparation from time zero: construction

This section constructs original data and then solves only forward
linearized NS. Choose a fixed smooth nonnegative bump chi, supported
strictly in the unit ball, with chi(0)=1. At time t* prescribe only the
smooth geometric targets

    S_*(y)=xi*.(y-y*),
    b_*(y)=a2 chi((y-y*)/d) b*.

Pull S_* back by the smooth q flow to define S(0), and thereafter let
D_q S=0. On each characteristic use the finite inverse amplitude map to
define b(0) from b_*, and thereafter solve D_q b=G b. These definitions
give exactly S(t*)=S_* and b(t*)=b_* on the phase patch. They do not
solve a backward parabolic equation. The initial support is the smooth
preimage of B(y*,d), and its volume is preserved.

The construction continues forward from t* to T along q. Use phase offset
pi/2, so the central oscillation is at a strain maximum throughout.
Define F=xi cross b/|xi|^2, d_b=curl F, and the primary curl packet

    W0=k curl[i F exp(i(S/k+pi/2))].                    (7)

One additional *linear* amplitude correction suffices for C1 tracking.
Let H1=i k[(D_q+A)d_b+grad(2xi.Ab/|xi|^2)], and solve forward

    D_q g=G g-Pi_xi H1,  g(0)=0.

Set W1=C_1[g] with its full forced pressure, including xi.H1/|xi|^2.
The approximation is Re(W0+W1). Its initial datum is exactly Re W0(0);
no extra mean or second harmonic is required in this linear equation.

The following sections record the derivative, residual and forward
tracking estimates needed for this construction. They are a proposed
restricted analytic derivation, pending independent review; they must
not be read as a nonlinear second-stage theorem.

## 5. Uniform jets on the entire first-stage interval

The higher-order argument in the outgoing note extends from its terminal
interval to [0,T]. A convenient dominating rate is

    m(t)=1+ell^(-1) exp(mu t),
    integral_0^T m(t)dt <=C ell.                         (8)

The sharp primary-amplitude bound is C h ell^(-1)exp(mu t), plus lower
terms h times positive powers of h times fixed powers of ell. Every
slow derivative substitutes a delta_1^(-1) factor, delta_1=sqrt(h), for
an oscillatory h^(-1), so its scaled derivative is smaller. The first
mean and harmonic corrections have scaled derivatives tending to zero.

To make every later fixed derivative explicit, choose first-stage
background H128, primary phase/amplitude order160, mean H132, and
harmonic-amplitude order129. Q0 in H132 uses amplitude134/phase135,
within those orders. The mean's H132 bound supplies C129 for the forced
harmonic equations. This gives U_app H128. The known Lipschitz integral
also gives q H128 from its original smooth datum. Interpolating their
difference with the first-stage L2 error gives

    h^(r-1)||D^r(q-U_app)||_infinity
       <=h^[1/4-(r+3/2)/128-o(1)],  1<=r<=24.

The smallest displayed exponent is 13/256. Therefore, for sufficiently
small h, the following actual-q bound holds with fixed constants:

    ||D^r q(t)||_infinity <=C_r m(t) h^(1-r),
              1<=r<=24,  0<=t<=T.                     (9)

This is a spatial derivative bound, not a bound for q's translating
O(1) velocity. Translate the h-cell by Y(t) and use the time variable
tau=integral_0^t m. Its coefficients have bounded spatial derivatives
through order24. The time interval is O(ell). Fixed forward and inverse
flow jets, normalized-covector jets, amplitude jets, and inverse-amplitude
jets therefore cost

    E_h=exp(C ell),                                    (10)

where the constant may be enlarged finitely many times. This remains
h^(-o(1)); none of these estimates introduces exp(exp(C ell)). The
normalized direction evolves on the compact unit sphere. Covector
magnitude and its reciprocal satisfy scalar linear equations, avoiding
a spurious nested exponential in the jet induction.

The preimage and every transported image of the target ball have diameter
at most d E_h=o(h). All vector potentials live on an embedded transported
patch and vanish smoothly before its boundary. Their zero extensions
are smooth periodic vector potentials. The volume of the transported
support is fixed, though its shape can be anisotropic.

For any required fixed r (primary derivatives through16 and correction
derivatives through13 suffice here), the two-sided geometric construction
in section4 has

    ||D^r b||_infinity <=C a2 d^(-r) E_h,
    ||D^r b||_2       <=C a2 d^(3/2-r) E_h,
    |D^r xi|         <=C h^(-r) E_h,
    |xi|+|xi|^(-1)   <=E_h.                            (11)

The late bump has point amplitude one, not unit L2 amplitude. Its L2
factor d^(3/2) is retained explicitly in (11). All Leray estimates are
in global unnormalized L2 and have constants independent of L.

## 6. Complete forward linearized viscous tracking

Write A=grad q, D=D_q and theta=S/k+pi/2. The primary exact pressure is
pi0=i k(2xi.Ab/|xi|^2)exp(i theta). Direct differentiation yields

    (D+A)W0+grad pi0=H1 exp(i theta).

The forced curl lift W1 has the pressure

    pi1=i k[2xi.Ag/|xi|^2+xi.H1/|xi|^2] exp(i theta).

The identity from the earlier notes cancels H1 exactly and leaves

    (D+A)(W0+W1)+grad(pi0+pi1)
       =k exp(i theta)[(D+A)c_g
             +i grad(2xi.Ag/|xi|^2+xi.H1/|xi|^2)],      (12)

where c_g=i curl(xi cross g/|xi|^2). The longitudinal forcing term is
retained. The identity works for the actual time-dependent q and uses
no Euler equation for that background.

The material derivative of a curl uses only D partial_j F=
partial_j D F-(partial_j q_m)partial_m F. Since Dxi and Db (or Dg)
are specified by their amplitude equations, there is no independent
q_t estimate. Bounds (9)-(11) and integration of the forced ODE give

    ||D^r g||_2 <=C a2 d^(3/2-r) (k/d) E_h,
    ||D^r g||_infinity <=C a2 d^(-r)(k/d) E_h.           (13)

With eta=a2 d^(3/2), the full linearized NS residual, including viscosity
and the exact Leray projection, consequently has integrated L2 bound

    integral_0^T ||R||_2 dt
       <=C_nu eta[(k/d)^2+epsilon/k^2] E_h
       <=h^(31/8) E_h.                                (14)

Here eta=h^(27/8)ell^(7/8), (k/d)^2=h^(1/2), and
epsilon/k^2=nu h. Powers of ell are absorbed in E_h. The viscous
L2 derivative of the curl lift uses at most third amplitude derivatives.
The lower covector bound in (11) is allowed to be subpolynomial rather
than a fixed number; its finite inverse powers are included in E_h.

In particular the potential principal viscous attenuation over the
whole original-time flight is bounded by

    (epsilon/k^2) integral_0^T |xi(t)|^2 dt
                        <=C_nu h exp(C ell)=o(1).

Its exponential attenuation therefore tends to one. This observation
alone is not used as an exact viscous transport formula: the full
forward comparison above also includes all envelope and curl Laplacians.

Let z solve the exact real homogeneous linearized NS equation about q,
forward from z(0)=Re W0(0). For each fixed h this is a classical linear
initial-value problem with prescribed smooth coefficients. The L2
energy inequality and integral ||S(q)||<=C ell give

    sup_[0,T] ||z-Re(W0+W1)||_2 <=h^(31/8) E_h.          (15)

To upgrade this to C1, use the weighted integer norm

    ||v||_{H_k^s}^2=sum_{|alpha|<=s} k^(2|alpha|)||D^alpha v||_2^2.

For s=12, differentiation of the *linear* equation gives

    d/dt ||z||_{H_k^s} <=C_s m(t)||z||_{H_k^s}.          (16)

Every transport commutator contains a factor
k^(j-1)||D^j q||_infinity<=C m(t)(k/h)^(j-1), and every differentiated
stretch term has the analogous factor k^j||D^(j+1)q||_infinity.
These are bounded by C m(t), since k<h. The undifferentiated transport
cancels; pressure disappears in the divergence-free pairing; viscosity
is dissipative. Thus (16) uses q derivatives only through order13 and
has constants uniform in the expanding torus. It avoids incorrectly
applying a nonlinear Hs tame bound to the linearized equation.

Both the initial datum and the approximation have H_k^12 norm at most
eta E_h, using (11)-(13). It follows that the H12 norm of z and of the
approximation is bounded by

    eta k^(-12) E_h=h^(-117/8) E_h.                    (17)

Uniform interpolation of (15) and (17) now gives

    ||z-Re(W0+W1)||_{W1,infinity} <=h^(1/48-o(1)),
    ||z-Re(W0+W1)||_infinity <=h^(25/16-o(1))=o(k).      (18)

The gradient exponent is (31/8)(1-5/24)+(-117/8)(5/24)=1/48.
The velocity exponent uses weight3/24 and equals25/16. Keeping only W0
would give L2 error h^(29/8-o(1)) and gradient exponent
-1/8-5/(8s)<0 for every s: the linear correction is necessary for this
C1 conclusion.

At t*, W0 is exactly the desired real affine-phase curl packet with
point amplitude a2 and radius d. The C1 norm of W1 is at most
(a2/d)E_h=h^(1/4)ell^(7/8)E_h=o(1). Therefore the original-time exact
linearized datum arrives at that late receiving packet with o(1) C1
error. The central receiving ODE on [t*,T], now run forward, gives

    ||S(z(T))||_infinity >=c ell^(9/8)-o(1).             (19)

This is a linearized preparation and a linearized strain observation.
It is not an additional NS solution q+z, because z.grad z was never
discarded from a claimed nonlinear equation.

## 7. What is and is not compatible with small initial feedback

Write b(0,x)=a2 chi_0(x) B_0(x), where chi_0 is the transported bump and
B_0 is the unweighted inverse polarization reaching b*. Let x_c be the
central initial particle, B_c=B_0(x_c), and N_c=xi_0(x_c). The jet and
inverse-map estimates give

    sup_support (|B_0-B_c|+|xi_0-N_c|)<=(d/h)E_h,
    E_h^(-1)<=|B_c|,|N_c|<=E_h.

Thus the relative variation of the unweighted polarization and phase
gradient is (d/h)E_h=o(1), after enlarging the fixed constant in E_h.
The bump itself varies from one to zero; neither the full amplitude
nor the scalar phase is asserted relatively constant.

For z(0)=b(0)cos(theta_0)-k d_b(0)sin(theta_0), the leading gradient is
-b tensor xi_0 sin(theta_0)/k. The other gradient terms are bounded by
C a2[d^(-1)+k d^(-2)]E_h, and the velocity by C a2 E_h. Relative to
a2|B_c||N_c|/k these cost at most
C[(k/d)+(k/d)^2+k]E_h=o(1). At x_c, chi_0=1 and theta_0=pi/2 exactly,
so the leading gradient is attained and the remaining curl-gradient
term is smaller. Using |xi*|=4 and the definition of C_h gives the
two-sided estimate

    c (a2/k) C_h <=||z(0)||_{C1}<=C (a2/k) C_h,         (20)

with fixed positive constants. Its support is specified at time zero,
and its smooth real zero-mean solenoidality follows from the original
curl; no late-time insertion or backward NS solve is used.

Equations (18)-(20) constitute a restricted forward viscous linearized
preparation with an explicit, unresolved initial-strain price. They do
not prove the smallness condition (4) for actual q. Nor would (4) alone
control nonlinear feedback before t*: one must also bound the arriving
seed's full earlier strain history and its nonlinear error. Generic
exp(C ell) amplitude bounds can make that history far too large for a
useful nonlinear stability estimate even though its velocity is small.

The next concrete actual-q quantity is therefore the adjoint row norm
in (3), together with a time-resolved version for earlier feedback.
The same-primary-phase class is already excluded by (6). The exact shear
control has a growing cost. The actual three-dimensional q map is not
yet evaluated sharply enough to establish either favorable preparation
or an unconditional inverse-cost obstruction. No nonlinear compatibility,
infinite iteration, or solution of ROOT is asserted.

## 8. Separate read-only review of the late nonlinear candidate

After the main derivation, the complete draft
[the late nonlinear second-handover draft](second-nonlinear-handover-draft.md) was independently read.
No load-bearing defect was found at its finite late-data scope. The
fixed q C24 budget covers the weighted mean H16 and harmonic order13;
the full pressure is retained; the listed residual/viscosity powers
check; the sharp strain integral is O(ell^(3/8)); and the first-stage
H12 factor is absorbed by its h^(35/8) relative power before the new
error bootstrap. Its gradient exponent1/48 and the observation on an
actual *base-q* particle are consistent. This review does not connect
that late nonlinear solution to the original-time datum constructed
for the linear equation here.

## 9. Independent review of sections 4–7 and correction record

A separate reviewer read sections 4–7 against the registered log-log
and outgoing-wave inputs. The pre-correction copy reviewed had SHA-256
`fe830671e125e23b5bd3ed73c3d10ee224970bac1a9935ec4045cb348b8369b5`.
The review accepted the forward linearized preparation, with the explicit
section 7 correction above. Its principal checks were:

- H128 interpolation supplies the whole-interval scaled C24 background
  jets; the worst positive h exponent is 13/256. Integrating
  m(t)=1+ell^(-1)exp(mu t) costs O(ell), including the earlier flight.
- Inverse flow, covector and polarization jets cost exp(C_r ell) at each
  fixed order. Volume preservation retains d^(3/2) in L2 even when the
  transported support is anisotropic.
- The forced pressure includes the term +xi.H1. Exact curl cancellation
  leaves a residual involving grad H1, without an unpriced material
  derivative of the background gradient.
- The complete viscosity residual and first finite-wave correction give
  integrated L2 error h^(31/8-o(1)). The linear weighted H_k^12 estimate
  uses only the background jets, giving H12 size h^(-117/8-o(1)).
- Uniform expanding-torus interpolation gives gradient error
  h^(1/48-o(1)) and velocity error h^(25/16-o(1))=o(k).
- Twelve independent exact rational checks verified the exponent ledger.
  These checks support the arithmetic; the PDE estimates remain written
  mathematics, not a formal-kernel certificate.

The correction separates the bump from the slowly varying polarization;
it changes neither the two-sided cost nor any parameter exponent. The
review did not estimate C_h favorably, control nonlinear feedback,
recheck the phase exclusion in section 3, or establish infinite iteration.
