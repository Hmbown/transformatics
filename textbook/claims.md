# Claim register

Generated from [claims.json](claims.json); edit that source and run `python scripts/build_textbook.py --update-claim-index`. The linked source records state the scope of each result.

AI review is a process record, not external expert acceptance or proof certification.

Each entry states the strongest evidence recorded — a written proof, an AI-assisted review, a symbolic or Lean check, or an imported theorem — and what is missing, such as external expert acceptance.

<a id="ROOT"></a>
## Global regularity for three-dimensional periodic NS

**Evidence record — Open — no proof of the full target recorded.**

All smooth real mean-zero solenoidal data on the fixed three-torus, fixed positive viscosity, zero forcing.

**Boundary.** No global regularity or finite-time blow-up theorem is established.

- **Provenance:** Local formulation of the classical unforced periodic regularity problem.
- **Proof status:** Open: no proof of the full target is recorded.
- **Review:** not recorded
- **Formalization:** No ROOT proof. The local Lean check covers only the separate conditional cone-algebra claim.

**Sources:** [docs/STATUS.md](../docs/STATUS.md)

<a id="FORCED-D"></a>
## Breakdown with a smooth periodic force

**Evidence record — Imported external written proof; local Lean target build passed; full imported-closure replay incomplete; Comparator not run.**

OpenAI’s published Theorem 1.1 and Corollary 10.6 establish the forced alternatives C and D for every fixed positive viscosity, with initially resting fluid and a force smooth through terminal time. The periodic case includes periodic pressure.

**Boundary.** Externally authored result. The exact exported NS target built locally, but this does not identify every paper assertion with its formal theorem type, verify the companion Euler library, or establish external expert acceptance. Independent Comparator/Nanoda not run. The result does not imply unforced ROOT.

- **Provenance:** Imported: OpenAI, Finite time blowup for Navier–Stokes, Theorem 1.1 and Corollary 10.6; this project did not produce the construction.
- **Proof status:** External published written proof of forced breakdown, including periodic alternative D; unforced ROOT is a different target.
- **Review:** Bounded AI-agent source audit found matching reference/solution definitions and theorem headers, and no identified statement defect. The 580-module local solution import closure excludes the challenge placeholders. Complete proof audit and external expert acceptance are not recorded.
- **Formalization:** Native Lean 4.34.0-rc2 build PASS at pinned commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538: all 580 project-local dependency modules compiled from unchanged sources using matching cached Mathlib artifacts. Both exported targets printed only propext, Classical.choice, Quot.sound. Challenge placeholders are excluded from the solution import closure. The stronger bundled-kernel imported-closure replay remains incomplete: an earlier attempt hit its 600-second limit, and a later attempt was stopped after 1485.74 seconds under severe host memory and swap pressure (exit 143, empty buffered log). Neither outcome is a proof rejection or a passing check. Independent Comparator/Nanoda not run.

**Sources:** [references/navier-stokes/openai-result-bridge.md](../references/navier-stokes/openai-result-bridge.md) · [references/navier-stokes/two-track-program.md](../references/navier-stokes/two-track-program.md) · [references/navier-stokes/forced-admissibility.md](../references/navier-stokes/forced-admissibility.md) · [references/navier-stokes/forced-viscosity.md](../references/navier-stokes/forced-viscosity.md) · [references/analysis/fixed-annulus-obstruction.md](../references/analysis/fixed-annulus-obstruction.md) · [references/analysis/viscous-stage-attempt.md](../references/analysis/viscous-stage-attempt.md) · [references/analysis/force-gain-audit.md](../references/analysis/force-gain-audit.md) · [references/analysis/external-statement-audit.md](../references/analysis/external-statement-audit.md) · [formalization/external_ns/README.md](../formalization/external_ns/README.md) · [formalization/external_ns/receipt.json](../formalization/external_ns/receipt.json)

<a id="phase-covariance-replacement"></a>
## Phase freedom in the leading covariance

**Evidence record — Local Lean module compiled and module-only kernel replay passed; separate AI-agent review recorded; external expert acceptance not recorded.**

A local corollary of the external actual periodized primary-covariance theorem: independently shifting the common radial and tangential phase within each signed slot preserves both leading radial-tangential covariance components, under every original geometric, partition, cone and scale hypothesis.

**Boundary.** No claim about all entries of the covariance tensor, the full curl-corrected velocity, arbitrary phase regularity, a material-derivative bound, an actual replacement in the complete iteration, or a new NS singularity. No priority claim for phase invariance.

- **Provenance:** Local teaching corollary derived directly from OpenAI/NavierStokesAndEuler physical_primary_covariance at pinned commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538. The pulse construction and analytic input are upstream work.
- **Proof status:** Restricted exact covariance corollary proved in Lean and explained in the extraction note.
- **Review:** Separate AI-agent review of the downstream phase-transport limitation; root source and scope review. No external expert acceptance claimed.
- **Formalization:** Lean 4.34.0-rc2 compilation and bundled module-only leanchecker replay both exited zero. Reported axioms: propext, Classical.choice, Quot.sound. The local receipt does not claim fresh replay of imported proofs or an independently implemented verifier.

**Sources:** [references/analysis/external-component-extraction.md](../references/analysis/external-component-extraction.md) · [formalization/phase_covariance/PhaseCovariance.lean](../formalization/phase_covariance/PhaseCovariance.lean) · [formalization/phase_covariance/README.md](../formalization/phase_covariance/README.md) · [formalization/phase_covariance/receipt.json](../formalization/phase_covariance/receipt.json)

<a id="E-prime"></a>
## The E-prime sufficient target

**Evidence record — Open — the sufficient hypothesis is unproved.**

The pointwise sufficient target retains the exact formulation and hypotheses of the source; it is not the retired rung-average hypothesis.

**Boundary.** No proof of this target or strictly easier reduction of ROOT is supplied.

- **Provenance:** Local sufficient-condition program for the classical unforced problem.
- **Proof status:** Open hypothesis; its conditional implication to ROOT does not establish the hypothesis.
- **Review:** not recorded
- **Formalization:** No proof of E-prime is recorded; the separate local cone-algebra certificate does not cover it.

**Sources:** [references/navier-stokes/route-classification.md](../references/navier-stokes/route-classification.md)

<a id="nse-growth-set-osgood"></a>
## Averaged-noncollapse regularity route

**Evidence record — Retired route — the required hypothesis conflicts with the finite energy cap.**

The attempted Q-GSO/M-GSO noncollapse route is retired by the unconditional finite-energy cap. Historical conditional implications retain their logical scope.

**Boundary.** Do not reinterpret historical OPEN labels as current targets.

**Prior inputs:** [nse-qgso-cap-vacuity](#nse-qgso-cap-vacuity).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Retired regularity route: the written conditional implications remain valid, but the required divergent averaged-price hypothesis conflicts with the finite energy cap.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/qgso-cap-vacuity.md](../references/navier-stokes/qgso-cap-vacuity.md)

<a id="nse-qgso-cap-vacuity"></a>
## The unconditional cap correction

**Evidence record — Written proof supplied; review not documented.**

Restricted corrective result: disjointness, the Betchov inequality and energy bound already cap the proposed sums.

**Boundary.** This refutes the research route, not global regularity.

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written corrective proof from the energy identity, disjoint rung intervals, and the Betchov growth bound.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/qgso-cap-vacuity.md](../references/navier-stokes/qgso-cap-vacuity.md)

<a id="nse-frequency-activation-local"></a>
## Sparse local activation

**Evidence record — Written proof supplied; review not documented; supporting exact algebra checks recorded.**

The finite-band real solenoidal datum and small perturbations in the source generate the stated mode on 0<t≤1/(512AN), for A≥νN, with an all-mode remainder bound.

**Boundary.** No critical-norm growth, infinite cascade, or global theorem.

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written local theorem from the full projected equation and a convergent majorant; finite exact algebra checks are supporting controls.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/frequency-activation.md](../references/navier-stokes/frequency-activation.md) · [experiments/nse_frequency_activation.py](../experiments/nse_frequency_activation.py) · [tests/test_nse_frequency_activation.py](../tests/test_nse_frequency_activation.py) · [artifacts/enstrophy_sup/nse_frequency_activation.json](../artifacts/enstrophy_sup/nse_frequency_activation.json)

<a id="nse-concentrated-packet-local"></a>
## Concentrated packet and local exclusion

**Evidence record — Written proof supplied; separate model review recorded (reviewer identity not documented); external expert acceptance not recorded.**

Explicit order-L³-mode packet, persistent background strain, relative energy for arbitrary high seeds, and prescribed short-time distant-activation exclusion under stated seed/separation hypotheses.

**Boundary.** No smoothness theorem for arbitrary L² seeds or exclusion at later times.

**Prior inputs:** [nse-frequency-activation-local](#nse-frequency-activation-local).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written local theorem using classical expansions and relative energy.
- **Review:** Separate model review of formulas, weak-solution scope, and accumulated gain recorded; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/concentrated-packet.md](../references/navier-stokes/concentrated-packet.md) · [experiments/nse_concentrated_packet.py](../experiments/nse_concentrated_packet.py) · [tests/test_nse_concentrated_packet.py](../tests/test_nse_concentrated_packet.py) · [artifacts/enstrophy_sup/nse_concentrated_packet.json](../artifacts/enstrophy_sup/nse_concentrated_packet.json)

<a id="nse-steady-background-local"></a>
## Steady Euler reference and NS comparison

**Evidence record — Written proof supplied; mathematical review recorded (reviewer type not documented); external expert acceptance not recorded.**

For one fixed compact steady Euler profile, a classical strong-norm NS comparison closes over a logarithmic small-viscosity interval. The specified pressure-normal periodic carrier has two unit polarization multipliers.

**Boundary.** This comparison theorem alone does not establish high-seed amplification; no uniformity over varying reference profiles.

**Prior inputs:** [external-compact-euler](#external-compact-euler), [external-angle-action](#external-angle-action).

- **Provenance:** Local classical comparison using imported compact steady Euler geometry.
- **Proof status:** Written small-viscosity comparison and restricted carrier-ODE obstruction.
- **Review:** Mathematical review recorded; reviewer type and external expert acceptance: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/steady-background.md](../references/navier-stokes/steady-background.md) · [experiments/nse_steady_background.py](../experiments/nse_steady_background.py) · [tests/test_nse_steady_background.py](../tests/test_nse_steady_background.py) · [artifacts/enstrophy_sup/nse_steady_background.json](../artifacts/enstrophy_sup/nse_steady_background.json)

<a id="external-compact-euler"></a>
## Compact steady Euler profile existence

**Evidence record — Imported published theorem (Gavrilov; Constantin–La–Vicol); used as an input.**

The source invokes Gavrilov and Constantin–La–Vicol for compact smooth stationary Euler profiles.

**Boundary.** An Euler profile is not a stationary unforced positive-viscosity NS solution.

- **Provenance:** Imported: Gavrilov; alternative construction by Constantin–La–Vicol.
- **Proof status:** Published compact stationary Euler existence theorems, used as inputs; they are not stationary unforced Navier–Stokes theorems.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/steady-background.md](../references/navier-stokes/steady-background.md)

<a id="external-angle-action"></a>
## Particle angle-action coordinates

**Evidence record — Imported published theorem (Baldi); used within its stated coordinate region.**

The fixed compact annulus uses Baldi’s particle-coordinate result as identified in the source.

**Boundary.** Particle coordinates alone do not establish polarization instability.

- **Provenance:** Imported: Baldi, periodic angle-action description of the selected Gavrilov flow.
- **Proof status:** Published geometric theorem used within its stated coordinate region.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/steady-background.md](../references/navier-stokes/steady-background.md)

<a id="nse-gavrilov-oblique-instability"></a>
## Expanding oblique principal polarization

**Evidence record — Written proof supplied; two mathematical reviews recorded (reviewer type not documented); separate cone-algebra Lean module checked.**

For the specified compact Gavrilov profiles, pressure cutoffs and rational action tori, all sufficiently large j admit a returning oblique covector with a real expanding inviscid principal polarization Floquet multiplier. Relative multipliers tend to exp(±4π/3); the source proves an eventual lower bound exp(13π/12).

**Boundary.** Existential threshold only; no computed j0. This principal-ODE theorem alone does not establish finite-wavelength viscous NS seed amplification, profile-family-uniform NS comparison, or an infinite cascade.

**Prior inputs:** [nse-steady-background-local](#nse-steady-background-local), [external-angle-action](#external-angle-action), [external-compact-euler](#external-compact-euler).

- **Provenance:** Local principal-polarization calculation using imported Gavrilov geometry.
- **Proof status:** Written inviscid ODE instability proof on the selected fixed profiles; the profile threshold is existential.
- **Review:** Two mathematical reviews recorded for the thin jet, cutoff, return, and lift; reviewer type and external expert acceptance: not recorded.
- **Formalization:** Partial local Lean coverage of the separate cone algebra only; geometric convergence, ODE cone invariance, monodromy, and the PDE application are not covered.

**Sources:** [references/navier-stokes/gavrilov-oblique.md](../references/navier-stokes/gavrilov-oblique.md) · [experiments/nse_gavrilov_oblique.py](../experiments/nse_gavrilov_oblique.py) · [tests/test_nse_gavrilov_oblique.py](../tests/test_nse_gavrilov_oblique.py) · [artifacts/enstrophy_sup/nse_gavrilov_oblique.json](../artifacts/enstrophy_sup/nse_gavrilov_oblique.json)

<a id="high-seed-realization"></a>
## Inherited seeds and scale-uniform iteration

**Evidence record — Open — full realization and iteration obligation unclosed.**

Finite nonlinear handover with both seeds supplied at original time zero, and a late-seed outgoing-wave linearized gain, are established separately. Generating or inheriting the next seed from the resulting state, a subsequent nonlinear stage, uniform interstage errors, and one smooth datum for infinitely many stages remain open.

**Boundary.** No claimed chain of proved dependencies reaches ROOT.

- **Provenance:** Local research obligation in the unforced program.
- **Proof status:** Open full realization/iteration obligation; the later finite varying-data results do not close it.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/research-strategy.md](../references/navier-stokes/research-strategy.md)

<a id="oblique-cone-algebra"></a>
## Conditional cone algebra in Lean

**Evidence record — Local Lean module compiled and declaration replay passed; hypotheses supplied, not proved; full imported-closure replay not completed.**

Original basis inverse and conjugacy, inward slope margins ±23/48 assuming coefficient errors ≤1/12, and conditional expansion coefficient ≥13/24. Lean 4.28.0 compilation and bundled new-module declaration replay passed against the pinned imported environment.

**Boundary.** No formalized ODE invariance, Gavrilov coefficient convergence, monodromy fixed point, localized NS amplification, or ROOT. Full fresh imported-closure replay timed out.

- **Provenance:** Local conditional algebra module for the oblique-carrier argument.
- **Proof status:** Conditional conjugacy, inverse-basis, cone-face, and expansion-rate algebra; the hypotheses are supplied rather than proved by this module.
- **Review:** Local compiler, axiom-printout, and declaration-replay receipts recorded; external expert review: not recorded.
- **Formalization:** Lean 4.28.0 compilation and leanchecker declaration replay succeeded for NSEObliqueCone428 with propext, Classical.choice, and Quot.sound. Fresh replay of the full imported closure timed out. No analytic ODE invariance, Gavrilov convergence, NS theorem, or ROOT proof is certified.

**Sources:** [references/navier-stokes/fluid-lean-integration.md](../references/navier-stokes/fluid-lean-integration.md) · [formalization/oblique_cone/NSEObliqueCone428.lean](../formalization/oblique_cone/NSEObliqueCone428.lean) · [formalization/oblique_cone/receipt.json](../formalization/oblique_cone/receipt.json) · [formalization/oblique_cone/README.md](../formalization/oblique_cone/README.md)

<a id="nse-viscous-packet-amplification"></a>
## Finite supplied-seed full-NS amplification

**Evidence record — Written proof supplied; linear and nonlinear reviews recorded (reviewer type not documented); external expert acceptance not recorded.**

One frozen compact profile and orbit, fixed physical viscosity, changing smooth initial data indexed by L: actual Fourier high-pass gain at least a₁ ε^(−μc) at the prescribed finite time. The same construction excludes the old absolute activation target throughout its window and keeps the rescaled perturbation small in H³.

**Boundary.** No inherited seed, strain takeover in this regime, effective numerical scale threshold, infinite cascade, or formal NS certificate.

**Prior inputs:** [nse-gavrilov-oblique-instability](#nse-gavrilov-oblique-instability), [nse-steady-background-local](#nse-steady-background-local).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written finite supplied-seed amplification and activation-exclusion theorem; initial data vary with scale.
- **Review:** Linear and nonlinear mathematical reviews recorded; reviewer type and external expert acceptance: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/viscous-packet.md](../references/navier-stokes/viscous-packet.md) · [experiments/nse_viscous_packet.py](../experiments/nse_viscous_packet.py) · [tests/test_nse_viscous_packet.py](../tests/test_nse_viscous_packet.py) · [artifacts/enstrophy_sup/nse_viscous_packet.json](../artifacts/enstrophy_sup/nse_viscous_packet.json)

<a id="nse-wave-handover-obstruction"></a>
## Wave cancellation and generic stability obstruction

**Evidence record — Written proof supplied; review not documented.**

Exact single-phase self-interaction cancellation; explicit solenoidal errors with initial energy growth at the fast a/h scale; explicit pressure-generated normal slow velocity. Restricted initial identities and insufficiency result.

**Boundary.** No sustained-growth theorem, exclusion of every prepared construction, or singularity.

**Prior inputs:** [nse-viscous-packet-amplification](#nse-viscous-packet-amplification).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written exact self-cancellation, arbitrary-error cost, and pressure-mean calculations; these concern the specified fields and operators.
- **Review:** not recorded
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/wave-handover.md](../references/navier-stokes/wave-handover.md) · [experiments/nse_wave_handover.py](../experiments/nse_wave_handover.py) · [tests/test_nse_wave_handover.py](../tests/test_nse_wave_handover.py) · [artifacts/enstrophy_sup/nse_wave_handover.json](../artifacts/enstrophy_sup/nse_wave_handover.json)

<a id="nse-loglog-strain-handover"></a>
## Log-log supplied-seed strain handover

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

Restricted reviewed analytic theorem for one frozen profile, fixed physical viscosity and changing smooth initial data: ε=νh⁴, δ=√h, ℓ=√log(1/h), T=(2/μ)log ℓ. Full mean and harmonic corrections close an H¹² strong bootstrap; perturbation strain starts O(1/ℓ) and reaches at least cℓ at a reference Euler trajectory location in rescaled coordinates.

**Boundary.** No identification with the perturbed material trajectory, fixed-viscosity small-data C¹ instability, effective minimum L, formal NS certificate, nonlinear next-stage transfer, infinite cascade, or ROOT. The earlier absolute activation target remains excluded.

**Prior inputs:** [nse-gavrilov-oblique-instability](#nse-gavrilov-oblique-instability), [nse-steady-background-local](#nse-steady-background-local), [nse-wave-handover-obstruction](#nse-wave-handover-obstruction).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written finite strain-handover theorem with separate strong continuation.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/loglog-handover.md](../references/navier-stokes/loglog-handover.md) · [experiments/nse_loglog_handover.py](../experiments/nse_loglog_handover.py) · [tests/test_nse_loglog_handover.py](../tests/test_nse_loglog_handover.py) · [artifacts/enstrophy_sup/nse_loglog_handover.json](../artifacts/enstrophy_sup/nse_loglog_handover.json)

<a id="nse-outgoing-wave-linearized"></a>
## Finer-wave gain in the outgoing NS linearization

**Evidence record — Written proof supplied; derivation and assembled-proof reviews recorded (reviewer type not documented); external expert acceptance not recorded.**

Restricted reviewed linearized theorem: around the actual smooth first-stage NS solution, a real unit-L² exactly solenoidal seed specified at t₀=Tₕ−ℓ^(−3/4), of wavelength h^(3/2) and width h^(5/4), reaches radial high-pass norm at least cℓ^(1/4) at Tₕ, with all-mode error h^(1/4−o(1)). Fixed physical viscosity and changing first-stage data; actual-characteristic phase tracking is proved separately.

**Boundary.** No nonlinear second handover, compatible original time-zero seed, expanding shear Floquet multiplier, effective minimum scale, formal PDE certificate, infinite iteration, or ROOT.

**Prior inputs:** [nse-loglog-strain-handover](#nse-loglog-strain-handover).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written theorem for the exact viscous linearization about the actual first-stage flow; the finer seed is supplied at a late time.
- **Review:** Derivation and assembled-proof reviews recorded; reviewer type and external expert acceptance: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/outgoing-wave.md](../references/navier-stokes/outgoing-wave.md) · [experiments/nse_outgoing_wave.py](../experiments/nse_outgoing_wave.py) · [tests/test_nse_outgoing_wave.py](../tests/test_nse_outgoing_wave.py) · [artifacts/enstrophy_sup/nse_outgoing_wave.json](../artifacts/enstrophy_sup/nse_outgoing_wave.json)

<a id="nse-original-time-nonlinear-handover"></a>
## Original-time finite nonlinear handover

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

One fixed unscaled compact profile, fixed physical viscosity and varying smooth data. Both waves are supplied at original time zero. The finer seed starts with rescaled C1 size O(ell^(-5/8)), yields added strain at least c ell^(11/8) at a base-q particle, and has whole-flight integrated gradient O(ell^(11/8)). Full pressure and H12 continuation give C1 tracking h^(1/48-o(1)). Written theorem with separate agent reviews.

**Boundary.** No new-frequency generation, one-data infinite iteration, prescribed high-pass result, effective threshold, novelty, external expert acceptance or formal PDE certificate. Small initial C1 is in rescaled coordinates.

**Prior inputs:** [nse-loglog-strain-handover](#nse-loglog-strain-handover), [nse-gavrilov-oblique-instability](#nse-gavrilov-oblique-instability).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written nonlinear handover theorem with both waves in the original datum; the datum varies with scale.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/original-nonlinear-handover.md](../references/navier-stokes/original-nonlinear-handover.md) · [references/analysis/matching-review.md](../references/analysis/matching-review.md) · [references/analysis/smooth-seed-supply.md](../references/analysis/smooth-seed-supply.md) · [experiments/nse_original_handover.py](../experiments/nse_original_handover.py) · [tests/test_nse_original_handover.py](../tests/test_nse_original_handover.py) · [artifacts/enstrophy_sup/nse_original_handover.json](../artifacts/enstrophy_sup/nse_original_handover.json)

<a id="nse-localized-profile-handover"></a>
## Finite handover with a heat-evolved flat profile

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

Restricted written analytic extension for one fixed smooth odd periodic phase profile, one fixed compact background and fixed physical viscosity, with initial data varying with h. The full phase mean, all Fourier corrections, pressure and separate H12 continuation retain C1 tracking h^(1/48-o(1)). At the finite endpoint, an actual rescaled NS solution has a ball of radius c h^(3/2) on which its gradient differs from the stated constant matrix by at most h^(1/48-o(1)). The receiver is supplied at original time zero.

**Boundary.** No exactly affine patch, persistence of the endpoint region, generated next seed, one-datum infinite trajectory, uniformity over varying phase profiles, formal PDE certificate or solution of ROOT or FORCED-D. Review is by AI agents, not external expert acceptance. The fixed flat profile retains the full-support C3 seed cost.

**Prior inputs:** [nse-original-time-nonlinear-handover](#nse-original-time-nonlinear-handover).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written finite-profile extension, endpoint region, and finer-frequency exclusion.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/localized-profile.md](../references/navier-stokes/localized-profile.md) · [references/navier-stokes/next-seed-analysis.md](../references/navier-stokes/next-seed-analysis.md) · [references/analysis/flat-profile-seed-cost.md](../references/analysis/flat-profile-seed-cost.md) · [references/analysis/profile-extension-review.md](../references/analysis/profile-extension-review.md) · [references/analysis/checks/check-profile-extension.py](../references/analysis/checks/check-profile-extension.py)

<a id="nse-later-flow-core"></a>
## A short continuation and transported region in the same flow

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

Restricted written finite theorem with AI-agent review. The existing unforced solution and original datum continue another c ell^(-27/8); an actual transported radius-c h^(3/2) region retains rescaled gradient error O(ell^(-1/4)) through an additional ell^(-5). Full nonlocal pressure, diffusive leakage and a separate H12 continuation argument are included.

**Boundary.** The actual future source has an upper bound only. No signed next-seed lower bound, new handover, higher-jet persistence, infinite trajectory, formal PDE certificate or global solution. The fine-frequency exclusion persists.

**Prior inputs:** [nse-localized-profile-handover](#nse-localized-profile-handover).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written continuation and transported-core theorem for the same actual flow over the specified additional interval.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/later-flow-attempt.md](../references/analysis/later-flow-attempt.md) · [references/navier-stokes/next-transfer-review.md](../references/navier-stokes/next-transfer-review.md) · [references/analysis/checks/check-annular-geometry.py](../references/analysis/checks/check-annular-geometry.py)

<a id="nse-forced-fixed-annulus"></a>
## Why a fixed axisymmetric annulus cannot contain viscous breakdown

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

Classical regularity argument at a restricted geometric scope, rederived and AI-agent reviewed here. A full compact axisymmetric velocity uniformly away from a fixed axis, with ordinary positive viscosity and admissible smooth forcing, continues past a finite candidate terminal time. Includes the stated smooth compact embedding in a fixed periodic domain with periodic pressure.

**Boundary.** Not a general NS regularity theorem. Does not exclude finite gain, an axis-approaching flow, noncompact or nonaxisymmetric components, or a merely local axisymmetric core. It prevents retaining the released Euler construction's entire annular support geometry for the desired viscous breakdown.

- **Provenance:** Local derivation of a classical geometric continuation obstruction with smooth forcing.
- **Proof status:** Written continuation theorem for the full velocity in the stated fixed-axis annular class; it does not exclude general three-dimensional forced breakdown.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/fixed-annulus-obstruction.md](../references/analysis/fixed-annulus-obstruction.md) · [references/analysis/viscous-stage-attempt.md](../references/analysis/viscous-stage-attempt.md) · [references/analysis/force-gain-audit.md](../references/analysis/force-gain-audit.md) · [references/analysis/checks/check-annular-geometry.py](../references/analysis/checks/check-annular-geometry.py)

<a id="nse-logarithmic-host"></a>
## The same supplied wave after its focus

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

Restricted finite written theorem, separately reviewed by AI agents. For a sufficiently small fixed eta, the same original datum continues to t_f+log(ell)/(8mu)+log(eta)/mu. Rescaled added strain reaches order eta ell^2; whole strain history retains the same small coefficient, and full nonlinear C1 tracking is at most h^(1/96). Complete pressure, heat/profile corrections and a separate H12 continuation are included.

**Boundary.** Initial data still vary with h. No newly generated phase, infinite cascade, full formal PDE certificate or global solution. The shrinking almost-affine region is an endpoint estimate; dominant next-scale strain remains excluded.

**Prior inputs:** [nse-localized-profile-handover](#nse-localized-profile-handover).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written finite continuation theorem for the same original datum at each scale and small fixed eta.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/navier-stokes/logarithmic-host.md](../references/navier-stokes/logarithmic-host.md) · [references/analysis/logarithmic-host-review.md](../references/analysis/logarithmic-host-review.md) · [references/analysis/logarithmic-error-review.md](../references/analysis/logarithmic-error-review.md) · [references/analysis/checks/check-postfocus.py](../references/analysis/checks/check-postfocus.py)

<a id="nse-finite-depth-profile"></a>
## A finite correction depth and a bound on finer frequencies

**Evidence record — Written proof supplied; separate AI-agent reviews recorded; external expert acceptance not recorded.**

For fixed eta>0 and a sufficiently large finite J fixed before h tends to zero, the existing original-data unforced Q_h is tracked through t_eta by a full pressure/mean/profile approximation with integrated L2 residual h^((29+2J)/8)E and C1 error h^((19J-17)/96-C_*eta-o(1)); E is subpower for fixed indices. For every fixed beta>3/2 and P>0, choosing a finite derivative order and J before h gives sup_[0,t_eta] ||grad P_(>h^(-beta))Q_h||infinity<=h^P. The initial datum varies with h but does not change with proof indices.

**Boundary.** Separate AI-agent reviews of recurrence and finer-scale corollary plus root read. Global mean norms, all ordered interactions, sharp projection of the error via H3, expanding-torus normalization and separate H12 continuation are included. No formal PDE certificate, external expert acceptance or global solution.

**Prior inputs:** [nse-logarithmic-host](#nse-logarithmic-host).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written recurrence, continuation, and finer-tail corollary; depth and horizon parameters are fixed before the scale limit.
- **Review:** Separate AI-agent reviews of the recurrence and finer-tail consequence recorded; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/finite-depth-profile.md](../references/analysis/finite-depth-profile.md) · [references/analysis/finite-depth-profile-review.md](../references/analysis/finite-depth-profile-review.md) · [references/analysis/finer-scale-review.md](../references/analysis/finer-scale-review.md) · [references/analysis/checks/check-source-depth.py](../references/analysis/checks/check-source-depth.py)

<a id="nse-threed-forced-stage"></a>
## An actual finite three-dimensional forced stage

**Evidence record — Written proof supplied; separate AI-agent reviews recorded; external expert acceptance not recorded.**

An explicit smooth compact periodic three-dimensional host equals Ax, A=diag(lambda,2lambda,-3lambda), in its core. Its localized curl wave has plateau velocity gain exp(3Theta-(nu K^2/(2lambda))(1-exp(-2Theta))), exceeding 12 for lambda=nu K^2 and Theta=1. Full pressure, viscosity, localization, activation and return force terms and every fixed mixed derivative are specified. A finite example can start and end at rest with smooth compact-time forcing. A pressure-independent circulation lower bound applies to the specified unchanged cutoff strip.

**Boundary.** AI-agent full-stage review plus root read. The unchanged-strip obstruction permits new velocity corrections and changed geometry; a large gain ratio can coexist with a small absolute output. No infinite all-order force sequence or formal PDE certificate. A separate inherited-host review and exact full-residual controls also passed. Changing the interior velocity can change the force; the additive bound does not assume that mixed outgoing profiles automatically match a next stage.

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written finite forced construction and restricted force-cost/inheritance obstructions for the specified unchanged fields.
- **Review:** Separate AI-agent reviews of the finite stage and inheritance calculation recorded; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/threed-forced-stage.md](../references/analysis/threed-forced-stage.md) · [references/analysis/threed-forced-stage-review.md](../references/analysis/threed-forced-stage-review.md) · [references/analysis/inherited-forced-host.md](../references/analysis/inherited-forced-host.md) · [references/analysis/inherited-forced-host-review.md](../references/analysis/inherited-forced-host-review.md) · [references/analysis/checks/check-source-depth.py](../references/analysis/checks/check-source-depth.py)

<a id="nse-normal-source-transport"></a>
## A generated component survives exact linear transport

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

In the existing unforced varying-data family, let W=Q_h-q and let Z be the exact viscous linearization about the actual first-stage q with the original receiver as initial datum. The generated remainder N=W-Z has zero initial datum. For one fixed sufficiently small rescaled t0 independent of h and every 0<t<=t0, its original normal velocity and normal diagonal strain are bounded below by c t M_h kappa_h^4 and c t M_h kappa_h^5, respectively, where M_h~h^(27/4)ell^(-13/4), kappa_h=h^(-5/4)mathcal_E_h^(-2), and mathcal_E_h is the fixed preparation subpower majorant. No additional donor is supplied.

**Boundary.** Fixed small initial rescaled time only. The estimate concerns N=(Q_h-q)-Z, not a dominant component of Q_h. No postfocus sign, new short-wave phase, localized next receiver, infinite trajectory, formal PDE certificate or global solution follows. Review is by AI agents.

**Prior inputs:** [nse-logarithmic-host](#nse-logarithmic-host).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written transport and signed-source calculation on a fixed short interval of the same actual unforced flow.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/normal-source-transport.md](../references/analysis/normal-source-transport.md) · [references/analysis/normal-source-transport-review.md](../references/analysis/normal-source-transport-review.md) · [references/analysis/actual-third-source.md](../references/analysis/actual-third-source.md) · [references/analysis/checks/check-source-depth.py](../references/analysis/checks/check-source-depth.py)

<a id="nse-postfocus-source"></a>
## A generated intermediate band in the full flow

**Evidence record — Written proof supplied; separate AI-agent reviews recorded; external expert acceptance not recorded.**

For the same original-data unforced Q_h and fixed sufficiently small eta, the signed generated remainder survives focus. An explicitly defined smooth intermediate annular filter B_h has endpoint velocity and symmetric-strain lower scales h^(7/4+o(1)) and h^(1/2+o(1)) in full Q_h. The initial band has upper scales h^(2-o(1)) and h^(3/4-o(1)). Separate full-band estimates for q and the exact linear receiver Z prevent cancellation. N=(Q_h-q)-Z has sup C1 at most C h^(1/96) and whole current-window gradient integral at most C h^(1/96) log ell, tending to zero.

**Boundary.** Fixed profile, sufficiently small fixed eta and finite indices precede h tending to zero; data still vary with h. The measured band is coarser than the supplied receiver. No later-time exclusion, full-field component dominance, formal PDE certificate, external expert acceptance or global result. Reviewed written analysis by AI agents.

**Prior inputs:** [nse-normal-source-transport](#nse-normal-source-transport), [nse-logarithmic-host](#nse-logarithmic-host).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written signed postfocus source, full-flow intermediate-band comparison, and associated affine transport calculation.
- **Review:** Separate AI-agent reviews of the source, full-flow band, and affine calculation recorded; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/postfocus-normal-source.md](../references/analysis/postfocus-normal-source.md) · [references/analysis/postfocus-normal-source-review.md](../references/analysis/postfocus-normal-source-review.md) · [references/analysis/actual-coarse-band.md](../references/analysis/actual-coarse-band.md) · [references/analysis/actual-coarse-band-review.md](../references/analysis/actual-coarse-band-review.md) · [references/analysis/affine-stress-transport.md](../references/analysis/affine-stress-transport.md) · [references/analysis/affine-stress-transport-review.md](../references/analysis/affine-stress-transport-review.md) · [experiments/nse_postfocus_normal_source_checks.py](../experiments/nse_postfocus_normal_source_checks.py) · [experiments/nse_coarse_band_linear_checks.py](../experiments/nse_coarse_band_linear_checks.py)

<a id="nse-coupled-forced-stages"></a>
## The full force of opposing and cyclic waves

**Evidence record — Written proof supplied; AI-agent review recorded; external expert acceptance not recorded.**

For the specified compact forced extensions of the affine-core stage, all pressure, localization, activation and fixed mixed force derivatives are retained. Opposing waves can have zero instantaneous interior force at equal frequency q, while the mixed spatial/time force derivative is at least 4 lambda ab q^2 on the stated plateau. A supplied three-direction cycle has P′=-nu(kappa^2+ell^2+m^2)P and exact quadratic feedback gradient S^2; specified surviving loops give pressure-independent force costs.

**Boundary.** Restricted unchanged-field and surviving-loop statements; they permit new interior velocity corrections. The reverse interior is planar, while the cycle uses all three directions. Instantaneous spectra do not control nonnormal propagation. No universal force obstruction or infinite construction. Reviewed written analysis by AI agents.

**Prior inputs:** [nse-threed-forced-stage](#nse-threed-forced-stage).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written complete residuals and pressure-independent force restrictions for the specified reverse pair and three-direction cycle; corrected velocities are outside the obstruction.
- **Review:** AI-agent mathematical review recorded at the stated scope; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/twoway-forced-coupling.md](../references/analysis/twoway-forced-coupling.md) · [references/analysis/cyclic-forced-coupling.md](../references/analysis/cyclic-forced-coupling.md) · [references/analysis/coupled-stages-review.md](../references/analysis/coupled-stages-review.md) · [references/analysis/checks/check-coupled-stages.py](../references/analysis/checks/check-coupled-stages.py)

<a id="nse-periodic-cycle-transfer"></a>
## Actual nonlinear transfer can raise total enstrophy

**Evidence record — Written proof supplied; AI-agent reviews recorded; external expert acceptance not recorded.**

For u0=A(sin(qx2),sin(qx3),sin(qx1)), integer q>=1, ordinary nu>0 and mu=nu q/A sufficiently small, the actual unforced periodic solution generates its initially absent sqrt(2)q shell. With tau=Aq t, full pressure-corrected jets and a uniform Sobolev remainder give Q(tau)/Q0=1-2mu tau+(1/2+2mu^2)tau^2+O(tau^3). One fixed tau0>0 and all 0<mu<=tau0/16 give Q(tau0)>=Q0(1+tau0^2/8), despite initial viscous decline. Kinetic energy decreases.

**Boundary.** A common spatial translation of the original activation prototype, extended to second-order pressure and total enstrophy. Finite gain only; no L-infinity velocity amplification, shape return, infinite transfer, formal PDE certificate or NS solution claim. Reviewed written analysis by AI agents.

**Prior inputs:** [nse-frequency-activation-local](#nse-frequency-activation-local).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written full-pressure short-time expansion, uniform remainder, and finite enstrophy-gain theorem for the actual periodic solution.
- **Review:** AI-agent reviews of the finite transfer and subsequent point-pressure diagnostic recorded; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/periodic-cycle-transfer.md](../references/analysis/periodic-cycle-transfer.md) · [references/analysis/periodic-cycle-transfer-review.md](../references/analysis/periodic-cycle-transfer-review.md) · [references/analysis/checks/check-periodic-cycle-transfer.py](../references/analysis/checks/check-periodic-cycle-transfer.py) · [references/analysis/cycle-point-feedback.md](../references/analysis/cycle-point-feedback.md) · [references/analysis/cycle-point-feedback-review.md](../references/analysis/cycle-point-feedback-review.md) · [references/analysis/checks/check-cycle-point-feedback.py](../references/analysis/checks/check-cycle-point-feedback.py)

<a id="nse-diagonal-window"></a>
## An arbitrarily slow growing comparison window

**Evidence record — Written proof supplied; AI-agent review and coordinating-agent read recorded; external expert acceptance not recorded.**

For the same fixed smooth-profile varying-data family, there exists an integer staircase eta(h) tending to infinity sufficiently slowly, with finite J(h),r(h), such that the actual unforced Q_h is smooth through t_f+log(ell)/(8mu)+log(eta(h))/mu. Its full C1 approximation error is at most h^eta(h), its endpoint symmetric strain and whole gradient clock are comparable to eta(h)ell^2, and every fixed finer-power tail beta>3/2 is smaller than every fixed power h^P. The schedule may be chosen below any prescribed divergent bound.

**Boundary.** Existential schedule only; no prescribed growth rate for arbitrary smooth profiles. Initial data depend on h but not proof indices. Same-datum uniqueness identifies the compared solutions. Absolute Fourier sums supply tail monotonicity. No one-datum infinite trajectory, formal PDE certificate or global result.

**Prior inputs:** [nse-finite-depth-profile](#nse-finite-depth-profile), [nse-logarithmic-host](#nse-logarithmic-host).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written existential diagonal corollary of reviewed fixed-parameter estimates; it provides no prescribed growth rate or single-data infinite trajectory.
- **Review:** AI-agent review and coordinating-agent read recorded for the same-datum quantifiers, endpoint/clock constants, continuation, and Fourier tail; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/diagonal-window.md](../references/analysis/diagonal-window.md) · [references/analysis/diagonal-window-review.md](../references/analysis/diagonal-window-review.md)

<a id="nse-cycle-speed-loss"></a>
## Strain energy can rise while maximum speed falls

**Evidence record — Written proof supplied; AI-agent reviews and separate exact Fourier controls recorded; external expert acceptance not recorded.**

For the actual periodic solution U_mu from (sin y,sin z,sin x), one fixed short T_*>0 works uniformly for 0<=mu<=1 and gives ||U_mu(tau)||infinity^2<=3-3mu tau-(4/5)tau^4 on 0<tau<=T_*. For sufficiently small positive mu, strain energy increases at a time in this same interval while maximum speed decreases. The full Euler moving-maximum expansion is 3-(8/5)tau^4+O(tau^5), with positive-viscosity correction -6mu tau+O(mu tau^2).

**Boundary.** Full pressure, all eight initial moving maxima and an actual uniform local PDE remainder are retained. This restricts early maximum-speed gain for this datum, not later times or other flows. Exact finite Fourier controls are not a PDE certificate; no general maximum principle or global result.

**Prior inputs:** [nse-periodic-cycle-transfer](#nse-periodic-cycle-transfer).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Written actual-flow maximum-speed loss theorem with all-mode time remainders and a viscosity-uniform interval; the fixed-positive-amplitude extension has its own source.
- **Review:** AI-agent analytic reviews and separate exact Fourier controls recorded; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/cycle-next-transfer.md](../references/analysis/cycle-next-transfer.md) · [references/analysis/cycle-next-transfer-review.md](../references/analysis/cycle-next-transfer-review.md) · [references/analysis/checks/check-cycle-next-transfer.py](../references/analysis/checks/check-cycle-next-transfer.py) · [references/analysis/asymmetric-cycle-speed.md](../references/analysis/asymmetric-cycle-speed.md) · [references/analysis/asymmetric-cycle-speed-review.md](../references/analysis/asymmetric-cycle-speed-review.md)

<a id="nse-growing-profile-window"></a>
## An explicit growing window for fixed Gevrey profiles

**Evidence record — Written proof supplied; separate AI-agent reviews recorded; external expert acceptance not recorded.**

Choose one fixed Gevrey-2 member of the stated Gavrilov/two-packet class before h tends to zero, and fix positive physical viscosity. With eta=ell^(1/16), T=t_f+3log(ell)/(16mu), and J=ceil(K eta) for a sufficiently large fixed K, the same datum at each h has an actual smooth unforced Q_h through T. A finite pressure-complete approximation has gradient error at most h^eta. Endpoint added symmetric strain is comparable to eta ell^2. Uniform derivative estimates and the full mean/profile recurrence have logarithmic loss o(eta ell^2), paying the ordinary fixed-H12 continuation cost.

**Boundary.** Additional quantitative Gevrey hypothesis, realized by fixed cutoffs on a positive pressure annulus. Arbitrary old smooth cutoffs are not automatically covered at this rate. Datum still varies with h; no new seed, infinite correction series, infinite one-datum trajectory, terminal force or global result. Separate AI-agent background/operator/assembly reviews and root read; no formal PDE certificate or external expert acceptance.

**Prior inputs:** [nse-finite-depth-profile](#nse-finite-depth-profile), [nse-logarithmic-host](#nse-logarithmic-host).

- **Provenance:** Local analysis using classical PDE, ODE, or Fourier methods; no priority claim.
- **Proof status:** Restricted written quantitative growing-window theorem for one fixed Gevrey-2 profile choice; the datum varies with scale.
- **Review:** Separate AI-agent reviews of the quantitative background, operators/recurrence, and continuation assembly, followed by coordinating-agent integration reads; external expert review: not recorded.
- **Formalization:** not recorded

**Sources:** [references/analysis/uniform-profile-window.md](../references/analysis/uniform-profile-window.md) · [references/analysis/uniform-profile-window-review.md](../references/analysis/uniform-profile-window-review.md) · [references/analysis/uniform-profile-assembly-review.md](../references/analysis/uniform-profile-assembly-review.md) · [references/analysis/growing-window-background.md](../references/analysis/growing-window-background.md) · [references/analysis/growing-window-background-review.md](../references/analysis/growing-window-background-review.md) · [references/analysis/growing-depth-budget.md](../references/analysis/growing-depth-budget.md) · [references/analysis/growing-depth-budget-review.md](../references/analysis/growing-depth-budget-review.md) · [references/analysis/growing-window-remainder.md](../references/analysis/growing-window-remainder.md) · [references/analysis/growing-window-remainder-review.md](../references/analysis/growing-window-remainder-review.md)
