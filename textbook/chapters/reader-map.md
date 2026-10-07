# A mathematical reading map

This book follows a prediction through changes of description. Its elementary
identities belong to established mathematics. What the course offers is a
sequence of examples in which the same questions recur: what information is
retained, how an error propagates, and which hypotheses a stronger conclusion
would need.

You can read it at different depths. The short problem below needs algebra.
The map that follows gives experienced readers conventional terminology and
direct entry points. The fluid sources require graduate analysis in addition
to the calculations displayed in their teaching chapters.

## A small problem with two ways forward

A system has state $(x,y)$ and update

$$
T(x,y)=(x+y,y).
$$

Only $x$ is measured: $R(x,y)=x$. Suppose the unobserved coordinate lies
in $[-b,b]$, where $b>0$ is fixed, so the state space is
$X=\mathbb R\times[-b,b]$. The update preserves this state space.
Can a model using only the present reading predict the next one?

The states $(x,b)$ and $(x,-b)$ look identical to the device, but their
next readings are $x+b$ and $x-b$. An exact scalar update is impossible.
There is also a precise limit to approximation. If a deterministic model
predicts $S(x)$, the triangle inequality gives

$$
2b\le |x+b-S(x)|+|S(x)-(x-b)|.
$$

At least one error is therefore at least $b$. The choice $S(x)=x$ attains
that worst-case bound over all $y\in[-b,b]$. Thus the best possible
worst-case one-step error is exactly $b$. This is an information limitation
within the stated observation model; numerical precision cannot reduce it.

There are two useful changes to the problem.

**Retain another measurement.** Recording $(x,y)$ makes the update exact.
For a general representation $R$, the
[factor criterion](transfer-systems.md#3-exact-transfer-and-the-test-for-lost-information)
says exactly when states with the same representation have the same next
representation. The sets of states sharing a reading are called its *fibers*.

**Retain some history.** Under this particular update, $y$ stays constant,
so exact consecutive readings satisfy

$$
x_{n+1}-x_n=y,\qquad x_{n+2}=2x_{n+1}-x_n.
$$

Two consecutive readings determine the next one. A first-order scalar
description failed, but a two-coordinate state $(x_n,x_{n+1})$ succeeds.
Its update is $(a,c)\mapsto(c,2c-a)$. This recovery uses the specified
dynamics and exact measurements; it is not a general theorem that two
observations recover a hidden state.

**Exercise: what did memory cost?**

1. At a fixed integer horizon $n\ge1$, using only $x_0$, find the smallest
   possible worst-case error in predicting $x_n$ over $|y|\le b$.
2. Suppose two consecutive readings have errors $\eta_0,\eta_1$ with
   $|\eta_j|\le\varepsilon$. Bound the error of the history-based
   prediction $2(x_1+\eta_1)-(x_0+\eta_0)$. Can the bound be attained?

<details markdown="1">
<summary>Solution: information and sensitivity are separate costs</summary>

The exact state is $x_n=x_0+ny$. The two possible extremes differ by
$2nb$, so the same triangle-inequality argument gives lower bound $nb$.
Predicting $x_0$ attains it. No assumption about a probability distribution
on the hidden state was made.

The history-based error is $2\eta_1-\eta_0$, of magnitude at most
$3\varepsilon$. Choosing $\eta_1=\varepsilon$ and
$\eta_0=-\varepsilon$ attains the bound. Memory removes the missing-state
ambiguity for exact observations, while the reconstruction has its own
sensitivity to measurement error.

</details>

These calculations are elementary consequences of factorization and the
triangle inequality. They motivate [transfer systems](transfer-systems.md),
[error propagation](composition.md), and
[information and control](information-action.md).

## The mathematics in familiar terms

Use this table to locate a statement without reading every introductory example.
“Transfer” is the book's common wording for several related comparisons; the
actual maps, norms and time domains determine each one.

| Book language | Established mathematical connection | Where to inspect the argument |
| --- | --- | --- |
| Action on observables, $U_Tf=f\circ T$ | Pullback; Koopman operator viewpoint | [Finite changes, Sections 2–5](transformations.md#2-moving-the-transformation-onto-the-observable): linearity on functions, finite product rule, reversal of composition order |
| Continuous generator, $L_vf=Df\,v$ | Lie derivative on scalar functions; autonomous flow | [Generators, Sections 2–4](generators.md#2-differentiating-the-observable-action): pointwise derivative and integral identity with an existence interval |
| Exact representation, $RT=SR$ | Factor dynamics; semiconjugacy when the relevant topological hypotheses hold | [Transfer systems, Section 3](transfer-systems.md#3-exact-transfer-and-the-test-for-lost-information): fiber criterion on $R(X)$; no automatic continuity assertion |
| Composition of representation defects | Approximate intertwining and a Lipschitz estimate | [Transfer systems, Section 5](transfer-systems.md#5-composing-two-representations): one intermediate term proves the bound |
| Accumulated one-step error | Consistency and stability; discrete Gronwall estimates | [Composition](composition.md#an-approximate-relation-needs-stability): local defects carry later amplification factors |
| Propagated residual | Variation of constants; continuous stability estimates | [Residuals, Sections 2–3](residuals.md#2-propagate-the-residual-before-judging-it): linear response and a separately justified fluid relative-energy estimate |
| Replacing a component of a construction | Perturbation estimates and preservation of an output margin | [Making a new construction, Sections 1–4](new-constructions.md#1-a-transfer-we-can-redesign): a solvable coupling example and its full error budget |
| One evolution from many stages | Compatibility, uniform estimates, and order of quantifiers | [Iteration](iteration.md#1-three-different-quantifiers): exact elementary examples preceding the PDE obligations |

The [literature guide](references.md) gives primary sources and longer
treatments. Terminological connections do not identify all hypotheses across
these subjects. For example, an algebraic factor need not be continuous, and
a pointwise generator identity is not a theorem about the domain of an
unbounded operator on a chosen Banach space.

## Questions to read for

**Which information is sufficient?** The fiber criterion makes an exact
statement. Test it on the square observable and translation, then on a
representation that does close. In the
[control example](information-action.md#1-which-action-works-for-everything-the-observation-allows),
the related question is whether one action works for every state compatible
with the reading. The information needed to act and the information needed
to reconstruct a state can differ.

**Is the claimed stability in the requested norm?** In
[transfer systems](transfer-systems.md#6-two-calculations-that-test-the-theorems-hypotheses),
a matrix contracts in a weighted norm but amplifies some Euclidean inputs.
Track both the contraction constant and the conversion back to the desired
measurement. Then compare the
[linear residual formula](residuals.md#2-propagate-the-residual-before-judging-it)
with an estimate that keeps only the matrix norm: what directional information
has that bound discarded?

**What is preserved by a changed component?** In
[the coupling example](new-constructions.md#3-a-new-variant-with-exactly-the-same-output),
an appropriately weighted integral preserves the complete terminal state.
An ordinary time average does not. The fluid example asks a harder version:
preserving an averaged stress leaves transport, viscosity and localization
terms to check. The elementary construction is self-contained; the fluid
replacement question remains a research problem.

**Which estimate is uniform, and over what objects?**
[Iteration](iteration.md#3-summable-local-errors-can-still-produce-an-unbounded-error)
exhibits summable fresh errors whose propagated total diverges. Its smooth
pulse example distinguishes control at each fixed derivative order from a
single sequence meeting all the required bounds. These are exact teaching
calculations. They isolate obligations that an actual PDE construction must
then meet with its own solutions.

You can use these questions in a seminar: first reconstruct the displayed
proof, then change one hypothesis and locate the first line that fails.
A sharpened bound, a counterexample, or a clearer connection to the literature
is a useful contribution whether or not it advances an open fluid problem.

## Where the self-contained course ends

The foundation chapters prove their elementary identities and estimates in
the text. The fluid equation chapter derives a smooth energy identity and
checks an exact shear. Later chapters mix explicit teaching calculations,
conditional arguments, and summaries of research proofs. The linked source
notes contain hypotheses and estimates that the summaries alone do not prove.

For the local packet arguments, start with
[finite amplification](viscous.md), then the
[optional research companion](advanced-transfer.md). Read each statement
with its datum, viscosity, domain, norm and interval in view. Their finite
families do not supply an unforced singular trajectory. The
[claim register](../claims.md) distinguishes local written arguments, AI
reviews, restricted formal checks and imported results. AI review is not
external expert acceptance.

The [published construction](published-proof.md) is separately authored by
OpenAI and concerns smooth external forcing. Its source and local verification
record have their own scope. The unforced ROOT target and E-prime estimate
remain open; research on them is currently paused.

The most useful expert feedback is specific: a missing hypothesis, an
incorrect estimate, an attribution that needs correction, or a place where
an elementary example obscures the harder problem. The
[contribution guide](../../CONTRIBUTING.md) explains how to attach such a
correction to its source.
