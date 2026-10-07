# A localized quasimode in the actual heat exterior

8 September 2026. Restricted written analysis; two independent agent reviews
passed at the stated scope.
The construction below uses the actual smooth periodic reference at each
late time. It retains the full Leray projection and ordinary viscosity.
It supplies an approximate eigenpair and a lower bound on an operator norm
of the actual time-dependent linearization. It does not identify an
eigenmode, prove growth of one specified packet, show force excitation,
or produce an unforced Navier–Stokes singularity.

The actual-source inputs are pinned in
[the exterior and modulation source note](external-modulation-source.md),
for [OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
Use its viscosity-one, terminal-time-one normalization. We retain the
symbol \(\nu\) in the algebra and estimates to expose the viscous costs;
for this actual reference it is set to \(\nu=1\).
The torus is the actual source's unit torus \(\mathbb R^3/\mathbb Z^3\);
no \(2\pi\) spatial rescaling is made. For small \(\tau\), the entire
tube lies in the interior of its coordinate cube
\((-1/2,1/2)^3\). The cylindrical angular variable still runs through
\(2\pi\), as usual for a Euclidean circle inside that chart.

## 1. A fixed spatial tube inside the exact exterior

Fix the source's \(0<h<1/100\), put \(D=1/2-h\), and choose
\(X_e>X_{\rm ext}\). Choose fixed \(\rho\in(0,1)\) small enough that
\[
L=\frac{X_e(1-\rho)^2}{X_{\rm ext}}>1.
\]
At \(t_0=1-\tau\), define
\[
r_0=\sqrt{2X_e\tau},\qquad
c_z=\sqrt{L-1}\,L^{-h},\qquad
\mathcal T_\tau=
\{(r,\theta,z):(1-\rho)r_0<r<(1+\rho)r_0,\ |z|<c_z\tau^D\}.
\tag{1}
\]
For sufficiently small \(\tau>0\), the complete reference equals the
uncut heat swirl on this tube, and remains equal there for
\(t_0\le t<1\). The localization and late time cutoffs are one.

Here is the source-coordinate check. Its equations give
\[
q-z^2q^{2h}=1-t,\qquad X=\frac{r^2}{2q}.
\]
At \(t=t_0\), substituting \(Q=L\tau\) in the left side gives a value
strictly larger than \(\tau\) when \(|z|<c_z\tau^D\).
Also \(Q>|z|^{1/D}\). On \(q\ge |z|^{1/D}\) the derivative is
\(1-2h\eta^2\ge1-2h>0\); hence the actual root satisfies \(q<Q\).
It follows that \(X>X_{\rm ext}\) throughout (1).
For fixed \(r,z\),
\[
q_t=-\frac1{1-2h\eta^2}<0,
\]
so \(X\) subsequently increases. This proves persistence of the fixed
tube in the exterior. Its dimensions tend to zero, so it lies in the
spatial cutoff plateau for all sufficiently small \(\tau\).

On this tube the full velocity and pressure are exactly
\[
U(t,x)=K(r,t)e_\theta,\qquad
K(r,t)=\kappa r^{-1-2h}H\!\left(\frac{4(1-t)}{r^2}\right),
\qquad P_r=K^2/r,\quad P_z=0,
\tag{2}
\]
and \(K_t=\nu(K_{rr}+r^{-1}K_r-r^{-2}K)\).
In particular the complete physical force is zero there.
No annular oscillatory component remains on this support.

Set
\[
\Omega=K/r,\quad B=K_r+K/r,\quad
g(\zeta)=h+\zeta H'(\zeta)/H(\zeta).
\]
The source proves \(H>0\) and \(g>0\) for \(\zeta>0\), so
\(B=-2g\Omega\). At \((r_0,t_0)\), let
\[
\Omega_0=\Omega(r_0,t_0)>0,\quad B_0=B(r_0,t_0)<0,\quad
\gamma=\sqrt{-2\Omega_0B_0}=2\Omega_0\sqrt{g(2/X_e)}.
\tag{3}
\]
All profile choices are fixed before \(\tau\downarrow0\). Thus
\(\gamma=c_\gamma\tau^{-1-h}\), with \(c_\gamma>0\) independent of
\(\tau\). On a smaller tube and for \(0\le t-t_0\le\tau/2\),
the explicit heat profile gives, for every fixed \(m,n\),
\[
|\partial_r^m\partial_t^n(\Omega,B)|
\le C_{mn}\gamma r_0^{-m}\tau^{-n}.
\tag{4}
\]
Its axial derivatives vanish. These are local heat-profile estimates,
not bounds on derivatives of the reference everywhere.

## 2. Operator, domain and packet scales

Let \(\mathcal H\) be the mean-zero, divergence-free subspace of
\(L^2(\mathbb T^3;\mathbb C^3)\), using ordinary volume measure.
The full linearized operator is
\[
\mathcal A(t)v=\nu\Delta v
-\mathbb P\big((U(t)\cdot\nabla)v+(v\cdot\nabla)U(t)\big),
\qquad D(\mathcal A(t))=H^2\cap\mathcal H.
\tag{5}
\]
At each fixed preterminal time the reference is smooth on the whole
torus. Its first-order terms are relatively bounded with arbitrarily
small relative bound with respect to the Laplacian. The frozen operator
therefore generates the usual analytic semigroup. Smooth time-dependent
coefficients give the linear evolution family on each compact
preterminal interval. Ordinary energy estimates ensure a finite bound
on that interval; no bound uniform in \(\tau\) is assumed here.

Choose exponents and scales
\[
0<a<b<h/2,\qquad
\ell=\tau^{1/2+a},\qquad k=\tau^{-1/2-b}.
\tag{6}
\]
Then \(\ell/r_0=O(\tau^a)\), \(k\ell=\tau^{a-b}\to\infty\),
and \(\nu k^2/\gamma=O(\tau^{h-2b})\to0\).
Thus the radial envelope is small compared with the swirl radius but
large compared with the axial wavelength. Also
\(\ell/\tau^D=\tau^{a+h}\to0\), so axial localization fits (1).

Fix nonzero real smooth bumps \(\eta_r,\eta_z\), supported in
\((-1,1)\), and set
\[
\chi(r,z)=\eta_r((r-r_0)/\ell)\eta_z(z/\ell),\qquad
H_k=\chi e^{ikz},\quad J=\frac{\partial_zH_k}{ik}.
\]
The carrier \(k\) need not be an integer: the entire field is supported
inside one coordinate chart and extended by zero before periodization.
All derivatives vanish at the chart boundary. Integer rounding would
also preserve the scale estimates.

Choose real \(R=1\) and \(T=\gamma/(2\Omega_0)\), so
\[
\gamma R=2\Omega_0T,\qquad \gamma T=-B_0R.
\]
Define the complete perturbation by
\[
\begin{aligned}
\psi&=-\frac{R}{ik}\chi e^{ikz},\\
v_{\rm mer}&=\nabla\times(\psi e_\theta),\qquad
v_\theta=T\chi e^{ikz},\\
v_r&=R\left(\chi+\frac{\chi_z}{ik}\right)e^{ikz},\qquad
v_z=Z=-\frac{R}{ik}\left(\chi_r+\frac{\chi}{r}\right)e^{ikz}.
\end{aligned}
\tag{7}
\]
Here \(\chi_r,\chi_z\) denote \(\partial_r\chi,\partial_z\chi\).
Formula (7) retains the radial
\(1/r\) curl correction.

This is an exactly divergence-free smooth periodic field. Its support
is away from the axis, so the cylindrical vector potential is smooth.
Its meridional part has zero mean as a periodic curl. Its azimuthal
part has zero mean because integration of \(e_\theta\) over the full
circle vanishes. Therefore \(v\in D(\mathcal A(t_0))\).

## 3. Norm and exact unprojected residual

Since \(\chi\) is real, its \(1/(ik)\) corrections are in quadrature
with the leading term. Orthogonality of the cylindrical basis gives
the exact norm identity
\[
\|v\|_2^2=(R^2+T^2)\|\chi\|_2^2+
\frac{R^2}{k^2}
\left(\|\partial_z\chi\|_2^2+
\|(\partial_r+r^{-1})\chi\|_2^2\right).
\tag{8}
\]
Integration uses \(dx=r\,dr\,d\theta\,dz\). On the support \(r\asymp r_0\);
hence
\[
\|\chi\|_2\asymp\sqrt{r_0}\,\ell,\qquad
\|v\|_2\asymp\sqrt{r_0}\,\ell.
\tag{9}
\]
Constants can depend on the fixed source and bumps but not on \(\tau\).
Normalize \(v\) by its exact \(L^2\) norm at the end.

Take
\[
\lambda=\gamma-\nu k^2>0
\tag{10}
\]
for all sufficiently small \(\tau\). Let
\[
\Delta_c=\partial_r^2+r^{-1}\partial_r+\partial_z^2,\qquad
\mathcal L_k=\Delta_c-r^{-2}+k^2,\quad
\mathcal M_k=\Delta_c+k^2.
\]
Use zero approximate perturbation pressure and form
\[
\mathcal R_{\rm raw}
=\lambda v-\nu\Delta v+
(U(t_0)\cdot\nabla)v+(v\cdot\nabla)U(t_0).
\]
The full cylindrical transport terms are
\(-2\Omega v_\theta\) in the radial component, \(Bv_r\) in the
azimuthal component, and zero in the axial component. The vector
Laplacian has the additional \(-r^{-2}\) term in both radial and
azimuthal components. Consequently the residual components are exactly
\[
\begin{aligned}
(\mathcal R_{\rm raw})_r
 &=2T[(\Omega_0-\Omega)H_k+\Omega_0(J-H_k)]
       -\nu R\mathcal L_kJ,\\
(\mathcal R_{\rm raw})_\theta
 &=R[(B-B_0)H_k+B(J-H_k)]-\nu T\mathcal L_kH_k,\\
(\mathcal R_{\rm raw})_z
 &=\gamma Z-\nu\mathcal M_kZ.
\end{aligned}
\tag{11}
\]
This includes all curvature and curl terms. Basis rotation is the
reason the first coupling is \(2\Omega\), not \(\Omega\).

The **actual full-pressure residual** is
\[
(\lambda-\mathcal A(t_0))v=\mathbb P\mathcal R_{\rm raw},
\qquad
\|(\lambda-\mathcal A(t_0))v\|_2\le\|\mathcal R_{\rm raw}\|_2.
\tag{12}
\]
The last step uses the orthogonal \(L^2\) projection, not locality of
pressure. It includes the entire pressure tail outside the tube.
No coefficient outside the support enters the raw residual, because
all local derivatives of \(v\) vanish there.

## 4. Quantitative quasimode estimate

Scaled bump derivatives and (4) give
\[
\begin{aligned}
\|J-H_k\|_2+\|Z\|_2
 &\le C(k\ell)^{-1}\|v\|_2,\\
\|(\Omega-\Omega_0)H_k\|_2+
\|(B-B_0)H_k\|_2
 &\le C\gamma(\ell/r_0)\|v\|_2.
\end{aligned}
\]
The harmless fixed eigenvector constants are included in \(C\).
For example,
\[
(\Delta_c+k^2)(\chi e^{ikz})
=e^{ikz}(\chi_{rr}+r^{-1}\chi_r+\chi_{zz}+2ik\chi_z).
\]
Thus the remaining viscous terms in (11) are bounded by
\[
C\nu(\ell^{-2}+k/\ell+r_0^{-2})\|v\|_2.
\]
Applying these estimates to (11)–(12) yields
\[
\frac{\|(\lambda-\mathcal A(t_0))v\|_2}{\gamma\|v\|_2}
\le C\left[
\tau^a+\tau^{b-a}+
\tau^{h-a-b}+\tau^{h-2a}+\tau^h\right].
\tag{13}
\]
All exponents are positive under (6).
The separate eigenvalue shift \(\nu k^2/\gamma\) has exponent \(h-2b\).

In particular choose
\[
\boxed{\ a=h/8,\qquad b=h/4.\ }
\]
For an exactly normalized packet \(v_\tau\),
\[
\boxed{\
\|v_\tau\|_2=1,\quad
\lambda_\tau=c_\gamma\tau^{-1-h}
 (1+O(\tau^{h/2})),\quad
\|(\lambda_\tau-\mathcal A(t_0))v_\tau\|_2
\le C\tau^{h/8}\lambda_\tau.\ }
\tag{14}
\]
The correction in \(\lambda_\tau\) is negative:
\(\lambda_\tau=\gamma-\nu k^2\).
These are approximate eigenpairs of the **actual full frozen generator**,
not just of its local symbol.

The construction may be made real. At least one of the real and
imaginary parts has norm at least \(\|v\|_2/\sqrt2\); take it and
renormalize. Since the operator is real, (14) changes only its constant.
Alternatively its real and complex Hilbert-space operator norms agree.

Equation (14) implies a positive actual initial energy derivative:
\[
\operatorname{Re}\langle v_\tau,\mathcal A(t_0)v_\tau\rangle
\ge\lambda_\tau(1-C\tau^{h/8})>0.
\tag{15}
\]
For the actual time-dependent linearized solution started at this packet,
the derivative of its squared \(L^2\) norm at \(t_0\) is twice (15).
This alone does not prove several e-folds of growth of that packet.

## 5. A frozen semigroup consequence without spectral assumptions

For any \(C_0\) semigroup \(S(t)\), a unit vector in the generator domain
with \(\|(\lambda-\mathcal A)v\|\le\epsilon\lambda\), \(\lambda>0\),
satisfies
\[
e^{\lambda t}v-S(t)v
=\int_0^t e^{\lambda s}S(t-s)(\lambda-\mathcal A)v\,ds.
\]
Writing \(M(t)=\sup_{0\le s\le t}\|S(s)\|\), the triangle inequality gives
\[
\boxed{\ M(t)\ge
\frac{e^{\lambda t}}{1+\epsilon(e^{\lambda t}-1)}.\ }
\tag{16}
\]
At \(t=\lambda^{-1}\log(1/\epsilon)\), for \(0<\epsilon<1\),
\[
M(t)\ge\frac1{\epsilon(2-\epsilon)}.
\]
This does not require a global semigroup upper bound, an eigenvalue or
normality. The amplified direction need not be \(v\).
The connection between approximate eigenvectors and transient growth
belongs to classical pseudospectral analysis; see Trefethen, Trefethen,
Reddy and Driscoll,
[Hydrodynamic stability without eigenvalues](https://people.maths.ox.ac.uk/trefethen/ttrd.pdf).
The derivation used here is displayed in full.

## 6. The actual time-dependent propagator: a weaker but rigorous lower bound

Keep the packet and \(\lambda_\tau\) fixed, and set
\[
y(t)=e^{\lambda_\tau(t-t_0)}v_\tau.
\]
On a late interval of length \(\Delta\le\tau/2\), (11) remains the
exact raw residual formula with \(\Omega(r,t),B(r,t)\).
No derivative of a time-dependent packet is being hidden.
The only additional coefficient error is, by (4),
\[
\|y'-\mathcal A(t)y\|_2
\le C\gamma\left(\tau^{h/8}+\frac{t-t_0}{\tau}\right)
e^{\lambda_\tau(t-t_0)}.
\tag{17}
\]
Crucially, the axisymmetric transport terms still reduce exactly to
\(-2\Omega v_\theta,Bv_r\). A crude Cartesian bound charging a large
carrier derivative to \(U_\theta\cdot\nabla v\) would lose that identity.

Choose one fixed sufficiently large \(C_0\), and define
\[
\epsilon_\tau=C_0\tau^{h/8}<1/2,\qquad
\Delta_\tau=\lambda_\tau^{-1}\log(1/\epsilon_\tau),\qquad
t_1=t_0+\Delta_\tau.
\tag{18}
\]
Then
\[
\Delta_\tau/\tau=O(\tau^h\log(1/\tau))=o(\tau^{h/8}).
\]
For sufficiently small \(\tau\), (17) therefore implies the uniform bound
\[
\|y'-\mathcal A(t)y\|_2
\le\epsilon_\tau\lambda_\tau
 e^{\lambda_\tau(t-t_0)},\qquad t_0\le t\le t_1.
\tag{19}
\]

Let \(\mathcal S_U(t,s)\) denote the actual full linearized evolution.
Duhamel's formula at \(t_1\) and (19), with
\[
M_\tau=\sup_{t_0\le s\le t_1}
\|\mathcal S_U(t_1,s)\|_{\mathcal H\to\mathcal H},
\]
give
\[
e^{\lambda_\tau\Delta_\tau}
\le M_\tau\left[1+\epsilon_\tau
(e^{\lambda_\tau\Delta_\tau}-1)\right].
\]
Consequently,
\[
\boxed{\ M_\tau\ge
\frac1{\epsilon_\tau(2-\epsilon_\tau)}
\ge c\tau^{-h/8}.\ }
\tag{20}
\]
This is a lower bound for the **actual time-dependent** operator family,
although its restart time and amplified direction are not identified.
No estimate transporting the chosen packet with small error is needed
for this weaker conclusion.

For all \(s\in[t_0,t_1]\),
\[
1\le\frac{1-s}{1-t_1}\le
\frac{\tau}{\tau-\Delta_\tau}\longrightarrow1.
\]
Thus (20) excludes a uniform bound
\[
\|\mathcal S_U(t,s)\|_{\mathcal H\to\mathcal H}
\le C\left(\frac{1-s}{1-t}\right)^\beta
\tag{21}
\]
with fixed finite \(C,\beta\ge0\), valid for every sufficiently late
restart and every mean-zero divergence-free \(L^2\) input.
It does not exclude a bound on one particular source response or on a
smaller controlled class of errors.

## 7. Why exact transport of this packet still needs an upper bound

If \(w(t)=\mathcal S_U(t,t_0)v_\tau\), its error from \(y(t)\) is
the propagated residual in (19). An energy repair can use
\[
M_{\rm en}(\tau)=\int_{t_0}^{t_1}
\|\max(0,\lambda_{\max}(-S(U(t))))\|_\infty\,dt.
\]
For a fixed number \(N\) of e-folds, \(\Delta=N/\lambda_\tau\), the
residual calculation gives, for example,
\[
\frac{\|w(t_0+\Delta)-y(t_0+\Delta)\|_2}{e^N}
\le C e^{M_{\rm en}(\tau)}
 \left(N\tau^{h/8}+N^2\tau^h\right).
\tag{22}
\]
A sufficient repair condition is that the right side tend to zero.
Uniform boundedness of \(M_{\rm en}\) would suffice. A logarithmic
bound with coefficient strictly less than \(h/8\) would also suffice
for fixed \(N\). These are upper-bound conditions; they are not supplied
by the local exterior identities.

The complete field outside the packet contains annular corrections with
their own derivative costs. The source's conservative jet estimates do
not provide (22)'s required smallness. If all one has is
\(\|\nabla U\|_\infty\le C\tau^{-p}\) with \(p>1+h\), its resulting
clock on this interval is \(O(\tau^{1+h-p})\), and exponentiating that
upper estimate does not close the repair. This does not prove that the
actual clock or propagator is that large.

Pressure projection can send the small residual outside the packet
immediately. There those global coefficients can enter its subsequent
evolution. Purely local heat coefficients are therefore enough for the
quasimode and the Duhamel lower bound (20), but not by themselves for a
small-error repair of this specified packet.

## 8. Exact direct-source orthogonality and the remaining forcing question

The complete physical force vanishes on \(\mathcal T_\tau\) during
the interval used above, because the velocity and pressure there solve
the exact unforced heat-swirl equations and all localization cutoffs are
one. The compact solenoidal packet consequently satisfies
\[
\boxed{\
\langle\mathbb P f(t),v_\tau\rangle
=\langle f(t),v_\tau\rangle=0,\qquad t_0\le t\le t_1.\ }
\tag{23}
\]
The same holds for its scalar multiple \(y(t)\).
This uses global self-adjointness of Leray and compact support of the
test, not pointwise vanishing of \(\mathbb P f\).

Therefore a nonzero projected terminal force elsewhere, together with
(20), does not establish excitation of this channel. A force-response
pairing at the endpoint uses an adjoint-evolved test, which may lose
support and has not been estimated here. Equation (23) gives no invariant
decoupling theorem.

The new results are the full frozen-generator quasimode, positive initial
linearized energy derivative, and nonuniform actual propagator norm.
The next distinct task is a signed full-force response estimate, or a
structured error estimate that survives the observed amplification.
None of these results removes the external force or changes unforced
ROOT's status.


## 9. Verification and scope of review

The integration reviewer independently read the full argument and checked the source
coordinate inversion, persistent tube, heat derivative estimates, exact
curl construction and mean, pressure-bearing residual, viscous powers,
and both Duhamel bounds. A second agent, Avicenna, independently read the
complete note and passed those steps, the real-subspace argument, the
time-ratio exclusion, and the direct-source orthogonality. Avicenna also
checked the exact divergence and all three residual components by symbolic
substitution for an arbitrary smooth envelope. The complete cylindrical
residual identities are also included in the reproducible
[exact symbolic controls](checks/check-force-removal.py);
the integration reviewer reports all 39 checks and negative controls passing.

These are reviews of the written argument, not a formal proof certificate.
No numerical fluid simulation or spectrum computation was used. The
reviewed conclusions are precisely (13), (14), (16), (20), and (23), with
the stated mean-zero space, actual reference, and short late windows.
The amplified direction and restart time in (20) remain unspecified;
force excitation, nonlinear persistence, and force removal remain open.
