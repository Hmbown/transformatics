# A finite-wave linear amplifier on the actual outgoing NS wave

**8 September 2026 — PROVED at the restricted linearized scope below.**
Node: `nse-outgoing-wave-linearized`. This is a written analytic proof
with independent reviews and exact algebra controls. No full formal
certificate, effective profile threshold, novelty claim, or DNS is supplied.
ROOT and `(E′)` remain OPEN.

The background is the actual smooth unforced NS solution from
[the first handover](loglog-handover.md). The present result
realizes a finer wave's gain in its exact homogeneous linearization.
The second seed is specified at a later time t0. A nonlinear second
handover, a compatible seed in the original datum, and infinite iteration
remain unproved.

Throughout, h ranges over that same first-stage family h=L^(-1/10),
with L sufficiently large integers, one frozen Gavrilov profile, and one
fixed physical viscosity nu>0. The principal ODE and the additional
actual-characteristic argument are proved in Appendix A; they are not
assumed from the large strain supremum alone. Equation numbers in the
appendix are local to that appendix.

## 1. Statement and scales

Put

    ell=sqrt(log(1/h)),      epsilon=nu h^4,
    Delta=ell^(-3/4),        t0=T_h-Delta,
    k=h^(3/2),              d=h^(5/4),

and let q be the actual first-stage smooth NS solution on the expanding
torus T_L, L=h^(-10). Let Y(t) be its particle starting at the original
central point x0 at time zero. In the following all L2 and Sobolev norms
on T_L are unnormalized. Write P_high=P_{|D_y|>1/k}.

**Theorem.** For all sufficiently small h in the first-stage family, there is a real, smooth,
mean-zero, exactly solenoidal datum f_{2,h}, supported in B(Y(t0),d), with
||f_{2,h}||_2=1, such that the exact solution of

    w_t-epsilon Delta_y w
       +P_L[(q.grad)w+(w.grad)q]=0,
    w(t0)=f_{2,h},                                        (1)

obeys

    ||P_high w(T_h)||_2
       >=c ell^(1/4)-C_nu h^(1/4) F_h
       >=(c/2)ell^(1/4),                                 (2)

where F_h=ell^K exp(C ell^(1/4)) for fixed finite K,C. The constants do
not depend on h or L. They may depend on the frozen first-stage profile,
fixed physical viscosity, and the fixed norm orders used below. In addition

    ||P_high f_{2,h}||_2=1-o(1).

Here h^(1/4)F_h=h^(1/4-o(1)) tends to zero. The datum is specified at t0,
which is an initial time for (1), not the original NS initial time zero.

## 2. The additional fixed-order estimates must be justified first

The first-stage Lipschitz bootstrap already gives

    integral_0^{T_h} ||grad q||_infinity dt <=C ell,
    ||q-U_app||_2<=h^(11/4-o(1)).                         (3)

Its H12 proof alone is not an H32 error estimate. We now extend the same
explicit U_app estimates at fixed higher orders. This does not change
U_app or q. For clarity, sufficient orders are: primary phase and
unweighted amplitude derivatives through order 40; mean estimates through
H36; harmonic-amplitude derivatives through order 33; and the fixed
background comparison through H32. All are fixed before h tends to zero.

These orders are available because the profile and bump are C-infinity.
The original weighted estimates hold at every fixed finite order.
Specifically, Q0 in H36 needs primary amplitude derivatives through 38
and phase derivatives through 39; its forced linear Euler solution m in H36 supplies
the C33 bounds used when differentiating m.xi times the primary amplitude.
F1,F2 and the tangent ODEs then supply the harmonic derivatives through
33. One further curl derivative suffices for U_app in H32. The previously
proved normalized-direction flow argument applies at the indicated
primary orders with fixed finite coefficients. No derivative index or
profile cutoff is chosen as a function of h.

The H32 background comparison has its own fixed finite rate, but its
logarithmic lifetime contains T_h=O(log log(1/h)) for sufficiently small
h. Uniqueness identifies this background with the one already in U_app.
The higher-order bookkeeping therefore yields

    ||U_app(t)||_{Hs} <=h^(7/4-s-o(1)),        s=32.

The ordinary NS Hs energy inequality, now using the already closed
Lipschitz bound (3), also gives

    ||q(t)||_{Hs} <=h^(7/4-s-o(1)).

Thus the error e=q-U_app has that same Hs upper bound. Uniform expanding-
torus interpolation, including its harmless L2 term, gives for fixed r

    ||D^r e||_infinity
       <=h^[5/4-r-(r+3/2)/s-o(1)],        s=32.            (4)

For r=1,...,5, multiplication by h^(r-1) leaves a positive power
(13-2r)/64-o(1). Consequently the error's derivatives are small compared
with ell h^(1-r). The old H12 bounds likewise give
||e||_infinity<=h^(9/8-o(1)), as used for the actual-particle phase lock.

On the terminal interval [t0,T_h], the primary amplitude is bounded by
C h ell across its whole transported support, and its covector is
uniformly bounded. To see the amplitude bound, factor out the transported
bump and use its initial-point continuity about the central expanding
polarization; its error is h times a positive power of h times a fixed
power of ell. Differentiating the oscillation r times gives the principal
bound C_r ell h^(1-r). Every slow-envelope or phase-jet derivative costs
only delta_1^(-1)poly(ell), where delta_1=h^(1/2), in place of h^(-1).
It is therefore smaller by a positive power of h. The mean and harmonic
correction cell-scale derivatives are smaller as well. The smooth
background contributes only fixed bounded derivatives. Together with
(4), this proves the global bounds

    ||D^r q(t)||_infinity <=C_r ell h^(1-r),
                  r=1,...,5,  t0<=t<=T_h.                 (5)

The r=0 field q includes its O(1) translating background; (5) does not
assert that q itself has size h ell. A translated cell below removes
that velocity from the derivative argument.

## 3. Central carrier and the correct geometric derivative scale

At t0 let Q have columns (p,n cross p,n), the first-stage orthonormal
frame. In physical coordinates choose xi0=4 Q(t0)e2 and B0=Q(t0)e3.
The robust
transient lemma in Appendix A.3 applies along the actual q-characteristic Y(t). It gives

    3<=|N(t)|<=5,       t0<=t<=T_h,
    |B_*(T_h)|>=c ell^(1/4),                             (6)

after making h sufficiently small. Here N and B_* are the physical
covector and polarization along Y. Their equations are

    N'=-A^T N,
    B_*'=-A B_*+2N(N.A B_*)/|N|²,
    A=grad q(t,Y(t)).

Scaling xi0 by four does not change the amplitude equation. The time
interval lies inside the proved first-stage lifespan; no continuation
beyond T_h is assumed.

Let Phi(t,a) be the q flow initialized at a at t0. Define the secondary
phase by D_q S=0 and S(t0,y)=xi0.(y-Y(t0)) on a ball slightly larger than
the packet. Then xi=grad S solves D_q xi=-A^T xi. Along every particle
let B(t,a) solve the same real polarization equation, initialized at the
constant vector B0, without including the envelope.

The unweighted quantities xi and B have initial-point derivative scale
h, the background cell size, rather than d, the bump size. To verify
the uniform time constants, set tau=ell(t-t0) and consider the translated
cell flow

    Z(tau,z)=[Phi(t,Y(t0)+h z)-Y(t)]/h.

Its vector field is

    [q(t,Y(t)+h Z)-q(t,Y(t))]/(ell h).

Its spatial derivatives through order five are bounded uniformly by
(5); its value at Z=0 is zero. The normalized covector n=xi/|xi| obeys
a smooth equation on S² whose derivatives through the required orders
are uniformly bounded in these variables. Its coefficients involve
A/ell and its scaled spatial derivatives. The scalar magnitude and its
reciprocal satisfy linear scalar equations, and B satisfies a linear
vector equation with uniformly bounded coefficients.
The translated cell is used only to estimate flow derivatives; the PDE
comparison in section 5 remains on the original expanding torus.

Differentiate these equations with respect to z, up to order three
(order four is available from (5)). The coefficient on the highest
derivative stays bounded, and lower derivatives enter finite products.
Induction and variation of constants therefore give fixed C_r with

    |D_a^r xi(t,a)|+|D_a^r B(t,a)|
                            <=C_r h^(-r) E_h,
    |D_a^r Phi(t,a)|        <=C_r h^(1-r) E_h,  1<=r<=3,  (7)

where E_h=exp(C ell^(1/4)); constants can be enlarged between lines.
The magnitude, reciprocal magnitude, and the relevant inverse-flow jets
have the same type of bounds. No q_t bound is used in this derivative
induction. Time dependence of the bounded coefficients causes no loss.

For |a-Y(t0)|<=d, (7) supplies

    |xi(t,a)-N(t)|+|B(t,a)-B_*(t)| <=C(d/h) E_h.          (8)

Since d/h=h^(1/4), (8) tends to zero. In particular xi is bounded above
and away from zero by fixed constants on the entire packet, not merely
on its central particle. Its transported support has diameter at most
C d E_h=o(h). All fields can be defined on that transported phase patch.

## 4. Exactly solenoidal packet and its derivative ledger

Fix a real smooth bump chi supported strictly inside the unit ball,
normalized by ||chi||_2=1. Write

    chi_d(a)=d^(-3/2)chi((a-Y(t0))/d),
    b(t,Phi(t,a))=chi_d(a) B(t,a).

It satisfies the exact tangent amplitude equation D_q b=G b and
xi.b=0. The flow is volume-preserving. Product differentiation, (7), and
the inverse-flow estimates give

    ||grad^r b(t)||_2 <=C_r d^(-r) E_h,       r=0,1,2,3.  (9)

Derivatives of xi/|xi|² have pointwise bounds C_r h^(-r) E_h.
The inequality d<h lets d^(-r) dominate all geometric inverse-cell
costs in (9). The d^(-3/2) pointwise normalization introduces no additional
L2 loss: its square is canceled by the volume Jacobian in the initial
bump integral. Coherence (8), however, must be applied to the unweighted
B, not estimated by derivatives of chi_d B.

Define the real field d_b=curl(xi cross b/|xi|²), and the complex packet

    W^a=k curl[i(xi cross b/|xi|²)exp(iS/k)]
       =(b+i k d_b)exp(iS/k).                            (10)

The vector potential vanishes smoothly near the phase-patch boundary.
Its zero extension is a smooth periodic vector potential, so W^a is
exactly divergence-free and mean-zero. No global affine periodic phase
or invariant Fourier support is assumed.

From (9), k<d<h, and the phase derivative bounds,

    ||d_b||_2 <=C d^(-1) E_h,
    ||W^a||_{H1} <=C k^(-1) E_h,
    ||Delta_y W^a||_2 <=C k^(-2) E_h.                    (11)

For the last estimate, the raw envelope powers are

    k^(-2),  k^(-1)d^(-1),  d^(-2),  k d^(-3).

Each is at most k^(-2). Additional derivatives of xi cost h^(-1),
which is smaller than d^(-1), and are included in E_h. This accounts
for the viscous derivative of the exact curl correction as well.

## 5. Full pressure residual; no time derivative of q is required

Let D=D_q and A=grad q. Put p_b=2xi.A b/|xi|² and
pi^a=i k p_b exp(iS/k). The exact identity is

    (D+A)W^a+grad pi^a
       =i k exp(iS/k)[(D+A)d_b+grad p_b].                (12)

It holds for every smooth time-dependent incompressible q. It does not
require q to solve Euler. To estimate the right side, if
F=xi cross b/|xi|², then DF is algebraic in A,xi,b,|xi|^(-1), since Dxi
and Db are already specified. The commutator is

    D(partial_j F_k)=partial_j(DF_k)-A_mj partial_m F_k.

Thus D curl F needs only spatial derivatives of A and the first spatial
derivatives of b and xi. There is no hidden q_t or A_t requirement.
Using (5), (9), and d<h gives

    ||(D+A)d_b||_2+||grad p_b||_2
                  <=C ell(d^(-1)+h^(-1))E_h
                  <=C ell d^(-1)E_h.                   (13)

The full viscous linearized residual, with its approximate pressure, is

    R=i k exp(iS/k)[(D+A)d_b+grad p_b]
                                           -epsilon Delta_y W^a.

Consequently

    ||R(t)||_2 <=C_nu[k ell/d+epsilon/k²]E_h
               <=C_nu[ell h^(1/4)+nu h]E_h.             (14)

Applying the exact periodic Leray projector removes pi^a. It is an L2
contraction uniformly in L, so (14) retains the full nonlocal pressure.
There is no background-mismatch term: the phase and amplitude were
transported by the actual q, not the earlier Euler background V.

For fixed h, equation (1) with smooth datum has a unique smooth solution
on the whole interval. For example, Galerkin approximation and fixed-order
linear energy estimates with the smooth prescribed coefficients q give
this statement. It involves no nonlinear continuation hypothesis beyond
the already existing smooth q. Let W solve its complex version with
W(t0)=W^a(t0). The exact error energy inequality is

    d/dt ||W-W^a||_2
           <=||S(q)||_infinity ||W-W^a||_2+||R||_2.

Since ||grad q||<=C ell and the interval has length Delta,

    sup_[t0,T_h] ||W-W^a||_2
       <=C_nu Delta[k ell/d+epsilon/k²] exp(C ell Delta)
       <=C_nu h^(1/4) F_h.                              (15)

Any fixed powers of ell are absorbed into F_h. The exponent
ell Delta=ell^(1/4) is sublogarithmic in 1/h. All norm constants above
are independent of the expanding volume.

## 6. Actual radial high-pass projection

The complex packet has the first-moment estimate

    ||(-i k grad-N(t))W^a(t)||_2
             <=C[(d/h)+(k/d)]E_h
             <=C h^(1/4)E_h.                           (16)

Indeed its two contributions are (xi-N) times the amplitude, controlled
by (8), and k times the slow amplitude derivatives, controlled by (9).
Products of E_h factors are absorbed by enlarging its fixed constant.

On a Fourier mode j/L with |j/L|<=1/k, (6) implies

    |k j/L-N(t)|>=|N(t)|-1>=2.

Parseval therefore gives ||P_low W^a||_2 at most one half the left side
of (16), uniformly in L. There is no mode-counting factor. This moment
estimate is applied to the complex packet; a real packet has two signed
carrier lobes and does not obey the same one-lobe moment estimate.

## 7. Real normalization and the final lower bound

The real part of (10) is

    Re W^a=b cos(S/k)-k d_b sin(S/k).

Pull back by the volume-preserving q flow. The phase becomes the initial
affine phase S0(a)=xi0.(a-Y(t0)). Its scalar bump integral is

    integral chi_d² cos²(S0/k)=1/2+O(k/d).                (17)

To verify the error, integrate exp(2iS0/k) once in the xi0 direction.
The factor is k/(2|xi0|), and ||grad(chi_d²)||_1<=C/d. The constant is
uniform in the orientation of xi0 because |xi0|=4.

By (8), the leading real packet at T_h differs in L2 from
chi_d(a) B_*(T_h)cos(S0/k) by at most C(d/h)E_h. Its real curl correction
has norm at most C(k/d)E_h. Consequently (6) and (17) give

    ||Re W^a(T_h)||_2
       >=|B_*(T_h)|sqrt(1/2-C k/d)
                         -C[(d/h)+(k/d)]E_h
       >=c ell^(1/4)-C h^(1/4)F_h.                      (18)

At t0 the same calculation, with B0 unit and constant, gives

    m_h:=||Re W^a(t0)||_2=1/sqrt(2)+O(k/d),
    1/2<=m_h<=2

for sufficiently small h. Define f_{2,h}=Re W^a(t0)/m_h. It has all
the smoothness, support, divergence, mean, and normalization properties
in the statement.

The radial Fourier projector commutes with taking real parts, and

    ||P_low Re W^a||_2<=||P_low W^a||_2.

Use this inequality after (16), not a one-lobe moment estimate on the
real wave. Since the linear equation has real coefficients, its solution
with datum f_{2,h} is Re W/m_h. Combining (15), (16), and (18) proves
(2). At the initial time (16) has no coherence term, since xi0 is constant;
it gives ||P_low f_{2,h}||_2<=C k/d=o(1). This proves the initial high-pass
normalization as well.

## 8. Scope and the next missing transfer

The above establishes a finite-wavelength, all-mode
linearized NS realization of the outgoing-wave transient. Its background
is the actual full unforced NS solution from the first handover, and the
second carrier has frequency of order h^(-3/2), finer than the original
h^(-1) wave. No steady viscous eigenvalue or Floquet assertion is used.

The gain is ell^(1/4)=(log(1/h))^(1/8). Physical rescaling preserves this
L2 gain ratio and the original fixed viscosity. The datum in this theorem
is specified at t0. No argument here places it in the original datum at
time zero, proves that nonlinear dynamics generated it, or controls its
quadratic self-interaction. A nonlinear second stage, compatible dormant
seed transport, and an infinite-stage conclusion remain separate open
tasks. None of them follows from (2).

## 9. Verification and reproduction

The [instrument](../../experiments/nse_outgoing_wave.py),
[independent tests](../../tests/test_nse_outgoing_wave.py), and
[receipt](../../artifacts/enstrophy_sup/nse_outgoing_wave.json) contain 36
exact controls and seven passing focused tests. They include direct
viscous linearized-PDE differentiation of an affine-shear plane wave,
its pressure Poisson equation, returning-plane Jordan dynamics, high-norm
scaling, and the two signed lobes of a real packet. The affine control
is local and unbounded; it is not an admissible periodic background.
These finite calculations do not certify the written PDE theorem.

Two independent derivations and a full assembled-proof review found no
load-bearing defect at the late-time linearized scope. The final proof
includes the requested component bootstrap, fixed higher-order estimates,
phase-derivative bookkeeping, finite flow-jet range, and complex-then-real
Fourier argument. The earlier curl/pressure identities also have the
[separate log-log controls](../../experiments/nse_loglog_handover.py).
No independent theorem of nonlinear seed compatibility is being imported.

## Appendix A. The outgoing shear and its actual-characteristic realization

### A.1. Complete principal dynamics of the exact parallel shear

Let U=F(z)e1, F(z)=a cos(z/h). For a periodic example choose compatible
periods; the particle/ODE calculation is local and works for every h>0.
On the particle starting at (x0,y0,z0),

    X(t)=(x0+t F(z0),y0,z0),
    A=grad U=sigma e1 tensor e3,
    sigma=F'(z0)=-(a/h)sin(z0/h),          A²=0.

The symmetric strain has eigenvalues sigma/2,-sigma/2,0, while all
eigenvalues of A are zero. Neither those strain eigenvalues nor their
magnitude are polarization Floquet exponents.

Write xi(0)=(p,q,r), xi(t)=(p,q,zeta(t)), and K(t)=|xi(t)|². The exact
covector and polarization equations are

    zeta=r-sigma p t,
    b'=sigma b3[-e1+2p xi/K],              xi.b=0.

In particular,

    b3(t) K(t)=C:=b3(0) K(0).                         (1)

For p nonzero put kappa=sqrt(p²+q²)>0 and

    J(s)=s/[2kappa²(kappa²+s²)] + atan(s/kappa)/(2kappa³).

The complete solution, with b1(0) determined by transversality, is

    b3=C/(kappa²+zeta²),
    b2=b2(0)-2q C[J(zeta)-J(r)],
    b1=-(q b2+zeta b3)/p.                              (2)

Direct symbolic differentiation independently checked all three ODE
components, including the pressure factor two. Formula (2) is bounded
for all real t for each fixed p nonzero. As t tends to positive infinity
when sigma p is nonzero, b3=O(t^-2), b2 approaches a finite limit, and
b1 approaches -q b2(infinity)/p. The constants are not uniform as p
tends to zero. Large finite transients are therefore entirely compatible
with this boundedness statement.

For example, if q=0, the planar x-z polarization has norm ratio
sqrt(K(0)/K(t)). When r/(sigma p)>0 it reaches its maximum at the swing
zeta=0, with ratio sqrt(K(0))/|p|. Its out-of-plane component b2 stays
constant. This is a transient calculation, not an exponential multiplier.

### A.2. Returning covectors and the viscous-shear distinction

For T>0, xi(T)=xi(0) if and only if sigma p=0.

If sigma=0, A=0 and every covector and polarization is constant. If
sigma is nonzero, every returning covector has p=0, and the exact solution
is

    xi=(0,q,r),
    b(t)=(b1(0)-sigma t b3(0),b2(0),b3(0)),
    q b2(0)+r b3(0)=0.                                (3)

On xi-perpendicular space, use the orthonormal basis

    e1,       v=(0,-r,q)/sqrt(q²+r²).

The time-T map is

    [[1, -sigma T q/sqrt(q²+r²)], [0,1]].               (4)

Both multipliers are one. It is a nontrivial Jordan map if sigma q is
nonzero, and the identity if q=0. In particular a covector normal to the
original wave, xi=e3, gives no polarization growth, while xi=e2 and
b(0)=e3 give b=e3-sigma t e1 and linear norm growth. The largest singular
value of [[1,gamma],[0,1]] is
(sqrt(gamma²+4)+|gamma|)/2, even though both eigenvalues equal one.

If F(z0) is nonzero, a particle on a torus closes after its x-translation
period; (4) describes the returning-covector map for that period. If
F(z0)=0 the particle is stationary and any observation period may be
used. Repeated periods produce linear, not exponential, growth.

The stationary cosine shear is a steady Euler solution. At nonzero
viscosity epsilon its unforced NS realization is the heat shear

    U(t,z)=a exp(-epsilon t/h²)cos(z/h)e1.

All formulas above remain valid after replacing sigma t by
Theta(t)=integral_0^t sigma(s)ds. This background is time-dependent, so
its finite-time maps should not be called Floquet maps. For a secondary
WKB wavelength k, the viscous principal attenuation additionally has
factor exp[-(epsilon/k²) integral |xi|²dt]; it is not part of the inviscid
polarization ODE (1)-(4).

Unit shear multipliers do not survive arbitrary bounded perturbations.
The exact trace-free local jet

    A=lambda e1 tensor e3 + gamma e3 tensor e1,
    lambda>0, gamma>0,

has returning xi=e2, while the pressure-corrected amplitude on the x-z
plane has exponents plus/minus sqrt(lambda gamma). The perturbation
gamma e3 tensor e1 is O(1) when gamma is fixed. This is an exact local
jet control, not a periodic finite-energy construction or a claim about
the actual Gavrilov background. It prevents promoting the pure-shear
calculation into a universal impossibility theorem.

### A.3. A robust, finite transient lemma

Here is a specific ODE estimate that does survive an O(1) background.
Let a characteristic have a C1 orthonormal frame Q(t), and suppose on
[0,d] its actual gradient obeys

    Q^T A Q = sigma(t) e1 tensor e3 + B(t),
    c0 lambda <= |sigma(t)| <= C0 lambda,
    sigma has one sign,
    ||B||+||Q^T Q'|| <= C0.                            (5)

Constants c0,C0 are fixed. The fields need only be regular enough for the
principal ODE; the lemma does not assume their periodicity or stationarity.
Start the new covector in direction Q(0)e2, and its unit polarization in
direction Q(0)e3. If lambda d>=1 and d+lambda d² is sufficiently small,
then, in the moving frame,

    k1=O(d),  k2=1+O(d),  k3=O(d+lambda d²),
    beta3=1+O(d+lambda d²),
    beta2=O(d+lambda d²),
    beta1=-integral_0^d sigma(s)ds
                     +O(lambda d(d+lambda d²)).         (6)

Consequently |beta(d)|>=c lambda d. The constants depend only on those
in (5), not on lambda. A convenient asymptotic choice is

    d=lambda^(-3/4),
    |beta(d)|>=c lambda^(1/4),
    |k(d)-e2|<=C lambda^(-1/2).                         (7)

These covectors are approximately returning over one short interval;
the lemma supplies no exact return or expanding Floquet multiplier.

Proof details matter because the leading operator is not normal. In the
moving frame the covector equation is

    k'=-sigma k1 e3 + E_x(t)k,             ||E_x||<=C.

The leading fundamental matrix is I-(integral sigma)e3 tensor e1.
Duhamel therefore bounds sup|k| by
1+C(d+lambda d²)sup|k|. This gives sup|k|<=2. The first component then
has the sharper k1=O(t); the second is 1+O(t), and the third is
O(t+lambda t²). Keeping k1's sharper estimate is indispensable.

The amplitude equation can be written

    beta'=-sigma beta3 e1
           +2sigma beta3 k1 k/|k|²+E_b(t,k)beta,
    ||E_b||<=C.

The bounded error includes the background pressure term and frame
rotation; it is not obtained by dropping pressure. Bootstrap simultaneously

    |beta3|<=2,   |beta2|<=1,   |beta1|<=K lambda t,

with K a sufficiently large fixed constant. The beta3 bound is needed
in the pressure-component estimates; a total norm bound alone would not
justify them. The condition lambda d>=1 and small d gives lambda>=1.
These component bounds imply |beta(t)|<=C(1+lambda t).
The bounded error contributes at most
C(t+lambda t²) to beta2,beta3. The second pressure component has the
same integrated bound. The third pressure component integrates to
O(lambda t³+lambda²t⁴), which is smaller under the assumed smallness.
Thus beta3=1+O(t+lambda t²) and beta2=O(t+lambda t²). Integrating the first
equation gives its error in (6); this also closes the bootstrap. The
same-sign assumption gives the lower bound for its main integral.

### A.4. Applicability to the actual first-stage solution

The already reviewed log-log proof gives an exact NS solution q, with
q-U_app=e, L2 error h^(11/4-o(1)), and H12 size h^(7/4-12-o(1)). Uniform
interpolation consequently gives the additional useful bound

    ||e||_infinity <= h^(9/8-o(1)).                    (8)

Take Y(t) to be the actual q-particle starting at x0, and pull it back by
the frozen V flow. Since ||q-V||_infinity<=h poly(ell), its pulled-back
displacement is h poly(ell), much smaller than delta=h^(1/2). This keeps
the bump near chi(0)=1 and gives, along that particle, the same central
amplitude and bounded covector estimates up to vanishing relative errors.

The actual phase drift has the exact identity

    D_q S = (q-V).xi.

The primary leading amplitude is tangent. Its normal component is
Z.xi=-h(div b)sin phi. This is O(h²/delta poly(ell)); the global mean has
the same bound. The harmonic lifts contribute still smaller normal
components. The background mismatch is O(h⁴ poly(ell)); (8), divided
by h, tends to zero as well. Integration over O(log ell) time therefore
keeps phi(Y(t),t)=pi/2+o(1). This uses velocity tracking stronger than
mere C1=o(1), rather than assuming phase shadowing from it.

Let p=b/|b|, n=xi/|xi| along Y, and choose the orthonormal frame
Q=(p,n cross p,n). The exact identities

    D_q b = G_V b+(q-V).grad b,
    D_q xi = -A_V^T xi+(q-V).grad xi

give bounded frame rotation. Indeed ||grad b||<=h delta^-1 poly(ell),
|b|>=c h/ell, ||q-V||<=h poly(ell), and the extra relative derivative is
O(h/delta poly(ell))=o(1). The corresponding xi error is smaller.

All slow derivatives, mean/harmonic corrections and the true C1 error
are o(1), so along this actual particle

    grad q = -(|b||xi|/h)sin(phi) p tensor n + A_V + o(1).

On the terminal interval

    [T_h-ell^(-3/4), T_h],

the signed coefficient is comparable to -ell. Thus (5) holds with
lambda=ell on an interval already covered by the strong solution. The
robust transient lemma applies to the undamped geometric-optics
polarization system along this actual NS background, with new covector along n cross p and new
polarization along n. This appendix supplies a finite principal-ODE
statement; sections 3–7 above supply its linearized finite-wave realization.

After the closed Lipschitz bootstrap and the higher-order U_app
bookkeeping in section 2, the usual Hs energy estimate is
available at every fixed higher index, with the same type of bound
h^(7/4-s-o(1)). For a fixed derivative order r, interpolation gives

    ||D^r e||_infinity
           <=h^[5/4-r-(r+3/2)/s-o(1)].

Hence h^r||D^r e||/(h ell)=o(1) when s>4(r+3/2). For example fixed s=32
covers r<=5. This supplies finite cell-scale coefficient control without
letting a derivative index depend on h. It does not by itself prove the
next finite-wave estimate.
