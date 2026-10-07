# GSO vacuity: the averaged-noncollapse hypotheses are refuted

**Standing:** ROOT remains **OPEN**. What dies here is the Q-GSO/M-GSO
*regularity route*: its averaged-noncollapse hypotheses are unsatisfiable,
refuted by the memo's own corollaries (3)/(5). The conditional
implications are valid but vacuous. No DNS was run.

Pins: `experiments/nse_qgso_cap_vacuity.py`,
`tests/test_nse_qgso_cap_vacuity.py`,
`artifacts/enstrophy_sup/nse_qgso_cap_vacuity.json`;
node `nse-qgso-cap-vacuity`; supersession `gso-averaged-noncollapse`.

## 1. The refutation (PROVED)

Fix `ρ > 1`, `q_0 > Q(0)`, first-passage rungs `[a_j, b_j]` (pairwise
disjoint interiors), `P_j = {Q' > 0}`, `A_j = ∫_{P_j} Q`,
`B_j = ∫_{P_j} M`, `H̄_j = A_j/B_j`. Three unconditional inputs:

- (i) `B_j ≥ logρ/c_B`: positive log-variation `≥ logρ` (last-to-first)
  plus pointwise Betchov `Q' ≤ c_B·M·Q`.
- (ii) `H̄_j ≤ A_j·c_B/logρ`: divide by the floor in (i).
- (iii) `Σ_j A_j ≤ E_0/(2ν)`: disjointness plus the energy identity.

Summing (ii) over **any** completed family, finite or infinite:

```text
Σ_j H̄_j ≤ (c_B/logρ)·Σ_j A_j ≤ (c_B/logρ)·(E_0/2ν) < ∞.   (cap)
```

This is memo-(3), but its derivation uses **no singularity assumption**:
it holds for every finite-energy trajectory. Hence the Q-GSO hypothesis
`Σ_j H̄_j = ∞` is unsatisfiable -- REFUTED, not open. Escape (summable,
decaying prices, `H̄_j → 0`) is MANDATORY on infinite ladders.

The hypothesis as stated ("if infinitely many rungs complete, `Σ = ∞`")
is therefore equivalent to "finitely many rungs complete", i.e. to `Q`
bounded -- which is the theorem's conclusion. The Q-GSO conditional
implication is valid but a tautology given the cap. It can never
discharge regularity.

The M-GSO hypothesis dies identically: `V_j⁺ ≥ 2log r` gives
`H̄_j/C_eff,j = ∫_{P_j}Q/V_j⁺ ≤ ∫_{P_j}Q/(2log r)`, so
`Σ_j H̄_j/C_eff,j ≤ E_0/(4νlog r) < ∞` on disjoint M-rungs, refuting
(M-GSO-eff); the ess-sup variant is smaller termwise, also refuted. The
oversight mechanism: (3)/(5) were framed as "singularity contrapositives"
(necessary blow-up phenomenology), obscuring that they hold
unconditionally and hence kill the hypotheses.

## 2. What survives

- **Proved GSO lemmas** (Betchov cap, rung-cost bounds, (3)/(5) as
  *necessary* blow-up conditions: singular ladders must have decaying
  prices). Preserved, not deleted.
- **(E′), O″, energy-codimension pointwise floors**: satisfiable
  (vacuous on regular solutions; unrefuted for NS), each implying ROOT
  (via BKM, or directly by contradicting the cap on infinite ladders).
  Non-vacuous targets. Note (E′) may be strictly stronger than ROOT
  (it also constrains infinite-time growth).
- **Transfer-budget signed criterion**: no cap in sight (`C`, `Z`
  unbudgeted); satisfiable in principle; genuinely OPEN.
- **L-eta-m compact branch**: independent of GSO prices; OPEN (partial:
  spread escapes remain even if it closes).
- **Campaign/ledger data**: valid NS measurements, reframed as blow-up
  phenomenology. All 14 trajectories sit deep inside both caps
  (Q-sums `0.018--0.106` vs cap `2.4394`; M-sums `≤ 0.38` vs `1`).
  Survival/escape verdicts are moot: finite ladders cannot witness the
  (impossible) divergence.

## 3. Dead targets (do not pursue)

Averaged noncollapse in any rung-average form; `B_j`/`K_j` prefix caps
with `α ≤ 1` (they imply the refuted divergence); lower-envelope price
floors with divergent sums (all contradict the cap); sub-clock
shortcuts (already disproved). The `V_b` kinematic path (summable
prices, bounded L³) is consistent with the cap, as it must be.
