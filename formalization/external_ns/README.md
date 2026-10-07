# Local verification of the external forced Navier–Stokes targets

The two exported forced-breakdown targets in OpenAI's
[pinned release](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538)
built successfully from unchanged project sources with official Lean
4.34.0-rc2 on Darwin ARM. The build compiled all 580 project-local modules
in their import closure, using the matching Mathlib artifact cache. Both
targets report exactly `propext`, `Classical.choice` and `Quot.sound` as
axiom dependencies. The [receipt](receipt.json) records the source,
toolchain, dependency and artifact hashes, commands and outcomes.

This verifies a specific formal target and environment. It does not build
the companion Euler library or assert that every detail of the paper is
literally present in the exported theorem types. The
[statement audit](../../references/analysis/external-statement-audit.md)
compares those types with the reference definitions and explains the time
normalization and energy predicates.

A separate attempt to replay the complete imported constant environment
using bundled `leanchecker --fresh` did not finish within its 600-second
limit. That replay is **incomplete**; the time limit is not a discovered
proof error. It uses Lean's own kernel. The independently implemented
Comparator/Nanoda workflow has not been run on the Navier–Stokes theorems: its
trusted Landrun environment requires Linux, and a sandbox probe confirmed only
that the tool environment starts. Neither a native build nor the bundled
checker is a substitute for that workflow.

### Later replay attempt — 8 September 2026

A later attempt to replay the same complete imported constant environment with
bundled `leanchecker --fresh` was stopped after 1485.7388758659363 seconds
under severe host memory and swap pressure. It exited with status 143 and
produced an empty buffered log. This is an interrupted run: it is neither a
proof rejection nor a passing verification, and it does not convert the
600-second result above into a completed replay. The successful native target
build and the module-only local replays are separate results with their own
scopes.

## Reproduce the target build

Use a fresh checkout at the exact commit above, the official matching
toolchain, and its unchanged `lake-manifest.json`. The source's declared
Mathlib revision resolves to `85e3a25e006c35636f0e53b0e9296caca2685bc0`.
All dependency revisions are recorded in the receipt. Keep generated
objects, caches and the third-party checkout outside this repository.

After placing the matching toolchain's `bin` directory first on `PATH`,
run from that checkout:

```sh
lean --version
git rev-parse HEAD
lake exe cache get
lake --no-ansi build NavierStokes.ComparatorSolution
```

The final output must name both
`NavierStokes.Comparator.navier_stokes_breakdown_R3` and
`NavierStokes.Comparator.navier_stokes_breakdown_periodic`, print their
axioms, and report a successful build. Reading the source's existing
`#print axioms` commands is not equivalent to obtaining that output.

The recorded run set `MATHLIB_NO_CACHE_ON_UPDATE=1`, selected an external
directory with `MATHLIB_CACHE_DIR`, and used `LEAN_NUM_THREADS=6`. The
target build also set `LAKE_CACHE_DIR` to that external workspace.
It fetched the locked dependencies without changing their manifest.

To attempt the stronger bundled-kernel replay after the build:

```sh
lake env leanchecker --fresh --verbose NavierStokes.ComparatorSolution
```

Record the actual exit status and any imposed time limit. A timeout leaves
that replay incomplete even when the native build succeeded. For the
separate independent workflow, follow the
[upstream Comparator instructions](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/README.md)
in a fresh supported environment.

## Attribution and scope

The singularity construction and imported proof are OpenAI's work. This
project supplies the local verification record, source reading and
learning notes explanation. Its unforced ROOT and E-prime targets remain open.
The [local phase-covariance corollary](../phase_covariance/README.md)
is a separately scoped teaching result derived from one upstream lemma.
