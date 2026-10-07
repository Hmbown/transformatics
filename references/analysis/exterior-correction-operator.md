# An actual exterior packet correction, and the remaining fixed-datum inverse

8 September 2026. Restricted written analysis. On a sufficiently short late
window, the actual global linearized evolution is quantitatively invertible
between the same finite packet spaces. This yields a smooth initial
perturbation cancelling the prescribed force response in all those endpoint
measurements. The perturbation is exponentially small in every fixed
Sobolev norm. The restart time and datum vary with the window; no single
force-removing datum or unforced singularity is constructed.

The inputs are the reviewed [exterior quasimode](exterior-quasimode.md),
its [packed real space](initial-correction.md#5-actual-heat-exterior-packets-form-a-large-common-quasimode-space),
the [global strain bound](global-strain-cost.md), and the
[complete source-response estimate](local-response-bound.md).
They concern the same fixed external construction, ordinary viscosity one,
the unit torus, and terminal time one. In particular, all reference
corrections and the full periodic pressure are retained. The argument below
uses variation of constants and a Neumann inverse, both classical operator
tools; its conclusion is specific to these source estimates.

## 1. Actual operators and a shorter window

Fix the source parameters, including \(0<h<1/100\), before any limit. Let

\[
 a_\tau=1-\tau,\qquad L=1+\log(1/\tau),\qquad
 d_\tau=c\tau^{1+h}\sqrt L,\qquad b_\tau=a_\tau+d_\tau.
 \tag{1}
\]

The fixed constant \(c>0\) is chosen below. For small enough \(\tau\),
\(d_\tau<\tau/2\). Write \(\mathcal S(t,s)\) for the actual global
linearized evolution with generator

\[
 \mathcal A(t)v=\Delta v-
 \mathbb P_{\mathbb T^3}\big((U\cdot\nabla)v+(v\cdot\nabla)U\big).
 \tag{2}
\]

Use real solenoidal \(L^2\), with ordinary torus volume. The evolution
also preserves its mean-zero subspace. For every smooth solenoidal input,
integration by parts gives

\[
 \frac12\frac d{dt}\|v\|_2^2
 =-\|\nabla v\|_2^2-\int v^T S(U)v.
\]

Thus the global source bound supplies a fixed \(A_*>0\) such that

\[
 \|\mathcal S(t,s)\|_{2\to2}
 \le \exp\big(A_*\tau^{-1-h}\sqrt L\,(t-s)\big),
 \quad a_\tau\le s\le t\le b_\tau.
 \tag{3}
\]

Choose \(c\) once with \(A_*c\le h/32\). No comparison of unknown
propagators or local replacement of pressure is made in (3).

Take the Gevrey-2 version of the previously constructed real packet space
\(E_\tau\), and denote its orthogonal \(L^2\) projection by \(P_\tau\).
Its packets have disjoint axial supports inside the actual heat tube and
common scales

\[
 \delta=\tau^{1/2+h/8},\qquad
 k=\tau^{-1/2-h/4},\qquad
 n_\tau:=\dim E_\tau\asymp\tau^{-9h/8},
\]
\[
 \lambda_\tau=c_\gamma\tau^{-1-h}-k^2
 \asymp\tau^{-1-h},\qquad c_\gamma>0.
 \tag{4}
\]

Each packet is the real part of the complete cylindrical curl packet,
including its radial-envelope and divergence corrections. All are smooth,
solenoidal and mean zero, and their axial translations have the same
\(\lambda_\tau\). For every \(v\in E_\tau\), the raw residuals have
disjoint supports; applying the global Leray projection after summing is
an \(L^2\) contraction. Consequently, uniformly on (1),

\[
 \|(\mathcal A(t)-\lambda_\tau)v\|_2
 \le C\tau^{h/8}\lambda_\tau\|v\|_2.
 \tag{5}
\]

This is an operator estimate on the entire space, with no dimension factor.
The time-variation cost is \(d_\tau/\tau=c\tau^h\sqrt L\), which is
smaller than the retained \(\tau^{h/8}\). Curvature, viscosity and
the nonlocal pressure tails are already included in (5). For each fixed
integer \(m\ge0\), disjoint-support derivative estimates also give

\[
 \|v\|_{H^m}\le C_m k^m\|v\|_2,\qquad v\in E_\tau.
 \tag{6}
\]

The chosen normalized real packets satisfy this simultaneously for all
fixed orders: cosine/sine averaging and \(k\delta\to\infty\) give
uniform normalization, without an order-dependent choice of quadrature.

## 2. Repairing every packet over this window

For \(v\in E_\tau\), variation of constants, applied to
\(y(t)=e^{\lambda_\tau(t-a_\tau)}v\), gives the exact identity

\[
 \mathcal S(t,a_\tau)v-e^{\lambda_\tau(t-a_\tau)}v
 =\int_{a_\tau}^t\mathcal S(t,s)e^{\lambda_\tau(s-a_\tau)}
       (\mathcal A(s)-\lambda_\tau)v\,ds.
 \tag{7}
\]

Divide by the positive exponential, and apply (3) and (5). Uniformly in
\(t\in[a_\tau,b_\tau]\),

\[
 \left\|e^{-\lambda_\tau(t-a_\tau)}
       \mathcal S(t,a_\tau)|_{E_\tau}-\iota_\tau\right\|_{E_\tau\to L^2}
 \le C\tau^{h/8}\lambda_\tau d_\tau
             e^{A_*\tau^{-1-h}\sqrt L\,d_\tau}
 \le C\sqrt L\,\tau^{3h/32}=:\epsilon_\tau.
 \tag{8}
\]

Here \(\iota_\tau\) is the inclusion. The last inequality absorbs the
fixed factor from \(L=1+\log(1/\tau)\); since \(A_*c\le h/32\),

\[
 \epsilon_\tau\le\tau^{h/16}\longrightarrow0
 \tag{9}
\]

after decreasing the allowed \(\tau\). In particular every unit vector
in the specified space, under its actual evolution from \(a_\tau\), obeys

\[
 (1-\epsilon_\tau)e^{\lambda_\tau d_\tau}
 \le\|\mathcal S(b_\tau,a_\tau)v\|_2
 \le(1+\epsilon_\tau)e^{\lambda_\tau d_\tau}.
 \tag{10}
\]

The gain is at least \(\tfrac12 e^{c c_\gamma\sqrt L/2}\) for small
\(\tau\), so the number of e-folds tends to infinity. This strengthens
the earlier unrestricted operator-norm lower bound on this shorter
window: the initial directions are now the specified packets. It makes
no claim about eigenvalues or a globally invariant unstable subspace.

Define the actual compressed transfer

\[
 B_\tau=P_\tau\mathcal S(b_\tau,a_\tau)|_{E_\tau}:E_\tau\to E_\tau.
\]

By (8),

\[
 B_\tau=e^{\lambda_\tau d_\tau}(I+D_\tau),\qquad
 \|D_\tau\|\le\epsilon_\tau<1/2,
\]
\[
 B_\tau^{-1}=e^{-\lambda_\tau d_\tau}
       \sum_{j=0}^{\infty}(-D_\tau)^j,
 \qquad
 \|B_\tau^{-1}\|\le2e^{-\lambda_\tau d_\tau}.
 \tag{11}
\]

This inverse involves finite-dimensional input and output spaces. It is
not an inverse of the full parabolic evolution on \(L^2\), nor does it
assert that \(\mathcal S E_\tau=E_\tau\).

## 3. A regular correction for the actual source in these measurements

Let the complete global zero-data response be

\[
 z_\tau(t)=\int_{a_\tau}^t\mathcal S(t,s)\mathbb Pf(s)\,ds.
 \tag{12}
\]

The translated-packet version of the reviewed source-response estimate
applies on (1), which is shorter than its permitted logarithmic window.
For fixed positive constants \(C_0,c_0\),

\[
 \sup_{a_\tau\le t\le b_\tau}\|P_\tau z_\tau(t)\|_2
 \le C_0 e^{-c_0\tau^{-h/16}}.
 \tag{13}
\]

It already charges the square root of the number of packets. The physical
force is zero on their support, but (13) uses the complete response,
including global pressure and boundary leakage; it does not replace
\(\mathbb Pf\) by zero in the exterior.

Choose the single perturbation at this restart time by the explicit formula

\[
 \eta_\tau=B_\tau^{-1}P_\tau z_\tau(b_\tau)\in E_\tau.
 \tag{14}
\]

Then the solution of the actual linear force-removal equation

\[
 e_\tau(t)=\mathcal S(t,a_\tau)\eta_\tau-z_\tau(t),\qquad
 (e_\tau)_t=\mathcal A(t)e_\tau-\mathbb Pf
\]

satisfies exactly

\[
 P_\tau e_\tau(b_\tau)=0.
 \tag{15}
\]

The sign in (14) is positive because the removed force enters negatively.
The correction is real, solenoidal, mean zero and compactly supported in
the same heat tube before periodization. Equations (6), (11) and (13) give
for every fixed integer \(m\ge0\)

\[
 \|\eta_\tau\|_{H^m}
 \le C_m k^m e^{-\lambda_\tau d_\tau}
                     e^{-c_0\tau^{-h/16}}
 \le C_m e^{-c_1\tau^{-h/16}},
 \tag{16}
\]

where \(c_1>0\) can be fixed independently of \(m\), with the smallness
threshold allowed to depend on \(m\). Its complete evolved contribution
is also small, since (8) bounds it by \(C e^{\lambda_\tau(t-a_\tau)}
\|\eta_\tau\|_2\). Thus this correction does not create a hidden large
unmeasured \(L^2\) contribution on its own window.

This is an exact finite-window cancellation of designated endpoint
observables. The remaining part of \(z_\tau\), low axial modes, annular
response and nonlinear error have not been cancelled. In particular (15)
is not the assertion that an unforced Navier–Stokes solution equals the
reference at the endpoint. The quadratic term
\(-\mathbb P\operatorname{div}(e\otimes e)\) is absent from this linear
construction and would need a separate correction and continuation proof.
The [nonlinear endpoint correction](nonlinear-endpoint-correction.md)
provides that separate finite-window extension. Its correction has a
polynomial nonlinear error budget; the stretched-exponential estimate
(16) belongs to the linear construction here.

## 4. The precise missing inverse at one fixed earlier time

Fix \(t_*<1\) once and choose a sequence of late windows as above, with
\(t_*<a_j<b_j\uparrow1\). The local constructions do not define an
initial datum at \(t_*\). The relevant source targets at \(b_j\) are

\[
 Z(t)=\int_{t_*}^t\mathcal S(t,s)\mathbb Pf(s)\,ds,
 \qquad
 \beta_{j,\ell}=\langle Z(b_j),v_{j,\ell}\rangle_2,
 \tag{17}
\]

where \(v_{j,\ell}\) is a real orthonormal basis of \(E_{\tau_j}\).
The exact decomposition is

\[
 Z(b_j)=\mathcal S(b_j,a_j)Z(a_j)+z_{\tau_j}(b_j).
 \tag{18}
\]

Only the second term has the smallness estimate (13). Discarding the
inherited first term would change the initial-value problem.

There is an explicit finite-dimensional diagnostic for the missing
one-datum inverse, without inventing a global frequency splitting. Fix
an integer \(m_0\ge0\), use the real solenoidal space \(H^{m_0}\), and
enumerate all the desired scalar measurements by an index \(p\). Write

\[
 w_p=(1-\Delta)^{-m_0}\mathcal S(b_p,t_*)^*v_p,
 \qquad
 \Gamma_{pq}=\langle w_q,w_p\rangle_{H^{m_0}}.
 \tag{19}
\]

The Sobolev norm here is defined by the multiplier \((1-\Delta)^{m_0/2}\).
The adjoint is the actual full periodic \(L^2\) adjoint; it carries every
pressure interaction and the reference coefficients between \(t_*\) and
\(b_p\). Smooth compact-time parabolic evolution makes each \(w_p\)
smooth. No spatial support property is claimed for these adjoint fields.

For the first \(N\) measurements, let \(\Gamma_N\) be their Gram matrix
and \(\beta_N\) the corresponding entries of (17). They are simultaneously
attainable by one \(H^{m_0}\) initial vector precisely when

\[
 \beta_N\in\operatorname{Ran}\Gamma_N.
 \tag{20}
\]

When this holds, the minimum-norm choice and its exact cost are

\[
 x_N=\sum_{p=1}^N w_p(\Gamma_N^\dagger\beta_N)_p,
 \qquad
 \|x_N\|_{H^{m_0}}^2
   =\beta_N^T\Gamma_N^\dagger\beta_N.
 \tag{21}
\]

Here \(\dagger\) denotes the Moore–Penrose inverse; it avoids an
unproved assertion that measurements at different times are independent.
To verify (20)–(21), split an arbitrary initial vector into its orthogonal
projection onto the span of the \(w_p\) and the common kernel of the
measurements. The latter changes none of their values and only increases
the norm. In the span, the constraints are precisely the Gram system.

Consequently a single \(H^{m_0}\) vector attaining every countable
measurement exists if and only if (20) holds for every \(N\) and

\[
 \sup_N\beta_N^T\Gamma_N^\dagger\beta_N<\infty.
 \tag{22}
\]

Necessity follows from minimum-norm optimality. For sufficiency, bounded
\(x_N\) have a weakly convergent subsequence in this Hilbert space. Each
fixed measurement is a continuous linear functional and is attained
exactly for all sufficiently large \(N\); the limit attains it as well.

A concrete stronger test yields a smooth datum. Define

\[
 (G_N^{(m)})_{pq}=\langle w_q,w_p\rangle_{H^m}.
\]

If, for every fixed integer \(m\ge0\),

\[
 \sup_N(\Gamma_N^\dagger\beta_N)^T
                 G_N^{(m)}(\Gamma_N^\dagger\beta_N)<\infty,
 \tag{23}
\]

then the same \(x_N\) are bounded in every fixed Sobolev space. A diagonal
subsequence, using compact embeddings on the torus, converges to one
smooth vector satisfying all measurements. This is a sufficient
regularity test on explicitly defined finite matrices, not a claim that
arbitrary independently chosen \(H^m\) minimizers coincide.

Neither (20), (22) nor (23) is proved here for a late-window sequence.
The local inverse (11) supplies no lower bound for these earlier-time
Gram matrices and no estimate of the inherited part of (18). The
natural-width radial boundary estimate likewise requires the actual
radial traces, axial matching and harmonic pressure. It does not make
those traces independent inputs of a global direct-sum evolution.

The finite-window conclusion is therefore positive and concrete: the
actual force excites the selected packet measurements so weakly that an
exponentially small, smooth late initial perturbation cancels them exactly.
The next one-datum estimate is the source-specific Gram cost (22), with
regularity such as (23), for the full targets (17). Even success there
would cancel only the listed linear observables. A terminal Green
construction controlling the entire error and its nonlinear interaction
would still be required for unforced singularity.

## 5. Review and scope

The coordinating agent and an independent source-audit agent each read
the complete argument, including the actual global Duhamel estimate,
dimension-independent packet inverse, force-removal sign, Sobolev
normalization, and fixed-earlier-time Gram criteria. Both reviews passed
without a mathematical correction at body SHA-256
`e087a5475cd43c73b251ae0a50a31f69ca2c058ec760f4975f80c71e9505c82b`.
Subsequent changes repair inline mathematics and control characters, add
the separate nonlinear-companion link, and record these reviews; they do
not change the displayed mathematics.

These are independent AI reviews of a written estimate, not formal PDE
certification or external expert acceptance. No simulation, full formal
build, actual global Gram bound, or terminal correction was produced.
