# Checked algebra for the oblique-carrier cone

[NSEObliqueCone428.lean](NSEObliqueCone428.lean) contains an original,
restricted Lean proof. It represents two-dimensional matrices by their
coordinate actions on `ℝ × ℝ` and checks:

- The limiting matrix `[[0,-8/9],[-1/2,0]]` is conjugate to
  `diag(2/3,-2/3)`, with an explicit inverse coordinate transformation.
- If every perturbation entry has absolute value at most `1/12`, the
  slope expression points inward at `±1/2` by at least `23/48`.
- For `|z|≤1/2` and `Xplus≥0`, the positive component's algebraic growth
  expression is at least `(13/24) Xplus`.

These are conditional algebraic statements. This file does **not** prove
Gavrilov coefficient convergence, quotient differentiation, ODE cone
invariance, a periodic return-map result, Euler/NS wave approximation,
nonlinear amplification, an infinite cascade, ROOT, or `(E′)`.

## Verification and provenance

[receipt.json](receipt.json) records the successful compilation, source digest, axiom printout, and separate bundled
`leanchecker` replay of the module's declarations. Every printed result
depends only on `propext`, `Classical.choice`, and `Quot.sound`.
The stronger `leanchecker --fresh` replay of the entire imported closure
timed out at 60 seconds and is **not verified**. The bundled checker uses
Lean's kernel; it is not an independently implemented verifier.

Checked source SHA-256:
`b1c04ded30010b65de978338d484fe9170fea88202a1a91307bca55e4d88d1ab`.
Compiler: Lean `4.28.0`, commit
`7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`.
Mathlib: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`, matching the existing
`mathlib_bridge` pin. No binary, cache, or vendored library is included here.

The [fluid_lean audit](../../references/navier-stokes/fluid-lean-integration.md)
identified a separate generic ODE tube theorem in upstream commit
`d0124689230b58b4f86e7b90ac59de06404b3b6b`. **No upstream code is copied
or imported by this checked file.** The proposed upstream tube application
remains outside this formalized result: its calculus dependencies were
missing. Upstream's forced Euler/Boussinesq claims are not imported as NS
claims.

## Replay from the repository root

Use an already installed **actual** Lean 4.28.0 compiler, not an `elan`
shim, and the matching built `mathlib_bridge` dependency cache. The
following compiles only this file and keeps generated objects outside
the repository; it performs no download or dependency build.

```bash
nse_lean_bin=/absolute/path/to/lean-4.28.0/bin
"$nse_lean_bin/lean" --version
git -C mathlib_bridge/.lake/packages/mathlib rev-parse HEAD
nse_build=$(mktemp -d)
nse_packages="$PWD/mathlib_bridge/.lake/packages"
nse_lean_path="$nse_build"
for nse_lib in "$nse_packages"/*/.lake/build/lib/lean; do
  if [ -d "$nse_lib" ]; then nse_lean_path="$nse_lean_path:$nse_lib"; fi
done
(
  cd formalization/oblique_cone
  LEAN_PATH="$nse_lean_path" "$nse_lean_bin/lean" \
    -o "$nse_build/NSEObliqueCone428.olean" NSEObliqueCone428.lean
)
PATH="$nse_lean_bin:$PATH" LEAN_PATH="$nse_lean_path" \
  "$nse_lean_bin/leanchecker" --verbose NSEObliqueCone428
```

Check the printed compiler and Mathlib identities against the pins above.
Both checking commands must exit zero. Missing dependencies are an
incomplete replay, not a passed verification. 
