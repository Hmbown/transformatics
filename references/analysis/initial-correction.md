# Initial-data correction and the cost of selecting growing directions

8 September 2026. Restricted written analysis; independently reviewed at
the stated scope.
There are two different conclusions here. A classical terminal-integral
construction can select one corrected initial datum, provided explicit
linear splitting and nonlinear estimates hold. For the actual external
reference, however, the heat exterior supplies arbitrarily large spaces of
quasimodes. These rule out a uniformly controlled stable complement of
fixed finite codimension in any fixed integer Sobolev space. They do not
identify the unstable spectrum or rule out nonuniform or infinite-dimensional
correction schemes.

The actual-reference inputs are the reviewed
[exterior quasimode](exterior-quasimode.md) and
[external source geometry](external-modulation-source.md),
for the same pinned external construction. The torus is
\(\mathbb R^3/\mathbb Z^3\), the actual viscosity is one, and the actual
terminal time is one. General identities below allow fixed \(\nu>0,T\).
No initial datum removing that construction's force is obtained here.

## 1. The exact equation with an adjustable initial value

Fix one \(t_0<T\). Let \(U,P,f\) be the complete smooth forced reference
on every compact subinterval of \([t_0,T)\). For \(V=U+e\), ordinary
unforced Navier–Stokes is equivalent to
\[
 e_t=\mathcal A(t)e-F(t)-\mathcal B(e,e),\qquad
 \mathcal A(t)e=\nu\Delta e-
 \mathbb P\big((U\cdot\nabla)e+(e\cdot\nabla)U\big),
\tag{1}
\]
where
\[
 F=\mathbb P f,\qquad
 \mathcal B(v,w)=\mathbb P\nabla\cdot(v\otimes w).
\]
The convention for the tensor divergence is chosen so that
\(\nabla\cdot(e\otimes e)=(e\cdot\nabla)e\) for solenoidal \(e\).
The pressure difference is the periodic solution, up to its spatial mean,
of
\[
 \Delta\pi=-\nabla\cdot f-
 \partial_i\partial_j(U_i e_j+e_i U_j+e_i e_j).
\tag{2}
\]
In particular, the full physical force and every pressure term remain.
The new freedom is \(e(t_0)=e_0\), rather than \(e_0=0\).
Its spatial mean must satisfy
\[
 \overline e(t)=\overline e_0-\int_{t_0}^t\overline f(s)\,ds.
\tag{3}
\]
We work in the full solenoidal space unless mean-zero forcing and data are
explicitly imposed. Mean cancellation is not silently assumed.

## 2. A precise terminal-integral hypothesis

Fix an integer \(m\ge3\), and write
\[
 X=H^m_\sigma(\mathbb T^3),\qquad Y=H^{m-1}_\sigma(\mathbb T^3).
\]
The product estimate is
\[
 \|\mathcal B(v,w)\|_Y\le C_m\|v\|_X\|w\|_X.
\tag{4}
\]
Thus one derivative must be paid by the propagator; a bound only from
\(X\) to \(X\) does not by itself close the nonlinear argument.
Let \(\mathcal S(t,s)\) be the actual forward evolution of (1)'s linear
part. It is well defined on every compact preterminal interval.

Assume the following splitting; it is not a consequence of smoothness of
\(U\) or of the quasimode theorem.

1. Bounded complementary projections \(P_s(t),P_u(t)\) act consistently on
   \(X,Y\), are strongly continuous, and obey
   \(P_s(t)\mathcal S(t,s)=\mathcal S(t,s)P_s(s)\), and likewise for \(P_u\).
2. The forward evolution restricted to the terminal subspaces is
   invertible between those subspaces. Denote its backward restriction by
   \(\mathcal S_u(t,s)\), for \(t\le s\), and set
   \(\mathcal S_s(t,s)=\mathcal S(t,s)P_s(s)\), for \(s\le t\).
   The backward map is assumed only on the specified subspaces. There is
   no backward heat operator on arbitrary Sobolev data.
3. Including the projections in the following operators, assume
   \[
   \|\mathcal S_s(t,s)\|_{Y\to X}\le K_s(t,s),\qquad
   \|\mathcal S_u(t,s)P_u(s)\|_{Y\to X}\le K_u(t,s).
   \tag{5}
   \]
   The forward singularity as \(s\uparrow t\) must be integrable; the
   usual parabolic singularity \((t-s)^{-1/2}\) is one possible mechanism.
   A finite-dimensional terminal bundle with smooth basis can instead
   make its backward \(Y\to X\) map bounded locally. Neither mechanism
   is asserted for the actual terminal bundle.

For compact notation, henceforth include \(P_u(s)\) in \(\mathcal S_u(t,s)\).
These are the parts of an evolution dichotomy needed for the argument.
A common stronger version bounds the forward and backward maps by
\(C\exp(-\alpha|\Theta(t)-\Theta(s)|)\) in an increasing clock \(\Theta\),
with compatible smoothing factors. We do not assume that stronger form.
The labels refer to forward and terminal boundary conditions, respectively;
a selected center direction requires its own estimates too.

Choose a positive continuous weight \(w\), finite and bounded away from
zero on each compact preterminal interval, and let
\[
 \|e\|_{\mathcal X_w}=\sup_{t_0\le t<T}\frac{\|e(t)\|_X}{w(t)}.
\]
The space consists of continuous \(X\)-valued functions with finite norm.
Assume the operator families in (5) are strongly continuous away from the
diagonal and that their kernel integrals below admit locally uniform
integrable majorants, including their tails at \(T\). This ensures
Bochner convergence and continuity; endpoint cancellation alone is not
a substitute for this requirement.

Define the signed Green operator
\[
 (\mathcal G g)(t)=
 -\int_{t_0}^t\mathcal S_s(t,s)g(s)\,ds
 +\int_t^T\mathcal S_u(t,s)g(s)\,ds.
\tag{6}
\]
The opposite signs are essential. For \(\xi\in\operatorname{Ran}P_s(t_0)\),
put
\[
 L_\xi(t)=\mathcal S_s(t,t_0)\xi+(\mathcal G F)(t),
 \quad a=\|L_\xi\|_{\mathcal X_w},
\]
\[
 b=C_m\sup_{t_0\le t<T}\frac1{w(t)}
 \left[\int_{t_0}^t K_s(t,s)w(s)^2\,ds
 +\int_t^T K_u(t,s)w(s)^2\,ds\right].
\tag{7}
\]
Here \(a\) may use the signed full force response. Replacing it by the
corresponding integrals of \(\|F\|_Y\) gives a sufficient upper bound,
but can lose cancellation. The number \(b\) is an actual derivative-paying
bilinear budget. All quantities depend on the reference, its force,
the proposed splitting, and \(\xi\), not on an unknown unforced solution.

## 3. Conditional correction theorem and its one-datum meaning

Suppose the preceding assumptions hold, \(a,b<\infty\), and
\[
 4ab<1.
\tag{8}
\]
Then the equation
\[
 \boxed{\ e=L_\xi+\mathcal G\mathcal B(e,e)\ }
\tag{9}
\]
has a unique solution in the closed ball \(\|e\|_{\mathcal X_w}\le2a\).
Indeed, the map sends the ball into itself because
\(a+4ba^2\le2a\), and its Lipschitz constant on that ball is at most
\(4ab<1\). When \(a=0\), the zero solution is the unique solution in
that zero-radius ball. This is the classical Lyapunov–Perron contraction,
with the pressure and one-derivative loss stated explicitly.

Splitting each integral at an intermediate time and using the evolution
identities shows that (9) solves the forward mild equation (1). This
argument does not differentiate a possibly nonsmooth projection. Its
initial value is the single vector
\[
 \boxed{\ e_0=\xi+
 \int_{t_0}^T\mathcal S_u(t_0,s)
       [F(s)+\mathcal B(e,e)(s)]\,ds.\ }
\tag{10}
\]
In particular, the correction depends on future force transport and on
its own nonlinear interaction. Cancelling only the linear term in (10)
is not the nonlinear construction.

For the usual converse terminal interpretation, assume in addition that,
for every fixed \(t<T\),
\[
 \|\mathcal S_u(t,s)\|_{X\to X}w(s)\longrightarrow0
 \quad\text{as }s\uparrow T.
\tag{11}
\]
Then every \(\mathcal X_w\) solution with
\(P_s(t_0)e(t_0)=\xi\) has
\(\mathcal S_u(t,s)P_u(s)e(s)\to0\). Project its forward variation formula,
run it backward on the terminal subspace, and let \(s\uparrow T\).
This gives the positive terminal integral in (6). The forward part has
initial value \(\xi\), so it recovers (9). Condition (11) is a weighted
transversality condition, not the assertion \(e(T)=0\); that terminal
value may not exist.

The fixed point gives \(e\in C([t_0,T);H^m)\) and the usual local strong
regularity of the parabolic equation. Consequently \(V=U+e\) solves
ordinary unforced Navier–Stokes on every compact subinterval. The theorem
initially supplies an \(H^m\) datum. It does not automatically supply
\(e_0\in C^\infty\) if the terminal subspace is infinite dimensional.
There are two legitimate remedies. If the terminal subspace at \(t_0\)
is finite dimensional and consists of smooth fields, and \(\xi\) is
smooth, (10) is smooth. Otherwise choose one fixed \(t_*\in(t_0,T)\);
positive-viscosity smoothing makes \(V(t_*)\) smooth. Restarting there
uses one fixed smooth datum, rather than a sequence of later restarts.
If its conserved mean is a nonzero vector \(m_0\), the constant Galilean
transformation \(V(t,x+m_0(t-t_*))-m_0\) on the same torus supplies
mean-zero smooth data and preserves unbounded speed.

To inherit a reference speed lower bound \(\|U(t_n)\|_\infty\ge A_n\to\infty\),
one still needs the quantitative margin
\[
 2C_{\rm emb}a\,w(t_n)\le\vartheta A_n,
 \qquad 0<\vartheta<1.
\tag{12}
\]
Without this margin, existence of the corrected solution does not imply
that it shares the reference singularity. Nothing in this section verifies
(5), (7), (8), or (12) for the external Navier–Stokes reference.

## 4. An exact scalar construction: nonzero terminal forcing can be cancelled

The preceding strategy has a genuine mechanism. Consider the scalar
linear equation, with \(\tau=T-t\),
\[
 e'=c\tau^{-1-h}e-f(t),\qquad c,h>0,
 \quad |f(t)|\le F_0.
\tag{13}
\]
Its forward propagator is
\[
 S(t,s)=\exp\!\left[\frac c h
 ((T-t)^{-h}-(T-s)^{-h})\right].
\]
Selecting one initial value
\[
 e_0=\int_{t_0}^T S(t_0,s)f(s)\,ds
\tag{14}
\]
gives the exact solution
\[
 e(t)=\int_t^T S(t,s)f(s)\,ds,\qquad
 |e(t)|\le\frac{F_0}{c}\tau^{1+h}.
\tag{15}
\]
For the bound, the increasing coefficient \(a(t)=c\tau^{-1-h}\) gives
\(S(t,s)\le e^{-a(t)(s-t)}\) for \(s\ge t\). Thus the terminal integral
is bounded by \(F_0/a(t)\). The force can be a nonzero constant all the
way to \(T\). Its contribution is cancelled by the initial value, not
by terminal flatness of the force.

The selection is sensitive: changing (14) by \(\delta\ne0\) adds exactly
\[
 \delta\exp\!\left[\frac c h
 (\tau^{-h}-(T-t_0)^{-h})\right].
\tag{16}
\]
This instability is compatible with existence of the specially selected
datum. It is not a prohibition on exact selection.

There is even a small nonlinear version. For
\(e'=c\tau^{-1-h}e-f-e^2\), use the same terminal kernel and
\(w(t)=\tau^{1+h}\). Since \(w(s)\le w(t)\) for \(s\ge t\),
\[
 a\le F_0/c,\qquad
 b\le (T-t_0)^{2+2h}/c.
\tag{17}
\]
Hence (8) holds whenever
\(4F_0(T-t_0)^{2+2h}<c^2\), and (10) constructs one datum with
\(|e(t)|\le2F_0\tau^{1+h}/c\). This is a proved scalar cancellation
example, not a Navier–Stokes model theorem. It explains why nonzero
terminal force and large forward growth alone cannot exclude initial-data
correction.

### An infinite parabolic correction can fail even to be a distribution

The scalar suppression does not settle the summability of infinitely many
corrections. On the one-dimensional unit torus consider the explicit
linear parabolic equation
\[
 e_t=\nu\partial_x^2 e+\gamma(t)e-\eta(t)g(x),\qquad
 \gamma(t)=c(T-t)^{-1-h},
 \quad g(x)=\sum_{n=1}^\infty e^{-n}\cos(2\pi nx).
\tag{17a}
\]
Fix \(t_0\) once, choose \(\delta>0\) with \(t_0+2\delta<T\), and take
\(\eta\ge0\), nonzero, smooth and supported strictly inside
\((t_0+\delta,t_0+2\delta)\). The spatial force is real analytic and the
full force vanishes on a neighborhood of the terminal time. All its
terminal time derivatives vanish.

Write \(e_n(t)\) for the cosine coefficients. Each satisfies
\[
 e_n'=[\gamma(t)-\nu(2\pi n)^2]e_n-\eta(t)e^{-n}.
\]
After the forcing pulse, its exact formula is
\[
 e_n(t)=\exp\!\left(\int_{t_0}^t\gamma(r)\,dr
                     -\nu(2\pi n)^2(t-t_0)\right)
 \left[e_n(t_0)-I_n\right],
\]
\[
 I_n=e^{-n}\int_{t_0}^T
 \exp\!\left(\nu(2\pi n)^2(s-t_0)
                  -\int_{t_0}^s\gamma(r)\,dr\right)\eta(s)\,ds.
\tag{17b}
\]
For every fixed \(n\), the first exponential grows faster than every
power of \((T-t)^{-1}\). Therefore even the weak requirement that every
fixed Fourier coefficient be bounded by some finite terminal power
forces \(e_n(t_0)=I_n\). The power and its constant may depend on \(n\).

The integral of \(\gamma\) is bounded on the fixed forcing support.
Because \(s-t_0\ge\delta\) there and \(\eta\) is nonnegative and nonzero,
there is a fixed \(C_\delta>0\) such that
\[
 I_n\ge C_\delta
 \exp\!\left(\nu(2\pi n)^2\delta-n\right).
\tag{17c}
\]
Fourier coefficients of a distribution on a compact torus grow at most
polynomially: a finite-order distribution bound applied to the sine and
cosine test functions gives that fact directly. Thus the required initial
coefficients do not belong even to a distribution. No distributional
initial datum can have the stated polynomial terminal behavior.

Every finite Fourier truncation does admit a smooth terminal-cancelling
initial datum, given by the finitely many numbers \(I_n\). Those data
have no distributional limit. The obstruction is the backward diffusive
cost over the fixed gap \(\delta\), before each fixed frequency eventually
becomes growing. It persists despite smooth time dependence of the force,
analytic spatial dependence, and exact vanishing of the force near \(T\).
This is an exact toy equation, not the Navier–Stokes linearization. It
shows why regularity and summability in (10) must be proved; solving each
scalar terminal cancellation separately does not prove them.

## 5. Actual heat-exterior packets form a large common quasimode space

Now return to the actual reference and write \(t_0=1-\tau\). These varying
probe times test a putative splitting on one fixed interval; they are not
a sequence of replacement initial data in the construction of §3. The reviewed
source tube has radial center \(r_0\asymp\tau^{1/2}\), fixed relative
radial width, and axial interval \(|z|<c_z\tau^{1/2-h}\). Throughout this
fixed spatial tube, and throughout the late window below, the complete
reference is the exact swirl \(U=K(t,r)e_\theta\), independent of \(z\),
with all localization cutoffs one and all annular corrections zero.

Keep the quasimode note's choices
\[
 \delta=\tau^{1/2+h/8},\qquad
 k=\tau^{-1/2-h/4},\qquad
 \lambda_\tau=\gamma_\tau-k^2
 \asymp\tau^{-1-h},
\tag{18}
\]
where \(\gamma_\tau>0\) is determined at the single radial center.
Choose disjoint axial intervals of radius \(\delta\), with centers
\(z_j\) separated by at least \(3\delta\) and lying in the middle half
of the source tube. Their number can be chosen to satisfy
\[
 n_\tau\ge c\frac{\tau^{1/2-h}}{\delta}
 =c\tau^{-9h/8}
\tag{19}
\]
for sufficiently small \(\tau\). Constants depend on the fixed source.
The radial envelope is unchanged for every packet. Replace the original
axial envelope and carrier by their translates in \(z-z_j\).

For clarity, with a common radial bump and translated axial bump let
\(H_j=\chi_j(r,z)e^{ik(z-z_j)}\). The full packet remains
\[
 v_j=\nabla\times\left(-\frac{H_j}{ik}e_\theta\right)
       +\sqrt{g_0}\,H_j e_\theta,
\tag{20}
\]
with the same positive \(g_0\) as in the source calculation. Thus
\[
 (v_j)_r=\left(\chi_j+\frac{\partial_z\chi_j}{ik}\right)e^{ik(z-z_j)},
 \quad
 (v_j)_z=-\frac{\partial_r\chi_j+\chi_j/r}{ik}e^{ik(z-z_j)}.
\]
This is exactly solenoidal, smooth, mean zero, and supported inside the
coordinate chart. Zero extension and periodization introduce no boundary
term. The common eigenvalue is unchanged because \(K,\Omega,B\) depend
on \(t,r\) only. No angular envelope has been introduced.

The unprojected residuals have disjoint supports, just as the packets do.
Consequently their squared \(L^2\) norms add for arbitrary linear
combinations. Applying the global Leray projection only afterwards is an
\(L^2\) contraction. It does not require disjoint pressure tails. Taking
and normalizing a real or imaginary part of each packet preserves these
facts, at the expense of a uniform constant. We therefore obtain a real
space \(E_\tau\) of dimension \(n_\tau\) such that every \(v\in E_\tau\)
satisfies the same relative residual bounds.

The assertion extends to each fixed integer \(m\ge0\), with constants
allowed to depend on \(m\). Use the local derivative norm for \(H^m\),
which is equivalent to its Fourier norm and makes disjoint-support
orthogonality explicit. Carrier differentiation and \(k\delta\to\infty\)
give
\[
 c_m k^m\|v_j\|_2\le\|v_j\|_{H^m}
 \le C_m k^m\|v_j\|_2.
\tag{21}
\]
For the lower bound use \(\partial_z^m v_j=(ik)^m v_j\) plus terms smaller
by \(O_m((k\delta)^{-1})\) for the complex packet; then choose a real
or imaginary part with at least half the squared complex \(H^m\) norm.
Alternatively, one phase integration by parts bounds the oscillatory
term in the cosine-square identity by \(C_m/(k\delta)\) times the
nonoscillatory mass. Thus the real cosine or sine packet has \(L^2\)
norm comparable to the complex packet, and its leading \(m\)-th axial
derivative has norm comparable to \(k^m\) times that real norm. This
also gives (21) directly for the real normalized packets.

The upper residual bound can be differentiated term by term in the exact
three raw residual components of the quasimode note. Each envelope or
basis derivative costs at most \(C_m\delta^{-1}\) or \(C_m r_0^{-1}\),
both smaller than \(C_m k\). An undifferentiated coefficient difference
costs \(\delta/r_0+(t-t_0)/\tau\). When at least one derivative lands on
that difference, the relative factor after division by \(k^m\) is bounded
by \((kr_0)^{-j}\), \(j\ge1\), hence by \(C\tau^{h/4}\). This is smaller
than the retained \(\tau^{h/8}\) error. The fixed heat-profile derivatives
needed here are available uniformly on the compact range of its similarity
variable. Viscous and cylindrical terms retain their smaller powers.
Leray commutes with derivatives and contracts the derivative norm.
All sums remain orthogonal before projection. There is no growing-order
Sobolev estimate or global derivative bound in this argument.

Fix \(m\) and take \(\epsilon_\tau=C_m'\tau^{h/8}<1/2\), with a large
fixed constant. Put
\[
 \Delta_\tau=\lambda_\tau^{-1}\log(1/\epsilon_\tau),\qquad
 t_1=t_0+\Delta_\tau.
\tag{22}
\]
Since \(\Delta_\tau/\tau=O(\tau^h\log(1/\tau))=o(\tau^{h/8})\), the
reviewed nonautonomous residual estimate yields, uniformly over this
entire space,
\[
 \left\|\frac d{dt}\left(e^{\lambda_\tau(t-t_0)}v\right)
 -\mathcal A(t)e^{\lambda_\tau(t-t_0)}v\right\|_{H^m}
 \le\epsilon_\tau\lambda_\tau e^{\lambda_\tau(t-t_0)}\|v\|_{H^m}.
\tag{23}
\]
In particular the instantaneous quadratic form of the actual generator
is positive on the whole space \(E_\tau\), for small \(\tau\). This
states a growing number of energy-growth directions, not a count of
unstable eigenvalues.

## 6. A quantitative obstruction to a fixed finite stable codimension

Suppose any bounded invariant projection family \(P_s(t)\) exists for
the actual evolution in this fixed \(H^m\) space, and put
\(P_u(t)=I-P_s(t)\). No spectral interpretation or backward evolution is
needed in this section. If
\[
 \operatorname{rank}P_u(t_1)<n_\tau,
\tag{24}
\]
linear algebra gives a unit vector \(v\in E_\tau\cap\ker P_u(t_1)\).
Only stability at the final endpoint is needed. In particular we need
not assume \(P_s(t_0)v=v\).

Write \(y(t)=e^{\lambda_\tau(t-t_0)}v\) and
\(r=y'-\mathcal A(t)y\). Exact Duhamel gives
\[
 y(t_1)=\mathcal S(t_1,t_0)v+
 \int_{t_0}^{t_1}\mathcal S(t_1,s)r(s)\,ds.
\]
Apply \(P_s(t_1)\) and use invariance to move it through the evolution.
The left side remains \(e^{\lambda_\tau\Delta_\tau}v\). Define
\[
 M_s(\tau)=\sup_{t_0\le s\le t_1}
 \|\mathcal S(t_1,s)P_s(s)\|_{H^m\to H^m}.
\]
The projection norms are included in this quantity, including at
\(s=t_1\). Equation (23) gives
\[
 e^{\lambda_\tau\Delta_\tau}
 \le M_s(\tau)\left[1+
 \epsilon_\tau(e^{\lambda_\tau\Delta_\tau}-1)\right].
\]
Since the exponential is \(1/\epsilon_\tau\),
\[
 \boxed{\ \operatorname{rank}P_u(t_1)<n_\tau
 \quad\Longrightarrow\quad
 M_s(\tau)\ge\frac1{\epsilon_\tau(2-\epsilon_\tau)}
 \ge c_m\tau^{-h/8}.\ }
\tag{25}
\]
This is a property of the actual full projected evolution, not its
principal symbol. Annular coefficients and all pressure tails enter
\(\mathcal S\); no upper bound on them was used.

For example, a dichotomy on one fixed interval \([t_*,1)\), with terminal
rank bounded by a fixed finite \(d\), cannot have
\[
 \|\mathcal S(t,s)P_s(s)\|_{H^m\to H^m}\le C
 \left(\frac{1-s}{1-t}\right)^\beta,
 \qquad C,\beta<\infty,\quad\beta\ge0.
\tag{26}
\]
Indeed, (19) eventually exceeds \(d\), while all time ratios on (22)'s
window tend to one. The same excludes a uniformly bounded exponentially
decaying stable propagator in any clock. A polynomially weighted version
with fixed exponents also has bounded weight ratios on these windows.

Conversely, insisting on a uniformly bounded \(M_s\) would require
terminal rank at least \(n_\tau\gtrsim\tau^{-9h/8}\). Under an actual
dichotomy with invertible terminal evolution, that rank is constant in
time, so it must be infinite. This is a conditional statement about such
a splitting. It does not prove that an infinite-dimensional well-controlled
splitting exists, nor that an infinite-dimensional correction is regular.

## 7. What remains possible, and a spectral negative control

Positive quasimodes are not unstable eigenvectors. The exact matrix
\[
 A_L=\begin{pmatrix}-1&L\\0&-1\end{pmatrix},\qquad
 v_L=\frac{(1,2/L)}{\sqrt{1+4/L^2}}
\]
has both eigenvalues equal to \(-1\), yet
\[
 \|(A_L-I)v_L\|=\frac{4/L}{\sqrt{1+4/L^2}}.
\tag{27}
\]
A direct sum of \(n\) such blocks has an \(n\)-dimensional common positive
quasimode space while every eigenvalue remains \(-1\). Its all-stable
propagator simply has a large transient norm. This elementary control
prevents replacing (25) by an unsupported eigenvalue count.

For the actual reference, the result leaves open a finite-dimensional
terminal subspace with a stable bound deteriorating at least as in (25),
a splitting only in a suitably restricted error class, a useful infinite
terminal subspace, or a formulation modulo moving parameters. Any such
route must verify its own weighted Green bounds. A finite number of
modulation parameters alone cannot make the entire complementary Sobolev
evolution uniformly controlled in the sense of (26).

The physical force vanishes on each packet support. Consequently
\(\langle\mathbb P f(t),v\rangle=0\) for all \(v\in E_\tau\) and all
times in the packet window, by the global self-adjointness of Leray.
Thus even the large family of growing directions does not prove that the
particular force response enters them. The backward terminal integral
uses transported projections or adjoint tests, which need not remain
supported in that tube.

The next missing construction is therefore specific: identify an actual
invariant splitting or another source-selective Green operator; estimate
its full \(Y\to X\) kernels and signed force response; and check (7)–(12)
for one fixed datum. The initial correction is not forbidden by nonzero
terminal force. What is excluded is the shortcut of removing finitely
many directions and assuming uniform stability of everything else.

The terminal-integral method is classical invariant-manifold mathematics.
For academic context, see Bento and Silva,
[Nonautonomous equations, generalized dichotomies and stable manifolds](https://arxiv.org/abs/0905.4935),
which assumes a generalized dichotomy and constructs stable manifolds for
small nonlinear perturbations. No theorem from that paper is asserted to
verify the external fluid's splitting; the contraction used here is proved
above. The actual exterior packing and the projection obstruction are the
source-specific calculations in this note. ROOT remains open.


## 8. Verification record

The integration reviewer independently read the Green formulation, one-datum
regularity argument, packet construction and fixed-Sobolev extension,
projection obstruction, and Jordan-matrix control. Avicenna independently
reviewed §§5–7 and found no mathematical correction. A separate pedagogy
agent independently reviewed §§2–4, including the diagonal parabolic
counterexample, and passed the signs, estimates and regularity claims.
Its clarification that the converse fixes the forward projection of the
initial value is included above.

Bounded exact symbolic checks independently confirmed the scalar kernel's
time derivative, the parabolic Fourier-mode propagator, the Jordan
matrix's residual and spectrum, and the Duhamel denominator. These checks
support the displayed algebra; they are not a formal PDE certificate.
No numerical fluid simulation or full formal build was run. The actual
Navier–Stokes result in this note is the finite-codimension obstruction
(25), with the explicit packet count (19). The correction theorem remains
conditional, and the parabolic obstruction remains a toy example.
