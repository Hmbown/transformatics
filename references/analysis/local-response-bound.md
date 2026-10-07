# A complete local response bound in an exterior frequency band

8 September 2026. Restricted written proof, independently reviewed at the
scope recorded below. This estimates a complete linear forcing response, rather than its
finite Taylor coefficients. Its conclusion concerns the pairing with the
specified exterior packet. It is not a bound on the whole response norm,
a nonlinear force-removal theorem, or an unforced singularity result.

The actual reference is the same unit-torus, viscosity-one construction as
in the [exterior quasimode](exterior-quasimode.md) and
[first force coupling](exterior-force-coupling.md), from
[OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The global source estimate used in the final specialization is
[the global strain-cost lemma](global-strain-cost.md).
The local estimate below first states all dependence on global norms
explicitly, so that this input remains separately checkable.

## 1. Statement and scales

Let \(t_0=1-\tau\), \(R=r_0=\sqrt{2X_e\tau}\), and use the fixed
source-free tube of the quasimode note. On it the complete velocity is
\(U=K(r,t)e_\theta\), independently of the axial coordinate \(z\),
throughout \([t_0,t_0+\tau/2]\). Write
\[
\Omega=K/r,\qquad B=K_r+K/r,\qquad
|\Omega|+|B|\le C\gamma,\qquad \gamma=c_\gamma\tau^{-1-h}.
\tag{1}
\]
Fix a time length \(0<d\le\tau/2\). The exact response is
\[
e_t=\mathcal A(t)e+\mathbb P_{\mathbb T^3}f,
\qquad e(t_0)=0,
\qquad
\mathcal A e=\nu\Delta e-
\mathbb P_{\mathbb T^3}\big((U\cdot\nabla)e+(e\cdot\nabla)U\big).
\tag{2}
\]
All norms of \(e,U,f\) below refer to this complete periodic equation.
In particular pressure from outside the tube is retained.

Choose the axial packet bump to be a fixed compactly supported Gevrey-2
function: \(\|\eta_z^{(m)}\|_\infty\le C_0^{m+1}(m!)^2\).
For example, a fixed multiple of \(\exp[-1/(1-z^2)]\) on \(|z|<1\),
extended by zero, has this property. This is a permitted choice among
the smooth packet bumps in the quasimode construction; it changes the
test, not the reference or force. Keep its complete solenoidal packet,
including both curl corrections, and normalize it to \(\|v_\tau\|_2=1\).
Let its envelope size be \(\ell\), carrier frequency \(k>0\), with
\(\ell/R\to0\) and \(k\ell\to\infty\).

Put, with suprema over \([t_0,t_0+d]\),
\[
E_j=\sup\|e(t)\|_{H^j},\qquad
F_j=\sup\|f(t)\|_{H^j},\qquad
A_j=1+\sup\|U(t)\|_{W^{j,\infty}},
\]
\[
G=C R^{-6}\big[(1+\nu+\gamma+A_2)E_3+F_1\big].
\tag{3}
\]
Here and below constants may depend on the fixed source profile,
relative cylinder widths and packet bumps, but not on \(\tau,k,d\).
For sufficiently small \(\ell/R\) and sufficiently large \(k\ell\),
we prove
\[
\boxed{\quad
\sup_{t_0\le t\le t_0+d}|\langle e(t),v_\tau\rangle|
\le C R^{-3}E_1 e^{-c\sqrt{k\ell}}
 +C dG\exp\!\big(C(\gamma+\nu k^2)d-c\sqrt{kR}\big).
\quad}
\tag{4}
\]
The inner product is complex Hermitian, linear in its first argument.
The deliberately loose fixed powers of \(R^{-1}\) in (3)–(4) pay for
localization; no power depending on the oscillatory differentiation
order is hidden there. Estimate (4) also applies to input \(-\mathbb Pf\).

## 2. An exact auxiliary equation with remote forcing

Take three fixed nested annular cylinders of radial and axial widths
comparable to \(R\), contained in the source-free tube. Their separation
is \(cR\), and the packet is inside the innermost one. All are inside
one Euclidean chart of the unit torus.

Average the actual response over rotations about the local axis, rotating
the vector components along with the argument, and call the result \(a\).
This operation is used only on these cylinders. It does not assert that
rotations are global symmetries of the torus. It preserves divergence,
does not increase local Cartesian Sobolev norms, and leaves pairing with
the axisymmetric packet unchanged.

Set
\[
\phi=\Delta_{\mathbb T^3}^{-1}\operatorname{div}f,\qquad
\pi=-\Delta_{\mathbb T^3}^{-1}\operatorname{div}
 \big((U\cdot\nabla)e+(e\cdot\nabla)U\big).
\]
On the tube \(\mathbb Pf=-\nabla\phi\). Averaging the physical equation,
including these pressures, therefore gives
\[
a_t-\nu\Delta a-Ma+\nabla p=0,\qquad \operatorname{div}a=0,
\quad p=\overline{\pi+\phi},
\]
\[
Ma=2\Omega a_\theta e_r-Ba_r e_\theta.
\tag{5}
\]
The Laplacian is the Cartesian vector Laplacian; its cylindrical radial
and angular components include \(-r^{-2}\). The two terms from
\(U\cdot\nabla\) and \(a\cdot\nabla U\) have become exactly the
zeroth-order matrix in (5). No radial or axial advection has been dropped.

There is a compact axisymmetric solenoidal extension \(v\) of \(a\)
to \(\mathbb R^3\), agreeing on the middle cylinder. To make this
explicit, choose a local meridional streamfunction \(\psi\) with
\[
\psi_r=ra_z,\qquad \psi_z=-ra_r.
\]
It exists on the meridional rectangle by incompressibility. One formula
is
\[
\psi(r,z)=\int_{r_c}^r s a_z(s,z)\,ds
-r_c\int_{z_c}^z a_r(r_c,\zeta)\,d\zeta.
\tag{6}
\]
For a fixed cutoff \(\chi\), supported in the outer cylinder and equal
to one on the middle cylinder, set
\[
v=\operatorname{curl}\big(\chi\psi e_\theta/r\big)
 +\chi a_\theta e_\theta.
\tag{7}
\]
Both terms are divergence-free; the second is an axisymmetric pure
swirl. The extension vanishes near the axis and hence is globally smooth.
It has \(v(t_0)=0\). Extend \(p\) by a compact cutoff equal to one on
the middle cylinder, calling the extension \(p_c\).

Extend \(\Omega,B\) radially to smooth functions vanishing outside a
slightly larger annulus, with size at most \(C\gamma\). The resulting
matrix \(M(x_\perp,t)\) is bounded on \(\mathbb R^3\), remains exactly
independent of \(z\), and equals (5)'s matrix on the middle cylinder.
Define the actual auxiliary residual
\[
g=v_t-\nu\Delta v-Mv+\nabla p_c.
\tag{8}
\]
It is zero on the middle cylinder. Thus its support is at Euclidean
distance at least \(cR\) from the packet support \(S\).
Projecting (8) on \(\mathbb R^3\) gives the exact identity
\[
v_t=\nu\Delta v+\mathbb P_{\mathbb R^3}(Mv)
 +\mathbb P_{\mathbb R^3}g,
\qquad v(t_0)=0.
\tag{9}
\]
This is an auxiliary representation of the actual local response.
Replacing the torus projection by a Euclidean one in (2) would be wrong;
here the actual torus pressure is already present in (8). Its effects
are included in \(g\), rather than declared absent.

For clarity, only fixed low norms are needed to bound this residual.
Rescale the meridional rectangle by \(R\) in (6). The trace on
\(r=r_c\) is bounded by its fixed-domain \(H^1\) norm. Formula (7),
its two spatial derivatives, and its time derivative then give the
safe bounds, for \(R<1\),
\[
\|v\|_2\le C R^{-3}\|e\|_{H^1},
\]
\[
\|g\|_2\le C R^{-6}\big[
(1+\nu+\gamma)\|e\|_{H^3}
+\|e_t\|_{H^1}+\|\pi+\phi\|_{H^1}\big].
\tag{10}
\]
These bounds allow more powers than are necessary: each cutoff derivative
costs \(R^{-1}\), the factor \(1/r\) and its differentiated versions
are controlled because \(r\asymp R\), and the streamfunction integral
and one trace require only the displayed fixed Sobolev orders.
Periodic product and pressure estimates give
\[
\|e_t\|_{H^1}\le C(\nu+A_2)\|e\|_{H^3}+C F_1,
\qquad
\|\pi+\phi\|_{H^1}\le C A_1\|e\|_{H^1}+C F_0.
\tag{11}
\]
For the second estimate, write
\(\pi=-\Delta^{-1}\partial_i\partial_j(U_i e_j+e_iU_j)\).
The periodic multipliers are bounded on \(H^1\), and \(\phi\) is
mean zero. Equations (10)–(11) justify \(\sup\|g\|_2\le G\).

## 3. A weighted axial-band Leray lemma

We need a pressure estimate that retains its transverse singularity.
Let \(b\) be a fixed Gevrey-2 multiplier supported in a compact positive
frequency interval \([c_0,C_0]\), with \(c_0>0\). On \(\mathbb R^3\)
define
\[
K_k=\mathbb P_{\mathbb R^3}\,b(D_z/k),\qquad D_z=-i\partial_z.
\]
For any nonempty closed set \(S\), put
\[
W(x)=\exp\left[-a\big(1+k^2\operatorname{dist}(x,S)^2\big)^{1/4}\right].
\tag{12}
\]
There is a fixed sufficiently small \(a>0\), depending only on the
multiplier, such that
\[
\|W K_k u\|_2\le C\|Wu\|_2.
\tag{13}
\]
The constants do not depend on \(S\) or \(k\). Also, almost everywhere,
\[
|\nabla\log W|\le Ca k,\qquad
\frac{W(x)}{W(y)}\le\exp(Ca\sqrt{k|x-y|}).
\tag{14}
\]
The distance is 1-Lipschitz, so these statements require no smoothness
of \(S\) or second derivative of the distance.

*Proof of the weighted operator bound.* Scaling reduces to \(k=1\).
In transverse Fourier variables \(\xi\in\mathbb R^2\) and axial
frequency \(\eta\), the multiplier is
\[
b(\eta)\left(I-
\frac{(\xi,\eta)\otimes(\xi,\eta)}{|\xi|^2+\eta^2}\right).
\tag{15}
\]
The two-dimensional inverse Fourier transform of its scalar denominator
is the screened Green kernel
\[
G_\eta(\rho)=\frac1{4\pi}\int_0^\infty
s^{-1}\exp\left(-s\eta^2-\frac{\rho^2}{4s}\right)\,ds,
\qquad \rho=|x_\perp|.
\tag{16}
\]
For \(\eta\) in the fixed band this equals
\(-(2\pi)^{-1}\log\rho\) plus a less singular term at \(\rho=0\),
and decays exponentially at large \(\rho\). The transverse second
derivatives have a two-dimensional Calderón–Zygmund leading kernel
of order \(\rho^{-2}\), **independent of \(\eta\)**. Subtract that
leading kernel with a fixed smooth radial cutoff equal to one near zero
and supported in \(\rho<1\), including its distributional identity term. The mixed
transverse/axial entries have at worst a \(\rho^{-1}\) singularity,
and the axial/axial entry at worst a logarithmic one.

Consequently the kernel of (15) is a finite sum of:

1. the identity in \(x_\perp\) times axial convolution by \(\check b\);
2. a truncated two-dimensional Calderón–Zygmund operator in
   \(x_\perp\), followed by axial convolution by \(\check b\);
3. a convolution kernel \(L(x_\perp,z)\) satisfying
   \[
   |L(x_\perp,z)|\le C F(\rho)e^{-c\sqrt{|z|}},
   \quad
   F(\rho)=
   \begin{cases}
   1+\rho^{-1}+|\log\rho|,&0<\rho\le1,\\
   C e^{-c\rho},&\rho>1.
   \end{cases}
   \tag{17}
   \]

Here is quantitative justification of the axial decay in (17). After
subtracting the leading transverse singularity, the remaining screened
kernel is analytic in \(\eta\) on a fixed complex neighborhood of the
positive band. In (16), this follows by taking that neighborhood small
enough that \(\Re\eta^2\ge c>0\). Cauchy estimates give
\(C^{m+1}m!F(\rho)\) for its \(m\)-th \(\eta\)-derivative, with
a smaller fixed exponential rate at infinity. Multiplication by the
Gevrey-2 cutoff changes this to \(C^{m+1}(m!)^2F(\rho)\). Integrating
the inverse Fourier integral by parts and choosing
\(m\asymp\sqrt{|z|}\) proves (17). The same argument gives
\(|\check b(z)|\le C e^{-c\sqrt{|z|}}\).

The integrable part (17) obeys a weighted Schur estimate by (14), choosing
\(a\) sufficiently small. Axial convolution by \(\check b\) does too.
For the truncated transverse singular operator \(T\), at each fixed
\(z\) write
\[
WTW^{-1}=T+
\int H(x_\perp-y_\perp)
 \left(\frac{W(x_\perp,z)}{W(y_\perp,z)}-1\right)(\cdot)\,dy_\perp.
\tag{18}
\]
The first term has its ordinary \(L^2\) bound. On the truncated support,
the ratio minus one is \(O(a|x_\perp-y_\perp|)\), by the Lipschitz
bound in (14). It makes the second kernel absolutely integrable in
two dimensions, uniformly in \(z,S\). Compose this weighted estimate
with the axial one. This proves (13). In particular, no absolute Schur
estimate has been applied to the original transverse singularity. ∎

## 4. Complete evolution estimate, including pressure and heat leakage

Choose a real Gevrey-2 multiplier \(b\), supported in \([1/2,2]\),
equal to one on \([3/4,5/4]\). Let
\(v_k=b(D_z/k)v\), and choose a second such cutoff \(\widetilde b\)
equal to one on the support of \(b\), supported in \([1/4,3]\).
Since \(M\) is independent of \(z\), axial multipliers commute with
\(M\), the Laplacian, and the Euclidean Leray projection. Thus (9)
gives the exact equation
\[
\partial_t v_k=\nu\Delta v_k+
\mathbb P\widetilde b(D_z/k)(M v_k)
+\mathbb P b(D_z/k)g,
\qquad v_k(t_0)=0.
\tag{19}
\]
Use weight (12) with \(S\) the packet support. Its value on \(S\) is
\(e^{-a}\), while on the support of \(g\) it is at most
\(C e^{-c\sqrt{kR}}\). The weighted pressure lemma bounds both
projected terms in (19); choose \(a\) small enough for both \(b\) and
\(\widetilde b\).

The diffusion calculation needs only the weak first derivative of \(W\):
\[
\Re\langle W^2v_k,\Delta v_k\rangle
=-\|\nabla(Wv_k)\|_2^2+
\|v_k\nabla W\|_2^2
\le C k^2\|Wv_k\|_2^2.
\tag{20}
\]
It follows, by the scalar energy inequality and (13), that
\[
\|Wv_k(t)\|_2
\le C\int_{t_0}^t
 e^{C(\gamma+\nu k^2)(t-s)}\|Wg(s)\|_2\,ds
\le C dG e^{C(\gamma+\nu k^2)d-c\sqrt{kR}}.
\tag{21}
\]
One can justify the calculation by smooth approximation of the Lipschitz
weight and spatial truncation; (14) gives uniform constants. This is an
estimate for the full time evolution. The diffusion term pays for heat
crossing the artificial boundary, and (13) pays for the nonlocal pressure
at every time. Neither is omitted as a small unspecified remainder.

Finally the normalized Gevrey packet satisfies
\[
\|(1-b(D_z/k))v_\tau\|_2\le C e^{-c\sqrt{k\ell}}.
\tag{22}
\]
Indeed the axial Fourier transform of its bump is evaluated at
\(\ell(\eta-k)\), and outside the plateau of \(b\) this has size
at least \(c k\ell\). Integrating the squared Gevrey tail gives (22).
The terms \(\chi_z/(ik)\) and \((\chi_r+\chi/r)/(ik)\) produce
only fixed polynomial factors, absorbed by decreasing \(c\).
Their normalizing factor is still \(\asymp\sqrt{r_0}\ell\).

Because \(b\) is real, it is self-adjoint. Pair (21) with the unit
packet on \(S\), and bound the complementary term by (22) and (10).
The local extension agrees with the averaged actual response on \(S\),
and angular averaging preserves this pairing. The result is (4).

## 5. Paying the global low norms without a high-order exponential

The low norms in (3) can be controlled by one global strain history and
fixed polynomial derivative costs. Write
\[
I=\int_{t_0}^{t_0+d}\|\nabla U(s)\|_\infty\,ds.
\]
The energy estimate for \(j\) derivatives of (2) has the triangular form
\[
\frac d{dt}\|e\|_{H^j}
\le C_j\|\nabla U\|_\infty\|e\|_{H^j}
+C_j A_{j+1}\sum_{i<j}\|e\|_{H^i}+C_j F_j,
\quad 0\le j\le3,
\tag{23}
\]
where the empty sum is zero. Diffusion is nonpositive, transport of the
highest derivative is skew in the energy pairing, and all terms with
two or more derivatives on \(U\) multiply a strictly lower derivative
of \(e\). The full Leray projection drops against the solenoidal energy
test. Thus no coefficient \(\|U\|_{H^4}\) is inserted into the exponent.

Choose one common constant in the exponential for \(j=0,1,2,3\), and
integrate (23) inductively from zero data. This gives the safe estimate
\[
E_3\le C F_3 d(1+A_4d)^3 e^{CI}.
\tag{24}
\]
The same bounds control \(E_1\). The source's fixed-order jet estimates
give \(A_4\le C\tau^{-P_4}\) for some fixed finite \(P_4\), while
the smooth terminal extension of \(f\) bounds \(F_3\). Consequently,
for some fixed finite \(N\), (4) implies
\[
\sup_{t_0\le t\le t_0+d}|\langle e(t),v_\tau\rangle|
\le C\tau^{-N}e^{C[I+(\gamma+\nu k^2)d]}
\left(e^{-c\sqrt{k\ell}}+e^{-c\sqrt{kR}}\right).
\tag{25}
\]
This is the explicit global input to the local result. Any proposed
global estimate must be substituted into (25), rather than inferred
from the local exterior alone.

## 6. Actual logarithmic flight and its precise scope

The [global strain-cost lemma](global-strain-cost.md)
gives for the complete actual reference
\[
\|\nabla U(t)\|_\infty
\le C\tau^{-1-h}\sqrt{\log(1/\tau)}
\quad\text{on }[t_0,t_0+\tau/2].
\tag{26}
\]
Use the original packet scales
\[
\ell=\tau^{1/2+h/8},\qquad k=\tau^{-1/2-h/4},
\qquad d\le C_*\tau^{1+h}\log(1/\tau),
\tag{27}
\]
where \(C_*\) is fixed. Then
\[
I\le C\log^{3/2}(1/\tau),\qquad
(\gamma+\nu k^2)d\le C\log(1/\tau),
\]
\[
\sqrt{k\ell}=\tau^{-h/16},\qquad
\sqrt{kR}\asymp\tau^{-h/8}.
\tag{28}
\]
Equations (25)–(28) therefore give, after decreasing the positive
constant in the exponent,
\[
\boxed{\quad
\sup_{t_0\le t\le t_0+d}
|\langle e(t),v_\tau\rangle|
\le C\exp(-c\tau^{-h/16}).
\quad}
\tag{29}
\]
This includes the logarithmic interval used in the quasimode's actual
propagator-norm lower bound. It improves fixed-jet smallness to a complete
linear-response pairing bound, using a specified Gevrey packet and the
separately proved global cost (26).

More generally, the same proof applies to fixed
\(0<a<b<h/2\), \(\ell=\tau^{1/2+a}\),
\(k=\tau^{-1/2-b}\), with exponent \((b-a)/2\) replacing \(h/16\).
The strict upper bound on \(b\) retains the quasimode's small relative
viscous damping. No uniform assertion as \(a\downarrow0\) or
\(b\uparrow h/2\) is needed.

There is also a uniform finite-dimensional consequence. Translate the
same Gevrey axial envelope to centers in the middle half of the complete
source tube, separated by at least \(3\ell\), as in
[the packed quasimode space](initial-correction.md#5-actual-heat-exterior-packets-form-a-large-common-quasimode-space).
Choose a packing with \(n_\tau\asymp\tau^{-9h/8}\), so both an upper
and a lower polynomial bound hold. For every center, the nested cylinders
of width \(R\) remain in the exact exterior with the same constants:
the available axial margin is comparable to
\(\tau^{1/2-h}\gg R\). Translation does not change any band estimate.
The real parts have uniformly comparable norms to their complex packets
and disjoint supports, so form an orthonormal real family after
normalization. For the real actual response and their span
\(E_\tau^{\rm G}\),
\[
\sup_{t_0\le t\le t_0+d}
\|\operatorname{Proj}_{E_\tau^{\rm G}} e(t)\|_2
\le C\sqrt{n_\tau}\,e^{-c\tau^{-h/16}}
\le C e^{-c'\tau^{-h/16}}.
\tag{30}
\]
The first inequality sums squared orthonormal coefficients; the polynomial
dimension cost is absorbed into the exponential. This is the Gevrey
choice of the previously constructed packet space, not a spectral
unstable subspace or a time-evolved projection.

The estimate tests the complete response against the **fixed** packet
chosen at \(t_0\). It does not estimate its projection on every possible
growing direction, on an independently evolved terminal packet, or on a
whole frequency sector without localization. The pressure moments and
lower axial frequencies may behave differently. The nonlinear error,
initial-data correction problem, and one unforced singular trajectory
remain unresolved.

**Review record.** The coordinating agent independently checked the
complete argument at body SHA-256
`3afcad4ac5a47da373a974bffed039739a3e98e0089cdcb6ae0d5f28d7d3de29`.
A source-audit agent separately passed the actual local reduction,
streamfunction extension, pressure sign, low norms, global input and
endpoint scope; it also read the weighted-band argument without finding
a defect. A third agent independently checked the transverse singular
kernel split, weighted operator and heat estimates, packet complement,
and final attenuation comparison. The coordinating agent also checked
the translated-packet corollary (30). The final clarifications specify
that the transverse cutoff equals one near zero and that the weight
constant works for both axial cutoffs. These are independent AI reviews
of a written estimate, not a formal PDE certificate or external expert
acceptance. No full nonlinear force-removal estimate is asserted.
