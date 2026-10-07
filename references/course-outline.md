# Teaching Transformatics

**Textbook course, 8 September 2026.** This curriculum supports the
[textbook](../textbook/chapters/index.md). It replaces the June sequence
through static vorticity–strain optimization. It is a course in finite
transformations, observables, and quantitative comparison of evolutions.
The core is a mathematical course with assessable results; the advanced
sequence applies it to our finite fluid constructions and the separately
authored published forced Navier–Stokes proof.

The student’s central task is to justify a prediction: **given an evolution,
a simpler description, and a measurement, determine what can be predicted,
with what error, for how long.** Success means producing a calculation and
its assumptions. Recognizing the vocabulary is insufficient.

## Entry knowledge and destination

The entry point is high-school algebra and single-variable calculus.
The first chapter uses function composition, polynomial algebra and finite
sums. The optional [calculus bridge](../textbook/chapters/calculus-bridge.md)
introduces small matrices, the multivariable chain rule, vector derivatives,
norms, integration by parts for heat flow, Fourier modes and quantifiers.
Assign its short checks at the point each tool first appears; it need not
be a preliminary unit completed before students encounter the main examples.
Previous study of operator theory is not required.

The bridge prepares specific calculations. It does not make graduate PDE
estimates prerequisites that a beginner has silently satisfied. A reader can
finish the foundation course and the exact shear example while treating the
advanced sources as a route for later study.

For experienced readers, the
[mathematical reading map](../textbook/chapters/reader-map.md) identifies the
standard connections and leads directly to the substantive statements.
A seminar can begin with its sharp prediction-error problem, prove the
factor criterion, and compare representation error with lost information.
Continue with the norm-conversion example, the weighted-coupling construction,
or the quantifier failures in iteration. Ask for a proof and a changed
hypothesis, rather than requiring repetition of elementary definitions.

These are proposed teaching routes, not results of a learner study. To review
them with people, ask a calculus reader to attempt the bridge's chain-rule
and norm exercises, and ask an experienced reader to inspect the factor
criterion and one later argument with its source. Record where either reader
first needs information the text has not supplied.

The course extends calculus by studying finite maps before taking limits,
and by comparing representations of the same dynamics. Its underlying
mathematics comes from finite differences, pullbacks and Koopman operators,
dynamical systems, Lie derivatives, and numerical analysis. The
[discipline statement](mathematical-background.md) explains the synthesis
and its lineage. Students do not need to accept a novelty claim in order
to use or assess these tools.

The project originates with Hunter Bown's question about how a study beyond
his experience of calculus could better explain change in real systems,
developed in collaboration with frontier and open-source models, especially
DeepSeek and GLM. Treat that motivation as an invitation to formulate and
test mathematics. It is not evidence of superiority to established fields.
The [credits chapter](../textbook/chapters/credits.md) records attribution;
students should distinguish the course's proposed synthesis from classical
theorems and from other authors' research.

By the end of the core, a student should be able to:

- Distinguish a state map from an observable and an operator on observables.
- Calculate finite changes, their order of composition, and their accumulated effect.
- Derive a generator and integrate its action along an existing flow.
- Specify an evolution family, representation, observable, norm and admissible time domain.
- Prove the exact factor criterion and quantitative composition theorem; exhibit a failed hypothesis in a counterexample.
- Compute a representation defect and propagate it using a justified stability bound.
- Convert field, derivative, time, and error scales together.
- Verify an exact fluid solution, including pressure, and state what an energy check does not establish.

These are the prerequisites for reading the research case studies. They
are not a promise that the reader can resolve their remaining PDE gaps.

## The core sequence

Read the five foundation chapters in order, then the fluid equation. Each
row specifies something the student must produce before moving on. Exercise
numbers refer to the chapter’s own exercise section.

| Unit and reading | Student work | Evidence of readiness |
|---|---|---|
| 1. [Finite transformations](../textbook/chapters/transformations.md) | Calculate pullbacks and finite differences; prove the product and telescoping laws; compare the two orders of a shear and a translation. | Exercises 2, 3, 5 and 6: distinguish an invariant measurement from an unchanged state, detect order with a chosen observable, telescope varying updates, and use a closed space of quadratic observables. |
| 2. [Generators](../textbook/chapters/generators.md) | Derive \(L_vf=v\cdot\nabla f\); recover finite change by integration; calculate both fixed-location and particle-following derivatives. | Exercises 3–6 check generator limits, material invariants, finite lifetime and numerical steps. Exercise 7 shows why a time-one map does not determine the intervening motion or its generator. |
| 3. [Transfer systems](../textbook/chapters/transfer-systems.md) | Type every map, prove the necessary and sufficient fiber condition for an exact quotient, and prove quantitative composition by inserting one intermediate state. | Exercises 1–4 separate exact representation from reconstruction, calculate a nonlinear output conversion, respect an existence interval, and distinguish linear from quadratic observable error. |
| 4. [Composition and error](../textbook/chapters/composition.md) | Derive \(e_{j+1}\le L_je_j+\delta_j\) and its iterated bound; distinguish composition across time from composition across descriptions. | Exercises 1, 2, 4 and 5 establish transfer and error calculations. Exercises 6–7 check operator order and require an invariant-region proof. Complete Assessment A. |
| 5. [Scale and resolution](../textbook/chapters/scaling.md) | Derive amplitude, derivative and volume factors; transform the equation and time interval; identify the same diffusion number in both descriptions. | Exercises 1–5 convert norms and tolerances, compute terms from time-dependent scale, distinguish criticality from conservation, and identify an aliased product. |
| 6. [The fluid equation](../textbook/chapters/equation.md) | Check every term of an exact shear; derive pressure and energy laws; identify strain as a deformation measurement. | Exercises 1–4 verify a three-dimensional datum, recover pressure, explain the limits of energy checks, and reject a terminally singular force. Complete Assessment B. |

The sequence has a specific dependency. Unit 3 determines the comparison
and the information missing from a representation. Unit 4 propagates its
error over time; Unit 5 determines what the bound means physically. Unit 6
supplies an evolution whose simplified examples
can be checked exactly and whose general nonlinear interactions make
approximation substantially harder.

For a semester seminar, allow two meetings each for finite changes,
generators and transfer systems, followed by one on temporal error and one
on Assessment A. Use two meetings on scaling and the fluid equation, then
one on Assessment B. The remaining three meetings can introduce residuals,
iteration, and a selected argument from the published-proof chapter. That
schedule is an introduction; reading every advanced source proof requires
substantially more time and graduate PDE preparation.

## How to teach one unit

The presentation takes inspiration from Leonard Bernstein's
[Norton Lectures](https://www.leonardbernstein.com/about/educator/norton-lectures):
concrete examples should carry an argument that becomes richer when the
examples return. This course implements that choice through calculation,
not musical analogy. The planar shear first tests composition order, then
distinguishes a moving observable from a fixed-location measurement, and
later tests whether eigenvalues control amplification.

Start with the chapter’s concrete problem before its definitions. Ask the
student to predict an outcome, calculate it directly, and then identify
what the general formula preserves from that calculation. The proof should
answer a question the student has already encountered.

Use three passes through the assigned work:

1. **Calculate.** Complete a direct example with the relevant definition visible.
2. **Justify.** Close the worked proof and reconstruct the step carrying the conclusion.
3. **Vary.** Change an input, representation, time interval, or norm and explain which conclusion survives.

For feedback, identify the first incorrect step and give a smaller check
that tests it. For example, a reversed pullback order can be tested on the
coordinate observable; a mistaken scaling exponent can be tested on one
first derivative before returning to a norm. Have students redo the
changed case before revealing the full solution.

A student is ready to advance when their written work specifies the maps
and domains, obtains the calculation, and explains its range of validity.
A correct formula copied without those distinctions needs another example,
not a longer list of definitions.

## Assessment A: one evolution, several measurements

The first [practice assessment](../textbook/chapters/practice.md#assessment-a)
uses \(a'=-a+b\), \(b'=-2b\). Students solve the full system, discover the
closed total \(R(a,b)=a+b\), calculate the error of the multiplier \(0.51\)
at steps of length \(\log2\), and reconstruct the full vector. A display
conversion \(P(r)=100r\) then makes the representation-composition factor
unavoidable. This assesses the first four units without PDE prerequisites.

Use the following 20-point rubric. Award reasoning credit when an early
arithmetic error is propagated consistently; withhold the relevant
hypothesis credit when a correct number comes from an invalid comparison.

| Evidence | Points | What a complete answer contains |
|---|---:|---|
| Evolution and generator | 4 | Exact solution, composition verification, and both observable derivatives. |
| Representation | 4 | Exact closure for all states and two states disproving the alternative closure. |
| Temporal error | 4 | Correct defect sign, Lipschitz factor, recurrence and accumulated bound. |
| Reconstruction and tolerance | 5 | Euclidean error, separate information loss, tolerance decision, and loss remaining with an exact multiplier. |
| Observable conversion | 3 | Correct display evolution, factor 100, and tolerance in the output units. |

An answer omitting reconstruction loss has not met the learning objective
even if it computes the retained coefficient exactly. Ask which extra
variable removes the loss. An answer claiming no scalar model exists can
be tested against the derivative of \(a+b\); one claiming every scalar
observable closes can be tested against the derivative of \(a^2\).

## Assessment B: one shear, several descriptions

The second [practice assessment](../textbook/chapters/practice.md#assessment-b)
adds physical fields, derivative-sensitive observations and resolution.
Use the two-frequency shear

\[
u_0(x,y,z)=\left(\sin y+\tfrac12\sin(8y)\right)e_1
\]

on the fixed \(2\pi\)-periodic box. Its nonlinear self-advection vanishes,
so its full unforced NS evolution is given by the heat multipliers already
derived in the core. The problem is sufficiently explicit that a wrong
prediction can be located exactly.

The assessment should ask students to compare three descriptions:

- The full exact evolution.
- An exact heat evolution retaining only selected Fourier modes.
- The same retained modes evolved with explicit Euler time steps.

For a stated viscosity, final time, norm, and tolerance, the student must
separate discarded information from time-stepping error, obtain a stability
condition, and justify or reject the proposed prediction. Then they must
convert the error into physical units. The final interpretation should
explain why this shear calculation does not control arbitrary nonlinear
fluid data.

Grade this assessment out of 20 using the following evidence: 4 points for
the state, energy and squared-gradient observables; 4 for verifying every
PDE term and the generator; 4 for transfer, reconstruction and physical
scaling; 5 for stability, accumulated error and the three tolerance
decisions; and 3 for a claim card with correct datum and time quantifiers.
Require an explanation of why temporal refinement cannot remove a spatial
error floor. A correct simulation plot does not substitute for that argument.

The [fluid laboratory](../textbook/chapters/simulator.md) can support a
follow-up comparison with its implemented benchmarks. Students should
predict the benchmark’s decay before running it and identify the solver’s
actual spatial and temporal methods before comparing results. Numerical
agreement is evidence about that implementation; the written exact
calculation supplies the mathematical benchmark.

## Entering the research case studies

There is a deliberate increase in prerequisites here. The foundations
prepare students to formulate the transfer questions. Full research proofs
also require Fourier analysis, Sobolev estimates, local existence and
continuation theory for PDEs. The case-study chapters give orientation and
selected derivations; the linked source notes carry the complete stated
arguments. They do not constitute a self-contained first PDE course.

| Reading | Question the student should answer in writing |
|---|---|
| [Residuals and smooth forcing](../textbook/chapters/residuals.md) | Derive a residual error equation, calculate its propagator, and distinguish a force with small amplitude from one with every required mixed derivative controlled. Verify the mean-stress pressure projection and the complete cutoff terms. |
| [Frequency creation](../textbook/chapters/activation.md) | Which interaction creates the selected mode, and what remainder estimate makes its leading coefficient informative about an actual solution? |
| [Concentration](../textbook/chapters/concentration.md) | Convert an accumulated-strain bound into an error certificate, including the background's contribution to the measured output. Explain why summing lifetimes of separate solutions does not join them into one trajectory. |
| [A steady reference flow](../textbook/chapters/steady.md) | Which estimates compare Euler and NS, on what interval, and which constants must be fixed before a scale tends to zero? |
| [Pressure and polarization](../textbook/chapters/oblique.md) | Derive the pressure coefficient by preserving transversality, compute a covector return with an inverse transpose, and evolve an eigenvector of the limiting amplitude matrix. Which comparison is still needed for the actual compact flow? |
| [Finite amplification](../textbook/chapters/viscous.md) | Construct a real packet as a curl, check its divergence and normalization, then use the stated PDE inputs to compare gain, damping, nonlinear error and the background tail. Distinguish a large amplification ratio from a large absolute output. |
| [Iteration and limits](../textbook/chapters/iteration.md) | Identify the data passed from one stage to the next. Prove the relevant accumulated error or convergence statement, and distinguish a sequence of regular solutions from stages of one solution. |
| [The published proof](../textbook/chapters/published-proof.md) | State the external theorem's domain, data, force class and terminal conclusion. Follow one complete transfer of an estimate through its construction; list the hypotheses supplied there that our finite results do not supply. |
| [Making a new construction](../textbook/chapters/new-constructions.md) | Prove the classical component-replacement estimate, construct a different coupling with the same complete handover, and identify the weighted condition that preserves its output. Formulate one specific replacement problem for the external construction without assuming it is solvable. |
| Optional: [Advanced transfer](../textbook/chapters/advanced-transfer.md) | Study original-time preparation, strain handover and later windows after the main course. Supplementary Exercise 8 distinguishes estimates for each fixed power from an estimate uniform in the power. These source-dependent extensions are not prerequisites for the elementary capstone. |

For each case, students should produce the claim card described in
[practice](../textbook/chapters/practice.md), then reconstruct one selected
estimate. A source proof, a formalized algebraic sublemma and a numerical
observation must retain their different scopes.

The [OpenAI release](https://openai.com/index/navier-stokes-solution/)
reports a smoothly forced breakdown proof of alternatives C and D, with
an accompanying Lean formalization. Attribute that result to its authors.
Our restricted finite constructions remain separate mathematics. Students
should connect them by comparing hypotheses and estimates, not by claiming
that a shared vocabulary makes one proof a prerequisite for the other.
The local unforced target and separate \((E′)\) estimate remain distinct
research questions. A family of changing initial data is not one terminal
trajectory. Consult [current status](../docs/STATUS.md) for the local claims and
the published-proof chapter for the external result and verification scope.

## A final reading assignment

Complete [the constructive capstone](../textbook/chapters/new-constructions.md)
before this assignment. Its freely chosen interior function gives an
explicit family to vary while preserving the handover. Use that experience
to distinguish proposing a replacement from proving that it meets the next
component's requirements.

After the advanced sequence, assign a two-page comparison of one local
finite theorem with one step in the external construction. Require the
student to write the actual maps or operators, the equation and domain,
the source and target norms, and the admissible time interval. Then select
one estimate and reproduce its derivation. A last paragraph should identify
exactly which new hypothesis would be needed to use the local theorem in
that external step. “Both use scaling” is an observation; matching a bound
with its constants and quantifiers is mathematical work.

This assignment assesses reading and transfer analysis. It does not certify
the external proof or the student's ability to close an unrelated open
problem. A correct negative conclusion—that the hypotheses do not match—is
valuable when supported by a precise calculation or counterexample.

## Historical curriculum

The June curriculum concentrated on static vorticity–strain witnesses,
ray-mass bounds, and a proposed return to NS regularity. Those topics remain
available as specialized historical material in
[VSA ray theorems](ray-theorems.md) and the
[June proof-chain audit](proof-chain-review.md). They no longer form
the core course or prescribe the active research frontier. Their status
must be checked against later corrections before assigning them as research.
The retired growth-set noncollapse route is likewise excluded from current
course guidance; its failure is documented in the
[cap-vacuity audit](navier-stokes/qgso-cap-vacuity.md).
