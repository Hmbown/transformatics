# Phase covariance corollary

This small Lean source states the phase-replacement corollary of the
released construction's exact leading covariance theorem. It changes only
the phase field of each signed slot's data, proves that the actual native
pulse matrix is unchanged, and applies the original theorem with all of its
geometric, partition, cone and scale hypotheses retained.

Dependency: [OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The imported declaration is
[PartitionedCovariance.physical_primary_covariance](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PartitionedCovariance.lean#L947).

**Local verification passed:** the corollary in namespace
Transformatics.PhaseCovariance compiled with the pinned project's official
Lean 4.34.0-rc2 toolchain. The bundled checker then replayed the
PhaseCovariance module successfully. The printed axiom dependencies were
only propext, Classical.choice and Quot.sound. The
[verification receipt](receipt.json) records the exact source and tool
hashes, versions, outputs and commands.

This was a module-only replay against previously built imported modules.
It was not a fresh replay of the imported proof or the full external
Navier–Stokes construction.

No dependency checkout, toolchain or compiled artifact is stored here.
To reproduce it after building the pinned dependency, use that project's
exact toolchain and lockfile. Set LEAN_NUM_THREADS to 1, put the official
toolchain's bin directory first in PATH, and set LEAN_PATH to the source's
.lake/build/lib/lean and each package's .lake/build/lib/lean. Compile
PhaseCovariance.lean with an output path in a separate local-corollary
directory. Add that directory to LEAN_PATH, then run the bundled
leanchecker with arguments --verbose PhaseCovariance. The receipt records
this precise module-only mode; do not substitute a full-import replay.

The result concerns two leading radial–tangential covariance components.
It supplies no regularity of arbitrary replacement phases, no estimate on
material derivatives, and no replacement theorem for the full
curl-corrected Navier–Stokes field. The scope and required next estimate
are explained in the
[source extraction note](../../references/analysis/external-component-extraction.md).

The corollary and its short proof were written for this project from the
published theorem. The pulse construction and imported analytic result
belong to their upstream authors. No independent priority is claimed for
phase invariance of an angular average.
