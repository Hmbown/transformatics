# What one further profile correction actually buys

8 September 2026. **Reviewed finite-depth lemma and finer-scale corollary.** Sections 1–7 passed
the [independent fixed-depth review](finite-depth-profile-review.md)
at its pinned source version. Section 8 passed a
[separate finer-scale review](finer-scale-review.md) at source
SHA-256 `8496abb26b5247a7afed95a16b9237ff07f153956231e255fe56fa6d58dd2615`.
Root independently read the arguments. Subsequent edits to this introduction
and its review labels do not change any equation or estimate. These are
AI-agent reviews of written analysis, not a formal PDE certificate or
external expert acceptance.
This note derives a correction recurrence about the actual first-stage q,
retaining the full phase mean and pressure. Its purpose is to resolve small
generated components below the current nonlinear tracking error. It changes
no initial datum. It is not an infinite correction theorem, an admissible
terminal force sequence, or a Navier–Stokes solution claim. ROOT, E-prime
and FORCED-D remain open. No DNS is used.

## 1. Setting and finite-depth claim

Keep the original data, fixed smooth periodic profile F, actual first-stage
q, transported phase S and central heat clock from the
[full-profile construction](../navier-stokes/localized-profile.md).
Use h, ell, k, d, epsilon as in the
[logarithmic host](../navier-stokes/logarithmic-host.md), with

\[
 \rho=k/d=h^{1/4},\qquad
 t_\eta=t_f+\log\ell/(8\mu)+\log\eta/\mu.
\]

In this note J is an arbitrary positive integer fixed before h tends to
zero. The coefficient eta is also fixed. All constants may depend on J,
the fixed profiles and eta. Write E for finitely enlarged factors with
log E=O_{J,eta}(ell^(9/8))+O_{J,eta}(log ell)=o(ell²).

The finite-depth conclusions are

\[
 \int_0^{t_\eta}\|R_J\|_2dt
       \le k\rho^{J+1}d^{3/2}E
       =h^{(29+2J)/8}E,                              \tag{1}
\]
\[
 U_J(0)=Q_h(0),\qquad
 \sup\|U_J\|_{H^{12}}\le h^{-117/8}E,\qquad
 \int\|\nabla U_J\|_\infty dt
                       \le B\eta\ell^2+o(\ell^2).  \tag{2}
\]

Here B is independent of J and eta, after a fixed enlargement: for each
fixed J and eta, the finitely many correction-gradient integrals vanish.
J=1 is exactly the current one-mean/one-full-profile correction, with
residual power 31/8. The base approximation J=0 contains only q and the
primary receiving curl packet.

The recurrence below supplies the asserted power gain; it is not assumed
from a formal expansion. In particular it cancels each new normal mean's
fast advection of the current oscillatory profile before estimating errors.

## 2. Norms, supports and fixed derivative orders

For a spatial mean v, use scaled global Sobolev seminorms

\[
 \mathcal S_r(v)=\sum_{|\alpha|\le r}
              d^{|\alpha|-3/2}\|D^\alpha v\|_2.
\]

For a periodic phase profile v(x,s), replace L2 by L2_x A_M, where
\(\|v\|_{A_M}=\sum_n(1+|n|)^M|\hat v(n)|\).
Scaled Sobolev embedding gives
\(d^r\|D^r v\|_\infty\le C\mathcal S_{r+2}(v)\), with constants
uniform on the expanding torus.
Thus a statement that v has size a means the required finite collection of
these norms and pointwise counterparts is at most aE. This does not assert
compact support for a mean or its pressure.

All oscillatory amplitudes and their nonzero-phase forcings remain in the
same transported chart, of volume O(d³). Global means use global norms.
Products use a pointwise bound on one factor and a global L2 bound on the
other, including products of two mean tails.

Only finite orders are required for finite J. A sufficient deliberately
nonminimal hierarchy starts with final spatial/phase order 30 and allows
eight additional spatial and phase derivatives for each preceding round.
This pays the at most three slow derivatives in the curl-viscous residual,
two additional phase derivatives from heat, and two spatial derivatives
for pointwise recovery. Take the initial profile and phase through order
N=30+8J, q through N+4, and F with finite A_(N+80) norm. They are fixed
smooth objects, so every such norm is finite.

The original q datum is independent of these proof indices. Its first-stage
high-order argument may use H_M with M>4(N+4+3/2), plus the corresponding
finite source indices. The scaled C^r error power
1/4-(r+3/2)/M is positive for r<=N+4. Hence its sharp q gradient and all
required jets retain the same subpower factors on the interval in question.
No estimate for unbounded J or a uniform family of derivative orders is
asserted.

## 3. An exact recursive correction

Let D=partial_t+q.grad, A=grad q, xi=grad S, and let kappa be the spatially
constant central heat rate. For any zero-phase-mean tangent profile a, set

\[
 V_a=-{\xi\times\partial_s^{-1}a\over|\xi|^2},\qquad
 r_a=\operatorname{curl}_x V_a,\qquad W_a=a+kr_a.
\]

Evaluation at s=S/k makes W_a exactly solenoidal. Write
\(\nabla^k=\nabla_x+(\xi/k)\partial_s\). Suppose

\[
 U_j=q+m_j+\mathcal E[W_{a_j}]
\]

has complete pressure P_j and residual \(\mathcal E[R_j]\), allowing
R_j's phase mean to have global spatial tails. The primary a_0 is the
original heat-evolved receiving profile, m_0=0. Keep R_j as an exact
profile expression, not a reconstruction from a spatial average.

Put r_j^0=<R_j>_s. First solve the full global solenoidal equation

\[
 D\delta m+A\delta m+\nabla\delta p_m=-r_j^0,
 \qquad \operatorname{div}\delta m=0,\quad\delta m(0)=0. \tag{3}
\]

Next define the zero-phase-mean forcing

\[
 H_j=R_j-r_j^0+{\delta m\cdot\xi\over k}\partial_s a_j, \tag{4}
\]

and solve

\[
 (D-\kappa\partial_s^2)\delta a=G\delta a-\Pi_\xi H_j,
 \quad\delta a(0)=0,\qquad
 G=-A+2\xi\otimes(\xi^TA)/|\xi|^2.                  \tag{5}
\]

Its complete pressure is

\[
 \delta p_a=-k\partial_s^{-1}
          {2\xi\cdot A\delta a+\xi\cdot H_j\over|\xi|^2}. \tag{6}
\]

Tangency, reality and zero phase mean are preserved. Equations (3)--(5)
are triangular: solve delta m first, then delta a. Set

\[
 m_{j+1}=m_j+\delta m,\quad a_{j+1}=a_j+\delta a,
 \quad P_{j+1}=P_j+\delta p_m+\mathcal E[\delta p_a].
\]

All new increments, including their curl lifts, vanish initially.
The original datum is therefore unchanged for every finite j.

## 4. Exact remainder after a round

Use the full forced-profile identity (13)--(14) of the source:

\[
 (D+A-\epsilon\Delta^k)W_{\delta a}
             +\nabla^k\delta p_a=-H_j+\mathcal R[\delta a;H_j].
\]

Let Z=W_(a_j), W=W_(delta a), m=m_j, and v=delta m+W. With all profile
terms evaluated only at the end, direct expansion gives

\[
 R_{j+1}=\mathcal R[\delta a;H_j]-\epsilon\Delta\delta m
      +m\cdot\nabla\delta m+\delta m\cdot\nabla m
\]
\[
 \quad+Z\cdot\nabla\delta m+\delta m\cdot\nabla_xZ
             +(\delta m\cdot\xi)\partial_s r_{a_j}
\]
\[
 \quad+Z\cdot\nabla^kW+W\cdot\nabla^k Z
       +m\cdot\nabla^kW+W\cdot\nabla m
       +v\cdot\nabla^k v.                           \tag{7}
\]

In the final term, delta m has no phase variable. The subtracted fast
term in (4) accounts for the missing part of delta m.grad^k Z. In
particular it is not discarded because delta m might be tangent: the
global pressure generally makes it nontangent.

Every fast tangent/tangent product in the third line vanishes at leading
order, because xi.a_j=xi.delta a=0. Normal curl corrections remain.
The identity includes mean-mean, mean-wave and all Fourier products.

## 5. Why the remainder gains rho

Assume R_j has size k rho^(j+1). Equations (3)--(5) and the finite
differentiated hierarchy give delta m, delta a and H_j that same size,
up to E. The extra term in (4) has size delta m times |a_j|/k, which is
delta m times E. It has no unfavorable power of h.

Inductively a_j has size k, and m_j has size k rho, up to E. The exact
terms in (7) now have the following costs relative to the new increments:

| Term | Small factor, apart from E |
|---|---|
| Linear curl and pressure remainder | k/d=rho |
| Leading central/actual diffusivity mismatch | epsilon/k²=nu h |
| Mixed slow/fast viscosity | epsilon/(kd)=nu h^(5/4) |
| Slow viscosity of the mean or profile | epsilon/d²=nu h^(3/2) |
| Tangent wave cross terms after cancellation | k/d=rho |
| Existing mean's fast advection of delta a | |m_j|/k=O(rho) |
| New mean's remaining interaction with the existing wave | k/d=rho |
| Mean-mean slow terms | k rho/d=rho² |
| New mean's fast advection of the new wave | O(rho^(j+1)), at most rho |

Factors from xi, its inverse and their derivatives enter E. In the exact
linear residual, material derivatives of the curl potential are eliminated
using (5) and Dxi=-A^Txi; this requires spatial derivatives of H_j, not an
uncontrolled time derivative. The full pressure numerator (6) is used in
that elimination.

All listed factors are at most rho times subpower factors. Therefore
R_(j+1) has size k rho^(j+2). The base residual R_0 has size k rho:
the leading k^-1 self-interaction vanishes, the remaining self/curl terms
have size k²/d, and the viscous terms are smaller. Induction proves (1).
Time integration costs only E. The finitely many new gradients have
size rho^(j+1)E, so their sum and time integral vanish and preserve (2).

## 6. Consequence for actual-flow resolution

Relative energy and a separate H12 bootstrap, exactly as in the logarithmic
host theorem, give

\[
 \|\nabla(Q_h-U_J)\|_\infty
 \le h^{(19J-17)/96-C_*\eta-o(1)},                   \tag{8}
\]

whenever its exponent has a positive fixed margin. The exponent follows
from (1), H12 order -117/8, and interpolation weights 19/24 and 5/24.
The constant C_* comes from the leading history B eta ell² and the H12
energy inequality, not from a claim that correction factors are uniform
in J. For each fixed J their constants belong to E.

For example J=1 gives 1/48 before the eta loss; J=3 gives 5/12. This can
make the full-Q error smaller than an h^(1/4) source component if that
component has its own nonzero lower bound. It does not provide that lower
bound by itself.

For any fixed eta>0 and desired fixed positive accuracy exponent, choosing
a sufficiently large fixed J would leave a positive margin in (8).
The q construction and central ODE extend to that fixed eta: their clock
is O_eta(ell^(9/8))=o(ell²). Thus this finite-depth statement, if validated,
removes the restriction to one particular small coefficient at the price
of a larger fixed finite approximation order. The threshold on h then
depends on both J and eta. It supplies no uniform assertion when eta or J
grows with h, or when h is held fixed and time tends to a singular endpoint.

For control of an actual small Fourier component, a Sobolev version can be
more useful. Interpolating the L2 error with H12 to H3 yields the pre-clock
power (3J-15)/16. Since H3 controls a Fourier-summed gradient uniformly
on these tori, increasing fixed J resolves prescribed fixed algebraic
gradient scales, including their high-pass projections. This must still
be compared with a signed source and its complete actual time evolution.

## 7. What is not bought by depth

The primary wave, original C3 preparation cost, physical viscosity and
phase geometry are unchanged. Finer residuals do not manufacture a new
independent phase or increase a fixed host's homogeneous velocity gain.
For a forced construction, every derivative conversion to physical units,
activation, reset and baseline-host force remains a separate cost.

Fixed finite J uses finitely many smooth-profile constants. Taking J to
infinity, choosing J(h), or gluing infinitely many physical stages requires
quantitative bounds on all those constants and one compatible schedule.
None of those conclusions follows from this finite induction.

## 8. Consequence: no algebraic-size output at a fixed finer power scale

Fix eta>0, beta>3/2 and P>0. Then the recurrence predicts the stronger
actual-solution estimate

\[
 \sup_{0\le t\le t_\eta}
 \|\nabla P_{>h^{-\beta}}Q_h(t)\|_\infty\le h^P
 \quad\text{for all sufficiently small }h.          \tag{9}
\]

The threshold on h depends on eta, beta and P. This statement includes
all generated modes and uses the full actual Q_h, not just its two supplied
packets. It says that the finer tail is smaller than every fixed algebraic
power across this varying-data family. It does not say that the tail is
zero. In particular it does not exclude the normal-source draft's
coarser envelope frequencies h^(-5/4+o(1)).

Here is the additional finite derivative accounting needed for (9).
Choose an integer r>=12, fixed before h tends to zero. In section 2,
replace final order 30 by max(30,r+4), and reserve the same eight extra
orders for each previous correction round. All coefficients are still
the same fixed smooth profiles. Only the proof's finite derivative
indices and constants change. Write E_(J,r,eta)=h^(-o(1)) for their
subpower factors.

The first-stage solution has

\[
 \|q_h\|_{H^r}\le[1+h^{7/4-r}]E_{J,r,\eta}.         \tag{10}
\]

Indeed its original first packet has amplitude O(h/ell), support volume
O(h^(3/2)), and derivative cost h^(-1) per order. Its initial H^r norm
is at most C[1+h^(7/4-r)]. The separate integer H^r energy inequality
uses the already established actual-q gradient clock
O_eta(ell^(9/8)); it therefore changes only E. This uses the actual
first-stage flow and its strong continuation, not a derivative of the
full-Q error bound.

The second packet and its fixed finitely many phase corrections have
amplitude at most kE, support volume O(d³), and evaluated derivative cost
at most k^(-1)E per order: slow derivatives cost d^(-1), which is smaller.
The global mean has size at most k rho in the scaled global norms.
Consequently

\[
 \|U_J\|_{H^r}
 \le [1+h^{7/4-r}+k^{1-r}d^{3/2}
                      +k\rho d^{3/2-r}]E_{J,r,\eta}
 \le h^{27/8-3r/2}E_{J,r,\eta}\qquad(r\ge12).       \tag{11}
\]

Mean tails are charged by their global L2 norms here, not by pretending
that they remain compact. The compact wave volume enters only the wave
terms. Fourier Cauchy–Schwarz on the expanding torus gives, uniformly
for R>=1 and r>5/2,

\[
 \|\nabla P_{>R}v\|_\infty
 \le C_r R^{5/2-r}\|v\|_{H^r}.                    \tag{12}
\]

The lattice sum carries the factor (2pi L)^(-3) associated with
unnormalized L2. Comparison with the radial integral makes C_r uniform
for L>=1. Setting R=h^(-beta) in (11)–(12) gives exponent

\[
 A_r(\beta)=r(\beta-3/2)+27/8-5\beta/2.            \tag{13}
\]

Since beta>3/2, choose one fixed r large enough that A_r(beta)>P+2.
It remains to bound the sharp projection of the error, which is not a
bounded operator on L-infinity. Use H3 instead. Relative energy and
the separate H12 bound give

\[
 \|Q_h-U_J\|_{H^3}
 \le h^{(3J-15)/16-C_3\eta-o(1)},\qquad
 C_3>B(3+C_{12})/4.                                \tag{14}
\]

The weights are 3/4 from L2 and 1/4 from H12, including their respective
clock losses. Fourier Cauchy–Schwarz with the inhomogeneous H3 weights
also gives \(\|\nabla P_{>R}e\|_\infty\le C\|e\|_{H^3}\)
uniformly in R>=1 and L>=1. Choose one fixed J large enough that the
exponent in (14) before o(1) exceeds P+2 and the C1 bootstrap margin in
(8) is positive. The latter independently supplies the actual lifetime.

The triangle inequality, (13) and (14), now prove (9) after reducing h
to absorb the subpower factors and fixed constants. The order of choices
is eta, beta, P; then r and J; then h. No index tends to infinity during
any one estimate, and no new initial component is chosen for this proof.

At beta=3/2 the coefficient of r in (13) vanishes and A_r=-3/8. This
argument deliberately gives no such assertion at the receiver's own
power scale. It gives no bound uniform as beta decreases to 3/2, no
exponential tail estimate and no claim beyond t_eta. If a proposed
descendant needs an algebraic-size seed at any fixed strictly finer power
scale during this interval, (9) rules out that requirement. A smaller
seed, a closer scale, the coarser generated mean, or later evolution needs
its own source and gain estimates.
