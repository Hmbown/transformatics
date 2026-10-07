# Route classification: no reductions, one tautology, three reach targets

**Standing:** ROOT remains **OPEN**. This note classifies every live
route: one is vacuous (already dead), one is tautological (proved here),
three are sufficient strengthenings (possibly stronger than ROOT), one
is partial and independent. No DNS was run.

Pins: `experiments/nse_route_classification.py`,
`tests/test_nse_route_classification.py`,
`artifacts/enstrophy_sup/nse_route_classification.json`;
node `nse-route-classification`.

## T1. Transfer supK is equivalent to continuation (PROVED)

For nontrivial solutions (`Q, D > 0`), with
`R = ‖C‖²/(2νD) − 2νD/Q` and `K(t) = ∫R`:

- (⟹) is the transfer memo §4: `D′/D ≤ R` gives `log(D/D₀) ≤ K`, so
  `sup K < ∞` bounds `D`, hence `Q` (periodic Poincaré, mean-zero `S`),
  hence continuation by the standard H¹ criterion.
- (⟸) is new: if the solution continues past `T`, then `R` is
  continuous on `[t₀, T]`, so `K` is bounded there. Continuity needs
  `D, Q ≠ 0`: on the torus `D = 0 ⟺ S ≡ const ⟺ S ≡ 0 ⟺ Q = 0`
  (a nonzero linear field is unbounded, hence non-periodic; the
  experiment pins this core), and `Q = 0 ⟺ u ≡ 0` (mean-zero), i.e.
  the trivial solution, for which continuation is moot.

Therefore `sup K < ∞ ⟺ continuation`. The transfer criterion is a
valid tautological-class reformulation, **not a reduction**: proving
its hypothesis is exactly as hard as proving continuation. The
transfer-budget node keeps its PROVED lemmas with this clarifying
banner; nothing there is refuted.

## T2. O″/(E′)/codimension imply ROOT directly (PROVED)

O″ (`Q ≥ φ(Q)M` for `M ≥ M₀`, `φ` nonincreasing,
`∫φ(eˢ)ds = ∞`) short-circuits the cap with no vacuous step. Suppose
an infinite first-passage ladder. High rungs lie in `M ≥ M₀` (since
`M ≥ √(Q/V) → ∞`), where `H = Q/M ≥ φ(Q) ≥ φ(ρqⱼ)`. Hence
`H̄ⱼ ≥ φ(ρqⱼ)` and `ΣH̄ⱼ ≥ Σφ(ρqⱼ) = ∞` by the integral test
(`logρ·φ(qⱼ₊₁) ≤ ∫φ`, pinned for `φ = 1/log` with its logarithmic
divergence mechanism) -- contradicting the cap. Finite ladder,
bounded `Q`, regular. (E′) is the case `φ ≡ h₀`; the codimension
floor `H_θ ≥ h₀` gives `Q ≥ θ²M²V_θ ≥ θ²h₀M`, i.e. (E′). So
codimension ⟹ (E′) ⟹ ROOT and O″ ⟹ ROOT, directly.

These are **reach strengthenings**: satisfiable (vacuous on regular
solutions; unrefuted for NS) and sufficient, but possibly strictly
stronger than ROOT -- the converse would require ruling out
infinite-time concentration, itself open. Ranked first among live
targets because they are the cleanest statements, not because they
are easy: each is ROOT-hard.

## T3. Strength table

| route | class | note |
|---|---|---|
| Q-GSO/M-GSO noncollapse | VACUOUS | dead (cap-vacuity) |
| Transfer supK | TAUTOLOGICAL | ⟺ continuation (T1) |
| (E′)/O″/codimension | REACH | ⟹ ROOT (T2); maybe stronger |
| L-eta-m compact | PARTIAL | independent; spread stays open |

There is no reduction of ROOT to a strictly easier statement
anywhere in the program. The honest map above is the deliverable;
the next mathematical move is an assault on a reach target or on
L-eta-m, each a major undertaking.
