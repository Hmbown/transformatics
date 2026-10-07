# From a calculation to a claim

A research claim has mathematical content, an origin, and a verification history. “The computation passed” is incomplete until we know what was computed, with what error, and what statement it can support.

## The working vocabulary

| Label | What it licenses |
|---|---|
| HEURISTIC | A proposed mechanism with a falsifiable prediction. |
| NUMERICAL | A recorded observation at the measured resolution and parameter values. |
| VERIFIED | Independent computational paths agree at the correct object. |
| CERTIFIED | A rigorous interval or exact verification supports the specified statement. |
| PROVED | A written mathematical proof under explicit hypotheses. The register states separately whether any review or formal check is recorded; a written proof is not by itself external expert acceptance. |
| IMPORTED | An externally authored result used with attribution and a source record; this does not assert a local formal replay. |
| KERNEL-CHECKED | The stated formal declarations passed the recorded kernel checks, with dependencies and coverage explicit. |
| OPEN | The required theorem has not been established. |
| DEAD / WITHDRAWN | A refuted route or invalid claim, preserved with its correction. |

These labels are a compact display vocabulary. They describe different axes:
where a theorem came from is separate from whether it was proved or formally
checked. An imported theorem can also have a kernel-checked proof. The
machine-readable register therefore records `provenance`, `proof_status`,
`review`, and `formalization` separately, alongside the legacy display label.
Read the exact statement and the verification scope together.

AI review is not external expert acceptance. The review entries document the checking process; formal receipts state the separate scope of machine verification.

The repository's historical working documents use further intermediate labels; [the discipline document](../../references/mathematical-background.md) defines one older version of that vocabulary. Those historical labels are not the current certification standard, and the register's evidence fields govern present standing. The labels are not interchangeable. A symbolic regression test can protect an algebraic identity while leaving an analytic theorem dependent on its written proof. A formalization claim needs the actual theorem, build, and axiom audit. The [archive reading guide](../../docs/sources.md) explains how to read the dated research record.

## The cap-vacuity lesson

An earlier route assigned prices to completed growth intervals and proposed that their sum diverge. But the same route's estimates, together with disjointness and the finite energy budget, already bounded that sum for every admissible finite-energy trajectory. Asking for divergence had not supplied a new dynamical estimate. The advertised route was retired.

The conditional implication could remain logically valid while the proposed strategy supplied no progress. This is why checking the truth of each implication is not enough: one must also ask whether the new hypothesis is attainable and whether proving it would merely repackage the original problem.

The latest correction governs older notes that call averaged noncollapse open. [The cap audit](../../references/navier-stokes/qgso-cap-vacuity.md) preserves the exact argument. **Do not revive rung-average noncollapse as a regularity target.**

## The momentum-residual lesson

A spatially realizable path can satisfy selected global energy and strain balances without solving Navier–Stokes. For a divergence-free proposed velocity $U$, inspect the full projected residual

$$
R_U=\partial_tU-\nu\Delta U+\mathbb P\nabla\cdot(U\otimes U).
$$

Vanishing pairings of $R_U$ against a few test fields do not imply $R_U=0$. A small residual also needs a stability estimate in a norm strong enough to protect the claimed observable. An $L^2$ error alone need not protect a strain maximum.

## Exercise 1 · Three orthogonal tests

Let $r$ be an element of an infinite-dimensional Hilbert space. If its inner products with three chosen vectors vanish, must $r=0$? Explain why this is relevant to a proposed fluid construction.

<details><summary>Solution</summary>
No. Any nonzero vector in the orthogonal complement of their finite-dimensional span is a counterexample. Matching three integrated balances tests only selected components of a PDE residual. A full momentum equation, or an appropriate complete weak formulation, is still required.
</details>

Source: [Kinematic budget obstruction](../../references/navier-stokes/qgso-kinematic-budget-obstruction.md) and [route classification](../../references/navier-stokes/route-classification.md).


## What a formal proof establishes

A formal proof checks a proposition expressed in a formal language. To use it,
we must understand that proposition. Suppose a file proves

$$
(\forall t<T,\ \|u(t)\|_\infty\le C)\quad\Longrightarrow\quad
\text{a continuation property}.
$$

That may be a useful theorem. It has not supplied the bound on the left.
A successful build cannot remove a hypothesis that remains in the statement.
Likewise, a proof about a finite-dimensional discretization does not become a
proof about all smooth fluid fields merely because both variables are named
`velocity`.

Three readings complement one another. First, read the mathematical statement:
its quantifiers, spaces, equation and conclusion. Second, read the formal
declaration and the definitions behind its notation. Third, inspect the
verification record: source revision, toolchain, dependencies, axiom output
and the declarations actually checked. Agreement among these three readings
is what makes the formal result useful to a mathematical reader.

For an introduction to the underlying language, see
[*Theorem Proving in Lean 4*](https://lean-lang.org/theorem_proving_in_lean4/).
The examples here concern interpretation of evidence, not a substitute for
learning the proof language.

## Formalization records with different scopes

This project contains a [small checked cone calculation](../../formalization/oblique_cone/README.md).
It diagonalizes a specified two-dimensional matrix and proves inequalities
for a perturbed slope expression. The recorded compiler is Lean 4.28.0.
The associated [receipt](../../formalization/oblique_cone/receipt.json)
records successful compilation and a replay of that module's declarations.
A stronger fresh replay of the entire imported closure timed out and is
recorded as incomplete. These distinctions are part of the result.

The calculation is relevant to [returning covectors](oblique.md). To reach a
fluid theorem, one would also need the profile geometry, differential
identities, ODE invariance and PDE approximation. Those assertions are not
hidden inside the two-dimensional algebra. A small verified lemma remains
valuable precisely because its contribution can be identified.

OpenAI's September release provides a different record: an external paper and
an accompanying repository reporting formalizations of the main forced
Navier–Stokes and unforced Euler results. Our
[source assessment](../../references/navier-stokes/openai-result-bridge.md)
identifies its pinned declarations and reported Lean 4.34.0-rc2 toolchain.
We subsequently built its exact Navier–Stokes target from unchanged sources:
all 580 project-local dependency modules compiled, and both exported
theorems reported only the three usual axioms listed in the
[verification record](../../formalization/external_ns/README.md).
That record separates compilation with cached Mathlib imports, the stronger
bundled-kernel replay, which remains incomplete: an earlier attempt hit a
ten-minute limit, and a later attempt was stopped after about 24.8 minutes
under host memory and swap pressure (exit 143, empty buffered log). Neither
outcome is a proof rejection or a passing verification. The record also notes
that the independently implemented Comparator/Nanoda check has not been run
here. The textbook retains **IMPORTED** to record
authorship; the separate formalization field records what was checked locally.

A third record concerns the
[phase-covariance corollary](../../formalization/phase_covariance/README.md)
used in [making a new construction](new-constructions.md). Its Lean proof
changes one field of the upstream wave data and proves that two leading
stress components are preserved. Compilation and a replay of the local
module passed. It gives no regularity or transport estimate for an arbitrary
new phase. The chapter's explicit shear calculation shows why that missing
information matters to the differential equation.

A changed result deserves a changed record. Earlier notes said the reported
OpenAI proof was private and unavailable. The publication supersedes that
availability statement. The older notes remain useful as dated research
history, but they cannot describe the current source status.

## Exercise 2 · Quantifiers inside a certificate

A formal declaration proves that for every smooth datum $u_0$ there exists
$T(u_0)>0$ and a smooth solution on $[0,T(u_0)]$. Does this establish a
solution on every finite interval? What additional information would you seek?

<details markdown="1"><summary>Solution</summary>

No. The existence time may depend on norms that grow during the evolution.
To continue indefinitely, one needs a continuation argument and estimates
preventing its required norms from becoming unbounded at finite time. A
uniform positive lower bound on repeated local existence intervals under
controlled hypotheses would be one possible mechanism.

</details>

## Exercise 3 · A conditional algebraic lemma

Suppose a checked file proves $b\ge 13a/24$ under hypotheses
$a\ge0$ and $|z|\le1/2$. Another argument proposes to use it along a
trajectory $z(t)$. Which new obligation appears?

<details markdown="1"><summary>Solution</summary>

The application must prove that the trajectory remains in $|z(t)|\le1/2$
on the interval of interest and that the variables satisfy the algebraic
identifications. An inward boundary inequality can help prove invariance,
but the ODE existence and boundary-crossing argument must still be supplied.

</details>

## An honest account of progress

A research program can become more informative while its main problem remains
open. A counterexample may eliminate an attractive false estimate. A corrected
finite theorem may identify the exact norm that a future iteration must
preserve. Both improve the next attempt, even when neither closes the problem.

In this collaboration, finite wave amplification, pressure-corrected transfer
and increasing-depth approximation became useful local results. What remained
was a compatible construction for one evolution through its limiting time.
The external proof supplies a separately authored construction with additional
geometry and all-order estimates. [The bridge chapter](published-proof.md)
identifies the relationship calculation by calculation.

There is no defensible percentage for how close this project was. Counting
lemmas gives a long elementary calculation and a missing decisive idea the
same weight. A better progress report states the strongest completed theorem,
the first missing implication, and what evidence would discharge it. That
practice is useful to both a human collaborator and a model continuing the work.
