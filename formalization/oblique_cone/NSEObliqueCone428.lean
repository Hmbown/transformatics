import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring.Basic

/-!
Original Transformatics cone algebra, 2026-09-08.
Two-dimensional matrices are represented by their coordinate actions,
so checking this file needs only the already cached algebra/tactic modules.
Analytic Gavrilov coefficient convergence and ODE/PDE existence are not
asserted or imported. Each bounded real coefficient is explicitly assumed.
-/

noncomputable section

namespace Transformatics.ObliqueCone

abbrev Vec2 := ℝ × ℝ

def B0 (v : Vec2) : Vec2 := (-(8 / 9 : ℝ) * v.2, -(1 / 2 : ℝ) * v.1)
def S (v : Vec2) : Vec2 := ((4 / 3 : ℝ) * v.1, v.2)
def Sinv (v : Vec2) : Vec2 := ((3 / 4 : ℝ) * v.1, v.2)
def C (v : Vec2) : Vec2 := (-(2 / 3 : ℝ) * v.2, -(2 / 3 : ℝ) * v.1)
def Q (v : Vec2) : Vec2 := (v.1 + v.2, -v.1 + v.2)
def Qinv (v : Vec2) : Vec2 := ((v.1 - v.2) / 2, (v.1 + v.2) / 2)
def D (v : Vec2) : Vec2 := ((2 / 3 : ℝ) * v.1, -(2 / 3 : ℝ) * v.2)

theorem symmetrizing_identity (v : Vec2) : B0 (S v) = S (C v) := by
  apply Prod.ext <;> dsimp [B0, S, C] <;> nlinarith

theorem diagonalizing_identity (v : Vec2) : C (Q v) = Q (D v) := by
  apply Prod.ext <;> dsimp [C, Q, D] <;> nlinarith

theorem full_conjugacy (v : Vec2) : B0 (S (Q v)) = S (Q (D v)) := by
  rw [symmetrizing_identity, diagonalizing_identity]

theorem basis_left_inverse (v : Vec2) : Qinv (Sinv (S (Q v))) = v := by
  apply Prod.ext <;> dsimp [Qinv, Sinv, S, Q] <;> nlinarith

theorem basis_right_inverse (v : Vec2) : S (Q (Qinv (Sinv v))) = v := by
  apply Prod.ext <;> dsimp [Qinv, Sinv, S, Q] <;> nlinarith

def slopeRhs (r11 r12 r21 r22 z : ℝ) : ℝ :=
  r21 + (-(4 / 3 : ℝ) + r22 - r11) * z - r12 * z ^ 2

theorem cone_face_margins (r11 r12 r21 r22 : ℝ)
    (h11 : |r11| ≤ 1 / 12) (h12 : |r12| ≤ 1 / 12)
    (h21 : |r21| ≤ 1 / 12) (h22 : |r22| ≤ 1 / 12) :
    slopeRhs r11 r12 r21 r22 (1 / 2) ≤ -(23 / 48 : ℝ) ∧
    (23 / 48 : ℝ) ≤ slopeRhs r11 r12 r21 r22 (-(1 / 2 : ℝ)) := by
  rcases abs_le.mp h11 with ⟨h11l, h11u⟩
  rcases abs_le.mp h12 with ⟨h12l, h12u⟩
  rcases abs_le.mp h21 with ⟨h21l, h21u⟩
  rcases abs_le.mp h22 with ⟨h22l, h22u⟩
  constructor <;> dsimp [slopeRhs] <;> nlinarith

theorem expanding_coefficient (r11 r12 z : ℝ)
    (h11 : |r11| ≤ 1 / 12) (h12 : |r12| ≤ 1 / 12)
    (hz : |z| ≤ 1 / 2) :
    (13 / 24 : ℝ) ≤ 2 / 3 + r11 + r12 * z := by
  have hprod : |r12 * z| ≤ (1 / 24 : ℝ) := by
    calc
      |r12 * z| = |r12| * |z| := abs_mul r12 z
      _ ≤ (1 / 12 : ℝ) * (1 / 2 : ℝ) :=
        mul_le_mul h12 hz (abs_nonneg z) (by norm_num)
      _ = 1 / 24 := by norm_num
  have h11l := (abs_le.mp h11).1
  have hprodl := (abs_le.mp hprod).1
  linarith

theorem expanding_component (r11 r12 z xp : ℝ)
    (h11 : |r11| ≤ 1 / 12) (h12 : |r12| ≤ 1 / 12)
    (hz : |z| ≤ 1 / 2) (hxp : 0 ≤ xp) :
    (13 / 24 : ℝ) * xp ≤ (2 / 3 + r11 + r12 * z) * xp :=
  mul_le_mul_of_nonneg_right (expanding_coefficient r11 r12 z h11 h12 hz) hxp

end Transformatics.ObliqueCone

#print axioms Transformatics.ObliqueCone.full_conjugacy
#print axioms Transformatics.ObliqueCone.basis_left_inverse
#print axioms Transformatics.ObliqueCone.basis_right_inverse
#print axioms Transformatics.ObliqueCone.cone_face_margins
#print axioms Transformatics.ObliqueCone.expanding_component
