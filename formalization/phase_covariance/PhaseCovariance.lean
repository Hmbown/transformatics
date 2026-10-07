import NavierStokes.PartitionedCovariance

/-!
# Slotwise phase freedom in the leading covariance

Dependency: OpenAI/NavierStokesAndEuler commit
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538.

This is a corollary of the imported, actual periodized covariance theorem.
It does not concern the full curl-corrected field or a differential equation.
No smoothness, derivative bound, or dynamics is inferred for the new phases.
-/

noncomputable section

namespace Transformatics.PhaseCovariance

open NavierStokes NavierStokes.PartitionedCovariance

/-- Change only the angular phase in each of the two signed slots. -/
def phaseShiftedPair {D h : ℝ} {vr vt : Plane}
    {sys : SlotSystem D h vr vt} {U : UnsignedLabel}
    (P : PairData sys U) (γ : Fin 2 → Plane → ℝ) : PairData sys U :=
  { P with phases := fun j Y => P.phases j Y + γ j Y }

/-- The actual native pulse integrals do not depend on angular phase. -/
@[simp] theorem phaseShiftedPair_matrix {D h : ℝ} {vr vt : Plane}
    {sys : SlotSystem D h vr vt} {U : UnsignedLabel}
    (P : PairData sys U) (γ : Fin 2 → Plane → ℝ) :
    (phaseShiftedPair P γ).matrix = P.matrix := by
  rfl

/-- Every hypothesis of the imported covariance theorem is retained.

Only the phase field changes. The output is the same two leading
radial–tangential covariance components, indexed by i : Fin 2.
-/
theorem physical_primary_covariance_phase_shift
    {D h : ℝ} {vr vt : Plane} (sys : SlotSystem D h vr vt)
    (hdet : vr.1 * vt.2 - vr.2 * vt.1 ≠ 0) (N : ℕ) (hN : 1 ≤ N)
    (P : (U : UnsignedLabel) → PairData sys (tailLabel N U))
    (γ : UnsignedLabel → Fin 2 → Plane → ℝ)
    {q : ℝ} (hq : 0 < q) (hqN : q ≤ ChartScales.Q N)
    (x : SlotColoring.Position) (T0 : Vec2)
    (hcone : ∀ U, mask D (tailLabel N U) q x ≠ 0 →
      SmoothCovariance.StrictCone (P U).matrix (chartTarget h q N T0 U))
    (i : Fin 2) :
    doubleAverage (fun Y θ =>
      assembledRadial (fun U => phaseShiftedPair (P U) (γ U)) hdet
        (physicalOuter h N) (physicalViscosity h N)
        (chartTarget h q N T0) q x Y θ *
      assembledTangent (fun U => phaseShiftedPair (P U) (γ U)) hdet
        (physicalOuter h N) (physicalViscosity h N)
        (chartTarget h q N T0) q x i Y θ) =
      q ^ (-velocityExponent h - 1 / 2) * T0 i := by
  apply physical_primary_covariance sys hdet N hN
    (fun U => phaseShiftedPair (P U) (γ U)) hq hqN x T0
  intro U hU
  simpa only [phaseShiftedPair_matrix] using hcone U hU

end Transformatics.PhaseCovariance

#print axioms Transformatics.PhaseCovariance.physical_primary_covariance_phase_shift
