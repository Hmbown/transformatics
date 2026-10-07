# Scale, norms, and resolution

A model may predict its velocity to within $10^{-4}$, yet miss a requested
physical tolerance. If physical velocity is ten times the model velocity,
the error becomes $10^{-3}$. If the model coordinates also magnify
lengths by a factor of one hundred, the same $10^{-4}$ bound on a model
derivative becomes a physical derivative bound of $0.1$. Differentiation
introduces a length conversion in addition to the amplitude conversion.

We will derive these factors rather than memorize a table. Substitution
in an integral accounts for volume; the chain rule accounts for derivatives
and time. Carrying the factors through the fluid equation will then show
that a single wave has the same viscous attenuation in either description.

The [composition theorem](transfer-systems.md) already tells us that a
change of representation can magnify an error. Scaling gives a particularly
explicit instance: the conversion factor depends on the chosen norm and
on the domain. We begin with one field on $\mathbb R^d$, then distinguish
that calculation from repeating a periodic pattern inside a fixed box.

## A field viewed at another scale

Let $v:\mathbb R^d\to\mathbb R^m$ be a field, smooth enough for the derivatives used below and with the stated norms finite. Define

$$
w(x)=A v(Lx),\qquad A>0,\quad L>0.
$$

The amplitude is multiplied by $A$. A feature of width one in $y=Lx$ has width $1/L$ in $x$. Thus $L>1$ narrows features and $L<1$ broadens them. For $1\leq p<\infty$, the $L^p$ norm is $(\int|v|^p)^{1/p}$. Each of the $d$ coordinates contributes a factor $1/L$ to volume, so $dx=L^{-d}dy$ and

$$
\|w\|_{L^p(\mathbb R^d)}^p
=A^p L^{-d}\int_{\mathbb R^d}|v(y)|^pdy,
\qquad \|w\|_p=A L^{-d/p}\|v\|_p.
$$

The $L^\infty$ norm measures the supremum size for these continuous fields, so its factor is simply $A$. The chain rule gives $\partial_{x_i}w(x)=AL(\partial_{y_i}v)(Lx)$. Repeating it adds one factor of $L$ for each derivative. Writing $D^r$ for the array of derivatives of order $r$,

$$
\|D^r w\|_p=A L^{r-d/p}\|D^r v\|_p.
$$

These statements also apply between correspondingly rescaled domains. On a fixed periodic box, $v(Lx)$ may repeat many copies instead of concentrating one copy; the domain and norm normalization must then be included explicitly. For example, when $L$ is a positive integer,

$$
\frac1{2\pi}\int_0^{2\pi}\sin^2(Lx)\,dx=\frac12.
$$

The normalized $L^2$ norm of $\sin(Lx)$ is unchanged: there are $L$ copies in the same box. This is not one concentrating copy on $\mathbb R$.

## Worked example: small energy, large gradient

Take a smooth, compactly supported, nonconstant scalar field $\phi$ on $\mathbb R^3$, and set $w_L(x)=\phi(Lx)$. Then

$$
\|w_L\|_2=L^{-3/2}\|\phi\|_2,
\qquad \|\nabla w_L\|_\infty=L\|\nabla\phi\|_\infty.
$$

For $L=10$, the square-integrated amplitude $\|w_L\|_2^2$ is $10^{-3}\|\phi\|_2^2$, while the maximum gradient is ten times larger. As $L\to\infty$, the first quantity tends to zero and the second diverges. A small $L^2$ error does not by itself control a derivative. If an approximation theorem needs $C^1$ accuracy, it must obtain it from further derivative information, interpolation, or a different norm.

For a velocity field $v:\mathbb R^d\to\mathbb R^d$, the same scaling holds componentwise. If $\nabla\cdot v=0$, then $\nabla\cdot[A v(Lx)]=AL(\nabla\cdot v)(Lx)=0$. Concentration can therefore preserve incompressibility. This calculation describes fields, without asserting that they form a solution trajectory of a particular evolution equation.

**Test the difference between a family and a flow.** Choose the scalar bump above to equal $1-|y|^2$ near the origin. Try to turn its scale into time by setting $w(t,x)=\phi(L(t)x)$, with $L(t)>0$. At the origin,

$$
\partial_t w(t,0)=0,
\qquad \nu\Delta_x w(t,0)=-6\nu L(t)^2.
$$

The central value stays equal to one, while heat diffusion would make it decrease. Thus this path does not solve even the scalar heat equation $w_t=\nu\Delta w$. Letting $L(t)$ diverge does not change that failure. To turn a family of fields into a fluid trajectory, we must verify the full evolution equation with one initial datum; the norm-scaling formulas alone cannot do this.

## Scaling an evolution equation

Spatial scaling describes a family of fields. To transform an evolution,
we must also choose its time and pressure scales so that the terms in the
equation can be compared. The calculation below fixes those choices and
derives the resulting viscosity.

The unforced incompressible Navier–Stokes equation is

$$
\partial_t u+(u\cdot\nabla_x)u+\nabla_x p
=\nu\Delta_x u,\qquad \nabla_x\cdot u=0.
$$

Here $u$ is velocity, $p$ is pressure per unit density, and $\nu>0$ is the coefficient of viscous diffusion. Write $y=Lx$, $s=ALt$, and set

$$
u(t,x)=Aq(s,y),\qquad p(t,x)=A^2\pi(s,y).
$$

All quantities on the right below are evaluated at $(s,y)=(ALt,Lx)$. Apply the chain rule term by term:

$$
\begin{aligned}
\partial_tu&=A(AL)\partial_sq=A^2L\partial_sq,\\
(u\cdot\nabla_x)u&=(Aq\cdot L\nabla_y)(Aq)
=A^2L(q\cdot\nabla_y)q,\\
\nabla_xp&=A^2L\nabla_y\pi,\\
\nu\Delta_xu&=\nu AL^2\Delta_yq.
\end{aligned}
$$

Dividing the equation by $A^2L$ gives

$$
\partial_s q+(q\cdot\nabla_y)q+\nabla_y\pi
=\epsilon\Delta_y q,\qquad \epsilon=\frac{\nu L}{A}.
$$

Also $\nabla_x\cdot u=AL\nabla_y\cdot q$, so incompressibility is
preserved. The coefficient $\epsilon=\nu L/A$ measures diffusion in the
new variables. Keeping the old viscosity while changing the other terms
would describe a different physical evolution.

These formulas have two uses. For **nondimensionalization**, take $A=U$, a physical velocity scale, and $L=1/\ell$, the inverse of a physical length scale. Then $y=x/\ell$, $s=Ut/\ell$, and

$$
\epsilon=\frac{\nu}{U\ell}.
$$

This coefficient is dimensionless: $\nu$ and $U\ell$ both have units of length squared per time. A rescaled time interval of length one corresponds to physical time $\ell/U$.

For **constructing a rescaled solution in fixed units**, start with an NS solution $u$ and choose the dimensionless factors $A=L=\rho$. The viscosity is preserved, giving the familiar NS scaling

$$
u_\rho(t,x)=\rho u(\rho^2t,\rho x),\qquad
p_\rho(t,x)=\rho^2p(\rho^2t,\rho x).
$$

The same algebra works on rescaled periodic domains. Whole-space scale invariance compares solutions on the same spatial domain $\mathbb R^3$; a torus changes size under the spatial rescaling unless a different interpretation is stated.

## Converting a model error back to physical variables

Suppose $q_{\mathrm{app}}$ approximates $q$ at rescaled time $s$, and reconstruct $u_{\mathrm{app}}(t,x)=Aq_{\mathrm{app}}(ALt,Lx)$. At the corresponding physical time $t=s/(AL)$, the same chain rule gives

$$
\begin{aligned}
\|u-u_{\mathrm{app}}\|_\infty
&=A\|q-q_{\mathrm{app}}\|_\infty,\\
\|\nabla_x(u-u_{\mathrm{app}})\|_\infty
&=AL\|\nabla_y(q-q_{\mathrm{app}})\|_\infty.
\end{aligned}
$$

Take $A=10$ metres per second and $L=20$ per metre, with $q,y,s$ dimensionless. Bounds of $10^{-4}$ on both the rescaled velocity error and its gradient give physical bounds of $0.001$ metres per second on velocity and $0.02$ per second on its gradient. To require physical gradient error at most $0.001$ per second, the rescaled gradient bound would need to be at most $0.001/(10\cdot20)=5\times10^{-6}$.

This is the conversion needed in the preceding chapter's error estimates. Choose the norm and physical tolerance before interpreting a small rescaled error.

## Critical measurements

For the NS scaling in three dimensions,

$$
\|u_\rho(t)\|_p=\rho^{1-3/p}\|u(\rho^2t)\|_p.
$$

The spatial $L^3$ norm is unchanged. It is called **critical** for this scaling. At $p=2$, the exponent is $-1/2$; kinetic energy can be small at a concentrating scale. At $p=\infty$, the exponent is one. Here the rescaled solution at time $t$ is compared with the original solution at time $\rho^2t$. This identity does not say that the norm of one solution is constant in time.

The time-space norm $L^q_tL^p_x$ first measures the spatial $L^p$ size at each time, then takes its $L^q$ norm over time. For finite $q$, set $s=\rho^2t$ to obtain

$$
\int_0^{T/\rho^2}\|u_\rho(t)\|_p^q\,dt
=\rho^{q(1-3/p)-2}\int_0^T\|u(s)\|_p^q\,ds.
$$

Taking the $q$th root gives

$$
\|u_\rho\|_{L^q(0,T/\rho^2;L^p)}
=\rho^{1-3/p-2/q}\|u\|_{L^q(0,T;L^p)}.
$$

The same formula holds for infinite exponents with $1/\infty=0$. Thus the critical relation is $3/p+2/q=1$; for example, $L^4_tL^6_x$ is critical because $3/6+2/4=1$. Proving that a particular solution actually has a bounded critical norm is a separate analytic task. The equality of exponents alone supplies no such bound.

## Worked example: the diffusion number survives a coordinate change

Consider a heat mode in rescaled coordinates,

$$
q(s,y)=b\,e^{-\epsilon|\xi|^2s/k^2}\cos(\xi\cdot y/k).
$$

Here $k>0$, $\xi\ne0$, and $b$ is a constant vector. Two derivatives of the cosine give $-|\xi|^2/k^2$ times that cosine, so $q_s=\epsilon\Delta_yq$. If $b\cdot\xi=0$, divergence and nonlinear self-advection also vanish, giving a special NS solution with constant pressure. The mode is defined on all space, or on a periodic box compatible with its wavevector; on all space it need not have finite energy.

The parameter $k$ is a length scale, not the full wavelength. In the $\xi$ direction the **rescaled wavelength** is $2\pi k/|\xi|$. Since $y=Lx$, the **physical wavelength** is $2\pi k/(L|\xi|)$, and the physical wavevector is $\kappa_{\mathrm{phys}}=L\xi/k$.

Over a rescaled time interval $\Delta$, the amplitude is multiplied by $e^{-\mathcal D}$, where $\mathcal D=\epsilon|\xi|^2\Delta/k^2$. The corresponding physical interval is $\Delta t=\Delta/(AL)$. Calculating directly in physical variables gives

$$
\begin{aligned}
\nu|\kappa_{\mathrm{phys}}|^2\Delta t
&=\nu\frac{L^2|\xi|^2}{k^2}\frac{\Delta}{AL}\\
&=\frac{\nu L}{A}\frac{|\xi|^2\Delta}{k^2}
=\mathcal D.
\end{aligned}
$$

This **dimensionless diffusion number** is invariant under the joint transformation. Equivalently, for physical wavelength $\lambda$, it is $4\pi^2\nu\Delta t/\lambda^2$. Relabeling a later stage with new coordinates cannot remove the damping already incurred in physical time.

Using metres and seconds as the physical units, choose $\nu=0.01$, $A=10$, $L=20$, $k=0.2$, and $\Delta=0.1$. Then $\epsilon=0.02$, and, choosing $|\xi|=1$, $\mathcal D=0.02(0.1)/(0.2)^2=0.05$. The physical interval is $0.1/(10\cdot20)=0.0005$, the physical wavevector has length $20/0.2=100$, and $\nu(100)^2(0.0005)=0.05$ again. The physical wavelength is $2\pi/100$, and the amplitude multiplier is $e^{-0.05}\approx0.95123$.

## Resolution is another representation map

On a periodic box of side $2\pi$, an $N^3$ grid samples positions $x_j=2\pi j/N$. Exponentials with frequencies $k$ and $k+Nm$, for integer vectors $m$, agree at every sampled point. This is **aliasing**: distinct continuum fields share the same grid representation.

Products create sums of frequencies. If the retained coordinates satisfy $|k_i|\leq K$, a quadratic product can reach $|k_i|=2K$. A wrapped frequency coordinate lies at least $N-2K$ from zero. Requiring $N-2K>K$ keeps it outside the retained band, giving the sufficient strict cutoff $3K<N$. The laboratory uses a two-thirds dealiased spectral approximation with its precise integer cutoff stated in the implementation. A visible tracer curve cannot reveal unresolved modes; the resolution is a mathematical part of the model.

Time discretization adds a second approximation. For advection, information crosses one grid cell in a time of order $\Delta x/\|u\|_\infty$. An explicit method therefore chooses a time step using a CFL restriction. Integrating viscosity exactly for each Fourier mode removes the corresponding linear diffusion step restriction, but does not remove the nonlinear accuracy and stability requirements.

## What a simulator could inherit from a proof

A global existence theorem would answer whether an appropriate continuum solution persists. To turn that into a numerical guarantee, one would additionally need an estimate of a form such as

$$
\sup_{0\leq t\leq T}\|u(t)-u_{N,\tau}(t)\|_X
\leq C(T,u_0,\nu)\bigl(N^{-s}+\tau^p\bigr),
$$

with proved hypotheses, a specified norm $X$, and a controlled constant. This formula is an example of the required approximation contract, not a theorem asserted for our solver. It shows why a proof and a simulation must be connected through stability and error analysis.

For a singularity construction, the corresponding numerical question
concerns intervals before the singular time and a criterion for losing
resolution. The [published-proof chapter](published-proof.md) concerns
a continuum breakdown construction; reproducing its behavior numerically
would require this additional approximation analysis.

## Exercises

1. For a nonzero smooth compactly supported field $v$, set $w_L(x)=L^\alpha v(Lx)$ on $\mathbb R^d$. Find the exponent of $\|D^r w_L\|_p$. Use it in three dimensions with $\alpha=1/2$ to compute the scaling of kinetic energy, $\|\nabla w_L\|_2^2$, and $\|\nabla w_L\|_\infty$. Which of these controls would permit an unbounded maximum gradient? Then let $L=L(t)$ and calculate $\partial_t w_{L(t)}$. Why is this additional calculation necessary before claiming a solution trajectory?
2. A new model uses $u=4q$, $y=50x$, and $s=200t$. It bounds both $\|q-q_{\mathrm{app}}\|_\infty$ and $\|\nabla_y(q-q_{\mathrm{app}})\|_\infty$ by $2\times10^{-5}$. Convert both errors and the interval $0\leq s\leq2$ to physical variables. Is physical gradient error at most $10^{-3}$ certified?
3. Derive the scaling factor for $\|p_\rho\|_{L^q_tL^p_x}$, where $p_\rho=\rho^2p(\rho^2t,\rho x)$, on the corresponding time intervals. State its critical relation. **Diagnose the claim:** “The velocity $L^3$ norm is scaling-critical, so it is conserved as the fluid evolves.”
4. A physical wavelength is halved while viscosity stays fixed. By what factor must the physical duration change to preserve its diffusion number? What happens to the attenuation exponent if duration is only halved? Can a new coordinate label alter that conclusion?
5. On a one-dimensional grid with $N=12$, show that multiplying two complex frequency-$4$ modes produces a frequency that aliases back to $-4$. Explain the strict condition $3K<N$. Which largest integer cutoff meets it?

<details markdown="1">
<summary>Hints</summary>

For 1, separate amplitude, derivative, and volume factors before squaring any norm. When $L$ varies with time, differentiate both $L^\alpha$ and the argument $Lx$. For 2, velocity and gradient have different conversion factors. For 3, change the time interval as well as the integrand. For 4, use $\mathcal D=4\pi^2\nu\Delta t/\lambda^2$. For 5, frequencies differing by $N$ agree on the grid.

</details>

<details markdown="1">
<summary>Solutions</summary>

**1.** The general exponent is $\alpha+r-d/p$. With $d=3$ and $\alpha=1/2$, energy has exponent $2\alpha-3=-2$, the squared gradient norm has exponent $2\alpha+2-3=0$, and the maximum gradient has exponent $\alpha+1=3/2$. Both small energy and a bounded **spatial integral** of the squared gradient are compatible with an unbounded maximum gradient in this family of fields.

At $y=L(t)x$, the time derivative is

$$
\partial_t w_{L(t)}(x)
=L'(t)L(t)^{\alpha-1}\bigl[\alpha v(y)+y\cdot\nabla v(y)\bigr].
$$

It contains terms that do not appear in the spatial norm identity. Those terms must satisfy the chosen evolution equation, together with its other spatial terms and initial data. Relabeling $L$ as a function of time does not supply that equality.

**2.** The physical velocity error is at most $4(2\times10^{-5})=8\times10^{-5}$. The gradient error is at most $4\cdot50(2\times10^{-5})=0.004$, and the interval is $0\leq t\leq2/200=0.01$. The gradient target is not certified. It would require a rescaled gradient bound of at most $10^{-3}/200=5\times10^{-6}$.

**3.** The factor is $\rho^{2-3/p-2/q}$, with the rescaled solution on the interval $(0,T/\rho^2)$ on the left and original interval $(0,T)$ on the right. Pressure is critical when $3/p+2/q=2$. Criticality compares rescaled solutions; conservation compares different times of a single solution. The former does not imply the latter. For a concrete counterexample to the conservation claim, take the transverse decaying heat wave above on a compatible periodic box: its velocity $L^3$ norm decays with its amplitude.

**4.** The duration must be divided by four. Dividing it only by two doubles $\mathcal D$, so an original multiplier $e^{-\mathcal D}$ becomes $e^{-2\mathcal D}$. Changing coordinates preserves this physical attenuation.

**5.** The product has frequency $8$. At grid points, $e^{8ix_j}=e^{-4ix_j}$, because their frequencies differ by $12$. Retaining the boundary $|k|=4$ allows this product to corrupt a retained coefficient. The largest integer satisfying $3K<12$ is $K=3$.

</details>

## Further reading

Alexandre J. Chorin and Jerrold E. Marsden's [*A Mathematical Introduction
to Fluid Mechanics*, third edition](https://link.springer.com/book/10.1007/978-1-4612-0883-9)
(Springer, 1993) develops the equations of motion and the physical
interpretation of fluid quantities. Read its derivation of the equations
alongside the change-of-variables calculation here: a choice of units must
transform the equation as well as the field.

For spatial and temporal approximation of differential equations, see
Randall J. LeVeque, [*Finite Difference Methods for Ordinary and Partial
Differential Equations*](https://faculty.washington.edu/rjl/fdmbook/)
(SIAM, 2007). Use the two-wave assessment to distinguish the effects of
refining a time step, retaining another frequency and changing the norm in
which accuracy is requested.
