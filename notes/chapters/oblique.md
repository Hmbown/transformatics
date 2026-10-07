# Pressure and returning covectors

Consider the steady Euler shear $V=(\sin y,0,0)$ and a short wave whose velocity points in the $y$-direction while oscillating in the $x$-direction, $e_2\cos(Nx)$. Initially the wave is divergence-free: its velocity lies along its wavefronts. As the shear tilts those fronts, which way must the velocity amplitude turn to remain divergence-free?

Answering requires two evolving objects: a normal to the wavefronts and a velocity vector tangent to them. The chain rule determines the first; pressure helps determine the second. We will derive their equations, check the shear example, and then ask when growth around a closed fluid path can repeat. The pressure projection from [the fluid chapter](equation.md) and matrix calculations from [composition](composition.md) are the main prerequisites.

## Follow the phase and the amplitude separately

Write a rapidly oscillating disturbance schematically as

$$
w(t,x)\approx\operatorname{Re}\{b(t,x)e^{iS(t,x)/\delta}\},
\qquad 0<\delta\ll1.
$$

Here $S$ is the **phase**, whose level surfaces mark equal stages of the oscillation. Its gradient $\xi=\nabla S$ points normal to those surfaces. It is called a *covector* because it measures the phase change caused by a displacement: a small displacement $r$ changes the phase by approximately $\xi\cdot r$. The local wavelength in that normal direction is $2\pi\delta/|\xi|$. The vector $b$ gives the velocity amplitude and its direction, called the **polarization**.

The largest term in the divergence of the complex wave is

$$
\nabla\cdot(be^{iS/\delta})
=\left(\nabla\cdot b+\frac{i}{\delta}\xi\cdot b\right)e^{iS/\delta}.
$$

The term with $1/\delta$ is the largest as the wavelength decreases. Its cancellation requires $\xi\cdot b=0$: the leading velocity amplitude lies tangent to a phase surface. The slower term $\nabla\cdot b$ remains when the amplitude varies in space. The localized packet in [the next chapter](viscous.md) will correct that term as well.

## The full principal system

Transport the phase with the background velocity $V$, so $\partial_tS+V\cdot\nabla S=0$. Along a particle path $X'=V(X)$, put $A=\nabla V(X)$, with $A_{ij}=\partial_jV_i$. Differentiating the phase equation gives $\xi'=-A^T\xi$. A changing velocity gradient therefore changes the wave normal.

The inviscid leading-order amplitude equation has the form $b'=-Ab+\alpha\xi$, where the last term comes from pressure. To find its coefficient, preserve the constraint:

$$
\frac{d}{dt}(\xi\cdot b)
=(-A^T\xi)\cdot b+\xi\cdot(-Ab+\alpha\xi)
=-2\xi\cdot Ab+\alpha|\xi|^2.
$$

For $\xi\ne0$, this is zero precisely when $\alpha=2(\xi\cdot Ab)/|\xi|^2$. The complete principal system is therefore

$$
X'=V(X),\quad\xi'=-A^T\xi,\quad
b'=-Ab+2\xi\frac{\xi\cdot Ab}{|\xi|^2},\quad\xi\cdot b=0.
$$

There are two equal contributions to the factor two: the amplitude moves, and the normal defining its transverse plane moves too. These ODEs describe the leading inviscid wave. Constructing an actual localized NS perturbation will additionally require divergence corrections, viscous damping and control of the nonlinear error.

Apply this principal system to the opening shear at the origin. Its gradient, a unit wave normal, and a unit transverse amplitude are

$$
A=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},
\qquad \xi=e_1,\quad b=e_2.
$$

Before evaluating the amplitude equation, the constraint already predicts the sign: since $\xi'=-e_2$, we need $e_1\cdot b'=1$ to preserve $\xi\cdot b=0$. Indeed, $Ab=e_1$ and the pressure-corrected equation gives $b'=e_1$, so the two contributions to the constraint derivative are $-1+1=0$. Omitting pressure would instead give $b'=-e_1$ and derivative $-2$. Pressure changes the answer even at the first instant.

## What returns after one circuit?

Imagine neighboring circular tracks traversed at slightly different angular speeds. One particle may complete a lap while a short line joining it to a neighbor becomes tilted. Returning to the same point therefore need not restore the deformation of a small wave.

To calculate this, use coordinates in which $\theta$ records angles around an orbit and $I$ labels the orbit. The equations $\theta'=\Omega(I)$, $I'=0$ keep the label fixed and advance the angles at a label-dependent rate. Such coordinates are called **action–angle coordinates**; their construction for Gavrilov's flow comes from [Pietro Baldi's analysis of its particle dynamics](https://arxiv.org/abs/2302.02982). At a fixed time $T$, the position map is $(\theta,I)\mapsto(\theta+T\Omega(I),I)$. Its derivative contains the difference between neighboring angular speeds:

$$
D\Phi_T=\begin{pmatrix}\mathrm{Id}&T\Omega'(I)\\0&1\end{pmatrix}.
$$

A displacement $r$ becomes $D\Phi_T r$. Transport preserves its phase change, so $\xi_T\cdot D\Phi_T r=\xi_0\cdot r$ for every $r$. Hence $(D\Phi_T)^T\xi_T=\xi_0$: the phase gradient transforms by the **inverse transpose**. Thus, even when the chosen particle has returned, its coordinate covector is sent to

$$
(\zeta_\theta,\zeta_I)\mapsto
(\zeta_\theta,\zeta_I-T\Omega'(I)\cdot\zeta_\theta).
$$

Here $\zeta_\theta$ and $\zeta_I$ are the angular and orbit-label components of that covector. Return requires $\Omega'(I)\cdot\zeta_\theta=0$. For example, in the one-angle model $\Omega(I)=I$, the particle at $I=1$ returns after $T=2\pi$, but $(\zeta_\theta,\zeta_I)=(1,0)$ becomes $(1,-2\pi)$. The particle returns; the phase normal does not.

A **return map** sends an initial transverse amplitude to its amplitude after one circuit, with the particle, covector and coordinate frame identified consistently. An eigenvalue of this map is a **Floquet multiplier**. If the multiplier has magnitude greater than one, repetition multiplies the corresponding eigenvector's amplitude by that factor each time. The return conditions are what make it the same map on each circuit.

A natural first choice is a wave normal parallel to the background pressure gradient, $\xi=\nabla P(X)$. On the regular periodic orbit specified in the source, $b=V(X)$ is a nonzero periodic amplitude. One multiplier is therefore one. The determinant of the two-dimensional transverse return map is also one, forcing the other multiplier to be one as well. This choice provides no expanding Floquet eigenvalue. It can still have transient or Jordan growth, and the calculation leaves other wave normals available.

## An unstable oblique carrier on actual compact flows

The [oblique theorem](../../references/navier-stokes/gavrilov-oblique.md) selects a family of compact Gavrilov Euler fields. The flow lies near a circular tube: *poloidal* motion goes around its small cross-section, while *axial* rotation goes around the symmetry axis. In its coordinates, $K(I)$ is the original pressure on the orbit, and $q(I)$ is the ratio of its axial and poloidal angular speeds. Here $q$ is a scalar function, unrelated to the velocity field named $q$ in later source notes. Choose the small action level $I_j$ by $q(I_j)=1/j$, let $P_j=K(I_j)$, and localize the original field with a smooth pressure cutoff whose value and slope at that level are

$$
f_j(P_j)=1,\qquad f_j'(P_j)=-1/P_j.
$$

The source specifies the entire cutoff and the exact covector. That covector satisfies the return condition, while its components in a moving orthonormal frame converge to $(0,-1/\sqrt2,2)$. The full gradient, frame rotation, and pressure correction give a two-dimensional limiting amplitude equation

$$
Y'=B_0Y,\qquad B_0=\begin{pmatrix}0&-8/9\\-1/2&0\end{pmatrix},
\qquad B_0^2=\frac49I.
$$

Here $Y$ contains two transverse-amplitude coordinates; it is not the particle position $X$. The vectors $(4,-3)^T$ and $(4,3)^T$ have eigenvalues $2/3$ and $-2/3$, respectively. The first gives the model solution $Y(s)=e^{2s/3}(4,-3)^T$. Over one limiting poloidal circuit, whose parameter length is $2\pi$, its amplitude multiplies by $e^{4\pi/3}$.

The limiting calculation tells us what to prove for a fixed compact field: its coefficient matrix must remain close enough to $B_0$ throughout the circuit that the expanding direction survives. Uniform control over the whole circuit, rather than agreement at one point, is the role of the analytic coordinate estimates.

## Why growth survives the closed orbit

One poloidal circuit rotates the particle and frame axially by $2\pi/j$. Axisymmetry makes the relative amplitude equation exactly periodic on that circuit. After $j$ circuits the physical particle, frame, and covector all return, so the full return map is exactly the $j$th power of the relative map.

For every sufficiently large $j$, the actual relative map has a positive expanding multiplier. Its two multipliers tend to $e^{\pm4\pi/3}$. The source also proves an explicit robustness bound: once the transformed matrix error is at most $1/12$ entrywise, the expanding relative multiplier is at least $e^{13\pi/12}$. The expanding multiplier on the full closed orbit is its $j$th power.

The written theorem proves this statement for every sufficiently large member of the specified family; its threshold is existential rather than a computed integer. Its conclusion concerns the inviscid principal ODE on actual compact Euler fields. The [registered claim](../claims.md#nse-gavrilov-oblique-instability) records that scope.

## Fix the profile before taking another limit

First fix one sufficiently large $j$, including its entire cutoff and chosen normalization. The supplied-wave construction retains $f_j(P_j)=1$. Only then concentrate that fixed profile using the parameter $L$ from [the steady-background chapter](steady.md). The cutoff derivatives grow as $j$ increases; the earlier NS comparison does not justify sending $j$ and $L$ to infinity together.

With that order of choices fixed, the [next chapter](viscous.md) constructs a localized finite-wavelength viscous realization and controls its nonlinear error at a restricted small-seed amplitude. Passing from a finite amplification theorem to an indefinitely repeatable evolution requires the additional hypotheses developed in [iteration](iteration.md).

## Which part has been formalized?

The matrix argument is small enough to inspect separately. The [Lean certificate](../../formalization/oblique_cone/NSEObliqueCone428.lean) checks the invertible change of basis, matrix conjugacy, inward cone margins $23/48$, and conditional expansion coefficient $13/24$. Its [verification receipt](../../formalization/oblique_cone/receipt.json) records compilation and bundled declaration replay. The uniform actual-flow comparison, ODE invariance and return-map proof are written analytic arguments. This division illustrates the distinction between a checked algebraic step and a formalized theorem discussed in [practice](practice.md).

## Exercises

### 1. Recover the pressure coefficient

Replace the factor 2 by $c$. Differentiate $\xi\cdot b$ and determine which $c$ preserves transversality for arbitrary admissible initial $b$.

<details markdown="1"><summary>Solution</summary>

The derivative is $-\xi\cdot Ab-\xi\cdot Ab+c\xi\cdot Ab=(c-2)\xi\cdot Ab$. The universal preservation condition is $c=2$. Special cases with $\xi\cdot Ab=0$ do not justify another coefficient in the general equation.

</details>

Source: [the steady-background note, §§5–6](../../references/navier-stokes/steady-background.md).

### 2. Separate orbit return from covector return

In the one-angle model $\Omega(I)=I$, work on the orbit $I=1$. Which nonzero coordinate covectors return after $2\pi$? What changes if $\Omega(I)=1$ for every orbit?

<details markdown="1"><summary>Solution</summary>

For $\Omega(I)=I$, return requires $\zeta_\theta=0$, so exactly the nonzero covectors $(0,\zeta_I)$ return. For the constant angular speed, $\Omega'=0$, and every covector returns. The difference is shear between neighboring orbits, not the period of the selected particle.

</details>

### 3. Read the limiting matrix

Find the eigenvalues of $B_0$ and write the solution starting at $Y(0)=(4,0)^T$ as a sum of its two eigenvector solutions. Explain why these explicit formulas alone do not prove the theorem for an actual compact flow.

<details markdown="1"><summary>Solution</summary>

The characteristic polynomial is $\lambda^2-4/9$, so the eigenvalues are $2/3$ and $-2/3$. Since $(4,0)^T=\tfrac12(4,-3)^T+\tfrac12(4,3)^T$,

$$
Y(s)=\tfrac12e^{2s/3}(4,-3)^T
    +\tfrac12e^{-2s/3}(4,3)^T.
$$

A limiting model needs a uniform comparison with the actual coefficients, including moving coordinates and pressure. The source supplies this comparison on one circuit and an exact rotational return to obtain the full closed-orbit map. A generic initial vector can contain both eigenvector directions; a growing eigenvalue does not say that every nonzero initial vector grows.

</details>

## Further reading

Susan Friedlander and Misha Vishik's [*Instability criteria for the flow of an inviscid incompressible fluid*](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.66.2204) develops geometric criteria for growth of perturbations of steady Euler flows. It places the use of particle trajectories and local deformation in the wider study of hydrodynamic instability.

Pietro Baldi's [*Nearly toroidal, periodic and quasi-periodic motions of fluid particles driven by the Gavrilov solutions of the Euler equations*](https://arxiv.org/abs/2302.02982) studies the particle dynamics of the compact fields used here. Read it for the geometric input behind the action–angle description. The particular cutoff, returning oblique covector and quantitative expanding multiplier are developed in the project's [oblique-carrier proof](../../references/navier-stokes/gavrilov-oblique.md).
