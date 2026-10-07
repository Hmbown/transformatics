# Q-GSO takeover: repaired compactness, cumulative prices, and the pressure gap

**Standing:** ROOT, `(E′)`, and Q-GSO averaged noncollapse remain **OPEN**.
This attempt does not solve Navier–Stokes. The starting checkout was clean
at `8f19a126`, following `a20e7637`. The sharpened spatial floors are not
reopened. The new work is an analytic audit of the argument built on them.

**Evidence:** written proofs below, exact symbolic identities, explicit
sequence/scalar obstructions, and arithmetic regressions in
`experiments/nse_qgso_prefix_audit.py` and
`tests/test_nse_qgso_prefix_audit.py`. A passing test is not a proof of
compactness, an infinite-series assertion, or regularity. No DNS was run.

## 1. An exact cumulative form of Q-GSO, without a peak/mean assumption

Let `[a_j,b_j]` be disjoint last-to-first Q-rungs with lower levels
`q_j=q_0 rho^j`, `rho>1`, and let `P_j={t in [a_j,b_j]: Q'(t)>0}`.
Write `d_j=|P_j|`, **the positive-set duration**, and define

```text
m_j = (1/d_j) int_Pj M dt,
c_j = (1/(d_j q_j)) int_Pj Q dt,        1 <= c_j <= rho,
B_j = log(m_j/m_0) - j log rho
    = sum_(k<j) [log(m_(k+1)/m_k) - log rho].
```

Here `d_j` is not the dissipation-thickness diagnostic with the same
letter in older notes. Smooth completed rungs have `d_j>0`. Directly,

```text
Hbar_j = (q_0/m_0) c_j exp(-B_j).
```

Consequently **averaged noncollapse is equivalent to**
`sum_j exp(-B_j)=infinity`. If this series diverges, the already-proved
Q-GSO theorem gives continuation. In particular

```text
B_j <= C + alpha log(j+1),   alpha <= 1,
```

is sufficient. The bound `M_sup,j <= K m_j` in the older sufficient
package is unnecessary for this exact mean-strain formulation. This is
an algebraic sharpening of that package, not a proof of its hypothesis.
Replacing `d_j` by `b_j-a_j` would destroy the stated meaning of `c_j`
when the positive set omits part of a rung.

A related version needs no mean-strain measurements. For **any** positive
`R_j >= sup_[a_j,b_j] M`, put

```text
A_j = log(R_j/R_0) - j log rho.
Hbar_j >= q_j/R_j = (q_0/R_0) exp(-A_j).
```

Thus `sum exp(-A_j)=infinity` suffices. This version is only sufficient:
an unnecessarily large `R_j` can make its floor summable while the true
prices are not. The distinction between exact mean prices and peak
floors must be retained.

## 2. Fixed-epsilon escape is not a necessary consequence

The earlier pressure face inferred from `gamma_j<=1` eventually being
sufficient that escape must have `gamma_j>=1+epsilon` infinitely often
for some fixed `epsilon>0`. That inference is false. The valid
contrapositive gives only `gamma_j>1` infinitely often.

There is a continuous scalar obstruction, not just a finite list of
numbers. For `r>=0`, `L>=4`, and `h=log rho`, set

```text
Q(r) = exp(r),      M(r) = exp(r)(r+L)^2,      dt/dr = 2/M(r).
```

Then `t` increases to a finite terminal time, since
`dt/dr <= 2 exp(-r)/L^2`. Also

```text
Q'/(M Q) = 1/2 < c_B = 4/(3 sqrt(6)),
M'/M^2 = (1/2)(1+2/(r+L)) <= 3/4,
int_0^T Q dt = 2/L < infinity,       int_0^T M dt = infinity.
```

The rungs are exactly `r in [jh,(j+1)h]` and are wholly positive. Their
actual prices satisfy the **exact** formulas

```text
Hbar_j = 1/[(L+jh)(L+(j+1)h)]
       = (1/h)[1/(L+jh)-1/(L+(j+1)h)],
sum_(j>=0) Hbar_j = 1/(hL) < infinity.
```

Their maxima occur at the upper endpoint, so

```text
gamma_j = 1 + (2/h) log[1 + h/(L+(j+1)h)] -> 1 from above.
```

Every fixed positive epsilon is eventually missed. This construction
obeys the displayed Q/M rate controls and the finite Q budget. It is
**not a Navier–Stokes velocity field** and is not claimed to satisfy
every spatial constraint or every item in the old standard battery.
Its purpose is to disprove the claimed logical implication from those
scalar inputs. The original pure blob is still an obstruction too:
its geometric prices also fail the new cumulative noncollapse gate.

This example explains why a useful dynamic bound must control the
**accumulated** excess. A vanishing per-rung excess can still accumulate
as `2 log j`, enough for summable prices. The `log j` threshold, with
coefficient at most one, includes the harmonic boundary case.

## 3. The correct strain-rate clock and its time intervals

Use `S=sym grad u`, `Omega=skew grad u`, `omega=curl u`, and
`H=Hess p`. For a smooth unforced incompressible solution,

```text
(partial_t + u.grad) S = nu Delta S - S^2 - Omega^2 - H,
S:Omega^2 = (1/4) omega^T S omega,
(1/2)(partial_t+u.grad)|S|^2
 = nu S:Delta S - tr(S^3) - (1/4)omega^T S omega - S:H.
```

At a spatial maximum of `|S|`, advection of `|S|^2` vanishes and
`S:Delta S=(1/2)Delta|S|^2-|grad S|^2<=0`. Let `X(t)` be the **entire**
argmax set, not one tracked point. For `M(t)>0`, Danskin's theorem and
the sharp trace-free matrix bounds yield, almost everywhere,

```text
D^+ log M(t) <= F(t),
F(t) = M(t)/sqrt(6)
     + sup_(x in X(t)) |omega(x,t)|^2 / (2 sqrt(6) M(t))
     + sup_(x in X(t)) |H_tf(x,t)|_F / M(t).
```

Indeed `-tr S^3<=M^3/sqrt(6)` and
`-omega^T S omega<=sqrt(2/3) M |omega|^2`. Pressure contraction uses
the Frobenius norm of the trace-free Hessian. A largest positive
eigenvalue by itself is not that norm or a bound with constant one.
This is a valid, nonnegative upper clock; a signed contraction can
produce a sharper one if handled with the same argmax bookkeeping.

The old probe's `S2_max_eig + PH_max_tracefree` omits the vorticity
contribution and mixes a matrix-eigenvalue diagnostic with the
Frobenius-strain derivative. A useful algebraic regression is
`S=diag(-2,1,1)`, `omega=(4,0,0)`, and isotropic
`H=-(tr((S+Omega)^2)/3)I`. The affine ODE
`A'=-A^2+(tr A^2/3)I` gives an exact local affine NS flow on `R^3`.
At this instant

```text
M' = 14/sqrt(6) > 4 = lambda_max(S^2) + lambda_max(H_tf).
```

The corrected bound is an equality for this jet. This disproves the
claimed matrix-algebra justification; the affine flow is **not** a
periodic finite-energy counterexample to the entire old rung statement.
The old periodic bound is withdrawn as unproved. Its finite-run sanity
flags remain reproducible observations, not a theorem certificate.

The spatial pressure inequality P1 survives:

```text
sup |H_tf|_F <= sup |H|_F <= sum_(k!=0)|fhat_k|
             <= sqrt(Z_3(2)) ||f||_Hdot2,
f = tr((grad u)^2) = |S|^2 - |omega|^2/2.
```

The old equality `f=|grad u|_F^2` is also false; the valid replacement
is `|f|<=|grad u|_F^2`, hence `||f||_2<=||grad u||_4^2` with matching
normalizations. P1 and the spatial carrier floors need only this
inequality. Historical scalar P4 clock calculations do not specify a
velocity field and cannot establish the missing dynamic upper bound.

For a clock-to-prefix route that accounts for all intervening times,
let `R_j=bar M(b_j)`, `bar M(t)=sup_(0<=s<=t)M(s)`, and define
`K_j=int_(b_0)^(b_j) F(t) dt`. The running maximum increases only when
`M=bar M`; thus `log(R_j/R_0)<=K_j`. Because `R_j` bounds rung j,

```text
K_j <= j log rho + C + alpha log(j+1),   alpha<=1,
```

would discharge noncollapse by section 1. Integrating only over a
positive-Q set or a single Q-rung cannot generally control the ratio
of maxima in successive rungs: maxima can occur inside the rungs and
growth can occur in the intervening gaps. The full prefix above avoids
that gap. No bound of the displayed strength is proved here. In
particular bounding the pressure part alone is insufficient without
controlling the local and vorticity contributions.

## 4. Repair of the compact branch

The original compact/spread note made two invalid intermediate steps:
`|S|<=1` does not imply `|grad u|<=1` or `|u(y)-u(0)|<=|y|`, and
subtracting `u(x_j,t)` while keeping the observation point fixed is
not a time-dependent Galilean symmetry. The exact periodic NS solution
`u=(1,exp(-t) sin(x-t),0)` exposes the latter error: subtracting its
value at the fixed origin leaves an equation residual with curl
`exp(-t) sin(x-t) e_z`, which no pressure correction can absorb.
Translating by the particle path `X(t)=(t,0,0)` as well repairs it.
The same fixed-origin defect occurs for the mean-zero two-dimensional
Taylor–Green solution shifted by `pi/4` in both coordinates; its bad
residual curl is `exp(-4t) sin(x-y) e_z`, also checked symbolically.

There is a cleaner repair which needs no time-dependent frame. First
remove the conserved spatial mean using an ordinary constant Galilean
transformation. The resulting periodic velocity has zero mean.

**Uniform spatial inequality.** For a mean-zero solenoidal velocity on
a torus of arbitrary period `L`, Sobolev and Korn at exponent two give
`||u||_6<=C||S||_2`. Korn at exponent six and interpolation give
`||grad u||_6<=C||S||_6<=C||S||_2^(1/3)||S||_infinity^(2/3)`.
Gagliardo–Nirenberg, with the zero-mean Poincare inequality absorbing
the torus lower-order term, gives

```text
||u||_infinity <= C ||u||_6^(1/2) ||grad u||_6^(1/2)
               <= C ||S||_2^(2/3) ||S||_infinity^(1/3).
```

All constants are independent of `L`: rescale to the unit torus and
the powers of `L` cancel. No endpoint `L^infinity` Korn inequality is
used. On `R^3`, the corresponding statement uses the decaying `L^6`
representative, not an arbitrary representative modulo rigid motions.

At strain-record times `t_j` with `M(t_j)=bar M(t_j)=M_j -> infinity`,
let `ell_j=sqrt(nu/M_j)`, and let `x_j` be actual strain maximizers.
On the expanding torus define the **unsubtracted** rescaling

```text
v_j(y,tau) = (ell_j/nu) u(x_j+ell_j y, t_j+tau/M_j).
```

It solves viscosity-one NS for `-M_j t_j<tau<=0`. Its strain satisfies
`||S(v_j)||_infinity<=1` and `|S(v_j)(0,0)|=1`, while

```text
int_(one period) |S(v_j)|^2 <= eta_bar_j
       = Q_bar(t_j)/(nu^(3/2) sqrt(M_j)).
```

If `eta_bar_j<=C_eta` along a subsequence, the spatial inequality
implies `||v_j||_infinity<=C C_eta^(1/3)` uniformly in space and all
backward times. Lift these smooth periodic solutions periodically to
`R^3`. They are bounded mild solutions there. Interior mild-solution
regularity gives uniform derivative bounds on every fixed backward
time window, including one-sided bounds at zero. The backward
lifespans tend to infinity. Compactness and the mild integral formula
then give a bounded ancient mild limit, with convergence of the first
spatial derivatives at `(0,0)`; therefore its strain is nonzero there.
This uses the standard bounded-mild compactness theorem, specifically
[KNSS, sections 4 and 6, Lemma 6.1](https://www-users.cse.umn.edu/~sverak/publications/liouville.pdf).
The periodic lift avoids an unproved change-of-domain compactness step.

For each fixed ball, it eventually fits in one expanding period.
Fatou and then exhaustion by balls give
`sup_tau int_R3 |S(v_infinity)|^2 <= C_eta`. Uniform `L^6` bounds also
pass to the limit. With bounded derivatives the limit tends to zero
spatially at **each fixed time**; uniform decay over the entire ancient
time axis is not asserted. Affine rotations and affine strains are
excluded by bounded velocity and the global `L^6`/enstrophy bounds.

This repairs the compact branch. It does **not** construct an ancient
limit from the strain bound alone on the spread branch.

The precise remaining conjecture is:

> **L-eta-m (OPEN).** A bounded ancient mild NS solution on `R^3` with
> uniformly finite strain enstrophy and the `L^6` representative is zero.

The general KNSS bounded-ancient-mild Liouville conjecture would imply
this restricted statement. Strict logical weakness is not established.
Finite enstrophy alone does not imply an `L^3` bound, so ESS does not
exclude this entire compact class. A single scalar self-similar blob
with bounded `L^3` is a much smaller obstruction class.

## 5. What eta and gamma actually say

The elementary alternative is `liminf eta_bar_j<infinity` or
`eta_bar_j -> infinity` along the **chosen strain-record sequence**.
One may not silently replace these records by per-Q-rung maxima.
For the separate diagnostic `eta_j=q_j/(nu^(3/2)sqrt(R_j))`, the exact
algebraic relation is

```text
log(eta_j/eta_0) = (log rho)/2 sum_(k<j)(2-gamma_k),
gamma_k = log(R_(k+1)/R_k)/log rho.
```

This is a prefix relation, not an eventual pointwise condition. For
`q_j=4^j`, the sequence `R_j=16^j a_j`, with `a_even=1,a_odd=2`, has
bounded eta and gamma alternating `2.5,1.5`. The sequence
`R_j=8^j a_j`, with `a_even=1,a_odd=4`, has eta tending to infinity
but gamma alternating `2.5,0.5`. Both `R_j` are increasing. These
explicit examples refute the previous equivalence with `gamma>=2`
eventually and the claimed `limsup gamma<=2` consequence of spread.

Nor does `eta_j -> infinity` settle the floor series:

```text
q_j/R_j = nu^3 eta_j^2/q_j.
```

A sufficient harmonic-scale growth is
`eta_j >= c sqrt(q_j/(j+1))`; unboundedness alone is much weaker.
Finite data with eta between roughly `1.2e5` and `8.5e6` establish
only large measured ratios. They do not classify either asymptotic
branch or prove that the compact branch is unreachable by all DNS.

## 6. Attempt on the stationary subcase, and the remaining gap

For a smooth stationary decaying solution, the usual cutoff energy
argument has a boundary error of the form

```text
C R^(-2) int_(R<|x|<2R)|u|^2
 + C R^(-1) int_(R<|x|<2R)(|u|^3+|p||u|).
```

Finite Dirichlet integral gives `u in L^6` in the decaying gauge, but
does not make the second term vanish by Holder alone. Adding a
bounded gradient does not fix that integrability deficit. An explicit
smooth solenoidal function-space obstruction is

```text
u_alpha(x,y,z) = (-y,x,0)/(1+x^2+y^2+z^2)^((alpha+1)/2),
alpha=3/5.
```

It has bounded gradient, finite `||grad u||_2` and `||u||_6`, but is
not in `L^(9/2)`. Its absolute cubic cutoff estimate scales as
`R^(2-3alpha)=R^(1/5)`. It is **not a stationary NS solution**: the
z-component of `curl((u.grad)u-Delta u)` equals 16 at the origin, so
no pressure gradient can cancel its residual. Its signed radial
transport can cancel. It demonstrates exactly why
the attempted absolute-value boundary estimate does not close; it
does not disprove the Liouville conjecture or a cancellation argument.

The literature check found additional sufficient criteria, not a
discharge of these missing assumptions. For example
[Tan, Corollary 1.1](https://arxiv.org/html/2501.03609v1) requires
low-frequency control beyond the Dirichlet bound, and
[Cho–Yang, Theorem 1](https://arxiv.org/html/2603.23833v1) assumes an
additional annular growth bound. Their hypotheses cannot be replaced
by merely finite enstrophy in this attempt. This is a scoped literature
check, not a proof that no relevant theorem exists.

**Actual next analytic target:** derive a dynamic, spatially justified
upper bound on the complete clock prefix in section 3, at most
`j log rho + log(j+1)+O(1)`, or prove a comparable bound on the exact
mean-strain prefix in section 1. Test every candidate against both the
old geometric blob and the new slowly summable scalar ledger before
DNS. The positive pressure amplitude, the omitted vorticity term, and
their coupling to the finite dissipation budget remain uncontrolled at
this strength. Neither the stationary attempt nor the repaired
compactness argument proves that bound.

## 7. Verification and preserved evidence

The focused local suite passes **92 tests**; the final affected subset
passes **18 tests**, including the mean-zero moving-frame regression.
The new receipt contains 30 passing symbolic/arithmetic checks. Ruff
passes on the new audit code/tests and the edited eta diagnostic/tests.
`scripts/coverage_audit.py` passes with **349 nodes** and its three
pre-existing single-attack-path warnings. These checks validate the
stated implementation and bookkeeping, not unconditional regularity.

The focused selection is reproducible with:

```sh
.venv/bin/python -m pytest -q tests/test_nse_growth_set_osgood.py \
  tests/test_nse_qgso_{mu_reduction,regularity_conditional,floor_sharp,floor_slack_verdict,compact_spread,pressure_nonlocal,prefix_audit,carrier_width_bridge,strain_half,h2clock_verdict,ksplit_verdict,phoctave_verdict,phoctave_deep_verdict,strainshare_verdict}.py
.venv/bin/python scripts/coverage_audit.py
```

The campaign JSON and dense NPZ, floor-slack probe, sharpened-floor
receipt, and both frozen pressure-Hessian receipts were checked
byte-for-byte against `8f19a126` and are unchanged. Historical pressure
receipt narratives are superseded by section 3 and the machine graph's
claim supersession, while numerical rows and frozen verdicts are
preserved. The derived eta receipt alone was regenerated for corrected
endpoint handling and interpretation; the nonlocal-pressure receipt's
claim metadata was corrected while its numerical checks were retained.
