# What the released force estimates provide for a late unforced restart

Date: 8 September 2026.

**Subsequent calculation.** The [terminal-force note](terminal-force-nonzero.md)
now proves that the actual projected terminal trace is nonzero, using a
circulation in the fixed cutoff annulus. This resolves the undecided
nonvanishing question in this earlier source audit. Its smoothness and
restart identities remain valid. No unforced continuation conclusion follows.

**Bounded conclusion.** The released construction has a force that is flat at the singular spacetime point and extends smoothly through the terminal time. Its localized force is not asserted to vanish on a terminal time interval, or on the entire terminal spatial slice. The source supplies bounded fixed-order force norms, hence a small time integral on a short terminal interval. It does not supply the stability estimate needed to remove that force while preserving the constructed singularity. Restarting without forcing is a legitimate new initial-value problem; its subsequent behavior is not identified by the released theorem.

This is a source inspection and a short calculation, not a new verification of the external proof. The [existing evidence bridge](../navier-stokes/openai-result-bridge.md) records the separate native Lean build and its limits. No build, simulation, or canonical status change was performed here.

## 1. Pinned sources and normalization

The primary sources are OpenAI's [*Finite time blowup for Navier–Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), particularly Theorem 3.1 and §10, and [the formal source at commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538). The inspected PDF SHA-256 is 8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81.

Use the paper's viscosity-one construction, terminal time \(T=1\), \(\tau=1-t\), and fixed parameters

\[
A=\tfrac12+h,\qquad D=\tfrac12-h,\qquad 0<h<1/100.
\]

Here \(z\) denotes the axial spatial coordinate, \(r\) the radial coordinate, and \(q\) the external similarity scale. These are not the velocity or logarithmic scales in this project's earlier packet notes. The comparison identity below allows any fixed viscosity \(\nu>0\). No uniformity over choices of the external construction is claimed.

## 2. Local flatness and global terminal traces are different estimates

Theorem 3.1(iii) controls the complete local momentum residual \(\mathcal R(u,p)\): for every fixed Cartesian derivative order, every power \(N\), and every finite similarity radius \(X_1\),

\[
|\partial_x^\alpha\partial_t^j\mathcal R(u,p)|
\le C_{\alpha,j,N,X_1}q^N\qquad(0\le X\le X_1,\ q\downarrow0).
\tag{1}
\]

Beyond a fixed \(X_{\rm ext}\), the **uncut** field is an exact azimuthal heat flow with its radial pressure, so its residual is zero. After localization, the cutoffs equal one near the singular point. Equations (10.3) and (10.9) therefore give, on a neighborhood of that point,

\[
|\partial_x^\alpha\partial_t^j f(x,t)|
\le C_{\alpha,j,N}(\tau+|z|^{1/D})^N.
\tag{2}
\]

For example, inside that neighborhood and on \(|z|\le\tau^D\), this is at most \(2^NC_{\alpha,j,N}\tau^N\). The constants and the sufficiently small scale can depend on the derivative orders and \(N\). This is not an estimate on the entire fixed spatial support with right side \(C_N\tau^N\).

The actual global statement, Lemma 10.2, is

\[
\partial_x^\alpha\partial_t^j f(\cdot,t)
\longrightarrow\partial_x^\alpha F_j
\quad\hbox{uniformly on }\mathbb R^3,
\qquad
F_j\in C_c^\infty,\quad \partial_x^\alpha F_j(0)=0.
\tag{3}
\]

All \(F_j\) have one fixed compact spatial support \(K\). The functions \(F_j(x)\) away from the origin are the actual terminal residual derivatives; they are not declared zero. The inspected statements do not determine which particular \(F_j\) are nonzero. Neither \(F_0\equiv0\) nor its negation is being promoted by this audit.

The corresponding formal construction is explicit:

- [JointResidualLimits.boundaryLimits](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/JointResidualLimits.lean#L121) assigns zero tensors at the origin and the actual Taylor tensors of smooth one-sided extensions at other points. The extension agrees with the old residual, so these are genuine limits, not freely chosen boundary data.
- [MixedPeriodicAssembly](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedPeriodicAssembly.lean#L267) applies this construction to the cut residual and periodizes the limits. Zero jets at the origin give zero jets at its integer translates, not at every point of the torus.
- [CandidateFromLimits.force_boundary_jets](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CandidateFromLimits.lean#L128) preserves every one of these terminal tensors. The force is identically zero for \(t\ge2\), by force_zero_from; that is a different assertion from vanishing near \(t=1\).
- [ActualCandidateAssembly.Witness](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualCandidateAssembly.lean#L1120) retains the boundary-tensor identity for the assembled actual fields and force.

Lemma 10.3 extends the force to \(t>1\) by a Taylor–Borel series using all the \(F_j\), with order-dependent time cutoffs. It is not a zero extension at \(t=1\).

## 3. What remains in the localization region

A direct calculation makes the possible surviving terms concrete. Restrict to the exterior region where the potential is zero and the uncut fields are

\[
u=K(r,t)e_\theta,\qquad
p(r,t)=-\int_r^\infty K(\rho,t)^2\,\frac{d\rho}{\rho},
\qquad p_r=K^2/r.
\]

Here \(K_t=K_{rr}+r^{-1}K_r-r^{-2}K\); the notation \(t\) evaluates the paper's \(K(r,\tau)\) at \(\tau=1-t\). Late enough, the time cutoff is one. For the fixed axisymmetric spatial cutoff \(\chi(r,z)\), the localized fields in this region are \(U=\chi K e_\theta\), \(P=\chi p\). Their **complete** viscosity-one residual is

\[
f=
\left[\chi(1-\chi)\frac{K^2}{r}+p\chi_r\right]e_r
+p\chi_z e_z
-\left[K\Delta\chi+2\chi_r K_r\right]e_\theta,
\quad
\Delta\chi=\chi_{rr}+r^{-1}\chi_r+\chi_{zz}.
\tag{4}
\]

Indeed the heat equation cancels the terms multiplied by \(\chi\), the centrifugal term is \(-\chi^2K^2e_r/r\), and the pressure gradient supplies \(\chi K^2e_r/r+p\nabla\chi\). No term in (4) was discarded or absorbed into an unspecified pressure.

For every \(j\), the terminal jet in this exterior cutoff region is obtained by replacing \(K,p,K^2\) in (4) by

\[
K_j=\lim_{t\uparrow1}\partial_t^jK,
\quad p_j=\lim_{t\uparrow1}\partial_t^jp,
\quad (K^2)_j=\sum_{\ell=0}^j\binom j\ell K_\ell K_{j-\ell}.
\tag{5}
\]

These limits exist on fixed positive-radius sets by (10.7)–(10.8). Thus even where the uncut residual is exactly zero, the localized terminal force has explicit cutoff terms. This formula identifies what must be checked for cancellation; it does not assert that a selected coefficient of the fully constructed force has been proved nonzero. In the rest of the cutoff region, the full potential and its curl-cutoff terms must also be retained.

## 4. Usable global norm bounds, and the pressure projection

Equation (10.10) says exactly

\[
\partial_x^\alpha\partial_t^j f(x,t)
=\partial_x^\alpha F_j(x)
-\int_t^1\partial_x^\alpha\partial_t^{j+1}f(x,s)\,ds.
\tag{6}
\]

Consequently, for each fixed nonnegative integer \(s\), the following bounds hold for the fixed construction, with finite constants on a fixed late interval:

\[
\|f(t)-F_0\|_{H^s}\le C_s(1-t),\qquad
\sup_{t_*\le t\le1}\|f(t)\|_{H^s}\le M_s.
\tag{7}
\]

On \(\mathbb R^3\) use the common compact support; on the unit torus use periodicity and a fixed fundamental cell. These are consequences of the source's smooth extension, rather than extra exported dynamical stability theorems. Constants need not be small, and no bound uniform in \(s\) or a changed choice of construction is supplied.

Let \(\mathbb P\) be the usual orthogonal Leray projection on either domain, retaining the constant mode on the torus. Its \(H^s\to H^s\) norm is at most one in the Fourier norm. Thus, for \(t_*\le t_0<1\), (7) yields

\[
\|\mathbb P f(t)-\mathbb P F_0\|_{H^s}\le C_s(1-t),
\qquad
\int_{t_0}^1\|\mathbb P f(t)\|_{H^s}\,dt\le M_s(1-t_0).
\tag{8}
\]

The last bound is genuine smallness of a time integral. It is not decay of the instantaneous norm to zero. Such decay would require \(\mathbb P F_0=0\), which the inspected source statements do not establish.

Moreover, \(\mathbb P f=f-\nabla\Delta^{-1}\operatorname{div}f\) is spatially nonlocal. The paper explicitly allows \(\operatorname{div}f\ne0\) after (10.5). Flatness of \(f\) at the singular point does not establish flatness of \(\mathbb P f\) there. It cannot be applied to the projected equation without controlling the pressure contribution from the rest of the support.

No terminal-interval Leray-projected smallness or force-removal theorem was identified in the inspected final assembly and force exports. A targeted search of the pinned source tree was consistent with this: [ActualParticularControl](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualParticularControl.lean#L200) explicitly distinguishes its source-path/frame bounds from bounds on the solution or projected forcing. This is a bounded source finding, not a claim that a text search proves the absence of every logically derivable estimate.

## 5. The exact late-restart comparison

Fix \(0<t_0<1\). The constructed \(U(t_0)\) is a smooth divergence-free datum. Let \(V\) solve the ordinary **unforced** equation with \(V(t_0)=U(t_0)\), at the same viscosity, on its classical lifespan. This is a new evolution; it does not splice the old forced solution into a smooth unforced solution across \(t_0\).

On any interval where both are smooth, put \(w=V-U\). Subtraction gives

\[
\partial_t w-\nu\Delta w+(V\cdot\nabla)w+(w\cdot\nabla)U+\nabla\pi=-f,
\qquad \operatorname{div}w=0,\quad w(t_0)=0.
\tag{9}
\]

The exact energy identity is

\[
\frac12\frac d{dt}\|w\|_2^2+\nu\|\nabla w\|_2^2
=-\int w\cdot S(U)w\,dx-\langle\mathbb P f,w\rangle,
\quad S(U)=\tfrac12(\nabla U+\nabla U^T).
\tag{10}
\]

With \(a(t)=\|S(U)(t)\|_{L^\infty(\mathrm{op})}\), this proves

\[
\|w(t)\|_2\le
\int_{t_0}^t
\exp\!\left(\int_s^t a(\sigma)\,d\sigma\right)
\|\mathbb P f(s)\|_2\,ds.
\tag{11}
\]

Every coefficient here belongs to the actual constructed \(U\). Smoothness on shorter closed time intervals makes (11) meaningful there. The force bound (8) alone does not control it uniformly as \(t\uparrow1\); no terminal bound on this amplification factor has been extracted. Even an \(L^2\) comparison by itself would not preserve an unbounded pointwise velocity in a concentrating region. The paper's finite energy estimate in Lemma 10.4 also does not supply this missing comparison.

For clarity, [ResidualStability](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ResidualStability.lean) and [DiagonalResidual](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalResidual.lean#L159) control how the **momentum residual changes under already controlled perturbations**. They do not prove that the error generated by switching off \(f\) has those perturbation bounds. Lemma 10.5 compares solutions with the same force; it cannot identify \(V\) with \(U\).

## 6. Smallest unresolved estimate

The next necessary investigation is the response to the **actual** \(\mathbb P f\) around the **same** \(U\), including the exterior cutoff contributions (4). On each regular shorter interval, let \(\mathcal S_U(t,s)\) denote the linearized incompressible evolution generated by

\[
L_Uw=\nu\Delta w-\mathbb P\big((U\cdot\nabla)w+(w\cdot\nabla)U\big).
\]

Then the full error has the variation-of-constants representation

\[
w(t)=-\int_{t_0}^t\mathcal S_U(t,s)
\left[\mathbb P f(s)+\mathbb P((w\cdot\nabla)w)(s)\right]ds.
\tag{12}
\]

A useful force-removal argument would bound the first term in a norm controlling the velocity on the paper's growing core and close the second term in a compatible space. For example, an actual error \(o(\tau^{-A})\) along the paper's velocity-growth path would preserve its leading divergence, provided the new solution exists that far. Neither such a weighted response bound nor its nonlinear closure is supplied here.

The remaining uncertainty is therefore specific: how the global projected force, including its terminal trace away from the core, propagates into that core under the singular background. The source gives a smooth forcing input and a singular forced trajectory. Removing that input remains a further mathematical problem, not a corollary of terminal flatness.
