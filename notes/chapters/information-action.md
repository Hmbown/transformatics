# Information and reliable action

A slider sits at either $x=-1$ or $x=1$. A controller can move it
one unit left or right. The goal is to place it at zero.

Suppose the sensor reports $x^2$. Its reading is $1$ in both cases.
Moving left succeeds from $1$ and fails from $-1$; moving right does
the opposite. Each possible state has a successful action, but the
controller cannot choose between them from this measurement.

Now let the sensor report the sign. One bit resolves the problem. Yet a
more accurate measurement of $x^2$ would accomplish nothing: both states
have exactly the same square. Useful information distinguishes situations
that require different actions.

This chapter makes that statement precise. We will first use finite sets,
then solve an interval model in which measurement uncertainty, disturbance
and control limits compete. The prerequisites are functions, intersections
of sets, inequalities and the meaning of a logarithm. The mathematical
foundations belong to existing control and information theory. Here they
become another application of the [transfer-system viewpoint](transfer-systems.md):
specify the state, the information retained, the allowed transformation
and the set of acceptable outputs.

## 1. Which action works for everything the observation allows?

Let $X$ be a finite nonempty state set and $\mathcal U$ a finite
nonempty control set. Let $W$ be a nonempty set of disturbances, and
suppose a model specifies the next state
$$
x^+=F(x,u,w).
$$
A chosen **receiver set** $R$ contains acceptable next states.
Any additional constraints must also be specified in the model.
For each state define its successful controls:
$$
A(x)=\{u\in\mathcal U:
       F(x,u,w)\in R\text{ and all constraints hold for every }w\in W\}.
$$
The universal quantifier is essential. Success here means success for
every allowed disturbance, with no probability distribution assumed.

An observation map $h:X\to Y$ supplies the reading $y=h(x)$.
The **observation fiber**
$$
F_y=\{x\in X:h(x)=y\}
$$
contains all states consistent with that reading. A deterministic
observation-based controller chooses one control $\pi(y)$, so it must
use the same control at every state in this fiber.

**Common-action theorem.** A controller that succeeds at every state
exists exactly when
$$
\bigcap_{x\in F_y}A(x)\ne\varnothing
\quad\text{for every realized observation }y\in h(X).
\tag{1}
$$

**Proof.** If a successful controller exists, its chosen $\pi(y)$
belongs to every $A(x)$ in the fiber, so the intersection is nonempty.
Conversely, choose one control from each nonempty intersection and define
$\pi(y)$ to be that control. There are only finitely many realized
observations. By construction it succeeds for every state and disturbance.
$\square$

The theorem distinguishes two failures. If $A(x)$ is empty, no
observation can make the available controls sufficient at $x$.
If all $A(x)$ are nonempty but a fiber intersection is empty, the
measurement groups incompatible control requirements together.

Refining an observation splits its fibers into smaller sets. Any control
that worked on an old fiber still works on each smaller one. Thus more
information cannot destroy feasibility when the model and available
controls remain fixed. Whether it creates feasibility depends on which
states the new information separates.

## 2. How many messages are enough?

Consider a different arrangement. An encoder knows the exact state $x$.
It sends a noiseless binary message to a decoder, which selects the control.
Every message has the same fixed length $b$, and the decoder has no
other state information. How small can $b$ be?

For each control $u$, define its success set
$$
S_u=\{x\in X:u\in A(x)\}.
$$
Assume these sets cover $X$. Let $K$ be the smallest number of
controls whose success sets still cover $X$:
$$
K=\min\left\{|C|:C\subseteq\mathcal U,\quad
                 X=\bigcup_{u\in C}S_u\right\}.
\tag{2}
$$
Because $X$ and $\mathcal U$ are finite and nonempty, this minimum
exists and $K\ge1$.

**Finite zero-error coding theorem.** The smallest fixed message length is
$$
b_{\min}=\lceil\log_2 K\rceil.
\tag{3}
$$

**Proof.** A decoder receiving $b$ bits can select at most $2^b$
distinct controls. Their success sets must cover all states, so
$K\le2^b$. Conversely, take a cover using $K$ controls and assign
each one a distinct message of length $\lceil\log_2K\rceil$.
At each state the encoder selects one covering control and sends its
message. That control succeeds for every disturbance. $\square$

For $K=1$, zero bits suffice: the decoder always uses the same action.
If no cover exists, no number of bits repairs the lack of a successful
control at some state.

Notice what is being compressed. The decoder needs enough information
to choose a successful action; it need not reconstruct the exact state.
Also notice who knows what. An encoder seeing only $h(x)$ cannot split
an observation fiber. Shared side information would change the coding
problem and must be included explicitly.

Equation (3) is a one-step, deterministic, worst-case count. It is not a
claim about average entropy, a noisy channel's capacity, or an asymptotic
rate over repeated control steps. Shannon's
[A Mathematical Theory of Communication](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1948.tb00917.x)
provides the foundational communication setting; the finite covering
argument above is proved directly under its own narrower assumptions.

## 3. A continuous model we can solve completely

We now allow real-valued states and controls. The interval calculation
below is direct; applying the finite coding theorem to a discretization
would require proving that the discretization preserves its guarantees.

Let
$$
x^+=x+u+w,\qquad |x-y|\le\varepsilon,\qquad
|w|\le d,\qquad |u|\le U,
$$
and take $R=[-b,b]$, where $b,\varepsilon,d,U$ are nonnegative.
The measurement $y$ leaves $x$ somewhere in
$[y-\varepsilon,y+\varepsilon]$.

Before calculating, predict what a control can change. Adding $u$
moves the whole possible-output interval, but does not shrink it.
Measurement uncertainty and disturbance determine its width:
$$
x^+\in[y+u-(\varepsilon+d),\,y+u+(\varepsilon+d)].
$$
This interval lies inside $[-b,b]$ exactly when
$$
|y+u|+\varepsilon+d\le b.
\tag{4}
$$
Put $r=b-\varepsilon-d$. If $r<0$, no control succeeds.
If $r\ge0$, the complete set of successful controls is
$$
[-U,U]\cap[-y-r,-y+r].
\tag{5}
$$
Two closed intervals intersect precisely when their centers are no
farther apart than the sum of their radii. Therefore robust feasibility is
equivalent to
$$
\boxed{\ \varepsilon+d\le b,\qquad |y|\le U+b-\varepsilon-d.\ }
\tag{6}
$$

Take $b=1$, $d=0.2$, $\varepsilon=0.3$ and $U=0.4$.
Then $r=0.5$, so the acceptable measurements satisfy $|y|\le0.9$.
At $y=0.8$, (5) gives $u\in[-0.4,-0.3]$.
Choosing $u=-0.3$ produces the full output interval $[0,1]$;
checking only the nominal value $y+u=0.5$ would have missed its
worst-case endpoints.

Now vary one parameter. Reducing $\varepsilon$ to $0.2$ increases
$r$ to $0.6$, and $u=-0.2$ suffices at the same measurement.
The improvement comes from reducing uncertainty, not from increasing
actuator authority. Conversely, if $\varepsilon+d>b$, making $U$
arbitrarily large cannot help: the possible-output interval is too wide.

## 4. Paying for an action

Suppose we additionally **assume** a cost model $c u^2\le E$, with
$c>0$ and $E\ge0$. This is a mathematical budget; interpreting it
as physical energy would require calibrated units and an experimentally
supported actuator model.

The effective control limit becomes
$$
U_{\rm eff}=\min\{U,\sqrt{E/c}\}.
\tag{7}
$$
Use $U_{\rm eff}$ in (5)–(6). When $r\ge0$, the least control
magnitude capable of reaching the receiver is
$$
u_{\min}=\max\{0,|y|-r\},
\tag{8}
$$
provided $u_{\min}\le U$. This follows by choosing the point of
$[-y-r,-y+r]$ nearest zero. Its least cost is $c u_{\min}^2$.

In the preceding example $u_{\min}=0.3$. For $c=2$, the least
cost is $0.18$. A budget $E=0.16$ therefore fails, even though the
original actuator bound $U=0.4$ allows the action. Reducing
$\varepsilon$ to $0.2$ makes the least cost $2(0.2)^2=0.08$.
Better information and a larger control budget can sometimes substitute
for each other, but (6) shows exactly where that substitution stops.

## 5. From one transition to a vehicle research question

For a vehicle moving between air and water, a state might include
position, velocity, orientation, remaining actuation budget and the
estimated surface configuration. A proposed transition model would map
that state and a control sequence to a receiving state under uncertain
waves, currents and model errors.

The receiver should describe a state from which the next controller can
recover. Merely crossing the surface is not enough if the resulting
orientation or speed prevents subsequent control. This is the same
handover requirement studied in [composition](composition.md):
one stage must deliver what the next stage requires.

The exact research question is then whether each relevant observation
fiber has a common successful transition. A richer sensor, a different
maneuver or a larger control allowance changes different parts of that
question. None is guaranteed to repair every empty intersection.

Using this formulation on hardware would require a validated transition
model and receiver set. Uncertainty bounds should be tested on held-out
conditions, and the resulting controller compared with a stated baseline
on transition success, recovery and measured resource use. Finite testing
can challenge a model and measure performance; it cannot by itself prove
a universal disturbance bound.

Aquatic–aerial vehicles already have an experimental literature. For
example, Kun Liu and coauthors' [SurfAAV study](https://arxiv.org/abs/2506.15450)
reports a vehicle combining underwater navigation, surface gliding and
flight. It is a relevant engineering reference, not evidence for the
performance of a vehicle designed with this chapter's proposed workflow.

There is also a substantial mathematical lineage. Tomar, Rungger and
Zamani study information requirements for maintaining invariance in
[uncertain control systems](https://arxiv.org/abs/1706.05242).
Tanaka, Mohajerin Esfahani and Mitter study directed information under
performance constraints in [linear-quadratic-Gaussian control](https://arxiv.org/abs/1510.04214).
Those works address richer temporal or probabilistic settings. Our
elementary intersections and finite covers provide an entry point,
without claiming their stronger conclusions or a new information theory.

## 6. Exercises

### Exercise 1 — Every pair agrees, but the whole group does not

Three states have successful-action sets
$$
A(x_1)=\{a,b\},\qquad A(x_2)=\{b,c\},\qquad A(x_3)=\{a,c\}.
$$
All three produce the same observation. Can an observation-based
controller succeed? If an encoder instead knows the exact state, how
many fixed-length bits suffice?

<details markdown="1">
<summary>Solution</summary>

The three pairwise intersections are nonempty, but the intersection
of all three sets is empty. No one action works for the observed fiber.

Two controls suffice with an informed encoder: send one message selecting
$b$ at $x_1,x_2$, and another selecting $a$ at $x_3$.
No single control succeeds everywhere, so $K=2$ and one bit is
necessary and sufficient. An encoder seeing only the common observation
cannot implement this state-dependent message.

</details>

### Exercise 2 — Find the measurement precision the budget requires

Use the scalar model with $y=0.8$, $b=1$, $d=0.2$,
$U=0.4$, $c=2$ and $E=0.18$.
What is the largest admissible $\varepsilon\ge0$?
Find the successful control at that limiting precision.

<details markdown="1">
<summary>Solution</summary>

Equation (7) gives $U_{\rm eff}=0.3$.
The first feasibility condition gives $\varepsilon\le0.8$.
The second gives
$0.8\le0.3+1-\varepsilon-0.2$, hence
$\varepsilon\le0.3$. Their joint limit is $0.3$.

At this limit $r=0.5$, and the intersection in (5) is
$[-0.3,0.3]\cap[-1.3,-0.3]=\{-0.3\}$.
This unique control costs exactly $0.18$ and delivers $[0,1]$.

</details>

### Exercise 3 — A receiver that survives the next step

After the first transition, suppose the exact new state $z$ is observed.
The following step is
$$
z^+=2z+v+w,\qquad |v|\le\tfrac14,\qquad |w|\le\tfrac1{10}.
$$
Find every $z$ from which some chosen $v$ guarantees $z^+\in[-1,1]$.
Why would a first-stage guarantee of only $z\in[-1,1]$ be insufficient?

<details markdown="1">
<summary>Solution</summary>

For the observed state $z$, success requires
$|2z+v|+1/10\le1$.
The admissible control intervals intersect exactly when
$$
|2z|\le\tfrac14+\tfrac9{10}=\tfrac{23}{20}.
$$
Thus the recoverable receiver is
$[-23/40,23/40]$.
The first stage must deliver into this smaller interval to guarantee
the stated next-step recovery. For example $z=1$ belongs to
$[-1,1]$, but even $v=-1/4$ leaves the nominal next state at
$7/4$, outside the target. These are two-step guarantees under the
given observations, not a proof of indefinite invariance.

</details>
