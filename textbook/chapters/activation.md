# Creating a new frequency

The exact shear in [the fluid chapter](equation.md) decays without changing its shape. A sum of shears can behave differently: one component transports another, multiplying their waves and creating new frequencies. Here we follow one initially absent Fourier coefficient from its first interaction to a definite positive size in the actual solution.

Use the Fourier convention from [composition](composition.md) and the pressure projection from [the fluid equation](equation.md). The argument has three steps: calculate production, include diffusion, and bound the remaining interactions. We then ask whether the new coefficient increases total strain energy or maximum speed. The answers differ, even along the same evolution.

## 1. Choose a measurement that starts at zero

Work on the periodic box $\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3$, with fixed viscosity $\nu>0$ and no forcing. Take a positive integer $N$ and amplitude $A>0$, and set

$$
u_0=A(\cos Ny,\cos Nz,\cos Nx).
$$

Each component is independent of its matching coordinate, so the divergence is zero. The six initial wavevectors are $\pm Ne_1,\pm Ne_2,\pm Ne_3$. They span all three spatial directions. Individually these shears have no self-advection; together they transport one another.

Before expanding the advection term, trace the transport of the third component. It depends only on the first coordinate: which velocity component multiplies its nonzero derivative? Predict the sums and differences of wavevectors that this multiplication can produce.

Our observable is the third velocity coefficient at $k_*=N(1,1,0)$. With the convention $u(x)=\sum_k\widehat u(k)e^{ik\cdot x}$, this coefficient is initially zero: $|k_*|=\sqrt2N$, while all initial waves have length $N$. We will show that its negative imaginary part becomes positive. The conjugate coefficient at $-k_*$ makes the resulting physical velocity real.

## 2. Work out the first interaction

Before calculating an approximation, evaluate the nonlinear term at the initial field. For its first component,

$$
(u_0\cdot\nabla)(u_0)_1
=A\cos Nz\,\partial_y(A\cos Ny)
=-A^2N\sin Ny\cos Nz.
$$

The other components follow by cycling the coordinates. Thus

$$
-(u_0\cdot\nabla)u_0
=A^2N(\sin Ny\cos Nz,\sin Nz\cos Nx,\sin Nx\cos Ny).
$$

This output is also divergence-free: its first component is independent of $x$, its second of $y$, and its third of $z$. The Leray pressure projection therefore leaves this first interaction unchanged. Later products need not have the same structure, so we retain the projection in the evolution equation.

To extract the coefficient at $k_*$, expand the third component:

$$
\sin Nx\cos Ny
=\frac{(e^{iNx}-e^{-iNx})(e^{iNy}+e^{-iNy})}{4i}.
$$

The coefficient of $e^{iN(x+y)}$ is $1/(4i)=-i/4$. Consequently

$$
\partial_t\widehat u_3(k_*,0)=-\frac{iA^2N}{4}.
$$

The viscous term contributes zero to this initial derivative because the coefficient itself starts at zero. As soon as the new wave appears, however, diffusion begins damping it. Its later amplitude depends on production and decay throughout the interval.

## 3. Include diffusion during production

Write $B(v,w)=-\mathbb P[(v\cdot\nabla)w]$. Start with the heat evolution of the initial field:

$$
U_1(t)=e^{\nu t\Delta}u_0=e^{-\nu N^2t}u_0.
$$

The first nonlinear correction accumulates the interaction of these decaying waves. Duhamel's formula evolves each contribution from the moment it is produced to the observation time:

$$
U_2(t)=\int_0^t e^{\nu(t-s)\Delta}B(U_1(s),U_1(s))\,ds.
$$

At the production time $s$, the input product has the factor $e^{-2\nu N^2s}$. The output wave has squared frequency $2N^2$, so its subsequent decay contributes $e^{-2\nu N^2(t-s)}$. Their product is independent of $s$. Integration gives

$$
\widehat{(U_2)}_3(k_*,t)
=-\frac{iA^2Nt}{4}e^{-2\nu N^2t}.
$$

This is an exact coefficient of the second approximation term. The factor $t$ measures accumulated production; the exponential records the damping of both the inputs and the output. We now need to compare that term with the actual solution.

## 4. Transfer the calculation to the actual solution

The new wave interacts with the old waves and with later outputs. To retain those interactions, organize the solution by degree in the initial amplitude. For $n\ge2$, define

$$
U_n(t)=\sum_{a+b=n}\int_0^t
e^{\nu(t-s)\Delta}B(U_a(s),U_b(s))\,ds.
$$

The sum includes all ordered positive integers $a,b$. Each term has frequencies at most $nN$; the full series can have infinitely many frequencies. This expansion includes feedback into the original modes as well as production of new ones.

To bound all of them together, use the **Wiener norm**

$$
\|v\|_{A^0}=\sum_k|\widehat v(k)|.
$$

Here the subscripted $A^0$ names a function space; it is separate from the amplitude $A$. Every individual coefficient is at most this norm. For our datum, $W=\|u_0\|_{A^0}=3A$: each of the six coefficients has magnitude $A/2$.

The [complete source proof](../../references/navier-stokes/frequency-activation.md) shows that the series converges to the smooth solution when $3NWt<1$, and that the remainder $R=\sum_{n\ge3}U_n$ satisfies

$$
\|R(t)\|_{A^0}\le
\frac{3W}{2}\frac{(NWt)^2}{1-3NWt}.
$$

The Wiener norm controls every individual coefficient, so it can be compared directly with our signal. This is the stability principle developed in [residuals](residuals.md), applied here using a convergent expansion. Since $U_1$ has no coefficient at $k_*$,

$$
-\operatorname{Im}\widehat u_3(k_*,t)
\ge \frac{A^2Nt}{4}e^{-2\nu N^2t}-\|R(t)\|_{A^0}.
$$

Put $\tau=ANt$, a dimensionless time. Substituting $W=3A$ and dividing by $A^2Nt$ for $t>0$ gives

$$
\frac{-\operatorname{Im}\widehat u_3(k_*,t)}{A^2Nt}
\ge \frac{e^{-2\nu N^2t}}4
-\frac{81\tau}{2(1-9\tau)}.
$$

If $A\ge\nu N$ and $0<\tau\le1/512$, the first term is at least $255/1024$, while the subtracted term is at most $81/1006$. Their difference exceeds $1/8$. We have obtained a positive lower bound over a specified interval for the full equation.

<details markdown="1">
<summary>What the convergence proof has to justify</summary>

The source bounds each homogeneous term by $Wc_n(NWt)^{n-1}$, with $c_n=n^{n-1}/n!$ and $c_{n+1}/c_n<3$. Starting at $c_3=3/2$, a geometric sum gives the stated remainder. Since the $n$th term has frequencies at most $nN$, each fixed number of spatial derivatives adds only a polynomial factor in $n$. The series still converges on every closed shorter interval. This justifies differentiation and substitution into the full equation. The source also proves uniqueness there. Merely writing a formal series would leave these steps unfinished.

</details>

## 5. A local theorem stable under small perturbations

The source also allows a real, mean-zero, divergence-free perturbation $w_0$ supported in $|k|\le N$, with $\|w_0\|_{A^0}\le A/256$. For

$$
u_0=A(\cos Ny,\cos Nz,\cos Nx)+w_0,
\qquad A\ge\nu N,
$$

it proves smooth existence through $t_*=1/(512AN)$ and

$$
-\operatorname{Im}\widehat u_3(k_*,t)\ge\frac{A^2Nt}{8}
\quad(0<t\le t_*).
$$

The support restriction keeps $k_*$ absent from the perturbed initial datum. Bounding the additional mixed and self-interactions then leaves enough margin for the same lower bound. The result therefore survives small changes in the starting waves.

At $t_*$, the coefficient has magnitude at least $A/4096$. The interval bound establishes activation, without requiring the coefficient to be monotone. To understand what this changes in the whole flow, consider total strain energy. For the unperturbed datum,

$$
Q(0)=\frac{3A^2N^2}{4},\qquad
Q'(0)=-\frac{3\nu A^2N^4}{2}<0,
$$

where this display uses the averaged integral $Q=(2\pi)^{-3}\int|S|_F^2$. A new coefficient appears while total strain energy initially decreases. The next calculation follows that apparent tension through a longer part of the same short evolution. The [concentration chapter](concentration.md) later changes the spatial arrangement of the waves.

## 6. Does the total strain energy eventually increase?

The negative initial derivative above does not settle what happens next.
To investigate it, translate all three spatial coordinates by
$-\pi/(2N)$. This replaces the cosines by positive sines without
changing any global norm. Set $X=Nx$, write the physical velocity as
$u=A U$ and physical pressure as $A^2p$, and rename the normalized
coordinates $X$ as $(x,y,z)$. Then

$$
U_0=(\sin y,\sin z,\sin x),\qquad
\tau=ANt,\qquad \mu=\frac{\nu N}{A}.
$$

The dimensionless number $\mu$ compares viscous damping with nonlinear
transfer. Put $F=(\sin z\cos y,\sin x\cos z,\sin y\cos x)$.
The first derivative is $U_\tau(0)=-F-\mu U_0$. Although the initial
pressure is zero, its first time derivative is already

$$
p_\tau(0)=-2\cos x\cos y\cos z.
$$

At the origin, the Hessian of this pressure derivative cancels the entire
second inviscid velocity-gradient derivative predicted by the unprojected
interaction. A cancellation at the first order has produced a necessary
pressure correction at the next.

The [complete second-order calculation](../../references/analysis/periodic-cycle-transfer.md)
gives a uniform local remainder for $0\le\mu\le1$: there are fixed
$T_0>0$ and $C\ge1$ such that

$$
\left|\frac{Q(\tau)}{Q(0)}-
\left[1-2\mu\tau+\left(\frac12+2\mu^2\right)\tau^2\right]\right|
\le C\tau^3,\qquad 0\le\tau\le T_0.
$$

Here $Q$ is the total strain energy of the normalized solution; the
ratio is independent of whether integrals are averaged. The positive
quadratic term accounts for the newly generated $\sqrt2$-frequency
shell and the change in the original shell together. It follows from
the full equation, with its pressure projection.

Choose one fixed $0<\tau_0\le\min(T_0,1/(4C),1)$, and suppose
$0<\mu\le\tau_0/16$. The three relevant contributions satisfy

$$
-2\mu\tau_0\ge-\frac{\tau_0^2}{8},\qquad
\left(\frac12+2\mu^2\right)\tau_0^2\ge\frac{\tau_0^2}{2},\qquad
-C\tau_0^3\ge-\frac{\tau_0^2}{4}.
$$

Therefore $Q(\tau_0)/Q(0)\ge1+\tau_0^2/8>1$: the initially declining
strain energy has risen above its starting value. Kinetic energy still
decreases by the exact energy identity. The flow has developed stronger
spatial variation while losing energy. Maximum speed is a third observable,
which requires its own calculation.

## 7. Which quantity grew?

Total strain energy and maximum speed measure different properties of a
velocity field. This same example separates them during one actual
evolution. Use the normalized velocity $U$ from section 6 and the
Euclidean speed $|U|$. Its initial maximum squared speed is

$$
M(0)=\max_{x,y,z}(\sin^2x+\sin^2y+\sin^2z)=3.
$$

The [moving-maximum calculation](../../references/analysis/cycle-next-transfer.md)
gives one fixed $T_*>0$ that works for every $0\le\mu\le1$:

$$
M(\tau)=\|U_\mu(\tau)\|_\infty^2
\le3-3\mu\tau-\frac45\tau^4<3\qquad(0<\tau\le T_*).
$$

Choose one fixed
$0<\tau_0\le\min(T_*,T_0,1/(4C),1)$, using the constants from
section 6, then take $0<\mu\le\tau_0/16$. The time is chosen before
the viscosity ratio $\mu=\nu N/A$. At that same time,

$$
Q(\tau_0)>Q(0),\qquad M(\tau_0)<M(0).
$$

The integral of squared strain has increased while maximum speed is
below its initial value. Integral growth does not require strain to
increase at every point. In physical units, the initial maximum speed
is $A\sqrt3$ and the observation time is $t_0=\tau_0/(AN)$.

This distinction matters when composing stages. A stage requiring greater
maximum speed cannot use this interval to obtain it. A stage requiring
increased $Q$ passes that test, but must also accept the outgoing shape,
orientation and available lifetime. The [iteration chapter](iteration.md)
formalizes those compatibility conditions. The present example supplies
one finite transfer; it does not establish that the resulting mixture can
repeat it at a new scale.

There is a subtle calculus point in this proof. A maximum can move.
Evaluating $|U(\tau,x)|^2$ at an initially maximizing point does not
compute its later global maximum. For the inviscid comparison, the source
follows all eight initial maxima and excludes other competing maxima for
small time. Their motion cancels an apparent quadratic loss at the fixed
points; the full pressure calculation gives a quartic loss instead.
A uniform comparison then controls the effect of positive viscosity.
The remainder estimates make the displayed inequality hold on an interval.

## Exercises

### 1. Predict all four signs

Find the coefficients of $\sin Nx\cos Ny$ at $(N,N,0)$, $(N,-N,0)$, $(-N,N,0)$, and $(-N,-N,0)$. Explain why the physical field is real.

<details markdown="1"><summary>Hint</summary>

Multiply the two exponential formulas from section 2. The sign comes from the sine factor, which depends on the first coordinate.

</details>

<details markdown="1"><summary>Solution</summary>

The four coefficients are $-i/4,-i/4,i/4,i/4$, respectively. Opposite wavevectors have conjugate coefficients, which is the Fourier reality condition. The two signs of the second coordinate have equal coefficients because the cosine is even.

</details>

### 2. An initial rate is not an interval bound

A calculation gives $g(0)=0$ and $g'(0)=1$. Does it establish $g(t)\ge t/2$ on $0\le t\le1$? Construct a smooth counterexample. What extra information played the corresponding role in our fluid calculation?

<details markdown="1"><summary>Hint</summary>

Try $g(t)=t-Ct^2$. Changing $C$ leaves the initial derivative unchanged.

</details>

<details markdown="1"><summary>Solution</summary>

With $C=1$, the function has the stated initial data but $g(1)=0<1/2$. A positive initial derivative gives positivity on some sufficiently short interval, without identifying a common interval for a family. In the fluid calculation, the full-series remainder bound specifies how small the interval must be relative to $A,N,\nu$.

</details>

### 3. State exactly what was activated

Compute the endpoint lower bound, check its units when $A$ is velocity and $N$ is inverse length, and decide whether the theorem implies an infinite cascade for one initial datum.

<details markdown="1"><summary>Hint</summary>

Substitute $t_*$ before interpreting the result. Identify both the observed frequency and the allowed interval.

</details>

<details markdown="1"><summary>Solution</summary>

The bound is $A^2N/(8\cdot512AN)=A/4096$. The rate $A^2N$ has units velocity per time; multiplication by $t_*$ returns velocity. One initially absent coefficient at length $\sqrt2N$ reaches that bound by a finite time. There is no estimate here that restarts the construction at infinitely many scales with the same datum. Increasing $N$ changes the datum and shortens the interval.

</details>

### 4. Identify the pressure error

At the stagnation point at $\tau=0$, suppose an unprojected second
interaction has gradient $2I$, while the Hessian of the first pressure
time derivative is $2I$.
What is their contribution to the second velocity-gradient derivative?
What basic condition would the unprojected answer violate?

<details markdown="1"><summary>Solution</summary>

The pressure-corrected contribution is $2I-2I=0$. Keeping $2I$
would give trace $6$, although incompressibility requires the trace
of every time derivative of the velocity gradient to vanish. This is
a quick consistency check; the full pressure calculation is still
needed to determine the actual trace-free part.

</details>

### 5. Match the gain to the next operation

In the normalized units of section 7, a proposed second stage requires
incoming maximum speed strictly above $\sqrt3$. Another requires
total strain energy strictly above $Q(0)$.
Which requirement does the evolution in section 7 meet at $\tau_0$?
What is the first speed threshold in physical units? Does either answer
establish that the entire second stage can run?

<details markdown="1"><summary>Solution</summary>

Since $M(\tau_0)<3$, maximum speed is below $\sqrt3$; the first
requirement fails. The second requirement holds because
$Q(\tau_0)>Q(0)$. Since $u=A U$, the physical speed threshold is
$A\sqrt3$. The increase in $Q$ does not establish the required
shape, spatial region, duration or compatibility of the incoming field.
Each of those conditions must be checked for the proposed second stage.

</details>

## Further reading

John K. Hunter's [*Notes on Partial Differential Equations*](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), §§5.1, 5.4–5.5 and Appendix 5.B, develop heat evolution, semigroups, semilinear equations and the Fourier transform. These supply the classical background for the Duhamel expansion used here. Majda and Bertozzi's [*Vorticity and Incompressible Flow*, Chapter 3](https://www.cambridge.org/core/books/abs/vorticity-and-incompressible-flow/energy-methods-for-the-euler-and-the-navierstokes-equations/E5489F542D15DFDC03F96046A8E05265) develops the energy methods behind comparisons of complete fluid evolutions.

The full calculations and constants for this example are in [the activation proof](../../references/navier-stokes/frequency-activation.md), [the total-enstrophy extension](../../references/analysis/periodic-cycle-transfer.md), and [the maximum-speed calculation](../../references/analysis/cycle-next-transfer.md). Their verification scope is recorded in the [claim register](../claims.md#nse-frequency-activation-local).

AI review is not external expert acceptance. These entries record the checking process, not certification.
