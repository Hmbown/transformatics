# Transformatics: finite change, evolution, and transfer (v7)

> **Archive context (added 8 September 2026).** This is a historical method
> document. Its status vocabulary — for example, "PROVED" as a short proof a
> referee could check — predates the current evidence fields and is not the
> current certification standard. Present standing is in
> [notes/claims.md](../notes/claims.md), [STATUS.md](../docs/STATUS.md) and the
> [archive reading guide](../docs/sources.md).

These learning notes and research examples were developed
by Hunter Bown in collaboration with language models. Its organizing viewpoint
brings established tools to a connected
problem: **how finite changes act on observable quantities, and under what
conditions conclusions can pass between descriptions of an evolving system.**

The motivating question grew out of Hunter's wish to understand finite change
beyond the usual presentation of calculus. The notes develop that question
through mathematics: express a construction, identify the assumptions that make
it work, and determine what can be changed while preserving its conclusion.
Its longer-term research aim is to make new constructions easier to find and
prove. That usefulness must be assessed through particular examples and
arguments. The [capstone](../notes/chapters/new-constructions.md) starts with a
standard perturbation estimate, develops a worked replacement example, and
states a further fluid question.

## The objects

A transfer problem starts with states \(x\in X\), evolution maps
\(T_{t,s}\), observations \(f:X\to\mathbb R\), and a representation
\(R:X\to Y\). The model evolves represented states by \(S_{t,s}\).
Every map comes with its domain, time interval and regularity assumptions.
Distances or norms specify the meaning of an approximation.

The question is whether the square commutes:

\[
R(T_{t,s}x)=S_{t,s}(Rx).
\]

For a normed model space, its defect is

\[
D_{t,s}(x)=R(T_{t,s}x)-S_{t,s}(Rx).
\]

An exact transfer has zero defect. An approximate transfer includes a bound on
this defect and a stability estimate for its propagation. A representation
that discards information need not admit any exact autonomous evolution.
The [transfer-systems chapter](../notes/chapters/transfer-systems.md)
proves the precise fiber criterion and gives a two-dimensional counterexample.

## The operations and their theorems

For a map \(T:X\to X\), pull back an observable by
\(U_Tf=f\circ T\), and define its finite difference
\(\Delta_Tf=U_Tf-f\). The finite product rule is

\[
\Delta_T(fg)=f\Delta_Tg+g\Delta_Tf+\Delta_Tf\Delta_Tg.
\]

Pullbacks reverse the order of state composition:
\(U_TU_S=U_{S\circ T}\). For a smooth flow \(\Phi_t\) with vector
field \(v\), differentiating gives \(L_vf=v\cdot\nabla f\), while
integration along the trajectory recovers the finite change. These are
classical identities; their proofs form the first two lessons.

To compose approximations, suppose the next model map has Lipschitz constant
\(L_j\) and its one-step defect has norm at most \(\delta_j\).
The accumulated error obeys

\[
e_{j+1}\le L_je_j+\delta_j.
\]

Repeated substitution gives an explicit weighted sum. A small defect may
produce a large error when the intervening maps amplify it. For continuous
evolution, variation of constants and energy estimates play the corresponding
role. A residual becomes useful only through such an estimate.

Finally, a change of length or amplitude changes norms by different powers.
For \(v(x)=A\phi(x/\ell)\) in dimension \(d\),
\(\|v\|_p=|A|\ell^{d/p}\|\phi\|_p\), whereas each spatial
derivative costs another factor \(\ell^{-1}\). The course repeatedly
uses this distinction to separate velocity, energy and gradient conclusions.

## What the reader learns to do

A reader completing the foundations should be able to calculate a finite
change, recover its infinitesimal generator, test whether a reduced state
admits exact evolution, propagate a representation error, and convert the
result into the norm of a physical observable. The later chapters use those
skills to study nonlinear frequency creation, pressure, diffusion, residual
correction and limits of repeated constructions.

The endpoint is an independent calculation. A satisfactory solution states
its hypotheses, derives its conclusion and explains how the conclusion changes
when one hypothesis is removed. The [curriculum](course-outline.md)
and [practice workshop](../notes/chapters/practice.md) supply exercises and
cumulative assessments. The notes' glossary, source chapters and course manifest
make the same mathematical structure accessible to automated readers.

## Relationship to established mathematics

The course draws on finite differences and operator theory for pullbacks,
dynamical systems for flows and factors, numerical analysis for stability and
consistency, and PDE analysis for localization and energy methods. These
connections are mathematical dependencies, not endorsements. The
[reading guide](../notes/chapters/references.md) links author, university and
publisher sources and explains where each belongs in the course.

One legacy API uses the spelling `resolvant` for a finite difference. This is
not the operator-theoretic resolvent \((zI-A)^{-1}\); the notes use
\(\Delta_T\) to keep the two objects distinct.

## Navier–Stokes and these notes

The collaboration pursued the Navier–Stokes problem and produced finite,
restricted constructions, diagnostic examples and corrected failed routes.
It did not complete its own singularity or global regularity proof. OpenAI's
8 September 2026 paper supplies a separately authored forced breakdown result;
the [bridge record](navier-stokes/openai-result-bridge.md) identifies the
inspected theorem, source version, formalization claims and reading scope.
FORCED-D is now **IMPORTED** in this project's register. Unforced ROOT and
E-prime remain **OPEN**.

The notes use the external result to ask a productive further question:
which operations in a difficult construction can be taught through simpler
examples without losing their hypotheses? Our local results offer several
such examples. They are preparation for reading the external construction,
not a derivation of it or a claim of priority. The
[collaboration record](../notes/chapters/credits.md) separates Hunter's account,
documented model labels and external scholarship.

## Historical research handbook (v5, preserved)

The remainder records the earlier methodology and its correction history.
Its definition of Transformatics as a methodology is superseded by the
mathematical curriculum above. Historical mission and route statements
must be read with the later canonical corrections. In particular, the
earlier assertion of a May 2026 NS proof was false and remains retracted.

**Historical v5 checkpoint, 8 September 2026:** section 10 adds precise transfer
contracts and partial-certificate coverage. The current research follows
the [smooth supplied-seed handover](navier-stokes/loglog-handover.md)
and the [outgoing-wave linearized result](navier-stokes/outgoing-wave.md)
toward a compatible nonlinear receiving seed and an iteration budget. ROOT and `(E′)` remain OPEN. The July case
studies and mission snapshot below are historical; the
[canonical status](../docs/STATUS.md) governs their present standing.

> *Mathematics done as an adversarial experimental science — but with the
> dials turned toward the goal. Structures are discovered computationally,
> claims are attacked before they are believed, and the mission is to resolve
> the Navier–Stokes regularity problem. The rules below are the operating
> principles that keep our results trustworthy. They are defaults that serve
> the mission, not a straightjacket that replaces it.*

**Rewritten 2026-07-01 (v4).** v1 claimed Navier–Stokes regularity was
"proved May 2026." It was not. v2 (2026-06-10) over-corrected into a
compliance manual. v3 (2026-06-17) rebalanced: every safeguard kept, reframed
as principles an ambitious agent uses to move fast and stay credible. **v4
adds the principles earned by the 2026-07-01 sessions** — a day that produced
two proved lemmas, two certified bounds, one killed conjecture-form, and two
corrections of our own prior numbers — and makes explicit what v3 only
gestured at: *the discipline is a teaching method.* Its case studies are how
a new agent (or human) learns to do this work at all.

Two failure modes, equally fatal:

- **Overclaiming** — the documented disease (v1). Calling something proved
  before it is.
- **Undercommitting** — the v2 disease. An agent so afraid of a wrong label
  that it never pursues a hard line, never states a conjecture, never commits
  to a decisive experiment. A research program that ships no bold claims ships
  nothing.

The principles below are how you avoid both.

---

## 1. What transformatics is

Transformatics is a methodology for attacking hard analysis problems
(flagship target: **3D Navier–Stokes regularity**) with a tight loop:

1. **Computational discovery** — optimizers, DNS, and adversarial searches
   find candidate structures and counterexamples.
2. **Structure identification** — discovered patterns are matched to
   classical mathematical objects, importing decades of theory at once.
3. **Adversarial verification** — every load-bearing claim is attacked by an
   independent code path and (for decisive moments) a registered prediction.
4. **Certification and theorem extraction** — surviving claims are upgraded
   along an evidence ladder toward certified numerics or short proofs.

The loop is not a pipeline; it cycles. Be bold in steps 1–2 (explore widely,
follow intuition, try strange approaches). Be honest in steps 3–4 (attack what
you found before you believe it). **The goal is to resolve the problem — the
discipline is what makes a resolution credible, not a substitute for one.**

### Shadow Math (operational, repaired)

Shadow Math is a discovery operator inside this loop, not an evidence class.
Its original "superposition" slogan was partially retracted after it licensed
assertion without proof.  The surviving method is concrete backward
propagation across the obstruction lattice: fuse constraints that are usually
studied separately, write the resulting candidate observable explicitly, and
try to kill it.

One named operator is **Counterfactual Defect Pullback**: construct the
smallest nearby or even impossible mathematical world in which the desired
theorem is easy; prove or label that shadow result; subtract the shadow law
from the real equation to obtain an exact, computable defect; then optimize
the real equations adversarially against that defect.  If the imagined world
does not produce a formula and a falsifier, it is a story, not Shadow Math.

---

## 2. Latitude (read this before the principles)

You are encouraged to:

- **Speculate.** State conjectures, even unproven ones — clearly labeled.
  A labeled conjecture ("HEURISTIC: I believe X because Y") is a legitimate
  research artifact. An unlabeled one masquerading as a theorem is not.
- **Pursue weird lines.** Shadow math, beampatterns, Riesz decomposition,
  Beurling transforms, winding numbers, quantum level-repulsion analogies —
  if naming a classical object imports a useful tool, use it, even if the
  analogy is imperfect. The worst outcome is an obituary (obituaries are half
  the project's value).
- **Move before you're certain.** Most probes are exploratory and do *not*
  require a registered prediction. Register only when the run is **decisive**
  — i.e., you will act differently depending on the outcome (principle 3).
- **Commit to a line.** When you have a real shot at a theorem or a
  counterexample, go for it. Undercommitting kills the program faster than a
  retracted lemma.

What you are *not* licensed to do: report a result that isn't there, label a
guess as proved, or skip verification on a load-bearing claim. That line is
non-negotiable — everything else is judgment.

---

## 3. The operating principles

Principles 1–10 are v3's, unchanged in substance. Principles 11–16 were
earned 2026-07-01; each carries its receipt. Every principle doubles as a
teaching case: *the receipt is the lesson plan.*

1. **Evaluate at the right object.** If a conjecture is about maximizers,
   measure at the *actual* maximizer — never a proxy point. *(One retraction,
   one false direction, from measuring r at the origin while the true max
   moved away.)*
2. **Two independent code paths for headline numbers.** Every number you'll
   act on or publish gets a reimplementation (FFT vs direct sum; closed form
   vs grid; DE vs multistart-SLSQP). Exploration can be single-path;
   load-bearing claims cannot.
3. **Register predictions before decisive runs.** When a run will change what
   you do next, commit the prediction to a doc *first*. A confirmed registered
   prediction is worth ten post-hoc fits. *(Only decisive runs — the point is
   to beat confirmation bias, not to file paperwork.)*
4. **Name the classical object.** The 2D VSA problem sat unidentified until
   `Q = ½·Beurling(T)` was recognized. The δ-witness sat as a mystery for one
   session until von Neumann–Wigner (codimension 2), Rellich (analytic
   branches), and Landau–Zener (transversal passage) were named — each import
   converted a vague difficulty into a precise sub-problem. Always ask: *what
   known operator/structure/phenomenon is this?* (A name can be wrong — the
   sidelobe reading of the beampattern was falsified by a registered
   prediction. That's the system working.)
5. **Adversarial optimization is a proof assistant.** An optimizer that slams
   into your bound *exactly* is telling you the bound is sharp. One that beats
   it is telling you the proof is wrong. Both are gold.
6. **Constants must survive the limit.** A "universal" constant that depends
   on the solution's own norms degenerates at blowup scale and proves nothing.
   *(Gap 1 audit: κ = 1/55 was an empirical fit in theorem clothing.)*
7. **Estimates have validity domains.** Calderón–Zygmund maps L∞→BMO, not
   L∞→L∞. Using an estimate one space past its domain is how plausible chains
   rot. Check the domain of every imported inequality.
8. **Pin headline witnesses immutably.** A record witness gets an immutable
   copy + a regression test, or it silently degrades.
9. **Formalization has an exact scope.** A claim is machine-checked only
   when its actual statement and proof typecheck with an audited dependency
   closure and no placeholders or unapproved custom axioms. Lean's standard
   foundational axioms must be reported, not confused with assumed PDE
   conclusions. A checked sublemma does not certify its application.
10. **Write the obituary.** Killed routes get one crisp doc: the exact
    estimate that failed and why. Dead ends, documented well, are the
    curriculum. *(Do not delete failed work. Banner it.)*

11. **Make the feasible set exact before you optimize on it.** A tolerance in
    a constraint is a subsidy the optimizer will always collect. If the
    constraint can be collapsed to an algebraic criterion, do that *first* —
    it is usually a provable lemma in its own right. *(Receipt: the 2-mode
    "ceiling" 1.1105 was measured with a grid check at tol=0.02; the pinned
    witness actually violated the exact criterion γ ≥ 0 by γ = −0.708. The
    box-vertex lemma collapsed the semi-infinite constraint to one polynomial
    inequality; the true ceiling is 1.0960, and the lemma then generalized —
    cut-polytope conditions — to unlock the 3-mode family.)*
12. **A solver's "optimal" is a proposal, not a certificate.** Floating-point
    SDP/LP output becomes a certificate only after an exact verification
    layer: treat every float as the rational it is, prove the Gram matrices
    PSD by rational LDL, bound the residual exactly, absorb it into the
    constant. This costs seconds and upgrades CERTIFIED-NUMERICAL to
    CERTIFIED. *(Receipt: `ceiling3d_2mode_sos_verify.py` — deg-4 residual
    2.3e-4, absorbed; the 3-mode pipeline verified same-day at 1.9e-7.)*
13. **Before declaring a quantity singular, change coordinates.** A blowup in
    a *labeled/sorted/gauge-fixed* quantity may be a coordinate artifact.
    Check the analytic continuation, the unsorted branches, the frame that
    moves with the object. *(Receipt: the sorted-eigenframe rotation W₂₃ = ∞
    at the δ-witness is a label swap; the analytic-frame rotation through the
    same crossing is exactly π/2. One session earlier this "infinity" looked
    like the death of the chain; in the right frame it is a bounded winding.)*
14. **When a pointwise bound dies, ask what the argument actually consumes.**
    Counterexamples often kill a *stronger* statement than the proof needs.
    Re-derive the requirement in integrated/averaged/a.e. form before
    declaring the route dead — then instrument the weaker form and measure it.
    *(Receipt: the kinematic δ-weighted bound is FALSE with an exact witness,
    but the chain consumes W₂₃ through Gronwall integrals; the integrated
    form is a winding number, the winding is measurably bounded in DNS, and
    the live conjecture — PROOF_STATE X.5 — survived its own counterexample.)*
15. **Evolve your counterexample.** A kinematic witness is also initial data.
    Running the dynamics from the engineered worst case is the cheapest
    decisive experiment available: either the evolution sustains the danger
    (real threat) or actively destroys it (mechanism discovered). *(Receipt:
    NS repelled the δ-witness instantly — level repulsion, numerator
    co-vanishing — and a 1%-perturbed run showed one finite spike then
    monotone escape. Four trajectories now support the dynamical form.)*
16. **A search maximum is a lower bound on the lower bound.** Adversarial
    sampling reports what *it found*, not the sup. Structured families with
    exact feasibility criteria are stronger lower-bound machines than
    black-box search — and when a family beats your old "ceiling," the old
    trend was optimizer bias. *(Receipt, twice: the 2D v3-ascent increments
    understated the VSA growth; then the 3-mode family hit 1.6536, above the
    adversarial-search 1.38 that the "no N-growth" triangulation had cited.
    The correction is on record; the burden moved to certified upper bounds.)*

Two more habits, smaller but bought with real time:

- **Read your own red flags.** The violated constraint was *in the pinned
  JSON* (`origin_frac: 0.9805`) for ten days. Artifacts should assert their
  invariants (tests), not merely record them (fields).
- **Prove the local part, isolate the nonlocal core, instrument what's left.**
  Decompose a hard conjecture until everything local is a sympy-verified
  lemma and the open content is one named, measurable object. *(Receipt: the
  Winding Conjecture reduced to the rotation rate of a single nonlocal
  pressure-anisotropy angle; everything else — direction freezing, strain
  parallelism, viscous vanishing — is proved harmless.)*

---

## 4. Evidence vocabulary (a language, not a gate)

Every claim carries a label — the label is a *vocabulary for honesty*, not a
bureaucratic hoop. Promotion is encouraged when earned; demotion is mandatory
when an audit fails.

- **HEURISTIC** — argument sketch, plausible. Must predict something testable.
- **NUMERICAL** — observed in experiments. Replayable script + artifact.
- **PREDICTED→CONFIRMED** — registered before the decisive run landed.
- **VERIFIED** — two independent code paths agree, at the correct object.
- **VERIFIED-by-triangulation** — several independent *lines of evidence*
  agree. *(v4 caveat, learned the hard way: triangulation lines must not
  share a bias. Three search-based lines all understated the product-bound
  ceiling — search bias is a common mode. At least one line must be an upper
  bound or an exact construction.)*
- **CERTIFIED-NUMERICAL** — a rigorous *format* (SOS/interval/dual
  certificate) executed in floating point; the certificate exists but has
  not been exactly verified.
- **CERTIFIED** — interval arithmetic, layered rigorous majorants, or a
  float certificate passed through an exact-rational verification layer
  (principle 12).
- **PROVED** — short, self-contained proof a referee could check.
- **DEAD / WITHDRAWN** — refuted or artifact, with a replayable refutation.

The jump from NUMERICAL to PROVED is the whole game. Don't stall at NUMERICAL
out of caution — push claims up the ladder by attacking them. But don't print
PROVED until a proof exists and a sharpness probe has tried to break it.

---

## 5. The certification ladder (numerics → rigor)

For "x* is a global maximizer" / "r = value" claims, weakest to strongest:

1. dense grid + Newton refinement of all near-peak competitors;
2. independent non-FFT re-evaluation; near-origin dense scans; Hessian
   spectrum at the candidate;
3. strict-margin variants (back the candidate off a boundary-riding tie);
4. **exact feasibility criteria** where derivable (principle 11) — replaces
   grid feasibility checks entirely for structured families;
5. **layered certificates** — interval concavity on an inner disk + nested
   fine Taylor majorants on annuli + global FFT majorant; *and the
   competitor-aware variant:* local-Hessian bounds at the actual far-field
   peaks (closes ~150× certificate-slack gaps for near-flat fields);
6. **SOS/Putinar certificates with exact-rational verification** (the
   2026-07-01 pipeline): lift to a polynomial formulation whose every true
   point is feasible (mind degenerate strata — the lift must dominate them
   honestly), solve the SDP, then rational-LDL the Grams and absorb the exact
   residual. Output: a certified inequality conditional only on integer
   arithmetic;
7. full interval arithmetic / Lean (reserved for final, load-bearing claims).

---

## 6. Anti-patterns (each one cost this project something)

- **Optimism-driven status docs** ("PROOF COMPLETE (conditional)" with
  unexamined conditions). State the evidence class per claim.
- **Empirical constants in theorem clothing** (κ = 1/55).
- **Measuring the proxy** (r at the origin while the max moved).
- **Tolerance subsidies.** (v4) A feasibility check with slack is an
  invitation the optimizer always accepts (tol=0.02 → a 2%-infeasible
  "record"). Exact criteria or strict-margin backoff, never bare tolerance.
- **Unread red flags.** (v4) Recording an invariant without asserting it.
  If a field in an artifact *would alarm you if you looked*, a test must look.
- **Correlated triangulation.** (v4) Three lines of evidence that share a
  failure mode (e.g., all are searches) are one line of evidence.
- **Coordinate-artifact panic or comfort.** (v4) Declaring a singularity real
  (or a bound safe) without checking whether it is an artifact of sorting,
  labeling, or gauge. Change frames before changing conclusions.
- **The 1/N fit on four points.** Log curves and saturating curves are
  indistinguishable on N = 3..6. Extend the range or say "unresolved."
- **Equivalent reformulations sold as progress.** An SDP dual of an open
  problem is the same open problem in a nicer suit. Reformulations count only
  when they import a tool that *does something* — the winding reformulation
  counts because it (a) survived the counterexample that killed the pointwise
  form, (b) made two lemmas provable, (c) defined a new DNS measurable.
- **Deleting failed work.** Banner it, never delete it.
- **Process-as-progress.** Filing a prediction doc is not progress; resolving
  the question is.

---

## 7. Division of labor (humans, agents, machines)

- Optimizers find structures and sharpness; they cannot be trusted about
  feasibility — certify independently (and prefer exact criteria, principle 11).
- Symbolic computation (sympy) verifies every algebraic identity before it
  enters a proof; identities that resist 5-line sympy verification get
  restated until they don't. *(sympy is also the referee of your guesses: the
  P(0)=0 parity guess was wrong, sympy caught it same-hour, and the honest
  correction is in the doc. Let it catch you.)*
- Adversarial review audits "RIGOROUS"/"PROVED" labels — schedule an audit
  after every major claim, and after every retraction audit everything
  adjacent.
- **Machines are shared.** (v4) Heavy runs (large-N DNS, multi-threaded SDP
  solvers that silently grab 11 cores) get thread caps, `nice`, memory
  budgets, and — on someone else's machine — explicit permission. A frozen
  workstation costs more trust than a delayed result.
- The orchestrator owns exactly two things the tools cannot: **choosing the
  next decisive experiment**, and **refusing to believe a result that hasn't
  earned its label.** Everything else is delegable. Use it.

---

## 8. The teaching method (v4)

Transformatics is transferable, and the transfer mechanism is specific: **the
curriculum is the corpus of receipts.** Not the successes — the retractions,
obituaries, and corrections, each paired with the principle it bought.

**Onboarding (a new agent or human, ~half a day):**

1. Read `STATUS.md` (state), this document (method), `PROOF_STATE.md`
   (the claim tree with evidence classes).
2. Read three obituaries end-to-end (window-design, E2 r→2, smooth Route A).
   The lesson is not the content; it is the *shape* of how a plausible line
   dies and what an honest burial looks like.
3. Read one correction pair: the 2-mode 1.1105 → 1.0960 docs. Note that the
   red flag was in the artifact all along.
4. **The drill:** pick any pinned claim and attack it. Recompute one headline
   number by an independent path before building anything on it. Finding a
   discrepancy is a *win* (twice this project's biggest advances started as
   someone re-checking a pinned number).

**The teachable moves** (each maps to a principle): collapse the constraint
(11); verify the solver (12); change the frame (13); weaken to what's consumed
(14); evolve the counterexample (15); distrust your own search (16); name the
classical object (4); register before you look (3).

**Grading yourself:** at session end, every new claim has a label from §4, a
test pinning it, and — if it displaced a previous claim — an explicit
correction note in the superseded doc. A session that produced only labeled,
pinned, honest artifacts was a good session *even if every result was
negative*. A session that produced one unlabeled "breakthrough" was a bad
session even if the breakthrough is real.

---

## 9. The mission: July 2026 snapshot

The flagship goal is **3D Navier–Stokes regularity on T³** — resolving
whether smooth solutions can form finite-time singularities. The current
strongest thread is the **strain-maximizer route**: control the growth of
`g = |S|²_F` at its moving global maximizer via the discriminant–Lyapunov
chain. As of 2026-07-01 the chain's two links have sharply different shapes:
**Link 1** (raw product bound) is on the certification ladder — exact-
constraint families bracketed by verified SOS certificates (2-mode
[1.0960, 1.1345], 3-mode [1.6536, 1.8619]); **Link 2** is the **Winding
Conjecture** (PROOF_STATE X.5): bounded winding of the strain-anisotropy
vector at the moving maximizer, with everything local proved harmless and the
open core isolated to one nonlocal pressure angle. See `docs/STATUS.md` for
exactly where each thread stands today.

Pursue it. The discipline is here so that when you succeed, people believe you
— and so that when a line is dead, you find out before it wastes a month.
Go solve it.

---

*Companion: `TRANSFORMATICS_PRIMER.md` (the mathematical setup — note it
predates the 2026-06 audits; trust `STATUS.md` for current claim standing).
Version history: v1 (overclaiming, retracted), v2 (2026-06-10, compliance
manual), v3 (2026-06-17, principles-first), v4 (2026-07-01, this document —
adds principles 11–16, the exact-verification ladder rung, the triangulation
caveat, and the teaching method); v5 (2026-09-08, transfer contracts and
explicit formal-certificate coverage).*

## 10. Transfer contracts: the September 2026 formal core

**v5 addition, 8 September 2026.** Transformatics is the name of this
proposed research methodology. The framework below makes its operations
precise; it does not establish a new universally applicable solution
method or resolve Navier–Stokes. The [learning notes](../notes/README.md)
provides a first teaching edition. Earlier case studies retain their
original dates and the standing assigned by the canonical claim ledger.

A **transfer contract** specifies how a tractable model can support a
claim about a target equation. It contains seven objects:

| Object | Required content |
|---|---|
| Target | Exact equation, domain, parameters, data class, and conclusion |
| Model | Auxiliary equation and the hypotheses under which it is solved |
| Reconstruction | A specified map from model objects to target-space objects |
| Defect | The residual after inserting that reconstruction into the target equation |
| Stability | A proved estimate relating residual and initial error to target error |
| Validity | Norms, time interval, constants, and order of parameter limits |
| Observable | The estimate that transfers target error into the claimed outcome |

For example, suppose `u'=F(u)` and a reconstructed curve v has residual
`r=v'-F(v)`. If a justified stability estimate in a norm X gives

\[
D^+\|u-v\|_X\le L(t)\|u-v\|_X+\|r(t)\|_X,
\]

with integrable L and r on the claimed interval, scalar Grönwall gives

\[
\|u(t)-v(t)\|_X\le
 e^{\int_0^t L}\|u(0)-v(0)\|_X+
 \int_0^t e^{\int_s^t L}\|r(s)\|_X\,ds.
\]

This is a conditional transfer lemma. In a PDE, existence, differentiability
or an appropriate weak inequality, and the stated stability estimate need
proof in the chosen spaces. Naming F does not make it Lipschitz there.
For a Lipschitz observable J with constant C on the relevant set,
`|J(u)-J(v)|≤C||u-v||X`; a positive model lower bound transfers only if
it exceeds this full propagated error. A small raw residual is insufficient.

For stages `e_(k+1)≤A_k e_k+d_k`, the corresponding exact upper bound is

\[
e_n\le\left(\prod_{k=0}^{n-1}A_k\right)e_0+
\sum_{j=0}^{n-1}\left(\prod_{k=j+1}^{n-1}A_k\right)d_j.
\]

Empty products are one. Finite-stage success does not justify an infinite
limit. The limit requires estimates for these products and sums, one
admissible initial object, convergence in a space that preserves the target
equation, and proof of the stated terminal observable.

### A worked transfer and its successors

In the [Gavrilov calculation](navier-stokes/gavrilov-oblique.md), the
model is a constant two-dimensional polarization system. Reconstruction
uses a specified family of smooth Euler profiles and their moving frames.
Uniform differentiated asymptotics bound the coefficient defect on one
relative period. An exact symmetry gives the full closed-orbit return as
the jth power of that relative map. The cone argument then transfers
expansion to the actual inviscid principal ODE.

Within that theorem, **actual** refers to the specified Euler-profile ODE.
The later [viscous-packet proof](navier-stokes/viscous-packet.md) supplies
a distinct reconstruction, pressure and localization defects, and stability
around a true viscous NS background. Fixing one profile before increasing
physical concentration is part of the validity contract; reversing the
limits would require additional uniform constants.

### A norm-sensitive transfer: finite strain handover

The [log-log handover proof](navier-stokes/loglog-handover.md) teaches why
the observable belongs in the contract. Its first approximation has small
L2 error of order h^(9/4-o(1)), but that estimate does not control the
pointwise strain. With the available Hs bound h^(7/4-s-o(1)), interpolation
would give a negative gradient exponent at every fixed s.

An explicit mean and two harmonic corrections improve the residual to
h^(11/4). The integral of the actual approximation's strain is O(ell),
where ell=sqrt(log(1/h)), so error amplification exp(C ell) is only
subpolynomial in h. A separate strong-solution bootstrap gives the high
norm needed for interpolation. For s=12 the gradient exponent is

\[
\frac{11}{4}\left(1-\frac{5}{24}\right)
+\left(\frac74-12\right)\frac{5}{24}=\frac1{24}>0.
\]

The true gradient error tends to zero while the model strain grows like
ell. This transfers a finite strain lower bound to a smooth NS solution.
The corrected residual, stability cost, high norm and observable are all
needed; an L2 estimate alone supplies no smooth handover theorem.

The next transfer requires a new contract again. A leading gradient
kappa p tensor N with p.N=0 is nilpotent even when its symmetric strain
is large. Therefore the outgoing wave cannot be assumed to inherit the
old background's expanding return map. The later
[outgoing-wave proof](navier-stokes/outgoing-wave.md) instead exploits
transient growth and realizes it in the exact viscous linearization
about the actual flow. A Jordan map can have two unit eigenvalues while
its largest singular value grows. The observable determines which
operator estimate matters.

That finer seed is specified at a later time. Its nonlinear evolution
and compatibility with the original datum are separate transfer
obligations. Infinite iteration additionally needs a joint error and
viscosity budget: a bound that is asymptotically small at each separately
chosen finite stage need not be uniform in the depth of one trajectory.


### Certificates have coverage, not a blanket authority

The [original cone certificate](../formalization/oblique_cone/README.md)
proves explicit algebraic statements with explicit hypotheses. Its source,
compiler version, dependencies, axiom printout, and replay result are
recorded. It does not formalize the complete transfer contract.
The [fluid_lean integration note](navier-stokes/fluid-lean-integration.md)
separates reusable ODE certification tools from forced-fluid statements
that do not imply the unforced viscous target.

Use a claim record containing: an identifier; exact quantified statement;
evidence class; dependencies; current source; falsifier or check; and
remaining obligations. A theorem's dependency edge asserts that the exact
hypotheses were supplied. A teaching or historical edge merely explains
context and must be labelled separately. The full research graph is preserved
in the private research archive; the learning notes claim index uses the current
repository's explicit conventions.

### How to teach a transfer

Explain the phenomenon in plain language, state the exact claim, derive
the model, and show where reconstruction can fail. Give a worked example,
an independent control, an exercise that exposes a missing hypothesis,
and a solution. End the case study at the proved boundary and state the
next mathematical obligation. Maintain the false starts when they teach
why an attractive shortcut fails. This makes the reasoning reproducible
for both people and agents while leaving room for new conjectures.
