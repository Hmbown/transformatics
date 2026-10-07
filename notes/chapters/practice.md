# Practice and proof workshop

The two assessments below ask you to build a justified prediction. The first joins finite transformations, generators, representation and error propagation in a two-variable system. The second adds spatial resolution, physical units and the [exact fluid equation](equation.md). Both can be checked completely by hand; neither asks you to accept a numerical simulation as a proof.

Complete Assessment A after [Transfer systems](transfer-systems.md) and [Composition and error](composition.md). Complete Assessment B after the fluid equation. Keep your calculations before opening a solution. When an answer differs, locate the first incorrect equality or missing hypothesis, then repair the reasoning as well as the final number.

<span id="assessment-a"></span>

## Assessment A: design a representation and certify a prediction

Consider the autonomous system on $X=\mathbb R^2$

$$
a'=-a+b,\qquad b'=-2b,\qquad (a(0),b(0))=(0,1).
$$

You may record one linear combination $r=ca+db$. The intended measurement
is the total $a+b$, but a later user also asks for the full vector. The
instrument applies one update every $\tau=\log2$ units of time and
approximates the retained multiplier by $0.51$.

Submit one argument answering these five questions. Each part builds on
the preceding part; do not substitute a familiar error formula until you
have checked its hypotheses.

1. Solve the two equations for arbitrary initial values $(a_0,b_0)$.
   Verify the evolution law from your matrix formula, and calculate the
   generator on the observables $a+b$ and $a^2$.
2. Choose $R(a,b)$ so that the intended total is retained and has an
   exact scalar evolution. Verify exact transfer for every initial state,
   not only $(0,1)$. Explain why $R(a,b)=a$ would fail that test.
3. At times $t_n=n\log2$, compare the true retained value $r_n$
   with the computed value $y_n=0.51^n$. Derive both the one-step
   defect and an accumulated error bound. Can you obtain the exact error?
4. Reconstruct with $L(y)=(y,0)$. Give the exact Euclidean full-state
   error and a bound that separates lost information from evolution error.
   At $n=4$, does that bound certify tolerance $0.011$? What remains
   if the multiplier is made exact while the representation is kept?
5. A display reports $z=100r$. Write its approximate update, use
   quantitative composition to bound the displayed error, and explain why
   a tolerance on $r$ cannot be reused unchanged on $z$.

<details markdown="1">
<summary>Hint: look for a measurement with a closed differential equation</summary>

Solve for $b$ first, then multiply the equation for $a$ by $e^t$.
Add the original equations before choosing a representation. To test a
different representation, find two states it identifies and compare their
represented derivatives. For reconstruction, insert and subtract
$LR(x_n)$. For the display, specify the Lipschitz constant of multiplication
by $100$.

</details>

<details markdown="1">
<summary>Worked solution: an exact quotient with a nonzero reconstruction cost</summary>

Integrating $b'=-2b$ gives $b(t)=e^{-2t}b_0$. Next,
$(e^t a)'=e^{-t}b_0$, so

$$
\begin{pmatrix}a(t)\\b(t)\end{pmatrix}
=\Phi_t\begin{pmatrix}a_0\\b_0\end{pmatrix},\qquad
\Phi_t=
\begin{pmatrix}e^{-t}&e^{-t}-e^{-2t}\\0&e^{-2t}\end{pmatrix}.
$$

The diagonal entries multiply correctly. The upper-right entry of
$\Phi_t\Phi_s$ is
$e^{-t}(e^{-s}-e^{-2s})+(e^{-t}-e^{-2t})e^{-2s}
=e^{-(t+s)}-e^{-2(t+s)}$. This proves $\Phi_t\Phi_s=\Phi_{t+s}$.
The generator is

$$
\mathcal LF=(-a+b)\partial_aF-2b\partial_bF,
\qquad \mathcal L(a+b)=-(a+b),\quad
\mathcal L(a^2)=-2a^2+2ab.
$$

Take $R(a,b)=a+b$, with exact scalar evolution $\Psi_t(r)=e^{-t}r$.
The matrix formula gives $R\Phi_t=e^{-t}R$ for all states. The total
therefore closes exactly. Recording only $a$ would not: states $(0,0)$
and $(0,1)$ have the same recorded value and different values of $a(t)$
for $t>0$.

At the instrument times,

$$
x_n=(2^{-n}-4^{-n},4^{-n}),\qquad r_n=2^{-n}.
$$

The computed update $S(y)=0.51y$ is globally $0.51$-Lipschitz.
Its transfer defect at a general state is
$D_R(x)=R\Phi_\tau(x)-S(Rx)=-0.01R(x)$. On this trajectory its
size is $0.01\,2^{-n}$. With $e_n=|r_n-y_n|$ and $e_0=0$,

$$
e_{n+1}\le0.51e_n+0.01\,2^{-n},\qquad
e_n\le0.01\sum_{j=0}^{n-1}0.51^{n-1-j}0.5^j
=0.51^n-0.5^n.
$$

The last quantity is also the exact error, since $y_n\ge r_n$.
Set $b_n=4^{-n}$. The full-state difference is
$x_n-Ly_n=(-e_n-b_n,b_n)$, hence

$$
|x_n-Ly_n|_2=\sqrt{(e_n+b_n)^2+b_n^2}
\le e_n+\sqrt2\,b_n.
$$

The term $\sqrt2 b_n=|x_n-LR x_n|_2$ is reconstruction loss;
the term $e_n$ is model evolution error, converted through a map of
Lipschitz constant one. At $n=4$, $e_4=0.00515201$ and
$b_4=0.00390625$. The bound is about $0.0106763<0.011$, so it
certifies the tolerance. An exact multiplier removes $e_n$ but leaves
$\sqrt2\,4^{-n}$ at every finite step. That loss could instead be
removed by retaining the missing coefficient and evolving it correctly.

Finally choose $P(r)=100r$. The displayed approximate update is
$H(z)=0.51z$, and $PS=HP$ exactly. The second transfer defect is
zero, but $P$ has Lipschitz constant $100$. The first defect and the
accumulated retained-state error are both multiplied by $100$. At step
four the displayed error is $0.515201$. Its larger numerical value
reflects the specified measurement, and must be compared with a tolerance
in the same units.

</details>

Before moving on, write a five-sentence certificate naming the detailed
evolution, the retained evolution, the reconstruction, the norm and finite
time index, and the resulting error. It should distinguish the exact
quotient from the approximate update and the incomplete reconstruction.
Those are three independent claims.

<span id="assessment-b"></span>

## Assessment B: one fluid, three descriptions

The next five tasks transfer the same reasoning to a velocity field.
Spatial derivatives give some discarded information a much greater cost
than its velocity amplitude suggests. This assessment also tests whether
you can distinguish an upper bound that is inconclusive from a lower
bound that proves failure.

## The common problem

On the fixed periodic box $\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3$, take fixed viscosity $\nu>0$, zero force, and

$$
u_0(x,y,z)=\left(\sin y+\frac12\sin(8y)\right)e_1,
\qquad e_1=(1,0,0).
$$

Compare three descriptions: the exact velocity field, an exact description retaining only frequency one, and a forward Euler approximation to that retained description. Use the **averaged** norm

$$
\|v\|_{2,\mathrm{av}}^2=(2\pi)^{-3}\int_{\mathbb T^3}|v|^2.
$$

You may use orthogonality: the average of $\sin^2(ny)$ is $1/2$, and the average of $\sin(ny)\sin(my)$ is zero for distinct positive integers $n,m$. The corresponding cosine identities also hold. No general Fourier convergence theorem is needed for this finite sum.

## 1. Choose the state and the measurement

Use fields of the form $u_{a,b}=(a\sin y+b\sin8y)e_1$. Choose a state space and initial state that retain both waves. Calculate the two observables

$$
E_{\mathrm{av}}(a,b)=\frac12\|u_{a,b}\|_{2,\mathrm{av}}^2,
\qquad H(a,b)=\|\nabla u_{a,b}\|_{2,\mathrm{av}}^2.
$$

If you discard the frequency-eight component initially, what fraction of each observable is lost? Does a good approximation to one automatically give a good approximation to the other?

<details markdown="1">
<summary>Hint: keep the frequency when differentiating</summary>

The state can be a pair of coefficients. Expand each square, eliminate the cross term by orthogonality, and remember that $\partial_y\sin(8y)=8\cos(8y)$. A lost fraction is the omitted contribution divided by the original total.

</details>

<details markdown="1">
<summary>Worked solution: the same omission has two different costs</summary>

Choose $X=\mathbb R^2$, with state $(a,b)$ and initial state $(1,1/2)$. The map $(a,b)\mapsto u_{a,b}$ reconstructs its velocity field. Orthogonality gives

$$
E_{\mathrm{av}}=\frac{a^2+b^2}{4},
\qquad H=\frac{a^2+64b^2}{2}.
$$

At the initial state, $E_{\mathrm{av}}=5/16$ and $H=17/2$. Dropping $b$ loses $1/16$ of energy, a fraction $1/5$, but loses $8$ from $H$, a fraction $16/17$. A fifth of the energy carries almost all the squared gradient norm in this example.

The coefficients form the state; either scalar formula is an observable. Changing the observable changes which discarded information matters. An error statement must name its measurement.

</details>

## 2. Solve the evolution and recover its generator

Verify zero divergence and compute $(u\cdot\nabla)u$ for this whole family. Find the unforced solution with $p=0$, and write its time-$t$ transformation $T_t(a,b)$. Check $T_{t+s}=T_t\circ T_s$.

For a differentiable observable $F(a,b)$, calculate the generator $\mathcal L F$. Apply it to $E_{\mathrm{av}}$ and check the energy law. Finally compute the exact finite energy change $\Delta_{T_t}E_{\mathrm{av}}$. Can the current energy alone determine its own instantaneous rate?

<details markdown="1">
<summary>Hint: distinguish spatial motion from coefficient motion</summary>

The velocity points in the $x$-direction, but its coefficients depend only on time and its sine waves only on $y$. First check the spatial PDE. Then differentiate $F(T_t(a,b))$ with respect to time at zero. Compare the states $(1,0)$ and $(0,1)$ when testing whether energy determines its rate.

</details>

<details markdown="1">
<summary>Worked solution: an exact PDE inside a two-dimensional state space</summary>

The only nonzero velocity component is independent of $x$, so both divergence and advection vanish. The two Laplacians are $\Delta(\sin y)=-\sin y$ and $\Delta(\sin8y)=-64\sin8y$. The full equation therefore reduces to

$$
a'=-\nu a,\qquad b'=-64\nu b,
\qquad T_t(a,b)=(e^{-\nu t}a,e^{-64\nu t}b).
$$

Exponential multiplication proves the composition law. In particular,

$$
u(t)=\left(e^{-\nu t}\sin y+\frac12e^{-64\nu t}\sin8y\right)e_1.
$$

The generator acts on observables by

$$
\mathcal L F=-\nu a\,\partial_aF-64\nu b\,\partial_bF,
\qquad \mathcal L E_{\mathrm{av}}=-\frac\nu2(a^2+64b^2)=-\nu H.
$$

This is exactly the unforced energy law in the averaged convention. The finite change is

$$
\Delta_{T_t}E_{\mathrm{av}}
=\frac14\left[(e^{-2\nu t}-1)a^2+(e^{-128\nu t}-1)b^2\right].
$$

Dividing by $t$ and taking $t\to0$ recovers the generator. The states $(1,0)$ and $(0,1)$ have equal energy $1/4$, but energy rates $-\nu/2$ and $-32\nu$. Recording energy alone loses the information needed to predict its next change.

This solves the full PDE for this family because its spatial terms were checked. The special cancellation of advection is also why the example has no nonlinear exchange between frequencies.

</details>

## 3. Separate transfer error from reconstruction error

Let $R(a,b)=a$ retain frequency one, and evolve the retained coefficient by $S_t(a)=e^{-\nu t}a$. Calculate the transfer defect

$$
D_R(a,b)=R(T_t(a,b))-S_t(R(a,b)).
$$

Reconstruct the retained state as $\widetilde u(t)=e^{-\nu t}\sin y\,e_1$. Calculate both $\|u(t)-\widetilde u(t)\|_{2,\mathrm{av}}$ and $\|\nabla(u(t)-\widetilde u(t))\|_\infty$. Explain how a zero transfer defect can coexist with these errors.

At one fixed instant, change amplitude and length scales by $U(x)=2u(t,5x)$ and $\widetilde U(x)=2\widetilde u(t,5x)$, on the corresponding periodic box of side $2\pi/5$. Convert both error bounds, using the averaged norm on that box.

<details markdown="1">
<summary>Hint: ask which space contains each difference</summary>

The transfer defect compares two scalar retained coefficients. The reconstruction error compares full velocity fields. For the last calculation, a derivative gains the factor $2\cdot5$. In an averaged integral, the rescaled volume appears in both the integral and its normalization.

</details>

<details markdown="1">
<summary>Worked solution: exact retained dynamics still discard a wave</summary>

Both routes give $e^{-\nu t}a$, so $D_R=0$. But

$$
u(t)-\widetilde u(t)=\frac12e^{-64\nu t}\sin8y\,e_1,
$$

and hence

$$
\|u-\widetilde u\|_{2,\mathrm{av}}=\frac{e^{-64\nu t}}{2\sqrt2},
\qquad \|\nabla(u-\widetilde u)\|_\infty=4e^{-64\nu t}.
$$

The retained coefficient is predicted exactly. The omitted component remains absent from the reconstruction. These are different comparisons, so their error statements do not conflict.

On the rescaled box, the averaged velocity error gains a factor of $2$, and the gradient error gains a factor of $10$:

$$
\|U-\widetilde U\|_{2,\mathrm{av}}=\frac{e^{-64\nu t}}{\sqrt2},
\qquad \|\nabla(U-\widetilde U)\|_\infty=40e^{-64\nu t}.
$$

The factor $5^{-3}$ from volume cancels its counterpart in the average. It would remain in an unnormalized squared integral. This calculation rescales the fields at a fixed instant; an evolution rescaling would also have to transform time and viscosity.

</details>

## 4. Accumulate the error of a time step

Now approximate only the retained coefficient by forward Euler:

$$
c_0=1,\qquad c_{j+1}=(1-\nu\tau)c_j,
\qquad t_j=j\tau,
$$

with $0<\nu\tau\le1$. Show that this step is nonexpanding and preserves a nonnegative coefficient. Bound the one-step defect using

$$
0\le e^{-r}-(1-r)
=\int_0^r(r-s)e^{-s}\,ds\le\frac{r^2}{2},\qquad r\ge0.
$$

Derive an accumulated error bound for $\eta_j=|e^{-\nu t_j}-c_j|$, starting from $\eta_0=0$. Then bound the full field error of $u^{\mathrm E}_m=c_m\sin y\,e_1$ at $t=m\tau$, retaining the omitted wave from Task 3.

Make two accuracy decisions with $\nu=1$. At $t=1$ and $\tau=0.1$, does your bound certify averaged $L^2$ error at most $0.04$? If the tolerance is tightened to $0.02$, check the exact Euler coefficient as well: does an inconclusive bound mean the approximation is inaccurate? At the earlier time $t=1/64$, could any number of time steps make the frequency-one reconstruction accurate to $0.1$?

If you also retain frequency eight, what stronger step condition makes *both* Euler multipliers nonnegative and nonexpanding? State separately the weaker condition for nonexpansion alone.

<details markdown="1">
<summary>Hint: apply the defect at the exact state</summary>

The exact retained coefficient at step $j$ is $e^{-\nu t_j}\le1$. Use the recurrence from [composition and error](composition.md): propagated old error plus new defect. For the final field comparison, its frequency-one error and omitted frequency-eight wave are orthogonal, so their squared norms add. To check the sharper tolerance, compute $c_{10}=(1-0.1)^{10}$ directly instead of substituting an upper bound for its error.

</details>

<details markdown="1">
<summary>Worked solution: temporal refinement has a spatial error floor</summary>

Write $q=1-\nu\tau$. The assumption gives $0\le q<1$, so $|qc-qd|\le|c-d|$, and $c\ge0$ implies $qc\ge0$. At the exact state, the new scalar defect is bounded by $(\nu\tau)^2/2$. Therefore

$$
\eta_{j+1}\le q\eta_j+\frac{\nu^2\tau^2}{2},
\qquad
\eta_m\le\frac{m\nu^2\tau^2}{2}
=\frac{\nu^2t\tau}{2}.
$$

We used $q\le1$; retaining its powers would give a sharper bound. The exact expression is $c_m=(1-\nu\tau)^m$, which provides a separate check.

The full field difference has two orthogonal parts:

$$
u(t)-u^{\mathrm E}_m
=(e^{-\nu t}-c_m)\sin y\,e_1
+\frac12e^{-64\nu t}\sin8y\,e_1.
$$

Consequently,

$$
\boxed{\|u(t)-u^{\mathrm E}_m\|_{2,\mathrm{av}}
\le\frac1{\sqrt2}
\sqrt{\left(\frac{\nu^2t\tau}{2}\right)^2
+\frac14e^{-128\nu t}}.}
$$

At fixed finite $t>0$, take $\tau=t/m\to0$. The time error tends to zero, but the full error tends to the positive omitted-wave norm $e^{-64\nu t}/(2\sqrt2)$. More time steps cannot recover a discarded frequency.

For $\nu=t=1$ and $\tau=0.1$, the bound is

$$
\frac1{\sqrt2}\sqrt{0.05^2+\frac14e^{-128}}
\approx0.03536<0.04,
$$

so it certifies the first tolerance. This bound does not certify $0.02$, but that is not a proof of failure. The exact coefficient $c_{10}=0.9^{10}\approx0.34867844$ gives

$$
\|u(1)-u^{\mathrm E}_{10}\|_{2,\mathrm{av}}
=\frac1{\sqrt2}\sqrt{(e^{-1}-0.9^{10})^2+\frac14e^{-128}}
\approx0.01358<0.02.
$$

Here the exact calculation proves more than the convenient general bound. At $t=1/64$, however, the omitted-wave norm is $e^{-1}/(2\sqrt2)\approx0.1301>0.1$. Orthogonality makes this a **lower** bound for the full error, whatever the retained coefficient is. That proves the early-time tolerance cannot be met with this representation. Keep these outcomes separate: a certified tolerance, an inconclusive upper bound, and a lower bound proving failure.

Retaining frequency eight adds the multiplier $1-64\nu\tau$. Both multipliers lie in $[0,1]$ when $64\nu\tau\le1$. Nonexpansion alone requires their absolute values to be at most one, giving $64\nu\tau\le2$. At the latter boundary the high mode alternates sign without damping; stability is weaker than accuracy. With both waves retained, the same defect argument applies separately at rates $\nu$ and $64\nu$, and gives convergence to this exact solution on every fixed finite interval as $\tau\to0$.

</details>

## 5. State exactly what has been proved

Evaluate these three conclusions, and replace each incorrect one with a statement justified by your calculations.

1. “The retained evolution has zero transfer defect, so the reconstructed field is exact.”
2. “Euler converges as the step tends to zero, so keeping frequency one is enough to recover the whole velocity at any fixed positive time.”
3. “The exact solutions $v_N(t)=e^{-\nu N^2t}\sin(Ny)e_1$ have unbounded initial gradients as $N\to\infty$, so one of them has a finite-time singularity.”

Then write a short claim card for what the workshop actually establishes: equation and domain, initial datum, observable and norm, time and step conditions, error bound, and scope. Explain what would have to change before the work addressed arbitrary smooth three-dimensional data or smoothly forced breakdown.

<details markdown="1">
<summary>Hint: write out the quantities and quantifiers</summary>

For 1, specify whether the comparison takes place before or after reconstruction. For 2, keep the nonzero term in the boxed bound. For 3, compute the gradient for each fixed $N$ before taking a limit across different initial data. None of those fields needs a force.

</details>

<details markdown="1">
<summary>Worked solution: a complete special case with explicit limits</summary>

**1.** The retained coefficient is exact; the reconstructed field omits a wave with a known norm. Zero transfer defect proves agreement after representation.

**2.** With frequency one fixed, Euler converges to the exact *retained* evolution. Recovering this full initial datum additionally requires retaining frequency eight. In general, spatial and temporal approximation need separate estimates.

**3.** For each fixed positive integer $N$,

$$
\|\nabla v_N(t)\|_\infty=Ne^{-\nu N^2t},
$$

which is finite and decreases for every $t\ge0$. The divergence of the initial gradients across a family changes the datum each time. It is not divergence along a single trajectory at a terminal time.

A suitable claim card reads:

> On the fixed $2\pi$-periodic box, the specified two-wave datum has the displayed global smooth unforced NS solution at each fixed $\nu>0$, with $p=0$. Its frequency-one representation commutes exactly with evolution. Forward Euler with $0<\nu\tau\le1$ has retained-coefficient error at most $\nu^2t\tau/2$ at $t=m\tau$. The full averaged $L^2$ reconstruction error obeys the boxed bound, including its spatial tail. These conclusions apply to the stated shear family.

General three-dimensional data need control of nonlinear transfer and pressure, which this shear cancels. A singularity construction must concern one admissible datum and one finite terminal time; a smoothly forced construction must also prove the complete force remains smooth through that time. This workshop establishes neither target. The external forced result is studied separately in [the published-proof chapter](published-proof.md); it does not change what this particular shear calculation proves.

</details>

The resulting calculation is the course method in use: the representation, evolution, measurement and error bound are all explicit. The remaining sections explain how to apply the same discipline when a source proof is too long to reproduce inside a lesson.

## A research claim card

Before working on a new estimate, write its equation and domain, solution class, time interval, observable, normalization, constants and their dependencies. State the genuinely new input, the countermodels that satisfy its hypotheses, and the exact implication it would have for the target. End with the weakest unresolved inequality.

For an approximate construction, give the full PDE residual and a strong-norm stability estimate. If errors propagate by $e_{j+1}\le L_je_j+d_j$, track the products of $L_j$ as well as the defects $d_j$. Small local defects need not remain small after many stages.

## Reproduce this edition

Clone the repository, retain its recorded research environment, and consult the source notes before running mathematical instruments. The website itself needs only Python and the pinned Markdown package:

```sh
python -m pip install -r notes/requirements.txt
python scripts/build_notes.py
python -m http.server 8000 --directory notes/_site
```

The builder emits the learning notes, chapter Markdown, a claim index in JSON, and copies of the referenced research sources. It checks local links and recorded source hashes. Open the local address above to read the generated edition.

Each theorem's source note links its focused instrument, test, and receipt. Test success checks the implemented pins; it does not replace reading the analytic estimates. No new DNS is needed for these chapters.

## Local formalization gap ledger

This table concerns the repository's original research modules. It does not
describe the external formalization linked by the OpenAI release. Consult
[the published-proof chapter](published-proof.md) for that separate work
and the distinction between a linked certificate and a local replay.

| Layer | What this edition has | What must be added before a stronger claim |
|---|---|---|
| Cone algebra | Lean-checked basis inverse, conjugacy, inward margins, and conditional expansion coefficient. | ODE existence/invariance, coefficient correspondence, and the return-map argument. |
| Local PDE estimates | Restricted written classical proofs. | Formal function spaces, existence/continuation imports, and all analytic dependencies. |
| Oblique polarization | A restricted written theorem on actual compact Euler profiles. | Formalize its geometric hypotheses, ODE comparison, and return-map argument. |
| Finite supplied-seed amplification | Restricted written full-NS theorem; gain and absolute-target exclusion proved together. | Formalize localization, viscous comparison, nonlinear continuation, and all norm conversions. |
| Strain handover | Restricted reviewed log-log theorem for a family of smooth solutions with supplied seeds. | Formalize mean and harmonic residuals, uniform interpolation, and strong continuation; establish any next-stage transfer separately. |
| Outgoing-wave amplifier | Restricted exact viscous linearized gain with a late-specified finer seed. | Formalize that theorem; the later original-time construction below supplies a particular mixed seed by an additional argument. |
| Original-time handover and growing windows | Restricted reviewed written proofs for changing initial data, with both seeds supplied initially; explicit growing windows require the stated fixed Gevrey profile. | Formalize the analytic dependencies and preserve every datum and profile restriction. Finite-window tracking alone does not give a terminal trajectory. |
| Subsequent coupling and infinite iteration in our construction | Not established by the local finite theorems. | Compatible stage inputs, a uniform depth/scale argument and the appropriate terminal limit. |
| Local unforced ROOT | OPEN. | A complete theorem for the original unforced target. |
| Independent local forced construction | Not completed by our finite-stage calculations. | A complete admissible terminal construction. The external C/D result is credited and analyzed separately. |

**Formal coverage is partial and explicit.** The original [cone algebra source](../../formalization/oblique_cone/NSEObliqueCone428.lean) compiled with Lean 4.28.0 against the pinned Mathlib cache. Lean’s bundled checker also replayed the new module’s declarations. The five principal declarations use `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx`; the [receipt](../../formalization/oblique_cone/receipt.json) records the exact environment and scope. A fresh replay of the entire imported closure timed out and is not claimed.

The checked statements cover the basis inverse and matrix conjugacy, inward slope margins of $23/48$ under entrywise errors at most $1/12$, and the conditional expansion coefficient $13/24$. They do not formalize the ODE invariance, Gavrilov geometry, or NS dynamics. The [integration audit](../../references/navier-stokes/fluid-lean-integration.md) distinguishes this original certificate from the imported `fluid_lean` work on forced inviscid equations. These particular local modules are not a Lean-certified NS theorem.

## From an assessment to a terminal theorem

A blow-up construction must produce one smooth initial datum, one positive viscosity, and one finite terminal time with a proved limit and diverging continuation norm. Different regular solutions with successively larger peaks do not meet that statement. A regularity proof must cover all admissible data, or prove that every hypothetical singularity belongs to its excluded class. A restricted packet theorem supplies neither coverage automatically.

Apply the same distinctions when reading the external proof: identify its
actual terminal construction, force class and limiting argument. Use
[Residuals and smooth forcing](residuals.md) to practice the derivative
accounting, [Iteration and limits](iteration.md) to test compatibility,
and [the published-proof chapter](published-proof.md) to study how the
released construction discharges its own obligations. A common vocabulary
helps compare methods; it does not make separate proofs logically depend
on one another.

The [next-transfer research appendix](../../references/navier-stokes/next-transfer-review.md)
records the current drafts and the stated scope of their reviews. AI review
is not external expert acceptance or proof certification.
It records the finite original-time construction, its
[later logarithmic extension](../../references/navier-stokes/logarithmic-host.md)
and subsequent scoped advances. Check the latest reviewed statement before
assigning a new task; historical unresolved questions may have been answered
in later notes. Inclusion in a source snapshot alone does not promote a
draft to a registered theorem.

Source: [Research strategy, §§4 and 8](../../references/navier-stokes/research-strategy.md), [current status](../../docs/STATUS.md), and [claim register](../claims.md).
