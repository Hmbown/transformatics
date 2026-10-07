# Adversarial Audit of the "RIGOROUS" Chain Steps — 2026-06-09

**Status:** COMPLETE — three load-bearing labels do not survive scrutiny
**Method:** independent adversarial review (Opus agent) of Gap 1, the Required
Lemma, and the Lean formalization, prompted by the 2026-06-09 retraction of
the cutting-plane kinematic-VSA refutation (same failure pattern: a favorable
number measured on specific data, promoted to a theorem).

---

## Verdicts

### A. Gap 1 (⟨θ⟩_w ≤ κ = 1/55 < 1/54) — **NOT RIGOROUS, downgraded to OPEN**

What is actually proved: only the algebraic identity
⟨θ⟩_w = 1/54 − ⟨Δ⟩/(27⟨|S|⁶⟩). The step producing a *number* < 1/54 fails
three ways:

1. **Non-universal constant.** The proposed "explicit κ" depends on
   the solution's own `max_t⟨|S|⁶⟩` — exactly the quantity that is unbounded
   at a putative blowup, where this κ degenerates to 1/54 (no gap). The
   fallback sets κ from the Kida N=64 dataset: an empirical fit, not a
   theorem.
2. **The c₁ > 2/3 repulsion engine is dead by the repo's own audit.**
   The earlier calculation records: at the canonical
   3-mode configuration c₁ = 0.237 ≪ 2/3, margin −0.526, "Pointwise Riccati
   is DEAD"; and the sign of dΔ/dt near axisymmetry is solution-dependent
   (Kida grows, TG decays), contradicting the assumed universal inequality.
3. **Assumed step:** `dΔ/dt ≥ C₀·|S|⁶·m` on the near-axisymmetric set is
   asserted, not proved.

### B. CZ step (Lemma 2A, also contaminates Gap 2a) — **INVALID AS STATED**

`‖P‖_{L^∞} ≤ C_P·‖g‖_{L^∞}` is "proved" via `‖∇²p‖_∞ ≤ C·‖f‖_BMO` with
"BMO ⊃ L^∞". The inclusion is used backwards: second Riesz transforms map
L^∞ → BMO, **not** L^∞ → L^∞; there is a genuine logarithmic loss. The earlier argument acknowledged this barrier elsewhere while Lemma 2A used the false version. The bound
`|dΔ_P| ≤ C·g^{7/2}` in Gap 2a inherits the same flaw.

### C. Lean formalization — **PLACEHOLDERS, NOT MACHINE-CHECKED**

- The historical alignment and repulsion drafts were outside the Lean build,
  with no compiled artifacts. The alignment draft referenced undefined
  identifiers (`T³`, `IsStrainMaximum`, …) and could not typecheck.
- Every load-bearing implication is vacuous: `axiom load_bearing_estimate : True`,
  `axiom vsa_conjecture : True`, `theorem ns_regularity_conditional_on_VSA
  (h : True) : True := trivial`, etc. Across the historical proof drafts there were approximately 291
  placeholder lines and essentially every file ended in `sorry`.
- Genuinely machine-checkable content: the exact commutator algebra
  (`commutator_decomposition_exact`, diagonal-entry formula) — true but
  undisputed identities, none of the inequalities.

Claims of "Lean formalized" / "machine-checked" for the chain are therefore
**false** and corrected in the status doc.

### D. Required Lemma — reduction sound, constants not uniform

The decomposition `[S,P] = −[S,Ω²] − [S,D_tS] + ν[S,ΔS]` and the reduction of
the Required Lemma to VSA are correct. But the auxiliary bounds import
`‖∇u‖_{L^∞} ≤ C·g^{1/2}` "by Sobolev embedding" — circular against the
regularity goal (this is the README's conceded non-uniform
compactness/continuity step) — and the eigenframe-rotation bound degrades at
eigenvalue collisions (δ → 0), precisely the regime Gap 1 concerns.

---

## Corrected chain status

| Component | Old label | Corrected label |
|---|---|---|
| Algebraic identities (commutator, Δ, ∇_SΔ) | RIGOROUS | RIGOROUS (sympy + genuinely checkable algebra) |
| Gap 1 (κ = 1/55 < 1/54) | RIGOROUS | **OPEN** (empirical constant; dead repulsion engine; assumed inequality) |
| Lemma 2A / Gap 2a CZ bound | PROVED | **INVALID** (L^∞→L^∞ misuse of CZ; log loss) |
| Required Lemma | PROVED conditional on VSA | reduction-to-VSA sound; **auxiliary constants circular** (assume ‖∇u‖_∞ control) |
| Lean formalization | machine-checked | **placeholders, out of build** |
| VSA Conjecture | OPEN | OPEN |
| NS regularity | conditional on VSA | **conditional on VSA + Gap 1 + de-circularized Required Lemma constants + repaired CZ steps** |

The honest summary: the program contributes a clean reduction *architecture*
and a sharp open conjecture, but the chain is conditional on **more than one**
open estimate, and nothing inequality-shaped is machine-checked.
