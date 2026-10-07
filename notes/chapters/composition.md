# Composition and the cost of error

An approximate model introduces an error at each step. Later steps may
dampen that error, preserve it, or amplify it. To understand the final
prediction, we must follow both the model state and the errors introduced
along the way.

Begin with two quantities that decay at different rates. In one step, the
first halves and the second falls to a quarter:

$$
T(x_1,x_2)=(x_1/2,x_2/4).
$$

You record only their total, $R(x_1,x_2)=x_1+x_2$, and model that total by halving it: $S(y)=y/2$. Starting from $(2,2)$, evolving the two quantities and then adding gives $1+1/2=3/2$. Adding first and then evolving the model gives $S(4)=2$. The discrepancy is $-1/2$.

The discrepancy is the **transfer defect** from the [previous
chapter](transfer-systems.md). Here it comes from discarded information:
$(4,0)$ and $(0,4)$ have the same total, but their totals after one
step are $2$ and $1$. No exact update of the total alone can handle
both. Even so, a model may remain useful on a stated set of inputs if we
can bound its defect and the subsequent propagation of that defect.

We will derive that bound first, then test it on rotation and heat flow.
Rotation will separate finite-time accuracy from long-time behavior; heat
flow will separate error in retained variables from the information missing
when we reconstruct a field.

## Two descriptions of one step

Let $X$ be a state space, let $Y$ be a normed vector space, and consider maps

$$
T:X\to X,\qquad S:Y\to Y,\qquad R:X\to Y.
$$

Here $T$ evolves the original state, $R$ represents it in another description, and $S$ evolves that description. Define the **transfer defect** by

$$
D_R(x)=R(Tx)-S(Rx).
$$

The subtraction takes place in $Y$; we have not assumed that states in $X$ can be subtracted. The defect depends on all three maps, although the notation emphasizes the representation $R$.

If $D_R=0$, the two routes agree: $R\circ T=S\circ R$. When $R$ is onto $Y$, this is an algebraic **semiconjugacy**. If $R$ is also invertible, the systems are algebraically conjugate. Topological versions additionally require appropriate continuity, with a homeomorphism for conjugacy. These are classical concepts; the defect measures failure of the exact relation.

**Proposition 3.1 — Exact transfer through repeated steps.** If $R\circ T=S\circ R$, then for every integer $n\geq0$,

$$
R\circ T^n=S^n\circ R.
$$

**Proof.** At $n=0$ both sides are $R$. If the identity holds at $n$, then

$$
R\circ T^{n+1}=(R\circ T)\circ T^n
=S\circ R\circ T^n=S^{n+1}\circ R.
$$

Induction completes the proof. An exact one-step relation supplies every finite iterate without additional error estimates.

## An approximate relation needs stability

Let $x_j=T^j x_0$ be the original trajectory, and let $y_{j+1}=S(y_j)$ be the model trajectory. Set

$$
e_j=\|R(x_j)-y_j\|,\qquad \delta_j=\|D_R(x_j)\|.
$$

Here $e_j$ is the discrepancy after $j$ steps; $\delta_j$ is the fresh one-step defect evaluated at the original state $x_j$. They are different quantities.

Suppose $S$ is $L$-Lipschitz on a set containing every pair
$R(x_j),y_j$ under consideration. The two model updates can then differ
by at most $L e_j$. To isolate that difference from the fresh transfer
defect, insert the intermediate state $S(R(x_j))$:

$$
\begin{aligned}
R(x_{j+1})-y_{j+1}
&=R(Tx_j)-S(y_j)\\
&=D_R(x_j)+\bigl[S(R(x_j))-S(y_j)\bigr].
\end{aligned}
$$

The triangle inequality and the Lipschitz bound therefore give

$$
e_{j+1}\leq \delta_j+L e_j.
$$

The first term is newly introduced error; the second is propagated old
error. The initial discrepancy $e_0$ has the same status as any other
inherited error. Even a zero defect at every later step will not remove it
unless the evolution supplies a suitable contraction.

**Proposition 3.2 — Finite-step error bound.** For every step at which the hypotheses hold,

$$
e_n\leq L^n e_0+\sum_{j=0}^{n-1}L^{n-1-j}\delta_j.
$$

**Proof.** The first two substitutions are

$$
e_1\leq Le_0+\delta_0,\qquad
e_2\leq L(Le_0+\delta_0)+\delta_1
=L^2e_0+L\delta_0+\delta_1.
$$

At step $n$, the defect introduced at step $j$ has passed through $n-1-j$ later steps. This gives its factor $L^{n-1-j}$. Substitution once more proves the formula at $n+1$, completing the induction.

If $e_0=0$ and each defect is at most $\delta$, the bound is $n\delta$ when $L=1$, at most $\delta/(1-L)$ when $0\leq L<1$, and $\delta(L^n-1)/(L-1)$ when $L>1$. The same local accuracy can have very different long-time consequences. A small defect has meaning only together with a stability estimate and a time interval.

## Worked example: approximating a rotation

The velocity of a rotating point is tangent to its circle. An explicit
Euler step moves along that tangent for a short distance; an exact step
stays on the circle. We can calculate both the local discrepancy and the
effect of repeating it.

Take $X=Y=\mathbb R^2$, $R=I$, and

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T_\tau=e^{\tau J},\qquad S_\tau=I+\tau J.
$$

The exact step rotates a vector by angle $\tau$. The approximate step is the explicit Euler method for $x'=Jx$. Since $J^2=-I$,

$$
T_\tau=(\cos\tau)I+(\sin\tau)J.
$$

For any real $a,b$, $(aI+bJ)^T(aI+bJ)=(a^2+b^2)I$. Thus

$$
\|D_I(x)\|=
\sqrt{(\cos\tau-1)^2+(\sin\tau-\tau)^2}\,\|x\|
=\left(\frac{\tau^2}{2}+O(\tau^4)\right)\|x\|.
$$

The exact orbit has constant radius $r=\|x_0\|$, so the defect has the same size at each exact state. A useful bound without an unspecified remainder follows from Taylor's integral formula:

$$
T_\tau-I-\tau J=-\int_0^\tau(\tau-s)e^{sJ}\,ds,
\qquad \delta_j\leq r\tau^2/2\quad(\tau>0).
$$

Each $e^{sJ}$ preserves length. The model has Lipschitz constant $L=\sqrt{1+\tau^2}$, since $S_\tau^TS_\tau=(1+\tau^2)I$. Start both trajectories at $x_0$, so $e_0=0$. For $t=n\tau$, Proposition 3.2 gives

$$
\begin{aligned}
e_n&\leq\sum_{j=0}^{n-1}L^{n-1-j}\frac{r\tau^2}{2}
\leq nL^{n-1}\frac{r\tau^2}{2}\\
&\leq\frac{rt\tau}{2}e^{t\tau/2},
\end{aligned}
$$

where $L^n=(1+\tau^2)^{n/2}\leq e^{n\tau^2/2}$. Holding $t$ fixed and taking $\tau\to0$ therefore gives error of order $\tau$. For $r=1$, $t=1$, and $\tau=0.1$, the bound is about $0.0526$.

The model's radius is exactly

$$
\|S_\tau^n x_0\|=(1+\tau^2)^{n/2}r.
$$

For $r>0$ and fixed $\tau>0$, it grows without bound as
$n\to\infty$. There is no contradiction with the preceding convergence
estimate: there we fixed $t=n\tau$ and decreased the step. Here we fix
the step and let the observation time grow. The formula for the radius
shows exactly why the two limits have different consequences.

## Worked example: an exact coarse heat evolution

Consider smooth periodic functions on $0\leq x<2\pi$. A Fourier series represents such a function as a sum of waves:

$$
v(x)=\sum_{k\in\mathbb Z}\widehat v(k)e^{ikx},\qquad
\widehat v(k)=\frac1{2\pi}\int_0^{2\pi}v(x)e^{-ikx}\,dx,
\qquad i^2=-1.
$$

The integer $k$ labels a frequency; $\widehat v(k)$ is its coefficient. Real functions have $\widehat v(-k)=\overline{\widehat v(k)}$, so the imaginary parts cancel in the sum. Taking two spatial derivatives multiplies the $k$th wave by $-k^2$. Consequently the heat equation $v_t=\nu v_{xx}$, with $\nu>0$, gives the separate ODE $\partial_t\widehat v(k)=-\nu k^2\widehat v(k)$ for each coefficient. Its time-$\tau$ map is

$$
\widehat{T_\tau v}(k)=e^{-\nu k^2\tau}\widehat v(k).
$$

Let $R=P_K$ discard frequencies with $|k|>K$, and let $S_\tau$ multiply the retained coefficients by the same heat factors. Each frequency evolves independently, so

$$
P_K T_\tau=S_\tau P_K.
$$

The transfer defect is zero: the low frequencies are predicted exactly. Nevertheless, discarding the tail can change the original field. For $v_0=\sin x+\tfrac12\sin(8x)$ and $K=2$, the represented evolution is $e^{-\nu t}\sin x$. The exact field is

$$
v(t,x)=e^{-\nu t}\sin x+\tfrac12e^{-64\nu t}\sin(8x).
$$

Reconstruct the model as a field by setting all omitted coefficients to zero. Its error is the remaining term $\tfrac12e^{-64\nu t}\sin(8x)$. In the normalized norm

$$
\|f\|_2^2=\frac1{2\pi}\int_0^{2\pi}|f(x)|^2dx,
\qquad \|\sin(8x)\|_2^2=\frac12,
$$

the reconstruction error is $e^{-64\nu t}/(2\sqrt2)$. Thus the retained
variables evolve exactly while the reconstructed field remains incomplete.
In this example the missing wave is known, so its cost can be calculated
separately from the temporal error of any numerical method.

This distinction becomes harder for nonlinear fluids: two discarded or retained frequencies can interact to generate another frequency. Fourier projection no longer automatically commutes with evolution. The [fluid laboratory](simulator.md) therefore needs a specified spatial approximation and numerical checks.

## When changing a profile does not commute with heat

The exact heat example worked because projection kept or discarded each frequency independently. Multiplying a field by a spatial profile has a different effect. Let $M_av=a(x)v(x)$, take $a(x)=\cos x$, and keep the same heat map $T_\tau$. With initial field $v=1$, the two orders give

$$
M_aT_\tau1=\cos x,
\qquad T_\tau M_a1=e^{-\nu\tau}\cos x.
$$

Heat leaves a constant unchanged, but damps the frequency introduced by multiplication. For the representation $R=M_a$ and the model step $S=T_\tau$, the transfer defect is therefore

$$
D_{M_a}(1)=(1-e^{-\nu\tau})\cos x.
$$

Check its sign at a small positive time: near $x=0$, multiplying *after* heat gives the larger value. This is a check on the order in the definition, not just the arithmetic.

The ordinary product rule identifies the infinitesimal source of the discrepancy. For smooth periodic $a,v$,

$$
(av)''-av''=a''v+2a'v',
\qquad
\left.\frac{d}{d\tau}D_{M_a}(v)\right|_{\tau=0}
=-\nu(a''v+2a'v').
$$

A constant profile makes this defect zero. A spatially varying one generally does not. Thus an operation that is exact on its own cannot automatically be moved past an evolution; its order must be checked. Exercise 6 follows the two orders through an explicit nonconstant field.

## Changing descriptions from stage to stage

Sometimes the representation itself changes: a moving frame, a new spatial scale, or a refined mesh. Let $T_j:X_j\to X_{j+1}$, $R_j:X_j\to Y_j$, and $S_j:Y_j\to Y_{j+1}$, with each $Y_j$ normed. The relevant defect is

$$
D_j(x)=R_{j+1}(T_jx)-S_j(R_jx).
$$

Now set $x_{j+1}=T_jx_j$, $y_{j+1}=S_jy_j$, $e_j=\|R_j(x_j)-y_j\|_{Y_j}$, and $\delta_j=\|D_j(x_j)\|_{Y_{j+1}}$. If $S_j$ has Lipschitz constant $L_j$ on the relevant states, the same proof gives

$$
e_n\leq \left(\prod_{m=0}^{n-1}L_m\right)e_0
+\sum_{j=0}^{n-1}\left(\prod_{m=j+1}^{n-1}L_m\right)\delta_j,
$$

where an empty product is one. For two stages starting with $e_0=0$, this reads $e_2\leq L_1\delta_0+\delta_1$. With equal defect bounds $\delta$, a gain of $4$ followed by a contraction of $1/4$ gives $e_2\leq5\delta/4$. Reversing those gains gives $e_2\leq5\delta$. Their product is one in both cases, but the error introduced between the stages has a different future. The order matters.

Both the norms and the representation maps matter. A small number measured in a new coordinate system may correspond to a large physical error; the next chapter computes the conversion factors.

For a nonlinear map, a derivative bound supplies a Lipschitz constant only on a suitable region connecting the points being compared. If the proof assumes the trajectories stay in that region, it must also prove they do. Otherwise the estimate is conditional on an unverified containment assumption.

## Eigenvalues can miss amplification

The shear provides another useful test. Its vertical coordinate stays
fixed, while its horizontal displacement accumulates. Predict the length
of the vector starting at $(0,1)$ after several identical shears, then
compare that prediction with the matrix's eigenvalues.

Consider the shear matrix

$$
A=\begin{pmatrix}1&a\\0&1\end{pmatrix}.
$$

Both eigenvalues equal one, but $A^n=\begin{pmatrix}1&na\\0&1\end{pmatrix}$. A unit vector initially in the second coordinate direction reaches length $\sqrt{1+n^2a^2}$. This is polynomial amplification without an expanding eigenvalue.

The largest singular value of $A^n$, and hence its Euclidean operator norm, is

$$
\|A^n\|_2=\frac{\sqrt{n^2a^2+4}+|na|}{2}.
$$

To check the formula, put $b=na$. The matrix

$$
(A^n)^TA^n=\begin{pmatrix}1&b\\b&1+b^2\end{pmatrix}
$$

has characteristic equation $\lambda^2-(2+b^2)\lambda+1=0$. Its larger eigenvalue is $(2+b^2+|b|\sqrt{b^2+4})/2$; taking the square root gives the displayed norm. Replacing this exact quantity with $\|A\|^n$ gives a generally much larger exponential bound. Submultiplicativity is valid, but its repeated use can lose the structure of the evolution.

A gain is a ratio, not an absolute output size. For an input $\eta(0,1)$, the output length is $|\eta|\sqrt{1+n^2a^2}$; a large gain can still leave a very small output. Nor does gain certify the accuracy of a model. If a model predicts a vector $y$, while the actual vector $z$ satisfies $\|z-y\|\leq e$, then

$$
\|y\|-e\leq\|z\|\leq\|y\|+e.
$$

To prove that the actual output exceeds a target $M$, it suffices to show $\|y\|-e>M$. Amplification, initial size, and model error must all enter that comparison. In fluid problems, obtaining the error bound requires controlling pressure and transport as well as the leading shear.

## Exercises

1. Let $T(x)=2x$, $R(x)=x^2$, and $S(y)=4y$. Compute $D_R$. Is $R$ a conjugacy on all of $\mathbb R$? What changes on $x>0$?
2. Suppose $e_0=0$, $L=1/2$, and $\delta_j=2^{-j}\delta$. Find the exact upper bound supplied by Proposition 3.2. Does it tend to zero?
3. Replace explicit Euler for rotation by $C_\tau=(I-\tau J/2)^{-1}(I+\tau J/2)$. Prove $C_\tau^TC_\tau=I$. Find its rotation angle and the leading one-step angle error.
4. In the heat example, replace the exact multiplier with $1-\nu k^2\tau$. Find a condition on $\tau$ making this model nonexpanding on all $|k|\leq K$. Compute the resulting transfer defect coefficient by coefficient.
5. **Diagnose the claim.** Take $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ and input $10^{-3}(0,1)$. A reader says: “Both eigenvalues are one, so there is no amplification. And any amplification would prove the actual output exceeds $0.01$.” Compute the model output length after ten steps. If the error between the model and actual output after ten steps is at most $0.003$, can you certify that target? What if the error bound is $0.03$?
6. **Check the order.** In the heat-and-multiplication example, use $v(x)=\sin2x$. Calculate $D_{M_a}(v)=M_aT_\tau v-T_\tau M_av$, using $\cos x\sin2x=(\sin3x+\sin x)/2$. Differentiate your answer at $\tau=0$ and check it against the product-rule formula. Why does the equality at $\tau=0$ not imply equality later?
7. **Prove the region you use.** Let $x_{j+1}=x_j^2+\delta$, $y_{j+1}=y_j^2$, and $x_0=y_0=0$. For $0\le\delta\le1/8$, prove both sequences stay in $[0,1/4]$. Justify a Lipschitz constant $L=1/2$ for squaring on that interval, and obtain an all-step error bound. Then change $\delta$ to $1/2$. Compute the first three $x_j$ and identify where using the same bound becomes unjustified.

<details markdown="1">
<summary>Hints</summary>

For 2, write out the summand before summing. For 3, use $J^2=-I$. For 4, test the absolute value of each multiplier, including the highest retained frequency. For 5, compare an absolute output with an absolute error. For 6, multiplication creates two frequencies; apply heat to each separately. For 7, first show that one step maps the proposed interval into itself, then use induction. A derivative bound only helps where its inputs lie.

</details>

<details markdown="1">
<summary>Solutions</summary>

**1.** Both routes give $4x^2$, so the defect is zero. On all of $\mathbb R$, $R$ identifies $x$ and $-x$, and is not invertible. Restricted to $x>0$, it is a bijection onto $y>0$, with inverse $\sqrt y$, and gives a conjugacy.

**2.** Each summand is $2^{-(n-1-j)}2^{-j}\delta=2^{-(n-1)}\delta$. There are $n$ summands, giving $e_n\leq n2^{-(n-1)}\delta\to0$.

**3.** Put $z=\tau/2$. Since $(I-zJ)^{-1}=(I+zJ)/(1+z^2)$,

$$
C_\tau=\frac{1-z^2}{1+z^2}I+\frac{2z}{1+z^2}J.
$$

The squared coefficients sum to one. The angle is $2\arctan(\tau/2)=\tau-\tau^3/12+O(\tau^5)$. Radius is preserved exactly, while phase still has a numerical error.

**4.** Let $a_k=\nu k^2\tau$. In the normalized $L^2$ norm, the model is nonexpanding precisely when every retained multiplier satisfies $|1-a_k|\leq1$. For $\tau\geq0$ and an integer cutoff $K\geq1$, this is $\nu K^2\tau\leq2$. The defect on a retained coefficient is

$$
\widehat{D_{P_K}(v)}(k)
=\bigl[e^{-a_k}-(1-a_k)\bigr]\widehat v(k),\qquad |k|\leq K.
$$

Its leading coefficient is $a_k^2/2$ as $a_k\to0$. A stable step can still be inaccurate near the highest frequency; stability alone is not an error tolerance.

**5.** The model output is $10^{-3}(20,1)$, of length $10^{-3}\sqrt{401}\approx0.020025$: the gain is about $20.025$, despite the eigenvalues. With error $0.003$, the actual length is at least $0.017025>0.01$, so the target is certified. With error $0.03$, the bound supplies no positive lower bound. That does not prove the target is missed; it means this estimate cannot decide.

**6.** Heating first multiplies $\sin2x$ by $e^{-4\nu\tau}$. Multiplying first instead produces frequencies one and three, whose heat factors differ. Hence

$$
D_{M_a}(v)=\frac12\left[
(e^{-4\nu\tau}-e^{-9\nu\tau})\sin3x
+(e^{-4\nu\tau}-e^{-\nu\tau})\sin x\right].
$$

Its time derivative at zero is $\nu(5\sin3x-3\sin x)/2$. The product-rule expression is $\nu\cos x\sin2x+4\nu\sin x\cos2x$; the same trigonometric identities give exactly that answer. The two routes agree at zero because the zero-time heat map is the identity. Their unequal derivatives show why that agreement does not persist.

**7.** If $0\le x_j\le1/4$, then
$0\le x_{j+1}\le1/16+1/8=3/16\le1/4$. Since $x_0=0$, induction proves containment. Also $y_j=0$ at every step. On this interval,
$|x^2-y^2|=|x+y||x-y|\le\tfrac12|x-y|$, so the fresh defect $\delta$ gives

$$
|x_n-y_n|\le\delta\sum_{j=0}^{n-1}2^{-j}
=2\delta(1-2^{-n})\le2\delta.
$$

The interval proof came first; the stability estimate can now be applied for every step. With $\delta=1/2$, however,
$x_1=1/2$, $x_2=3/4$, and $x_3=17/16$. The first step already leaves the interval. Reusing its Lipschitz constant would predict the false bound $x_3\le7/8$. The failure is in applying a regional estimate outside its proved region.

</details>

## Further reading

The distinction between local defects, stability and convergence is central
to numerical analysis. Randall J. LeVeque develops it for differential
equations in [*Finite Difference Methods for Ordinary and Partial
Differential Equations*](https://faculty.washington.edu/rjl/fdmbook/)
(SIAM, 2007). The author's University of Washington page includes the
contents, exercises and accompanying programs. Compare a method's local
error estimate with the separate argument controlling its repeated steps.

Gerald Teschl's [*Ordinary Differential Equations and Dynamical
Systems*](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/) provides the
continuous and discrete dynamical-systems setting for questions about
stability and long-time behavior. The contraction and shear calculations
here are elementary examples within that broader theory.

[Continue: scale, norms, and resolution](scaling.md) ·
[Try cumulative Assessment A](practice.md#assessment-a)
