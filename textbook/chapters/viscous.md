# Finite viscous amplification

The exact shear in [the fluid equation](equation.md) loses amplitude at rate $\nu N^2$. The [oblique-wave calculation](oblique.md) instead finds a direction that a steady Euler flow amplifies. What happens when a short wave experiences both effects? And how accurately must we approximate the fluid to know that the predicted gain survives?

We will answer these questions for one finite packet construction. First solve a scalar model of growth and damping. Then construct a real, localized, divergence-free packet. Finally use explicitly stated estimates from the research proof to compare its predicted signal with the error in an actual nonlinear solution. The scalar and packet calculations are proved here; the cited PDE estimates are inputs, with their full proofs in the source.

The needed tools are integrating factors, the product rule for curl, Fourier orthogonality, and the scale conversions in [scaling](scaling.md). [Residuals](residuals.md) explains how an error in an equation produces an error in its solution. When the argument invokes a Sobolev norm or continuation theorem, we will state what it contributes instead of treating it as an unexplained algebraic step.

A **packet** is an oscillating velocity disturbance confined by a smooth envelope. Its **seed** is the initially supplied disturbance. A **handover** occurs when its strain becomes larger than the host's on the specified region or at the specified point. This chapter establishes the logic of finite velocity amplification. Strain handover and subsequent research extensions are developed separately in the optional [advanced-transfer companion](advanced-transfer.md).

## First compare gain, damping and error

For orientation, consider a scalar amplitude $a(t)$ satisfying the model ODE

$$
a'(t)=\bigl(\sigma(t)-\nu K(t)^2\bigr)a(t).
$$

Here $\sigma$ is an imposed amplification rate, $K$ is a spatial frequency, and $\nu K^2$ is the heat-damping rate. Define accumulated growth $G(t)=\int_0^t\sigma(s)\,ds$ and accumulated damping $D(t)=\nu\int_0^tK(s)^2\,ds$. Then

$$
a(t)=a(0)e^{G(t)-D(t)}.
$$

Growth wins in this model when $G>D$. Before choosing numbers, predict what happens when the frequency doubles while the growth rate stays fixed. For constant $\sigma=3$, $\nu=1$, and $K=1$, the gain after time one is $e^2$. At frequency $K=2$ it is $e^{-1}$: doubling the frequency quadruples the damping rate. The actual fluid polarization is a vector system coupled to phase and pressure, so this scalar calculation identifies the competing terms without replacing that system.

There is a third quantity. Suppose a constructed packet predicts an output norm $A_{\mathrm{pred}}$, while the actual solution differs from it by at most $E_{\mathrm{err}}$ in the **same norm**. The triangle inequality gives

$$
\|\text{actual output}\|\ge A_{\mathrm{pred}}-E_{\mathrm{err}}.
$$

The error must be smaller than the signal in the norm being measured. As in [residuals](residuals.md), a discrepancy in the equation must first be propagated before it bounds a discrepancy in the solution. For a scalar error bound $E'\le L(t)E+r(t)$, the integrating-factor estimate is

$$
E(t)\le e^{\int_0^tL(s)\,ds}E(0)
+\int_0^t e^{\int_s^tL(\tau)\,d\tau}r(s)\,ds.
$$

In the fluid estimates, velocity gradients contribute to $L$. An amplifier can magnify errors as well as its selected seed. This is why both the whole history of the gradients and the residual matter.

## Build a real divergence-free packet

Start with a plane wave in the $e_2$-direction, oscillating in the $x_1$-direction. It is divergence-free. To confine it to a small region, multiply by a smooth envelope $\chi_\delta(x)$. Predict the problem before calculating: the velocity now varies in its own direction wherever the envelope varies with $x_2$. Indeed,

$$
\nabla\cdot\left[\chi_\delta(x)\cos(2x_1/h)e_2\right]
=(\partial_2\chi_\delta)\cos(2x_1/h).
$$

Choose a real smooth function $\chi$, supported strictly inside the unit ball, with unnormalized $L^2$ norm one. Let

$$
\chi_\delta(x)=\delta^{-3/2}\chi(x/\delta),\qquad
\|\chi_\delta\|_2=1,\qquad
\|\nabla\chi_\delta\|_2=\delta^{-1}\|\nabla\chi\|_2.
$$

Assume $0<h\le\delta$ and that the supporting ball fits strictly inside the periodic cell. A curl is automatically divergence-free, so define

$$
W_h=\operatorname{Re}\left\{
 h\nabla\times\left(\frac{i}{2}\chi_\delta e_3 e^{2ix_1/h}\right)
\right\}.
$$

The compact vector potential extends smoothly by zero and then periodically. Its phase need only be defined on the patch: $2/h$ need not be an integer. Differentiating gives the explicit real field

$$
W_h=
\begin{pmatrix}
-\frac h2(\partial_2\chi_\delta)\sin(2x_1/h)\\
\chi_\delta\cos(2x_1/h)+\frac h2(\partial_1\chi_\delta)\sin(2x_1/h)\\
0
\end{pmatrix}.
$$

The first component is the compensating motion. Its $x_1$-derivative cancels the envelope divergence and the mixed derivative contributed by the second component. Alternatively, $\nabla\cdot(\nabla\times A)=0$ proves the cancellation at once. Integrating a periodic curl also shows that the field has zero spatial mean.

The two correction terms have $L^2$ size at most $C h/\delta$. This is the first reason to separate wavelength from envelope width: many oscillations fit inside the envelope when $h/\delta$ is small. To check the normalization, use $\cos^2\theta=(1+\cos2\theta)/2$ and integrate the oscillatory term once in $x_1$:

$$
\left|\int\chi_\delta^2 e^{4ix_1/h}\,dx\right|
\le\frac h4\|\partial_1(\chi_\delta^2)\|_1
\le C\frac h\delta.
$$

The leading term therefore has squared norm $1/2+O(h/\delta)$. The cross term with the correction is $O(h/\delta)$, and its squared norm is $O((h/\delta)^2)$. Thus

$$
\|W_h\|_2^2=\frac12+O(h/\delta).
$$

For sufficiently small $h/\delta$, this is at least $1/4$, so normalization costs at most a fixed factor. We have constructed a smooth real seed, with exact divergence and mean constraints and controlled size. We have not yet evolved it. In the curved-flow construction below, the wave normal and amplitude vary along the flow, but taking a curl plays the same role.

## One finite amplification result

The [finite viscous-packet source theorem](../../references/navier-stokes/viscous-packet.md) starts with the growing polarization vector and places an oscillating wave around its orbit. Realize the wave as a curl to preserve divergence, compare it with an exact linearized solution, and then estimate the nonlinear interactions. The linearized equation retains terms of first order in the disturbance; the final comparison accounts for the remaining quadratic terms. Each passage has its own error cost. The resulting theorem gives arbitrarily large **relative** high-frequency gain across a family of smooth solutions, while keeping the absolute output below a specified target.

A norm growing from $h^7$ to $h^6$, with $0<h<1$, gains a factor $h^{-1}$, while both norms tend to zero. Relative gain compares the output with its own starting size. Reaching a target compares that same output with a separately chosen scale.

### Fix the field before changing the scale

Freeze one compact Gavrilov velocity profile $V$, its selected orbit, and its positive polarization exponent $\mu$. These do not vary with the concentration parameter $L$, which tends to infinity. Fix physical viscosity $\nu>0$. In rescaled coordinates, $h$ is the wave's oscillation scale, $\epsilon$ is viscosity and $\delta$ is the envelope width:

$$
h=L^{-1/10},\qquad \epsilon=\nu h^4,\qquad \delta=h^{1/2}.
$$

The proof works on the expanding torus with unnormalized norms and then rescales to the original torus at viscosity $\nu$. Write $q$ for the rescaled velocity. With velocity multiplier $A_L=L^{7/5}$, the map is $u_L(t,x)=A_Lq(A_LL t,Lx)$. Rescaled time is $\tau=A_LL t$, and a rescaled unnormalized $L^2$ norm acquires the factor $h/(2\pi)^{3/2}$ in the physical averaged norm. The initial datum changes with $L$; this is not one solution passing through infinitely many scales.

### Inputs from the full PDE proof

The rest of this subsection states the analytic inputs used by the source theorem. Their proofs require uniform Sobolev estimates, the full pressure residual and a continuation argument; the chapter will use these inputs to check the amplification margin, rather than claim to reprove them here. A growing vector on one particle is not yet a growing fluid perturbation. The proof transports a local phase $S$ by the fixed Euler flow, sets the covector $\xi=\nabla S$, and evolves its tangent polarization $b$ with the pressure-corrected equation from the preceding chapter. In this chapter $S$ denotes phase, not the strain matrix of the equation chapter. The proof forms a complex oscillatory approximation $w^a$ as an exact curl, with $i^2=-1$:

$$
w^a=h\,\nabla\times\left(i\frac{\xi\times b}{|\xi|^2}e^{iS/h}\right).
$$

The compact vector potential extends smoothly by zero outside its transported patch. Its curl is exactly solenoidal (divergence-free) and mean-zero. A real packet is extracted in the normalization step below. The packet has a Fourier tail; compact support in space does not mean finitely many frequencies.

Four costs connect this approximation to the actual time-dependent NS linearization: localization near the selected orbit, the curl and envelope correction, viscous damping, and the difference between the Euler and NS backgrounds. Their scales are $\delta$, $h/\delta$, $\epsilon/h^2$, and $\epsilon/h$, with explicitly controlled exponential time factors. Choosing a sufficiently small fixed $c>0$ makes them subordinate to the signal on $T=c\log(1/\epsilon)$. A Fourier-moment estimate controls the actual radial high-pass norm, rather than only the amplitude at the central particle.

The nonlinear step is separate. Choose a real normalized seed and multiply it by the small seed factor $\eta=h^6$. A strong $H^3$ bootstrap and a nonlinear error estimate then realize the gain for an actual smooth solution. Here $H^s$, for integer $s$, controls square-integrable derivatives through order $s$; a bootstrap assumes a bound on a smooth existence interval and proves a stricter bound that allows continuation. All constants may depend on the frozen profile; the proof gives no computed minimum $L$.

### A large ratio can have a small numerator

Let $P_{>H}$ retain Fourier modes with radial wavevector magnitude greater than $H$. For the physical threshold $H=L/h$, the [full theorem](../../references/navier-stokes/viscous-packet.md) proves gain by at least $a_1\epsilon^{-\mu c}$, tending to infinity, with fixed positive lower-bound constant $a_1$. Write $K_n$ for the fixed growth constant in the nonlinear bootstrap, and $C_\nu$ for an upper-bound constant that may depend on the fixed viscosity and profile. The theorem also proves throughout the controlled interval

$$
\|P_{>H}u_L(t)\|_{2,\mathrm{av}}
\le C_\nu\bigl(h^9+h^{7-4cK_n}\bigr),
\qquad 7-4cK_n>\frac{11}{2}.
$$

For the benchmark absolute target $H^{-1/10}=h^{11/10}$, dividing the displayed upper bound by the target gives a quantity tending to zero. The gain ratio diverges while the output stays below that target. The seed also stays small in rescaled $C^1$, so this regime does not yet transfer the background strain to the wave.

## Check the amplification margin

The theorem's conclusion depends on a balance that can now be calculated. With the scales above, the four errors in the linear comparison have sizes

$$
\delta=h^{1/2},\qquad \frac h\delta=h^{1/2},\qquad
\frac\epsilon{h^2}=\nu h^2,\qquad
\frac\epsilon h=\nu h^3.
$$

The first two balance spatial coherence against the derivative of the envelope. The third is the viscous cost at the carrier wavelength. The last charges the difference between using the Euler flow and the actual viscous flow to transport the packet.

Here is a precise input from Part I of the [source proof](../../references/navier-stokes/viscous-packet.md). For its exact linearized solution $w$, initially normalized in $L^2$, the predicted high-pass signal is bounded below by a fixed positive multiple of $e^{\mu T}$. The error is bounded above by

$$
C\left[
(\delta+h/\delta+\epsilon/h^2)e^{\Gamma T}
+(\epsilon/h)e^{(\Gamma+\kappa)T}
\right],
\qquad T=c\log(1/\epsilon).
$$

The fixed positive rates $\Gamma$ and $\kappa$ control the packet errors and the viscous background comparison. They depend on the frozen profile, not on $h$. The source retains the complete pressure projection and proves this for the actual Fourier high-pass norm over the whole domain. It also selects and normalizes a real quadrature of the complex packet for this observation time; the cosine quadrature in the elementary example need not by itself be the growing one.

Since $\epsilon=\nu h^4$, evaluating the exponentials converts this bound into

$$
C_\nu\left[
 h^{1/2-4c\Gamma}+h^{2-4c\Gamma}
 +h^{3-4c(\Gamma+\kappa)}
\right].
$$

Choose $c>0$ sufficiently small, in particular
$4c(\Gamma+\kappa)<1/4$. Each power is then positive: the error tends to zero. Meanwhile the signal $e^{\mu T}=\epsilon^{-\mu c}$ tends to infinity. The lower triangle inequality now proves gain for the exact linearized solution from the stated input estimates. Choosing $c$ comes after fixing the profile and all its rates.

### Include the nonlinear error and the background

Let $v_\epsilon$ be the actual viscous background starting at $V$, and let $q$ solve the full unforced equation starting at $V+\eta f_h$, where $f_h$ is the source's real unit seed. With $\eta=h^6$, write

$$
q=v_\epsilon+\eta w+e,\qquad e(0)=0.
$$

This is an exact decomposition once the solutions exist. The nonlinear terms produce $e$; they are absent from the equation defining $w$. Part II of the source supplies two separate estimates, with fixed rates $K_n,K_e>0$:

$$
\|q-v_\epsilon\|_{H^3}\le C h^3e^{K_n\tau},
\qquad
\|e\|_2\le C\eta^2h^{-4}e^{K_e\tau}.
$$

The first estimate is obtained by a strong-solution bootstrap and guarantees continuation to $T$ when $c$ obeys the source's smallness conditions. The second comes from the exact difference equation and relative energy. These are distinct PDE inputs: a small $L^2$ comparison error does not itself establish smooth existence.

Decrease the same fixed $c$, if necessary, so that
$4cK_n<3/2$ and $4cK_e<1$, as well as the source's remaining smallness conditions. At the endpoint the first bound is $C_\nu h^{3-4cK_n}=o(1)$, strictly inside the bootstrap range for sufficiently small $h$. The nonlinear error relative to the seed size satisfies

$$
\frac{\|e(T)\|_2}{\eta}
\le C_\nu h^{2-4cK_e}\longrightarrow0.
$$

For comparison with the whole velocity, the background's Fourier tail must also be counted. Its uniform fixed-order Sobolev bound gives
$\|P_{>1/h}v_\epsilon\|_2\le C h^8$ throughout this interval; here the projector acts in the rescaled coordinates. The triangle inequality yields

$$
\|P_{>1/h}q(T)\|_2
\ge\eta\|P_{>1/h}w(T)\|_2
-\|P_{>1/h}v_\epsilon(T)\|_2-\|e(T)\|_2.
$$

After division by $\eta=h^6$, the background costs $O(h^2)$, the nonlinear error tends to zero, and the linearized signal grows like $\epsilon^{-\mu c}$. Initially, the total high-pass norm is at most $\eta+C h^8$; the source's seed also has asymptotically unit high-pass norm. Hence the final-to-initial ratio grows by a fixed positive multiple of $\epsilon^{-\mu c}$. Physical rescaling multiplies both norms by the same factor, preserving that ratio.

We have proved the amplification implication from the stated PDE estimates, including the background and nonlinear error. The source proof establishes those estimates with all modes and pressure present. Its simultaneous upper bound, displayed above, shows why this unbounded ratio still lies below the specified absolute activation target.

## What changes when the output is strain?

Velocity and strain require different error norms. Along the periodic sequence $h=1/n$, the field $h\sin(x_1/h)e_2$ tends to zero in $L^2$, while its gradient has sup norm one. A velocity error small in $L^2$ can therefore obscure a strain signal. In the representative theorem, the separate $H^3$ estimate controls first derivatives by Sobolev embedding, but keeps the disturbance small rather than proving strain handover.

The [advanced companion](advanced-transfer.md#to-transfer-strain-control-derivatives-of-the-error) studies a larger amplitude, corrected means and harmonics, and interpolation estimates that make the derivative error small enough to compare strain. It then examines original-time preparation, finite regions of nearly uniform strain, later windows and smoothly forced stages. Those are additional research results with their own hypotheses, not further conclusions of the single packet argument proved conditionally here.

For the core course, continue to [iteration](iteration.md): a family of finite amplifications must satisfy new compatibility and uniformity requirements before it can describe one complete evolution. The external forced C/D result has its own construction, discussed in [the published-proof chapter](published-proof.md).

## Exercises: test the conclusion before using it

### 1. Compare ratio and target

Suppose an initial norm is $h^7$, and its final norm is $h^6$. What happens to the gain ratio and to the ratio of the final norm to $h^{11/10}$ as $h\to0$?

<details markdown="1"><summary>Solution and feedback</summary>

The gain is $h^{-1}\to\infty$, while the final-to-target ratio is $h^{49/10}\to0$. A diverging amplification factor alone says nothing about reaching that absolute target. The numerator, denominator and target must all be tracked as the parameter changes.

</details>

### 2. Charge the viscous cost

In the scalar model, take constant growth rate $\sigma>0$, frequency $K>0$ and viscosity $\nu>0$ for time $t_*$. Find the condition for gain. If the frequency is doubled while the duration is divided by four, what happens to the growth and damping exponents?

<details markdown="1"><summary>Solution and feedback</summary>

Gain requires $\sigma>\nu K^2$, since the factor is $e^{(\sigma-\nu K^2)t_*}$. The change leaves damping $\nu K^2t_*$ unchanged, while growth $\sigma t_*$ is divided by four. Shorter time does not make a finer wave's damping free; compare both terms over the same interval.

</details>

### 3. Decide whether an error estimate proves growth

Suppose a predicted output norm is exactly $h^2$. An approximation theorem bounds the error in that norm by $h^3$. Give a lower bound for the actual output. Now suppose the only available error bound is $h$. Has the predicted signal been justified or disproved?

<details markdown="1"><summary>Solution and feedback</summary>

The first bound gives $h^2-h^3=h^2(1-h)>0$ for $0<h<1$. The second gives only the uninformative bound $h^2-h<0$; nonnegativity then supplies zero. A bound too large to certify the signal does not prove that the signal is absent. It identifies a missing comparison estimate.

</details>

### 4. Locate the quantifier error

For every positive integer $j$, suppose a smooth solution $u_j$ from datum $u_{0,j}$ has a finite amplification factor at least $j$. A reader concludes: “A solution has infinite amplification, hence a finite-time singularity.” Explain both gaps.

<details markdown="1"><summary>Solution and feedback</summary>

The hypothesis gives a possibly different datum and solution for every $j$. It does not produce one datum whose trajectory realizes all stages. Also, a diverging ratio across a family need not give a diverging absolute velocity or derivative, let alone breakdown at a common finite time. The finite theorems need their full initial-data, time and norm quantifiers when used in another argument.

</details>

## Further reading

Majda and Bertozzi's [*Vorticity and Incompressible Flow*, Chapter 3](https://www.cambridge.org/core/books/abs/vorticity-and-incompressible-flow/energy-methods-for-the-euler-and-the-navierstokes-equations/E5489F542D15DFDC03F96046A8E05265) develops energy methods for Euler and Navier–Stokes. John K. Hunter's [*Notes on Partial Differential Equations*](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), §1.13, Chapter 3 and §§5.4–5.5, provides background on Gronwall's inequality, Sobolev estimates, semigroups and semilinear evolution.

The research proof used here is [finite viscous amplification](../../references/navier-stokes/viscous-packet.md): Part I establishes the localized linear comparison, and Part II establishes nonlinear continuation and the remaining error estimate. The [claim register](../claims.md#nse-viscous-packet-amplification) records its written and AI-review scope. The optional [advanced-transfer companion](advanced-transfer.md) retains the later extensions and supplementary exercises 5–8.

AI review is not external expert acceptance. These entries record the checking process, not certification.
