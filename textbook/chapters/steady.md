# A steady reference flow

Return to the exact shear $u=a(0)e^{-\nu N^2t}\sin(Ny)e_1$. If viscosity is set to zero, its layers slide forever at their original speeds: the velocity field is steady. With positive viscosity, the same initial field begins to decay. A steady inviscid field can therefore serve as a reference, provided we keep track of the difference created by viscosity.

In the [concentration chapter](concentration.md), stronger strain came with a shorter guaranteed lifetime. A steady reference offers a way to extend the comparison. The difficulty is that a general reference flow can amplify the very error that viscosity creates. If we make viscosity a hundred times smaller in the rescaled equation, how much longer can the two flows remain close?

## A small defect that grows with time

Let $\epsilon>0$ measure a constant source of error, let $F>0$ measure its size, and let $\kappa>0$ be an amplification rate. Consider the scalar equation

$$
z'=\kappa z+\epsilon F,\qquad z(0)=0.
$$

Here the independent variable is $\tau$, and the prime means $d/d\tau$. The constant source creates error even from zero initial error; the term $\kappa z$ then amplifies what has accumulated. Before solving, compare this with the unforced shear amplitude, whose coefficient was negative. We now expect growth rather than damping. Multiplying by the integrating factor $e^{-\kappa\tau}$ gives

$$
\frac{d}{d\tau}(e^{-\kappa\tau}z)
=\epsilon F e^{-\kappa\tau}.
$$

Integrating from zero to $\tau$ and multiplying back gives

$$
z(\tau)=\frac{\epsilon F}{\kappa}(e^{\kappa\tau}-1).
$$

To keep $z\le r/2$, where $r>0$ is a chosen tolerance, solve the inequality:

$$
\tau\le \frac1\kappa
\log\left(1+\frac{\kappa r}{2\epsilon F}\right).
$$

For $\kappa=F=r=1$ and $\epsilon=1/100$, the allowed interval is $\tau\le\log51$, about $3.93$. Reducing $\epsilon$ to $1/10{,}000$ extends it to $\log5001$, about $8.52$. A hundredfold reduction in defect does not give a hundredfold longer interval: amplification makes the gain logarithmic.

For the fluid, the same integrating factor will estimate a norm rather than solve for a scalar amplitude exactly. A nonlinear term makes the estimate conditional on the error staying small. We will close that condition by a **bootstrap argument**: derive a bound strictly inside the assumed range, then use continuity to rule out a first exit.

## Separate the equations and scales

The shear gave a simple steady Euler reference. For the later amplification construction we need a three-dimensional reference localized in space. Fix a nonzero smooth, compactly supported Euler profile $V$ satisfying

$$
\nabla\cdot V=0,\qquad (V\cdot\nabla)V+\nabla P=0.
$$

The existence of such fields is a theorem of [A. V. Gavrilov](https://arxiv.org/abs/1810.08020). [Peter Constantin, Joonhyun La and Vlad Vicol](https://arxiv.org/abs/1903.11699) develop a related construction through localizable Grad–Shafranov equations. We take this existence theorem as an input; our calculation concerns the viscous evolution starting from a fixed one of these fields.

Choose a positive amplitude factor $a_L$ and a concentration parameter $L$, and set

$$
A_L=a_LL^{3/2},\qquad y=Lx,\qquad\tau=A_LL t,
\qquad\epsilon=\frac{\nu L}{A_L}.
$$

For sufficiently large $L$, the compact support of $V$ fits inside $(-\pi L,\pi L)^3$. Repeating it periodically places it on a torus of side $2\pi L$; this is the **expanding torus**. The coordinate change $y=Lx$ returns it to the fixed physical box of side $2\pi$.

Then $U_L(t,x)=A_Lv_\epsilon(\tau,y)$, where $v_\epsilon$ solves unforced NS with viscosity $\epsilon$ on that expanding torus and begins at $V$. The factors have distinct roles: $L$ contracts length, $A_L$ multiplies velocity, and $A_LL$ converts physical time to the natural advective time. Substitution leaves the viscosity coefficient $\epsilon=\nu L/A_L$.

The small-viscosity limit in this comparison means choosing $A_L/L\to\infty$, so that $\epsilon\to0$. The physical viscosity $\nu$ stays fixed throughout; the initial datum changes with $L$.

## Derive the bootstrap estimate

For the shear, one amplitude described the entire error. Here the error can change shape, so we measure the field and its derivatives together. For an integer $s\ge3$, the Sobolev norm $H^s$ measures their square-integrable size through derivative order $s$. We use unnormalized integrals on the expanding torus, with the precise convention in the source. This norm provides both a measure of closeness and enough spatial regularity to continue the comparison.

Set $z=\|v_\epsilon-V\|_{H^s}$ and $F=\|\Delta V\|_{H^s}$. The Euler terms for $V$ cancel exactly, but the viscous term $\epsilon\Delta V$ remains. This is the continuous source of error represented by $\epsilon F$ in the scalar model. The [source proof](../../references/navier-stokes/steady-background.md) estimates the complete difference equation, including pressure, to obtain

$$
z'\le C_Vz+C_sz^2+\epsilon F,\qquad z(0)=0.
$$

Here $C_V$ depends on the fixed reference field, and $C_s$ also records the regularity used in the nonlinear estimate. The term $C_Vz$ propagates error through the reference flow; $C_sz^2$ comes from the error interacting with itself.

Fix $r>0$. **As long as** $z\le r$, we have $z^2\le rz$, so

$$
z'\le (C_V+C_sr)z+\epsilon F
\le\kappa z+\epsilon F,
\qquad \kappa\ge C_V+C_sr>0.
$$

The integrating-factor calculation from the warm-up now yields an upper bound:

$$
z(\tau)\le\frac{\epsilon F}{\kappa}(e^{\kappa\tau}-1).
$$

This gives $z\le r/2$ through

$$
T_\epsilon=\frac1\kappa\log\left(1+\frac{\kappa r}{2\epsilon F}\right).
$$

To complete the argument, suppose there were a first time before $T_\epsilon$ at which $z=r$. Continuity gives $z\le r$ up to that time, so the estimate we just derived applies there. It instead gives $z\le r/2$, a contradiction. The margin between $r/2$ and $r$ prevents a first exit.

The same bound also addresses existence. The local existence theorem allows continuation while the relevant $H^s$ norm stays bounded. Since $\|v_\epsilon\|_{H^s}\le\|V\|_{H^s}+r/2$, that obstruction cannot occur before the endpoint. The proof has now established both the existence of the evolving solution and its closeness to the reference throughout the claimed interval.

## Keep the profile and the time units fixed

The logarithmic interval follows from a particular order of choices: fix $V$, the regularity index and the tolerance first; then decrease $\epsilon$. The constants are independent of the expanding cell size. Changing the shape of $V$ at the same time could change $C_V,F,\kappa$, and hence the conclusion. Exercise 3 shows how strongly this can matter even in the scalar model.

The interval $T_\epsilon$ is measured in the rescaled time $\tau$. In physical time it is

$$
t_\epsilon=\frac{T_\epsilon}{A_LL}.
$$

A rescaled interval can lengthen while the physical interval shortens, because the conversion factor $A_LL$ also changes. Each $L$ specifies one initial datum and one finite comparison. To concatenate such stages into a single evolution would require the endpoint compatibility studied in [iteration](iteration.md).

Compact support changes the frequency analysis too. A nonzero smooth profile that vanishes outside a spatial region has infinitely many Fourier modes after periodic embedding. Smoothness makes the far-frequency coefficients small, so estimates now use their decay rather than an exactly empty tail.

## Exercises

### 1. Why a shorter logarithmic window converges

For $0<c<1/\kappa$, show that the error bound at $\tau=c\log(1/\epsilon)$ tends to zero as $\epsilon\to0$.

<details markdown="1"><summary>Hint</summary>

Rewrite $e^{\kappa c\log(1/\epsilon)}$ as a power of $\epsilon$, keeping $F$ and $\kappa$ fixed.

</details>

<details markdown="1"><summary>Solution</summary>

The exponential becomes $\epsilon^{-\kappa c}$. Hence $z\le(F/\kappa)\epsilon^{1-\kappa c}$, after dropping the negative term. The exponent is positive precisely under the stated restriction. For sufficiently small $\epsilon$, this is below $r/2$, so the same first-exit argument justifies the estimate throughout the proposed shorter interval. This proves convergence for a fixed profile; it does not amplify a seed.

</details>

### 2. Find the circular step

A proposed proof reads: “Assume $z\le r$. The estimate gives $z\le2r$ until time $T$. Therefore the bootstrap assumption holds until $T$.” Explain the gap. Does the bound $2r$ itself show that the actual error leaves the range?

<details markdown="1"><summary>Hint</summary>

At a proposed first exit, the error equals $r$. Would $z\le2r$ contradict that value?

</details>

<details markdown="1"><summary>Solution</summary>

It would not: $z=r$ satisfies the bound $z\le2r$. The proof has supplied no reason the assumption persists. Nor does an upper bound of $2r$ show that the actual error reaches $r$; it may simply be a poor estimate. Our $r/2$ bound is useful because it contradicts a first exit at $r$.

</details>

### 3. Changing the profile changes the calculation

In the scalar warm-up, take $F=r=1$ but let $\kappa=1/\epsilon$. Find the time for which $z\le1/2$. Does it grow like $\log(1/\epsilon)$ as before?

<details markdown="1"><summary>Hint</summary>

Substitute the new $\kappa$ into the exact tolerance formula, including the factor outside the logarithm.

</details>

<details markdown="1"><summary>Solution</summary>

The time is
$$
T_\epsilon=\epsilon\log\left(1+\frac1{2\epsilon^2}\right).
$$
It tends to zero as $\epsilon\to0$, since $\epsilon\log(1/\epsilon)\to0$. A vanishing defect is compatible with a shorter guaranteed interval when amplification grows fast enough. This is why the dependence of the constants on the reference profile is part of the theorem.

</details>

## Further reading

Gavrilov's [*A steady Euler flow with compact support*](https://arxiv.org/abs/1810.08020) supplies the existence result used here. Constantin, La and Vicol's [*Remarks on a paper by Gavrilov*](https://arxiv.org/abs/1903.11699) gives a complementary route to compactly supported steady fields. These are sources for the reference geometry; the comparison above starts after one field has been chosen.

The bootstrap and Sobolev energy method belong to classical PDE analysis. Majda and Bertozzi's [chapter on energy methods](https://www.cambridge.org/core/books/abs/vorticity-and-incompressible-flow/energy-methods-for-the-euler-and-the-navierstokes-equations/E5489F542D15DFDC03F96046A8E05265) provides the broader theory. For the constants, expanding-domain estimates and complete proof used in this project, see [the steady-background note, §§1–4](../../references/navier-stokes/steady-background.md) and its [registered claim](../claims.md#nse-steady-background-local).

A long-lived reference alone does not tell us which disturbances grow. The next chapter follows [pressure and returning covectors](oblique.md) to identify a particular expanding direction.
