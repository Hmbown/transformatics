# Residuals, exact solutions, and smooth forcing

Suppose you have drawn a plausible motion, computed a promising wave, or built a sequence of increasingly accurate approximations. What would make that construction a solution of the equation? This chapter develops a concrete answer: insert the proposed field into the **complete equation**, keep the resulting residual as a mathematical object, and prove the estimate appropriate to your objective.

There are two different uses. A small residual can help locate a nearby solution of a prescribed equation. Alternatively, a constructed field can become an exact solution of a forced equation by taking its residual as the force. The first use requires stability. The second requires the force to satisfy the prescribed regularity and boundary conditions. Neither requirement follows merely from computing a small number.

The [September 2026 OpenAI release](https://openai.com/index/navier-stokes-solution/) reports a forced Navier–Stokes breakdown result establishing alternatives C and D, with smooth forcing. The [published-proof chapter](published-proof.md) treats that result and its scope. Here we develop elementary tools for understanding the distinction between singular motion and admissible forcing; this chapter is not a derivation of the released proof.

You should be comfortable with the product rule, integration by parts, and linear ODEs. The [composition chapter](composition.md) introduced propagation of a discrete defect; we now derive its continuous counterpart. The [concentration](concentration.md) and [viscous amplification](viscous.md) chapters show why the resulting time and derivative costs matter in fluid mechanics.

## 1. A residual belongs to a specified equation

Consider the scalar ODE

$$
y'=F(t,y),\qquad y(0)=y_0.
$$

For a differentiable trial function $v$, define

$$
r_v(t)=v'(t)-F(t,v(t)).
$$

This is the **equation residual**. Its sign is fixed by this definition. The initial discrepancy $v(0)-y_0$ is a separate object. A function can satisfy the differential equation exactly and still solve the wrong initial-value problem.

For example, $v(t)=1+t$ is a trial function for $y'=y$, $y(0)=1$. It starts correctly, but

$$
r_v=1-(1+t)=-t.
$$

The exact solution is $e^t$; its error relative to $v$ is $e^t-1-t$. The residual is not the error. One measures failure of the differential relation, while the other compares two states.

For an incompressible fluid, choose a trial velocity $U$, trial pressure $P$, viscosity $\nu>0$, and prescribed force $f$. Define the momentum residual

$$
\mathcal R[U,P;f]
=\partial_tU+(U\cdot\nabla)U+\nabla P-\nu\Delta U-f.
$$

There are additional requirements:

$$
\nabla\cdot U=0,\qquad U(0)=u_0,
$$

together with the chosen spatial conditions. The momentum residual alone does not test incompressibility or the initial datum. If a spatial cutoff has made $U$ compressible, reporting a small momentum residual leaves a different equation unsatisfied.

Pressure also belongs in this accounting. Replacing $P$ by $P+\chi$ changes $\mathcal R$ by $\nabla\chi$. For divergence-free evolution it is often useful to apply the Leray projector $\mathbb P$, which removes gradient fields on the periodic box. But when a particular physical force is prescribed, its full value and the compatible pressure must still be recovered. “The projected equation holds” and “this chosen velocity, pressure, and force satisfy the equation” require a stated relation between them.

## 2. Propagate the residual before judging it

Start with the linear vector equation

$$
y'=A(t)y+b(t).
$$

For a trial $v$, let $r=v'-Av-b$ and $e=y-v$. Subtraction gives the exact error equation

$$
e'=A(t)e-r.
$$

Let $\Phi(t,s)$ be the evolution matrix: $\partial_t\Phi(t,s)=A(t)\Phi(t,s)$ and $\Phi(s,s)=I$. Variation of constants gives

$$
e(t)=\Phi(t,0)e(0)-\int_0^t\Phi(t,s)r(s)\,ds.
$$

This identity says precisely how a residual at time $s$ affects the later state. Its size, direction, time of introduction, and subsequent propagation all matter. If $\|A(t)\|\le L(t)$, a sufficient estimate is

$$
\|e(t)\|
\le e^{\int_0^tL}\|e(0)\|
 +\int_0^t e^{\int_s^tL(\tau)\,d\tau}\|r(s)\|\,ds.
$$

This bound may be coarse: an exact evolution matrix can preserve directions or cancellations that the operator-norm estimate loses. The [shear example](composition.md) explains why eigenvalues alone do not replace a propagator bound. [Transfer systems](transfer-systems.md) also shows how changing the norm introduces a conversion cost when returning to the requested measurement.

**Worked comparison: the same residual in two equations.** Let $v=0$, let $\delta>0$, and start from zero. For

$$
y'=\lambda y+\delta,\qquad \lambda>0,
$$

the residual is constantly $-\delta$, but the exact solution is

$$
y(t)=\frac{\delta}{\lambda}(e^{\lambda t}-1).
$$

When $0<\delta<1$, at $t=\lambda^{-1}\log(1/\delta)$ this equals $(1-\delta)/\lambda$. The residual tends to zero while the observation interval grows, and the error does not tend to zero.

For $y'=-\gamma y+\delta$, with $\gamma>0$, the same trial has the same residual, yet

$$
y(t)=\frac{\delta}{\gamma}(1-e^{-\gamma t})
\le\frac{\delta}{\gamma}
$$

for every $t\ge0$. Accuracy of the differential relation acquires its meaning through the dynamics that propagate it.

## 3. Relative energy for a nonlinear fluid

Work with smooth periodic fields on the same box and interval. Let $u,p$ solve Navier–Stokes with force $f$, and let the divergence-free approximation $U,P$ have residual $r=\mathcal R[U,P;f]$. Set $e=u-U$ and $\pi=p-P$. Exact subtraction gives

$$
\partial_te+(U\cdot\nabla)e+(e\cdot\nabla)U
 +(e\cdot\nabla)e+\nabla\pi-\nu\Delta e=-r.
$$

Use the unnormalized norm $\|e\|_2^2=\int|e|^2\,dx$. Multiply by $e$ and integrate. Periodicity and zero divergence give

$$
\int e\cdot(U\cdot\nabla)e=0,\qquad
\int e\cdot(e\cdot\nabla)e=0,\qquad
\int e\cdot\nabla\pi=0.
$$

The pressure has disappeared from this particular scalar pairing; it has not disappeared from the field equation. Diffusion gives $+\nu\|\nabla e\|_2^2$ on the left. Therefore

$$
\frac12\frac d{dt}\|e\|_2^2+\nu\|\nabla e\|_2^2
\le\|\nabla U\|_\infty\|e\|_2^2+\|r\|_2\|e\|_2.
$$

The matrix norm in $\|\nabla U\|_\infty$ can be taken to be the operator norm; the Frobenius norm supplies a sufficient upper bound. Writing $I(t)=\int_0^t\|\nabla U(s)\|_\infty\,ds$, one obtains

$$
\boxed{\quad
\|e(t)\|_2\le e^{I(t)}\|e(0)\|_2
 +\int_0^t e^{I(t)-I(s)}\|r(s)\|_2\,ds.
\quad}
$$

At a zero of $\|e\|_2$, one can justify the division implicit in this step by first using $(\|e\|_2^2+\varepsilon^2)^{1/2}$, then letting $\varepsilon$ decrease to zero.

For matching initial data, an approximation with $\int_0^T\|r\|_2\le h^3$ and $I(T)\le\frac12\log(1/h)$ gives $\|e(T)\|_2\le h^{5/2}$. If $\|U(T)\|_2=h^2$, the actual norm is at least $h^2-h^{5/2}>0$ for $0<h<1$. The prediction has a certified error margin in the norm actually compared.

This is a conditional comparison on a smooth common interval. To prove that the actual solution reaches its endpoint, a PDE argument must also supply continuation bounds. To compare strain, an $L^2$ error is insufficient: strain contains a derivative. The extra high-regularity and interpolation estimates in [viscous amplification](viscous.md) serve exactly this purpose.

## 4. An exact forced solution asks a different question

Suppose instead that we choose $U,P$ first and define

$$
f_{\mathrm{req}}=\partial_tU+(U\cdot\nabla)U+\nabla P-\nu\Delta U.
$$

Then the forced momentum equation holds identically wherever these expressions exist. This is an elementary and useful construction. It becomes a theorem in a specified class only after checking the divergence constraint, data, energy and spatial conditions, and the required regularity of $f_{\mathrm{req}}$.

In particular, smoothness for every $t<T$ does not imply smoothness through $T$. Nor does a force becoming small in amplitude imply that its derivatives stay bounded. The scalar function

$$
g(t)=(T-t)\sin\!\left(\frac1{T-t}\right)
$$

tends to zero, but

$$
g'(t)=-\sin\!\left(\frac1{T-t}\right)
 +\frac1{T-t}\cos\!\left(\frac1{T-t}\right)
$$

has no bounded terminal limit. Taking $f(t,x)=g(t)\sin x$ does not repair this time-derivative failure.

**Worked cancellation with a singular state.** In the scalar nonlinear equation $y'=y^2+f$, set $s=T-t$, $y_*(t)=s^{-1}$. Then $y_*'=y_*^2$: the two singular terms cancel exactly. If we perturb the proposed state to $v=s^{-1}+\phi(t)$, its required force is

$$
f_{\mathrm{req}}=\phi'-2s^{-1}\phi-\phi^2.
$$

Thus a smooth, rapidly vanishing $\phi$ can leave a smooth force despite a singular state. The cancellation is explicit and specific to this scalar equation. It is neither a fluid construction nor a justification for omitting viscosity or pressure from one.

## 5. Flatness controls every derivative

Define

$$
\phi(t)=
\begin{cases}
\exp[-1/(T-t)^2],&t<T,\\
0,&t\ge T.
\end{cases}
$$

The claim is stronger than $\phi(t)\to0$: every derivative exists and equals zero at $T$. Such a smooth function is called **flat at $T$**.

Put $z=(T-t)^{-1}$. Since $dz/dt=z^2$, repeated differentiation gives

$$
\phi^{(m)}(t)=P_m(z)e^{-z^2},\qquad
P_0=1,\qquad P_{m+1}=z^2(P_m'-2zP_m).
$$

Each $P_m$ is a polynomial. The first two computations are

$$
\phi'=-2z^3e^{-z^2},\qquad
\phi''=(4z^6-6z^4)e^{-z^2}.
$$

For every fixed $q$, $z^qe^{-z^2}\to0$ as $z\to\infty$. Consequently every left derivative tends to zero, even after division by any fixed power of $T-t$. Difference quotients at $T$, followed by induction on derivative order, show that extension by zero is $C^\infty$. This also proves that $\phi'-2s^{-1}\phi-\phi^2$ in the scalar example has a smooth zero extension.

The phrase “every fixed order” matters. The constants can depend on the derivative order. Nothing here asserts one bound controlling all orders simultaneously.

For a force, space derivatives matter as well. If $\psi$ is a fixed smooth compactly supported function and $\beta>0$, consider

$$
f(t,x)=\phi(t)\psi\!\left(\frac{x}{(T-t)^\beta}\right).
$$

A spatial derivative costs a factor $(T-t)^{-\beta}$. A time derivative of the rescaled argument costs a factor $(T-t)^{-1}$ times that argument, which is bounded on the support of $\psi$ and its derivatives. The product rule therefore bounds each fixed mixed derivative by $\phi(t)$ times a fixed negative power of $T-t$. Every such derivative tends uniformly to zero. Shrinking support at this algebraic rate is compatible with smooth terminal extension.

That conclusion depends on the rate. For $f(t,x)=\phi(t)\psi(x/\phi(t)^2)$, a first spatial derivative has size

$$
\|\partial_xf(t)\|_\infty
=\phi(t)^{-1}\|\psi'\|_\infty.
$$

It diverges when $\psi'$ is not zero. Even a flat amplitude does not automatically pay for arbitrarily rapid concentration. This is why the physical derivative conversions from [scaling](scaling.md) belong in a force estimate.

## 6. Zero mean waves can generate a nonzero mean

For a decomposition $U=q+w$, the nonlinear term expands exactly as

$$
(U\cdot\nabla)U
=(q\cdot\nabla)q+(q\cdot\nabla)w
 +(w\cdot\nabla)q+(w\cdot\nabla)w.
$$

Solving an equation for $w$ to first order does not remove the last term. When $w$ oscillates, its quadratic product can contain a slowly varying part. An average of a product is not generally the product of the averages.

Here is an exact periodic calculation. Let $k$ be a positive integer and put

$$
w(x,y,z)=
\bigl(0,\sin(2z)\cos(kx),\sin y\cos(kx)\bigr).
$$

The field is divergence-free: its second component is independent of $y$, and its third is independent of $z$. Its average over $x$ is zero. Yet

$$
(w\cdot\nabla)w
=\bigl(0,2\sin y\cos(2z),\cos y\sin(2z)\bigr)\cos^2(kx).
$$

Since the average of $\cos^2(kx)$ is $1/2$, the mean nonlinear term is

$$
F=\bigl(0,\sin y\cos(2z),\tfrac12\cos y\sin(2z)\bigr).
$$

It is also $\nabla\cdot\overline{w\otimes w}$, where the tensor has entries $w_iw_j$ and the bar denotes this $x$-average. This averaged tensor is often called a **Reynolds stress**; no probabilistic averaging is required here.

Pressure must still be included. On the periodic box,

$$
\mathbb PF=F-\nabla\Delta^{-1}(\nabla\cdot F).
$$

Here $\nabla\cdot F=2\cos y\cos(2z)$ and
$\Delta^{-1}(\nabla\cdot F)=-(2/5)\cos y\cos(2z)$. Consequently

$$
\boxed{\quad
\mathbb PF=
\bigl(0,\tfrac35\sin y\cos(2z),
              -\tfrac3{10}\cos y\sin(2z)\bigr)\ne0.
\quad}
$$

Checking its divergence gives zero. Averaging over $x$ commutes with spatial derivatives and the periodic Fourier projector $\mathbb P$. For the actual smooth unforced solution starting from $w$, the initial derivative of its $x$-mean is therefore $-\mathbb PF$; the mean of the viscous term is zero initially. Thus this is a genuine initial source for a mean velocity. It is not yet a proof of its later amplitude, persistence, or usefulness as another amplifier.

## 7. A cutoff changes the equation

Cutoffs are mathematical operations with derivative costs. For a time-dependent scalar cutoff $\chi(t)$, take $v=\chi U$ and $p=\chi P$, where $U,P$ solve the equation with force $f$. Direct expansion gives the complete required force

$$
f_v=\chi f+\chi'U+(\chi^2-\chi)(U\cdot\nabla)U.
$$

The ramp term $\chi'U$ and the change in the nonlinear term are present even if $f=0$. If the transition lasts $\Delta t$, its derivatives typically cost powers of $1/\Delta t$. Smoothness of each individual cutoff does not give uniform bounds for an infinite sequence of shorter transitions.

Spatial cutoffs require more care. Multiplying a divergence-free field by $\chi(x)$ gives
$\nabla\cdot(\chi U)=\nabla\chi\cdot U$, generally nonzero. If a smooth vector potential $A$ with $\nabla\times A=U$ is available on a region, choose $\chi$ supported inside that region. The corrected localization

$$
v=\nabla\times(\chi A)=\chi U+\nabla\chi\times A
$$

is exactly divergence-free. The correction is part of $v$, so all of its time derivatives, diffusion and nonlinear cross terms belong in the force.

Even before this correction, product rules expose the cutoff costs. Write $\mathcal N(U,P)=\mathcal R[U,P;0]$. For a general $\chi(t,x)$,

$$
\begin{aligned}
\mathcal N(\chi U,\chi P)
={}&\chi\mathcal N(U,P)+\chi_tU
 +(\chi^2-\chi)(U\cdot\nabla)U\\
&+\chi(U\cdot\nabla\chi)U+P\nabla\chi\\
&-\nu\left[2\sum_j(\partial_j\chi)\partial_jU
                       +(\Delta\chi)U\right].
\end{aligned}
$$

For $c=\nabla\chi\times A$, the force of the solenoidal field $v=\chi U+c$, with pressure $\chi P$, additionally contains

$$
\partial_tc+(\chi U\cdot\nabla)c
 +(c\cdot\nabla)(\chi U)+(c\cdot\nabla)c-\nu\Delta c.
$$

These formulas follow from ordinary calculus. They explain why checking only the interior equation does not check the full localized construction.

There is a simpler use of a cutoff that should be distinguished from changing a velocity. Once a required force has a smooth extension through $T$, multiply that **force** by a smooth time cutoff equal to one through a neighborhood of $T$ and zero sufficiently later. This preserves the preterminal equation and gives compact time support. It does not require the singular velocity itself to extend through $T$. On a periodic spatial domain, the resulting smooth force has the required bounded mixed derivatives and rapid later-time decay; on all of space, the spatial decay conditions remain a separate requirement.

## Exercises

### 1. Check both the sign and the datum

For $y'=y$, $y(0)=1$, take $v=1+t$. Recover $e=e^t-1-t$ using variation of constants and the residual $r=-t$. Then take $v=2e^t$. What does its zero residual fail to establish?

### 2. A direction that amplifies errors

Let $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $e(0)=0$, and $e'=Ae-r$ with $r=(0,\delta)$, $\delta>0$. Compute $e(t)$. Does $\|r\|=\delta$ imply $\|e(t)\|\le\delta t$?

### 3. Price a predicted signal

Suppose matching initial data, $\int_0^T\|r\|_2\le h^3$, and $I(T)\le\alpha\log(1/h)$, with fixed $\alpha\ge0$. A model predicts a signal of size $h^2$ in an $L^2$ observable whose error is at most $\|e(T)\|_2$. For which $\alpha$ does the estimate certify a positive signal for small $h$? Explain the case $\alpha=1$.

### 4. Pay for mixed derivatives

Let $s=T-t$, $\phi=e^{-1/s^2}$, and $\psi\in C_c^\infty(\mathbb R)$. For $0<s\le1$, prove that

$$
\left\|\partial_t^m\partial_x^r
       [\phi(t)\psi(x/s^2)]\right\|_\infty
\le C_{r,m}s^{-2r-3m}e^{-1/s^2}.
$$

Deduce a smooth zero extension through $T$. Compare it with $s^3$ extended by zero for $t\ge T$.

### 5. Decide whether pressure removes the mean

Replace $\sin(2z)$ in the worked mean-stress example by $\sin(mz)$, with positive integer $m$. Compute $F_m$ and $\mathbb PF_m$. What happens at $m=1$, and what does that teach about inferring velocity from a nonzero stress divergence?

### 6. Compute a complete finite ramp

The unforced shear
$U(t,x,y,z)=a_0e^{-\nu n^2t}\sin(ny)e_1$, $P=0$, is exact. Let $\chi$ be a smooth time cutoff. Compute the force for $v=\chi U$, verify zero divergence, and give its spatial derivative of order $r$ in the $y$ direction. If $\chi(t)=\chi_0(t/\Delta)$, identify the contribution of differentiating the cutoff once more in time.

<details markdown="1">
<summary>Solutions</summary>

**1.** The error equation is $e'=e+t$, $e(0)=0$. Hence
$$
e(t)=\int_0^t e^{t-s}s\,ds=e^t-1-t.
$$
The sign is positive because the residual enters with a minus sign. For $v=2e^t$, the residual vanishes, but $v(0)=2$. It solves a different initial-value problem. Its discrepancy from the specified solution is $e^t$.

**2.** Since $A^2=0$, $\Phi(t,s)=I+(t-s)A$. Thus
$$
e(t)=-\int_0^t(\delta(t-s),\delta)\,ds
=(-\delta t^2/2,-\delta t).
$$
Its length is $\delta t\sqrt{1+t^2/4}$, which exceeds $\delta t$ for $t>0$. The residual enters one coordinate and is then transferred into the other. The zero eigenvalues of $A$ do not give a norm-preserving propagator.

**3.** Relative energy gives $\|e(T)\|_2\le h^{3-\alpha}$. The certified output is at least $h^2-h^{3-\alpha}$, which is positive for $0<h<1$ when $\alpha<1$. At $\alpha=1$, the lower bound is zero; constants or sharper information would be needed. For $\alpha>1$, this estimate also fails to certify the signal. Failure of an error bound does not prove that the actual signal vanishes.

**4.** After $r$ spatial derivatives the expression is $s^{-2r}\phi\,\psi^{(r)}(x/s^2)$. Each time derivative differentiates the power of $s$, the flat factor, or the rescaled argument. These cost at most $s^{-1}$, $s^{-3}$, and $s^{-1}$, respectively, with bounded functions of $x/s^2$ on the compact support. Induction and $s\le1$ give the displayed bound, with constants depending on the fixed derivative orders and finitely many derivatives of $\psi$. Every bound tends to zero faster than each power of $s$, proving the smooth extension, including at $x=0$. By contrast, the zero extension of $s^3$ is $C^2$, while its third left derivative is $-6$ and its third right derivative is zero.

**5.** Direct averaging gives
$$
F_m=\bigl(0,\tfrac m2\sin y\cos(mz),
                  \tfrac12\cos y\sin(mz)\bigr),
\qquad \nabla\cdot F_m=m\cos y\cos(mz).
$$
Its inverse Laplacian is $-m\cos y\cos(mz)/(1+m^2)$, so
$$
\mathbb PF_m=
\left(0,\frac{m(m^2-1)}{2(1+m^2)}\sin y\cos(mz),
       \frac{1-m^2}{2(1+m^2)}\cos y\sin(mz)\right).
$$
At $m=1$ it vanishes: $F_1$ is a pure gradient. At $m=2$ it gives the nonzero worked example. The pressure projection decides which part can change a divergence-free velocity; a nonzero unprojected source alone does not.

**6.** The shear's self-advection is zero, so
$$
f_v=\chi'(t)a_0e^{-\nu n^2t}\sin(ny)e_1.
$$
Both $U$ and $v$ have only a first component independent of $x$, hence zero divergence. Differentiating $r$ times in $y$ gives
$$
\partial_y^rf_v
=\chi'a_0e^{-\nu n^2t}n^r\sin(ny+r\pi/2)e_1.
$$
One additional time derivative includes
$$
a_0e^{-\nu n^2t}[\chi''-\nu n^2\chi']\,
 n^r\sin(ny+r\pi/2)e_1.
$$
For $\chi(t)=\chi_0(t/\Delta)$, the cutoff contributions scale as $\Delta^{-1}$ and $\Delta^{-2}$. A finite smooth ramp is admissible on a finite interval, but this calculation alone gives no uniform derivative control for ramps with $\Delta\to0$.

</details>

## What to carry into the next calculation

Residual equations, variation of constants, relative energy, smooth flat functions, Reynolds stresses, and cutoff commutators are classical mathematics. Transformatics organizes their use when a construction moves between descriptions: an ODE, a wave profile, a localized field, an exact evolution, and a physical-scale statement.

Specify the equation and constraints; compute the full residual; identify the
propagation estimate or force class required by the target; carry every
correction through the same calculation; and check the resulting statement
at the intended time and scale. These questions also guide the reading of
the separately authored [published result](published-proof.md).
