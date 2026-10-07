# Making a new construction

A proof can become a source of new problems. Once a construction works,
we can ask which choices were essential, which were convenient, and what
can be changed while preserving its conclusion. The answer should produce
a new object together with a proof of what it does.

We begin with a two-variable flow whose transfer can be calculated exactly.
Changing its coupling will produce a family of different motions with the
same terminal output. A general replacement estimate explains what survives
when exact preservation is unavailable. These calculations use
[transfer systems](transfer-systems.md), [residual propagation](residuals.md)
and the interval conditions from [iteration](iteration.md).

## 1. A transfer we can redesign

Consider

$$
x'=-x+c(t)y,\qquad y'=-2y,\qquad x(0)=0,\quad y(0)=1.
$$

The second component decays independently. The coupling $c(t)$
transfers some of it into the first component. With $c=8$,

$$
y(t)=e^{-2t},\qquad x(t)=8(e^{-t}-e^{-2t}).
$$

At $T=\log2$, the output is $x(T)=2$. A unit input in the second
coordinate has produced a first-coordinate output of two, although both
diagonal rates are negative. Predict what happens if we weaken the coupling
early and strengthen it later. Does keeping its ordinary time average
unchanged preserve the output?

Multiplying the first equation by $e^t$ answers the question:

$$
\boxed{x(T)=e^{-T}\int_0^T c(s)e^{-s}\,ds.}
$$

The relevant quantity is a **weighted** integral. The weight combines the
remaining second-coordinate input with the later decay of the first
coordinate. Changing the timing of the coupling can therefore change the
output even when its ordinary average is fixed.

## 2. A component-replacement theorem

The same issue occurs for a general linear system. Use the Euclidean norm
and its induced matrix norm. Let $A,E:[0,T]\to\mathbb R^{d\times d}$
and $b,r:[0,T]\to\mathbb R^d$ be continuous. Compare

$$
x'=Ax+b,\quad x(0)=x_0,
\qquad
\widetilde x'=(A+E)\widetilde x+b+r,
\quad\widetilde x(0)=x_0+e_0.
$$

Here $E$ replaces part of the coupling and $r$ changes the drive.
These define different model evolutions. They do not assert that an altered
trajectory still solves the original equation.

**Theorem (standard perturbation estimate).** Suppose the reference solution has a known continuous bound
$|x(t)|\le M(t)$, with $M\ge0$, and put
$L(t)=\|A(t)+E(t)\|$. Then

$$
\begin{aligned}
|\widetilde x(T)-x(T)|\le B(T):={}&
e^{\int_0^T L}|e_0|\\
&+\int_0^T e^{\int_s^T L}
       \bigl(\|E(s)\|M(s)+|r(s)|\bigr)\,ds.
\end{aligned}
$$

For a linear observable $\ell:\mathbb R^d\to\mathbb R$, a reference
lower bound $\ell(x(T))\ge m$ therefore yields

$$
\ell(\widetilde x(T))\ge m-\|\ell\|B(T).
$$

In particular, a target $a<m$ survives whenever
$\|\ell\|B(T)\le m-a$.

**Proof.** Continuous linear coefficients on a compact time interval give
unique solutions throughout that interval. This is the standard linear
ODE existence theorem; no nonlinear continuation hypothesis is being
assumed. Subtract the two equations and set $e=\widetilde x-x$:

$$
e'=(A+E)e+Ex+r.
$$

The term $Ex$ is essential: a coefficient change acts on the reference
trajectory as well as on its error. Let $\widetilde\Phi(t,s)$ be the
evolution matrix for $A+E$. Variation of constants gives the exact identity

$$
e(T)=\widetilde\Phi(T,0)e_0+
\int_0^T\widetilde\Phi(T,s)(E(s)x(s)+r(s))\,ds.
$$

For a vector evolved from time $s$, the norm inequality
$D^+|z|\le L(t)|z|$ gives
$\|\widetilde\Phi(t,s)\|\le e^{\int_s^t L}$. Applying this bound,
the triangle inequality and $|Ex|\le\|E\|M$ proves the first claim.
Finally,
$\ell(\widetilde x)=\ell(x)+\ell(e)\ge m-\|\ell\||e|$, which
proves the observable estimate. $\square$

This is the classical variation-of-constants stability principle, organized
here as a component-replacement statement. For the underlying linear ODE
theory, see Teschl's [*Ordinary Differential Equations and Dynamical
Systems*](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/). The teaching
formulation lets us apply that theory to a design choice; it does not claim
a new general stability theorem.

The theorem is useful when the replacement can be measured more easily
than the new solution can be solved. Its cost includes the whole reference
trajectory and the new propagator. Matching only eigenvalues, an endpoint
matrix, or a component's name would not supply these estimates.

## 3. A new variant with exactly the same output

Return to the triangular system and set

$$
c_\varepsilon(t)=8\left[1+\varepsilon
             \left(1-\frac43e^{-t}\right)\right],
\qquad 0\le\varepsilon\le1,\quad 0\le t\le\log2.
$$

This coupling is weaker than eight early in the interval and stronger
later. It is smooth and positive: throughout the interval,
$16/3\le c_\varepsilon\le32/3$. The weighted change is

$$
\int_0^{\log2}(c_\varepsilon-8)e^{-s}\,ds
=8\varepsilon\left[\frac12-\frac43\frac38\right]=0.
$$

Consequently every member has $x(T)=2$, exactly. Integrating at an
intermediate time gives the complete new trajectory:

$$
x_\varepsilon(t)=8(e^{-t}-e^{-2t})+
\frac{8\varepsilon}{3}e^{-t}(1-e^{-t})(1-2e^{-t}).
$$

For $0<t<\log2$ and $\varepsilon>0$, the correction is negative.
The trajectories differ before arriving at the same endpoint. This is a
construction, not just an error bound: its equations, admissible parameter
range, full trajectory and preserved output are explicit.

We also know what it costs in time variation:
$c_\varepsilon'=(32\varepsilon/3)e^{-t}$. Those derivative bounds
would matter if this component were to be placed inside a larger
time-dependent construction. Endpoint agreement alone does not supply them.

There is also a systematic way to find replacements that agree near both
endpoints. Choose any smooth nonzero $H$ supported strictly inside
$(0,T)$, and put

$$
r_H(t)=e^tH'(t),\qquad c_H(t)=8+\varepsilon r_H(t).
$$

Then $\int_0^T e^{-t}r_H(t)dt=H(T)-H(0)=0$, while the whole
trajectory changes by $\varepsilon e^{-t}H(t)$. The coupling and all
its derivatives agree with the original constant near the endpoints.
Moreover, $|\varepsilon|e^T\|H'\|_\infty<8$ guarantees positive
coupling. We have parameterized a family by a freely chosen interior
function rather than guessed one successful perturbation. For each fixed
derivative order its cost is explicit:

$$
\|r_H^{(m)}\|_\infty
\le e^T\sum_{k=0}^m\binom mk\|H^{(k+1)}\|_\infty.
$$

This freedom is useful precisely because the constraint it must preserve
has been identified and solved. The second coordinate is unchanged, and
the first agrees with the original trajectory near $T$. A subsequent
deterministic stage starting at $T$ therefore receives the same complete
state. The alteration changes an interior part of the construction while
preserving its handover.

## 4. A counterexample to preserving the wrong quantity

Instead choose $\widehat c(t)=8+\varepsilon(t-T/2)$. Its ordinary
integral is unchanged because $\int_0^T(t-T/2)\,dt=0$. Its weighted
integral is not:

$$
\int_0^T(t-T/2)e^{-t}\,dt
=\frac{2-3\log2}{4},\qquad T=\log2.
$$

Thus

$$
\widehat x(T)-2=\varepsilon\frac{2-3\log2}{8}\ne0
\quad(\varepsilon\ne0).
$$

For a sufficiently small positive $\varepsilon$, the coupling remains
positive but the output falls below two. The failure is precise: we
preserved the average of the component instead of the integral through
which the evolution uses that component.

## 5. Exercises

**1. Change a decay rate.** Replace $y'=-2y$ by $y'=-y$, keeping
$x'=-x+c(t)y$ and the same initial values. Derive the terminal-output
formula. Which changes in $c$ now preserve the output? Does the family
$c_\varepsilon$ from Section 3 still preserve it at $T=\log2$?

<details markdown="1">
<summary>Solution</summary>

Now $(e^t x)'=c(t)$, so $x(T)=e^{-T}\int_0^T c(s)\,ds$.
Zero ordinary integral is the correct replacement condition for these
equal decay rates. For the earlier family the change in the integral is
$8\varepsilon(T-2/3)$, which is nonzero at $T=\log2$ when
$\varepsilon>0$. Its output changes by
$4\varepsilon(\log2-2/3)$. Changing a decay rate changes the condition
that a coupling replacement must satisfy.

</details>

**2. Spend an output margin.** In the original system, replace $c=8$
by $8+r(t)$, with $|r(t)|\le\delta$. Bound the terminal-output
change sharply using the explicit integral. How small must $\delta$
be to guarantee $x(\log2)\ge1.9$? Does this amplitude assumption
also give a common bound on $r'$ for every smooth replacement?

<details markdown="1">
<summary>Solution</summary>

The change has magnitude at most
$e^{-T}\delta\int_0^T e^{-s}ds=\delta/4$, attained by constant
replacements of either sign. Thus $\delta\le0.4$ guarantees the
target. No common derivative bound follows: $r_n(t)=\delta\sin(nt)$
has amplitude at most $\delta$ while $|r_n'(0)|=\delta n$.
A later theorem requiring derivative bounds needs additional hypotheses.

</details>

## 6. A research problem suggested by the published proof

The [published construction](published-proof.md) uses oscillatory waves
to realize a prescribed stress. This suggests a concrete replacement
problem: change a wave's phase while preserving the stress it supplies.
Before attempting that construction, consider what such preservation
actually tells us.

On the periodic domain $(\mathbb R/2\pi\mathbb Z)^3$, fix an integer
$N\ge1$, viscosity $\nu>0$, and a smooth real function $\theta(t)$.
Let $e_2=(0,1,0)$ and set

$$
\begin{gathered}
w_\theta(t,x)=a(t)\cos(Nx_1+\theta(t))e_2,\\
a(t)=e^{-\nu N^2t}.
\end{gathered}
$$

The phase $\theta$ moves the crests of the shear. Predict whether it
changes the spatial average of $w_\theta\otimes w_\theta$, the matrix
with entries $(w_\theta)_i(w_\theta)_j$. Writing angle brackets for
the normalized spatial average, integration over a full period gives

$$
\langle w_\theta\otimes w_\theta\rangle
=\frac{a(t)^2}{2}\,e_2\otimes e_2.
$$

Every phase gives exactly the same averaged stress. Does every phase also
give a solution of the unforced equation?

The field is divergence free: its only nonzero component points in the
$x_2$ direction and is independent of $x_2$. For the same reason,
$(w_\theta\cdot\nabla)w_\theta=0$. The Laplacian is
$\Delta w_\theta=-N^2w_\theta$, and $a'=-\nu N^2a$, so the
momentum residual with zero pressure is

$$
\begin{aligned}
R_\theta
&=\partial_t w_\theta+(w_\theta\cdot\nabla)w_\theta
                         -\nu\Delta w_\theta\\
&=-a(t)\theta'(t)\sin(Nx_1+\theta(t))e_2.
\end{aligned}
$$

For constant phase this vanishes. A moving phase requires an additional
force. The residual is itself divergence free and has zero mean, so the
Leray projection leaves it unchanged; periodic pressure cannot remove it.
Moreover, with $\theta(t)=\delta\sin(Mt)$, the phase change is at most
$\delta$, while $\|R_\theta(0)\|_\infty=\delta M$.
Arbitrarily small phase changes can therefore require arbitrarily large
forces. They also have the same initial velocity as the zero-phase shear.
Matching a stress, or even matching it at every time, does not control the
rate at which the underlying wave moves.

There is nevertheless a precise opening in the published proof. Its
[assembled covariance identity](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PartitionedCovariance.lean#L947)
allows arbitrary phases in its paired-wave data while keeping the required
two leading radial–tangential covariance components, with its specified
pulses, labels, masks and cone conditions. The full curl-corrected velocity
and its differential equation still need separate estimates.

The [phase-covariance corollary](../../formalization/phase_covariance/README.md)
states this freedom precisely and has passed Lean compilation and a replay
of its local declarations. Its [derivation and dependency record](../../references/analysis/external-component-extraction.md)
retain the geometric assumptions. This is a consequence of the published
identity; no new general covariance theorem is claimed.

The next test comes from transport. In the source's local coordinates,
write a complex carrier as $e^{iK\Phi}$, where $K\ne0$ is constant
within a chosen label and band, and let $D$ denote the material
derivative along the base flow. Adding an angular phase $\gamma$ means

$$
\widetilde\Phi=\Phi+\frac\gamma K,
\qquad D\widetilde\Phi=D\Phi+\frac{D\gamma}{K}.
$$

The [linear residual](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/LinearWaveResidual.lean#L111)
contains $iK(D\Phi)a$, with $a$ now the wave's complex amplitude.
The published [actual phase estimate](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualPrimaryBounds.lean#L1284)
controls this defect through every derivative order. Covariance supplies
none of these derivative bounds.

A concrete next research obligation is to construct one spatially
nonconstant modulation $\gamma_n$ and prove, on every active patch,

$$
\|\partial^\alpha(D\gamma_n)(z)\|
\le C_m\varepsilon_n^{1/2}G_n(z)^{p_m},
\qquad |\alpha|\le m.
$$

Here $n$ indexes bands, $\varepsilon_n$ is the small scale parameter,
and $G_n\ge1$ is the proof's fixed chart-growth weight. For each
$m$, the constants and polynomial degree must work for all bands,
labels and points. With the published reciprocal-frequency bound of order
$\varepsilon_n^{1/2}$, this proposed condition gives the added phase
defect the required order $\varepsilon_n$. It is a **sufficient proposed
condition for this one residual term**, not an established replacement
theorem.

A complete result must also derive the changed polarization, pressure,
solenoidal correction and support estimates. Iteration would then require
the compatible sums and derivative losses discussed in
[iteration](iteration.md). The immediate aim is one explicit new wave
variant with a proved transport cost. The calculation above identifies
what must be learned beyond stress preservation; it supplies no new
Navier–Stokes singularity construction.
