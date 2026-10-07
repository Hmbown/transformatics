# Finite transformations and their calculus

Begin with the update $x\mapsto2x+1$. It increases the number $x$
by $x+1$. To find the increase in its square, however, we must square
the new value before subtracting the old one:

$$
(2x+1)^2-x^2=3x^2+4x+1.
$$

The update is one object; the quantity measured is another. We call the
current number a **state**, the update a **transformation**, and the square
an **observable**. Keeping these objects separate lets us ask the same
question about position, energy, or any other measurement of a state.

Starting from zero, the successive states are $0,1,3,7$, and their
squares are $0,1,9,49$. The total increase is $49$. A useful calculus
should recover that answer by adding the three changes, and should tell
us how to do so when no formula for the last state is available. We will
develop its product rule, composition rule and summation rule from ordinary
algebra.

No limiting process is needed for these rules. Function composition,
polynomial algebra and finite sums suffice; one integral reformulation
uses the fundamental theorem of calculus. In the [next chapter](generators.md),
we will take a limit and see how the differential rules emerge from the
finite ones.

## 1. States and observables

**Definition 1.1 (state, transformation, observable).** A *state space* is a set $X$. A *transformation* is a map $T:X\to X$. A real-valued *observable* is a function $f:X\to\mathbb R$.

The state contains the information on which the update depends. An observable selects a quantity from that information. For a particle, the state might contain position and momentum, while an observable gives kinetic energy. For an iterative calculation, the state might be a vector of numbers and an observable its squared length. The same definitions also apply to a finite set of configurations, where differentiation need not make sense.

Our choice of $X$ must make the transformation well-defined. For example, $T(x)=1/x$ is a transformation of $\mathbb R\setminus\{0\}$, but not of all $\mathbb R$. If repeated updates are intended, each output must remain an admissible input.

An observable need not distinguish every pair of states. On $X=\mathbb R$, the observable $f(x)=x^2$ gives the same value at $x$ and $-x$. An unchanged measurement therefore does not necessarily mean an unchanged state.

We use $(T\circ S)(x)=T(S(x))$: the rightmost map acts first. In an expression such as $fg$, however, we mean the pointwise product $(fg)(x)=f(x)g(x)$, not composition. Keeping these two operations separate will matter in the product and composition laws.

## 2. Moving the transformation onto the observable

There are two equivalent ways to predict a reading. We may update the
state and apply the old observable, or form a new observable that already
includes the update and evaluate it at the original state. The second
description is especially convenient when several measurements follow the
same motion.

**Definition 1.2 (pullback).** The *pullback* associated with $T$ is the operator

$$
U_Tf=f\circ T,\qquad (U_Tf)(x)=f(T(x)).
$$

Here $U_T$ takes a function as input and returns another function. The new function answers: “What will this observable read after the update, if the present state is $x$?”

For reference, write $\mathcal F(X)$ for the set of all real-valued functions on $X$. The types of the objects are

| Object | Input | Output |
|---|---|---|
| $T:X\to X$ | A state $x$ | The updated state $T(x)$ |
| $f:X\to\mathbb R$ | A state $x$ | A measurement $f(x)$ |
| $U_T:\mathcal F(X)\to\mathcal F(X)$ | An observable $f$ | The observable $f\circ T$ |

For our running example, $T(1)=3$, $f(1)=1$, and $(U_Tf)(1)=f(3)=9$. The expression $U_Tf$ is a function; the expression $(U_Tf)(1)$ is a number. We introduce an operator on functions because it allows us to compare several measurements under the same update.

**Proposition 1.3 (pullbacks preserve observable algebra).** For observables $f,g$, real constants $a,b$, and the constant observable $1$,

$$
U_T(af+bg)=aU_Tf+bU_Tg,\qquad
U_T(fg)=(U_Tf)(U_Tg),\qquad U_T1=1.
$$

**Proof.** At each $x\in X$,

$$
(af+bg)(T(x))=af(T(x))+bg(T(x)),
$$

and $(fg)(T(x))=f(T(x))g(T(x))$. A constant function has the same value at every input. These pointwise equalities prove the operator identities. $\square$

Thus $U_T$ is linear in the observable even when $T$ is nonlinear
in the state. For $T(x)=x^2$, the pullback sends the coordinate $x$
to $x^2$, then to $x^4$, and so on. The operator is linear, but this
sequence does not stay in a fixed finite-dimensional polynomial space.
Section 4 will give an example where such a space does close, allowing
every pullback to be calculated by a small matrix.

## 3. The exact finite difference

**Definition 1.4 (difference along a transformation).** Write $I$ for the identity operator on observables. Define

$$
\Delta_T=U_T-I,\qquad
\Delta_Tf(x)=f(T(x))-f(x).
$$

The identity operator on functions is different from the identity transformation on states, although pulling back by the identity transformation gives the identity operator.

The expression $\Delta_Tf$ is an observable: the amount by which $f$ changes depends on the starting state. It is linear in $f$ and annihilates constants. If $X=\mathbb R$ and $T_h(x)=x+h$, then it becomes the usual forward difference $f(x+h)-f(x)$. General transformations allow the displacement to depend on the state, or allow states that are not numbers at all.

**Proposition 1.5 (finite product law).** For any two observables,

$$
\boxed{\Delta_T(fg)
=f\,\Delta_Tg+g\,\Delta_Tf+(\Delta_Tf)(\Delta_Tg).}
$$

Equivalently,

$$
\Delta_T(fg)=(U_Tf)\,\Delta_Tg+g\,\Delta_Tf.
$$

**Proof.** Set $a=\Delta_Tf$ and $b=\Delta_Tg$. Then $U_Tf=f+a$ and $U_Tg=g+b$. Proposition 1.3 gives

$$
\Delta_T(fg)=(f+a)(g+b)-fg=fb+ga+ab.
$$

Grouping the first and last terms gives the second form. $\square$

The extra product measures the interaction of the two finite changes. For a rectangle with side lengths $f$ and $g$, increasing the sides by $a$ and $b$ adds areas $fb$, $ga$, and the corner area $ab$. Discarding the corner gives an approximation whose error is exactly known. The ordinary differential product rule will follow when this corner becomes negligible after division by the step size.

There is also an exact rule for a nonlinear measurement. For a function $F:\mathbb R\to\mathbb R$,

$$
\Delta_T(F\circ f)
=F(f+\Delta_Tf)-F(f).
$$

If $F$ is continuously differentiable on the interval between these two values, the fundamental theorem of calculus rewrites this as

$$
\Delta_T(F\circ f)
=\Delta_Tf\int_0^1 F'(f+\theta\Delta_Tf)\,d\theta.
$$

Thus $F'(f)\Delta_Tf$ is generally only the first approximation. The integral retains the variation of $F'$ over the whole finite change.

## 4. Worked example: an affine update and a quadratic measurement

Take $X=\mathbb R$, $T(x)=2x+1$, and let $q(x)=x$. We have

$$
U_Tq=2x+1,\qquad \Delta_Tq=x+1.
$$

Applying the product law to $q^2$ gives

$$
\begin{aligned}
\Delta_T(q^2)
&=2q\,\Delta_Tq+(\Delta_Tq)^2\\
&=2x(x+1)+(x+1)^2\\
&=3x^2+4x+1.
\end{aligned}
$$

This agrees with direct substitution. At $x=1$, the state changes from $1$ to $3$, so its square increases by $8$. The differential-looking term $2x\,\Delta_Tq$ gives only $4$; the missing $4$ is the squared increment.

Here the operator also has a familiar matrix representation. Every quadratic observable has the form $f=a+bq+cq^2$, and substitution gives

$$
U_Tf=(a+b+c)+(2b+4c)q+4cq^2.
$$

Thus the coefficients of $U_Tf$ are obtained from those of $f$ by

$$
\begin{pmatrix}a\\b\\c\end{pmatrix}
\longmapsto
\begin{pmatrix}1&1&1\\0&2&4\\0&0&4\end{pmatrix}
\begin{pmatrix}a\\b\\c\end{pmatrix}.
$$

The matrix acts on coefficients of measurements, not on the state $x$. This works because the pullback of a quadratic by this affine map is still quadratic. For the nonlinear map $T(x)=x^2$, pulling back $q^2$ gives $q^4$, so the same three-dimensional collection of observables would not be preserved.

Why did we keep the coordinate $q$, even though our desired measurement is $q^2$? Set $f=q^2$. Knowing only the present square does not determine the next square. The two states $x=1$ and $x=-1$ have the same measured value, but

$$
f(1)=f(-1)=1,\qquad f(T(1))=9,\qquad f(T(-1))=1.
$$

Thus no function $F:[0,\infty)\to[0,\infty)$ can satisfy $f(T(x))=F(f(x))$ for every $x$: it would have to assign both $9$ and $1$ to the input $1$. The pullback $U_Tf$ is well-defined because it still takes the full state as input. The matrix computes the coefficients of that observable; evaluating it still requires $x$, including its sign. [Composition and error](composition.md) will ask when a smaller description contains enough information to make its own predictions.

To calculate repeated updates, shift the coordinate by one. If $z=x+1$, then the next shifted coordinate is $2z$. Consequently,

$$
T^N(x)=2^N(x+1)-1.
$$

Starting at zero, three updates produce

$$
0\longmapsto1\longmapsto3\longmapsto7.
$$

The squared observable takes values $0,1,9,49$. Its successive changes are $1,8,40$, whose sum is $49$. Notice that we must evaluate the difference at the successive states. Three copies of the initial difference would give $3$, which describes a different calculation.

## 5. Composition reverses pullback order

Recall our convention for function composition:

$$
(T\circ S)(x)=T(S(x)):
\quad\text{apply }S\text{ first, then }T.
$$

**Proposition 1.6 (composition law).** For transformations $S,T:X\to X$,

$$
U_{T\circ S}=U_SU_T,
\qquad
\Delta_{T\circ S}
=\Delta_S+\Delta_T+\Delta_S\Delta_T.
$$

**Proof.** Operator multiplication also means composition, with the rightmost operator acting first. Therefore

$$
(U_SU_Tf)(x)=(U_Tf)(S(x))=f(T(S(x))).
$$

For the difference identity, substitute $U_S=I+\Delta_S$ and $U_T=I+\Delta_T$, multiply, and subtract $I$. The order of the last product is retained. $\square$

An equivalent expression makes the successive changes visible:

$$
\Delta_{T\circ S}f(x)
=\Delta_Sf(x)+(\Delta_Tf)(S(x)).
$$

The second change must be measured at the state reached after the first. Substituting the original state for that intermediate state loses the term $\Delta_S\Delta_Tf$.

## 6. Worked example: a shear and a translation

Imagine raising a point and sliding it horizontally by an amount determined
by its height. Before calculating, predict which order puts the point
farther to the right: raise it first, or slide it first? We can isolate
the effect by changing the order while keeping both maps fixed.

On $\mathbb R^2$, define

$$
S(x,y)=(x+y,y),\qquad T(x,y)=(x,y+1).
$$

The first map shears horizontally by an amount equal to the vertical coordinate. The second raises the vertical coordinate by one. Their compositions are

$$
(T\circ S)(x,y)=(x+y,y+1),
$$

$$
(S\circ T)(x,y)=(x+y+1,y+1).
$$

Raising the point first increases the subsequent horizontal shear. The two outcomes differ by one horizontal unit.

Choose $f(x,y)=x^2+2y$. Direct calculation gives

$$
\Delta_Sf=2xy+y^2,\qquad \Delta_Tf=2.
$$

Because $\Delta_Tf$ is constant, $\Delta_S\Delta_Tf=0$. In the reverse order,

$$
\Delta_T\Delta_Sf
=2x(y+1)+(y+1)^2-(2xy+y^2)
=2x+2y+1.
$$

The composition law now gives

$$
\Delta_{T\circ S}f=2xy+y^2+2,
$$

$$
\Delta_{S\circ T}f=2xy+y^2+2x+2y+3.
$$

For the starting point $(1,2)$, the initial observable is $5$. Applying $S$ then $T$ gives $(3,3)$, where $f=15$. Applying $T$ then $S$ gives $(4,3)$, where $f=22$. The respective changes, $10$ and $17$, agree with the formulas.

<figure class="map-demo" data-map-demo id="map-order-animation">
<figcaption><strong>See the order change the answer.</strong> Both blue points start at (1, 2). Predict their destinations, then apply each map.</figcaption>
<div class="map-controls">
<button type="button" data-map-play aria-pressed="false" disabled>Play both orders</button>
<button type="button" data-map-step disabled>Next map</button>
<button type="button" data-map-reset disabled>Reset example</button>
<label>Progress<input type="range" min="0" max="2" step="0.001" value="0" disabled></label>
</div>
<p data-map-phase>Starting state</p>
<div class="map-panels">
<section data-map-order="shear-first">
<h3>Shear S, then translation T</h3>
<svg viewBox="0 0 360 276" role="img" aria-label="Coordinate plot for a shear followed by a translation. The point and observable are reported below."></svg>
<output aria-live="off">Point (1, 2); f = 5; change = 0</output>
</section>
<section data-map-order="translation-first">
<h3>Translation T, then shear S</h3>
<svg viewBox="0 0 360 276" role="img" aria-label="Coordinate plot for a translation followed by a shear. The point and observable are reported below."></svg>
<output aria-live="off">Point (1, 2); f = 5; change = 0</output>
</section>
</div>
<p class="map-note">The dashed square marks the starting shape. The blue outline shows the same points after the maps. Read f = x² + 2y at the moving point: the final changes are 10 and 17. The slider interpolates exact partial shears and translations; it is an illustration of maps, not a fluid simulation.</p>
<noscript><p>Animation needs JavaScript. The calculation above gives both endpoints and their observables.</p></noscript>
</figure>
<script type="module" src="../assets/maps.js"></script>

The difference of operator orders is called a *commutator*. With the convention $[A,B]=AB-BA$, this example gives

$$
[U_S,U_T]f=[\Delta_S,\Delta_T]f=-2x-2y-1.
$$

This is a function of the starting point, not merely a yes-or-no statement about whether the transformations commute. [Composition and interaction](composition.md) develops what such differences can measure.

## 7. Accumulated change and invariants

**Definition 1.7 (orbit and accumulated difference).** Put $T^0=\operatorname{id}_X$. The *orbit* starting at $x$ is $x,T(x),T^2(x),\ldots$. For an integer $N\ge0$, define

$$
\mathcal A_T^N f(x)
=\sum_{j=0}^{N-1}\Delta_Tf(T^j(x)),
$$

with the empty sum equal to zero.

**Proposition 1.8 (finite fundamental theorem).**

$$
\boxed{\mathcal A_T^N f(x)=f(T^N(x))-f(x).}
$$

**Proof.** Each summand equals $f(T^{j+1}(x))-f(T^j(x))$. The negative value at every intermediate state cancels the positive value from the preceding term. Only the last and first values remain. For $N=0$, both sides vanish. $\square$

An *invariant observable* satisfies $\Delta_Tf=0$ everywhere. Proposition 1.8 then shows that it remains constant along every orbit. Conversely, constancy along every orbit includes the first update and therefore implies $\Delta_Tf=0$.

We can also estimate accumulation without knowing its sign:

$$
|f(T^N(x))-f(x)|
\le\sum_{j=0}^{N-1}|\Delta_Tf(T^j(x))|.
$$

For instance, a uniform one-step bound $|\Delta_Tf|\le\varepsilon$ gives a bound $N\varepsilon$ after $N$ steps. Cancellation can make the actual change smaller. Establishing such cancellation requires information about the signs along the orbit; it does not follow from the absolute bound alone.

## 8. Exercises

Work through the first two directly from the definitions before using the general laws. The later problems ask you to choose and adapt a law.

**Exercise 1 — A cubic measurement.** For $T_h(x)=x+h$ and $f(x)=x^3$, calculate $U_{T_h}f$ and $\Delta_{T_h}f$ as functions of $x$. Then evaluate the change at $x=1,h=2$. Identify the error made by retaining only $3x^2h$.

<details markdown="1">
<summary>Solution: distinguish the function from its value</summary>

The pullback is $(x+h)^3$. Expanding and subtracting $x^3$ gives
$$
\Delta_{T_h}f=3x^2h+3xh^2+h^3.
$$
At $x=1,h=2$, the change is $27-1=26$. The term $3x^2h$ gives $6$, discarding $3xh^2+h^3=20$.

</details>

**Exercise 2 — An unchanged measurement.** Let $T(x)=-x$ and $f(x)=x^2$. Find $\Delta_Tf$, and describe the orbit of a nonzero state. Does invariance of this observable make $T$ the identity? Find another observable that detects the change. Although the square loses the sign, can its next value under this particular $T$ be predicted from its present value alone?

<details markdown="1">
<summary>Solution</summary>

We have $\Delta_Tf=(-x)^2-x^2=0$, but the orbit alternates between $x$ and $-x$. Thus $T$ is not the identity. The coordinate observable $q(x)=x$ detects the change through $\Delta_Tq=-2x$, which is nonzero away from the origin.

The square's next value is exactly its present value: the rule for the measurement is $F(y)=y$ on $[0,\infty)$. Information loss therefore does not always prevent prediction. It matters whether the chosen update needs the discarded information. Unlike the affine update in Section 4, this reflection does not need the sign to predict the next square.

</details>

**Exercise 3 — Detecting order.** For the shear and translation in the second worked example, calculate $[U_S,U_T]q$ for $q(x,y)=x$, and then for $q(x,y)=y$. Explain why one observable detects the difference of order and the other does not.

<details markdown="1">
<summary>Hint and answer</summary>

First write out $q(T(S(x,y)))$ and $q(S(T(x,y)))$. For the horizontal coordinate these are $x+y$ and $x+y+1$, so the commutator is $-1$. For the vertical coordinate both are $y+1$, so the commutator is zero. A purely vertical observable cannot detect a horizontal difference.

</details>

**Exercise 4 — A quotient law.** Suppose $g(x)\ne0$ and $g(T(x))\ne0$. Prove, at this state, that
$$
\Delta_T\left(\frac fg\right)
=\frac{g\,\Delta_Tf-f\,\Delta_Tg}{g\,U_Tg}.
$$
Explain why replacing the denominator by $g^2$ is generally incorrect.

<details markdown="1">
<summary>Solution: use the old and new denominators</summary>

$$
\frac{U_Tf}{U_Tg}-\frac fg
=\frac{g(f+\Delta_Tf)-f(g+\Delta_Tg)}{g\,U_Tg}.
$$
Cancellation yields the claimed numerator. The denominator involves both the old and new values of $g$; they need not agree.

</details>

**Exercise 5 — A variable sequence.** Let $x_{j+1}=T_j(x_j)$, where each $T_j:X\to X$ may depend on $j$. Prove
$$
f(x_N)-f(x_0)=\sum_{j=0}^{N-1}\Delta_{T_j}f(x_j).
$$
Which part of the proof of Proposition 1.8 survives unchanged?

<details markdown="1">
<summary>Hint</summary>

Write the summand as $f(x_{j+1})-f(x_j)$, then write out the first three terms. Cancellation uses the shared intermediate states; it does not require the maps $T_j$ to be equal.

</details>

<details markdown="1">
<summary>Solution and a check with different updates</summary>

By definition, $\Delta_{T_j}f(x_j)=f(x_{j+1})-f(x_j)$. Therefore

$$
\sum_{j=0}^{N-1}\Delta_{T_j}f(x_j)
=\sum_{j=0}^{N-1}\bigl(f(x_{j+1})-f(x_j)\bigr)
=f(x_N)-f(x_0).
$$

Every intermediate value cancels once positively and once negatively. For $N=0$, the sum is empty and the difference is zero.

For a concrete check, start at $x_0=1$, take $T_0(x)=2x$, $T_1(x)=x-3$, $T_2(x)=x+4$, and measure $f(x)=x^2$. The states are $1,2,-1,3$; the measurements are $1,4,1,9$. The changes $3,-3,8$ sum to $8=9-1$. Evaluating all three differences at the original state instead would give $3+3+24=30$. The identity depends on using the state reached at each step.

</details>

**Exercise 6 — A finite matrix for all the updates.** For $T(x)=2x+1$, use the coefficient matrix in Section 4 twice on $f(x)=x^2$. Check the resulting polynomial by computing $f(T^2(x))$ directly. Then explain why repeated use of this matrix gives the exact observable after any number of updates.

<details markdown="1">
<summary>Solution</summary>

The coefficient vector $(0,0,1)^{\mathsf T}$ first becomes $(1,4,4)^{\mathsf T}$, then $(9,24,16)^{\mathsf T}$. Directly, $T^2(x)=4x+3$, whose square is $16x^2+24x+9$. The quadratic observables stay within the same three-dimensional space after every pullback. Also $U_T^N=U_{T^N}$, so matrix powers calculate exactly the observable at the state reached after $N$ updates.

</details>

## Further reading and notation

The summation rules belong to discrete calculus; the action on observables
belongs to the pullback and Koopman traditions. For a deeper study of sums
and recurrences, see Ronald L. Graham, Donald E. Knuth and Oren Patashnik,
[*Concrete Mathematics*, second edition](https://cs.stanford.edu/~knuth/gkp.html)
(Addison-Wesley, 1994). Try translating a recurrence from that text into a
state update, then use its summation methods to calculate an accumulated
observable change.

For the historical operator viewpoint, B. O. Koopman's 1931 paper
[*Hamiltonian Systems and Transformation in Hilbert Space*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1076052/)
studies dynamics through operators on functions. Our pointwise algebra
requires much less structure than its Hilbert-space setting; analytic
operator theorems need their own function-space hypotheses.

The accompanying [operator implementation](../../transformatics/operators.py) calls $U_T$ `shift`, $\Delta_T$ `resolvant`, and the telescoping sum `accumulation`. We use $\Delta_T$ throughout the lessons to keep the finite difference distinct from the spatial gradient $\nabla$. The implementation's name `resolvant` should also be distinguished from the standard operator resolvent $(zI-A)^{-1}$.

[Contents](index.md) · [Continue: generators and continuous change](generators.md)
