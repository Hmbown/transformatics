# What the external Navier–Stokes formal statements assert

8 September 2026. **Bounded independent AI-agent source audit.** The two exported formal statements and their solution predicates agree with forced alternatives C and D at the inspected scope. No hidden viscosity restriction, pressure-periodicity omission, derivative-junk-value escape, or extra assumption on a competing periodic solution was found. This is a reading and static import audit, not a compilation, kernel replay, external expert review, or certification of every construction lemma.

The audited public source is [openai/NavierStokesAndEuler at commit `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538). The checkout's commit was verified locally. Comparison targets were the [paper-to-notes comparison](../navier-stokes/openai-result-bridge.md), [published-proof chapter](../../notes/chapters/published-proof.md), and the external paper's Theorem 1.1 and Corollary 10.6 as recorded there. No toolchain installation, dependency script, build, or DNS was run by this audit.

## 1. The challenge placeholders do not supply the submitted proof

The [challenge file](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/NavierStokes.lean) deliberately leaves its two reference theorems as `sorry`. Its purpose is to state the targets. Consequently, “the entire repository contains no `sorry`” is incorrect.

The [submission](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ComparatorSolution.lean) imports `ComparatorR3Theorem` and `ComparatorTheorem`. Those use the separate `ComparatorDefinitions`, which contains the definitions and helper proofs but neither challenge theorem. The following local source checks passed:

- Recursively following source `import` lines from `NavierStokes.ComparatorSolution` reaches **580 project-local Lean modules** and **209 distinct external Mathlib module imports**. No `ComparatorChallenges` module occurs in that local closure.
- After removing nested block comments and line comments, the challenge contains exactly **two** `sorry` tokens. No `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, or `implemented_by` token was found in the 580 local dependency sources. This is a lexical source check, not an axiom report from an elaborated theorem.
- The complete common definitions and helper bodies in the challenge and `ComparatorDefinitions` match after comments and whitespace are removed. Both exported theorem headers also match the reference headers under that comparison.

The [Comparator configuration](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/NavierStokes.json) names the challenge and solution modules separately, selects the two exported declarations, enables Nanoda, and permits `propext`, `Quot.sound`, and `Classical.choice`. The [README](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/README.md) describes running Comparator against that configuration. **Configuration and textual agreement are not evidence that this check has run successfully.** Mathlib, the compiler, elaboration, generated proof terms, and the actual transitive axiom set were not independently verified here.

## 2. Quantifiers and solution predicates

The namespace is `NavierStokes.Comparator`. Both exported theorems take exactly a real viscosity `nu` and `hnu : nu > 0`, then assert existence of initial data and force for which the relevant global solution predicate is impossible.

| Item | Meaning of the inspected formal source |
| --- | --- |
| Viscosity | Every positive real viscosity; neither a small-viscosity hypothesis nor an exceptional selected viscosity is assumed in the exported targets. |
| Initial data | The target existentially quantifies a smooth divergence-free datum with the appropriate decay or periodicity. Both adapter proofs explicitly choose `fun _ => 0`, so zero initial velocity is present in the witness even though it is not written into the exported theorem type. |
| Equation | Ordinary incompressible NS: time derivative plus the spatial Fréchet derivative applied to the velocity equals `nu` times the Laplacian minus the pressure gradient plus the force. All three velocity components are retained. |
| Global smoothness | Velocity, pressure, and force are jointly `ContDiffOn ℝ ∞` on the full future half-space. Smoothness is required through every finite positive time, not merely away from a proposed terminal time. Here `∞` means all finite differentiability orders, not analyticity. |
| Initial time | The comparator uses `derivWithin` on `[0,∞)` at time zero and imposes the equation there. The candidate construction uses the equation at positive preterminal times and imposes initial values separately. The contradiction only needs the positive-time equation of a hypothetical global solution. |
| Whole space C | The competing velocity must belong to `L²` at each future time and satisfy one uniform-in-time kinetic-energy bound. No compact support, periodicity, derivative bound at infinity, or growth bound on the competing pressure is added by the inspected adapter. |
| Periodic D | Initial data and force are unit-periodic in all three spatial directions. Both the competing velocity **and pressure** must be unit-periodic for every future time. No separate uniform-in-time energy assumption is added. |

These predicates are in [ComparatorDefinitions](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ComparatorDefinitions.lean). In particular, the whole-space predicate includes both `MemLp (‖v · t‖) 2` and `∃ E, ∀ t ≥ 0, ∫ ‖v x t‖² < E`. The integrability condition prevents an undefined/nonintegrable integral's default value from trivializing the energy requirement. The missing factor `1/2` in the displayed energy integral only changes the existential constant.

Fréchet derivatives have default values outside their differentiability hypotheses, but this does not provide an identified loophole here. Joint smoothness gives smooth spatial slices, and every positive time is interior to the future domain. `ComparatorBridge` proves the divergence, gradient, Laplacian, and positive-time derivative identifications; the Laplacian conversion uses an explicit twice-differentiable spatial slice. The boundary derivative uses the actual half-space convention.

## 3. Force decay includes every mixed derivative

The force conditions quantify **every natural total derivative order** and **every real decay exponent**, followed by a constant uniform in space and future time. Whole-space C uses the norm of the complete spacetime derivative tensor divided by `(1+‖x‖+t)^K`; periodic D uses `(1+t)^K`. Thus the bounds cover every mixed space/time component, including time-zero derivatives within the future domain. Constants may depend on derivative order, decay exponent, and the selected viscosity. No uniform constant across all derivative orders is asserted or required.

The proof does not assume decay from smoothness alone. [CandidateConsequences](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CandidateConsequences.lean) derives the periodic bounds from smoothness, periodicity of the full jets, compactness of a fundamental spatial cell, and compact future time support. [CompactSpatialForceDecay](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CompactSpatialForceDecay.lean) instead uses one compact spatial support set for the whole-space force. Both include derivative vanishing beyond the support.

The selected construction is stronger than the target predicate in another respect: `ActualCandidateAssembly.Witness` retains a force satisfying `ContDiff ℝ ∞` on the entire spacetime, as well as its terminal derivative identities. [CandidateFromLimits](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CandidateFromLimits.lean) glues the actual residual to a smooth extension of its boundary jets and makes the force zero from time two in the viscosity-one normalization. Those boundary jets need not vanish away from the singular spatial point. This agrees with the bridge's distinction between smooth terminal extension and zero terminal forcing everywhere.

## 4. The adapters close their candidate hypotheses

The short adapter theorems `option_C_of_compact_candidate` and `option_D_of_candidate` are conditional. The final exported proofs discharge that condition rather than passing it to the theorem user:

1. `ActualCandidateAssembly.selected_witness` specializes the finite-stage construction to fixed selected budget and threshold constants. `selected_candidate` extracts the periodic `CandidateProperties` witness.
2. `R3ActualCandidate.selected_compact_candidate` extracts the compact whole-space fields from that same selected witness through `R3CompactCandidate.of_localized_fields`.
3. The periodic proof invokes the candidate/global-solution contradiction based on periodic uniqueness. The whole-space proof invokes `R3FiniteEnergyComparison.compact_candidate_excludes_global_solution`.

The whole-space comparison retains the competitor's uniform finite energy in its call to `R3.WholeSpaceUniqueness.classical_uniqueness_on_Icc`. Compact support belongs to the constructed reference velocity, not to the competitor. The inspected uniqueness signature does not quietly impose pressure decay on the competitor. Its proof calls separate pressure-recovery and pressure-flux results; this audit inspected that interface and call, not the complete proofs of those results.

`ProblemStatement.candidateStatement` is a proposition defined by explicit field conditions, not an axiom. Its old “OPEN” comments describe the statement-only module. The later `selected_candidate` theorem supplies a proof term in a different module. Conversely, reading that final invocation alone does not independently verify the hundreds of upstream construction lemmas.

## 5. Two distinctions the evidence in these notes should preserve

**The exported type is narrower than every detail of the paper theorem.** It states nonexistence of a global admissible solution. It does not itself mention zero data, compact support, blow-up time one, or the constructed velocity's uniformly bounded preterminal energy. Zero data, support, and unbounded speed are visible in the inspected witnesses. Uniform preterminal energy of the constructed velocity is not a field of `CandidateProperties` or `R3CompactCandidate.Properties`; the explicit uniform energy condition in the comparator concerns a hypothetical whole-space competitor. The paper's preterminal energy assertion should retain its paper attribution unless a corresponding formal theorem or an additional formal derivation is identified.

**The arbitrary-viscosity adapter changes time.** Starting from a viscosity-one candidate, it uses

\[
u_\nu(t,x)=\nu u_1(\nu t,x),\qquad
p_\nu(t,x)=\nu^2p_1(\nu t,x),\qquad
f_\nu(t,x)=\nu^2f_1(\nu t,x).
\]

Every momentum term then gains the same factor `nu²`, and space is unchanged. Its candidate's terminal time is `1/nu`; the exported nonexistence statement does not specify a terminal time. This is sufficient for C and D. The paper's statement with terminal time one for each fixed viscosity is therefore not the literal normalized witness supplied by this adapter. This distinction is not a defect in the stated C/D theorem.

The current bridge already labels the upstream full-formalization assessment as **reported**, with no full local replay. Retain that wording. Neither the paper nor the inspected formal statements set the force to zero, and none closes this project's unforced ROOT.

## 6. Selected source fingerprints

The commit above pins every linked dependency. Additional byte fingerprints for the statement boundary are:

| Source | SHA-256 |
| --- | --- |
| `ComparatorChallenges/NavierStokes.lean` | `0cd193b8d5cbd0266e6e2f72e68dd5abcdcf2430ebd435dd9289737e9aa7da61` |
| `ComparatorChallenges/NavierStokes.json` | `7610ecead7b390d80ff7f4229a3ff8f18d630e046f7ad1de4f92c7e8e76845b8` |
| `NavierStokes/ComparatorDefinitions.lean` | `8d90e0f9eee14f8b01773852083a02fd58bda59d4de2abb60d1787bbc9f6ebf4` |
| `NavierStokes/ComparatorSolution.lean` | `52950d5d618a8d34c9bfbdb16641c81c276e97b6d7fd2a76c08577353f0b0227` |
| `NavierStokes/ProblemStatement.lean` | `d2f5cdf24a060acd41011b50492e89058991965e18d2cb797c58d915f95af633` |
| `NavierStokes/ComparatorTheorem.lean` | `94b2218013c242e55b8726523ca1151bc1bd5e2b55a5d6d0909cd867bf5e1f59` |
| `NavierStokes/ComparatorR3Theorem.lean` | `bcf984eb9f9b70d2f0a3850b146bccef918b36d27831f607b5c1aed14aab92a3` |
| `NavierStokes/ActualCandidateAssembly.lean` | `bba2f74a938039caec486ca6a35576efd21e6fe35c1ba695e4d21609d89b8a94` |
| `NavierStokes/R3CompactCandidate.lean` | `5831f975030543c5b670ee3b0ed116222848725df7b14892ba4d6592a47ae5f0` |

The remaining verification step is an actual elaboration/build and axiom/dependency comparison for these exported declarations, using the intended isolated toolchain. The coordinating task owns that work; this source audit does not report its outcome.
