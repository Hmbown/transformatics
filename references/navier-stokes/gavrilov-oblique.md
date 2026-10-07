# Oblique polarization instability on selected compact Gavrilov flows

**Date:** 8 September 2026 UTC / 7 September Pacific.  
**Standing:** PROVED analytic existence result for the **inviscid principal
polarization ODE** on specified smooth compact steady Euler backgrounds.
The smallness threshold is existential, not numerically computed.
**ROOT and `(E′)` remain OPEN.** No finite-wavelength NS amplification,
infinite cascade, or priority/novelty claim is made.

Pins: [exact algebra](../../experiments/nse_gavrilov_oblique.py),
[independent controls](../../tests/test_nse_gavrilov_oblique.py),
[receipt](../../artifacts/enstrophy_sup/nse_gavrilov_oblique.json);
node `nse-gavrilov-oblique-instability`, outside the critical path into ROOT.

This executes the oblique-carrier task in the
[steady-background note](steady-background.md). The
pressure-normal carrier was neutral, but a different orientation and a
specified pressure-cutoff slope yield an unstable two-dimensional system.
The proof transfers its growth to actual Gavrilov flows by analytic
coordinate estimates and an exact rotational return, rather than treating
a straight-column approximation as the desired flow.

## 1. Statement and imported geometry

Use the original radius-one Gavrilov field `(U,P)` before localization.
[Gavrilov, section 3](https://arxiv.org/html/1810.08020v1), proves

\[
\operatorname{div}U=0,\qquad (U\cdot\nabla)U=-\nabla P,
\qquad U\cdot\nabla P=0.
\tag{1}
\]

For a smooth scalar cutoff f, `V=f(P)U` is again steady Euler, with
pressure gradient `∇Ṕ=f(P)²∇P`. Cutoffs supported in a sufficiently small
positive pressure annulus give smooth compact velocities on R³. This
is an external existence theorem for Euler, not for stationary viscous NS.

[Baldi, Theorem 1.1](https://arxiv.org/html/2302.02982v1), supplies
coordinates `Φ(σ,β,I)` and analytic functions K,R with

\[
P\circ\Phi=K(I),\quad K(I)=I+O(I^3),\quad
q(I)=\sqrt I\,R(I),\quad R(I)=1+O(I),
\tag{2}
\]

and `K'>0`, `q'>0` for sufficiently small I>0. For the localized field,

\[
\dot\sigma=\Omega_1(I)=f(K(I))K'(I),\quad
\dot\beta=\Omega_2(I)=q(I)\Omega_1(I),\quad \dot I=0.
\tag{3}
\]

The position map has the axisymmetric form

\[
\Phi=(\rho\cos(\beta+\eta),\rho\sin(\beta+\eta),\zeta),
\quad
\rho=1+\sqrt{2I}\sin\sigma+O(I),\quad
\zeta=\sqrt{2I}\cos\sigma+O(I),\quad \eta=O(I).
\tag{4}
\]

Crucially, Φ is analytic in `(σ,β,√I)` as specified in that theorem.
Thus these are differentiable analytic remainders, not just bounds on
position values. On the compact angle torus, fixed angle derivatives
of the stated remainders have the same powers. One radial derivative
lowers the power by one. This supplies the uniform jet estimates below.

Fix one C∞ bump χ supported in `[3/4,3/2]` and equal to one near 1.
An explicit choice is

\[
h(s)={\psi(s)\over\psi(s)+\psi(1-s)},\quad
\psi(s)=\begin{cases}e^{-1/s}&s>0,\\0&s\le0,\end{cases}
\quad
\chi(s)=h(8(s-3/4))h(4(3/2-s)).
\tag{5}
\]

For every sufficiently large integer j, define Iⱼ uniquely by
`q(Iⱼ)=1/j`, and set

\[
P_j=K(I_j),\quad r_j=\sqrt{2I_j},\quad
f_j(P)=e^{1-P/P_j}\chi(P/P_j),\quad V_j=f_j(P)U.
\tag{6}
\]

The smooth field Vⱼ is compactly supported after the standard zero
extension. It satisfies `fⱼ(Pⱼ)=1`, `fⱼ'(Pⱼ)=−1/Pⱼ`. We do not change
the field during an orbit. Define the coordinate covector

\[
\zeta_j=\left(-{2\Omega_2'(I_j)\over\Omega_1'(I_j)},\ 2,\ 0\right).
\tag{7}
\]

**Theorem.** For all sufficiently large j, the regular particle orbit of
Vⱼ on I=Iⱼ is periodic, and the physical covector obtained from ζⱼ
returns with it. The inviscid principal system

\[
X'=V_j(X),\quad \xi'=-A^T\xi,\quad
b'=-Ab+2\xi{\xi\cdot Ab\over|\xi|^2},\quad
\xi\cdot b=0,\quad A=\nabla V_j(X)
\tag{8}
\]

has a real expanding polarization Floquet multiplier on this orbit.
After identifying one poloidal circuit by its exact axial rotation, its
two multipliers tend to `exp(±4π/3)` as j→∞. For all sufficiently large
j, the expanding relative multiplier is at least `exp(13π/12)`, and
the expanding multiplier of the full closed orbit is its jth power.

The theorem selects an explicit family of cutoffs and exact implicit
rational tori. It does not supply a computed integer j₀ or a numerical
profile. Once any j beyond the proved existential threshold is fixed,
that one smooth profile can be used in later estimates. Uniformity over
all these increasingly thin cutoffs is not asserted for the later NS
comparison.

## 2. Why the pressure-normal result does not decide this carrier

There is a useful exact check before calculation. Write
`ω=curl V`, `a=ξ×b`. From (8), incompressibility and the cross-product
identity for a trace-free matrix give

\[
a'=Aa+(\omega\cdot\xi)b
=Aa-(\omega\cdot\xi){\xi\times a\over|\xi|^2}.
\tag{9}
\]

Steady Euler gives `ω'=Aω` along particles, so `ω·ξ` is constant.
Also `V'=AV`, so `V·ξ` is constant. If `ω·ξ=0`, (9) reduces to
particle deformation. The action-angle flow and its inverse grow at
most linearly on a fixed compact annulus. For a returning covector,
its magnitude has a positive minimum on a period. Hence such a carrier
cannot have an exponentially growing polarization multiplier. This
additional neutral class does not include the limit of (7): below,
its vorticity-covector pairing is `−1/2`.

Nor does integrable particle motion itself exclude wave growth: the
second term in (9) remains. It is essential to calculate the amplitude
system with its pressure correction.

## 3. The complete gradient and moving frame in the thin limit

At `φ=β+η(σ,I)`, use the right-handed orthonormal frame

\[
n=\sin\sigma\,e_\rho+\cos\sigma\,e_z,\quad
t=\cos\sigma\,e_\rho-\sin\sigma\,e_z,\quad a=e_\varphi,
\quad E=(n,t,a).
\tag{10}
\]

Here a denotes the frame's axial direction only; it is not the
vorticity amplitude in (9). Put c=1/√2. The analytic expansion (4),
with r=√(2I), gives uniformly in the angles

\[
U=r(t+ca)+O(r^2),\quad P=r^2/2+O(r^6),\quad
\nabla P=rn+O(r^2),
\tag{11}
\]

and

\[
E^T\nabla U E=
\begin{pmatrix}0&-1&0\\1&0&0\\c&0&0\end{pmatrix}+O(r).
\tag{12}
\]

For clarity, the derivative assertion follows by using the scaled
coordinate columns `r ΦI`, `Φσ/r`, `Φβ`: in the E frame they equal
the identity plus O(r). Differentiating `U=r(t+ca)+O(r²)` radially
gives `(t+ca)+O(r)`, and differentiating in σ then dividing by r gives
`−n+O(r)`. The physical axial derivative is O(r). Inverting the
scaled coordinate matrix preserves these errors. This also shows why
the analyticity and `η=O(I)` in (4) are needed.

On the exact pressure level Pⱼ, only the first cutoff derivative enters:

\[
\nabla V_j=\nabla U-{U\otimes\nabla P\over P_j}.
\]

Consequently its full physical gradient and the frame's time rotation
have limits

\[
A_E:=E^T\nabla V_j E=A_0+O(r_j),\qquad
A_0=\begin{pmatrix}0&-1&0\\-1&0&0\\-c&0&0\end{pmatrix},
\tag{13}
\]

\[
E^TE'=O_0+O(r_j),\qquad
O_0=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}.
\tag{14}
\]

The latter uses `Ω₁=K'(Iⱼ)=1+O(rⱼ⁴)`, `Ω₂=c rⱼ+O(rⱼ³)`.
Higher derivatives of the cutoff grow as j increases but do not enter
(13). They will matter for later profile-dependent PDE constants.

## 4. Exact covector return and its limiting orientation

The derivative of the coordinate particle flow is

\[
B(\tau)=\begin{pmatrix}
1&0&\tau\Omega_1'\\0&1&\tau\Omega_2'\\0&0&1
\end{pmatrix}.
\]

The cotangent transport is `B(τ)^{-T}`. The choice (7) annihilates the
shear exactly: `Ω₁' ζσ+Ω₂' ζβ=0`. Its coordinate components are
therefore constant throughout the orbit. The physical covector is
`ξ=DΦ^{-T}ζⱼ`; it solves the exact covector equation, not an approximate
one.

At I=Iⱼ, differentiation of (3) gives

\[
\Omega_1'=-{K'^2\over K}+K''=-{2\over r_j^2}+O(r_j^2),\qquad
\Omega_2'=q'K'+q\Omega_1'=-{c\over r_j}+O(r_j).
\tag{15}
\]

Thus `ζσ/rⱼ→−c`, `ζβ=2`, `rⱼζI=0`. Applying the inverse transpose
of the scaled coordinate matrix in section 3 yields

\[
k_j:=E^T\xi=(0,-c,2)^T+O(r_j)=k_0+O(r_j),
\tag{16}
\]

uniformly, also after a fixed σ derivative. In particular ξ never
vanishes, and the same limit holds on the entire poloidal circuit.

## 5. Pressure-corrected two-dimensional system

For the physical amplitude let `\widetilde b=E^Tb`. Equations (8)
and (14) give

\[
\widetilde b'=-A_E\widetilde b-E^TE'\widetilde b
+2k_j{k_j\cdot A_E\widetilde b\over|k_j|^2}.
\tag{17}
\]

Both the moving-frame term and the full pressure term are retained.
For the limit define coordinates

\[
v=b_n,\qquad s=k_t b_a-k_a b_t.
\]

The inverse on `k·b=0` is

\[
b_t={-k_tk_n v-k_a s\over k_t^2+k_a^2},\qquad
b_a={-k_ak_n v+k_t s\over k_t^2+k_a^2}.
\tag{18}
\]

Substituting A₀,O₀,k₀ into (17) gives exactly

\[
{d\over d\tau}\binom v s=B_0\binom v s,
\qquad B_0=\begin{pmatrix}0&-8/9\\-1/2&0\end{pmatrix},
\qquad B_0^2={4\over9}I.
\tag{19}
\]

The eigenvalues are ±2/3. This is a signed amplification calculation,
not an upper bound on strain. The full pressure term restores the plane
constraint; deleting it leaves the defect `(√2,0)` acting on `(v,s)`.
At this limiting orientation it happens to vanish under the two chosen
coordinate functionals, so comparing only a projected 2×2 expression
would miss that error. The full three-component equation is checked.

For actual j, the coordinates (18) remain uniformly invertible. Their
σ derivative must also be included because kⱼ varies. Converting time
to σ and differentiating these coordinate maps yields an exact
two-dimensional equation

\[
{dY\over d\sigma}=B_j(\sigma)Y,\qquad
\sup_\sigma\|B_j(\sigma)-B_0\|=O(r_j).
\tag{20}
\]

This follows from (13)–(16), their uniform differentiated remainders,
and `Ω₁→1`; no term singular in r remains in (18).

## 6. Growth survives on the true orbit

Axisymmetry is decisive here. The columns E and DΦ are equivariant under
axial rotation, whereas all their relative components depend only on σ,I.
Thus Bⱼ(σ) is **exactly 2π-periodic**. One poloidal circuit changes β
by `2πq=2π/j`; the endpoint frame and physical covector are the start
rotated by that angle. This is a relative return, not yet the closed
physical orbit. After j circuits the axial rotation is 2π and the frame,
particle, and covector all return. The full polarization return map is
exactly the jth power of the one-circuit relative map Mⱼ.

Continuous dependence applied on the fixed interval `[0,2π]` to (20)
gives `Mⱼ→exp(2πB₀)`. It is not necessary to approximate a trajectory
over a time interval growing like j. Hence the limiting multipliers are
`exp(±4π/3)` and the expanding one remains above one for all large j.

Here is a separate explicit robustness margin. With

\[
T=\begin{pmatrix}-4/3&4/3\\1&1\end{pmatrix},\qquad
T^{-1}B_0T=\operatorname{diag}(2/3,-2/3),
\]

(20) ensures that, for all sufficiently large j,
`T^{-1}Bⱼ(σ)T=diag(2/3,−2/3)+R(σ)` with every `|Rkl|≤1/12`.
For `z=x_-/x_+` the exact equation is

\[
z'=R_{21}+(-4/3+R_{22}-R_{11})z-R_{12}z^2.
\tag{21}
\]

At the two cone boundaries,

\[
z'\big|_{z=-1/2}\ge{23\over48}>0,\qquad
z'\big|_{z=1/2}\le-{23\over48}<0.
\tag{22}
\]

Inside the cone `x₊>0`, `|z|≤1/2`,

\[
x_+'\ge\left({2\over3}-{1\over12}-{1\over24}\right)x_+
={13\over24}x_+.
\tag{23}
\]

First-exit comparison proves cone invariance, including starting on the
boundary by its strict inward direction or continuous dependence. The
one-period slope map is continuous and maps `[-1/2,1/2]` into itself.
The intermediate value theorem supplies a fixed slope. Its vector is
therefore an eigenvector of Mⱼ with positive multiplier at least
`exp((13/24)2π)=exp(13π/12)>1`.

Finally, the trace of the physical polarization equation on ξ⊥ is
`−d log|ξ|/dτ`, as derived in the preceding note. The moving orthonormal
frame adds zero trace. The covector norm and coordinate chart return
after each relative circuit, so `det Mⱼ=1`. Its other eigenvalue is
the positive reciprocal. Raising Mⱼ to its jth power proves the full
closed-orbit statement. This completes the theorem.

## 7. What this accomplishes for the full NS program

This supplies a specific unstable inviscid principal wave system on an
actual compact Euler background. It removes the previously open
oblique-multiplier question for the selected family. It does not yet
remove the forcing issue, justify a localized high-frequency solution,
or prove NS blow-up.

The order of limits is mandatory: first fix one sufficiently large j and
its entire cutoff/profile, then normalize and concentrate that fixed
profile at physical frequency L. Only the second step has the uniform
small-viscosity NS comparison from the previous note. Taking j and L to
infinity together would require new control of the exploding cutoff
derivatives and Sobolev constants.

The next mathematical step is to propagate a localized short-wave
approximation through the actual viscous NS background, compare the full
linearized equations and then the nonlinear solution, and preserve a
positive amount of the gain. The estimates must include the pressure
projection, packet spread, covector and amplitude error, viscosity,
initial seed size and feedback. For the proposed scaling,
`ε=νL^{-2/5}`, relative wavelength `h=L^{-1/10}`, and background time
`O(log L)`, a term called small at fixed time is insufficient: its
amplified error must remain small on that logarithmic interval.

Even a successful finite packet amplification theorem would leave seed
supply, transition errors, and a construction from one smooth initial
datum unresolved. The new expanding multiplier must not be identified
with the solution of ROOT.

## 8. Verification and teaching record

The instrument pins 20 exact identities/inequalities. The independent
tests reconstruct the limiting gradient from the Cartesian steady column
`(-y/r²,x/r²,1/(√2r))`, check its pressure, verify an explicit growing
three-component polarization, and reject a large-error cone control.
The column is used only as an algebra check. The actual compact-flow
conclusion follows from sections 1–6, not from column numerics.

Two independent mathematical reviewers checked the thin jet, cutoff
slope, exact covector return and the relative-cycle lift. No actual
Gavrilov ODE was integrated and no explicit small j threshold was
computed. The supplied fluid_lean library's ODE-tube component offers a
formalization route for (22); its forced-fluid theorems are separate
from this result. Kernel-check standing is recorded independently in
[the formalization audit](fluid-lean-integration.md).

The teachable sequence is: identify the neutral orientation; retain the
vorticity coupling; choose a cutoff derivative that changes its sign;
derive the pressure-corrected limit; prove uniform differentiated error;
use exact symmetry to compare one fixed period; and state separately
what remains before a PDE or infinite-cascade conclusion. No stage is
hidden inside a numerical maximum or the word “formalized.”
