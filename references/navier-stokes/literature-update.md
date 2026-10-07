# Euler, Navier–Stokes and the internal-model claims

> **Source update — 8 September 2026.** OpenAI published the external forced-breakdown construction. See the [source assessment](openai-result-bridge.md). FORCED-D is **IMPORTED**; unforced ROOT and E-prime remain **OPEN**. Earlier FORCED-D labels below describe the local research before that publication.


**Primary sources checked 8 September 2026, through approximately 11:51 UTC.**
Three independent research lanes checked current announcements, mathematical
statements, versions and released code. This is a bounded source audit, not
verification of every new proof. No public OpenAI NS proof was located in the
checked sources. [Clay still lists NS as unsolved](https://www.claymath.org/millennium/navier-stokes-equation/);
that status can lag research and does not disprove a private result.

**Subsequent method analysis, 8 September:** both [unforced ROOT and periodic
smoothly forced FORCED-D](two-track-program.md) are now active
project targets. The [reviewed viscosity comparison](forced-viscosity.md)
excludes literal reuse of the released compact Euler velocity with smooth
NS force, but identifies a common principal heat operator preserving its
selected central return. The [force analysis](forced-admissibility.md)
gives exact physical scaling and sufficient terminal extension conditions.
These are new local calculations using the stated sources, not a newly
located NS proof or a repeat of the full announcement audit.

## The internal OpenAI story: what is actually public

[Buckmaster's university-hosted statement](https://cims.nyu.edu/~tristanb/statement.pdf)
is a primary account of what he was told, not an available NS proof. He
reports September 6 discussions about an internal OpenAI model and an
approximately 100-page proof of smoothly forced NS breakdown on R3 and T3,
under Fefferman's C/D conditions. He explicitly writes, “I have not seen
OpenAI’s proof.” His [public announcement](https://mastodon.social/@tristanbuckmaster/117233413705701198)
was posted at 2026-09-08 03:58:50 UTC and links the statement, three fluid
papers and `fluid_lean`. The checked repository contains Euler and two
Boussinesq projects; no IPM formalization was located. The public
[API record](https://mastodon.social/api/v1/statuses/117233413705701198)
was used to verify that timestamp.

[Bubeck's own response](https://x.com/SebastienBubeck/status/2097214122471432349)
disputes allegations about his conduct. The accessible excerpt from X's
official oEmbed endpoint contains no mathematical proof. This audit does
not adjudicate the dispute or infer that private drafts were used. Model
names, comparative capability and access to an internal proof are not
established by the materials inspected. An announcement about other AI
mathematics is not an NS proof dependency.

**Forcing requires precision.** The [official Fefferman statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf),
pp. 1–2, has four alternatives. A/B ask for unforced global smoothness;
C/D allow breakdown with a force satisfying specified all-order smoothness
and decay conditions. A correct forced-NS proof meeting those conditions
could resolve a Clay alternative. Forced Euler, fractional dissipation, or
a force smooth only before the proposed singular time does not automatically
meet them. This repository's ROOT is the distinct unforced periodic claim.

## Released work and its usable content

### The new forced-fluid constructions

The released [Euler](https://cims.nyu.edu/~tristanb/euler.pdf),
[Boussinesq](https://cims.nyu.edu/~tristanb/boussinesq.pdf) and
[IPM](https://cims.nyu.edu/~tristanb/ipm.pdf) papers concern smooth-forcing
blowup in their respective equations. The first two are by Alpöge and
Buckmaster; the IPM paper also credits Matei P. Coiculescu. Buckmaster's
statement reports further unreleased hypodissipative work; that is not a
released theorem for the ordinary Laplacian viscosity.

[Tao's 7 September exposition](https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/)
explains the localized wave construction and prospective extensions to NS
and removal of forcing. This is the context of the supplied Tao screenshot.
An extension being plausible is distinct from a completed released argument.

Three concrete methods deserve attention:

- **An exactly linear interior.** The Boussinesq construction uses a smooth
  periodic odd profile equal to its argument near zero, with a localized
  primitive. Later waves can sit inside an exactly affine core. Its
  two-field modulation system and controlled rotation reset the outgoing
  state. This uses a temperature channel and forcing; neither is available
  automatically in unforced NS. See the Boussinesq introduction, pp. 3–5.
- **One sequence controlling every derivative.** Boussinesq Theorem 7.3,
  equation (7.24), p. 63, bounds the complete physical force pair in mixed
  C^k_{x,t} norms by lambda_q^(-1/2) for k<=k_q. Theorem 8.2, pp. 67–68,
  chooses one sequence; Lemma 9.3, p. 71, supplies smooth terminal extension
  using summability and the next derivative order. The force includes
  compact inverse-curl reconstruction, not just a curl residual.
- **Exact preceding dynamics.** Euler's construction transports new
  localized circulation/velocity oscillations by the preceding corrected
  field and organizes mixed derivatives and smooth physical forcing in
  sections 6 and 12–13. Its parameter and outgoing-state control should be
  compared with our one-datum gap; ordinary NS viscosity remains an extra
  obligation.

These are proposed imports of methods. The full new papers were not all
independently re-proved in this audit.

### The separate unforced Euler candidate remains conditional

The live [Ganeshram–Duruisseaux–Anandkumar manuscript](https://anima-ai.org/wp-content/uploads/2026/09/Euler.pdf)
is 107 pages. Its printed p. 5 states that rigorous certification of
profile-dependent margins is unfinished. Theorem 1 on p. 13 assumes
residual, damping and nonlinear estimates; section 4.6 also needs rescaled
local well-posedness and continuation. The checked version does not supply
an unconditional blowup theorem. At its critical scaling, ordinary NS
viscosity would survive in the profile equation rather than disappear.

[Tao's 8 September assessment](https://mathstodon.xyz/@tao/117234157753860650),
posted at 07:08 UTC, likewise describes a promising numerical ansatz with
rigorous stability still requiring work. The manuscript is a useful
profile/certification target, not a certified Euler or positive-viscosity
NS solution. Page numbers are printed pages, not zero-based PDF indices.

**Further primary-source check, 8 September:** in a comment on
[Tao's exposition](https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/),
Gonzalo Cao-Labora asks for first and second derivative bounds on the GDA
profile residual. He explains that a small undifferentiated residual did
not suffice in earlier work to establish a nearby smooth solution. He
explicitly does not claim that the GDA candidate fails. This is an expert's
request for missing certification data, not a refutation or a new theorem.

### A concrete mechanism for generating the next seed in actual NS

[Palasek, *Arbitrary norm growth in the 3D Navier–Stokes equations*,
arXiv:2509.18595v1](https://arxiv.org/html/2509.18595v1), Theorem 1.1 and
section 1.2, constructs full unforced periodic NS solutions using data in
one high frequency shell. High-high-to-low interactions generate a lower
shell, which supplies another before its donor dissipates. The finite,
varying-data solutions remain global and can approximate large prescribed
shears. This is an inverse transfer mechanism, not forward singularity.
Its precise generated-source and donor-timing estimates are useful for our
seed-supply problem; reversing its direction would be unjustified.

## Other circulating claims: read the exact statement and version

| Released item | What the checked version establishes or claims | Boundary for this project |
|---|---|---|
| [Hou–Wang–Yang, 2509.25116v2](https://arxiv.org/html/2509.25116v2) | Computer-assisted unforced NS nonuniqueness with localized L2 data retaining an origin singularity; a self-similar profile/eigenpair and stable/unstable decomposition. | The initial datum is not smooth at the origin. [Public interval code](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness) was inspected, not replayed; its README requires substantial resources. No smooth-data Clay conclusion. |
| [Cheskidov–Dai–Palasek, 2511.09556v2](https://arxiv.org/html/2511.09556v2) | A weak branch blows up as time approaches a joining time from the right and lies outside the stated energy spaces nearby. | The classical branch remains available. This is not forward breakdown of that classical solution from smooth data. |
| [Palasek, 2605.13827v1](https://arxiv.org/abs/2605.13827) | Blowup in an elementary shell model; actual-equation embedding remains separate. | The sign and transfer conditions must be realized by the full Leray-projected NS interaction, with every omitted term controlled. |
| [Shahmurov Part II, 2605.01873v2](https://arxiv.org/html/2605.01873v2) | Claims global continuation using a companion axisymmetric theorem. | The companion [2605.01875v4](https://arxiv.org/html/2605.01875v4), revised 2 September, is now *Hardy Criticality in Axisymmetric Swirl* and explicitly gives a restricted power-weight classification. Its current statement cannot be substituted for the earlier claimed global theorem. This is a dependency/version finding, not a review of the whole series. |
| [Ri, 2601.15685v1](https://arxiv.org/html/2601.15685v1) | Claims full global regularity, including an all-time bound for the inhomogeneous H^{s+1} time integral in (1.3). | The displayed estimate has the low-frequency obstruction below. No independent acceptance or formal certificate was located. |
| [Onodera's public record](https://zenodo.org/records/15605346) and [repository](https://github.com/hironodera/navier-stokes-global-regularity-proof) | A claimed constructive proof and finite diagnostic scripts. | The inspected concentration script evolves C'=K C^(3/2), which itself permits blowup; the driver repeatedly measures an initial Fourier array. Those checks do not certify the PDE. The entire manuscript was not audited. |

A useful fact in Shahmurov's current restricted paper is that stretching
cancellation at the chosen power weight coincides with loss of a uniform
Hardy gradient gap. Both effects must be checked before importing a weighted
energy argument. [Current Theorem 3.3](https://arxiv.org/html/2605.01875v4#S3.Thmthm3).

**Independent low-frequency check of Ri's printed estimate.** At viscosity
one choose a real solenoidal Schwartz field phi_r with Fourier support
r<=|xi|<=2r and L2 norm one. Its heat flow has

    integral_0^(r^-2) ||exp(t Delta)phi_r||_2^2 dt >= exp(-8)r^-2,
    ||phi_r||H^s^2 <= (1+4r^2)^s.

The claimed uniform quadratic estimate would pass to this heat flow by
linearizing NS about zero with initial data a phi_r and letting a tend to
zero at each fixed r and finite time. Letting r tend to zero contradicts
that estimate as printed. This elementary diagnosis was independently
rederived here; it is not a published verdict on the entire paper, and a
change to the norm notation alone would not validate its remaining proof.

## What changes in our next attempt

These are our proposed calculations, not results attributed to the authors:

1. Test the flat-core profile in the **full viscous equation**. Retain its
   exact pressure and self-advection cancellation; compute heat rounding,
   envelope terms and profile products. The existing sine/two-harmonic
   proof does not automatically cover a new periodic profile.
2. Extract a signed generated-seed estimate from actual NS, using Palasek's
   forward-time source calculation as a comparison. Specify the receiving
   phase, donor timing and cancellation control. Do not replace it with a
   newly inserted seed or reverse an inverse cascade.
3. Charge every mixed space/time derivative of the complete approximation
   defect in common physical coordinates. Under u=A q(ALt,Lx), the force
   multiplier is A²L, with L per spatial derivative and AL per time
   derivative. Our small rescaled L2 residual does not establish smooth
   all-order terminal forcing. A nonzero smooth force would define a
   separate forced result; the exact Q in our finite theorem is unforced.

The first comparison has already produced a [reviewed viscous affine-model calculation](../analysis/viscous-flat-core.md): exact heat-evolved waves, exponential interior rounding and an explicit localization-gauge term. Its finite-energy extension remains open.

The [current theorem](original-nonlinear-handover.md) now
supplies both original-time seeds for each finite family member. Extending this
to one smooth datum requires control of the outgoing geometry and the joint
depth/viscosity budget. That infinite-stage obligation remains unresolved.

## Version and formalization receipts

Upstream [fluid_lean](https://github.com/tristanbuckmaster/fluid_lean) was
at `d0124689230b58b4f86e7b90ac59de06404b3b6b`, committed at
2026-09-08 04:07:52 UTC. Hmbown/fluid_lean is its fork. The published
[tube lemmas](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/BoussinesqBlowup/Num/Tube.lean)
have explicit regularity, initial-enclosure and inward-boundary hypotheses.
They can support bounded ODE certificates; they do not certify an unrelated
PDE by invocation. Release metadata reports Lean 4.32.2 and pinned Mathlib.
The checked Euler metadata has author statement review; Boussinesq and
affinecore still flag statement review as outstanding. No fresh full
closure replay was performed. The [local formalization audit](fluid-lean-integration.md)
retains its exact build and axiom scope.

Retrieved PDF SHA-256 values, allowing future checks to detect replacement:

| Source | SHA-256 |
|---|---|
| Buckmaster statement | `8d7723941bcda2fa55c1e74faa6298e04c706d17ff8abd2ad01878039c621f9d` |
| Released Euler | `97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8` |
| Released Boussinesq | `895a628d1783bcb039374686f50b895b5f450f53b8ef8aa173523487a7a4a21b` |
| Released IPM | `b3ebdbb8d9a93dcca5f3b3f8796e63f7f28b48e0b0e258b909110a4b69c72a12` |
| Anima Euler candidate | `f0164c40fad09a646412acec95f7908ea6b2fd61d16b809954a4048665fb5f78` |

The Anima response had Last-Modified 2026-09-08 06:48:30 UTC. Its unfinished
certification and continuation conditions remained in that version. A source
hash records the artifact inspected, not its correctness.
