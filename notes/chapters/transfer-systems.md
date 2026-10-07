# Transfer systems: what a model is allowed to predict

Suppose a measuring device reports the square of a real number. At one
instant it reads $4$. If the number changes sign, the next reading is
still $4$. If the number increases by one, the next reading could be
$9$ or $1$. The same measurement is sufficient for one evolution and
insufficient for another. A representation is useful because of its
relationship to an evolution, not merely because it compresses a state.

The [finite-transformation chapter](transformations.md) taught us to
calculate a measurement after an update. [Generators](generators.md)
connected those updates to differential equations. We now compare whole
descriptions of an evolution. Our central theorem will show exactly how
errors accumulate when one representation is followed by another.

You need function composition, the triangle inequality, the chain rule,
and multiplication of small matrices. The chapter develops the required
notions of a norm and a Lipschitz bound through examples. These are
classical mathematical tools. The
[calculus bridge](calculus-bridge.md#4-norms-say-which-error-matters)
is available for a first encounter with norms. Experienced readers can
begin with the factor criterion in Section 3 and the composition estimate
in Section 5; the [reading map](reader-map.md) gives their standard connections.

## 1. Specify the evolution before comparing it

A state is the input needed to determine the motion. An observable is a
quantity computed from that state. They may have different types: the
state of an oscillator is a position–velocity pair, while its energy is a
single number. The energy need not determine the pair's later motion.

For a fixed interval $I=[0,T]$, an **evolution family** on a set $X$
consists of maps

$$
\Phi_{t,s}:X\to X,\qquad 0\le s\le t\le T,
$$

satisfying

$$
\Phi_{s,s}=\operatorname{id}_X,
\qquad
\Phi_{t,r}\circ\Phi_{r,s}=\Phi_{t,s}
\quad(s\le r\le t).
$$

The second equation says that stopping at an intermediate time does not
change the final state. Two time labels allow an evolution law to depend
on the current time. For $x'=t x$, for example,

$$
\Phi_{t,s}(x)=e^{(t^2-s^2)/2}x.
$$

Multiplication of these factors verifies the law. Its dependence on both
$s$ and $t$ cannot be replaced by dependence on $t-s$ alone. For an
autonomous flow we may instead write $\Phi_{t,s}=T_{t-s}$. Discrete
evolution uses integer times and compositions of successive updates.

Our definition assumes existence on the stated interval for all states
in $X$. A local differential equation may not supply that. The solution
of $x'=x^2$, started at $x_0>0$, is

$$
x(t)=\frac{x_0}{1-tx_0},\qquad 0\le t<1/x_0.
$$

Any comparison with this solution must end before its denominator vanishes.
For a local evolution, use only states and time pairs on which every map
in a proposed composition exists. Writing a symbol for a later-time map
is not a proof of its existence.

## 2. A representation is another map with a stated purpose

Let $Y$ be a second state space, with evolution $\Psi_{t,s}$. A
**representation** is a map $R_t:X\to Y$; its time dependence is allowed
but not required. It may record a Fourier coefficient, change coordinates,
rescale a field, or discard part of a vector. Its output is a model state.
An observable $g:Y\to\mathbb R$ then measures that state.

Here is the complete collection of objects for one comparison.

| Object | Meaning | What must be supplied |
|---|---|---|
| $X,\Phi_{t,s}$ | Detailed states and their evolution | Admissible states and time domain |
| $Y,\Psi_{t,s}$ | Represented states and their proposed evolution | A rule defined on every state used |
| $R_t:X\to Y$ | Information retained at time $t$ | Its formula, domain, and any time dependence |
| $f:X\to\mathbb R,\ g:Y\to\mathbb R$ | Desired and predicted measurements | The relation between the two measurements |
| A norm on $Y$ | Size of a representation error | Normalization and units |
| A stability bound | Response to perturbed inputs | Region, interval, and constant dependencies |

These entries constitute a *transfer problem*. There is no universal norm
attached to it. On $\mathbb R^2$, the Euclidean norm is
$|v|_2=(v_1^2+v_2^2)^{1/2}$. Another norm may weight one coordinate more
heavily. For fields, velocity error and derivative error are different
measurements. A claim of accuracy is incomplete until it selects one.

It is often useful to reconstruct an approximate detailed state with a map
$L_t:Y\to X$. Reconstruction is additional information; it is not part
of the definition of a representation and need not invert $R_t$.

## 3. Exact transfer and the test for lost information

**Definition 3.1.** The representation transfers the evolution **exactly**
when

$$
\boxed{R_t\Phi_{t,s}(x)=\Psi_{t,s}R_s(x)}
$$

for every admissible state and time pair. The left side evolves the
detailed state and then represents it. The right side represents first
and evolves the resulting model state. Exact transfer means these two
routes agree; it does not mean that the representation can recover all
details of the original state.

For one autonomous discrete update, there is a precise test for whether
an exact represented update can exist.

**Proposition 3.2 (information required for one step).** Given
$T:X\to X$ and $R:X\to Y$, a map $S:R(X)\to R(X)$ satisfying
$RT=SR$ exists if and only if

$$
R(x)=R(x')\quad\Longrightarrow\quad R(Tx)=R(Tx').
$$

If it exists, $S$ is unique on the image $R(X)$.

**Proof.** Necessity follows by applying $S$ to the common value
$R(x)=R(x')$. For sufficiency, define $S(y)=R(Tx)$ using any state
with $R(x)=y$. The displayed condition says that every such choice gives
the same output. That output belongs to $R(X)$, since $Tx\in X$.
Every value of $S$ on the image is forced by this rule. $\square$

The theorem concerns algebraic existence. Continuity, differentiability,
or a useful stability constant for $S$ require further arguments.
There is also no specified value for $S$ outside $R(X)$.

Apply the test to $R(x)=x^2$. For $T(x)=-x$, we have
$R(Tx)=x^2$, so the exact model is $S(y)=y$ on $[0,\infty)$.
The representation loses the sign, but the sign is irrelevant to all
future squared measurements under this update. For $T(x)=x+1$, the
states $2$ and $-2$ have the same representation and later readings
$9$ and $1$. No exact model using the square alone can predict both.
More accurate arithmetic cannot restore the missing sign.

## 4. Approximate transfer and observable error

Assume now that $Y$ is a normed vector space. Define the **transfer
defect** over the stated time interval by

$$
D_R(t,s;x)=R_t\Phi_{t,s}(x)-\Psi_{t,s}R_s(x)\in Y.
$$

An approximate transfer statement bounds its norm on a specified set of
states. A bound at one state is not automatically uniform over that set.
The subtraction is in $Y$; no subtraction of abstract states in $X$
has been assumed.

Suppose $x_t$ is the detailed state, $y_t$ the computed model state,
and $e_t=\|R_t x_t-y_t\|_Y$. To predict an observable, we also need to
compare $f$ with $g\circ R_t$. If at the detailed state

$$
|f(x_t)-g(R_t x_t)|\le a_t
$$

and $g$ is $C_g$-Lipschitz between the represented and computed
states, then adding and subtracting $g(R_t x_t)$ gives

$$
\boxed{|f(x_t)-g(y_t)|\le a_t+C_g e_t.}
$$

“Lipschitz” means that output distances are at most $C_g$ times input
distances on the stated region. For $g(y)=y^2$ with $|y|\le M$,
the factorization $u^2-v^2=(u-v)(u+v)$ gives $C_g=2M$. There is
no finite global Lipschitz constant for the square on all of $\mathbb R$.
Thus even an observable conversion has a region of validity.

The term $a_t$ measures information lost by the chosen representation;
$e_t$ measures its dynamical or computational error. Zero transfer defect
does not force $a_t=0$. If $X$ is also normed and reconstruction is
used, the analogous calculation is

$$
\|x_t-L_t y_t\|_X
\le\|x_t-L_tR_t x_t\|_X+C_L\|R_t x_t-y_t\|_Y,
$$

provided $L_t$ is $C_L$-Lipschitz on the required pair. The first
term survives even when the model evolves its retained information exactly.

## 5. Composing two representations

Suppose a second representation $P_t:Y\to Z$ converts the first model
into a third description, evolved by $\Theta_{t,s}$. Take $Y,Z$
to be normed vector spaces. Define

$$
D_P(t,s;y)=P_t\Psi_{t,s}(y)-\Theta_{t,s}P_s(y).
$$

**Theorem 3.3 (quantitative composition).** Fix an admissible $s,t,x$.
Suppose all the displayed maps exist, and $P_t$ is $L_P$-Lipschitz
between the points $R_t\Phi_{t,s}(x)$ and $\Psi_{t,s}R_s(x)$.
Then the composite representation $(PR)_t=P_tR_t$ satisfies

$$
\boxed{
\|D_{PR}(t,s;x)\|_Z
\le L_P\|D_R(t,s;x)\|_Y
+\|D_P(t,s;R_s x)\|_Z.}
$$

In particular, exact transfer through both representations gives exact
transfer through their composition.

**Proof.** Insert the intermediate term $P_t\Psi_{t,s}R_s(x)$:

$$
\begin{aligned}
D_{PR}(t,s;x)
={}&P_t(R_t\Phi_{t,s}x)-P_t(\Psi_{t,s}R_sx)\\
&+P_t\Psi_{t,s}R_sx-\Theta_{t,s}P_sR_sx.
\end{aligned}
$$

The last line is $D_P(t,s;R_sx)$. Bound the first line by the Lipschitz
constant and apply the triangle inequality in $Z$. $\square$

Notice where the second defect is evaluated: at the represented **initial**
state $R_sx$. Notice also that the first defect is measured in $Y$
before its conversion to $Z$. Adding the two error numbers without that
conversion would generally be wrong.

For a chain of three representations, with defect bounds $d_1,d_2,d_3$
and Lipschitz constants $L_2,L_3$ for the last two representations,
repeated application gives

$$
d_{\mathrm{total}}\le L_3L_2d_1+L_3d_2+d_3.
$$

The first error passes through both later conversions. This is composition
across descriptions at one chosen interval. [Composition and
error](composition.md) separately derives propagation across successive
time steps. A calculation may require both kinds of composition.

## 6. Two calculations that test the theorem's hypotheses

First take one-step scalar systems

$$
T(x)=x+\varepsilon,\quad S(y)=y,\quad R(x)=x,
\quad P(y)=Ky,\quad H(z)=z,
$$

where $K>0$. The first defect is $D_R=\varepsilon$. The second
representation is exact because $PS=HP$, so $D_P=0$. Yet

$$
D_{PR}=P(Tx)-H(Px)=K\varepsilon.
$$

The theorem gives equality: $L_P=K$. With $\varepsilon=10^{-6}$
and $K=10^6$, the final defect is $1$. A small number in one set of
units or coordinates need not be a small error in the requested output.

Next examine the matrix

$$
A=\begin{pmatrix}1/2&2\\0&1/2\end{pmatrix}.
$$

Both eigenvalues are $1/2$, but for $v=(0,1)^T$,

$$
Av=(2,1/2)^T,\qquad |Av|_2=\sqrt{17}/2>2|v|_2.
$$

It is therefore false that every error contracts by a factor $1/2$
at every step in the Euclidean norm. The off-diagonal entry converts the
second coordinate into the first. Write $A=\tfrac12 I+B$, where
$B^2=0$. The binomial expansion, with every term beyond the first two
zero, gives for $n\ge1$

$$
A^n=\begin{pmatrix}2^{-n}&n2^{2-n}\\0&2^{-n}\end{pmatrix}.
$$

For each fixed vector the eventual limit is zero, while intermediate
amplification is possible. Eventual decay and a one-step stability bound
are distinct statements.

Can another norm help? Set $\|v\|_*=|v_1|+8|v_2|$. Directly,

$$
\|Av\|_*\le\tfrac12|v_1|+6|v_2|
\le\tfrac34\|v\|_*.
$$

This is a valid contraction estimate, but returning to Euclidean length
costs a norm conversion:

$$
|v|_2\le\|v\|_*\le\sqrt{65}|v|_2,
\qquad
|A^n v|_2\le\sqrt{65}(3/4)^n|v|_2.
$$

The first inequality follows because the weighted sum dominates the
ordinary sum of absolute coordinates. The second is Cauchy–Schwarz.
The conversion factor allows early Euclidean amplification. Changing the
norm can simplify the proof; it cannot erase the cost of the original
measurement.

## 7. Exercises: build and test a transfer statement

Attempt each exercise before opening the solution. An answer should name
the state spaces and the interval or region where its estimate holds.

**1. An exact quotient.** On $X=\mathbb R^2$, let
$T(a,b)=(a+b,a+b)$ and $R(a,b)=a+b$. Find the unique exact represented
map on $Y=\mathbb R$. Does the reconstruction $L(y)=(y/2,y/2)$
recover every input? What happens after one step?

<details markdown="1">
<summary>Solution: exact evolution with initially missing information</summary>

We have $R(T(a,b))=2(a+b)$, so $S(y)=2y$. The representation is
onto, and Proposition 3.2 gives uniqueness. Initially,
$LR(a,b)=((a+b)/2,(a+b)/2)$, which equals $(a,b)$ only if $a=b$.
After one step, $LSR(a,b)=(a+b,a+b)=T(a,b)$. This update itself removes
the missing difference. Exact representation alone did not imply exact
initial reconstruction; the extra property of this update gives exact
reconstruction at later integer times.

</details>

**2. A nonlinear conversion.** At one time pair, two intermediate states
lie in $[-3,3]$ and differ by at most $0.01$. The next representation
is $P(y)=y^2$, whose own transfer defect is at most $0.002$. Bound
the composite defect. Why must the region appear in your answer?

<details markdown="1">
<summary>Solution: the derivative bound has a domain</summary>

On this interval, $|u^2-v^2|\le6|u-v|$. Theorem 3.3 gives
$6(0.01)+0.002=0.062$. Without a bound on $|u+v|$, the same
input difference has arbitrarily large squared-output difference. A
derivative formula supplies no uniform constant on an unbounded region.

</details>

**3. A time-domain obstruction.** For $x'=x^2$, compare initial states
$x_0$ and $x_0+\varepsilon$, both in $[0,a]$, with $a>0$.
Derive a uniform difference bound on $[0,T]$, where $T<1/a$.
Can the same argument give a finite bound at $T=1/a$?

<details markdown="1">
<summary>Solution: stability depends on staying within the existence interval</summary>

The derivative of $x\mapsto x/(1-tx)$ is $(1-tx)^{-2}$.
For $0\le x\le a$ and $0\le t\le T$, it is at most
$(1-Ta)^{-2}$. The mean value theorem gives difference at most
$|\varepsilon|/(1-Ta)^2$. At $T=1/a$, the state starting at $a$
has no finite value. Both the evolution domain and the proposed uniform
constant fail. This is not repaired by selecting a smaller arithmetic
rounding error.

</details>

**4. Match the observable.** For the matrix in Section 6, take
$f(v)=v_1$ and $g(v)=|v|_2^2$. Is a bound of $0.01$ on state
error sufficient to certify a bound of $0.01$ on each observable error?
Assume for the second comparison that both states have Euclidean norm at
most $M$.

<details markdown="1">
<summary>Solution: linear and quadratic measurements respond differently</summary>

The coordinate observable satisfies $|f(v)-f(w)|\le|v-w|_2$, so its
error is at most $0.01$. For the squared length,
$|g(v)-g(w)|=|(v+w)\cdot(v-w)|\le2M|v-w|_2$, giving $0.02M$.
The state-error assumption alone does not certify the requested quadratic
tolerance for arbitrary $M$. No matrix-eigenvalue argument changes
this observable conversion.

</details>

Continue to [Composition and the cost of error](composition.md) to
derive time-step accumulation. The first [cumulative
assessment](practice.md#assessment-a) then asks you to build a complete
transfer statement without being given the representation in advance.
