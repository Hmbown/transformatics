# A non-effective expanding window for the same varying-data family

8 September 2026. **Reviewed written corollary at the stated scope.** The
[independent review](diagonal-window-review.md) and root read
passed. These are AI-agent reviews, not external expert acceptance or a
formal PDE certificate. The review pins the version before this label and
the central-model focus clarification; no estimate was changed.
The reviewed fixed-depth estimates imply an existential diagonal schedule
with eta and the finite correction depth both tending to infinity. This
does not supply a prescribed rate, an infinite correction series, or one
initial datum with an infinite trajectory. ROOT, E-prime and FORCED-D remain
OPEN. No DNS, canonical claim edits or external publication are involved.

The logical issue is the distinction between an arbitrary prescribed
parameter schedule and one schedule chosen sufficiently slowly after all
fixed-parameter thresholds are known to exist. No quantitative control of
their dependence on the parameters is needed for the latter existence claim.

## 1. Inputs and source pins

The inputs are the fixed-depth recurrence and its separate continuation and
Fourier-tail arguments, together with the central outgoing comparisons:

| Source | Current SHA-256 |
| --- | --- |
| [Fixed finite-depth construction](finite-depth-profile.md) | `909e21a42ddb67636f2f08e695111d07005ee0935c9d36a8991a2e7c0fa75c4e` |
| [Independent fixed-depth review](finite-depth-profile-review.md) | `7b4cc95fa5db65eb17a088a1551c2901e0b310a97f06ca6386d4ebb90321e3d0` |
| [Independent finer-tail review](finer-scale-review.md) | `17d877dcc092c0586cbbb532da335b0a1669ff260379a171f6fdf2cd3a8373f6` |
| [Logarithmic-host assembly](../navier-stokes/logarithmic-host.md) | `2d06d4bf6edc170b79728e9494fb2ccfe7af3c803ad8535636359016b5f01761` |
| [Central outgoing polarization](outgoing-outer.md) | `15dcb45ba500a790e2778b752aa2937c2ba85a56cf3715392e3e4312b9e68c92` |
| [Exact future covector](future-covector.md) | `f64fc0bdd440e7b6a20de501cfcbf178a1761f1ea6c58c8ca41655feb6915142` |

Fix the same smooth profiles and physical viscosity as those sources. Keep
their original datum Q_h(0), including both originally supplied waves.
The datum depends on h but not on eta, correction depth J, or derivative
orders used to prove an estimate. Write

\[
 \ell=\sqrt{\log(1/h)},\quad k=h^{3/2},\quad d=h^{5/4},
 \quad t_f={2\over\mu}\log\ell-\ell^{-3/4},
\]
\[
 T(h,a)=t_f+{\log\ell\over8\mu}+{\log a\over\mu}.
                                                        \tag{1}
\]

Here t_f is the designated exact central-model focus, not an exact focusing
event of actual Q_h. It is not replaced by the nominal time (2/mu) log ell.
All times and spatial norms below are rescaled.

For every fixed a>0 and sufficiently large fixed J, the finite-depth source
gives a smooth actual Q_h through T(h,a), with an approximation U_J satisfying
U_J(0)=Q_h(0). Its relevant estimates are

\[
 \sup\|\nabla(Q_h-U_J)\|_\infty
 \le h^{(19J-17)/96-C_*a-o_{J,a}(1)},
\]
\[
 \sup\|Q_h-U_J\|_{H^3}
 \le h^{(3J-15)/16-C_3a-o_{J,a}(1)},                 \tag{2}
\]
\[
 \int_0^{T(h,a)}\|\nabla U_J\|_\infty\,dt
 \le Ba\ell^2+o_{J,a}(\ell^2).                     \tag{3}
\]

C_*, C_3 and B can be fixed independently of J and a at this finite-order
scope. Constants in the subpower factors need not be uniform. The C1/H12
bootstrap in (2), not the tail estimate alone, supplies the strong lifetime.
At every fixed finite depth, the correction beyond U_0 has C1 size at most
h^(1/4) E_(J,a), where log E_(J,a)=o(ell²). U_0 is q plus the original
receiving curl packet. Higher proof indices leave all these data unchanged.

The host theorem by itself restricted a to a small interval. The reviewed
finite-depth source, sections 6 and 8, supplies the extension to every fixed
a>0 by increasing fixed J. That stronger fixed-a quantifier is essential.

## 2. Statement of the diagonal corollary

There are integer-valued functions n(h), J(h), r(h), finite for each
sufficiently small admissible h, such that

\[
 n(h)\longrightarrow\infty,\qquad J(h),r(h)\longrightarrow\infty.
\]

Set eta(h)=n(h), T_h=T(h,eta(h)), and let U(h) be the corresponding finite
approximation U_(J(h)). Then the same original-data actual flow is smooth
on [0,T_h], and the schedule can be chosen to have all the following properties:

\[
 \sup_{[0,T_h]}\|Q_h-U(h)\|_{C^1}\le h^{n(h)},\qquad
 \sup_{[0,T_h]}\|Q_h-U_0\|_{C^1}\le2h^{1/8}.        \tag{4}
\]

The first bound comes from the H3 estimate and uniform Fourier embedding;
the second also uses the small finite profile corrections. There is no
claim that U_(J(h)) converges as J tends to infinity at one fixed h.

Let S(v)=(grad v+grad v^T)/2 and Y_h(t) be the reference particle of q used
by the host theorem. Positive constants c_E,C_E,c_I can be fixed for this
schedule, independently of h, so that at T_h

\[
 c_E\eta(h)\ell^2
 \le |S(Q_h-q_h)(T_h,Y_h(T_h))|_F
 \le C_E\eta(h)\ell^2.                             \tag{5}
\]

The same two-sided estimate holds for S(Q_h), after changing fixed constants.
For the full gradient clock,

\[
 c_I\eta(h)\ell^2
 \le I_h:=\int_0^{T_h}\|\nabla Q_h\|_\infty\,dt
 \le [B+o(1)]\eta(h)\ell^2.                        \tag{6}
\]

These lower constants require the common-horizon central comparison proved
in section 3 below. They do not follow merely by absorbing unspecified
a-dependent endpoint comparison constants into a threshold on h.

For frequencies k_m=m/L and normalized Fourier coefficients on the torus
of side 2pi L, define the absolute gradient tail

\[
 \mathcal A_R(v)=\sum_{|k_m|>R}|k_m|\,|\widehat v(m)|.
\]

The schedule can also satisfy the stronger tail statement

\[
 \sup_{[0,T_h]}
 \mathcal A_{h^{-(3/2+1/n(h))}}(Q_h)\le h^{n(h)}.    \tag{7}
\]

In particular, for every fixed beta>3/2 and P>0,

\[
 \sup_{[0,T_h]}\|\nabla P_{>h^{-\beta}}Q_h\|_\infty
 \le h^P
 \quad\hbox{for all sufficiently small }h.          \tag{8}
\]

This remains a superalgebraic exclusion on the full solution at strictly
finer power scales, with no assertion at beta=3/2. Its countable diagonal
does not eliminate the known coarser generated band.

The construction can make eta, J and r smaller than any given function
G(h) tending to infinity as h tends to zero, and simultaneously ensure

\[
 \log\eta(h),\ \log J(h),\ \log r(h)=o(\log\ell).  \tag{9}
\]

It therefore supplies no particular rate such as eta=ell^(1/16). It supplies
an unbounded coefficient of ell², not a demonstrated upper limit on how
large a more quantitative construction could make that coefficient.

## 3. Endpoint and clock constants

Fix once and for all C_0=1/(4mu) in the central outgoing theorem. Its
estimates (1)--(2) hold on delta<=tau<=C_0 log ell with constants depending
only on C_0, delta and the fixed profile. For each fixed integer n>=1,
reduce h until n<=ell^(1/8). Then

\[
 L_{\ell,n}={\log\ell\over8\mu}+{\log n\over\mu}
 \le C_0\log\ell.
\]

Consequently the same central constants work for all these fixed-n
problems, after n-dependent thresholds on h. In particular

\[
 {|b_c(t_f+\tau)||\xi_c(t_f+\tau)|\over k}
 \asymp\ell^{15/8}e^{\mu\tau}                      \tag{10}
\]

holds on each last unit interval T(h,n)-1<=t<=T(h,n), once its left endpoint
lies beyond t_f+delta. At t=T(h,n), the right side is exactly n ell².
This proves a uniform central two-sided comparison, including a lower
bound throughout a time interval of fixed positive length.

For each fixed n and J, the actual-q central comparison, whole-support
error, small central heat clock, flat-profile derivative and slow curl
terms have the vanishing errors stated in the host assembly. Their
constants may depend on n and J, but their errors tend to zero as h tends
to zero. Its comparison estimates are uniform in time through T(h,n).
The leading symmetric rank-one matrix has Frobenius norm
|b_c||xi_c|/(sqrt(2) k). Finite profile corrections and (2) vanish in C1.
The background satisfies

\[
 \sup_{[T(h,n)-1,T(h,n)]}\|\nabla q_h\|_\infty
 \le C_n(1+n\ell^{9/8})=o_n(n\ell^2).
\]

We may therefore reduce each fixed-n threshold until every subtracted
error is smaller than one fixed fraction of the central lower bound.
This proves (5), and uniformly on the last unit interval gives

\[
 \|\nabla Q_h(t)\|_\infty
 \ge c_0 n\ell^2 e^{\mu(t-T(h,n))}.                \tag{11}
\]

The comparison uses the q particle only as a test location for a spatial
supremum. It does not identify that particle with a Q_h trajectory.
Integrating (11) yields c_I=c_0(1-e^(-mu))/mu>0 in (6).
An endpoint lower bound alone would not justify this clock lower bound.

For the upper bound, choose the fixed-n threshold so that the remainder
in (3) is at most ell²/n and the integrated actual error is at most ell²/n.
Then

\[
 I_h\le Bn\ell^2+2\ell^2/n
       =(B+2/n^2)n\ell^2.                          \tag{12}
\]

B is the fixed coefficient already present in the reviewed sharp
whole-support estimate; no high-order norm is substituted for that clock.

## 4. Finite Fourier and derivative choices

For each positive integer n, fix

\[
 a_n=n,\qquad \beta_n=3/2+1/n,\qquad
 r_n=12+n^2+4n.
\]

The tail exponent of the fixed-depth source is

\[
 A_{r_n}(\beta_n)
 =r_n/n-3/8-5/(2n)
 =n+29/8+19/(2n)>n+3.                              \tag{13}
\]

Choose increasing finite integers J_n>=n such that

\[
 {19J_n-17\over96}-C_*n>n+3,\qquad
 {3J_n-15\over16}-C_3n>n+3.                        \tag{14}
\]

These choices are possible without knowing any high-order profile constants.
Construct the finite hierarchy with terminal order max(30,r_n+4), eight
extra orders per prior round, and the corresponding finite first-stage
Sobolev index specified in the source. All these indices are fixed during
the nth estimate; the same smooth profiles have all the needed finite norms.

The Fourier Cauchy--Schwarz argument in the source actually proves

\[
 \mathcal A_R(v)\le C_rR^{5/2-r}\|v\|_{H^r},\quad
 \mathcal A_R(e)\le C\|e\|_{H^3}\qquad(R\ge1),      \tag{15}
\]

uniformly on the expanding tori. It bounds the absolute Fourier sum before
estimating the spatial supremum. The factor (2pi L)^(-3/2) from normalized
coefficients cancels the L^(3/2) lattice-counting factor. The same argument
including low frequencies gives the uniform H3-to-C1 bound used in (4).

Apply (15) to U_(J_n) and Q_h-U_(J_n). Equations (13)--(14), the fixed-depth
H^r estimate, and sufficiently small h give

\[
 \sup\|Q_h-U_{J_n}\|_{C^1}\le h^n,\qquad
 \sup\mathcal A_{h^{-\beta_n}}(Q_h)\le h^n.         \tag{16}
\]

There is ample fixed margin to absorb the constants and sum the two tail
terms. Similarly h^(1/4) E_(J_n,n)<=h^(1/8) for sufficiently small h,
which gives the second part of (4), since n>=1 and 0<h<1.

Using the absolute sum is important: the L-infinity norm of a sharp Fourier
tail is not monotone in its cutoff. Once (7) is available, however,
mathcal A_R is monotone. For fixed beta>3/2 and P, eventually
beta_n<beta and n>=P. Thus (7) implies (8) for every fixed real beta and P,
not just a countable list of rational beta values.

## 5. Choosing one schedule

For each n, the preceding fixed-parameter results provide a positive
threshold below which (5), (11), (12), (16), smooth continuation and the
finite-correction bound all hold. Choose decreasing thresholds H_n>0
recursively, with H_(n+1)<H_n/2, below all the nth thresholds and with
H_1<e^(-1). Decrease H_n further to arrange, for every 0<h<=H_n,

\[
 n\le\ell(h)^{1/8},\qquad
 \max(n,J_n,r_n)\le\ell(h)^{1/n},\qquad
 \max(n,J_n,r_n)\le G(h).                          \tag{17}
\]

These requirements are possible because each left side is a fixed finite
number at the nth step and both ell(h) and G(h) tend to infinity. Limits
provide thresholds valid for every smaller admissible h, not merely one
selected subsequence. If no auxiliary G is wanted, omit its requirement.

For H_(n+1)<h<=H_n, set n(h)=n, eta(h)=n, J(h)=J_n and r(h)=r_n.
Each h is assigned only finitely many corrections. Since H_n decreases to
zero, n(h) tends to infinity. Every chosen h is below the threshold for its
own fixed-n estimate, proving (4)--(8); (17) proves (9).

All constructed approximations start at the same Q_h(0). Strong uniqueness
identifies actual Q_h solutions on overlapping smooth intervals when two
fixed-n arguments apply to the same h. The staircase changes the proof
parameters and observation window across the family; it does not restart
the solution, add a seed or select a different datum at a fixed h.

## 6. Consequences and limits of the conclusion

Since ell²=log(1/h), (6) gives

\[
 {I_h\over\log(1/h)}\longrightarrow\infty.
\]

Thus a sufficiently small fixed coefficient of ell² is not an absolute
ceiling on this same varying-data construction once deeper finite
approximations are allowed. At the same time, (9) gives

\[
 T_h=\left({17\over8\mu}+o(1)\right)\log\ell.
\]

The additive extension beyond any fixed-eta window tends to infinity,
but the leading logarithmic rescaled lifetime coefficient is unchanged by
this chosen slow schedule. In physical variables the source multiplies
times by h^24 and gradients by h^(-24); h^24 T_h still tends to zero.
No fixed datum has been followed toward a singular time.

The earlier fixed-depth disclaimer excluding eta(h), J(h) and r(h) should
therefore be narrowed for this corollary: the finite theorem gives no
arbitrary or prescribed growing schedule. It does give the non-effective
existential staircase above. This is a quantifier consequence, not an
all-orders estimate or a convergent infinite expansion.

Three negative controls mark the distinction:

* Fixed-parameter thresholds can deteriorate arbitrarily fast. The abstract
  condition h<exp(-exp(a)) holds for every fixed a and sufficiently small h,
  but fails eventually at a=ell^(1/16). It therefore cannot justify that
  prescribed rate; neither can bare fixed-a quantifiers.
* If one knew only endpoint lower bounds c(a) a ell² with arbitrary c(a)>0,
  shrinking h would not make c(a) uniform. For example c(a)=exp(-a²) remains
  small along every a tending to infinity. The uniform common-C_0 central
  comparison in section 3 is what supplies (5)--(6).
* An endpoint strain bound does not bound its time integral from below
  without persistence. Equation (11), on a last interval of length one,
  supplies precisely that missing input here.

Nothing here proves a new phase, velocity amplification, useful subsequent
feedback of the generated band, or a smoothly forced infinite construction.
The fine-tail exclusion and actual-flow continuation coexist with those
open problems. A quantitative schedule or a single-data infinite-stage
argument requires additional work beyond this diagonal result.
