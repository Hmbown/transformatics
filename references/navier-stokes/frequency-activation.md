# First activation attempt: an actual local trajectory and the sparse-packet limit

**Date:** 8 September 2026 UTC / 7 September Pacific.  
**Standing:** PROVED restricted local estimates, using classical local theory;
no novelty claim, global regularity theorem, or blow-up construction.
**ROOT and `(E′)` remain OPEN.** The retired GSO route is not used.

Pins: [exact instrument](../../experiments/nse_frequency_activation.py),
[independent tests](../../tests/test_nse_frequency_activation.py),
[receipt](../../artifacts/enstrophy_sup/nse_frequency_activation.json);
node `nse-frequency-activation-local` (not a closed route into ROOT).

This executes the first work package in the
[research plan](research-strategy.md). The useful outcome is
twofold: an explicit example of internally generated modes in a true,
unforced three-dimensional NS solution, with every omitted mode bounded
over an interval; and an explicit reason this sparse construction does
not implement the concentrating shell-model mechanism. The first result
is an application of standard convergent local expansions. It is a
validated starting calculation, not a major regularity advance.

## 1. Fixed equation and a precise result

Work on the fixed torus `(R/2πZ)³` with one constant `ν>0`, zero forcing,
mean-zero real solenoidal data, and the full Leray-projected equation

\[
u_t-\nu\Delta u=B(u,u),\qquad B(v,w)=-\mathbb P[(v\cdot\nabla)w].
\]

Use Fourier coefficients `u(x)=Σ û(k)e^{ik·x}`. In this note
`||u||_{2,av}²=(2π)^{-3}∫|u|²=Σ|û(k)|²` and
`||u||_{A^s}=Σ|k|^s|û(k)|`, with Euclidean norms of vector coefficients.
Physical L² norms are `(2π)^{3/2}` times these mean L² norms. The symbol
`W` below denotes a Wiener norm, not the project's maximum strain `M`.

**Local activation theorem.** Let `N≥1` be an integer, `A>0`, and
`A/(νN)≥1`. Set

\[
u_0=A(\cos Ny,\cos Nz,\cos Nx)+w_0,
\quad \operatorname{supp}\widehat w_0\subset\{|k|\le N\},
\quad \|w_0\|_{A^0}\le A/256,
\tag{1}
\]

where `w0` is real, mean-zero and divergence-free. There is a unique
smooth solution on an interval containing `[0,t*]`, where

\[
t_*={1\over512AN}.
\]

For every `0<t≤t*`, its previously absent coefficient at `k*=N(1,1,0)` obeys

\[
-\operatorname{Im}\widehat u_3(k_*,t)
\ge {A^2Nt\over8}.
\tag{2}
\]

In particular this coefficient reaches magnitude at least `A/4096` by
`t*`, while every coefficient outside the initial support is generated
by the unforced PDE. This is a lower envelope over an interval, not a
monotonicity assertion. The threshold is small and explicitly fixed;
the result does not say that enstrophy or a critical norm increases.

The three nonzero axial seed coefficients survive the allowed
perturbation. Their wavevectors span R³, so there is no direction of
translation invariance; this is not a 2D3C example. Equal amplitudes do
have a discrete cyclic symmetry. The perturbation allowance makes (2)
independent of retaining that symmetry. The initial tail is **exactly
zero beyond N**; this hypothesis cannot be replaced silently by generic
smooth data or small unmeasured high-frequency seeds.

## 2. The all-mode interval estimate

Here is a self-contained classical majorant argument that controls the
actual solution. It does not discard pressure or assume finite support
is invariant. Let the initial Fourier support be inside `|k|≤N`, and
write `W=||u0||A0>0`. Define homogeneous terms

\[
U_1(t)=e^{\nu t\Delta}u_0,\qquad
U_n(t)=\sum_{a+b=n}\int_0^t e^{\nu(t-s)\Delta}B(U_a,U_b)(s)\,ds.
\tag{3}
\]

Every ordered pair `a,b≥1` is included. Inductively
`supp Ûn ⊂ {|k|≤nN}`. The Leray projector has Euclidean operator norm
one at each nonzero frequency, and the heat multiplier is at most one.
For terms of homogeneous degrees a,b, therefore,

\[
\|B(U_a,U_b)\|_{A^0}\le bN\|U_a\|_{A^0}\|U_b\|_{A^0}.
\]

Put `x=NWt`. Induction in (3) gives

\[
\|U_n(t)\|_{A^0}\le W c_n x^{n-1},\qquad
c_1=1,\quad
(n-1)c_n={n\over2}\sum_{a+b=n}c_a c_b,
\quad c_n={n^{n-1}\over n!}.
\tag{4}
\]

The time integral contributes `1/(n−1)`; pairing the ordered terms
replaces b by `n/2`. To verify the formula for all n, let
`T(z)=Σc_n z^n`. The recurrence says
`z(1−T)T'=T`, hence `T exp(−T)=z`; coefficient extraction by Lagrange
inversion gives (4). These rooted-tree coefficients and this local
expansion are standard, not a newly proposed calculus.

Moreover

\[
{c_{n+1}\over c_n}=(1+1/n)^{n-1}<e<3.
\]

Thus `ΣUn` converges whenever `3x<1`. Because the nth term is supported
inside radius nN, multiplying its bound by any fixed power `(nN)^s`
still gives a convergent series. Spatial differentiation, the Laplacian,
and the bilinear convolution therefore converge on every closed
subinterval with `3x<1`. The summed integral equation solves the full
NS equation smoothly, including at t=0. The usual difference-energy
argument gives uniqueness: the spatial Lipschitz norm of this solution
is bounded on such a subinterval. This also justifies using (3) to
describe the actual local strong solution, rather than an ansatz.

Using `c3=3/2` and the ratio bound, the omitted sum `R=Σ(n≥3)Un` satisfies

\[
\|R(t)\|_{A^0}\le {3\over2}W{x^2\over1-3x}.
\tag{5}
\]

This controls infinitely many modes. A stronger explicit version, with
`r=3x`, is

\[
\|R(t)\|_{A^3}
\le {3\over2}WN^3x^2
{27-44r+31r^2-8r^3\over(1-r)^4}.
\tag{6}
\]

It follows by summing `(j+3)^3r^j`. Thus the error is controlled in a norm
that also bounds derivatives; it is not just an L² residual. Equations
(5)–(6) have a stated interval of validity. They provide no continuation
estimate once that interval is exhausted.

### Creation across an initially empty gap

For `H≥N`, terms of degree `n≤floor(H/N)` cannot reach `|k|>H`.
Consequently, for `r=3NWt<1`, the same expansion proves

\[
\sum_{|k|>H}|\widehat u(k,t)|
\le {W r^{\lfloor H/N\rfloor}\over1-r}.
\tag{7}
\]

In particular, throughout `0≤t≤1/(6NW)`,

\[
\sum_{|k|>H}|\widehat u(k,t)|
\le 2W\,2^{-\lfloor H/N\rfloor}.
\tag{8}
\]

This is a quantitative **short-time** restriction on reaching a distant
empty band, including all intermediate-frequency production. It is a
standard local-analyticity consequence with explicit constants, not a
global spectral-gap preservation theorem. An initially supplied distant
seed is outside (7)'s assumptions. For `H=N^b`, `b>1`, the bound at this
local time is exponentially small in `N^(b−1)`. Waiting longer or
changing the initial tail requires further analysis.

## 3. Signed activation, pressure and backreaction

For the unperturbed datum in (1), all initial modes have length N.
The first generated field is exactly

\[
U_2(t,x)=A^2Nt e^{-2\nu N^2t}
(\sin Ny\cos Nz,\sin Nz\cos Nx,\sin Nx\cos Ny).
\tag{9}
\]

Its 12 nonzero modes have length `√2 N`. In particular

\[
\widehat{(U_2)}_3(N,N,0,t)
=-{i\over4}A^2Nt e^{-2\nu N^2t}.
\tag{10}
\]

The heat factor is integrated exactly: the input product decays as
`exp(−2νN²s)` and this output as `exp(−2νN²(t−s))`. The initial
nonlinearity happens to be divergence-free, but that does not make
pressure disappear at the next order.

To make the omitted interactions explicit, use the unit seed V and set
`B0=B(V,V)`, `C=B(V,B0)+B(B0,V)`. Exact continuum Fourier algebra gives:

| Quantity | Exact value |
|---|---|
| `||B0||²_{2,av}` | `3/4` |
| `Ĉ(1,0,0)` | `(0,0,−1/4)` — feedback into the original modes |
| `Ĉ(1,2,0)` | `(0,0,−1/8)` — additional modes at length √5 |
| Raw coefficient at `(1,1,1)`, before pressure | `−(1,1,1)/4` |
| Same coefficient after Leray projection | `0` |
| Energy feedback | `⟨V,C⟩av+||B0||²_{2,av}=0` |

C has 18 nonzero modes: six original and twelve at length √5. Its
coefficients enter U3 with the actual integrals
`A³N²∫₀ᵗ s exp[−νN²(|κ|²(t−s)+3s)]ds` at `k=Nκ`.
The vanishing diagonal listed above is an order-specific calculation;
no general absence of that frequency in perturbed solutions is inferred.
Both feedback and modes outside the first two shells are present.

For comparison with the plan, the exact sharp split `u=ℓ+h` gives

\[
\tfrac12\partial_t\|h\|_2^2+\nu\|\nabla h\|_2^2
=-\langle h,(\ell\cdot\nabla)\ell\rangle
-\int h^TS(\ell)h.
\tag{11}
\]

Indeed `⟨h,(ℓ·∇)h⟩=⟨h,(h·∇)h⟩=0` by incompressibility, and the
remaining high-low contraction is the symmetric strain pairing.
Projection can be removed in these pairings because h is solenoidal.
The exact tests check (11) on fields with modes on both sides of the
cutoff; the proof uses the full equation, not a shell truncation.

The initial unperturbed enstrophy derivative is negative for `ν>0`:
with mean normalization, `Q0=3A²N²/4` and
`Q'(0)=−3νA²N⁴/2`. New mode creation therefore does not itself imply
net enstrophy growth.

### Uniform error margin and perturbations

Let `τ=ANt≤1/512`, `ε=1/256`, `m=3+ε`. The perturbed datum has
`W≤mA`. The change in U2 caused by w0 obeys

\[
\|U_2[u_0]-U_2[AV]\|_{A^0}
\le A\tau(6\varepsilon+\varepsilon^2).
\]

This uses both ordered mixed interactions and the perturbation's
self-interaction, with derivative at most N on each input. Also (5) gives

\[
\|R\|_{A^0}\le A\tau\,
{(3/2)m^3\tau\over1-3m\tau}.
\]

Since `Re=A/(νN)≥1`, `exp(−2τ/Re)≥1−2τ`. The lower bound for the
left side of (2), divided by `Aτ`, is therefore at least

\[
{1-2\tau\over4}-(6\varepsilon+\varepsilon^2)
-{(3/2)m^3\tau\over1-3m\tau}.
\tag{12}
\]

This expression decreases as τ and ε increase in the stated range.
At their maximum values it equals exactly

\[
{2442796163\over16877486080}
={1\over8}+{333110403\over16877486080}>{1\over8}.
\]

The series ratio there is `3mτ=2307/131072<1`. This proves (2) on the
whole interval, allowing all higher interactions and all the specified
perturbations. There is no numerical time-step error or unresolved
spectral truncation in this argument.

## 4. The first failed extension: sparse modes do not supply concentration

The recent [Palasek shell-model construction](https://arxiv.org/html/2605.13827v1)
uses a low-high amplification rate modeled by `L^α aL`, with `α>2` in
the viscous blow-up theorem. Its physical interpretation assumes spatial
concentration; its forcing protects dormant seeds. The theorem is about
that model, not the unforced PDE. Our calculation handles internally
generated nearby modes but supplies neither the concentration nor that
seed protection.

There is a simple exact restriction on a proposed finite-mode embedding.
If v has at most m nonzero Fourier coefficients, all with `|k|≤L`, then

\[
\|S(v)\|_{\infty,op}
\le\sum_k |k||\widehat v(k)|
\le L\sqrt m\,\|v\|_{2,av}.
\tag{13}
\]

For any high-frequency field h, its low-strain energy amplification
contribution is thus bounded by
`L√m ||v||2,av ||h||²2,av`. To realize a rate at least
`c L^α ||v||2,av`, uniformly as L increases with c fixed, one necessarily needs

\[
m\ge c^2L^{2\alpha-2}.
\tag{14}
\]

**Fixed Fourier sparsity only permits the exponent α=1 in this
mechanism.** Reaching `α>2` requires more than quadratic growth of the
Fourier support count. Full three-dimensional dependence alone does not
supply that concentration. This elementary Fourier estimate is not new;
its role here is to reject extending the present sparse prototype as
if it already had the shell model's amplification power.

More quantitatively, let `aL=||v||2,av` and let all frequencies of h be
at least H. For this low-strain channel even to exceed viscous damping,
it is necessary that

\[
m> {\nu^2H^4\over L^2a_L^2}.
\tag{15}
\]

The full solution's energy bounds aL by its initial mean L² norm. With
`H=L^b`, fixed positive viscosity and bounded energy, (15) demands at
least the power `L^(4b−2)` in m. Since a ball of radius L contains only
O(L³) lattice points, this channel cannot win asymptotically when
`b>5/4`. At `b=5/4` constants and amplitudes matter; the inequality
does not decide the boundary. This is a **necessary scaling restriction
on the selected amplification channel**, consistent with the model's
parameter window. It is not an exclusion of arbitrary NS cascades:
generated intermediate modes, other channels and source terms remain.

The first failed line of a sparse-cascade extension is consequently
the replacement of the actual `L√m aL` rate by `L^α aL`, `α>2`,
without producing the required growing m and coherent strain. Constants
cannot repair this lost power. NS does not preserve finite support;
(13)–(15) apply to whatever low packet is actually being used at a
given time, not to the whole future solution under a sparsity assumption.

## 5. Scale accounting and falsification

| Quantity | Dependence and limit |
|---|---|
| Local expansion parameter | `x=NWt`; independent of viscosity only because heat is bounded above by 1 |
| Local guaranteed interval | `t≤1/(6NW)`; cannot be reset indefinitely without controlling W |
| Prototype activation time | `1/(512AN)`, requiring `A≥νN` |
| New coefficient | at least `A/4096` at that time; a small fraction of the original amplitude |
| Remainder | (5) in A0, (6) in A3, including every order and frequency |
| Distant empty bands | exponentially suppressed by (8) during this interval |
| Low-mode amplifier | at most `L√m aL`; α>2 needs m growing faster than L² |
| Infinite iteration | unproved; profiles, errors, seeds and growth intervals are not propagated |

Increasing N while keeping the theorem's Re condition changes A and
therefore the initial energy. These are different smooth initial data,
not a single singular solution. Even if the next packet could be put
back into the prototype class at frequency `√2 N` with its guaranteed
amplitude `A/4096`, the guaranteed Reynolds number would be multiplied
by `1/(4096√2)`. This lower bound cannot sustain the hypothesis through
infinitely many steps. It also does not prove the actual amplitude is
that small: failure to obtain a larger lower bound is not an upper bound.

| Test object | Applicability and result |
|---|---|
| Geometric, slow and ESS-compatible scalar ledgers | Not Fourier solutions of the stated initial-value problem; cannot be counterexamples to (2) or satisfy its proof assumptions. They still warn against replacing the dynamics by moments. |
| Spatial E/Q/D-matched path | Does not satisfy (3); the known momentum residual prevents using the convergent solution expansion for that path. No repeated residual experiment is needed. |
| Static and affine witnesses | Test instantaneous estimates only; (2) uses an actual periodic solution throughout a fixed interval. |
| One-direction shear/heat solution | B(u,u)=0. Its exact expansion creates no modes, so no universal activation conclusion is being inferred from the majorant. |
| Prior 2D3C obstruction | The present data have Fourier rank three; a small finite-band perturbation is included in the estimate. This does not solve the earlier full-3D cumulative-enstrophy gap. |
| Pressure and feedback deletion | Explicitly fails the cubic-order checks above. |
| Finite invariant triad | Explicitly fails: the next order creates √5 modes. |
| Palasek's regular norm growth | Compatible. A small local transfer is not a criterion separating regularity from singularity. |
| Arbitrary high-frequency initial tails | Outside the finite-band theorem. Their heat evolution and mixed interactions must be included in any extension. |

The exact Fourier checks were also compared with independent physical
products and spectral pressure on grids 16 and 24. Those are finite
algebra checks, not DNS or numerical evidence for an asymptote. The
universal-in-time-within-the-window statements come from the written
majorant proof and its exact rational margin, not from these grids.

**Verification receipt:** 22/22 exact instrument checks and 38 focused
tests passed (new activation tests plus transfer, cap-vacuity and route
classification pins). The coverage audit passed at 357 nodes with the
same three existing warnings. No new DNS, proof-assistant verification,
external computer-assisted reproduction or CI run was performed.

## 6. Next mathematical obligation

**Same-day completion update:**
[the concentrated-packet follow-up](concentrated-packet.md)
has executed this task at its stated restricted scope. It supplies an
explicit packet and background persistence, then excludes the specified
short-time activation of a sufficiently small seed. The
[steady-background supplement](steady-background.md) gives
a longer comparison interval and the current next carrier test. The
paragraphs below preserve the original work package; do not repeat it.

Do not commission a larger simulation of the sparse seed or optimize
the small threshold in (2). The next class must have spatially
concentrated packets and a growing number of active Fourier modes.
Use (14)–(15) as necessary tests before choosing a family.

One concrete scale test is `H=L^(11/10)`, `aL=L^(−1/10)`, and a smooth
Fourier packet occupying O(L³) modes in an annulus comparable to L.
It permits the *upper-bound* strain power `L^(12/5)` against damping
`νL^(11/5)`. This arithmetic leaves room; it proves neither the sign
nor attainment of the upper bound. A real solenoidal construction can
be specified by a fixed smooth transverse Fourier profile, sampled on
that annulus and normalized in L². Constants, polarization and spatial
overlap must then be computed from that profile.

The next estimate must show whether a high packet remains aligned and
overlapping for enough accumulated strain to reach its prescribed
amplitude from an admissible seed, including transport, deformation,
pressure, viscous losses and backreaction. The seed must be inherited
from the same initial datum or quantitatively generated by the full
equation. It cannot be maintained by an unaccounted force.

The present absolute majorant only covers a fraction of a nonlinear
turnover and deteriorates with `W≈√m aL`. It does not establish a
long-lived straining region, adequate gain from very small seeds, or
uniform transition error bounds. Those are the substantive missing
dynamics. A useful next result must control at least one of them in
the concentrated packet class; an expression containing the same
uncontrolled integral would repeat the earlier problem.

For Transformatics, the worked case illustrates a concrete separation:
the transformation to homogeneous interactions preserves the full
equation; the convergent sum controls discarded terms; the sparse
embedding loses a required scale power. The local theorem is true,
while its value for ROOT is limited. Keeping those judgments separate
is part of the method, not a new regularity claim.
