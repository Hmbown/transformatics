# From one transfer to a complete evolution

A mechanism that works once need not work twice. A mechanism that works
any fixed number of times need not work infinitely often. This chapter
explains the missing mathematics between those statements.

**Prerequisites:** finite composition, the error recurrence in
[composition](composition.md), and the derivative conversions in
[scaling](scaling.md). For the final application, also read
[residuals](residuals.md).

Our first task is concrete: construct a force from infinitely many pulses
whose spatial frequencies increase and whose time intervals shrink, while
keeping the force smooth at the accumulation time. Our second task is to
understand why accomplishing that alone does not construct a fluid solution.

## 1. Three different quantifiers

Consider an assertion $P(h,J)$ about a small parameter $h$ and a
number of stages $J$. These statements have different meanings:

1. For each fixed $J$, there exists $h_J>0$ such that
   $P(h,J)$ holds whenever $0<h<h_J$.
2. For one prescribed function $J(h)\to\infty$, the assertion
   $P(h,J(h))$ holds for all sufficiently small $h$.
3. At one fixed $h$, the assertion holds for every $J$, with the
   compatibility needed to define one infinite construction.

The first does not imply the second for an arbitrary proposed rate.
For example, let

$$
P(h,J)\quad\text{mean}\quad h<\exp(-\exp J).
$$

Every fixed $J$ has a positive threshold. But choosing
$J(h)=\lceil\log(1/h)\rceil$ violates the condition for small $h$: its right
side is at most $\exp(-1/h)$, much smaller than $h$.

The first statement does allow a sufficiently slow *existential*
schedule. Choose decreasing numbers $H_J$ below the first $J$
thresholds and below $H_{J-1}/2$. On
$H_{J+1}<h\le H_J$, use order $J$. This schedule tends to
infinity, but its rate depends on thresholds we may not know explicitly.
It also changes $h$; it establishes no infinite process at one fixed
datum.

This distinction explains two different results in the project's fluid
work: [a slow diagonal schedule](../../references/analysis/diagonal-window.md)
and [a quantitative window for a specified Gevrey class](../../references/analysis/uniform-profile-window.md).
The latter needs bounds on how derivative constants grow with order.
Neither result, by its quantifiers alone, joins infinitely many fluid
stages into one singular trajectory.

## 2. A stage must accept the state it actually receives

Let a stage act on a set $A_j$ of admissible states and produce states
in a set $B_j$. A sequence of stage theorems can be composed only if
the actual output of stage $j$ belongs to $A_{j+1}$.

An output norm bound does not usually establish this membership. A
following stage might require a particular orientation, a sign, a region
where a profile is nearly affine, a phase relation, or a complete pressure
field. Two outputs with the same norm can satisfy different requirements.

For a small finite-dimensional example, define

$$
A_2=\{(x,y):x>0,\ |y|\le x/10\}.
$$

Both $(10,0)$ and $(0,10)$ have Euclidean norm ten. Only the first
is an admissible input for this second stage. Replacing the membership
condition with “the output norm is at least ten” changes the theorem.

A useful stage specification therefore lists the incoming state class,
the complete outgoing state, the protected measurements, and the allowed
error in the next stage's norm. In a fluid problem, a newly generated
Fourier component is one measurement of that state. It is not the whole
state handed to the next interval.

## 3. Summable local errors can still produce an unbounded error

Let $e_j,\delta_j,L_j$ be nonnegative and suppose

$$
e_{j+1}\le L_j e_j+\delta_j,\qquad e_0=0.
$$

Repeated substitution gives

$$
e_J\le\sum_{j=0}^{J-1}\delta_j
                \prod_{k=j+1}^{J-1}L_k.
$$

The product records what happens to an error *after* it is introduced.
It cannot be discarded just because the local errors have a finite sum.

For an exact example, compare scalar updates

$$
x_{j+1}=2x_j+2^{-3j},\qquad y_{j+1}=2y_j,
\qquad x_0=y_0=0.
$$

Their difference is positive and equals

$$
e_J=\sum_{j=0}^{J-1}2^{J-1-j}2^{-3j}
    =2^{J-1}\frac{1-2^{-4J}}{1-2^{-4}}.
$$

Although $\sum_j2^{-3j}<\infty$, the accumulated discrepancy grows
like $2^J$. Earlier errors experience more amplification than later
ones. By contrast, if every $L_j\le1$, the same recurrence gives
$e_J\le\sum_{j<J}\delta_j$.

Neither example settles a nonlinear PDE. They identify a question that
its proof must answer: which propagator acts on the full error, and what
bound is valid for that propagator on the entire interval?

## 4. A smooth train of increasingly fine pulses

We now construct the promised force example. It is a scalar function on
the periodic spatial coordinate $x\in\mathbb R/(2\pi\mathbb Z)$.
The construction applies componentwise to vector-valued functions.

Let

$$
t_j=1-2^{-j},\quad d_j=t_{j+1}-t_j=2^{-j-1},
\quad I_j=(t_j,t_{j+1}),\qquad j\ge1.
$$

Choose a fixed nonzero smooth function $\psi$ supported strictly inside
$(0,1)$, and let

$$
f_j(t,x)=a_j\psi\!\left(\frac{t-t_j}{d_j}\right)
                  \sin(\lambda_j x),\qquad
\lambda_j=2^{j^2},\quad a_j=2^{-j^3}.
$$

The frequencies are integers, so the functions are periodic in $x$.
Define $f=f_j$ on each $I_j$, and set $f=0$ elsewhere,
including at and after $t=1$. The time supports are disjoint and stay
away from the endpoints of their respective intervals. Away from
$t=1$, smoothness is immediate.

For nonnegative integers $m,r$, differentiation gives

$$
\|\partial_t^m\partial_x^r f_j\|_\infty
\le C_m a_j d_j^{-m}\lambda_j^r
=C_m2^{-j^3+m(j+1)+rj^2}.
$$

Fix $m,r$ before letting $j\to\infty$. The negative cubic term
dominates the quadratic and linear terms, so the bound tends to zero.
In fact it tends to zero faster than every fixed power of $1-t$.
Each mixed derivative therefore has continuous extension zero at the
terminal time.

To check that these extended derivatives really are derivatives of the
extended function, proceed inductively. If an extended derivative $g$
and its next time derivative are continuous and both vanish at one,
then, for $t<1$,

$$
\frac{g(t,x)-g(1,x)}{t-1}
=\frac{1}{1-t}\int_t^1\partial_s g(s,x)\,ds
\longrightarrow0.
$$

The convergence is uniform in $x$. Spatial differentiability follows
from the analogous uniform derivative bounds on the compact torus.
Induction over all mixed orders proves $f\in C^\infty$, with every
derivative zero at $t=1$.

This is a complete example of smooth terminal gluing. Rapidly increasing
frequency is compatible with smoothness when the amplitudes pay every
time and spatial derivative cost in one common sequence.

## 5. Smallness at one derivative order is insufficient

Keep the intervals and bump, set $\lambda_j=1$, and instead choose
$a_j=d_j^2$. Then

$$
\|f_j\|_\infty\le C d_j^2\to0,\qquad
\|\partial_t f_j\|_\infty\le C d_j\to0.
$$

The extension is continuously differentiable in time. But

$$
\partial_t^2 f_j(t,x)
=\psi''\!\left(\frac{t-t_j}{d_j}\right)\sin x.
$$

At a fixed interior argument where $\psi''\ne0$, this expression
does not approach zero as the pulse number grows. The extension cannot
be twice continuously differentiable across time one.

The same problem occurs if one controls all spatial derivatives but
forgets time derivatives of an activation cutoff. A smooth force through
a proposed singular time needs *mixed* derivative bounds, not a
zeroth-order force plot or a fixed finite list of spatial estimates.

## 6. One sequence must work for every fixed derivative order

There is an important order of choices in section 4. We selected
$a_j,d_j,\lambda_j$ once. We then proved the bound for each fixed
pair $(m,r)$. We did not choose a different force for each pair.

Suppose, instead, that a construction establishes: “For every order
$m$, there is a sequence of forces that is small through order
$m$.” This does not by itself produce one force small at all orders.
The sequences might be incompatible.

A diagonal selection can sometimes repair this. At stage $j$, enforce
all estimates of orders at most $j$, while preserving the already
chosen earlier stages. For every fixed order, all sufficiently late
stages then satisfy its estimate. But that argument requires a choice
at each stage that meets **all** the simultaneous constraints, including
the incoming-state condition. One cannot diagonalize away a nonexistent
admissible state or change completed stages without accounting for the
change.

The pulse construction is an explicit successful schedule. A fluid
construction has additional equations tying its amplitudes, frequencies,
stress and background together. Those constraints are precisely why the
schedule is part of the proof.

## 7. Where the fluid equation enters

Given smooth preterminal fields $u,p$, define their momentum residual

$$
f=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p.
$$

This identity alone is inexpensive: it defines a force for any proposed
incompressible field. The demanding assertion is that the same $f$
extends smoothly through the terminal time while $u$ does not.
The individual terms in the residual may grow; all required derivatives
of their sum must have the prescribed behavior.

The pulse example in section 4 constructs a smooth function $f$.
It says nothing about whether the solution driven by that function has
unbounded velocity. Conversely, prescribing a velocity with unbounded
size says nothing about whether its residual is an admissible smooth
force. A complete argument must establish both properties for the same
fields and the same time axis.

This is the bridge to the [published forced Navier–Stokes case
study](published-proof.md). Its all-orders cancellation and localization
are substantive mathematical inputs. The earlier finite examples in this
book prepare us to formulate those inputs, but do not imply them merely
by repetition.

## 8. Why finite energy does not prevent a growing maximum

Here is a separate exact scaling calculation. Let
$v_t(x)=A(t)\phi(x/\ell(t))$ on $\mathbb R^3$, with $A(t),\ell(t)>0$, where
$\phi$ is a fixed nonzero compactly supported smooth vector field.
Then

$$
\|v_t\|_\infty=A(t)\|\phi\|_\infty,\qquad
\|v_t\|_2^2=A(t)^2\ell(t)^3\|\phi\|_2^2.
$$

Taking $A(t)=(1-t)^{-1/4}$ and $\ell(t)=(1-t)^{1/2}$
produces an unbounded maximum and squared $L^2$ norm proportional
to $1-t$, which tends to zero. This is a kinematic example; it has
not been shown to solve a momentum equation with an admissible force.

The calculation identifies why an energy estimate cannot substitute
for the missing evolution equation. It also makes a good transfer test:
a proposed norm conversion must include both the amplitude and the volume.

## Exercises

### 1. A prescribed schedule

For $P(h,J):h<e^{-e^J}$, determine whether
$J(h)=\lfloor\tfrac12\log\log(1/h)\rfloor$ eventually satisfies $P$.

<details markdown="1"><summary>Solution</summary>

Put $L=\log(1/h)$. It suffices that $L>\sqrt L$, since $e^{J(h)}\le\sqrt L$,
which holds for $L>1$. Taking an integer floor only decreases the
required right side. This particular slow schedule works, even though
the faster one in section 1 fails.

</details>

### 2. A compatible input

If a stage approximates $(10,0)$ with Euclidean error at most
$\varepsilon$, give a sufficient $\varepsilon$ ensuring that
its output lies in $A_2$ from section 2.

<details markdown="1"><summary>Solution</summary>

The output satisfies $x\ge10-\varepsilon$ and
$|y|\le\varepsilon$. It suffices that
$\varepsilon\le(10-\varepsilon)/10$, or
$\varepsilon\le10/11$. This bound also ensures $x>0$.
The error tolerance was derived from the next stage's actual domain.

</details>

### 3. Slow derivative decay

Use $d_j=2^{-j-1}$, $\lambda_j=2^j$, and $a_j=2^{-10j}$.
Which fixed mixed orders does the simple derivative bound prove tend to
zero? Does it prove all-orders smooth terminal extension?

<details markdown="1"><summary>Solution</summary>

The bound is $C_m2^m2^{(-10+m+r)j}$, which tends to zero when
$m+r<10$. At equality it is merely bounded; above equality it
grows. This estimate supplies no all-orders extension. For a nontrivial
bump and sine mode, suitable interior evaluations show the failure at
some higher orders directly.

</details>

### 4. An anisotropic volume

A three-dimensional profile has two radial lengths
$\ell_r=\tau^\alpha$, one axial length
$\ell_z=\tau^\beta$, and velocity amplitude $\tau^{-\gamma}$.
Find its squared $L^2$ scaling and the condition for it to vanish as
$\tau\downarrow0$.

<details markdown="1"><summary>Solution</summary>

The Jacobian is $\ell_r^2\ell_z=\tau^{2\alpha+\beta}$, so the
squared norm scales as $\tau^{2\alpha+\beta-2\gamma}$.
It vanishes when $2\alpha+\beta>2\gamma$. The maximum can still
diverge if $\gamma>0$. This calculation imposes no momentum equation.

</details>

### 5. Diagnose an infinite-stage argument

A proposed proof shows smooth existence on each prescribed finite scale
interval, a summable list of interval lengths, and force amplitude tending
to zero. Name three additional statements needed before these facts could
describe one admissible forced singular evolution.

<details markdown="1"><summary>Solution</summary>

One needs compatible actual endpoint states belonging to the next stage's
input class; one common force with every mixed derivative controlled through
the accumulation time; and a proof of the claimed unbounded observable for
the same solution, with its required energy and spatial conditions. Error
propagation and uniqueness must also justify that the assembled pieces
solve the stated equation. Many separate finite solutions are insufficient.

</details>

### 6. Restore the missing amplification factors

For the scalar updates in section 3, replace $2^{-3j}$ by
$2^{-j^2}$. Does the discrepancy remain bounded as $J\to\infty$?

<details markdown="1"><summary>Solution</summary>

No. Its first term alone is $2^{J-1}$. Faster decay of later defects
cannot undo amplification of the first positive defect in this recurrence.
A different construction would need a different stability mechanism,
compatible cancellation, or a different protected observable, each proved.

</details>

## From one step to a whole evolution

Finite transformations describe one step. A complete transfer argument
also specifies the domains of successive steps, the propagation of their
errors, the order of its quantifiers and the regularity of any limiting
object. The examples show why each requirement matters: a compatible
endpoint, summable propagated errors, and the right order of choices are
different things to establish before a local calculation can describe
a whole evolution.
