# A proved short continuation of the actual outgoing flow

8 September 2026. Written analytic lemma, derived for the existing localized-profile family. This is a further finite interval for exactly the same unforced Navier–Stokes solution and original datum. It gives a transported almost-affine region and a full, pressure-projected source bound. It does **not** give a signed lower bound for a new receiver, another handover, an infinite trajectory, or a solution of ROOT. No DNS or formal PDE certificate is used.

## 1. Statement at the existing endpoint

Use the actual solution and fixed-profile choices of [the localized-profile extension](../navier-stokes/localized-profile.md). All coordinates and norms below are its rescaled coordinates and unnormalized norms on the torus of side \(2\pi L\). Keep the same original datum and

\[
h=L^{-1/10},\quad \ell=\sqrt{\log(1/h)},\quad k=h^{3/2},
\quad\epsilon=\nu h^4>0.
\]

Translate only the **time label**: \(u(\tau)=Q_h(t_f+\tau)\), so \(u_0=Q_h(t_f)\). This does not reset its initial preparation cost. The existing theorem supplies, with fixed constants selected before \(h\to0\),

\[
\|\nabla u_0\|_\infty\le P_h:=C_0\ell^{11/8},\qquad
\|u_0\|_{H^{12}}\le H_h:=h^{-117/8}G_h,
\quad\log G_h=o(\ell^2),                                      \tag{1}
\]

and an endpoint ball \(B_R(x_0)\), \(R=c_0k\), with

\[
\sup_{B_R(x_0)}|\nabla u_0-A_*|\le\delta_h:=h^{1/48}G_h,
\qquad |S(A_*)|_F\ge c_1\ell^{11/8}.                          \tag{2}
\]

Enlarge \(C_0,G_h\) finitely if needed so \(P_h\ge1,H_h\ge e\). Set

\[
K_h=1+\log L+\log(e+H_h)=O(\ell^2),\qquad
\Delta_h=\frac{c}{P_hK_h}.                                   \tag{3}
\]

For the global gradient input in (1), the localized-profile source's (3) controls the primary whole-support gradient, its (2) controls the base \(q\), and its (34), (36) control all correctors and the actual nonlinear error. The source's (36) supplies \(H_h\), and its (38) supplies the ball estimate (2). The bound on the primary phase derivative also uses heat contraction for the one fixed smooth profile. No supremum over the whole torus has been inferred from a central value.

For one sufficiently small fixed \(c>0\), the same strong solution exists through \(t_f+\Delta_h\), with

\[
\sup_{0\le\tau\le\Delta_h}\|\nabla u(\tau)\|_\infty\le2P_h,
\qquad \sup_{0\le\tau\le\Delta_h}\|u(\tau)\|_{H^{12}}\le2H_h,
\quad\int_0^{\Delta_h}\|\nabla u\|_\infty\,d\tau\le\frac{2c}{K_h}.
                                                                    \tag{4}
\]

In particular a fixed sufficiently small multiple of \(\ell^{-27/8}\) is an available additional lifetime. Let \(\Phi_\tau\) be the actual \(u\)-flow starting at \(\tau=0\). For \(0<\tau\le\Delta_h\),

\[
\sup_{a\in B_{R/2}(x_0)}
 |\nabla u(\tau,\Phi_\tau(a))-A_*|
\le \delta_h+C P_h\exp\!\left(-\frac{c'R^2}{\epsilon\tau}\right)
                  +C P_h^2K_h\tau.                            \tag{5}
\]

The constant in the exponential is uniform on this interval. In particular, on the shorter but still logarithmic interval

\[
0\le\tau\le\ell^{-5},
\qquad
\sup_{a\in B_{R/2}(x_0)}
 |\nabla u(\tau,\Phi_\tau(a))-A_*|=O(\ell^{-1/4})=o(1).        \tag{6}
\]

The transported set contains a ball of radius \(R/3\) about \(\Phi_\tau(x_0)\) for small \(h\). Thus the endpoint almost-affine gradient persists on a specified moving region of the **actual full flow**. Its strain lower bound remains \(c\ell^{11/8}\). This is persistence of the already obtained strain, not new amplification.

Equation (6) is an absolute small error in the **rescaled first spatial derivative**. It does not assert equally small errors in higher spatial derivatives or in material time derivatives. Those stronger jets, if needed by a receiving-wave construction, remain a separate estimate.

## 2. The pressure estimate, including the growing torus

The following elementary logarithmic estimate is sufficient. Let \(v\) be smooth and solenoidal on \(\mathbb T_L^3\), \(L\ge1\), and let its periodic pressure obey

\[
\Delta p=-\operatorname{tr}[(\nabla v)^2].
\]

The right side has spatial mean zero by integration by parts. Write \(P=\max(1,\|\nabla v\|_\infty)\) and \(H=\max(e,\|v\|_{H^{12}})\). Then

\[
\|\nabla^2p\|_\infty
 \le C P^2\,[1+\log L+\log(e+H)].                            \tag{7}
\]

Here and below matrix norms are fixed equivalent Euclidean norms. No boundedness of an unlocalized Riesz transform on \(L^\infty\) is assumed.

To prove (7), put \(f=\operatorname{tr}[(\nabla v)^2]\). Resolve all **nonzero** frequencies into smooth dyadic annuli, starting at \(2^{j_L}\asymp L^{-1}\). On each annulus the multiplier of \(\nabla^2\Delta^{-1}\), combined with the smooth cutoff, has a convolution kernel with uniformly bounded \(L^1\) norm. This follows by periodizing the Euclidean annular kernel; its \(L^1\) norm on one period is at most the Euclidean \(L^1\) norm. Consequently every block is bounded by \(CP^2\).

For \(j\ge0\), the uniform Bernstein inequality and the product estimate give the stronger bound

\[
\|\Delta_j\nabla^2p\|_\infty
\le C2^{3j/2}\|\Delta_j f\|_2
\le C2^{-19j/2}\|f\|_{H^{11}}
\le C2^{-19j/2}PH.                                          \tag{8}
\]

The product estimate is the usual differentiated tame product bound \(\|ab\|_{H^{11}}\le C(\|a\|_\infty\|b\|_{H^{11}}+\|b\|_\infty\|a\|_{H^{11}})\). The same annular-kernel argument gives uniform constants on these tori. Choose

\[
J=\max\left(0,\left\lceil\frac{2}{19}
                       \log_2(e+H/P)\right\rceil\right).
\]

The sum above \(J\) is \(O(P^2)\); the remaining number of blocks is at most \(C[1+\log L+\log(e+H)]\). This proves (7). In particular the low modes down to \(1/L\) are **charged** through \(\log L\), rather than discarded using an invalid uniform Poincaré constant.

## 3. Strong lifetime from a gradient maximum principle

Let \(A=\nabla u\), with entries \(A_{ij}=\partial_j u_i\). The exact differentiated NS equation is

\[
(\partial_\tau+u\cdot\nabla-\epsilon\Delta)A
       =-A^2-\nabla^2p.                                    \tag{9}
\]

The scalar maximum principle applied to a smooth approximation of \(|A|\), followed by its limit, implies

\[
\|A(\tau)\|_\infty
 \le\|A(0)\|_\infty+
 C\int_0^\tau P(s)^2[1+\log L+\log(e+H(s))]\,ds.            \tag{10}
\]

The diffusion is dissipative at the maximum; (10) does **not** require a small bound for \(\epsilon\nabla^3u_0\). Independently the integer Sobolev energy inequality gives

\[
H(\tau)\le H_h\exp\left(C_{12}\int_0^\tau P(s)\,ds\right).
                                                                    \tag{11}
\]

On a bootstrap interval where \(P\le2P_h\), equations (3), (11) imply \(H\le2H_h\) and \(1+\log L+\log(e+H)\le2K_h\), provided the fixed \(c\) is small enough. Substitution in (10) improves \(P\le2P_h\) to \(P\le(3/2)P_h\). The \(H^{12}\) local existence and continuation theorem, already used by the original construction, therefore prevents breakdown before \(\Delta_h\) and proves (4). This is a separate continuation proof, not an assumption that smoothness at \(t_f\) gives a uniform further lifetime.

## 4. Transported core: pressure and diffusive leakage are retained

By (4), (7), the right side \(F=-A^2-\nabla^2p\) of (9) has global bound

\[
\sup_{[0,\Delta_h]}\|F\|_\infty\le CP_h^2K_h.              \tag{12}
\]

Apply the backward diffusion representation componentwise to (9), subtracting the fixed constant matrix \(A_*\). For a final point \(x=\Phi_\tau(a)\), the backward process is

\[
dX_s=-u(\tau-s,X_s)\,ds+\sqrt{2\epsilon}\,dB_s,
\quad X_0=x,\quad 0\le s\le\tau.
\]

Its deterministic counterpart \(Y_s\) ends at \(Y_\tau=a\). Lift both paths to the covering space. Since the drift has Lipschitz bound \(2P_h\), their integral equations and Gronwall imply

\[
\sup_{s\le\tau}|X_s-Y_s|
\le\sqrt{2\epsilon}\,e^{2P_h\tau}\sup_{s\le\tau}|B_s|.
\]

For \(a\in B_{R/2}(x_0)\), leaving \(B_R(x_0)\) at the initial-time endpoint requires this separation to be at least \(R/2\). The one-dimensional reflection bound in each of three coordinates and a union bound yield

\[
\mathbb P\{X_\tau\notin B_R(x_0)\}
 \le C\exp\left[-\frac{c R^2 e^{-4P_h\tau}}{\epsilon\tau}\right]
 \le C\exp\left[-\frac{c'R^2}{\epsilon\tau}\right].          \tag{13}
\]

Using periodic distance can only decrease the event relative to the covering-space bound. The deterministic source term contributes at most (12) times \(\tau\). At the initial endpoint the error is at most \(\delta_h\) inside the core and at most \(CP_h\) outside; the latter also uses \(|A_*|\le CP_h\), a consequence of (1), (2). The representation therefore proves (5).

For \(\tau\le\ell^{-5}\),

\[
P_h^2K_h\tau\le C\ell^{11/4+2-5}=C\ell^{-1/4},
\qquad
\frac{R^2}{\epsilon\tau}\ge c_\nu h^{-1}\ell^5.
\]

Both \(\delta_h\) and the Gaussian leakage are smaller than the stated logarithmic error, giving (6). The flow and its inverse have Lipschitz constants at most \(e^{2P_h\tau}\); hence the image of \(B_{R/2}(x_0)\) contains \(B_{(R/2)e^{-2P_h\tau}}(\Phi_\tau(x_0))\). This contains the claimed \(R/3\) ball. On any such ball, integrating (6) along line segments also gives an almost-affine **velocity difference** after subtracting the actual center velocity, with error at most \(Ck\ell^{-1/4}\).

This subtraction compares values at a fixed time. It is not an invocation of a time-dependent Galilean symmetry, and no globally affine pressure or frozen host history has replaced the actual pressure.

## 5. Actual future source: exact Duhamel formula and upper bound

The initial rescaled kinetic energy is bounded independently of \(h,L\). Indeed \(V\) is one fixed compact field; the original primary packet has velocity amplitude \(h/\ell\) and width \(h^{1/2}\); the supplied receiver and its curl terms have an \(L^2\) bound tending to zero from the existing packet estimates. The ordinary unforced energy identity then gives

\[
\sup_{\tau\le\Delta_h}\|u(\tau)\|_2\le C_E.                \tag{14}
\]

A uniform local interpolation estimate gives \(\|u\|_\infty\le C(\|u\|_2+\|u\|_2^{2/5}\|\nabla u\|_\infty^{3/5})\le C_E P_h\). One elementary proof integrates \(|u|^2\) over a ball of radius \(\min(1,\|u\|_\infty/(2\|\nabla u\|_\infty))\) about an approximate maximum. Such balls have uniform Euclidean volume on \(L\ge1\).

For the full nonlinearity \(N(u)=\mathbb P\operatorname{div}(u\otimes u)\), the uniform \(L^2\) boundedness of the Leray multiplier and the tame product estimate imply

\[
\|N(u)\|_{H^{11}}
\le C\left(\|u\|_\infty\|u\|_{H^{12}}
                 +\|\nabla u\|_\infty\|u\|_{H^{11}}\right)
\le C_E P_hH_h.                                            \tag{15}
\]

Let \(P_{>R_0}\) be the sharp Fourier projection onto \(|n|/L>R_0\), \(R_0\ge1\). The exact future-generated contribution relative to linear heat evolution of the **complete actual endpoint** is

\[
W_{R_0}(\tau)
:=P_{>R_0}u(\tau)-e^{\epsilon\tau\Delta}P_{>R_0}u_0
=-\int_0^\tau e^{\epsilon(\tau-s)\Delta}
                    P_{>R_0}N(u(s))\,ds.                   \tag{16}
\]

This retains both ordered quadratic interactions and the full pressure projection. It is not a frozen two-wave calculation. Uniform Fourier Cauchy–Schwarz, with the same unnormalized convention as [the next-seed estimate](../navier-stokes/next-seed-analysis.md), gives

\[
\|\nabla P_{>R_0}e^{\epsilon a\Delta}v\|_\infty
 \le C R_0^{-17/2}e^{-\epsilon R_0^2a}\|v\|_{H^{11}}.
\]

Consequently

\[
\|\nabla W_{R_0}(\tau)\|_\infty
\le C_E P_hH_h R_0^{-17/2}
       \min\{\tau,(\epsilon R_0^2)^{-1}\}.                 \tag{17}
\]

At \(R_0=h^{-9/4}\), this is at most

\[
C_E P_hG_h h^{9/2}\min\{\tau,\nu^{-1}h^{1/2}\}
\le C_{E,\nu}P_hG_hh^5.                                   \tag{18}
\]

There is a stronger bound for the **net** contribution from the propagated \(H^{12}\) budget: by (4) and the old uniform tail lemma,

\[
\sup_{\tau\le\Delta_h}\|\nabla P_{>h^{-\beta}}u(\tau)\|_\infty
 \le C h^{(19/2)\beta-117/8}G_h.                            \tag{19}
\]

The heat evolution of \(u_0\) has the same bound, so their difference in (16) has it too, up to a factor of two. At \(\beta=9/4\), both the actual high-pass gradient and the net contribution \(W_{R_0}\\) are \(O(h^{27/4}G_h)\). Equation (17) is useful for identifying the complete source and its diffusion budget; it is not claimed to improve (19).

No particular signed mode, ray, or polarization has been isolated in (16). It includes the subsequent nonlinear evolution of already present signals as well as genuinely newly generated ones, with all cancellations. Thus it cannot be called an independently supplied third seed, nor does an upper bound furnish a signed source lower bound.

## 6. Consequence for the next attempt

The original endpoint is now extended into an actual transported state. This removes the specific absence of any proved further lifetime and core persistence. It also extends the existing fine-frequency exclusion over that additional lifetime: for every fixed \(\beta>117/76\), (19) tends to zero. The new interval contributes only \(O(\ell^{-2})\) to the accumulated strain clock, so it does not meet the necessary \(O(\ell^2)\) clock for fixed positive fine-scale activation.

The missing step is now sharper: exploit a specified departure from the already studied invariant two-wave geometry to prove a signed receiver contribution, or continue the actual outgoing host much longer with a usable transfer/error budget. The nearly constant matrix in (6) alone does not identify the pressure Hessian with that of the exact affine model. Estimate (12) allows the actual pressure to change the matrix by \(CP_h^2K_h\tau\), and the present argument must pay that cost. Optimizing fixed constants in this bound will not create the missing clock or receiver.

Physical coordinates are unchanged: the additional physical time is \(h^{24}\Delta_h\), the transported ball has physical radius comparable to \(k/L=h^{23/2}\), and velocity gradients gain the common factor \(h^{-24}\). Statements such as the error \(o(1)\) in (6) concern the displayed rescaled gradient; the relative error compared with the existing physical strain still tends to zero. There is no new datum or viscosity choice between \(t_f\) and the new endpoint.

### Evidence and review boundary

The pressure estimate, maximum-principle continuation, drift–diffusion localization and source estimate are written arguments given above. An independent AI agent rederived the pressure estimate including low torus modes, the endpoint inputs, the \(H^{12}\) bootstrap, backward-diffusion sign and leakage, transported ball, and complete source upper bound; no load-bearing defect was found. The coordinating agent separately checked the global gradient input. Seven exact rational checks confirmed the lifetime, core-error, history, source/tail, damping, and physical-radius exponents. Arithmetic checks cannot certify these PDE arguments. No new experiment, claim-graph node, independent external mathematical review, or Lean certificate is implied. ROOT, `\(E′\)` and FORCED-D remain OPEN.
