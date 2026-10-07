# Reading OpenAI’s external result

Checked 8 September 2026. This record accompanies [the chapter on the published construction](../../notes/chapters/published-proof.md). It attributes an external result and records a bounded source inspection; it is not a local certification of the complete proof or a claim that the project produced that result.

## Release pins and inspected scope

| Item | Current evidence |
|---|---|
| Announcement | OpenAI, [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/), dated 8 September 2026. |
| Primary paper | OpenAI, [Finite time blowup for Navier–Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), 165 pages. Downloaded bytes have SHA-256 `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`. |
| Paper reading | Theorem 1.1; physical description and proof outline in §§1–3, including Theorem 3.1; Corollary 10.6 and its periodicization/uniqueness argument. Targeted reading of stress, correction, localization and force-extension passages. No line-by-line audit of all 165 pages. |
| Public formalization | [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538), inspected commit `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`; GitHub API gives commit timestamp `2026-09-08T10:57:25Z`. |
| Local native build | The exact `NavierStokes.ComparatorSolution` target built successfully with official Lean `4.34.0-rc2` on Darwin ARM and the locked dependencies. All 580 project-local modules compiled from unchanged sources; matching Mathlib artifacts were cached. Both exported theorems printed only `propext`, `Classical.choice`, `Quot.sound`. [Commands, pins and checking scope](../../formalization/external_ns/README.md). |
| Stronger imported-closure replay | Bundled `leanchecker --fresh` did not finish within its 600-second limit. This replay is incomplete, not a reported proof error. It uses Lean's kernel, not an independently implemented verifier. |
| Formalization claims | [`formalization.yaml`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/formalization.yaml) reports full main-result formalization and `propext`, `Classical.choice`, `Quot.sound`; review status is `self-assessed`. Its no-`sorry` report concerns the main results. The separate Navier–Stokes challenge deliberately contains two placeholders; the submitted proof's import closure excludes that challenge. |
| Local statement audit | The [bounded source audit](../analysis/external-statement-audit.md) compared complete shared definitions and theorem headers, inspected adapter predicates, and followed 580 project-local solution imports. It found no statement defect, proof-hole tokens, or axiom declarations in that local closure. This is source evidence, not compiled axiom output or a kernel replay. |
| Explicit theorem surface | [`NavierStokes/ComparatorSolution.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ComparatorSolution.lean) exposes `NavierStokes.Comparator.navier_stokes_breakdown_R3` and `NavierStokes.Comparator.navier_stokes_breakdown_periodic`. Their declarations quantify every positive viscosity and existential data/force. |
| Independent-check configuration | [`ComparatorChallenges/NavierStokes.json`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/NavierStokes.json) selects those two declarations, enables Nanoda, and permits the three listed axioms. The [Comparator instructions](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/README.md) were read; the check was not executed. |

The theorem statement and force/data distinctions are reproduced concisely in the chapter. C/D are the forced alternatives; no unforced Navier–Stokes conclusion follows. The companion Euler theorem concerns a different equation. The official problem's pressure-periodicity erratum was checked directly in [Fefferman's statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).

Terminal regularity means smooth extension through the finite breakdown time, normalized to one in the paper's whole-space theorem. The inspected arbitrary-viscosity formal adapter instead rescales a viscosity-one witness to terminal time `1/nu`; its exported nonexistence statement fixes no terminal time. The local residual is flat at the singular space-time point, but Lemma 10.2 allows nonzero limiting force derivatives away from that point. The chapter's scalar zero-extension exercise is a sufficient illustrative construction, not a claim that the paper's localized force vanishes everywhere at time one. The paper's uniform preterminal energy assertion remains paper-attributed here: the explicit energy condition in the inspected comparator type concerns a hypothetical global whole-space competitor.

## Logical bridge, with ownership preserved

The chapter's bridge table separates three kinds of relationship:

1. **Exact standard identities:** complete residual expansion; divergence-free curl realization; integration by parts and pressure orthogonality. Our project notes and the released construction use these operations. This does not establish a historical or causal connection.
2. **Conceptual parallels:** finite shear amplification with ordinary diffusion, mean/oscillation correction, and finite-order error accounting. A lemma on our actual periodic background is not automatically a lemma on the external profile.
3. **Additional external construction:** a compatible concentrating core and stress geometry, actual stress realization, a summed field with all-order residual estimates, compact forcing through the terminal time, and the uniqueness argument that identifies breakdown. The project had not supplied this assembly.

Selected public source inspections support the distinction: [`ActualPrimaryCovariance.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualPrimaryCovariance.lean) assembles the selected labels before covariance averaging; [`DiagonalResidual.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalResidual.lean) explicitly distinguishes fixed derivative losses from stage-dependent constants. [`PeriodicLocalization.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PeriodicLocalization.lean) and [`CompactForceDecay.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CompactForceDecay.lean) expose localization and all-derivative decay steps. This was declaration/comment inspection with selected proof reading, not replay of their dependency graphs.

Our fixed-annulus exclusion only concerns a complete axisymmetric velocity uniformly separated from one fixed axis. It cannot be applied to an arbitrary shrinking-core construction or to a whole field that contains angular oscillations. Our finite corrected-packet families also remain varying-data finite theorems; the external result does not retroactively turn them into a single singular trajectory. The project ROOT and E-prime claims require their own evidence. Any canonical status reconciliation belongs to the coordinating task, not this source record.

## Local teaching checks

The new chapter contains independent worked examples rather than a compressed imitation of the external proof:

- A compact divergence-free potential family yields exact energy exponent `97/200`, radial dissipation exponent `-103/200`, and axial dissipation exponent `-101/200` at the illustrative parameter `alpha=1/200`. These are kinematic norm calculations only.
- An explicit stationary periodic wave cancels a shear's complete mean residual after pressure correction, but its full new residual retains `nu*(1+N^2)*w` and the old/new interaction. Exact symbolic differentiation reproduced the entire vector identity. Pairing with the horizontal solenoidal wave proves a pressure-independent normalized L2 force lower bound `nu*(1+N^2)*sqrt(1+N^(-2))/2` for these unchanged velocities.
- Exercise solutions check positive flux-cone coefficients and a perturbation margin, the all-orders requirement for smooth zero extension, and the theorem's quantifiers.

The [component extraction](../analysis/external-component-extraction.md) identifies the actual periodized leading covariance identity and a phase-replacement corollary. Its [local Lean companion](../../formalization/phase_covariance/README.md) passed compilation and a replay of its declarations. The complete transport, pressure, correction and terminal estimates for a changed phase remain separate obligations.

The exact external Navier–Stokes target has now been built locally; the independent Comparator/Nanoda workflow has not been run. The stronger bundled-kernel imported-closure replay has its own outcome in the verification receipt. No DNS, external expert certification, publication or repository visibility change was performed by this bounded task.


## Why removing the force remains a separate problem

The active research target is an unforced solution with one fixed smooth
datum and fixed positive viscosity. The external forced theorem supplies a
reference construction; it does not settle this target. A successful
comparison must control the complete momentum error and prove that the new
solution either breaks down earlier or retains singular growth. Its terminal
time need not coincide with that of the reference.

The first three notes establish the comparison framework:

- [The source audit](../analysis/external-force-removal-source.md)
  records the actual terminal force traces, exterior cutoff terms and the
  same-datum restart comparison.
- [The stability analysis](../analysis/force-removal-stability.md)
  gives conditional error budgets and identifies the missing estimate needed
  to preserve concentrating velocity growth after force removal.
- [The projection-locality example](../analysis/force-projection-locality.md)
  constructs a smooth force that vanishes near a point while its Leray
  projection has nonzero strain there. This illustrates the pressure issue;
  it is not a computation of the external construction's actual force.

Subsequent calculations resolve some of that framework's open questions:

| Question | Result and scope |
|---|---|
| Does the actual projected force vanish at the terminal time? | **No.** The [terminal-force calculation](../analysis/terminal-force-nonzero.md) finds a nonzero circulation in the source's cutoff annulus. A gradient cannot remove it. This concerns this construction's actual localization. |
| Can the coarse Sobolev comparison remove it? | **No.** The [inner-circle calculation](../analysis/external-modulation-source.md) gives a full-gradient lower bound of order `(1-t)^(-1-h)`. Together with the nonzero projected force, it makes the earlier scalar Gronwall test fail at every fixed late restart. This is not a lower bound on the true error. |
| Is an elongated support enough for the nonlinear estimate? | **No.** The [anisotropic error analysis](../analysis/anisotropic-error-budget.md) proves an unbounded heat–Leray bilinear map for an unrestricted localized error class. It also proves useful bounds for two smaller classes, including axisymmetric errors whose leading centrifugal interaction is a pressure gradient. Membership and preservation of those classes remain unproved for the actual error. |
| Can the singularity's time and position move? | **Yes, within a conditional comparison.** The [modulation note](../analysis/modulated-force-removal.md) derives the exact moving-frame residual, mean-force correction and error equations. It does not establish their required bounds for this construction. |
| Can all linear errors obey a uniform bound depending polynomially on the ratio of remaining times? | **No in L2.** The [exterior quasimode calculation](../analysis/exterior-quasimode.md) localizes the source's centrifugal coupling, keeps the full global Leray projection and derives amplification of the actual two-parameter linearized propagator. Its lower bound concerns an unspecified perturbation and restart time, not the response to removing the actual force. |
| Does that amplification imply that the force excites those packets? | **No.** The [actual force-coupling calculation](../analysis/exterior-force-coupling.md) expresses the first possible coupling through a global pressure moment. Its sign is unknown, and its pairing with the specified rapidly oscillating packet is smaller than every fixed power of the remaining time. The [response-jets extension](../analysis/force-response-jets.md) proves this smallness for every fixed linear-response derivative. It does not bound the full response or its Taylor remainder. |
| Could correcting finitely many directions make the remaining linear evolution uniformly controlled? | **Not in the stated full Sobolev space.** The [initial-correction analysis](../analysis/initial-correction.md) packs at least `c tau^(-9h/8)` independent exterior packets. Any invariant complement of smaller codimension has projected propagator norm at least `c_m tau^(-h/8)` on a short late window. This is a transient-growth statement, not an unstable eigenvalue count. |
| Could one specially chosen initial datum still remove the force? | **Possibly; the construction is missing.** The same note proves a conditional terminal-integral theorem, with a derivative-paying nonlinear budget and a precise requirement for preserving singular growth. A scalar example permits exact cancellation. A separate parabolic example shows that infinitely many mode cancellations can require initial coefficients too large even for a distribution. Neither example decides the actual Navier–Stokes case. |
| Can the complete linear response be estimated for the specified exterior packets? | **Yes, on their logarithmic flight.** The [full response estimate](../analysis/local-response-bound.md) gives packet pairing at most `C exp(-c tau^(-h/16))` for a fixed Gevrey-2 axial bump. A weighted pressure estimate retains the complete nonlocal response. The [global strain bound](../analysis/global-strain-cost.md) pays for all reference waves and the infinite correction tail. This bounds selected local pairings, not the whole response norm or the nonlinear error. |
| Does the leading slowly varying pressure moment supply a simpler amplifier? | **No closed amplifier follows from that moment alone.** The [slow axial calculation](../analysis/low-axial-response.md) gives an exact affine local response and a classical strained-vortex completion, but their strain rate depends on global pressure boundary data. It also proves that sufficiently thin radial packets with slow axial variation are dissipative. |
| Can the natural radial scale be treated without freezing the profile? | **Yes, with explicit boundary input.** The [natural radial calculation](../analysis/natural-radial-response.md) retains curvature, viscosity and the full changing heat profile. Its conditional energy estimate and radial boundary lift have explicit costs; converting the normal velocity trace can lose `tau^(-h)`. The actual global traces and axial matching residual remain unresolved. The sufficient damping condition is not yet verified for the source constants. |
| What determines the pressure arriving from elsewhere? | **A signed integral of the full response.** The [global pressure calculation](../analysis/global-pressure-feedback.md) retains core, annular, exterior and periodic-image stresses. At separation comparable to `sqrt(tau)`, the remote axial pressure Hessian is bounded by `C tau^(-9/4-h)||e||2`. Test fields paired with the actual reference attain this scale with opposite signs, despite identical norms and zero local jets. Those tests are not the actual force response; the result identifies the spatial information a closing estimate must use. |
| Can an actual nonlinear unforced solution track the reference for a growing strain clock? | **Yes, for a finite interval at each restart.** The [nonlinear comparison](../analysis/nonlinear-force-comparison.md) starts from exactly `U(1-tau)` and continues through `d=c tau^(1+h) sqrt(L)`, `L=1+log(1/tau)`. The velocity error is at most `C tau^(3(1+h)/16) sqrt(L)` and its integrated gradient at most `C tau^(11(1+h)/16) L`, both tending to zero. Sharp fixed spatial derivatives and a scaled H3 energy estimate retain the complete quadratic error and pressure. The datum varies with `tau`; this supplies no singular trajectory. |
| Can the selected growing directions be corrected in the actual nonlinear equation? | **Yes, for one finite endpoint.** The [nonlinear endpoint correction](../analysis/nonlinear-endpoint-correction.md) proves a dimension-independent inverse estimate for the endpoint map on the entire specified packet space. A contraction chooses one small smooth initial adjustment that cancels that projection exactly while retaining the finite unforced comparison. Its nonlinear error bound includes a polynomial term; it is not stretched exponentially small in every Sobolev norm. Neither the complementary error nor one fixed earlier datum is supplied. |
| What would make these corrections come from one earlier datum? | **Uniform actual reachability estimates.** The [linear correction note](../analysis/exterior-correction-operator.md) gives exact Gram-matrix range and inverse-cost criteria for finite or countably many endpoint measurements at a common initial time. It includes all inherited forcing. The uniform costs, smoothness and nonlinear extension across intervals remain open. |
| Does the signed pressure moment close under evolution? | **The first weight does not form a closed family.** The [pressure evolution](../analysis/pressure-response-evolution.md) derives its exact global tensor and adjoint identities. Direct annular force injection vanishes, but the next weight creates a meridional component and global pressure tail. The annular pressure moment's actual initial curvature depends on the undetermined terminal force moment; no full later-flight estimate follows. |
| Can the primary wave's high frequency average away the large strain? | **No such material-time averaging follows.** The [phase analysis](../analysis/primary-strain-averaging.md) shows that the carrier is nearly stationary along an actual trajectory while it stays in one valid label chart. Its nilpotent gradient still incurs coordinate distortion, and a complete-pressure Kelvin example defeats the specified simple weighted metric. Other adapted estimates remain possible. |

The distinction between growth and excitation is decisive. The compact test fields used in the
quasimode calculation lie in an exterior region where the physical force is
exactly zero. Their direct pairing with its Leray projection therefore
vanishes. A large operator norm does not prove a large response to this
particular source. Conversely, local flatness of the physical force does not
give a global stability estimate.

The linear packet result controls the full time interval for one specified
family of tests. This is stronger than smallness of each fixed Taylor coefficient:
the pressure estimate accounts for all intermediate times. It remains
compatible with a large propagator norm and with an uncontrolled response
in other directions.

The nonlinear result addresses a shorter interval and the full difference
between two solutions. On that interval the unforced flow has a strain
clock tending to infinity, even though the error's strain clock tends to
zero. This is possible because the initial flows themselves become larger
as the restart approaches time one. It does not show that any one of those
flows becomes singular. The absolute gradient error may grow; the velocity
error and integrated gradient are the quantities shown to vanish.

The endpoint correction now strengthens that finite result. Every selected
packet follows the actual linearized evolution on a sufficiently short
window, giving a uniform compressed inverse. The nonlinear solution map
retains this property throughout a small initial ball. A single adjustment
then makes the specified endpoint measurements zero. This is a finite
nonlinear correction theorem; the projection is not invariant, and the
remaining error need not vanish.

**Next mathematical task.** Realize compatible constraints from one fixed
earlier datum. In the linear problem, the new Gram criterion states this
exactly: the full force measurement vector must lie in the range of each
finite Gram matrix, with uniformly bounded minimum initial norm. Smoothness
needs the stated all-order bounds on the same sequence of minimizers.
The inherited forcing before each local window is part of that vector.
No available estimate yet verifies these actual-source conditions.

A nonlinear construction also needs control of the complementary error and
interactions between constraints. The earlier sufficient restart tolerance
is initial scaled H3 error at most `C_in d`; its general endpoint bound
does not verify that allowance at the next interval. Cancelling the chosen
projection does not by itself repair this gap. Neither failure of an upper
estimate nor a successful finite correction decides the global question.

The natural radial calculation now provides a boundary transfer estimate;
its application needs the actual slowly varying and annular response with
global pressure and axial matching data. The exact moment hierarchy now
shows where its next global pressure contribution enters, but does not
bound that contribution through the needed interval. A terminal Green
operator remains another way to select one initial correction, if its
integral converges in a useful function space. Either route must retain nonlinear
continuation and a quantitative fraction of singular growth for one datum.
The cylindrical class above remains a candidate, not an established
invariant class. No reset of the error is justified by these finite results.
The pressure record identifies the complete linear cross stress; a nonlinear
application must also include the error's own quadratic stress, which need
not be supported where the reference is supported.

These are restricted written analytic results with separate AI-agent
reviews and root checks. The [symbolic companion](../analysis/checks/check-force-removal.py)
checks elementary identities, exponents and negative controls. It does not
verify the source identification or the analytic proofs. No new full formal
certificate or DNS is claimed. Unforced ROOT and E-prime remain **OPEN**.
