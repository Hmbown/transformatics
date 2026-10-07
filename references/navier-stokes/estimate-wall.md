# Estimate-level wall: no new cancellation, tight blow-up condition, O″ blocked

**Standing:** ROOT remains **OPEN**. This note pins the wall at the
estimate level: the natural cancellation family is classified (nothing
new through degree two), the pointwise blow-up condition is exactly the
negation of (E′), and O″ is blocked from every pinned qualitative
input. No DNS was run.

Pins: `experiments/nse_estimate_wall.py`,
`tests/test_nse_estimate_wall.py`,
`artifacts/enstrophy_sup/nse_estimate_wall.json`;
node `nse-estimate-wall`.

## W1. Cancellation classification through degree two (PROVED)

For `P(-Δ)` of degree `≤ 2`, write `P(λ) = a + bλ + cλ²`. Then
`⟨P(-Δ)S, ω⊗ω⟩ = a·I₀ + c·I₂` since Miller's `I₁ = 0`. Two exact
witness fields (deterministic seeds 0–1, small-integer div-free
Fourier data) give `(I₀, I₂) = (-1/3, 6)` and `(-25/12, -9/2)`,
with determinant `14 ≠ 0` (exact). Hence `a·I₀ + c·I₂ ≡ 0` forces
`a = c = 0`: **Miller's `P = -Δ` spans the vanishing ideal through
degree two.** Betchov (`P = 1`) and `Δ²` do not vanish. Miller is
re-verified (`I₁ = 0` exactly) on every tried field. An independent
float-spectral dual reproduces both witnesses to 1e-6. Axial-mode
fields obey extra selection rules (all pairings vanish there); the
winners need the `(1,1,·)` modes.

## W2. Blow-up forces liminf H = 0; (E′) is its negation (PROVED)

On an infinite ladder the cap gives `ΣH̄ < ∞`, so `H̄ⱼ → 0`. Each
`H̄ⱼ` is the `M`-weighted average of `H = Q/M` over `Pⱼ`; if
`inf_{Pⱼ}H ≥ ε > 0` eventually, then `H̄ⱼ ≥ ε`, contradiction. Thus
**`inf_{Pⱼ}H → 0` along a subsequence**: blow-up requires `H`
arbitrarily small on positive sets. The blob illustrates it
exactly (`H·Q = 1`, `H → 0`). (E′) (`H ≥ h₀` for `M ≥ M₀`) implies
`H̄ⱼ ≥ h₀` on high rungs (there `M ≥ √(qⱼ/V) ≥ M₀`; pinned
threshold `j* = 25` for the reference numbers), i.e. exactly the
negation of the necessary condition: **(E′) is tight** — it cannot
be weakened in this direction.

## W3. O″ witnesses: V_b and tier-2 (PROVED)

- **V_b**: from the pinned scalings, `H·Q = A_Q²/A_M =: c₀ > 0`
  exactly. Any `φ` with `φ(Q) ≤ H = c₀/Q` eventually has
  `∫φ(eˢ)ds ≤ c₀∫e^{-s}ds < ∞`. So **V_b violates every
  divergent-φ O″** while matching E/Q/D balances, Betchov, and
  Miller. Balances + abstract identities do not imply O″.
- **Tier-2** (cross-receipt): ESS diverges and the full battery is
  green while prices stay geometric (summable). By the T2
  short-circuit (O″ ⟹ `ΣH̄ = ∞`), tier-2 violates O″. So
  **ESS + the whole standard battery do not imply O″**.

Consequence: O″ needs a genuinely new quantitative PDE estimate;
none is in hand, and no weaker sufficient condition is known. The
witness table above is the precise obstruction record.
