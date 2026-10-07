# fluid_lean, Tao's commentary, and the formalization boundary

**8 September 2026 UTC. ROOT and `(E′)` OPEN.** The imported project
addresses forced inviscid equations. Our new kernel check covers original
conditional cone algebra; it does not prove a fluid singularity.

## 1. What the supplied repository establishes

We audited [Hmbown/fluid_lean](https://github.com/Hmbown/fluid_lean) at
commit `d0124689230b58b4f86e7b90ac59de06404b3b6b`, a public fork of
Tristan Buckmaster's repository. Its statements concern:

| Project | Equation and domain | Conclusion stated by its solution module |
|---|---|---|
| `euler-blowup` | Forced inviscid Euler on R³ | Finite-time unbounded vorticity with smooth forcing |
| `boussinesq-blowup` | Forced inviscid Boussinesq on R² | Finite-time gradient/vorticity blow-up with smooth forces |
| `affinecore` | Forced inviscid Boussinesq on R² | A construction with odd initial temperature and zero initial velocity |

The precise definitions and theorem statements are in the pinned
[Euler challenge](https://github.com/Hmbown/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/Challenge.lean),
[Boussinesq challenge](https://github.com/Hmbown/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/Challenge.lean),
and their `Solution.lean` modules. The Euler definition has neither a
viscous term nor a requirement that forcing vanish. Transferring this
construction to unforced viscous NS requires a new mathematical argument.

A comment/string-aware scan of 3,748 Lean source files found only three
executable `sorry` tokens, one in each intentional challenge placeholder.
The solution modules use their proved libraries. This source audit is
not a kernel replay of those libraries. Their pinned toolchain is Lean
4.32.2 with Mathlib commit `81a5d257c8e410db227a6665ed08f64fea08e997`.
Upstream author/comparator review labels differ between the projects;
none has been promoted here to independently reproduced verification.

## 2. The screenshot in its original context

The supplied image is a crop of
[Terence Tao's second post](https://mathstodon.xyz/@tao/117233528517340774),
posted 8 September 2026 at 04:28 UTC. Its
[preceding post](https://mathstodon.xyz/@tao/117233527638291447)
identifies the Alpöge–Buckmaster work and its use of localized high-frequency
perturbations. The original public text was verified through Mathstodon's
status API, including the portion below the screenshot's crop.

Tao describes low-frequency flows amplifying localized high-frequency
corrections, followed by successive transfers. He discusses a simple
amplitude–frequency ODE for the Boussinesq ansatz and substantial work to
control spatial cutoffs. Possible extension to Navier–Stokes and removal
of forcing are prospective directions with enormous technical difficulties.
His remarks are not an announcement of an unforced NS proof or an
endorsement of this repository. He also emphasizes understanding the
mechanism and making its reasoning teachable.

That advice informs this textbook's order: show the target equation,
derive the simplified mechanism, identify its exact correspondence to the
full equation, then account for every approximation error and feedback
term. The screenshot is contextual evidence, not a mathematical premise.

## 3. Concrete reuse: a small certificate before a large import

The generic numerical layer contains useful tools independent of the
forced-fluid construction:

- [`Num/Tube.lean`](https://github.com/Hmbown/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/EulerBlowup/Num/Tube.lean): inward-face ODE invariance and chaining.
- [`Num/Kernel.lean`](https://github.com/Hmbown/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/EulerBlowup/Num/Kernel.lean): outward-rounded interval arithmetic.
- [`Num/Expr.lean`](https://github.com/Hmbown/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/EulerBlowup/Num/Expr.lean) and [`Num/Check.lean`](https://github.com/Hmbown/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/EulerBlowup/Num/Check.lean): expression enclosures and sound polynomial-tube certificates.

In particular, the checker's `FieldSem` obligation separates an executable
coefficient enclosure from proof that it represents the actual real
coefficient. That correspondence is essential for any application to the
Gavrilov profile. A successful Boolean calculation cannot supply it.
Any future copied source must retain its Apache-2.0 license and notices.
No upstream source is vendored in the present cone certificate.

## 4. What has actually passed Lean

The original [cone source](../../formalization/oblique_cone/NSEObliqueCone428.lean)
and [verification receipt](../../formalization/oblique_cone/receipt.json)
certify the following part of the
[oblique-carrier argument](gavrilov-oblique.md):

1. The limiting matrix `B₀ = [[0,−8/9],[−1/2,0]]` is conjugate, through
   an explicitly invertible basis, to `diag(2/3,−2/3)`.
2. If every transformed coefficient error has absolute value at most
   `1/12`, the quotient ODE points inward on slopes `±1/2` with margins
   at least `23/48`.
3. In this cone its positive component has algebraic growth coefficient
   at least `13/24`, with all sign and coefficient hypotheses explicit.

Official Lean **4.28.0** compiled this source against the existing
Mathlib cache pinned to `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
The printed dependencies of the five principal declarations are exactly
`propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx`.
The bundled `leanchecker` also replayed the new module's declarations
successfully in their imported environment. This is a second check using
Lean's bundled checker, not a separately implemented verifier.

A stronger fresh replay of the full imported closure exceeded its
60-second bound and was not verified. An attempted adaptation of the
upstream tube proof stopped on missing calculus objects; its dependency
closure requires 1,064 additional Mathlib objects. We did not rebuild it.
This records an environment limitation, not a flaw in that theorem.

The checked algebra does **not** formalize the Gavrilov coefficient
convergence, ODE invariance/existence, the return-map fixed point,
finite-wavelength approximation, or NS dynamics. The analytic theorem
retains its written-proof standing; its Lean coverage is explicitly partial.
See [replay instructions](../../formalization/oblique_cone/README.md).

## 5. From the checked algebra to the next transfer

The [viscous-packet note](viscous-packet.md) now establishes
a finite supplied-seed amplification estimate in smooth, unforced NS.
It fixes one Gavrilov profile before taking the concentration limit,
includes pressure and localization errors, and proves strong continuation
separately. This is a written analytic proof with exact algebra controls;
the PDE argument has not been formalized in Lean.

That small-seed theorem also excludes the original absolute activation
target throughout its window. A large gain ratio does not make its seed
large enough to take over the background strain. The
[handover obstruction](wave-handover.md) identifies both
the generic error growth rate and the normal mean velocity generated by
pressure. The subsequent [log-log handover proof](loglog-handover.md)
now controls those corrections and establishes smooth finite strain
handover, with a separate H12 continuation argument. Its analytic PDE
steps remain outside the current Lean certificate.

The next mathematical question follows the [outgoing-wave linearized result](outgoing-wave.md)
with nonlinear receiving-seed control and original-time compatibility.
That finer-wave theorem is also a written analytic result, outside the
present Lean coverage. Infinite iteration still requires one smooth
initial datum, one viscosity and a uniform depth/error budget.
The [textbook](../../textbook/README.md) teaches the known transfers and their
remaining obligations; it does not present an unfinished chain as a solution.
