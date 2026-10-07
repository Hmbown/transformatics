# Cancelling a growing packet space in the full nonlinear evolution

8 September 2026. Restricted written proof with two independent AI-agent
reviews. On one late interval, a small smooth change to the initial datum
can cancel the entire endpoint error projected onto the specified exterior
packet space. The dimension of that space grows as the restart approaches
time one. Pressure and the full nonlinear equation are retained. This is
not a correction at one fixed earlier time or an unforced singularity.

The reference is the viscosity-one construction on the unit torus pinned
in the [external source record](../navier-stokes/openai-result-bridge.md).
The inputs are the [packed exterior quasimodes](initial-correction.md#5-actual-heat-exterior-packets-form-a-large-common-quasimode-space),
the [complete Gevrey packet response](local-response-bound.md),
and the [nonlinear comparison](nonlinear-force-comparison.md).
All construction parameters, including \(0<h<1/100\), are fixed.

## 1. One fixed packet space on one interval

Set
\[
t_0=1-\tau,\quad L=1+\log(1/\tau),\quad
K=\tau^{-(1+h)/2},\quad
k=\tau^{-1/2-h/4},\quad \ell=\tau^{1/2+h/8}.
\tag{1}
\]
Let \(E_\tau\) be the real Gevrey packet space from the cited results,
and \(P_\tau\) its orthogonal projection in solenoidal \(L^2\).
The packets have disjoint supports in the actual source-free heat
exterior. They are smooth, mean zero and exactly divergence free. Their
number and fixed derivative norms satisfy
\[
\dim E_\tau\asymp\tau^{-9h/8},\qquad
\|v\|_{H^j}\le C_j k^j\|v\|_2\quad(v\in E_\tau).
\tag{2}
\]
Constants are independent of the dimension. In the scaled norm
\[
X_K(v)^2=\sum_{j=0}^3K^{-2j}\|\nabla^jv\|_2^2,
\tag{3}
\]
we therefore have \(\|v\|_2\le X_K(v)\le C_E\|v\|_2\), because
\(k/K=\tau^{h/4}\le1\).

Write \(\mathcal A_U(t)\) for the full Leray-projected linearization
about the actual reference. There is a common positive growth parameter
\(\lambda=\gamma-k^2\asymp K^2\), with \(\gamma=c_\gamma K^2\),
such that
\[
\|(\lambda-\mathcal A_U(t))v\|_2
\le C\lambda\tau^{h/8}\|v\|_2
\quad(v\in E_\tau).
\tag{4}
\]
This holds on the previously proved logarithmic flight, hence also on the
shorter interval chosen below. The pressure tails in (4) have already been
included before taking the norm. \(E_\tau\) is a fixed test and initial
parameter space; it is not asserted to be an invariant spectral subspace.

Fix
\[
\delta=h/64,\qquad d=cK^{-2}\sqrt L,
\qquad t_1=t_0+d,
\tag{5}
\]
where \(c>0\) is sufficiently small depending only on the fixed source
and energy constants. Specifically choose a constant \(C_*\) dominating
both the scaled \(H^3\) comparison coefficient and the \(L^2\) energy
coefficient of \(U\), and impose \(C_*c\le\delta\). We use
\[
a=C_*K^2\sqrt L,\qquad
e^{ad}\le e^\delta\tau^{-\delta}.
\tag{6}
\]
This choice is smaller than the available comparison window. It is made
before \(\tau\) tends to zero. Also
\[
A_\tau:=e^{\lambda d}\longrightarrow\infty,
\qquad \lambda d=c c_\gamma\sqrt L-o(1).
\tag{7}
\]

## 2. Uniform nonlinear existence for the required initial parameters

For a smooth \(\xi\in E_\tau\), let \(V^\xi\) be the unforced
solution starting from \(U(t_0)+\xi\), and put \(E^\xi=V^\xi-U\).
The difference obeys exactly
\[
(E^\xi)_t=\mathcal A_U E^\xi-\mathbb P f
-\mathbb P((E^\xi\cdot\nabla)E^\xi),\qquad E^\xi(t_0)=\xi.
\tag{8}
\]
Its pressure difference satisfies
\[
\Delta\Pi^\xi=-\operatorname{div}f
-\partial_i\partial_j(U_iE^\xi_j+E^\xi_iU_j+E^\xi_iE^\xi_j).
\tag{9}
\]
In particular the quadratic pressure on the full torus is retained.

For \(X_K(\xi)\le d\), the proof of the preceding nonlinear comparison,
with the smaller constant in (5), gives smooth existence through \(t_1\)
and
\[
X_K(E^\xi(t_0+s))\le C(X_K(\xi)+s)e^{as},\quad 0\le s\le d.
\tag{10}
\]
The fixed constant includes the bounded \(H^3\) force norm. Indeed its
Riccati inequality is \(X'\le aX+C K^{5/2}X^2+C_f\); the quadratic
bootstrap cost is at most
\[
C K^{5/2}d^2e^{ad}
\le C\tau^{3(1+h)/4-\delta}L\longrightarrow0.
\tag{11}
\]
The bounded \(H^3\) norm at each fixed \(\tau\) proves strong
continuation; one does not assume that the local lifespan covers the
interval in advance.

The uniform consequences used below are
\[
\|E^\xi\|_\infty\le C K^{3/2}d\tau^{-\delta},\qquad
\|\nabla E^\xi\|_\infty\le C K^{5/2}d\tau^{-\delta},
\tag{12}
\]
and
\[
\int_{t_0}^{t_1}\|\nabla E^\xi\|_\infty\,dt
\le C K^{5/2}d^2\tau^{-\delta}=o(1).
\tag{13}
\]
Thus the actual linearization about each \(V^\xi\) in this parameter
ball has the uniform \(L^2\) energy bound
\[
\|\mathcal S_{V^\xi}(t,s)\|_{2\to2}
\le C e^{a(t-s)}\quad(t_0\le s\le t\le t_1).
\tag{14}
\]
Transport is skew and pressure is orthogonal in this estimate. The extra
factor from (13) is bounded uniformly. This is a finite-window estimate,
not a uniform terminal stability assertion.

## 3. The nonlinear endpoint defect is smaller than the whole error

First take \(\xi=0\). Let \(z\) be the zero-data linear response
\(z_t=\mathcal A_U z-\mathbb P f\). The previously proved packet
bound gives
\[
\|P_\tau z(t_1)\|_2\le C e^{-b\tau^{-h/16}}
\tag{15}
\]
for a fixed \(b>0\). Its sign of forcing is immaterial for this norm
bound. The complete nonlinear Duhamel formula is
\[
E^0(t_1)=z(t_1)-\int_{t_0}^{t_1}\mathcal S_U(t_1,s)
\mathbb P((E^0\cdot\nabla)E^0)(s)\,ds.
\tag{16}
\]
Using the full propagator bound rather than a localized replacement,
\[
\|\mathbb P((E^0\cdot\nabla)E^0)\|_2
\le\|E^0\|_\infty\|\nabla E^0\|_2
\le C K^{5/2}X_K(E^0)^2.
\tag{17}
\]
Equation (10) at zero data then bounds the integral in (16) by
\(C K^{5/2}d^3e^{2ad}\). Hence, for a fixed sufficiently large \(C_q\),
\[
\|P_\tau E^0(t_1)\|_2\le q_\tau,
\qquad
q_\tau=C_q\left(e^{-b\tau^{-h/16}}
                   +K^{5/2}d^3\tau^{-2\delta}\right).
\tag{18}
\]
In particular
\[
q_\tau/d\longrightarrow0,
\qquad
K^{5/2}d^3\tau^{-2\delta}
=c^3\tau^{7(1+h)/4-2\delta}L^{3/2}.
\tag{19}
\]
The second term is a nonlinear upper bound; it is not stretched
exponentially small. No claim of nonlinear Gevrey localization is used.

## 4. An invertible derivative for the actual endpoint map

Define on the finite-dimensional parameter ball
\[
\mathcal F_\tau(\xi)=P_\tau(V^\xi(t_1)-U(t_1))\in E_\tau.
\tag{20}
\]
For fixed \(\tau\), local strong-solution dependence on smooth initial
data makes this map continuously differentiable. Differentiating (8)
shows, for \(v\in E_\tau\),
\[
D\mathcal F_\tau(\xi)v=P_\tau\mathcal S_{V^\xi}(t_1,t_0)v.
\tag{21}
\]
One can also obtain this derivative from the difference equation and its
quadratic remainder in \(H^3\); the parameter space is finite-dimensional
and consists of smooth data. The dimension-independent bounds below use
\(L^2\), not a coordinatewise derivative estimate.

By (2), (4) and (12), the comparison path \(e^{\lambda s}v\) has
residual against \(\mathcal A_{V^\xi}\) at most
\[
e^{\lambda s}\left(C\lambda\tau^{h/8}
+C K^{5/2}d\tau^{-\delta}\right)\|v\|_2.
\tag{22}
\]
Here the additional terms are exactly
\(\mathbb P((E^\xi\cdot\nabla)v+(v\cdot\nabla)E^\xi)\).
They are bounded by
\(C(k\|E^\xi\|_\infty+\|\nabla E^\xi\|_\infty)\|v\|_2\),
and \(k\le K\). There is no pressure deletion or assumption that the
nonlinear error is supported in the packet tube.

Variation of constants, (14), and \(\lambda>0\) now give uniformly
for \(X_K(\xi)\le d\),
\[
\left\|A_\tau^{-1}\mathcal S_{V^\xi}(t_1,t_0)|_{E_\tau}
             -I_{E_\tau\hookrightarrow L^2}\right\|_{2\to2}
\le\eta_\tau,
\tag{23}
\]
where
\[
\eta_\tau\le C\left(
\tau^{h/8-\delta}\sqrt L+
\tau^{3(1+h)/4-2\delta}L\right)\longrightarrow0.
\tag{24}
\]
For example, after dividing the Duhamel integral by \(A_\tau\), its
exponential factor is bounded by \(C e^{ad}\le C\tau^{-\delta}\);
multiplication by \(d\) and (22) gives (24). Projection in (21) is
a contraction and is the identity on the comparison vector \(v\).
Consequently
\[
\|A_\tau^{-1}D\mathcal F_\tau(\xi)-I_{E_\tau}\|_{2\to2}
\le\eta_\tau.
\tag{25}
\]
This controls every parameter direction simultaneously. It also proves
growth of these specified initial vectors in the actual variational
evolution on this shorter interval. It is not an eigenvalue count.

## 5. A single corrected datum for the finite endpoint condition

Put \(r_\tau=2A_\tau^{-1}q_\tau\). By (19),
\(C_Er_\tau\le d\) for sufficiently small \(\tau\). Thus the closed
\(L^2\) ball \(B_{r_\tau}\subset E_\tau\) lies in the existence
region of §2. Define
\[
\mathcal G_\tau(\xi)=\xi-A_\tau^{-1}\mathcal F_\tau(\xi).
\tag{26}
\]
Equations (18) and (25) give
\(\|\mathcal G_\tau(0)\|_2\le r_\tau/2\) and a Lipschitz
constant at most \(\eta_\tau\le1/4\) on the ball. Hence it maps
the ball into itself and is a contraction. Its unique fixed point
\(\xi_\tau\) satisfies
\[
\boxed{\quad
\|\xi_\tau\|_2\le2e^{-\lambda d}q_\tau,
\qquad
P_\tau(V^{\xi_\tau}(t_1)-U(t_1))=0.
\quad}
\tag{27}
\]
The initial datum is precisely \(U(t_0)+\xi_\tau\), chosen once
for this interval. It is smooth, solenoidal and has the same mean as the
reference datum. The resulting velocity solves the full unforced equation
and continues through \(t_1\). Every fixed Sobolev norm of the correction
is bounded by \(C_j k^j e^{-\lambda d}q_\tau\); these norms need not
tend to zero at every derivative order as \(\tau\) tends to zero.

Since \(X_K(\xi_\tau)\le d\), (12)–(13) yield
\[
\sup_{[t_0,t_1]}\|V^{\xi_\tau}-U\|_\infty
\le C\tau^{(1+h)/4-\delta}\sqrt L\longrightarrow0,
\tag{28}
\]
\[
\int_{t_0}^{t_1}\|\nabla(V^{\xi_\tau}-U)\|_\infty\,dt
\le C\tau^{3(1+h)/4-\delta}L\longrightarrow0.
\tag{29}
\]
Thus endpoint cancellation does not sacrifice the finite nonlinear
comparison. It cancels the chosen projection exactly, not the whole error.

## 6. The remaining one-datum problem

The correction lies in a growing-dimensional packet space, but is selected
at a restart time \(t_0=1-\tau\) that changes with the scale. Equation
(27) supplies no preimage at one fixed earlier time. Forward diffusion
cannot be inverted on arbitrary smooth data, and a finite compressed
inverse on \([t_0,t_1]\) does not give such an earlier inverse.

A global construction would need compatible endpoint constraints at all
relevant scales and a convergent correction at one fixed initial time.
It must also control the complementary error, actual pressure and nonlinear
interactions between the constraints. The common packet projection is
neither invariant nor a verified description of every growing direction.
Those are additional obligations, not consequences of (27). Unforced ROOT
and E-prime remain open.

## Review and verification scope

The complete argument in §§1–6 received separate full reads by the
outgoing-evolution and continuation/pressure reviewers. Both passed the
uniform scaled initial allowance, actual nonlinear continuation, full
variational pressure, two derivative-error exponents, and the
dimension-independent contraction. The root author checked the source
inputs and integrated those reviews. The reviewed mathematical body had
SHA-256 `a97ccf5e02e542a4d1761ce45743e1adf1e1d2a1c5188592c33a5e08444b064f`;
subsequent changes record review status only.

The [symbolic companion](checks/check-force-removal.py)
checks elementary scaling identities separately. It does not verify the
PDE estimates, identify the actual source or construct the fixed point
numerically. These are written analytic results reviewed by AI agents,
not a formal PDE certificate or external expert acceptance.
