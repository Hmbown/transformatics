# Where this book meets the literature

A new course is easier to judge when its debts are visible. The word
*Transformatics* supplies an organizing viewpoint; the mathematical subjects
below supply much of its substance. These references let you study those
subjects in their own terms, compare conventions, and continue beyond our
examples. A citation records an intellectual connection, not an endorsement
of this project by the cited author.

## Finite transformations and observables

B. O. Koopman's 1931 paper, [*Hamiltonian Systems and Transformation in
Hilbert Space*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1076052/), gives an
important historical source for studying dynamics through operators on
observables. Our elementary pullback calculation belongs to that lineage.
The algebraic linearity of an operator on observables does not say that a
nonlinear state equation has become a finite-dimensional linear system.
Return to the examples in [finite changes](transformations.md) with this
distinction in mind.

For flows, existence, uniqueness and stability, see Gerald Teschl,
[*Ordinary Differential Equations and Dynamical Systems*](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode),
Graduate Studies in Mathematics 140, American Mathematical Society, 2012.
The author's page includes an authorized online edition. This is the natural
companion to [generators](generators.md) and [transfer systems](transfer-systems.md).
Read the treatment of local solutions before treating a flow map as globally
defined: the interval of existence is part of the mathematical object.

## Approximation, stability and computation

Randall J. LeVeque, [*Finite Difference Methods for Ordinary and Partial
Differential Equations*](https://faculty.washington.edu/rjl/fdmbook/), SIAM,
2007, develops the relationship between approximation and stability that
underlies our [composition](composition.md) and [residual](residuals.md)
chapters. His author page provides supporting materials. Our error recurrence
is an elementary instance of a broad numerical-analysis question: how does a
local discrepancy affect the final answer?

For conservation laws and another family of numerical discretizations, see
LeVeque, [*Finite Volume Methods for Hyperbolic Problems*](https://amath.washington.edu/research/publications/finite-volume-methods-hyperbolic-problems),
Cambridge University Press, 2002. It provides context for distinguishing a
physical conservation law from the discrete rule used to approximate it.
The [fluid laboratory](simulator.md) uses a Fourier method; the method and
its assumptions are described there rather than attributed to this reference.

## Incompressible fluids and PDE analysis

Jacob Bedrossian and Vlad Vicol, *The Mathematical Analysis of the
Incompressible Euler and Navier–Stokes Equations: An Introduction*, Graduate
Studies in Mathematics 225, American Mathematical Society, 2022, provides a
systematic route into the analysis behind our fluid chapters. It is listed on
[Vicol's university publications page](https://cims.nyu.edu/~vicol/publications.html).
Use it to develop the local existence, function-space and energy-method
background that our advanced packet calculations assume.

Andrew J. Majda and Andrea L. Bertozzi, *Vorticity and Incompressible Flow*,
Cambridge University Press, is a further foundation for the geometric and
analytic study of fluids. [Majda's university bibliography](https://math.nyu.edu/faculty/majda/publicationrevised.html)
identifies the book. The velocity, vorticity and strain descriptions in our
[fluid equation chapter](equation.md) should be understood as related
classical descriptions of the same field.

Terence Tao's [*Nonlinear Dispersive Equations: Local and Global
Analysis*](https://terrytao.wordpress.com/books/nonlinear-dispersive-equations-local-and-global-analysis/),
CBMS 106, American Mathematical Society, 2006, develops local-to-global
reasoning for a different family of PDEs. It is useful here for the method of
moving between model examples, estimates and existence arguments. Dispersive
and viscous equations have different analytic mechanisms; a technique still
needs its hypotheses checked when moved between them.

For the exact question behind the research case study, read Charles L.
Fefferman's [official Navier–Stokes problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf),
including its pressure-periodicity erratum. It distinguishes whole-space and
periodic settings, unforced regularity alternatives and forced breakdown
alternatives. These distinctions determine what a claimed result answers.

## Research sources used in the case study

Alexander Gavrilov's [*A steady Euler flow with compact support*](https://arxiv.org/abs/1810.08020)
is the source of the compact Euler profiles used in our [steady background](steady.md)
and [oblique covector](oblique.md) chapters. Those chapters state the
additional choices and estimates used by this project. The original profile
theorem and the project's subsequent comparisons have separate attributions.

OpenAI's [*Finite time blowup for Navier–Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
and [public formalization](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538)
are the external sources for [the published-proof chapter](published-proof.md).
The [source record](../../references/navier-stokes/openai-result-bridge.md) pins
versions and states what was inspected. This book teaches selected underlying
operations through independent examples. It does not substitute for reading
the full research proof.

Our earlier encounters with Tao's commentary and the `fluid_lean` project
are documented in the [Tao context and formalization audit](../../references/navier-stokes/fluid-lean-integration.md).
That dated record preserves the scope of the material then available. The
released OpenAI theorem is a later source and has its own record.

## Information and control

The [information and action chapter](information-action.md) starts from finite
sets and a scalar interval model. Its intersections and covering proof are
self-contained. The following sources develop broader theories and an
experimental application:

- **Claude E. Shannon**, *A Mathematical Theory of Communication* (1948).
  [Original paper, IEEE-hosted reproduction](https://reach.ieee.org/wp-content/uploads/2023/05/IEEE_REACH_A_Mathematical_Theory_of_Communication.pdf).
  Read the communication model and the distinction between a message alphabet,
  entropy and channel capacity. The chapter's zero-error fixed-length count
  supplies none of the assumptions needed to identify these quantities.
- **Mahendra Singh Tomar, Matthias Rungger and Majid Zamani**,
  [*Invariance Feedback Entropy of Uncertain Control Systems*](https://arxiv.org/abs/1706.05242).
  This studies information requirements for enforcing invariance under
  uncertainty, extending the horizon beyond our single transition.
- **Takashi Tanaka, Peyman Mohajerin Esfahani and Sanjoy K. Mitter**,
  [*LQG Control with Minimum Directed Information: Semidefinite Programming Approach*](https://arxiv.org/abs/1510.04214).
  This treats information and control performance in a stochastic setting;
  expected cost and directed information differ from a worst-case control cover.
- **Kun Liu and coauthors**,
  [*SurfAAV: Design and Implementation of a Novel Multimodal Surfing Aquatic-Aerial Vehicle*](https://arxiv.org/abs/2506.15450).
  This is an experimental reference for aquatic–aerial operation. It does not
  validate a vehicle or transition algorithm developed by this project.

## Formal proof and mathematical communication

Jeremy Avigad, Leonardo de Moura, Soonho Kong and Sebastian Ullrich,
[*Theorem Proving in Lean 4*](https://lean-lang.org/theorem_proving_in_lean4/),
is an introduction to the language and logic used by the formal examples.
Read it alongside [the evidence chapter](evidence.md), especially when
comparing an informal theorem statement with the proposition actually checked.

A useful reading habit is to carry one example across these sources. Begin
with the exact decaying shear in [the fluid equation](equation.md), compute
its norms under [scaling](scaling.md), insert an altered amplitude into the
[residual equation](residuals.md), and ask what estimates would survive
[repeated stages](iteration.md). Keeping one example in view makes the
connections testable.
