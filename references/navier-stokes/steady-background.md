# A longer-lived concentrated background and the next amplification test

**Date:** 8 September 2026 UTC / 7 September Pacific.  
**Standing:** written classical small-viscosity comparison and a restricted
geometric-optics ODE obstruction. No unstable packet, cascade, novelty, or
global NS theorem is claimed. **ROOT and `(E′)` remain OPEN.**

This is the analytic follow-up to the finite interval established in
[the concentrated-packet note](concentrated-packet.md).
It addresses the time limitation by changing the reference profile.
An exact steady Euler field has no inviscid nonlinear defect; its viscous
defect is small after concentration. This gives logarithmically many
controlled turnover times for the true unforced NS background. It does
not imply that a high seed amplifies during them.

The full proof below is the evidence for the comparison theorem; the
[symbolic instrument](../../experiments/nse_steady_background.py),
[tests](../../tests/test_nse_steady_background.py), and
[receipt](../../artifacts/enstrophy_sup/nse_steady_background.json) pin the
rescaling, comparison formula, cotangent return condition, and ODE algebra.
Node `nse-steady-background-local` has only this restricted scope. No
numerical Gavrilov profile, orbit, or PDE trajectory was computed.

**Follow-up completed:** the [oblique-carrier note](gavrilov-oblique.md)
now proves the section 6 inviscid carrier task at an existential, selected-profile
scope. The next obligation is localized finite-wavelength NS comparison.
ROOT and `(E′)` remain OPEN.

## 1. The external input, with its equation fixed

[Gavrilov's main theorem](https://arxiv.org/html/1810.08020v1) constructs
a nonzero smooth compactly supported stationary three-dimensional Euler
velocity; section 3 localizes it using a pressure first integral.
[Constantin–La–Vicol](https://arxiv.org/html/1903.11699v1), Theorems 1–2,
give an alternative construction through Grad–Shafranov equations.
These are Euler existence results, not stationary unforced viscous flows.

Fix one such profile and its pressure:

\[
V\in C_c^\infty(\mathbb R^3;\mathbb R^3),\quad V\ne0,\quad
\nabla\cdot V=0,\quad (V\cdot\nabla)V+\nabla P=0.
\tag{1}
\]

Normalize `||V||L²(R³)=(2π)^{3/2}` by multiplying velocity and pressure
by the corresponding constant and its square. Subtract the exterior
constant from P. Both V and P then vanish outside some sufficiently large
ball. For `L≥L₀≥1`, embed this ball and a collar in `(-πL,πL)³` and
periodize onto `𝕋L=(R/(2πLZ))³`. The steady Euler identity remains exact
everywhere, including across the cell boundary. Moreover

\[
\int_{\mathbb R^3}V_i=\int_{\mathbb R^3}\nabla\cdot(y_i V)=0.
\]

Thus the periodic datum is mean-zero without a time-dependent velocity
subtraction or an unproved change of frame.

This profile has infinitely many Fourier modes. Its compact physical
support does not imply a finite spectral cutoff. The empty-tail bound of
the preceding finite-band construction cannot be transferred to it.

## 2. Fixed physical viscosity and uniform comparison norms

Given `aL>0`, define

\[
A_L=a_LL^{3/2},\qquad y=Lx,\qquad \tau=A_LL t,\qquad
U_L(t,x)=A_Lv_\epsilon(\tau,y),\qquad
\epsilon={\nu L\over A_L}={\nu\over a_LL^{1/2}}.
\tag{2}
\]

Here vε solves the full **unforced** rescaled NS equation on 𝕋L,

\[
\partial_\tau v_\epsilon-\epsilon\Delta v_\epsilon
+\mathbb P_L[(v_\epsilon\cdot\nabla)v_\epsilon]=0,
\qquad v_\epsilon(0)=V.
\tag{3}
\]

Then Uᴸ solves NS with the original fixed ν on the fixed `2π` torus,
and `||Uᴸ(0)||₂,av=aL`. Each L specifies a different initial datum.
This family is not one solution performing infinitely many stages.

For an integer `s≥3` use the **unnormalized**, inhomogeneous norm

\[
\|f\|_{H^s(\mathbb T_L)}^2
=\sum_{|\alpha|\le s}\int_{\mathbb T_L}|\partial^\alpha f|^2.
\]

The fixed profile has its Euclidean norm in every such cell. Sobolev,
product, and commutator constants can be chosen independently of L≥1.
For example the Fourier Cauchy–Schwarz proof of `Hˢ→W^{j,∞}` has the
factor

\[
\left[(2\pi L)^{-3}\sum_{k\in\mathbb Z^3}
{(|k|/L)^{2j}\over(1+|k/L|^2)^s}\right]^{1/2},
\qquad s>j+3/2,
\tag{4}
\]

with the numerator interpreted as 1 for j=0. Lattice-cube comparison
bounds this uniformly by an integrable Euclidean weight. Fourier weighted
convolution gives the uniform product inequalities. The solenoidal
commutator estimate follows by the Leibniz rule, transport cancellation,
and these embeddings/interpolation bounds. The Leray multiplier is an
Hˢ contraction; derivative and Fourier Sobolev norms have equivalence
constants depending only on s. No expanding-domain Poincaré constant is
used. Mean-normalizing this large-torus norm while keeping the same
embedding constant would be an error.

## 3. A logarithmic lifetime for the actual NS background

Write `w=vε−V`, `z=||w||Hˢ`, and `F=||ΔV||Hˢ>0`. Subtracting (1)
from (3),

\[
w_\tau-\epsilon\Delta w+
\mathbb P_L[(V\cdot\nabla)w+(w\cdot\nabla)V+(w\cdot\nabla)w]
=\epsilon\Delta V,\qquad w(0)=0.
\tag{5}
\]

The right side is the reference profile's residual, not an external
force applied to (3). Differentiating through order s, pairing with the
same derivatives of w, and using section 2 gives

\[
\frac12(z^2)' +\epsilon\|\nabla w\|_{H^s}^2
\le C_Vz^2+C_sz^3+\epsilon Fz,
\qquad C_V=C_s\|V\|_{H^{s+1}},
\tag{6}
\]

after increasing Cₛ if necessary. The zeroth transport term cancels;
commutators account for its differentiated terms. Dividing at positive z,
or regularizing the norm at zero, yields

\[
z'\le C_Vz+C_sz^2+\epsilon F.
\tag{7}
\]

Fix any radius r>0 and `κ≥Cᵥ+Cₛr`, with κ>0 independent of L,ε.
As long as z≤r, Gronwall gives

\[
z(\tau)\le {\epsilon F\over\kappa}(e^{\kappa\tau}-1).
\tag{8}
\]

This closes with `z≤r/2` throughout

\[
T_\epsilon={1\over\kappa}
\log\left(1+{\kappa r\over2\epsilon F}\right).
\tag{9}
\]

Local strong existence and its Hˢ continuation alternative justify the
entire interval: the estimate prevents the norm from leaving the strict
bootstrap boundary. In particular, for any fixed `0<c<1/κ`, at sufficiently
small ε,

\[
\sup_{0\le\tau\le c\log(1/\epsilon)}\|v_\epsilon(\tau)-V\|_{H^s}
\le {F\over\kappa}\epsilon^{1-\kappa c}\longrightarrow0.
\tag{10}
\]

The constants depend on the chosen fixed V and s, not on L. There is
no uniform estimate here over profiles whose cutoff thickness or other
shape parameters also vary with L. Numerical values for those constants
have not been computed.

Since Hˢ embeds into C¹, velocity and strain persist in the Eulerian
sense. For `aL=L^{-1/10}`, this background is smooth and close to its
steady reference in the rescaled norm of (10) for

\[
0\le t\le c L^{-12/5}\log(L^{2/5}/\nu),\qquad
\epsilon=\nu L^{-2/5},
\tag{11}
\]

for sufficiently large L. This is logarithmically many rescaled turnover
times. Smoothness here concerns the specific background initialized at V;
it is not a smoothness theorem for an additional merely L²-small seed.

## 4. Particle positions require their own comparison

Let `Xε'=vε(τ,Xε)` and `X'=V(X)` have the same starting point. With
`K=||∇V||∞`, Gronwall bounds their distance d in compatible lifts by

\[
d(\tau)\le C_s\int_0^\tau e^{K(\tau-q)}z(q)\,dq.
\]

Choose the fixed rate κ above also to satisfy κ≥K+1. Applying (8),

\[
d(\tau)\le {C_s\epsilon F\over\kappa(\kappa-K)}e^{\kappa\tau}.
\tag{12}
\]

Thus positions also converge over the shorter logarithmic interval in
(10). For a selected compact material region, the initial distance to
its boundary must exceed this error. Comparing wavevectors and
polarizations requires further ODE bounds with their own growth constants
and, potentially, a smaller c. Equation (10) is not already that proof.

## 5. The first wave orientation does not give exponential amplification

For the Gavrilov family, [Baldi's Theorem 1.1](https://arxiv.org/html/2302.02982v1)
gives particle coordinates `(θ₁,θ₂,I)` with
`θ'=Ω(I), I'=0`, including the pressure cutoff. It describes periodic
and quasiperiodic particle motion. It makes no high-seed amplification
claim. The following implications and ODE calculation are our deductions,
not additional theorems attributed to that paper.

On a **fixed compact action annulus** the coordinate maps and their
derivatives are bounded. The flow derivative in these coordinates is

\[
D\Phi_\tau=
\begin{pmatrix}I_2&\tau\Omega'(I)\\0&1\end{pmatrix}.
\tag{13}
\]

Its derivative and inverse therefore grow at most `C(1+|τ|)` in physical
coordinates. This excludes a hyperbolic particle orbit in that annulus;
it does not establish stability of the different polarization equation.

The inviscid short-wave system, obtained from the leading eikonal and
amplitude equations of linearized Euler, is

\[
X'=V(X),\qquad \xi'=-A^T\xi,\qquad
b'=-Ab+2\xi{\xi\cdot Ab\over|\xi|^2},\qquad
\xi\cdot b=0,\quad A=\nabla V(X).
\tag{14}
\]

The factor 2 is the pressure correction: differentiating `ξ·b=0` forces
`ξ·b'=ξ·Ab`, which determines the component of b′ parallel to ξ after
the `−Ab` term. This is the principal ODE; no localized approximate
solution or finite-wavelength error theorem is established here.

Consider a regular periodic orbit with period T, `V≠0`, `∇P≠0`, for a
localizable steady Euler field satisfying `V·∇P=0`. Choose
`ξ=∇P(X)`. Differentiating the first-integral relation gives
`ξ'=−Aᵀξ`. Also `AV=−ξ` by (1), so `b=V(X)` solves (14): its right
side is `ξ−2ξ=−ξ=V'`. It is a nonzero periodic polarization orthogonal
to ξ. The same argument works with the original pressure first integral
before cutoff when its gradient is collinear with the localized one.

In a periodic oriented orthonormal frame of ξ⊥, the polarization
coefficient matrix has trace

\[
-\operatorname{tr}A+\widehat\xi^TA\widehat\xi
=\widehat\xi^TA\widehat\xi
=-{d\over d\tau}\log|\xi|.
\tag{15}
\]

The moving frame's skew rotation has zero trace. Since ξ returns after
one orbit, the determinant of the polarization return map is one.
The periodic solution b=V supplies one eigenvalue 1; the other is also 1.
Thus the **pressure-normal carrier has no exponentially growing Floquet
multiplier**. Jordan growth remains possible. This does not exclude
oblique carriers, nonperiodic covectors, finite transient growth, or
instability of the full linearized Euler/NS operator.

## 6. The concrete next attempt and its stopping rule

Fix one Gavrilov profile/cutoff and a compact interior pressure annulus.
Select a closed orbit by a rational ratio of its two angle frequencies.
An angle-action covector `(ζθ,ζI)` returns after the orbit precisely when

\[
\Omega'(I)\cdot\zeta_\theta=0,
\tag{16}
\]

because `(DΦT)^{-T}` sends it to
`(ζθ,ζI−T Ω'(I)·ζθ)`. Use **returning oblique covectors** in the
remaining test; the pressure-normal choice `ζθ=0` is already handled.
A closed particle path without a returning covector does not by itself
justify a periodic coefficient matrix for an ordinary Floquet claim.

Derive the pressure-corrected polarization return map for that specified
orbit and carrier class. Either rigorously certify a multiplier with
modulus greater than one, or prove a class-specific obstruction. First
seek an analytic sign/invariant; if a numerical ODE is needed, freeze
the profile, orbit, event, and validated error bounds before running it.
No new DNS is justified by the present result.

If a growing multiplier is found, compare its gain and error constants
with (10)–(12), localized short-wave approximation errors, viscous decay,
the available seed size, and nonlinear feedback. Only then attempt an
actual finite-interval NS amplification theorem. Particle-flow growth
from (13) gives the preliminary arithmetic

\[
\epsilon\int_0^T|\xi(q)|^2\,dq
\le C\epsilon(H/L)^2(T+T^3)
=O\big(\nu L^{-1/5}(\log L)^3\big)\to0
\tag{17}
\]

when `H/L=L^{1/10}` and `T=O(log L)`. This is an inviscid-covector
damping feasibility check, not an error estimate for the true viscous
polarization or an amplitude theorem.

A multiplier alone would not provide unforced dormant seeds or an
infinite smooth-data cascade. In particular O(log L) controlled time
with a fixed growth exponent yields only polynomial amplification in L.
It cannot automatically amplify a prescribed superpolynomially small
smooth initial tail to a polynomial target. Actual seed production and
interstage errors would still have to be controlled by the full equation.

**Next obligation:** the returning-oblique-covector calculation in
(14)–(16). If it fails for the stated profile, record exactly that
obstruction and do not replace it with generic claims that persistent
strain must amplify waves. None of these local results settles ROOT.

**Verification:** 16/16 symbolic pins for this supplement passed; the
three current local-estimate test files total 44 passing tests. Both new
notes received independent mathematical review. Coverage audit: OK at
359 nodes, with the same three existing warnings (`nse-qgso-h2clock`,
`nse-qgso-ksplit`, `nse-qgso-phoctave-deep`). No DNS, compact profile
evaluation, Floquet computation, proof-assistant check, or CI run was
performed. The proof of the PDE estimates is the written argument above.
