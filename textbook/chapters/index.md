# A calculus of transformations

How can we predict a measurement after many updates, and know how accurate that prediction is? This course begins with a map of a number, develops a calculus for its action on measurements, and uses that calculus to compare descriptions of an evolving fluid. Its subject is **quantitative transfer**: the conditions under which a conclusion in one description remains valid in another.

Take a state $x\in\mathbb R$, an update $T_h(x)=x+h$, and the observable $f(x)=x^2$. The exact change is

$$
\Delta_{T_h}f(x)=f(T_hx)-f(x)=2xh+h^2.
$$

At $x=2,h=1$, the square increases by $5$. Multiplying the derivative by the step gives $f'(2)h=4$; the missing unit is the finite term $h^2$. For several updates, a second issue appears: each change is evaluated at a new state. The exact accumulation is

$$
\sum_{j=0}^{n-1}\Delta_{T_h}f(x+jh)
=(x+nh)^2-x^2.
$$

You will learn to perform this calculation for general maps, recover derivatives when limits exist, and estimate the consequences when an exact update is replaced by an approximation.

## What Transformatics organizes

The starting objects are a **state space**, a **transformation** $T:X\to X$, and an **observable** $f:X\to\mathbb R$. Instead of following only the state, we can ask how the transformation acts on the measurement:

$$
U_Tf=f\circ T,\qquad \Delta_Tf=U_Tf-f.
$$

A translation, a rotation, a numerical time step, and a fluid flow all act on observables this way. The course connects finite changes, continuous generators, representations, stability, and scale conversion. For each comparison, you will specify the state, evolution, observable, norm and time domain before asserting that an approximation is useful.

*Transformatics* names the organizing viewpoint of this book: follow a
mathematical prediction through changes of state, representation, scale and
approximation. Its foundations are classical finite differences, pullbacks
and Koopman operators, dynamical systems, Lie derivatives, numerical analysis
and PDE estimates. The [reading map](reader-map.md#the-mathematics-in-familiar-terms)
connects our terminology to those subjects.

The purpose of collecting these ideas is to make their connections usable.
We will change a component of an example, calculate the resulting discrepancy,
and ask which conclusions survive. Some answers are short algebraic proofs;
others require substantial analysis; some remain open. The relevant chapter
identifies which kind of answer it supplies.

Hunter Bown initiated the project with AI assistance, especially DeepSeek and
GLM according to his account. The [credits](credits.md) describe the history.

## Choose a route through the book

**If your background is high-school calculus**, begin with
[finite transformations](transformations.md). It needs algebra and function
composition. Use the [calculus bridge](calculus-bridge.md) when vectors,
partial derivatives or norms first appear, then work through the five
foundation chapters below. The bridge includes small checks with solutions;
you can read one section at a time. Assessment A is a useful first destination.

**If you already know linear algebra and analysis**, start with
[the mathematical reading map](reader-map.md). It leads directly to the exact
factor criterion, the distinction between representation error and lost
information, and examples where a weak estimate cannot support a stronger
conclusion. The questions about their hypotheses supply the further work.

**If you are here for fluids**, the [exact decaying shear](equation.md#worked-flow-shear-reduces-the-pde-to-one-ode)
is a manageable first calculation. A first reading can follow that example,
its energy budget and the opening statement of the
[external result](published-proof.md#1-state-the-external-theorem-before-interpreting-it).
The later pressure, localization and PDE estimates need more preparation;
the [literature guide](references.md#incompressible-fluids-and-pde-analysis)
provides a route into it.

The common habit is to ask what information the example retains, then change
one assumption. You can complete the elementary course on its own or use it
as a way into the research material.

## The core course

Read the five foundation chapters in order, then the fluid equation. Each row names a calculation you should be able to complete without copying the worked example.

| Chapter | Question | Your work before moving on |
|---|---|---|
| [Finite transformations](transformations.md) | What changes when a map acts on a measurement? | Compute a finite product law, detect the order of two maps, and telescope changes along successive states. |
| [Flows and generators](generators.md) | Which instantaneous law describes a continuous motion? | Derive a generator, integrate it along a trajectory, and distinguish a material derivative from a fixed-location derivative. |
| [Transfer systems](transfer-systems.md) | Which information can a model predict, and how do representations compose? | Test exact closure, prove the quantitative composition theorem, and convert error through a norm or observable. |
| [Composition and error](composition.md) | What can a simpler description predict? | Find a transfer defect and bound its propagated error; distinguish discarded information from inaccurate evolution. |
| [Scale and resolution](scaling.md) | What does a model’s error mean in physical variables? | Convert velocity and gradient errors, time intervals and viscous attenuation; identify an aliased Fourier product. |
| [The fluid equation](equation.md) | How do these tools apply to an evolving velocity field? | Verify an exact shear, recover required pressure, and derive its energy budget. |

There are two cumulative assessments. [Assessment A](practice.md#assessment-a), after composition, asks you to design an exact scalar representation of a coupled system and certify a reconstructed prediction from an approximate update. [Assessment B](practice.md#assessment-b), after the fluid equation, compares the full evolution of a two-wave shear with a description keeping fewer frequencies and a numerical time step. Both require a tolerance decision supported by a calculation, including information that the model discarded.

The [fluid laboratory](simulator.md) is available after the equation chapter. Predict the decay of its exact shear benchmark before running it. Its particles are tracers carried by the computed periodic velocity field; the chapter explains what the solver computes and how to compare resolutions.

Two visual examples accompany the course: [a 2D animation of transformation order](transformations.md#map-order-animation), with exact coordinate readouts, and the [3D fluid laboratory](simulator.md), with a numerical velocity field. Both begin paused. Use their controls after making a prediction on paper.

## Before you begin

The first chapter needs algebra, function composition and finite sums.
Derivatives and integrals enter next. The
[calculus bridge](calculus-bridge.md) supplies an introduction to small
matrices, the multivariable chain rule, integral norms and Fourier modes.
It is a reference to revisit while working examples, rather than a substitute
for a full linear algebra or analysis course. No prior operator theory is needed.

Try these three checks before revealing the reasoning. Each difficulty points to a specific prerequisite to revisit.

1. Let $T(x)=2x+1$, $f(x)=x^2$, and start at $x=1$. Find the new state and the change in the observable. Are those the same quantity?
2. If $x(t)=e^t x_0$, differentiate $x(t)^2$. Where does the chain rule enter?
3. Apply $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ to $v=(0,1)^T$. Compare $|Av|^2$ with $|v|^2$. If matrices are new, read [calculus bridge §1](calculus-bridge.md#1-a-vector-is-a-state-with-several-coordinates) first.

<details markdown="1">
<summary>Check your reasoning and find the relevant lesson</summary>

1. The new state is $3$, so its change is $2$. The observable changes from $1$ to $9$, an increase of $8$. [Finite transformations](transformations.md) begins with this distinction.
2. The derivative is $2x(t)x'(t)=2e^{2t}x_0^2$. Differentiating a measurement along a moving state is the starting point of [generators](generators.md).
3. $Av=(1,1)^T$, so the squared length grows from $1$ to $2$. [Composition and error](composition.md) develops the consequences of such amplification for a predicted output and its error.

</details>

## How to use the exercises

The teaching approach takes inspiration from Leonard Bernstein's
[Norton Lectures](https://www.leonardbernstein.com/about/educator/norton-lectures),
where concrete examples carried a sustained argument. Here the examples
are calculations: predict an outcome, work it out, vary one assumption,
then return to the example with a more precise question. The planar shear
reappears as a finite map, a continuous flow and a source of amplification.
Its changing role lets us deepen the mathematics without continually
replacing the object being studied.

Write down the input and output of each map before using it. During a worked proof, cover the next line and try to derive it. Then change one input or reverse two operations and predict what changes in the conclusion.

For an exercise, attempt the calculation before opening a hint or solution. If your answer differs, find the first step where the arguments diverge and redo that step on a simpler example. A correct last formula is not enough if it comes from the wrong composition order or an unstated assumption.

The foundation chapters lead toward the workshop: explaining why a representation is exact or inexact, deriving an accumulated error bound, and converting it to the requested norm and units. One destination is the inequality below; its notation is introduced in [composing two representations](transfer-systems.md#5-composing-two-representations), so you do not need to recognize it before starting:

$$
\|D_{P R}\|\le \operatorname{Lip}(P)\|D_R\|+\|D_P\|
$$

In words: the combined discrepancy is at most the first discrepancy amplified by the next map, plus that map's own discrepancy. You will learn to evaluate these defects at the correct states. Repeating an evolution also requires a separate stability estimate. The [instructor curriculum](../../references/course-outline.md) maps these outcomes to exercises and gives criteria for evaluating the two assessments.

## From the core to the research case studies

After the fluid equation and laboratory, follow [frequency creation](activation.md), [concentrated strain](concentration.md), [steady reference flows](steady.md), [pressure and polarization](oblique.md), and [finite amplification](viscous.md). Each case asks whether a simpler wave calculation reliably describes an actual nonlinear solution. Then study [Residuals and smooth forcing](residuals.md): insert a proposed motion into the complete equation, propagate its residual, and distinguish an approximation error from a force with admissible derivatives. The [iteration chapter](iteration.md) explains which additional hypotheses let finite stages form one evolution.

These chapters introduce research arguments with stated hypotheses. Reading their complete source proofs also requires Fourier analysis, Sobolev estimates, and local existence and continuation theory for PDEs. The core course prepares the transfer questions; the linked notes retain the analytic details.

The [OpenAI release of 8 September 2026](https://openai.com/index/navier-stokes-solution/) reports a smooth-forced breakdown construction establishing the Clay alternatives C and D, accompanied by a written proof and Lean formalization. The [published-proof chapter](published-proof.md) examines that result, its hypotheses and its relationship to this course. The result belongs to its authors; our earlier finite constructions are separate work, not a claimed derivation of their proof.

Our finite estimates provide concrete exercises in wave transport, pressure, approximation and continuation. Their connection to a terminal theorem must be made by matching hypotheses and proving the missing steps. Large finite amplification across changing initial data alone is not a singular evolution from one smooth datum. The repository's unforced target ROOT and separate $(E′)$ estimate remain **open**.

The capstone, [Making a new construction](new-constructions.md), turns this reading into a design problem. It proves a component-replacement estimate and constructs different coupled flows with the same terminal output. It then derives a phase-covariance corollary from the published fluid construction, with a checked Lean statement. An exact shear example shows that preserving average stress can still change the required force. This identifies the next research obligation: construct a modified wave and prove its transport and derivative estimates. The broader fluid replacement problem remains open.

Connecting any singularity theorem to a reliable simulator additionally requires an approximation theorem controlling resolution, time steps and error over a specified interval. The laboratory teaches finite numerical evolution and its benchmarks; the proof chapters teach statements about the continuum equation.

## A second application: information and action

[Information and reliable action](information-action.md) asks which measurements let a controller choose an action that succeeds despite uncertainty. An elementary finite theorem counts the messages needed to choose such an action. A worked interval model then derives exactly how sensing uncertainty, disturbance and control limits determine feasible transitions. The final exercise asks whether one controller delivers a state the next controller can recover from.

This route can be read after transfer systems and composition, without the fluid chapters. It connects to established information and control theory and frames air–water autonomy as a proposed research application, with the model validation and experiments still to be done.

## Using the book as a reference

Every chapter is available as Markdown. The [claim register](../claims.md)
connects research statements to their source proofs; its
[JSON version](../claims.json) records source hashes for this edition.
AI review is not external expert acceptance. Review entries record the checking
process; they are not proof certification.
For the standing of those arguments, consult the
[current status](../../docs/STATUS.md) and the replay and formalization
material in [practice](practice.md). Unsolved Navier–Stokes research is paused;
historical next-attempt notes are preserved checkpoints.

[Begin with finite transformations and observables](transformations.md).
