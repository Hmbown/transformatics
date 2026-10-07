# The missing half-power is one spatial dimension — energy codimension ledger

**Date:** 2026-07-25.
**Prediction:** recorded before the fields were recomputed.
**Resolved verdict:** **Outcome B (transitional)**.  The registered prediction
was Outcome A and was wrong.
**Scope:** the criterion below is analytic. The later numerical observations are historical experiments.

## 0. Summary

The global energy dissipation does contain the missing half-power, but only
after one additional geometric input.  Put

```text
M(t)       = ||S(t)||_infinity = sqrt(g_max(t)),
E_theta(t) = {x : |S(x,t)|_F >= theta M(t)},
V_theta(t) = |E_theta(t)|,
H_theta(t) = M(t) V_theta(t).
```

Then:

> **Energy-Codimension Criterion (PROVED, elementary).**  If for some fixed
> `theta in (0,1)`, `M_0`, and `h_0>0`,
> `H_theta(t) >= h_0` whenever `M(t)>=M_0`, then the solution continues
> smoothly.  Equivalently, the sufficient geometric gain is
> `V_theta >= h_0/M = h_0/sqrt(g_max)`.

This is the requested half-power.  At the parabolic strain scale
`r=M^(-1/2)`, it says that intense strain may shrink in at most two spatial
directions: `V_theta >= c r^2`.  Isotropic concentration has
`V_theta~r^3=M^(-3/2)` and misses by exactly one spatial dimension.

Two attacks delimit the result:

1. **CKN plus the magnitude of the global dissipation budget is insufficient
   by itself (PROVED scale ledger).**  An isotropic type-I octave costs only
   `O(r)` dissipation, so dyadic costs are summable, while every octave costs
   `O(1)` BKM clock, so that clock diverges.  CKN detects every octave but does
   not make it expensive enough.  The proposed direct
   parabolic-average-to-pointwise `(D)` bridge is therefore **DEAD as a
   standalone magnitude argument**.  This does not rule out an NS-specific
   CKN bridge with a new geometric or evolutionary input.
2. **Universal kinematic noncollapse is false (PROVED scaling family).**
   Smooth compactly supported divergence-free packets have bounded (indeed
   vanishing) kinetic energy while `H_theta -> 0`.  Any useful noncollapse
   statement must be evolutionary and solution-dependent.

The registered DNS discriminator lands between the two clean geometries.
At the peak, the `theta=.7` effective dimension is `2.6045` on the grid and
`2.6154` after an independent `3N/2` Fourier replay; the corresponding
`H` ratio is `.8863/.8832`.  Both paths resolve frozen **Outcome B**.  The
threshold scan reveals a new morphology: a broad filamentary shoulder
(`theta=.5`, `d_eff=1.11/1.21`) surrounding an approximately isotropic core
(`theta=.9`, resolution-sensitive).  This is NUMERICAL on two smooth Kida
trajectories, not a theorem.

ROOT remains OPEN.

## 1. Exact packing identity and continuation criterion

For a smooth solution on `T^3`,

```text
E(t) = 1/2 int |u|^2 dx,
dE/dt = -nu int |grad u|^2 dx = -2nu int |S|_F^2 dx.
```

On `E_theta(t)`,

```text
|S|_F^2 >= theta^2 M(t)^2.
```

Therefore

```text
theta^2 M(t)^2 V_theta(t) <= int |S|_F^2 dx
```

and, after time integration,

```text
int_0^T M(t)^2 V_theta(t) dt
    <= E(0)/(2 nu theta^2).                         (1)
```

Suppose `H_theta=M V_theta>=h_0` whenever `M>=M_0`.  On those times,

```text
M <= h_0^(-1) M^2 V_theta.
```

Equation (1) makes the right side integrable.  On the complementary times
`M<=M_0`, the time integral is finite trivially.  Hence

```text
int_0^T ||S(t)||_infinity dt < infinity.
```

The vorticity maximum inequality
`d||omega||_infinity/dt <= ||S||_infinity ||omega||_infinity`, followed by
BKM continuation, closes the proof.  No pressure estimate, winding estimate,
or pointwise viscous lower bound is used.

In the old `g` notation, (1) controls `int g_max V_theta`; the noncollapse
condition supplies `V_theta>=c g_max^(-1/2)`, leaving
`int sqrt(g_max)`.  Thus the algebraic half-power and the geometric
one-dimension gain are the same object.

## 2. Why CKN alone is one dimension short

Consider a dyadic parabolic scale `r_n=2^(-n)`.  The type-I bookkeeping is

```text
strain amplitude M_n ~ r_n^(-2),
duration           dt_n ~ r_n^2,
isotropic volume   V_n  ~ r_n^3.
```

The unscaled energy/dissipation cost of the octave is

```text
M_n^2 V_n dt_n ~ r_n^(-4) r_n^3 r_n^2 = r_n.
```

Thus

```text
sum_n M_n^2 V_n dt_n ~ sum_n 2^(-n) < infinity,
sum_n M_n dt_n       ~ sum_n 1       = infinity.
```

Moreover the CKN-scaled cost is exactly critical:

```text
r_n^(-1) [M_n^2 V_n dt_n] ~ 1.
```

So a singular-scale ledger can satisfy the CKN lower bound at every scale,
spend finite global dissipation, and accumulate infinite BKM clock.  This is
not an NS blowup construction.  It is a rigorous compatibility calculation:
the two scalar inequalities alone have no contradiction in them.

If one spatial direction does not shrink, `V_n~r_n^2`; then every octave costs
`O(1)` energy, and infinitely many octaves contradict (1).  That is exactly
the codimension threshold in the theorem.

**Obituary.**  The handoff proposed converting a CKN parabolic average into a
pointwise lower bound on `nu|grad S|^2` at the maximizer.  Average-versus-
pointwise is a real obstruction, but it is not the first obstruction.  Even
before pointwise localization, the CKN lower bound spends only `O(r)` per
scale.  A new one-dimension noncollapse, quantization, topology, or equivalent
fixed-cost-per-octave mechanism is required.

## 3. Kinematic falsifier

Let `A` be a nonzero smooth compactly supported vector potential in a ball
strictly inside a coordinate chart of `T^3`, and let `U=curl A`.  For large
`lambda`, define

```text
u_lambda(x) = lambda U(lambda(x-x_0))
```

on its shrinking support and zero outside.  It is smooth, periodic, and
divergence-free.  Direct change of variables gives

```text
||u_lambda||_2^2      = lambda^(-1) ||U||_2^2,
M_lambda              = lambda^2 M_U,
V_theta(u_lambda)     = lambda^(-3) V_theta(U),
H_theta(u_lambda)     = lambda^(-1) H_theta(U) -> 0.
```

Every member is legitimate smooth NS initial data.  Adding a fixed
divergence-free background with disjoint support keeps the total kinetic
energy bounded away from zero while the concentrated packet still dominates
the strain maximum.  Therefore no lower bound for `H_theta` can follow
kinematically from incompressibility and an energy bound, even with constants
depending only on that bound and `nu`.

This is the volume analogue of the amplified Taylor--Green falsifier for
pointwise `(D)`: the surviving target is irreducibly evolutionary.

## 4. Registered E3 discriminator

The exact E3 dynamics were replayed with two FFT workers.  The principal path
measures the grid field; the independent path zero-pads the retained peak
velocity coefficients to `3N/2`, reconstructs `S`, and uses its own maximum
and cell volume.

### 4.1 Measurement gates

| gate | low-M `N=96, nu=.01` | high-M `N=128, nu=.005` | verdict |
|---|---:|---:|---|
| G-C1 `g_peak` replay error | `0.305%` | `0.011%` | PASS |
| G-C2 peak spectrum tail | `.00755` | `.00854` | PASS |
| G-C3 max divergence | `5.5e-15` | `8.0e-15` | PASS |
| G-C4 `V_.7` grid/replay difference | `6.45%` | `7.31%` | PASS |

The grid peak data used in the frozen outcome are:

| cohort | peak time | `g_peak` (refined) | grid `M` | `V_.7` | `H_.7` |
|---|---:|---:|---:|---:|---:|
| low-M | `1.6000` | `152.099` | `12.6510` | `1.18427` | `14.9821` |
| high-M | `1.44041` | `334.990` | `18.8613` | `.7039999` | `13.2784` |

### 4.2 Geometry result

| `theta` | grid `H_high/H_low` | replay `H_high/H_low` | grid `d_eff` | replay `d_eff` |
|---:|---:|---:|---:|---:|
| `.5` | `1.1950` | `1.1731` | `1.1078` | `1.2096` |
| **`.7`** | **`.8863`** | **`.8832`** | **`2.6045`** | **`2.6154`** |
| `.9` | `.8087` | `.8734` | `3.0634` | `2.6706` |

The `.9` volumes are sampling-sensitive (grid/replay differences
`39.0%/29.3%`), so the apparent core dimension is DIAGNOSTIC only.  The
registered `.7` volume differences are below the frozen 15% cut and both
paths independently score **Outcome B**.

G-C5 (`H` ratio at least `.90`) fails narrowly.  G-C6 (`d_eff<=2.25`) fails.
The value `2.6045` lies inside the frozen transitional band `(2.25,2.75)`;
the gate was not moved.

An unregistered time-window check (`g>=g_peak/2`) makes the threshold split
sharper.  The high/low ratio of the minimum observed `H_theta` is
`1.102/.497/.340` for `theta=.5/.7/.9`.  This is exploratory because it was
not part of the frozen outcome.

## 5. Prediction accuracy

The registered prediction was Outcome A:

```text
H_.7(high)/H_.7(low) >= .90,
d_eff(.7) <= 2.25.
```

Measured:

```text
H ratio = .8863 grid / .8832 replay,
d_eff   = 2.6045 grid / 2.6154 replay.
```

The first miss is narrow; the dimension miss is decisive.  **Prediction A is
refuted; registered Outcome B is the result.**  The favorable `.5` threshold
is not substituted post hoc for `.7`.

## 6. What is now an ingredient of what

The live direct-to-ROOT implication is:

```text
one-direction noncollapse at some fixed theta
    + global energy dissipation
    -> finite strain BKM clock
    -> regularity.
```

This is a genuine reduction to a statement with explicit geometric content,
unlike `(D)`, which is equivalent to regularity.  But the noncollapse
hypothesis is OPEN, kinematically false, and supported only at the broad
`.5` shoulder on two finite-Re Kida trajectories.

The Shadow-Math defect is now explicit:

```text
D_codim,theta(t) = 1 / [M(t) V_theta(t)].
```

The easy shadow world has one macroscopic direction and bounded `D_codim`.
The real inverse attack is an evolving near-isotropic intense-strain blob for
which `D_codim -> infinity`.  Such blobs exist kinematically; the open
question is whether NS evolution can sustain them through an unbounded strain
ladder.

The next decisive computation, if funded, is a freshly registered
`theta=.5` test on the resolved `nu=.0025, N=192` and `nu=.001, N=256`
cohorts, recording fields at the peak rather than rerunning them repeatedly.
The analytic target is not “prove CKN.”  It is:

> **OPEN — evolutionary one-direction noncollapse.**  Show that for at least
> one fixed moderate `theta`, a high-strain component cannot shrink in all
> three spatial directions throughout an unbounded turnover ladder.

Anything weaker must state how it still produces fixed dissipation cost per
octave.

## 7. Classical neighbor (and non-claim)

The named object is the concentration dimension of strain superlevel sets.
Geometric measure regularity criteria based on local one-dimensional
sparseness of intense regions already exist; see Grujić,
[A geometric measure-type regularity criterion for solutions to the 3D
Navier--Stokes equations](https://arxiv.org/abs/1111.0217), and the later
asymptotic-criticality framework of Grujić--Xu,
[arXiv:1911.00974](https://arxiv.org/abs/1911.00974).

Those criteria and the lower-volume criterion here point in complementary
directions: sufficient sparseness lets diffusion win, while sufficient
noncollapse makes the global energy budget win.  **No covering dichotomy is
claimed.**  A near-isotropic blob can be globally small yet locally dense at
its parabolic scale, and is exactly the configuration the new node leaves
OPEN.
