# The equation and its observables

Imagine fluid arranged in parallel layers. Each layer slides horizontally, with neighboring layers moving at different speeds. Viscosity should gradually reduce those differences. If we fit twice as many alternating layers into the same space, should the motion decay twice as fast, four times as fast, or at the same rate? We will answer this by finding an exact solution.

The [flow chapter](generators.md) described a particle path by an ODE. Here there is a path for every starting particle, and the velocity field driving all those paths must itself evolve. The Navier–Stokes equation relates that evolving field to acceleration, pressure and viscosity. The sliding-layer example will let us check each term before using the equation to measure energy and deformation.

For a first reading, work through the sliding-layer solution and its energy
calculation. The [calculus bridge](calculus-bridge.md#3-differentiating-a-field)
introduces the vector derivatives used below and derives the corresponding
one-dimensional heat energy identity. The pressure projection is a further
step; return to it after the scalar calculation is comfortable.

We work on the fixed periodic box $\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3$: functions repeat every $2\pi$ in each coordinate. One can calculate on the cube $[0,2\pi]^3$, with opposite faces identified. The velocity $u(t,x)\in\mathbb R^3$ gives direction and speed at position $x$ and time $t$. With density normalized to one, the equation is

$$
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f,
\qquad \nabla\cdot u=0.
$$

Here $p(t,x)$ is pressure per unit density, $\nu>0$ is a fixed kinematic viscosity, and $f(t,x)$ is an applied force per unit mass. The **unforced** equation sets $f=0$.

## Read the equation along a moving particle

**Preparation:** the [multivariable chain rule](calculus-bridge.md#2-partial-derivatives-hold-the-other-coordinates-fixed) and [field derivatives](calculus-bridge.md#3-differentiating-a-field).

Let $X'(t)=u(t,X(t))$. Applying the chain rule to the velocity measured by that particle gives

$$
\frac{d}{dt}u(t,X(t))
=\partial_tu(t,X(t))+(u\cdot\nabla)u(t,X(t)).
$$

Thus the two terms on the left together are acceleration. A particle can accelerate by entering a region of different velocity even when the field has no explicit time dependence; this is the contribution of **advection**, $(u\cdot\nabla)u$. On the right, pressure gradients accelerate fluid from higher toward lower pressure. The Laplacian $\Delta u$, the sum of the second spatial derivatives of each component, makes viscosity sensitive to how rapidly the velocity varies in space.

The second equation is a constraint. Explicitly,

$$
\nabla\cdot u=\partial_xu_1+\partial_yu_2+\partial_zu_3=0.
$$

It says that a small material volume has no instantaneous expansion or contraction. Its shape can still change: stretching in one direction can balance compression in another. We start from real, smooth, divergence-free initial data. In the unforced chapters we also choose zero spatial mean, which the evolution preserves.

## Worked flow: shear reduces the PDE to one ODE

**First reading:** ordinary derivatives and the exponential solution of $a'=-ca$. The field derivatives are calculated below.

Choose a positive integer $N$, write $e_1=(1,0,0)$, and try

$$
u(t,x,y,z)=a(t)\sin(Ny)e_1,\qquad p=0.
$$

This is the sliding-layer picture: the integer $N$ counts the oscillations across one $2\pi$ period. Before differentiating, notice the direction of motion. A particle moves along a layer, where the velocity has no spatial variation, rather than across the layers where it varies. We therefore expect the advective acceleration to vanish. Indeed, the field has zero mean and zero divergence, and

$$
(u\cdot\nabla)u=a(t)\sin(Ny)\,\partial_xu=0,
\qquad \Delta u=-N^2u.
$$

The unforced equation therefore becomes $a'=-\nu N^2a$. Its exact solution is

$$
a(t)=a(0)e^{-\nu N^2t}.
$$

Viscosity damps a mode with twice the frequency four times as fast. This is the same Fourier attenuation seen in [scale and resolution](scaling.md). The particles themselves keep their initial $y$ and $z$, and

$$
X_1(t)=X_1(0)+\frac{a(0)}{\nu N^2}
\bigl(1-e^{-\nu N^2t}\bigr)\sin\bigl(NX_2(0)\bigr).
$$

We have answered the opening question: doubling $N$ multiplies the decay rate by four. We also know why this example closes into a single ODE. Advection vanishes exactly, leaving one Fourier mode whose amplitude decays. To study transfer between modes, we will need velocities for which that cancellation fails.

## How pressure preserves the constraint

**Further step:** divergence, matrix multiplication and [Fourier modes](calculus-bridge.md#6-fourier-modes-are-waves-with-calculable-derivatives). You can go directly to the energy calculation on a first reading.

Setting $p=0$ worked for the shear. How can we tell whether it will work for another field? The divergence constraint supplies the test. Take the divergence of the equation and use $\nabla\cdot u=0$:

$$
\Delta p=\nabla\cdot f-
\sum_{i,j=1}^3(\partial_i u_j)(\partial_j u_i).
$$

This is a Poisson equation on the whole periodic box. Even when $f=0$, its right side usually does not vanish. Pressure supplies the gradient acceleration needed to keep the evolving velocity divergence-free. Its spatial mean can be fixed to zero because only $\nabla p$ enters the equation. The velocity and pressure must both be periodic here.

There is an equivalent Fourier description. Let $\mathbb P$ be the orthogonal projection onto divergence-free fields. At each nonzero wavevector $k\in\mathbb Z^3$,

$$
\mathbb P_kv=v-k\frac{k\cdot v}{|k|^2},
\qquad \mathbb P_k=I-\frac{k\otimes k}{|k|^2}.
$$

Here $I$ is the identity matrix and $k\otimes k$ is the matrix with entry $k_i k_j$ in row $i$, column $j$. Thus $(k\otimes k)v=k(k\cdot v)$: the matrix formula expresses the same operation as the vector formula. For example, at $k=(1,0,0)$, the projection $\mathbb P_k$ sends $(v_1,v_2,v_3)$ to $(0,v_2,v_3)$.

This subtracts the component parallel to $k$, leaving $k\cdot\mathbb P_kv=0$. The zero mode is left unchanged. Applying this projection gives

$$
u_t-\nu\Delta u=B(u,u)+\mathbb Pf,
\qquad B(v,w)=-\mathbb P[(v\cdot\nabla)w].
$$

The projection performs the pressure correction mode by mode. This is why one may use the projected equation in a proof while retaining the effect of pressure. Nonlinearity multiplies Fourier modes, so their wavevectors add; even finite initial spectral support can evolve into an infinite set of modes.

## Measure energy and deformation

**First reading:** products, integrals and [integration by parts](calculus-bridge.md#5-integration-by-parts-becomes-an-energy-calculation). The later strain calculation also uses matrices.

The kinetic energy is $E(t)=\frac12\int_{\mathbb T^3}|u|^2\,dx$. To find its rate of change, multiply the equation by $u$ and integrate. The two cancellations are

$$
\int u\cdot(u\cdot\nabla)u
=\int\nabla\cdot\left(\frac{|u|^2}{2}u\right)=0,
\qquad
\int u\cdot\nabla p=\int\nabla\cdot(pu)=0.
$$

Boundary contributions cancel between opposite periodic faces. Integration by parts in the viscous term then gives

$$
E'(t)=-\nu\int|\nabla u|^2\,dx+\int f\cdot u\,dx.
$$

The unforced energy decreases. With forcing, the second integral is the rate of external work and may have either sign. This scalar budget is necessary for a smooth solution; it does not determine the spatial momentum equation.

For the exact shear above,

$$
E(t)=\frac{(2\pi)^3}{4}a(t)^2,
\qquad \int|\nabla u|^2\,dx
=\frac{(2\pi)^3}{2}N^2a(t)^2.
$$

Differentiating the first formula using $a'=-\nu N^2a$ verifies the energy law, including its constants.

Now keep $a(t)$ fixed at a particular instant and compare two shears with different $N$. Their energies agree, but their velocity gradients differ by the frequency ratio. Energy alone cannot distinguish a gently varying velocity from one with the same size and finer spatial variation.

To measure the deformation of nearby particles, introduce the symmetric matrix

$$
S=\frac{\nabla u+\nabla u^T}{2}
$$

called **strain**. For a separation vector $r$ carried by the linearized particle flow, $r'=(\nabla u)r$, so $\frac d{dt}|r|^2=2r\cdot Sr$. The antisymmetric part rotates the vector without contributing to that rate. The integral $Q=\int|S|_F^2\,dx$ measures the total squared strain; $|S|_F^2$ is the sum of the squared matrix entries. In the shear, $S_{12}=S_{21}=Na(t)\cos(Ny)/2$, and $Q=N^2E$. Doubling the frequency at fixed amplitude therefore quadruples both the squared strain and the energy-dissipation rate.

<details markdown="1">
<summary>Reference: the norm conventions used by the research chapters</summary>

Write $u(x)=\sum_k\widehat u(k)e^{ik\cdot x}$. The activation notes use

$$
\|u\|_{2,\mathrm{av}}^2=(2\pi)^{-3}\int_{\mathbb T^3}|u|^2=\sum_k|\widehat u(k)|^2,
\qquad \|u\|_{A^s}=\sum_k|k|^s|\widehat u(k)|.
$$

The $A^s$ norm sums Fourier amplitudes weighted by frequency. The averaged $L^2$ norm makes Parseval's identity a sum with no volume factor; the energy above uses the unnormalized integral. Converting between them requires the factor $(2\pi)^3$. A separate issue arises with strain estimates: control of $S$ in the sup norm does not, through a general Korn inequality, give sup-norm control of every component of $\nabla u$.

</details>

## Unforced and smoothly forced problems

Local smooth existence is a starting theorem. Questions about later breakdown depend on what is prescribed in the equation, especially the force. The [two-track program](../../references/navier-stokes/two-track-program.md) distinguishes the following statements; the [published-proof chapter](published-proof.md) discusses the external forced C/D result.

| Track | Fixed inputs | What would complete the task |
|---|---|---|
| Unforced ROOT | One fixed $\nu>0$; $f=0$; admissible smooth periodic divergence-free data | Prove global smooth existence for every such datum, or refute it with a counterexample from one such datum. ROOT names the global regularity claim. |
| FORCED-D | One fixed $\nu>0$, one smooth periodic divergence-free datum, and one prescribed admissible smooth periodic force | Prove that no global smooth periodic velocity and pressure solve those data. Finite-time breakdown of the unique classical solution would suffice. |

For FORCED-D, the force must be smooth **through** any proposed terminal time $T$, and defined for all later times with every mixed derivative decaying faster than every power of time. Explicitly, for each spatial multi-index $\alpha$ and integers $m,K\ge0$, there must be a finite constant $C_{\alpha,m,K}$ such that

$$
\sup_x|\partial_x^\alpha\partial_t^m f(t,x)|
\le C_{\alpha,m,K}(1+t)^{-K}.
$$

A force with a smooth extension through $T$ can be smoothly cut off later, giving the required time decay. Smoothness only for $t<T$ is insufficient. If the force is obtained by inserting a proposed velocity into the equation, its complete extension and all these bounds still have to be proved.

The shear makes this distinction computable. With $N=1$, prescribing $a(t)=(T-t)^{-1}$ requires

$$
f=\left[\frac1{(T-t)^2}+\frac{\nu}{T-t}\right]\sin y\,e_1.
$$

This is smooth at every time before $T$, but diverges at $T$, so it does not meet FORCED-D. Conversely, if $a'+\nu a=g(t)$ with bounded smooth $g$, then

$$
a(t)=e^{-\nu t}a(0)+\int_0^t e^{-\nu(t-s)}g(s)\,ds
$$

stays bounded on each finite interval. The same shear thus gives both a failed forced construction and an exact explanation of its failure. The external forced result requires a different mechanism, explained in [the published-proof chapter](published-proof.md). The project's unforced ROOT claim and its separate $(E′)$ estimate remain open.

## Exercises

### 1. Check the admissible datum

Show that $u_0=A(\cos Ny,\cos Nz,\cos Nx)$, with $A\ne0$ and positive integer $N$, is mean-zero and divergence-free. Is it independent of some fixed spatial direction? Compare it with the worked shear.

<details markdown="1"><summary>Solution and feedback</summary>

Each component has zero mean and is independent of its matching coordinate, so $\partial_xu_1+\partial_yu_2+\partial_zu_3=0$. Its nonzero wavevectors lie on all three coordinate axes and span $\mathbb R^3$. A translation-invariance direction would have to be perpendicular to every one of them, so it must be zero. The shear is independent of both $x$ and $z$. Divergence-free does not imply that a flow effectively depends on fewer spatial coordinates.

</details>

### 2. Recover pressure in another exact flow

Take $u=a(t)(\sin y,\sin x,0)$. Compute $(u\cdot\nabla)u$, and show that $p=a(t)^2\cos x\cos y$ cancels it. Find the ODE for $a$ in the unforced equation. What goes wrong if one sets $p=0$ without projecting?

<details markdown="1"><summary>Solution and feedback</summary>

The transport is $a^2(\sin x\cos y,\sin y\cos x,0)$, which is $-\nabla p$. Also $\Delta u=-u$, so $a'=-\nu a$. Without pressure, the proposed acceleration would have divergence $-2a^2\cos x\cos y$, contradicting preservation of incompressibility when $a\ne0$. Pressure does no net work in the periodic energy law, yet it is essential in the pointwise equation.

</details>

### 3. Use the energy check, then identify its limit

Verify $Q=N^2E$ for the worked shear. Suppose a different smooth divergence-free field has the same energy and energy-decay rate at one instant. Must it have the same subsequent velocity?

<details markdown="1"><summary>Solution and feedback</summary>

The two off-diagonal strain entries give $|S|_F^2=N^2a^2\cos^2(Ny)/2$. Integrating yields $Q=(2\pi)^3N^2a^2/4=N^2E$. Matching two scalar measurements does not specify a vector field or its spatial momentum equation. The equality is an exact check on this example, not a uniqueness principle based only on energy.

</details>

### 4. Diagnose a proposed forced singularity

A proposed velocity has a singularity at $T$, and its computed force is smooth for every $t<T$. The author concludes that FORCED-D is proved. Identify the missing requirement. For the shear equation with $|g(t)|\le G$, obtain an explicit upper bound on $|a(t)|$.

<details markdown="1"><summary>Solution and feedback</summary>

The force must extend smoothly through $T$, with all mixed derivative bounds and the required later-time decay. Preterminal smoothness alone does not establish this. The integrating-factor formula gives

$$
|a(t)|\le e^{-\nu t}|a(0)|+\frac G\nu(1-e^{-\nu t}).
$$

Thus bounded forcing cannot produce amplitude blow-up in this particular shear. This rules out that construction, not general smoothly forced breakdown.

</details>

Continue with the [fluid laboratory](simulator.md) to inspect these checks numerically, or with [frequency creation](activation.md) to study what the shear's cancellation leaves out.

## Further reading

For a systematic treatment of the equation, particle trajectories and pressure projection, read Andrew J. Majda and Andrea L. Bertozzi's [*Vorticity and Incompressible Flow*](https://www.cambridge.org/core/books/vorticity-and-incompressible-flow/393C35E544EDD0711CAA7F7AB05D7432), beginning with Chapter 1. Its [Chapter 3 on energy methods](https://www.cambridge.org/core/books/abs/vorticity-and-incompressible-flow/energy-methods-for-the-euler-and-the-navierstokes-equations/E5489F542D15DFDC03F96046A8E05265) develops the estimates behind local existence and comparison of solutions.

Charles Fefferman's [official Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) specifies the unforced and forced alternatives, their domains, and the regularity required of the data. Read the hypotheses alongside any proposed example.

Project derivations: [frequency activation, §§1–2](../../references/navier-stokes/frequency-activation.md), and [the two-track statement and exact forced shear](../../references/navier-stokes/two-track-program.md).
