# A bridge from single-variable calculus

You can begin [finite transformations](transformations.md) with algebra and
function composition. This optional chapter supplies the next few tools as
you need them. Each starts with something you can calculate, gives the
notation a name, and points to where it will be used.

The starting knowledge is differentiation and integration of elementary
functions, including the chain rule. You do not need to read the whole bridge
before starting the course. Sections 1–3 help with generators; Sections 4–6
help with errors, scaling and fluids; Section 7 helps with theorem statements.

## 1. A vector is a state with several coordinates

A state can be a pair, such as position and velocity. Write it as
$v=(a,b)$, or as a column when multiplying by a matrix. Its Euclidean length is

$$
|v|=\sqrt{a^2+b^2}.
$$

A matrix records a linear update of the coordinates. For example,

$$
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},
\qquad
A\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}a+2b\\b\end{pmatrix}.
$$

Read one row at a time: multiply its entries by the input coordinates and
add. The vector $(0,1)$ becomes $(2,1)$, so its length changes from 1 to
$\sqrt5$. The matrix has sheared the plane: horizontal lines slide by
amounts depending on their height.

The product $AB$ means apply $B$ first and $A$ second. This is the same order
as function composition. The transpose $A^T$ interchanges rows and columns.
The dot product $v\cdot w=a w_1+b w_2$ is a number; in particular,
$v\cdot v=|v|^2$.

**Try it.** Let $B(a,b)=(a,b+a)$. Starting from $(1,0)$, compare $ABv$
and $BAv$. Which operation acted first in each case?

<details markdown="1">
<summary>Solution: order changes the state</summary>

$Bv=(1,1)$, so $ABv=(3,1)$. But $Av=(1,0)$, so $BAv=(1,1)$.
The two matrix products describe different transformations.

</details>

Return to [map order](transformations.md#6-worked-example-a-shear-and-a-translation)
or [amplification](composition.md#eigenvalues-can-miss-amplification).

## 2. Partial derivatives hold the other coordinates fixed

For $f(x,y)=x^2+3y^2$, there are two independent directions of change.
The partial derivative $\partial_x f$ differentiates in $x$ with $y$ held
fixed. Thus

$$
\partial_x f=2x,\qquad \partial_y f=6y,
\qquad \nabla f=(2x,6y).
$$

The vector $\nabla f$ is the **gradient**. Now let both coordinates move,
following $(x(t),y(t))$. Applying the ordinary chain rule to both inputs gives

$$
\frac{d}{dt}f(x(t),y(t))
=\partial_x f\,x'(t)+\partial_y f\,y'(t).
$$

Both partial derivatives on the right are evaluated at $(x(t),y(t))$.
If the velocity is $v=(x',y')$, the expression is $v\cdot\nabla f$.
This is the generator formula in coordinates.

For $x(t)=t$ and $y(t)=2t$, direct substitution gives $f=13t^2$, hence
derivative $26t$. The partial-derivative formula gives
$(2t)(1)+(12t)(2)=26t$, the same answer by a different route.

If a measurement also changes explicitly with time, write $F(t,x,y)$.
Along a path its derivative has an extra term:

$$
\frac{d}{dt}F(t,x(t),y(t))
=\partial_tF+\partial_xF\,x'+\partial_yF\,y'.
$$

**Try it.** For $F(t,x,y)=t+x^2+3y^2$ on the path above, compare the
derivative along the path with $\partial_t F$ at a fixed location.

<details markdown="1">
<summary>Solution: changing the field and moving through it</summary>

Along the path, $F=t+13t^2$, so the derivative is $1+26t$.
At a fixed $(x,y)$, only the explicit $t$ changes, so $\partial_tF=1$.
Movement through spatial variation accounts for the difference.

</details>

Return to [generators](generators.md#2-differentiating-the-observable-action)
and [the material derivative](generators.md#6-time-dependent-observables-and-the-material-derivative).

## 3. Differentiating a field

A velocity field assigns a vector to each location. In three dimensions write
$u=(u_1,u_2,u_3)$. Its derivative matrix has entries
$(\nabla u)_{ij}=\partial_j u_i$: row $i$ differentiates component $i$.

Three combinations occur often:

$$
\nabla\cdot u=\partial_xu_1+\partial_yu_2+\partial_zu_3,
$$

$$
\Delta f=\partial_x^2f+\partial_y^2f+\partial_z^2f,
$$

$$
\nabla\times u=
(\partial_yu_3-\partial_zu_2,
\partial_zu_1-\partial_xu_3,
\partial_xu_2-\partial_yu_1).
$$

These are **divergence**, **Laplacian**, and **curl**, respectively.
Divergence measures the instantaneous local rate of volume expansion of the
particle flow. Curl describes its local rotation. The Laplacian sums second
derivatives; applied to a vector, it acts on each component separately.

For the shear $u=(y,0,0)$, only one first derivative is nonzero:
$\partial_yu_1=1$. Consequently,

$$
\nabla\cdot u=0,\qquad \nabla\times u=(0,0,-1),
\qquad \Delta u=0.
$$

Zero divergence allows shear and rotation. It does not mean the velocity is
constant. This linear shear is a field on $\mathbb R^3$; it is not periodic
in $y$. The periodic fluid example instead uses $\sin(Ny)$.

**Try it.** For $u=(\sin y,0,0)$, compute divergence, curl and Laplacian.
Check $(u\cdot\nabla)u$ too: expand the directional derivative before applying it.

<details markdown="1">
<summary>Solution: a periodic shear</summary>

The divergence is zero, the curl is $(0,0,-\cos y)$, and
$\Delta u=(-\sin y,0,0)=-u$. Although the field varies with $y$, its
directional derivative along itself is $\sin y\,\partial_xu=0$.
The direction of motion matters as well as the direction of variation.

</details>

Return to [the fluid equation](equation.md).

## 4. Norms say which error matters

A **norm** assigns a size to a vector or function. It is nonnegative, is zero
only on the zero vector, satisfies $\|a v\|=|a|\|v\|$, and satisfies the
triangle inequality $\|v+w\|\le\|v\|+\|w\|$.

For a continuous function on $[0,2\pi]$, two useful sizes are

$$
\|f\|_\infty=\max_{x\in[0,2\pi]}|f(x)|,
\qquad
\|f\|_{2,\mathrm{av}}
=\left(\frac1{2\pi}\int_0^{2\pi}|f(x)|^2\,dx\right)^{1/2}.
$$

The first records the largest magnitude. The second is the root mean square.
Without the subscript “av,” this book uses the integral without division by
the interval's length. That convention changes a numerical constant.

For $f(x)=a\sin(Nx)$ with positive integer $N$,

$$
\|f\|_\infty=|a|,\qquad
\|f\|_{2,\mathrm{av}}=\frac{|a|}{\sqrt2},
\qquad \|f'\|_\infty=N|a|.
$$

The middle identity follows by integrating
$\sin^2(Nx)=(1-\cos(2Nx))/2$. Two waves can have the same amplitude and
root mean square but very different derivative sizes.

An error bound must therefore name its norm. If an output map satisfies
$|g(a)-g(b)|\le L|a-b|$ on a specified interval, it is **Lipschitz** there
with constant $L$. The mean value theorem supplies such a bound when
$|g'|\le L$ on that interval. For $g(x)=x^2$ on $[-M,M]$, take $L=2M$.
The same constant does not work on arbitrarily large intervals.

**Try it.** Let $f_n(x)=n^{-1}\sin(n^2x)$ for integers $n\ge1$.
Does the function become small in maximum size? Does its derivative?

<details markdown="1">
<summary>Solution: a small function can have a large derivative</summary>

$\|f_n\|_\infty=1/n\to0$, whereas
$f_n'(x)=n\cos(n^2x)$ and $\|f_n'\|_\infty=n\to\infty$.
Control of function values alone cannot justify a conclusion about their
derivatives. This family is a calculation about norms, with no assertion
that it evolves by a fluid equation.

</details>

Return to [error conversion](transfer-systems.md#4-approximate-transfer-and-observable-error)
or [scaling](scaling.md).

## 5. Integration by parts becomes an energy calculation

Suppose $v(t,x)$ is smooth, periodic with period $2\pi$ in $x$, and solves
the one-dimensional heat equation $v_t=\nu v_{xx}$ with $\nu>0$.
Define $E(t)=\tfrac12\int_0^{2\pi}v(t,x)^2\,dx$.
Differentiate under the integral, then integrate by parts:

$$
\begin{aligned}
E'(t)&=\int_0^{2\pi}v v_t\,dx
=\nu\int_0^{2\pi}v v_{xx}\,dx\\
&=\nu[vv_x]_0^{2\pi}-\nu\int_0^{2\pi}v_x^2\,dx
=-\nu\int_0^{2\pi}v_x^2\,dx\le0.
\end{aligned}
$$

The boundary term is zero because both $v$ and $v_x$ agree at the two
endpoints. The assumptions of smoothness justify these operations here.
For less regular solutions, justifying them is part of the analysis.

**Try it.** Verify the heat equation and the energy identity for
$v(t,x)=e^{-\nu t}\sin x$.

<details markdown="1">
<summary>Solution: check the equation and its consequence separately</summary>

$v_t=-\nu e^{-\nu t}\sin x=\nu v_{xx}$. Also
$E(t)=\tfrac\pi2e^{-2\nu t}$, so $E'=-\nu\pi e^{-2\nu t}$.
Since $v_x=e^{-\nu t}\cos x$, the dissipation integral has exactly
that value with a minus sign. We checked the equation first; the energy
identity alone would not determine it.

</details>

In a periodic box, integration means integrating in each coordinate.
The same integration-by-parts argument in each direction produces the
viscous term in [the fluid energy law](equation.md#measure-energy-and-deformation).

## 6. Fourier modes are waves with calculable derivatives

The functions $\sin(Nx)$ and $\cos(Nx)$ repeat over $[0,2\pi]$ when
$N$ is an integer. Differentiating twice multiplies either one by $-N^2$.
Consequently a heat solution $v(t,x)=a(t)\sin(Nx)$ satisfies

$$
a'=-\nu N^2a,\qquad a(t)=a(0)e^{-\nu N^2t}.
$$

An oscillating wave is called a **mode**. Products can create different modes:

$$
\cos(ax)\cos(bx)
=\tfrac12\cos((a+b)x)+\tfrac12\cos((a-b)x).
$$

For integer frequencies $a,b$, this identity already explains why multiplying
two periodic fields can produce a frequency absent from either input.

The compact complex notation uses $i^2=-1$ and
$e^{i\theta}=\cos\theta+i\sin\theta$. In three dimensions,
$e^{ik\cdot x}$ uses the integer vector $k=(k_1,k_2,k_3)$, and

$$
\partial_j e^{ik\cdot x}=ik_j e^{ik\cdot x},
\qquad \Delta e^{ik\cdot x}=-|k|^2e^{ik\cdot x}.
$$

For a finite sum, these rules follow term by term. Infinite Fourier series
need convergence and regularity hypotheses before differentiation or
rearrangement; those are additional analysis, not properties supplied by
the notation. Paired opposite frequencies describe real fields:
$\widehat u(-k)=\overline{\widehat u(k)}$, where the bar means complex
conjugation. The real sine and cosine calculations remain available.

**Try it.** Which frequencies occur in $\cos(2x)\cos(3x)$?
If the product is used as initial data for the heat equation, do the two
resulting modes decay at the same rate?

<details markdown="1">
<summary>Solution: one product, two time scales</summary>

The product is $(\cos(5x)+\cos x)/2$. Its heat evolution is
$e^{-25\nu t}\cos(5x)/2+e^{-\nu t}\cos x/2$.
The decay rates differ by a factor of 25. One scalar attenuation factor
cannot describe this whole profile for $t>0$.

</details>

Return to [resolution](scaling.md#resolution-is-another-representation-map),
then [frequency creation](activation.md).

## 7. Read an estimate one quantifier at a time

The statement $|e(h)|\le Ch^2$ for $0<h\le h_0$ means there are fixed
positive constants $C,h_0$ that work for every such $h$. The constant may
depend on named data, but not on $h$. Writing $e(h)=O(h^2)$ abbreviates
such a bound. Writing $e(h)=o(h^2)$ makes the stronger assertion
$e(h)/h^2\to0$ as $h\to0$.

For example, $3h^2$ is $O(h^2)$ but not $o(h^2)$, while $h^3$ is both.
The notation $A\asymp B$ means $cB\le A\le CB$ for fixed positive
constants on the stated parameter range, with $A,B$ nonnegative.

A bound can hold separately at every fixed time and still fail uniformly
up to an endpoint. The elementary function $1/(1-t)$ is finite at each
$t<1$, but no finite constant bounds it for all $0\le t<1$.
When reading “bounded,” ask which variables are allowed to vary.

Later sources use $C^m$ for continuous derivatives through order $m$ and
$C^\infty$ for derivatives of every finite order. A multi-index records
several spatial differentiations: for example, $\alpha=(1,2,0)$ means
$\partial^\alpha=\partial_x\partial_y^2$. For an integer $s\ge0$,
an $H^s$ Sobolev norm measures the square-integral sizes of a function and
its derivatives through order $s$. This description decodes the notation;
embedding, product and continuation theorems require further hypotheses.

**Try it.** For every positive integer $N$, the choice $x=N$ satisfies
$x\ge N$. Does that supply a single real $x$ satisfying $x\ge N$ for
every positive integer $N$?

<details markdown="1">
<summary>Solution: the order of the choices matters</summary>

No. The first statement allows $x$ to change with $N$. Given any single
real $x$, there is an integer greater than it. An argument about a family
of separately chosen objects needs an additional step before it establishes
a property of one object. [Iteration](iteration.md#1-three-different-quantifiers)
uses this distinction in a less elementary setting.

</details>

You now have a reference for the notation used in the core course.
Continue with [generators](generators.md), or use the
[reading map](reader-map.md) to choose a different calculation.
