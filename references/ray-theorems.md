# Ray-Class Boundedness Theorems for 2D Kinematic VSA

**Date:** 2026-06-09 (late); **UPDATED 2026-06-10** with the Ray-Mass Lemma
**Status:** Theorems 1–2 PROVED (elementary, self-contained); Theorem 3 proved
with regime-split (constant not optimized) and verified SHARP; **Ray-Mass
Lemma (§0b) PROVED in full generality** — it subsumes Theorem 1 and converts
the boundedness question into "is ray recruitment bounded?".
**Verification:** `experiments/vsa_ray_theorems_check.py`,
`artifacts/vsa_beurling/ray_theorems_check.json`

---

## 0b. The Ray-Mass Lemma (general; PROVED 2026-06-10)

> **Lemma (ray mass).** Let Q = Σ_{k∈Λ} q_k cos(k·x) be ANY trig polynomial
> with |Q(x)| ≤ A := |Q(0)| for all x ∈ T². For every primitive direction u
> (half-plane representative), let f_u(s) = Σ_t β_{tu} cos(ts) be the
> vorticity profile of the u-ray. Then
>
>     ‖f_u‖_∞ ≤ 2A    — in particular |Σ_t β_{tu}| = |f_u(0)| ≤ 2A.

*Proof.* Let v = (−u₂, u₁) and average Q over the 1-subtorus coset
x(τ) = x₀ + τv, where u·x₀ = c. For a mode k, avg_τ cos(k·x(τ)) = 0 unless
k·v = 0, i.e. k = tu; those modes have k·x ≡ tc. Since q_{tu} =
−(1/2)β_{tu}e^{2iθ_u} (constant Beurling phase along a ray),

    avg_τ Q = −(e^{2iθ_u}/2)·Σ_t β_{tu} cos(tc) = −(e^{2iθ_u}/2)·f_u(c),

and |avg Q| ≤ sup|Q| = A. ∎

Two immediate consequences:

1. **Theorem 1 is a corollary** (single ray: Σβ = f_u(0), r = f_u(0)²/4A² ≤ 1).
2. With the Plancherel constraint Σ_k β_k² ≤ 8A² (from ∫|Q|² ≤ A²), the
   boundedness question becomes exactly:

> **Ray-recruitment problem (equivalent to 2D kinematic VSA boundedness).**
> √r = (Σ_u m_u)/(2A) with per-ray |m_u| ≤ 2A. Is the number of rays that a
> feasible field can simultaneously load at Θ(A) mass bounded by a universal
> constant?

**Witness diagnostic** (2026-06-10): the certified witnesses load rays as

| witness | √r = eff. ray count | top ray masses /2A |
|---|---|---|
| N=5 (r=11.81) | 3.44 | 0.94, 0.48, 0.47, 0.29 |
| N=12 (r=15.94) | 3.99 | 0.90, 0.52, 0.47, 0.39, 0.25, 0.23 |
| N=32 (r=27.12, certified) | 5.21 | 0.79, 0.62, 0.60, 0.59, 0.23, 0.23 |

Growth is pure ray recruitment: the four cardinal/diagonal rays first, then
(1,±2)/(2,±1), then (3,±1)… each near a fixed fraction of its individual cap.
The decisive probe is therefore r(R) for explicit R-ray families
(`experiments/vsa_multiray_probe.py`).

**Line-average generalization** (same proof with weight e^{ijτ}): for every
lattice line ℓ = {k : k·v = j} (any direction, any offset), the twisted
coefficient sum along ℓ is bounded by A. The objective only has constant
Beurling phase on rays (lines through 0), but the full Radon-type family of
line constraints is available to any future cross-ray argument.

## 0c. Recruitment phenomenology (2026-06-10 probes)

Three measurements that frame the ray-recruitment problem:

1. **Shape-tied recruitment saturates at 3 rays.** The multiray Fejér probe
   (`experiments/vsa_multiray_probe.py`: per-ray amplitudes × shared profile
   shape, R = 2..16 rays offered) loads exactly three rays — masses/2A =
   1.00, 0.94, 0.93 on (0,1),(1,1),(1,−1) — and assigns 0.00 to every other
   offered ray; r flat at 8.21 from R = 4 to R = 16. With tied shapes,
   ridge collisions block further recruitment. (R=2 case = 1.0000 exactly:
   Theorem 2's perpendicular-ray ceiling, hit again.)

2. **No sparse-ray skeleton: feasibility is collectively shimmed.**
   Truncating the certified N=32 witness (980 rays) to its top-R rays by
   mass is catastrophically infeasible for EVERY R ≤ 50: feasibility
   restoration collapses all the way to the anchor (r = 1). The hundreds of
   small-mass rays are load-bearing — they patch competitor peaks created
   by the big rays. High-r fields are not "few rays + decoration"; the
   recruitment cost of a big ray includes a global shimming overhead.

2b. **Free per-mode profiles on explicit rays don't beat the shape-tied
   construction.** `experiments/vsa_multiray_free.py` (R = 3..8 rays, free
   per-mode β, Powell): best feasible r = 4.89 (3–4 loaded rays); the
   30–80-parameter landscape traps the optimizer in low basins — at R = 4
   it lands exactly on the Theorem-3 two-ray ceiling r = 2.0000 (another
   sharpness confirmation). The on-ray recruitment record remains 3 rays /
   r = 8.21; everything beyond demonstrably requires off-ray shimming.

3. **Plancherel occupancy is stable at ≈ 1/2, not binding.** mean|Q|²/A² =
   0.50, 0.48, 0.51, 0.54 for the r = 11.8/15.9/26.4/27.1 witnesses. The
   ℓ² budget has 50% slack throughout — the binding cross-ray constraint is
   genuinely sup-norm/Diophantine, not L². (The stable value ≈ 1/2 looks
   like a structural invariant of the extremal family; unexplained.)

4. **The shimming cloud is objective-ALIGNED, not opposed (2026-06-10,
   `experiments/vsa_shim_mass_diagnostic.py`, NUMERICAL; registered
   prediction partially confirmed, interpretation corrected).** Sub-threshold
   (|m_u| < 0.1·2A) ray ℓ¹ mass grows with recruitment — S_tot/2A = 0.97,
   1.31, 1.80 across the N=5/12/32 witnesses, marginal cost ≈ 0.30·2A per
   recruited ray beyond 3 (stable N=12→32) — CONFIRMING the registered
   growth prediction. BUT within-ray cancellation collapses (S_can/2A =
   0.53 → 0.18 → 0.016) and total ℓ¹ ≈ Σβ (excess 0.02·2A in the certified
   witness): essentially every mode of the extremal field contributes
   positively to the objective. The 970-ray tail is simultaneously the
   feasibility patch (top-50 truncations collapse, item 2) and ~30% of √r.
   There is no "wasted" ℓ¹ to budget against; the shimming-budget bound
   must instead price the tail's DIMINISHING objective return per unit of
   feasibility repair, or find a budget that the aligned tail itself
   exhausts (candidates: the line-average/Radon family, not ℓ¹ or ℓ²).

5. **The line-average (Radon) family is SLACK at the extremizers
   (2026-06-10, `experiments/vsa_line_saturation_census.py`, NUMERICAL;
   registered prediction REFUTED).** Census over all lattice lines with
   |v| ≤ 3 (282/492/1318 lines): near-tight lines (σ > 0.9) number 1, 0, 0
   across N=5/12/32, and the max saturation DECREASES with recruitment
   (0.94 → 0.90 → 0.88). Together with item 4 and the per-ray caps (top
   mass 0.79·2A) and Plancherel (≈ 1/2): NO known linear or quadratic
   constraint family is active at the witnesses. The binding constraints
   are the pointwise |Q(x)| ≤ A at the near-maximal set itself (the m-ray
   subtorus leak), so a budget argument must price the ACTIVE SET — its
   dual certificate (cf. `experiments/vsa_dual_representer*.py`) is the
   natural carrier, not any of the off-the-shelf relaxations.

6. **The active set is small and ~CONSTANT across recruitment (2026-06-10,
   `experiments/vsa_active_set_census.py`, NUMERICAL; registered
   prediction REFUTED).** Off-origin local maxima of |Q|/A above 0.99:
   8 → 13 → 9 across N=5/12/32 (above 0.95: 16/13/13). The number of
   near-ties does NOT grow with recruitment. Caveat: grid+Newton counts
   isolated local maxima; ridge-like near-maximal curves would be
   undercounted. Combined with items 4–5: recruitment proceeds with every
   measured budget slack and a fixed ~10-point contact set. The dual
   certificate on this small active set is now the sharpest object to
   compute: its weights are the prices of feasibility, and with only ~10
   support points against 1602 mode-equalities it is massively
   overdetermined — whatever structure lets it exist IS the recruitment
   mechanism (and its failure mode would be the boundedness proof).

7. **Atomic KKT closure FAILS — witnesses are not full-space optima
   (2026-06-10, `experiments/vsa_dual_atomic_closure.py`, NUMERICAL;
   registered prediction CONFIRMED).** Least-squares dual weights on the
   measured active atoms leave relative RMS residual 0.67/0.78/1.00 for
   N=5/12/32; for the certified witness λ ≈ 0: the objective direction is
   near-ORTHOGONAL to all active-constraint gradients. (Active points pair
   antipodally — |Q(−x)| = |Q(x)| — so the gradient matrix has rank ≈
   atoms/2.) Read: the witness sits at a parametrization wall, not a
   feasibility wall. There is a first-order unobstructed ascent direction
   (project 1 onto the null space of active gradients), so (i) r = 27.12
   should be beatable by projected-gradient ascent in full β-space [P3],
   and (ii) the boundedness question becomes: does this ascent terminate
   by ACCUMULATING active points until the dual system closes? The
   closure dynamics along the ascent is the recruitment mechanism, and
   the sharpest current attack on C₀ < ∞ [P1].

8. **REGISTERED PREDICTION (2026-06-10, pre-run) — projected-gradient
   ascent in full β-space (`experiments/vsa_projected_ascent.py`).** Setup:
   maximize Σβ at fixed g(0) from the certified N=32 witness (r = 27.1172),
   projecting the objective onto the null space of active-constraint
   gradients (envelope theorem at the Newton-refined competitor peaks),
   step-capped so no watched competitor crosses g0, Gauss-Newton tie
   restoration, every accepted step gated by the same `true_peak_violation`
   machinery that gated the certified witness (TIE_TOL 1e-9). Predictions,
   in decreasing confidence: **(a)** r climbs past 27.5 within the budget
   (≤ 600 steps) — the witness sits at a parametrization wall (item 7:
   λ ≈ 0, unit-scale unobstructed gradient), HIGH confidence; **(b)** the
   active set ACCUMULATES along the ascent, from ~0 strict ties (the
   certified witness was margin-re-optimized, peaks ≥ 1e-3 below g0) to
   ≥ 15 simultaneous near-ties (census found ~10 at ε = 0.01), MEDIUM
   confidence; **(c)** the KKT residual decreases from ≈ 1 but does NOT
   close (stays > 0.1) within budget — recruitment-limited ascent, no
   within-budget termination, LOW-MEDIUM confidence (this is the decisive
   part; r at fixed N = 32 IS bounded — Plancherel forces r ≤ 2·n_modes —
   so the ascent must terminate eventually; the question is whether the
   terminal structure is reachable and visibly closing). Refutation of (c)
   — residual → 0 with a small active set — would be the first direct
   evidence FOR a finite ceiling shape and would hand us the dual
   certificate at the true fixed-N optimum.

   **RESULT (2026-06-10, same day, `projected_ascent_N32.json`,
   NUMERICAL): all three predictions WRONG, for an unregistered reason.**
   The ascent gained only Δr = +0.0115 (27.1172 → 27.1287) and collapsed
   in 9 steps with ZERO far-competitor ties formed [(b) refuted] and KKT
   residual pinned at 1.0 [(c) technically as predicted but for the wrong
   reason]; r never approached 27.5 [(a) refuted as-run]. The binding
   constraint was never in the v1 constraint dictionary: the SOFT
   EIGENVALUE OF THE ORIGIN HESSIAN collapsed from −0.279·g0 (the
   certified margin) to ~0, a secondary maximum bifurcated at |x| ≈
   1.5e-3 along the soft eigenvector, and the acceptance gate (rightly)
   refused everything past viol = 1e-9. The v1 endpoint actually has
   λ_soft/g0 = +0.0017 — past the pitchfork (origin a saddle along the
   soft direction; the off-origin twin peaks 1e-9 above g0, inside
   TIE_TOL) — so r = 27.1287 is wall-grazing, NOT a clean record; the
   certified record stands at 27.1172.

9. **The witness wall is HESSIAN DEGENERATION of the origin, not far
   competitors (2026-06-10, `experiments/vsa_hessian_wall_closure.py`,
   NUMERICAL).** λ_soft(∇²g(0)) has an O(1) analytic β-gradient
   (simple-eigenvalue perturbation, FD-checked to 3e-6): the wall is a
   first-class constraint row, unlike the secondary-peak rows whose
   gradients vanish quadratically as the peak merges into the origin.
   Adding this single row to the atomic KKT system drops the closure
   residual 1.00 → 0.79 at the certified witness (the soft mode carries
   ~38% of the objective's squared norm; the ~10 far ties carry ≈ 0).
   Corrected reading of item 7: the ascent from the witness is
   unobstructed by far ties but obstructed at second order by origin-max
   degeneration — Σβ-ascent buys r at the price of Hessian margin
   (measured trade: Δr ≈ +0.0115 per 0.28·g0 of λ_soft). Residual 0.79
   means the system is still far from closed: the fixed-N optimum lies
   ALONG the wall (ride λ_soft ≤ −δ as an explicit constraint, with
   near-origin twin-peak detection as the verification layer — ascent
   v2). Open: whether wall-riding recruits the far ties (the registered
   accumulation picture, one level up) or terminates with the Hessian
   row closing the dual.

10. **Wall-riding ascent (v2): r = 45.9392 at N=32 — VERIFIED candidate,
   +69% over the certified record (2026-06-10,
   `projected_ascent_N32_v2_restored.json`).** With twin-peak detection,
   the λ_soft safety row, and blocker promotion, the ascent climbed
   27.1172 → 45.9397 in 42 steps, accumulating up to 44 simultaneous
   ties (7 near-origin twins). Under this corrected machinery the
   item-8 registered predictions land: (a) r > 27.5 CONFIRMED, (b) ≥ 15
   accumulated ties CONFIRMED, (c) no within-budget KKT closure —
   residual fell 0.79 → 0.26, rose to ~0.7 as ties released near the
   stall; closure UNRESOLVED (the stall is a machinery limit, not a
   measured KKT point). Endpoint restored against M = 4096 AND M = 8192
   true-peak verification (restoration cost 5e-7 of r): r = 45.939201,
   two independent code paths to 1e-13, viol = 0.0 on both grids,
   near-origin excess −5e-6, λ_soft/g0 = −0.19. √r = 6.78 effective
   rays vs 5.21 for the structured family at the SAME N: the
   structured-family scaling data (and its log-N fit) badly
   underestimate fixed-N recruitment; the log-vs-saturation question
   must be re-asked against full-β-space optima per N (v2 from the
   N=12 witness queued). Certification of the endpoint: in progress
   (`vsa_certify_beta.py`, margin backoff + the four layers).

   **Methodological lesson (now a standard):** the in-loop M = 2048
   acceptance gate leaked a 6.07e-5 violation that M = 4096 caught —
   with O(50) near-ties, top-K-seeded grid+Newton peak finding silently
   loses competitors. Tie-dense candidates must be gated on two grid
   resolutions (4096 + 8192 here), and a "stall" diagnosis is
   unreliable until the endpoint re-verifies at both.

11. **v2 from the N=12 witness: r = 30.2329 — N=12 ALONE now exceeds the
   old certified N=32 record (2026-06-10,
   `projected_ascent_N12_v2_restored.json`, VERIFIED: dual-grid clean
   with zero restoration, two code paths to 1e-13).** 15.9466 → 30.2329
   in ~410 steps, 47 active ties. Two structural findings: (i) the KKT
   residual fell near-monotonically to 0.065 — at N=12 the ascent is
   visibly CONVERGING to a KKT point (the fixed-N dual looks closable
   with better tie-dense machinery), unlike the N=32 run where the
   stall hit first; (ii) λ_soft/g0 ended PINNED at the artificial
   safety floor (−1e-4) — the true fixed-N optimum pushes the origin
   Hessian to DEGENERACY (λ_soft → 0, quartic regime), so the optimal
   extremal field has a flat-direction origin and any sharp fixed-N
   ceiling analysis must handle the 4th-order jet at the maximum.
   Full-β verified scaling so far: √r*(12) ≥ 5.50, √r*(32) ≥ 6.78
   (lower bounds; both endpoints stalled on machinery, not KKT).

**Where the boundedness proof must come from:** per-ray caps (§0b) +
pairwise ridge-intersection constraints allow √r ~ c·R; what stops
recruitment in practice is the interaction between a new ray's ridge system
and the existing field's near-maximal set, mediated by the shimming clouds.
Making that quantitative — e.g. a lower bound on the ℓ¹-mass of shims per
recruited ray, summed against the per-ray caps — is the sharpest currently
visible path to proving C₀ < ∞.

These are the first rigorous boundedness results in this program: complete
proofs of kinematic VSA on the pure-ray subclasses, powered by the mean-zero
mechanism described in the proofs below.

---

## 0. Setup

For a 2D streamfunction ψ = Σ_{k∈Λ} c_k cos(k·x) on T² (Λ ⊂ Z²\{0} finite,
c_k real), with k_c = k₁ + ik₂:

```
Q(x) = -(1/2) Σ c_k k_c² cos(k·x)     (complex strain;  g = |S|²_F = 2|Q|²)
T(x) = -Σ c_k |k|² cos(k·x)           (vorticity;  |Ω|²_F = T²/2)
β_k  = c_k |k|²                        (vorticity weight)
```

**Constraint (g-maximizer at 0):** |Q(x)| ≤ |Q(0)| =: A for all x ∈ T², A > 0.
**VSA ratio:** r = T(0)²/(4A²) = (Σβ_k)²/(4A²).

A *ray* is the set of modes {t·u : t ≥ 1} for a primitive u ∈ Z². All modes
on a ray share the strain phase w = e^{2i·arg(u)} (Beurling phase). For a ray
with direction u and 1D profile f(s) = Σ_t β_t cos(ts):

```
ray contribution to Q at x  =  -(w/2)·f(u·x),        Σβ_t = f(0).
```

**The mean-zero fact.** f has no constant term, so ∫f = 0, hence
min f ≤ 0 ≤ max f. This is the engine of every proof below.

---

## 1. Theorem 1 (single ray): r = 1

If Λ lies on one ray, Q(x) = -(w/2) f(u·x), so |Q(x)| ≤ |Q(0)| means
|f(s)| ≤ |f(0)| for all s: f attains its maximum modulus at 0. Then
|Σβ| = |f(0)| and 2A = |f(0)|, so r = f(0)²/f(0)² = **1** (when A > 0). ∎

## 2. Theorem 2 (two perpendicular rays, e.g. both diagonals or both axes): r ≤ 1

Let u₁ ⊥ u₂ (then w₂ = e^{2i(arg u₁ + π/2)} = −w₁). Write f₁, f₂ for the two
profiles, s_j = u_j·x. Then

```
Q(x) = -(w₁/2)·[f₁(s₁) − f₂(s₂)].
```

**Surjectivity.** x ↦ (u₁·x, u₂·x) maps T² ONTO T² (the integer matrix
U = (u₁; u₂) has det ≠ 0, so U: ℝ² → ℝ² is onto and descends mod 2π).
Hence the constraint is: |f₁(a) − f₂(b)| ≤ |f₁(0) − f₂(0)| =: D for ALL
(a,b) ∈ T², independently.

WLOG D = f₁(0) − f₂(0) > 0 (D = 0 forces g(0) = 0, excluded). Taking
a = argmax f₁, b = argmin f₂:

```
max f₁ − min f₂ ≤ D = f₁(0) − f₂(0) ≤ max f₁ − min f₂,
```

so equality: **f₁(0) = max f₁ and f₂(0) = min f₂.** By mean-zero,
f₁(0) ≥ 0 ≥ f₂(0). The objective is Σβ = f₁(0) + f₂(0) ∈ [−D, D] (it is a
sum of a number in [0, D] and that number minus D). Hence

```
r = (f₁(0) + f₂(0))² / D² ≤ 1.  ∎
```

Remarkable contrast: the *unconstrained-phase* heuristic suggested the
diagonal channel was "free"; the mean-zero mechanism caps it at r ≤ 1 — even
below the single-ray value augmented... the two-ray perpendicular class is
STRICTLY worse for the adversary than generic mixed classes (witnesses reach
27 by combining ≥ 4 rays with low-mode anchors).

## 3. Theorem 3 (two generic rays) — TIGHTENED 2026-06-10: the sharp law

Let u₁, u₂ be linearly independent primitive vectors, w_j = e^{2iθ_j} their
Beurling phases, γ = 2(θ₂ − θ₁) the phase angle. Then
2Q(x) = −[w₁f₁(s₁) + w₂f₂(s₂)] and by surjectivity (det(u₁;u₂) ≠ 0) the
value set over x is the full Minkowski sum

```
V = w₁·[m₁, M₁] + w₂·[m₂, M₂],     m_j = min f_j < 0 < M_j = max f_j
```

(strict signs by mean-zero unless f_j ≡ 0, which is the single-ray case),
a parallelogram. The constraint is V ⊂ D̄(0, 2A); p₀ = w₁f₁(0) + w₂f₂(0)
has |p₀| = 2A, is a farthest point of V, hence a vertex (|z|² is strictly
convex on segments): f_j(0) ∈ {m_j, M_j} =: ε_j.

**Theorem 3′.**
(i) r ≤ 2/(1+cos γ) for every γ ≠ π.
(ii) If cos γ ≤ −1/2 then r ≤ 1.
(iii) For −1/2 < cos γ the bound (i) is SHARP — attained by equal-max
profile pairs with ρ := |min f|/max f ≤ 1 − 2·max(0, −cos γ) (any
profiles for cos γ ≥ 0, e.g. single modes; Fejér profiles K_n − 1 with
1/n ≤ 1 − 2|cos γ| for −1/2 < cos γ < 0). Consequently
**C₂ = sup over two-ray classes = 4**, approached (never attained) as
cos γ ↓ −1/2; the old "two-ray ceiling 2.0000" was an artifact of
single-mode-profile optimizers, and the old regime-split C₂ ≤ ≈ 8 is
replaced by the exact envelope max(1, 2/(1+cos γ))·1_{cosγ>−1/2} + ...
i.e. r ≤ 2/(1+cosγ) if cos γ > −1/2, r ≤ 1 otherwise.

**Proof.**
*Mixed-sign vertex (ε₁ε₂ < 0, say ε₁ = M₁, ε₂ = m₂):* 4A² =
M₁² + |m₂|² − 2cosγ·M₁|m₂|. If cos γ ≤ 0 the cross term is ≥ 0, so
max(M₁,|m₂|) ≤ 2A and |ε₁+ε₂| = |M₁ − |m₂|| ≤ 2A: r ≤ 1. If cos γ > 0,
(ε₁+ε₂)² = M₁²+|m₂|²−2M₁|m₂| ≤ M₁²+|m₂|²−2cosγ·M₁|m₂| = 4A²: r ≤ 1.

*Both-extreme vertex (ε₁ε₂ > 0, say both maxima; both minima is the
mirror m_j ↔ −M_j):* the farthest-vertex identity and AM-GM give
4A² = M₁² + M₂² + 2cosγ·M₁M₂ ≥ 2(1+cosγ)M₁M₂, so

```
(M₁+M₂)² = 4A² + 2M₁M₂(1−cosγ) ≤ 4A²[1 + (1−cosγ)/(1+cosγ)]
         = 8A²/(1+cosγ),    i.e.  r ≤ 2/(1+cosγ).            (i)
```

*Infeasibility for cos γ ≤ −1/2 (write c = −cos γ ≥ 1/2):* the cross
vertices w₁M₁ + w₂m₂ and w₁m₁ + w₂M₂ also lie in D̄(0,2A):
M₁² + |m₂|² + 2c·M₁|m₂| ≤ 4A² forces M₁ < 2A strictly (|m₂| > 0), same
for M₂. But on the farthest-vertex ellipse M₁² + M₂² − 2c·M₁M₂ = 4A²,
M₂ ≤ 2A requires √(4A² − (1−c²)M₁²) ≤ 2A − cM₁, which squares to
M₁ ≥ 4Ac ≥ 2A — contradiction. So for cos γ ≤ −1/2 the farthest vertex
must be mixed-sign, and r ≤ 1 by the first case. (ii)

*Attainment:* take f₁ = f₂ = f with max f = f(0) = M, ρ = |min f|/M.
All four vertices lie in D̄(0, |w₁+w₂|M) iff the cross vertex does:
M²(1 + ρ² + 2cρ) ≤ M²(2 − 2c) ⟺ ρ² + 2cρ − (1−2c) ≤ 0 ⟺ ρ ≤ 1 − 2c
(c = −cosγ ∈ (0, 1/2)); for cos γ = d ≥ 0 the condition is ρ ≤ 1 + 2d,
always true. Then 2A = |w₁+w₂|M, Σβ = 2M, r = 4M²/(2+2cosγ)M² =
2/(1+cosγ) exactly. Fejér profiles f = (K_n − 1)/n have ρ = 1/n → any
ρ-threshold is realizable with finitely many modes. The off-origin
EXACT ties are the solutions of (u₁·x, u₂·x) ≡ (0,0): exactly
|det(u₁;u₂)| − 1 of them (f attains max only at 0 for Fejér). ∎

**Sharpness/refutation probe (`experiments/vsa_two_ray_fejer_probe.py`).
REGISTERED PREDICTIONS (2026-06-10, committed pre-run; exact rationals
via cos γ = (m²−n²)/(m²+n²) for u₁=(1,0), u₂=(m,n)):**

| u₂ | cos γ | profile | predicted |
|---|---|---|---|
| (1,1) | 0 | Fejér n=6 | r = 2, feasible, 0 off-origin ties |
| (2,1) | +3/5 | Fejér n=6 | r = 5/4, feasible, 0 ties |
| (3,4) | −7/25 | Fejér n=6 | **r = 25/9 ≈ 2.778**, feasible, 3 ties |
| (2,3) | −5/13 | Fejér n=8 | **r = 13/4 = 3.25**, feasible, 2 ties |
| (5,8) | −39/89 | Fejér n=9 | **r = 89/25 = 3.56**, feasible, 7 ties |
| (1,2) | −3/5 | Fejér n=6 | INFEASIBLE, true-peak excess = 0.5347 |

The three bold values exceed the believed two-ray ceiling 2.0000; the
(1,2) row tests the infeasibility mechanism of (ii) quantitatively.

**Remark (two full LINES).** Theorem 3′ holds verbatim when each ray is
replaced by the full line {tu : t ∈ Z\{0}} (1D profiles with sine terms,
i.e. general mean-zero trig polynomials): the proof used only (a) the
value set of each profile is an interval [m_j, M_j] with m_j < 0 < M_j
(mean-zero), (b) surjectivity of x ↦ (u₁·x, u₂·x) (det ≠ 0), and (c) the
constant Beurling phase on the line — none of which needs evenness. The
objective still reads f₁(0) + f₂(0) (sines vanish at 0).

**RESULT (2026-06-10, same day, `two_ray_fejer_probe.json`):
6/6 PREDICTED→CONFIRMED.** All r values land EXACTLY (2.777778,
3.250000, 3.560000; both code paths agree to 1e-9; true-peak excess
0.0 — the predicted exact ties, counts 3/2/7 = |det U|−1 after
identifying the 0~2π seam); the (1,2) construction is infeasible with
measured excess 5.347e-1 matching the predicted (1+ρ²+2|cosγ|ρ)/(2−2c)−1
to 4 digits. Theorem 3′ is therefore PROVED with a confirmed sharpness
probe: the two-ray ceiling is the exact envelope
r*(γ) = 2/(1+cosγ) for cosγ > −1/2 (sup 4, not attained), r* ≤ 1 for
cosγ ≤ −1/2. Two corollaries for the recruitment program: (1) the
m-ray problem's "leak" already appears at m = 2 — Fejér-degenerate
profiles (ρ → 0) are the extremal shape, consistent with the witnesses'
preference for asymmetric profiles; (2) class ceilings are
DISCONTINUOUS in the ray geometry (4 vs 1 across cosγ = −1/2), so any
universal C₀ argument must not rely on continuity in ray angles.

### 3.a Proposition (anchored two lines; PROVED 2026-06-10, upper bound only)

Let Λ ⊂ L₁ ∪ L₂ ∪ E where L₁, L₂ are lines through 0 with independent
primitive directions u₁, u₂ (U = (u₁; u₂), phase angle γ ≠ π), and E is a
finite set of off-line "anchor" modes with **E ∩ UᵀZ² = ∅**, occupying
anchor directions u₃, …, u_p. Then

```
√r ≤ √(2/(1+cos γ)) + Σ_{j≥3} |f_j(0)|/(2A) ≤ √(2/(1+cos γ)) + (p − 2).
```

*Proof.* The kernel of x ↦ Ux mod 2π is a finite group K of order
|det U|; averaging 2Q over a fiber x₀ + K weights mode k by the character
sum (1/|K|)Σ_{κ∈K} e^{ik·κ}, which is 1 for k ∈ UᵀZ² and 0 otherwise.
Both lines lie in UᵀZ² (u_j = Uᵀe_j); E misses it by hypothesis. Hence
for EVERY (a, b) ∈ T² (surjectivity), |w₁f₁(a) + w₂f₂(b)| =
|avg_fiber 2Q| ≤ 2A: the full product constraint of the two-line problem
survives the anchors. The Minkowski parallelogram is in D̄(0, 2A), so the
both-max corner gives M₁² + M₂² + 2cosγ·M₁M₂ ≤ 4A², and with AM-GM
(M₁+M₂)² ≤ 8A²/(1+cos γ) — no farthest-vertex argument needed, so this
holds regardless of where Q(0) sits. Then f₁(0) + f₂(0) ≤ M₁ + M₂ and
the Ray-Mass Lemma caps each anchor direction's mass |f_j(0)| ≤ 2A. ∎

Reading: anchors couple to a two-line core ONLY through the residue
classes of UᵀZ² they occupy — off-sublattice anchors cannot damage the
two-line Minkowski geometry at all; they can only add their own (per-ray
capped) masses. The dangerous shims are the in-sublattice ones, which
deform the effective constraint surface Φ(a,b) = w₁f₁(a) + w₂f₂(b) +
Σ_{k=Uᵀι∈E} β_k w_k cos(ι·(a,b)) — a concrete, low-dimensional object
for the m-ray attack. (Sharpness of the (p−2) term is UNPROBED; the
cos γ ≤ −1/2 strengthening of Theorem 3′ does NOT transfer — it needs
the farthest-vertex equality, which anchors break.)

## 4. The m-ray subtorus problem — the sharp remaining question

For m ≥ 3 rays u₁,…,u_m, the map x ↦ (u₁·x, …, u_m·x) lands in a 2-dimensional
subtorus H ⊂ T^m (NOT all of T^m): the constraint is

```
|Σ_j w_j f_j(a_j)| ≤ 2A   only for (a₁,…,a_m) ∈ H,
```

which is strictly weaker than the product constraint used above. The whole
content of 2D kinematic VSA is:

> **m-ray subtorus problem.** Is sup r over all m, all ray sets, and all
> profiles, with the constraint imposed only on H, finite?
>
> Equivalently: how much can the Minkowski-sum argument leak when the
> combination set is a 2D subtorus instead of the full product?

The certified witnesses (r = 27.1 at N=32) live exactly in this leak: they
combine ~4+ ray directions with low-mode anchors, exploiting points of T^m
that H misses. The diagonal-probe saturation and the trace-free load lemma
say the leak is bounded for the channels tested; the m-ray problem is the
clean statement of what a full boundedness proof must control. Diophantine
structure enters precisely here (which (a_j) combinations are attainable),
vindicating the intuition — but not the proof sketch — of the May 12
"Lemma 1 (Diophantine covering)".

## 5. Relation to the program

- These are the first UNCONDITIONAL theorems about r at certified strain
  maxima in any subclass. They confirm the mean-zero mechanism is real and
  proof-grade, not just numerics.
- They bound exactly the channels that the F2 trace-free lemma says carry
  all asymptotic weight — closing the asymptotic loop modulo the
  anchor/finitely-many-low-modes interaction (the m-ray leak).
- Next theorem-shaped targets, in order: (i) two rays + finitely many
  off-ray modes (perturbed two-ray), (ii) m rays with H of finite index in
  T^m (small determinant relations), (iii) the general m-ray subtorus
  problem.

### Registered prediction — decisive N=64 v3 run (committed pre-run, 2026-06-10)

v3-grade per-doubling growth so far: √r* = 4.825 (N=8) → 6.994 (N=32),
i.e. +1.084 per doubling over two doublings (N=12/16 v3 complete).
**PREDICTION** for the N=64 v3 ascent (seed `scaling_N64.json`, budget
1200 steps / 7200 s): under continued log-type growth the endpoint
reaches √r ∈ (7.6, 8.6) — r ∈ (57.8, 74.0) — with kkt(ε=1e-5 window)
< 0.2. **Saturation signal** would be r(64) < 53 (√r < 7.28) WITH
kkt < 0.2 (a genuine wall, not a machinery stall). **Conditionality:**
if the run ends with kkt(1e-5) ≥ 0.2, the result is machinery-limited
and counts as NO VERDICT (lower bound only) — neither confirmation nor
refutation.

### Dual-certificate structure across N (2026-06-10, `vsa_dual_structure.py`, NUMERICAL)

| N | r | dual mass on twins | on far ties | top-atom radius | radius × N |
|---|---|---|---|---|---|
| 8 | 23.28 | 0 | 24.8 | 0.582 | 4.7 |
| 12 | 31.19 | 0 | 42.8 | 0.388 | 4.7 |
| 16 | 36.61 | 38.6 | 33.2 | 0.292 | 4.7 |
| 32 | 48.92 | 45.1 | 76.3 | 0.144 | 4.6 |
| 64 | 60.84 | 242.9 | 71.7 | 0.063 | 4.0 |

Two structural facts: (1) the dual price MIGRATES INWARD with N — by
N=64, 77% of the certificate's mass sits on near-origin twin atoms;
(2) the top atom's radius obeys |x*| ≈ 4.6/N — the binding competitor
sits a fixed number of wavelengths of the highest mode from the origin,
i.e. the wall is SELF-SIMILAR at scale 1/N. This is the quantitative
face of the Hessian-degeneration wall (→ issue #30: the quartic-jet
ceiling should be computed in the rescaled variable y = Nx, where the
wall geometry is N-independent). Euler identities verified at all five
endpoints; multipliers all nonnegative.
