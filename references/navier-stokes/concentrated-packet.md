# Concentrated packets: persistent strain and a short-time activation obstruction

**Date:** 8 September 2026 UTC / 7 September Pacific.  
**Standing:** PROVED restricted full-PDE estimates, by classical local
expansions and relative energy. No novelty, infinite cascade, or global
regularity claim. **ROOT and `(E′)` remain OPEN; GSO remains DEAD.**

Pins: [exact instrument](../../experiments/nse_concentrated_packet.py),
[independent tests](../../tests/test_nse_concentrated_packet.py),
[receipt](../../artifacts/enstrophy_sup/nse_concentrated_packet.json);
node `nse-concentrated-packet-local`, outside the closed route into ROOT.

This executes the concentrated-packet task in the
[first activation note](frequency-activation.md).
The packet attains the required concentration power, and its actual NS
evolution preserves strong strain on a material neighborhood for an explicit
interval. A relative-energy estimate then handles an arbitrary high seed
without imposing an artificial lifespan depending on its top frequency.
It proves that a sufficiently small seed cannot reach the specified distant
activation threshold during the certified local window. The missing input
is longer accumulated amplification, not a stronger instantaneous strain.

## 1. Equation, norms, and the prepared class

Use one fixed viscosity `ν>0`, zero forcing, and the mean-zero real
solenoidal NS equation on `(R/2πZ)³`:

\[
u_t-\nu\Delta u=B(u,u),\qquad B(v,w)=-\mathbb P[(v\cdot\nabla)w].
\]

Write `||v||²₂,av=(2π)⁻³∫|v|²=Σ|v̂(k)|²`,
`||v||Aˢ=Σ|k|ˢ|v̂(k)|`, and `S(v)=(∇v+∇vᵀ)/2`.
Matrix sup norms below are operator norms. In particular these estimates
do not use a false L∞ Korn inequality.

Let `n≥1` be an integer, `L=3n`, and `a>0`. Put

\[
\begin{split}
I_n&=\{n,\ldots,2n-1\},\qquad d=2n+1,\\
\mathcal K_n&=I_n\times(I_n\cup(-I_n))\times\{-n,\ldots,n\},\\
F_n(x)&=\sum_{k\in\mathcal K_n} k_1k_2(-k_2,k_1,0)\sin(k\cdot x),\\
S_r&=\sum_{j=n}^{2n-1}j^r,\qquad E=2dS_2S_4,\qquad D=2dS_2^2,\\
U_0&={a\over\sqrt E}F_n,\qquad
m=4n^2d,\qquad \overline W=a\sqrt m,\qquad
\sigma={aD\over\sqrt E}.
\end{split}
\tag{1}
\]

Here `m` counts the actual nonzero positive and negative vector Fourier
coefficients, and `W̄` is an **upper bound**, not the exact Wiener norm.
Let U be the exact NS solution with initial data U₀ alone. Let u have
initial data `u₀=U₀+w₀`, where w₀ is any real, mean-zero, solenoidal L²
perturbation, with `ε=||w₀||₂,av`. Smooth w₀ is permitted, with no upper
frequency restriction. The perturbation bounds below hold for every
Leray–Hopf u; a claimed smooth realization must separately establish its
smoothness. U is a comparison solution, **not** the evolving low-pass
projection of u.

## 2. Exact concentration and three-dimensional dependence

Every coefficient in (1) is already transverse to its wavevector; no
projection repairs the input. Orthogonality of the sine functions and
the k₂/k₃ symmetries give

\[
\|F_n\|_{2,av}^2=E,\qquad
\nabla F_n(0)=\operatorname{diag}(-D,D,0),\qquad
\|U_0\|_{2,av}=a.
\tag{2}
\]

The support spans R³. Its maximum squared frequency is
`9n²−8n+2<L²`, and its minimum is at least `2n²`. Thus it is a
three-dimensional annular packet, with O(L³) modes. Since
`S₂≥n³` and `S₄≤4n²S₂`,

\[
{\sigma^2\over L^2\overline W^2}
={S_2^3\over18n^4S_4}\ge{1\over72}>{1\over81},\qquad
\sigma\ge{L\overline W\over9}.
\tag{3}
\]

Moreover `8n³≤m≤12n³`, so

\[
{1\over2}aL^{3/2}\le\overline W\le {2\over3}aL^{3/2},\qquad
{aL^{5/2}\over18}\le\sigma\le L\overline W.
\tag{4}
\]

This realizes the concentration power absent from a fixed sparse seed.
The physical field is a smooth trigonometric polynomial. Its spectral box
has a sharp boundary, and its physical tails have not been discarded.
We prove strong strain on a ball below; we do not assert that all its
energy is inside that ball.

For each coordinate reflection R, `U₀(Rx)=R U₀(x)`. The full NS equation
preserves this covariance by uniqueness, so `U(t,0)=0` and its gradient
there remains diagonal. Initial `U₀,3=0` does not define an invariant
two-component system: exact convolution gives

\[
\widehat{B(F_1,F_1)}(2,0,2)=(i/2,0,-i/2).
\tag{5}
\]

Pressure immediately produces the third component. This calculation is
an initial tangent used to verify the equation and symmetry class; the
time-dependent assertions come from the full estimates below.

## 3. Strain persists in the actual background solution

The convergent full-NS expansion proved in the first note has homogeneous
terms with support at most nL and bound
`||Uₙ(t)||A⁰≤W̄ cₙ xⁿ⁻¹`, where
`x=L W̄ t`, `cₙ=nⁿ⁻¹/n!≤3ⁿ⁻¹`. Summing after differentiation gives,
for `3x<1`,

\[
\begin{split}
\|\nabla U(t)\|_\infty&\le {L\overline W\over(1-3x)^2},\\
\mathcal A_U(t):=\int_0^t\|S(U(s))\|_\infty\,ds
&\le {x\over1-3x},\\
\sup_{|e|=1}\|\partial_e S(U(t))\|_\infty
&\le L^2\overline W{1+3x\over(1-3x)^3}.
\end{split}
\tag{6}
\]

The same integrated bound holds with `||∇U||∞` in place of `||S(U)||∞`.
These are convergent all-mode sums, including the pressure projection.

Assume the background's effective Reynolds condition
`δ=νL/W̄≤1`. On `0≤x≤1/512`, the heat part and the nonlinear remainder
give respectively

\[
\|\nabla(U(t)-U_0)\|_\infty
\le L\overline W\left[\delta x+{1\over(1-3x)^2}-1\right]
<{L\overline W\over36}\le{\sigma\over4}.
\tag{7}
\]

For `|y|≤1/(64L)`, (6) similarly gives

\[
\|S(U(t,y))-S(U(t,0))\|_{op}
\le L\overline W{1+3x\over64(1-3x)^3}
<{L\overline W\over36}\le{\sigma\over4}.
\tag{8}
\]

At `x=1/512` the margins against `1/36` in (7) and (8) are exactly
`16716335/1193845248` and `55932389/4747400244`. Monotonicity proves the
bounds throughout the interval. Consequently

\[
e_1^T S(U(t,y))e_1\le-\sigma/2,\qquad
e_2^T S(U(t,y))e_2\ge\sigma/2
\tag{9}
\]

on that whole space-time cylinder.

The material trajectories of U starting in `|y|≤1/(128L)` remain in
the ball of (9). Indeed the origin is fixed and their radial expansion
factor is at most `exp(1/509)≤509/508<2`. At the endpoint
`tₚ=1/(512L W̄)` their integrated fixed-direction compression is at least

\[
\int_0^{t_p}-e_1^TS(U(s,X(s)))e_1\,ds
\ge{\sigma t_p\over2}\ge{1\over9216}.
\tag{10}
\]

This proves persistence of the **background** geometry. It is not a
proof that a transported seed retains a favorable polarization or phase.
For example, in the local affine matrix `diag(−σ,σ,0)`, a velocity
polarization e₁ with carrier covector e₃ can grow while the covector
does not. The compressively growing covector e₁ instead requires velocity
polarization perpendicular to e₁. Simultaneous frequency and amplitude
gain cannot be inferred from (9) alone.

## 4. Relative energy handles arbitrary high seeds and their feedback

Set `w=u−U`. On the common smooth lifetime, direct subtraction gives

\[
w_t-\nu\Delta w+
\mathbb P[(U\cdot\nabla)w+(w\cdot\nabla)U+(w\cdot\nabla)w]=0.
\]

Pairing with w yields exactly

\[
{1\over2}{d\over dt}\|w\|_{2,av}^2
+\nu\|\nabla w\|_{2,av}^2
=-\langle w,S(U)w\rangle_{av}.
\tag{11}
\]

The background transport and perturbation self-transport cancel by
incompressibility. Pressure cancels in this solenoidal pairing; it was
not removed from the evolution. All generated frequencies and all feedback
are present in w. Gronwall and (6) imply

\[
\|w(t)\|_{2,av}\le e^{\mathcal A_U(t)}\varepsilon
\le \exp\left({x\over1-3x}\right)\varepsilon.
\tag{12}
\]

For every Leray–Hopf u, the weak–strong relative-energy inequality gives
the same bound on the entire existence interval of the smooth U. This
follows by combining u's energy inequality, U's energy equality, and the
cross-term identity obtained by testing the weak equation against U,
then applying the cancellation in (11). The inequality initially holds
at energy times; weak continuity
and lower semicontinuity extend the L² bound to all times. This extension
does **not** assert that u is strong or smooth.

In particular define

\[
\tau={1\over6L\overline W}.
\]

Then `x≤1/6`, `𝒜U≤1/3`, and
`exp(𝒜U)≤1/(1−𝒜U)≤3/2`. Thus
`||w(t)||₂,av≤3ε/2` throughout `[0,τ]`, independently of the seed's
highest frequency. No effective Reynolds condition is needed for this
upper estimate. The condition in section 3 is only for the strain lower
bound. Using the high-seeded datum's full bandwidth in the local series
would lose this useful frequency independence.

## 5. A full-PDE exclusion of the prescribed short-time activation

Let `H≥L`, `J=⌊H/L⌋`, and `r=3x`. The first note's support argument
and the convergent expansion of U give

\[
\|P_{>H}U(t)\|_{2,av}
\le\|P_{>H}U(t)\|_{A^0}
\le{\overline W r^J\over1-r}.
\tag{13}
\]

This term includes production through **every** intermediate background
frequency, not just one low-low interaction. Combining (12) and (13),

\[
\boxed{\quad
\|P_{>H}u(t)\|_{2,av}
\le {\overline W(3x)^J\over1-3x}
+e^{x/(1-3x)}\varepsilon
\le 2\overline W2^{-J}+{3\over2}\varepsilon,
\quad 0\le t\le\tau.\quad}
\tag{14}
\]

For any target `η>0`, assume

\[
\varepsilon\le\eta/3,\qquad
J\ge\max\left(1,\left\lceil\log_2{8\overline W\over\eta}\right\rceil\right).
\tag{15}
\]

Then the background contribution is at most η/4 and the perturbation
contribution at most η/2. The total stays at most `3η/4<η` for the
whole interval. Thus an activation event defined by
`||P>H u(t)||₂,av≥η` cannot occur there. The result has explicit data,
time, and event hypotheses, and needs no persistent frequency-gap
assumption.

Viscosity remains in (11). Its integrated form gives

\[
\|w(t)\|_{2,av}^2+2\nu\int_0^t\|\nabla w\|_{2,av}^2\,ds
\le e^{2\mathcal A_U(t)}\varepsilon^2.
\]

Consequently the high-frequency difference has the occupancy bound

\[
\int_0^\tau\|P_{>H}w(s)\|_{2,av}^2\,ds
\le{e^{2/3}\varepsilon^2\over2\nu H^2}
\le{9\varepsilon^2\over8\nu H^2}.
\tag{16}
\]

This is an integrated bound, not a pointwise exponential high-frequency
damping law for w. Support need not stay high. An exact example uses
the real conjugate pairs
`p=(2j,0,0), q=(−2j,1,0)` with coefficients
`v̂(p)=e₂`, `v̂(q)=(1,2j,0)`. Every input frequency is above j, but
`B(v,v)̂(0,1,0)=(−i,0,0)`. It disproves support invariance, which
therefore cannot justify replacing `||∇w||₂²` by `H²||w||₂²`
throughout an interval.

## 6. The scale test and the exact remaining gap

For the proposed choices

\[
a=L^{-1/10},\qquad H=L^{11/10},\qquad
\eta=H^{-1/10}=L^{-11/100},
\tag{17}
\]

(4) gives `σ≍L¹²⁄⁵`, `W̄≍L⁷⁄⁵`, and `τ≍L⁻¹²⁄⁵`.
The geometric factor `2^{-⌊L¹⁄¹⁰⌋}` in (14) eventually defeats
every polynomial, so (15) holds at sufficiently large L for any
`ε≤η/3`. This is a symbolic asymptotic statement, not a claim of useful
scale separation on small constructed grids. For example `L≥2¹⁰⁰`
is a crude sufficient gap threshold: with `z=log₂L`, compare
`2^{z/10}−1` with `3+(151/100)z`. The latter bounds the logarithm
in (15), and the difference is positive and increasing for `z≥100`.
For fixed ν the additional persistence condition `δ≤1` also holds
eventually, for example once `L≥(2ν)^{5/2}`.

Although the pointwise strain has the desired power, its certified
accumulation is O(1). The seed cannot gain an arbitrarily large factor
in this window. More generally, as long as U stays smooth, reaching η
at a time when `η−||P>H U(t)||₂,av>ε` requires

\[
\mathcal A_U(t)\ge
\log{\eta-\|P_{>H}U(t)\|_{2,av}\over\varepsilon}.
\tag{18}
\]

This is necessary, not sufficient: favorable signed polarization,
phase, localization, and viscous control would still need proof.
The [shell-model paper](https://arxiv.org/html/2605.13827v1) motivates
long seed-amplification intervals and protects dormant seeds by forcing;
neither feature is automatically inherited by the unforced NS equation.

The packet class is not ruled out at later times. A logarithmic number
of turnover intervals might still fit in summable physical time along
lacunary scales. Conversely, restarting (14) repeatedly is not a proof:
one would have to bound the change of reference background, its generated
tail, and the cumulative comparison error at every restart. These are
precisely the unproved transition estimates.

The next analytic candidate is a background whose Euler nonlinearity
balances pressure exactly, allowing a longer small-viscosity comparison.
The [steady-background note](steady-background.md) checks
this proposal and separates persistence from short-wave amplification.
Do not rerun this explicit packet or optimize its constants as a substitute
for that new estimate.

## 7. Evidence and applicable adversarial checks

The written arguments prove the PDE statements; the executable pins
check their algebra and constants. The receipt contains 47 exact checks.
Independent physical trigonometric constructions, on grids 16/24/32,
verify raw divergence, Fourier normalization, the gradient and pressure
coefficient. Separate tests compare the full projected difference pairing
with its physical energy cancellation. The new and first-activation tests
total 38 passing tests (44 including the steady-background supplement).
The coverage audit passed at 359 nodes with three existing warnings.
An independent model audited the formulas, the
weak-solution scope, and the loss in accumulated gain. No DNS was run,
and these checks are not continuum interval certification of a numerical
maximum; the strain bounds here are analytic.

| Potential false shortcut | What this result actually controls |
|---|---|
| A moment-matched shrinking field is treated as an NS solution | (11) requires the full difference momentum equation; the old kinematic residual is not admissible. |
| A scalar escape is called a counterexample to the theorem | The theorem has explicit periodic Fourier data and PDE hypotheses, absent from a scalar ledger. It proves no general escape exclusion. |
| The seed or spectral gap stays fixed | (12) permits all frequencies and nonlinear feedback; the high-high-to-low witness refutes support invariance. |
| The background silently remains two dimensional | Spectral rank is three; (5) generates a third velocity component. |
| Small relative L² error proves regularity | The Leray–Hopf estimate is only an L² estimate; no perturbation strain or continuation norm is bounded. |
| Local compression proves a cascade | (9)–(10) concern a fixed finite interval and background directions; polarization, later seed supply, and iteration remain unproved. |

**Unresolved:** no signed high-seed amplification theorem, no adequate
unforced seed-supply estimate for an infinite construction, no uniform
transition recurrence, and no one-datum singular solution or general
regularity estimate. ROOT and `(E′)` remain OPEN.
