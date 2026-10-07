# From a transfer calculation to a published proof

A finite transfer calculation can explain how a wave gains energy, how a new frequency appears, or why a proposed approximation fails. A singularity theorem has a different obligation: construct **one evolution** and verify the equation all the way to its terminal time. This chapter teaches how to read that passage without mistaking an intermediate calculation for the completed argument.

Read [scaling](scaling.md), [concentration](concentration.md), and [the fluid equation](equation.md) first. You will use changes of variables, integration by parts, divergence, curl, and the distinction between a field and a solution. By the end, you should be able to check a concentration budget, compute a complete stress-cancellation residual, and identify the additional hypotheses needed for an infinite construction.

## 1. State the external theorem before interpreting it

OpenAI's *Finite time blowup for Navier–Stokes*, released on 8 September 2026, states the following in Theorem 1.1. For every fixed $\nu>0$, there exist

$$
f\in C_c^\infty(\mathbb R^3\times(0,\infty);\mathbb R^3),
\qquad u(\cdot,0)=0,
$$

and a smooth solution on $[0,1)$ of

$$
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad \nabla\cdot u=0,
$$

with $u,p$ supported in one fixed compact spatial set and

$$
\sup_{t<1}\|u(t)\|_2<\infty,
\qquad \limsup_{t\uparrow1}\|u(t)\|_\infty=\infty.
$$

The force is smooth **through** time one. Corollary 10.6 supplies the corresponding unit-periodic result, including periodic pressure. [Paper, Theorem 1.1 and Corollary 10.6](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

These are the forced alternatives C and D of the official problem. Alternatives A and B explicitly set $f=0$. An existence statement about a specially constructed force does not decide what happens without that force. [Fefferman's problem statement, pp. 1–2 and pressure erratum](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).

The separate **unforced problem** asks whether smooth initial velocity and
fixed positive viscosity always give a globally smooth evolution when
$f=0$. This project's preserved force-removal studies examined whether the
released construction could help answer it. That research is currently
paused, and the unforced question remains open here.

A [finite nonlinear comparison](../../references/analysis/nonlinear-force-comparison.md) follows an unforced solution from the reference velocity at a late initial time, with a small velocity error over a specified interval. A subsequent [correction argument](../../references/analysis/nonlinear-endpoint-correction.md) adjusts that initial velocity so that a whole specified family of endpoint error measurements vanishes. It retains the full nonlinear equation and pressure. These are restricted written arguments with independent AI reviews.

The distinction between a finite correction and a singularity proof is a distinction between quantifiers. For each late interval, the argument chooses a suitable initial velocity. A singularity proof needs **one initial velocity** whose evolution remains controlled through all the required intervals and becomes singular. The current corrections have not been shown to arise from one fixed earlier state, and the unmeasured part of the error still needs control. The [research record](../../references/navier-stokes/openai-result-bridge.md#why-removing-the-force-remains-a-separate-problem) gives the precise remaining conditions. The unforced problem remains open here.

The forced breakdown theorem is externally authored. Our earlier calculations help explain some of its mathematical operations; they do not logically imply the whole construction. The companion unforced Euler result is also separate: changing $\nu>0$ to $\nu=0$ changes the equation. [Official repository overview](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).

## 2. Worked example: growing speed with vanishing energy

The question “does the energy stay finite?” requires both amplitude and occupied volume. We can isolate this issue with an exact divergence-free **kinematic family**. It will not be an asserted solution of Navier–Stokes.

Choose $\psi_0\in C_c^\infty(\mathbb R^3)$ so that

$$
V=(\partial_2\psi_0,-\partial_1\psi_0,0)
$$

is nonzero. Write $\tau=1-t$, and choose a fixed $0<\alpha<1/6$. Define

$$
\ell_r=\tau^{1/2},\qquad
\ell_z=\tau^{1/2-\alpha},\qquad
A=\tau^{-1/2-\alpha},
$$

$$
\psi_\tau(x)=A\ell_r\,
\psi_0\!\left(\frac{x_1}{\ell_r},
              \frac{x_2}{\ell_r},\frac{x_3}{\ell_z}\right),
\qquad
v_\tau=(\partial_2\psi_\tau,-\partial_1\psi_\tau,0).
$$

Mixed derivatives commute, so $\nabla\cdot v_\tau=0$. In particular, we have not assumed that an arbitrary anisotropic coordinate change preserves divergence. The chosen potential makes it true.

Set $y=(x_1/\ell_r,x_2/\ell_r,x_3/\ell_z)$. Then $v_\tau(x)=A V(y)$ and $dx=\ell_r^2\ell_z\,dy$. Consequently,

$$
\|v_\tau\|_\infty=A\|V\|_\infty\longrightarrow\infty,
$$

$$
E(\tau):=\frac12\int|v_\tau|^2dx
=\frac12\|V\|_2^2 A^2\ell_r^2\ell_z
=C_E\tau^{1/2-3\alpha}\longrightarrow0.
$$

Compute the dissipation integrand too. With
$C_r=\|\partial_1V\|_2^2+\|\partial_2V\|_2^2$ and
$C_z=\|\partial_3V\|_2^2$,

$$
\nu\|\nabla v_\tau\|_2^2
=\nu C_r\tau^{-1/2-3\alpha}
 +\nu C_z\tau^{-1/2-\alpha}.
$$

Both terms are integrable at $\tau=0$ when $\alpha<1/6$. For the concrete choice $\alpha=1/200$, the energy exponent is $97/200$, and the two dissipation exponents are $-103/200$ and $-101/200$. The peak grows while the total energy vanishes and the time integral of the dissipation remains finite.

This calculation establishes **compatibility of norms**. It has not checked momentum, pressure, or the force needed to maintain this path. In particular, its decreasing energy near $t=1$ cannot explain how a fluid initially at rest became nonzero. That requires an earlier evolution and its energy input.

The published core uses this pattern of anisotropic exponents, with its own fixed small parameter and an actual profile construction. [Paper, §2.1](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf). Our $\alpha=1/200$ is an illustrative choice, not an identification of their selected profile parameter.

## 3. Worked example: canceling a stress does not cancel the equation

For a specified velocity and pressure, define the **momentum residual**

$$
\mathcal R_\nu(u,p)
=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p.
$$

A forced solution requires $\mathcal R_\nu(u,p)=f$. Expanding a sum gives the exact identity

$$
\begin{aligned}
\mathcal R_\nu(U+w,P+\pi)
={}&\mathcal R_\nu(U,P)
 +\partial_tw-\nu\Delta w+\nabla\pi\\
 &+(U\cdot\nabla)w+(w\cdot\nabla)U
 +(w\cdot\nabla)w.
\end{aligned}
$$

For divergence-free $w$, the last term is $\nabla\cdot(w\otimes w)$, where $(w\otimes w)_{ij}=w_iw_j$ and $(\nabla\cdot T)_i=\sum_j\partial_jT_{ij}$. Its average is a momentum flux, often called a stress. This exact expansion is also the accounting rule in our [physical-force analysis](../../references/navier-stokes/forced-admissibility.md).

We can make the cancellation explicit. Work on the $2\pi$-periodic torus, use fixed $\nu>0$, and choose an integer $N\ge1$. All fields in this example are independent of time. Put

$$
U=V(x)e_3,\qquad V(x)=-\frac{\sin2x}{8\nu},
$$

$$
w_N=\left(\sin x\cos Ny,
          -\frac{\cos x\sin Ny}{N},
          \sin x\cos Ny\right).
$$

Both fields are divergence-free. Average over $y$, using
$\langle g\rangle_y=(2\pi)^{-1}\int_0^{2\pi}g\,dy$. The flux of the third component in the first direction is

$$
\langle(w_N)_1(w_N)_3\rangle_y=\frac12\sin^2x,
\qquad
\partial_x\langle(w_N)_1(w_N)_3\rangle_y=\frac12\sin2x.
$$

Meanwhile, $\mathcal R_\nu(U,0)=-\nu V''e_3=-(\sin2x/2)e_3$. Thus this averaged flux has exactly the desired sign and magnitude.

Now calculate everything, including pressure. Direct differentiation gives

$$
(w_N\cdot\nabla)w_N
=\left(\frac{\sin2x}{2},
        \frac{\sin2Ny}{2N},
        \frac{\sin2x}{2}\right).
$$

Choose the periodic pressure

$$
\pi_N=\frac{\cos2x}{4}+\frac{\cos2Ny}{4N^2}.
$$

Its gradient cancels the first two components. The remaining third component cancels the entire old residual. Nevertheless, since
$\Delta w_N=-(1+N^2)w_N$, the **complete** new residual is

$$
\boxed{
\mathcal R_\nu(U+w_N,\pi_N)
=\nu(1+N^2)w_N+V'(x)(w_N)_1e_3.
}
$$

The first term is the full ordinary viscosity cost. The second is an interaction with the old velocity. The mean-stress calculation omitted both.

This cost cannot be hidden by a different periodic pressure. Let
$w_H=((w_N)_1,(w_N)_2,0)$, and use normalized torus measure. Then $\nabla\cdot w_H=0$, so every periodic pressure gradient pairs to zero with $w_H$. The vertical interaction also pairs to zero. For any smooth periodic pressure $\widetilde\pi$, Cauchy–Schwarz therefore gives

$$
\begin{aligned}
\|\mathcal R_\nu(U+w_N,\widetilde\pi)\|_2
&\ge\nu(1+N^2)\|w_H\|_2\\
&=\frac{\nu(1+N^2)}2\sqrt{1+N^{-2}}.
\end{aligned}
$$

Increasing frequency makes this chosen stationary construction more expensive. It does not prove that every evolving or corrected construction has the same cost. This example is planar in its spatial dependence and is not a three-dimensional singularity model.

## 4. Read the proof as a sequence of obligations

The external proof builds a concentrating core, realizes its remaining annular stress with two wave families, corrects pressure and mean defects, and sums corrections before localizing. The resulting residual is flat at the singular space-time point to every derivative order. Away from that point its terminal values need not vanish; the final localized force is extended smoothly through time one. Smooth extension is the required property, while zero extension is a useful sufficient construction in our simpler examples. [Paper, §§3–10, especially Theorem 3.1, Proposition 9.9 and Lemma 10.2](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

Here is the mathematical connection to the earlier chapters and reviewed project notes. “Shared identity” means the same standard algebra applies; “parallel” means that the operations resemble each other but their hypotheses and outputs must be proved separately.

| Earlier material | Type of connection | What must still be supplied for a complete construction |
|---|---|---|
| [Physical residual accounting](../../references/navier-stokes/forced-admissibility.md) | Shared identity: expand the full increment, including old/new products. | Estimates for the actual fields, not just cancellation of their average. |
| [Localized phase profiles](../../references/navier-stokes/localized-profile.md) | Shared identities: taking curls preserves divergence; physical phase evaluation has chain-rule terms. | The chosen amplitudes, pressure and support corrections must satisfy their own estimates. |
| [Viscous finite amplification](viscous.md) | Parallel: deformation can amplify a wave while diffusion damps it. | Required momentum flux, compatible incoming amplitudes, and complete forcing costs. A gain factor alone supplies none of these. |
| [Finite-depth profile correction](../../references/analysis/finite-depth-profile.md) | Parallel: recompute the mean and oscillatory residual after each correction. | One summed field with control of every fixed derivative order; constants depending on a fixed depth do not automatically provide it. |
| [Force admissibility](../../references/navier-stokes/forced-admissibility.md) | Shared analytic requirement: all physical space-time derivatives must extend through the terminal time. | A single pressure/force choice and actual extension estimates, including transition regions. |
| [Fixed-annulus exclusion](../../references/analysis/fixed-annulus-obstruction.md) | Hypothesis check: that exclusion concerns the whole axisymmetric velocity uniformly away from its axis. | Verify the geometry of the whole candidate before applying it. A core approaching the axis is outside that hypothesis. |
| [Frequency activation](activation.md) and the [finite cycle analysis](../../references/analysis/cycle-next-transfer.md) | Observable check: frequency production, enstrophy growth and maximum-speed growth are different claims. | Prove the observable stated in the target theorem along the same solution. |

The public formalization has distinct modules for the assembled primary covariance, diagonal residual estimates, periodization, and derivative decay of compact-time forces. These divisions give useful reading targets: the covariance module retains the actual selected labels before averaging; the residual module distinguishes derivative order from approximation stage. [Primary covariance](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualPrimaryCovariance.lean), [diagonal residual](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalResidual.lean).

Why is the last passage stronger than “arbitrarily accurate finite approximations”? A bound such as

$$
|\partial^\gamma R_J|\le C_{J,\gamma}\tau^{b_J-L_\gamma},
\qquad b_J\longrightarrow\infty,
$$

still describes different residuals $R_J$. To conclude anything about one limiting residual $R$, one also needs a summation construction and estimates on $R-R_J$. The derivative loss $L_\gamma$, the stage constants, and the cutoff derivatives must all be accounted for. This quantifier distinction is explicit in the [external diagonal-residual module](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalResidual.lean).

Localization has a similar obligation. If $u=\nabla\times A$, multiplying $u$ by a cutoff $\chi$ generally destroys divergence. Instead,

$$
\nabla\times(\chi A)=\chi u+\nabla\chi\times A.
$$

The second term restores divergence but also contributes to momentum. Compact support of a potential does not make those new terms zero. After a compactly supported solution has been constructed inside a fundamental cube with a gap to its boundary, disjoint translated copies can be periodized without introducing nonlinear cross interactions. The [periodization module](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PeriodicLocalization.lean) treats the actual locally finite lattice sum. The [force-decay module](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CompactForceDecay.lean) then obtains all derivative decay bounds from global smoothness, spatial periodicity, and compact time support.

## 5. Exercises

### Exercise 1 — Find the energy-compatible range

In §2, determine the values of $\alpha>0$ for which the energy tends to zero and the radial dissipation is time-integrable. Explain the endpoint $\alpha=1/6$.

<details markdown="1">
<summary>Solution</summary>

Energy tends to zero exactly when $1/2-3\alpha>0$. Radial dissipation is integrable exactly when $-1/2-3\alpha>-1$. Both give $0<\alpha<1/6$. At $\alpha=1/6$, the energy is constant in this family and the radial dissipation behaves like $\tau^{-1}$; its integral diverges logarithmically. These norm conditions do not verify the momentum equation.

</details>

### Exercise 2 — Realize two flux components with positive amplitudes

On the normalized $2\pi$-torus, let

$$
b_1=(1,1,1),\quad k_1=(1,-1,0),\qquad
b_2=(1,-1,2),\quad k_2=(1,1,0),
$$

$$
w=\sqrt{2c_1}\,b_1\cos(k_1\cdot x)
 +\sqrt{2c_2}\,b_2\cos(k_2\cdot x).
$$

Show that $w$ is divergence-free. Find positive $c_1,c_2$ with
$(\langle w_1w_2\rangle,\langle w_1w_3\rangle)=(1,4)$. Show that the coefficients remain positive when both target components change by at most one. Does this solve a prescribed momentum equation?

<details markdown="1">
<summary>Solution</summary>

The dot products $b_i\cdot k_i$ vanish. Distinct Fourier frequencies have zero cross average and each cosine square averages to $1/2$. Thus the flux vector is

$$
c_1(1,1)+c_2(-1,2)=(c_1-c_2,c_1+2c_2).
$$

For a target $(T_1,T_2)$, solve
$c_1=(2T_1+T_2)/3$, $c_2=(T_2-T_1)/3$. At $(1,4)$, this gives $(2,1)$. If $T=(1+e_1,4+e_2)$ with $|e_i|\le1$, then $c_1\ge1$ and $c_2\ge1/3$. This is an explicit interior margin in the positive cone of the two flux directions.

It is only covariance algebra. The average is spatially constant, so its divergence is zero. Spatially varying targets require envelopes and divergence corrections; temporal evolution, viscosity, pressure and unaveraged products still have to be calculated. Positive squared amplitudes do not complete those tasks.

</details>

### Exercise 3 — Separate finite order from flatness

Extend both $g(\tau)=\tau^{10}$ and $h(\tau)=e^{-1/\tau^2}$, initially defined for $\tau>0$, by zero for $\tau\le0$. Which extension is smooth? Why would a small bound on a residual without derivative bounds be insufficient?

<details markdown="1">
<summary>Solution</summary>

The extension of $g$ is $C^9$, but its tenth derivative has one-sided limits $10!$ and zero. Every derivative of $h$ is a polynomial in $1/\tau$ times $e^{-1/\tau^2}$, so every derivative tends to zero faster than any prescribed positive power of $\tau$. Its extension is smooth and flat at zero.

A small function can have large derivatives: for instance, $\tau^{10}\sin(\tau^{-20})$ tends to zero while its first derivative is unbounded. Smooth terminal forcing therefore requires control of the actual differentiated residual, not just its size.

</details>

### Exercise 4 — Audit the quantifiers

Consider the statement: “For every $\nu>0$, some smooth force causes finite-time breakdown from zero initial velocity.” Does it imply breakdown for $f=0$, breakdown for every smooth force, or a singular numerical simulation from arbitrary data?

<details markdown="1">
<summary>Solution</summary>

None follows. The existentially chosen force can depend on $\nu$; replacing it by zero or an arbitrary force changes the assertion. Zero data with zero force give the zero smooth solution. The theorem also provides no error certificate for a particular numerical discretization. A simulation would require a specified instance and its own approximation analysis.

</details>

## 6. What has been checked here

The examples in this chapter are original teaching calculations. The divergence, complete nonlinear residual and pressure identities in §3 were also reproduced by exact symbolic algebra. They are not a numerical fluid simulation.

The external repository reports full main-result Lean formalizations with the usual listed axioms `propext`, `Classical.choice`, and `Quot.sound`; its metadata labels review as self-assessed. Its separate challenge file contains two intentional `sorry` placeholders, which specify the targets. The submitted solution imports a separate copy of the definitions and does not depend on those placeholders. A comment-aware inspection of its 580 project-local dependency modules found no proof-hole or axiom-declaration tokens. This is evidence about source text, not an axiom report from the compiled theorem. [Formalization metadata](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/formalization.yaml), [theorem entry points](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ComparatorSolution.lean).

The exported theorem types assert the forced alternatives C and D for every positive viscosity. They do not specify a breakdown time. The inspected adapter rescales a viscosity-one witness by $u_\nu(t,x)=\nu u_1(\nu t,x)$, giving terminal time $1/\nu$. Thus the paper's time-one normalization in §1 should not be read as a literal parameter of those formal declarations. Likewise, the bounded energy of the constructed preterminal velocity in §1 remains attributed here to the paper; the energy condition in the exported whole-space type is imposed on a hypothetical global competitor. The [statement audit](../../references/analysis/external-statement-audit.md) explains these distinctions.

The exact Navier–Stokes target subsequently built successfully here with the official Lean 4.34.0-rc2 toolchain and pinned dependencies. All 580 project-local modules in its import closure compiled from unchanged sources; Mathlib artifacts came from the matching cache. Both exported theorems printed only the three axioms listed above. The [verification record](../../formalization/external_ns/README.md) gives the commands, hashes and scope, including the separate imported-closure replay attempt.

The stronger bundled-kernel replay of the entire imported proof environment did not finish within its ten-minute limit and remains incomplete. The independent Comparator/Nanoda check has not been run here; its trusted checking environment requires Linux. The [provided instructions](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/README.md) specify that separate action. The successful local build covers these formal declarations, not every detail of the paper, the companion Euler library, or an external expert assessment.

For agents continuing the reading, the [source bridge record](../../references/navier-stokes/openai-result-bridge.md) pins the inspected release and the boundaries of this comparison.
