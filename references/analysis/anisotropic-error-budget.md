# Anisotropic localization and the nonlinear error budget

8 September 2026. Bounded analytic test of the heat-based nonlinear
estimate in [force-removal stability](force-removal-stability.md).
No DNS, actual-reference propagator estimate, or unforced solution is
constructed here.

**Result.** Support in the thin, elongated core alone does not improve
the comparable-time heat–Leray quadratic estimate: an explicit smooth
solenoidal class retains its \(\tau^{-h}\) weighted loss. This holds on
\(\mathbb R^3\) and the fixed three-torus, including pressure. A separate
polarization assumption does give a power improvement for fixed smooth
profiles. No claim is made that the actual force-removal error has that
polarization.

## 1. Scales and the statement being tested

Fix \(\nu>0\) and \(0<h<1/2\); this includes the source range
\(0<h<1/6\). For \(0<\tau<1\), set

\[
r=\tau^{1/2},\qquad L=\tau^{1/2-h},\qquad
\lambda=r/L=\tau^h,\qquad
\alpha=1/2+h,\qquad A=\tau^{-\alpha}.
\]

Let \(C_\tau=\{|x_\perp|<r,\ |x_3|<L\}\), where
\(x_\perp=(x_1,x_2)\). The torus is
\((\mathbb R/2\pi\mathbb Z)^3\), with the core embedded around zero
for small \(\tau\). All integrals below use ordinary Lebesgue measure.
Let \(\mathbb P\) denote the full three-dimensional Leray projection.
Its multiplier at nonzero frequency is
\(I-\xi\otimes\xi/|\xi|^2\); the torus zero mode is retained.

We will construct \(e_\tau\in C_c^\infty(C_\tau;\mathbb R^3)\) with
\(\nabla\cdot e_\tau=0\), \(\|e_\tau\|_\infty=A\), and constants
\(c_*>0\), \(\tau_*>0\) such that

\[
\left\|e^{\nu c\tau\Delta}\mathbb P\nabla\cdot
             (e_\tau\otimes e_\tau)\right\|_\infty
\ge c_*\frac{A^2}{r},
\qquad \frac12\le c\le1,\quad 0<\tau<\tau_*.
\tag{1}
\]

Constants may depend on \(\nu\) and the fixed profiles, not on
\(\tau,c\) or the aspect ratio. The convention is
\((\nabla\cdot(e\otimes e))_i=\partial_j(e_i e_j)\).

## 2. A compact transverse interaction that pressure cannot erase

In two variables \(X=(X_1,X_2)\), choose a smooth cutoff \(\chi\)
supported in \(|X|<1\), equal to one on \(|X|\le1/2\). Put

\[
\psi(X)=\chi(X)X_1^2X_2,
\qquad v_0=(\partial_2\psi,-\partial_1\psi),
\qquad v=v_0/\|v_0\|_\infty.
\]

Thus \(v\) is smooth, compact, divergence free and has supremum norm
one. Define

\[
f_2=(v\cdot\nabla_X)v,
\qquad b=\partial_1(f_2)_2-\partial_2(f_2)_1.
\]

The scalar \(b\) is not zero. Before normalization, on \(\chi=1\),

\[
v_0=(X_1^2,-2X_1X_2),\qquad
(v_0\cdot\nabla)v_0=(2X_1^3,2X_1^2X_2),\qquad
\operatorname{curl}_2((v_0\cdot\nabla)v_0)=4X_1X_2.
\]

For instance this is nonzero at \((1/4,1/4)\). Normalization only
multiplies \(b\) by a positive constant.

Choose smooth \(0\le\eta\le1\), supported in \((-1,1)\), with
\(\eta=1\) on \([-1/2,1/2]\). In isotropically rescaled coordinates
\((X,Z)\in\mathbb R^2\times\mathbb R\), define

\[
V_\lambda(X,Z)=(v(X)\eta(\lambda Z),0).
\]

It is exactly divergence free. Its axial extent is of order
\(\lambda^{-1}\), although the velocity is transverse. Because its
third component vanishes,

\[
\nabla\cdot(V_\lambda\otimes V_\lambda)
       =(f_2(X)\eta(\lambda Z)^2,0).
\tag{2}
\]

There is no derivative of the axial envelope in (2). This is why long
axial support does not itself force weak interaction.

Take \(\zeta\ge0\) smooth, supported in \((-1/4,1/4)\), with
\(\int\zeta=1\), and use the fixed vector test

\[
g(X,Z)=(\partial_2b(X),-\partial_1b(X),0)\zeta(Z).
\]

This test is compact and divergence free. Leray self-adjointness and
commutation with heat therefore give the exact identity

\[
\begin{aligned}
&\left\langle e^{\nu c\Delta_3}\mathbb P
       \nabla\cdot(V_\lambda\otimes V_\lambda),g\right\rangle\\
&\quad=I(c)J_\lambda(c),\\
I(c)&=\int_{\mathbb R^2}(e^{\nu c\Delta_2}b)b\,dX,\\
J_\lambda(c)&=\int_{\mathbb R}\zeta(Z)
       e^{\nu c\partial_Z^2}[\eta(\lambda\,\cdot)^2](Z)\,dZ.
\end{aligned}
\tag{3}
\]

To verify the sign, integrate the first two components against
\((\partial_2b,-\partial_1b)\): the result is the pairing of their
two-dimensional curl with \(b\). Curl commutes with heat. The pressure
was removed only from this divergence-free pairing, not from the field
being estimated, and no two-dimensional replacement of \(\mathbb P\)
was made.

Fourier transformation or the heat semigroup identity gives

\[
I(c)=\|e^{\nu c\Delta_2/2}b\|_2^2>0.
\]

Strict positivity follows because \(b\ne0\) and the Gaussian Fourier
multiplier never vanishes. Continuity gives
\(\min_{c\in[1/2,1]}I(c)>0\).
For \(0<\lambda\le1\), \(\eta(\lambda Y)=1\) when
\(|Y|\le1/4\). Keeping only that part of the positive one-dimensional
heat kernel proves

\[
J_\lambda(c)\ge
\int\zeta(Z)\int_{-1/4}^{1/4}
\frac{e^{-(Z-Y)^2/(4\nu c)}}{\sqrt{4\pi\nu c}}\,dY\,dZ
\ge j_*>0
\tag{4}
\]

uniformly for \(c\in[1/2,1]\). Equations (3)–(4), followed by
\(|\langle H,g\rangle|\le\|H\|_\infty\|g\|_1\), give a uniform
positive lower bound for the rescaled operator.

Set

\[
e_\tau(x)=A\bigl(v(x_\perp/r)\eta(x_3/L),0\bigr)
         =A V_\lambda(x/r).
\]

The Euclidean heat operator and Leray projection commute with isotropic
dilation, so the resulting quadratic field is \(A^2/r\) times the
rescaled field in (3). This proves (1) on \(\mathbb R^3\).

## 3. Fixed-torus pressure and the same lower bound

For small \(\tau\), periodize \(e_\tau\) and the test \(g(x/r)\)
on the fixed torus. Their supports do not overlap their translates.
After dilation, the torus has side length \(R=2\pi/r\).
The field's axial support is \(|Z|<\lambda^{-1}\), which fits because
\(L<\pi\).

The pressure cancellation in (3) remains exact on this torus. The heat
kernel separates by coordinates, giving \(I_R(c)J_{R,\lambda}(c)\),
where each heat operator is periodic with period \(R\). In the radial
factor, both copies of \(b\) have fixed compact support. The periodic
heat kernel is the sum of the Euclidean Gaussian over translations by
\(R\mathbb Z^2\). Nonzero translations tend uniformly to zero on this
support for \(c\in[1/2,1]\): for \(|X|,|Y|\le1\), their distances
are at least \(R|k|-2\). The resulting Gaussian series is uniformly
summable and tends to zero. Therefore \(I_R\to I\) uniformly and
\(I_R\) has the same positive lower bound up to a fixed factor.

For the axial factor, the periodic heat kernel is positive and includes
the untranslated Gaussian. Keeping \(|Y|\le1/4\) proves the same
lower bound (4). The test's physical \(L^1\) norm is
\(r^3\|g\|_1\); the physical pairing is bounded below by a constant
times \((A^2/r)r^3\). Their ratio proves (1) on the fixed torus.
This argument includes the complete periodic pressure projection.

## 4. The actual heat bilinear map retains the power loss

The lower bound also survives a signed time integral; it is not merely
an obstruction involving an integral of operator norms. Fix \(t_0<T\)
and define

\[
\mathcal B(e,e)(t)=\int_{t_0}^t
 e^{\nu(t-s)\Delta}\mathbb P\nabla\cdot(e\otimes e)(s)\,ds,
\qquad
\|e\|_{X_\alpha}=\sup_{t_0<s<T}(T-s)^\alpha\|e(s)\|_\infty.
\]

Choose a nonzero smooth \(0\le q\le1\) supported in \((3/2,2)\).
For each small \(\tau\), let \(t_\tau=T-\tau\), freeze the spatial
profile at that \(\tau\), and put, with \(\sigma=T-s\),

\[
e^{[\tau]}(s,x)=\sigma^{-\alpha}q(\sigma/\tau)
                  V_{\tau^h}(x/\sqrt\tau).
\tag{5}
\]

This is a smooth time-compact solenoidal test with
\(\|e^{[\tau]}\|_{X_\alpha}\le1\). Its spatial support lies in
\(C_\sigma\) whenever it is nonzero, since \(\sigma>\tau\) and
both core dimensions increase with \(\sigma\). Its time support lies
after the fixed \(t_0\) for small \(\tau\).

Pair the output at \(t_\tau\) with \(g(x/\sqrt\tau)\).
For every contributing time,
\(c=(t_\tau-s)/\tau=\sigma/\tau-1\in(1/2,1)\).
All pairings (3) have the same positive sign, so

\[
\begin{aligned}
\tau^\alpha\|\mathcal B(e^{[\tau]},e^{[\tau]})(t_\tau)\|_\infty
&\ge c_*\tau^\alpha\tau^{-1/2}
 \int_{3\tau/2}^{2\tau}\sigma^{-2\alpha}q(\sigma/\tau)^2\,d\sigma\\
&=c_{**}\tau^{1/2-\alpha}
=c_{**}\tau^{-h}.
\end{aligned}
\tag{6}
\]

Thus the heat bilinear map has no finite bound
\(\|\mathcal B(e,e)\|_{X_\alpha}\le C\|e\|_{X_\alpha}^2\)
on this class based only on core support, amplitude and divergence
freedom. Different values of \(\tau\) give different test histories.
None is asserted to solve the actual error equation. In particular,
(6) proves neither growth of an actual error nor a lower bound for the
linearized propagator about the published reference.

## 5. A polarization class that does improve the power

There is a concrete extra assumption under which the short derivative
is compensated by a smaller transverse velocity. Fix
\(B\in C_c^\infty(\{|X|<1,|Z|<1\};\mathbb R^3)\), with
\(\nabla_{X,Z}\cdot B=0\) and \(\|B\|_\infty\le1\), and put

\[
D_\lambda=\operatorname{diag}(\lambda,\lambda,1),\qquad
e_\tau(x)=A D_\lambda B(x_\perp/r,x_3/L).
\tag{7}
\]

This is exactly solenoidal because \(\lambda/r=1/L\).
There are nonzero compact examples: take
\(B=(-\partial_Z\Psi,0,\partial_{X_1}\Psi)\) for a smooth compact
product bump \(\Psi\), then normalize. Let
\(Q=(B\cdot\nabla_{X,Z})B\). Direct differentiation gives

\[
\nabla\cdot(e_\tau\otimes e_\tau)
       =\frac{A^2}{L}D_\lambda Q(x_\perp/r,x_3/L).
\tag{8}
\]

Retain pressure by using its bounded Fourier multiplier. With
\(\widehat Q(\xi)=\int e^{-iX\cdot\xi}Q(X)dX\), anisotropic
change of variables in Fourier inversion gives, for every heat time
\(s\ge0\),

\[
\|e^{\nu s\Delta}\mathbb P\nabla\cdot(e_\tau\otimes e_\tau)\|_\infty
\le\frac{A^2}{L}(2\pi)^{-3}\|\widehat Q\|_1.
\tag{9}
\]

Indeed, the projection is evaluated at
\((\xi_1/r,\xi_2/r,\xi_3/L)\) and has norm at most one;
the heat multiplier and \(D_\lambda\) do also. The Fourier Jacobian
cancels the spatial Jacobian. Smooth compact \(Q\) has integrable
Fourier transform. On the fixed torus the same bound, with a different
fixed constant, follows by summing its Schwartz bounds on the lattice
\((rk_1,rk_2,Lk_3)\):
\(r^2L\sum_k|\widehat Q(rk_1,rk_2,Lk_3)|\) is uniformly bounded
for \(0<r,L\le1\). No \(L^\infty\)-boundedness of bare Leray
projection is assumed.

On a comparable-time interval of length of order \(\tau\), (9)
therefore has weighted scale

\[
\tau^\alpha\,\tau\,\frac{A^2}{L}
 =\tau^{\alpha+1-2\alpha-(1/2-h)}=1,
\tag{10}
\]

instead of \(\tau^{-h}\). This removes the power loss for this
fixed-profile polarization class; it does not make the bound small or
control the entire history. Uniform families require a uniform bound
on the corresponding Fourier norms of \(Q\).

## 6. A broader cylindrical class: pressure removes the leading centrifugal term

Section 5 is sufficient, not necessary. Axisymmetry permits a broader
class with large azimuthal as well as axial velocity. Allow fixed
multiples of the core dimensions, and use cylindrical coordinates
\((\varrho,\vartheta,x_3)\). Set
\(s=\varrho/r\), \(\zeta=x_3/L\). Let \(R,\Theta,W\) be fixed smooth
profiles supported in a positive-radius annulus
\(a<s<b\), \(|\zeta|<c_0\), where \(0<a<b<\infty\). Define

\[
e_\tau=A\bigl(\lambda R(s,\zeta)e_r
              +\Theta(s,\zeta)e_\theta+W(s,\zeta)e_z\bigr),
\qquad
\frac1s\partial_s(sR)+\partial_\zeta W=0.
\tag{11}
\]

The profiles do not depend on \(\vartheta\). Their physical divergence
is \(A/L\) times the expression in (11), hence vanishes exactly.
Nonzero compact examples exist: choose a compact meridional
streamfunction \(\Psi_m\) in the annulus and set
\(R=-\partial_\zeta\Psi_m/s\),
\(W=\partial_s\Psi_m/s\); the swirl profile \(\Theta\) is arbitrary
and smooth with the stated support.

The full cylindrical convection formula, including derivatives of the
basis vectors, is

\[
\begin{aligned}
N_r&=\frac{A^2}{L}\lambda(RR_s+WR_\zeta)
                 -\frac{A^2}{r}\frac{\Theta^2}{s},\\
N_\theta&=\frac{A^2}{L}
                  (R\Theta_s+W\Theta_\zeta+R\Theta/s),\\
N_z&=\frac{A^2}{L}(RW_s+WW_\zeta),
\qquad N=(e_\tau\cdot\nabla)e_\tau.
\end{aligned}
\tag{12}
\]

Thus suppressing the radial velocity has not by itself removed the
large centrifugal term. Its pressure structure is essential. Define

\[
\Psi(s,\zeta)=\int_s^\infty\frac{\Theta(q,\zeta)^2}{q}\,dq.
\tag{13}
\]

For \(s<a\), this is independent of \(s\); for \(s\ge b\), it is
zero. It is smooth across both boundaries and compact in \(\zeta\).
Consequently \(\Psi(|X|,\zeta)\) is a smooth compact function on
\(\mathbb R^2\times\mathbb R\), including the axis \(X=0\).
Its support fills the inner cylinder rather than only the annulus.
There is no singularity from the factor \(1/q\), because the integrand
vanishes near \(q=0\).

Direct differentiation gives the global identity

\[
-\frac{A^2}{r}\frac{\Theta^2}{s}e_r
=\nabla_x[A^2\Psi(\varrho/r,x_3/L)]
 -\frac{A^2}{L}\Psi_\zeta(s,\zeta)e_z.
\tag{14}
\]

The first term is a genuine smooth compact scalar gradient. Let

\[
\begin{aligned}
Q_\lambda(X,\zeta)={}&
\lambda(RR_s+WR_\zeta)e_r\\
&+(R\Theta_s+W\Theta_\zeta+R\Theta/s)e_\theta\\
&+(RW_s+WW_\zeta-\Psi_\zeta)e_z,
\qquad s=|X|.
\end{aligned}
\]

The first two components vanish near the axis; the last is smooth there
by the radial constancy just proved. Thus \(Q_\lambda\) is a uniformly
smooth compact family for \(0<\lambda\le1\). Equations (12)–(14) give

\[
\mathbb P N=\frac{A^2}{L}\mathbb P
 Q_\lambda(x_\perp/r,x_3/L).
\tag{15}
\]

This keeps the entire remaining pressure projection. The primitive
\(\Psi\) extracts one gradient; it need not equal the whole pressure
potential of \(N\).

As in Section 5, Fourier inversion proves

\[
\|e^{\nu t\Delta}\mathbb P N\|_\infty
\le C\frac{A^2}{L},\qquad t\ge0,
\tag{16}
\]

because \(Q_\lambda=Q_0+\lambda Q_1\) for two fixed smooth compact
Cartesian vector fields, so
\(\sup_{0<\lambda\le1}\|\widehat Q_\lambda\|_1<\infty\).
The anisotropic Fourier Jacobians cancel and the full Leray multiplier
has Euclidean operator norm at most one. On the fixed torus, periodize
the compact scalar in (14) as well as the fields; for small \(\tau\)
all supports fit inside a fundamental cube, so the same gradient identity
holds globally. The remaining Fourier series is bounded uniformly by
Schwartz decay. Explicitly, each factor in a product majorant obeys
\(a\sum_{k\in\mathbb Z}(1+a|k|)^{-2}\le3\) for \(0<a\le1\);
use \(a=r,r,L\) in the three directions. This proves (16) on the torus
without assuming boundedness of Leray projection on arbitrary
\(L^\infty\) fields.

The comparable-time weighted cost is again order one, as in (10).
This broader class needs axisymmetry, small radial velocity, controlled
axial derivatives and the stated uniform profile bounds. Support and
component amplitudes alone do not imply those hypotheses.

### The centrifugal symbol and its component ratios

The [external source extraction](external-modulation-source.md)
identifies a negative centrifugal discriminant at a fixed exterior
similarity radius \(X_e\). Write

\[
d_e=h+\zeta_e H'(\zeta_e)/H(\zeta_e)\in(0,h),\qquad
\zeta_e=2/X_e,\qquad
\Omega=C_e\tau^{-1-h}>0.
\]

Here \(d_e\) is a fixed positive number, independent of \(\tau\).
For the frozen axisymmetric symbol, set
\(k=(k_r,0,k_z)\ne0\),
\(\chi=k_z/|k|\), \(\rho=k_r/|k|\), and write
\((u_r,u_z)=w(\chi,-\rho)\).
With the Fourier convention \(e^{ik\cdot x}\), the pressure amplitude is

\[
p_k=-\frac{2i\Omega k_r}{|k|^2}u_\theta.
\]

Indeed the radial equation is
\((\partial_t+\nu|k|^2)u_r=2\Omega u_\theta-ik_rp_k\),
the axial equation is
\((\partial_t+\nu|k|^2)u_z=-ik_zp_k\), and their divergence vanishes.
Thus pressure reduces the radial coupling to
\(2\Omega\chi^2u_\theta\). The remaining two-component system is

\[
(\partial_t+\nu|k|^2)
\begin{pmatrix}w\\u_\theta\end{pmatrix}
=\begin{pmatrix}0&2\Omega\chi\\2d_e\Omega\chi&0\end{pmatrix}
\begin{pmatrix}w\\u_\theta\end{pmatrix}.
\tag{17}
\]

For \(\chi\ne0\), put \(\mu=2\Omega\sqrt{d_e}|\chi|\).
The plus-branch eigenvalue is \(-\nu|k|^2+\mu\), with polarization

\[
(u_r,u_\theta,u_z)
=w\bigl(\chi,\operatorname{sgn}(\chi)\sqrt{d_e},-\rho\bigr).
\tag{18}
\]

When \(\rho\ne0\), the transverse-to-axial amplitude ratio is
\(\sqrt{\chi^2+d_e}/|\rho|\ge\sqrt{d_e}\). A mode with nonvanishing
normalized amplitude therefore does not fit Section 5's requirement
that both transverse components be smaller by \(\lambda\to0\).
This excludes that sufficient class, not every useful anisotropic class.

For the natural anisotropic covectors
\(k_r=m_r/r\), \(k_z=m_z/L\), with fixed nonzero \(m_r,m_z\),

\[
\frac{|u_r|}{|u_z|}=\left|\frac{m_z}{m_r}\right|\lambda,
\qquad
\frac{|u_\theta|}{|u_z|}=\frac{\sqrt{d_e}}{|\rho|}\asymp1.
\tag{19}
\]

These ratios are compatible with the broader class (11). They do not
construct a compact profile or prove bounds for its derivatives.
Here \(\mu\asymp\tau^{-1}\), rather than \(\tau^{-1-h}\);
positive net growth would require comparing its coefficient with
\(\nu|k|^2\asymp\tau^{-1}\). It does not follow automatically from
taking \(\tau\) smaller.

The frozen evolution distinguishes the two classes even before selecting
an eigenvector. Starting with \(w(0)=w_0\), \(u_\theta(0)=0\), at
elapsed frozen time \(\delta\ge0\) one has

\[
\begin{aligned}
w(\delta)&=e^{-\nu|k|^2\delta}w_0\cosh(\mu\delta),\\
u_\theta(\delta)&=e^{-\nu|k|^2\delta}
 \operatorname{sgn}(\chi)\sqrt{d_e}\,w_0\sinh(\mu\delta).
\end{aligned}
\]

The ratio \(u_r/u_z=-\chi/\rho\) stays fixed. Hence the small radial
component is preserved by this frozen coupling when \(\chi/\rho\)
is of order \(\lambda\). Swirl of the same order as the meridional
amplitude is generated when \(\mu\delta\) is of order one, violating
Section 5's stronger transverse suppression but not (11)'s component
ordering. The scalar viscous factor cancels from these ratios.

For a fixed nonzero ratio \(|\chi|\), the plus eigenvector
instead has order-one radial velocity and fails (11)'s radial condition.
Even an initially pure swirl mode develops such a radial component:
its ratio is
\(|u_r/u_\theta|=|\chi|\tanh(\mu\delta)/\sqrt{d_e}\).
Thus a condition on radial amplitude alone is not invariant under all
frozen covectors. Moreover, a fixed-angle mode at \(|k|\asymp r^{-1}\)
has axial frequency of order \(r^{-1}\), already inconsistent with
uniform fixed-profile axial derivative bounds at scale \(L\).
When \(\chi=0\), this particular centrifugal coupling vanishes.

These are statements about the frozen symbol. Coefficient variation,
cylindrical divergence and viscosity corrections, localization, and the
actual projected force response have not been estimated here. Neither
the compatibility in (19) nor the exact nonlinear cancellation (14)
proves that the full reference propagator preserves the broader class,
or that the actual force-removal error lies in it.

## 7. Consequence for the next estimate

The long axial scale helps when the error's polarization or other
structure makes its effective projected interaction long as well.
The lower construction has order-one transverse velocity and exhibits
the short derivative \(r^{-1}\). The class (7) suppresses transverse
velocity by \(r/L\), and its complete nonlinear source instead costs
\(L^{-1}\), with pressure included. The cylindrical class in Section 6
also allows large swirl: its leading centrifugal term is an exact gradient,
and the retained axial pressure correction costs \(L^{-1}\).

For force removal, the unresolved step is a proof that the **actual**
error, its forcing response and the full linearized propagator preserve
an appropriate structure or a different useful norm. Core localization
alone does not supply it. Neither the lower test nor the special upper
bound estimates that actual propagator, proves a new unforced trajectory,
or excludes every possible force-removal argument.

Two independent AI-agent reviews passed at the stated written scope.
The coordinating agent checked Sections 3–6, including the fixed-torus
lower bound, the signed Duhamel obstruction, both restricted upper bounds
and the complete centrifugal comparison. A peer agent independently
checked the compact-profile algebra, positive test pairing and scaling,
and then the new cylindrical convection, pressure primitive and axial
sign, smooth filled-cylinder extension, Fourier/lattice bounds, pressure
amplitude, eigenvector and frozen evolution ratios. Both reviews retain
the absence of an actual-error invariance or source-excitation theorem.
No formal certificate, external expert acceptance or numerical-flow
evidence is asserted.
