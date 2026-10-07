# Concentration and the time budget

Two shears with the same amplitude have the same energy, even when one varies much faster in space. We saw in [the fluid equation](equation.md) that their gradients differ by the frequency ratio. Now keep the frequencies in roughly the same band and change something else: use many waves, sharing the same total averaged size. Can their derivatives add at one point strongly enough to produce an additional gain?

We will first calculate that spatial gain. Then we will ask how long the resulting strain can act. Fourier orthogonality from [composition](composition.md), norm scaling from [scale and resolution](scaling.md), and integration by parts are enough to follow the main calculations.

## Work a scalar example first

Choose distinct positive integers $n_1,\ldots,n_m$ between $L$ and $2L$, and define a real periodic function

$$
\phi(x)=a\sqrt{\frac2m}\sum_{j=1}^m\sin(n_jx),\qquad a>0.
$$

The coefficient decreases like $m^{-1/2}$ as we add waves. Predict what this does to two measurements: the integral of the square, and the derivative at zero. In the integral, distinct sine functions are orthogonal and each has averaged square $1/2$. Consequently

$$
\frac1{2\pi}\int_0^{2\pi}|\phi|^2\,dx
=\frac{2a^2}{m}\frac m2=a^2.
$$

At the origin, however, all derivatives add positively:

$$
\phi'(0)=a\sqrt{\frac2m}\sum_{j=1}^m n_j,
\qquad
\sqrt2\,aL\sqrt m\le\phi'(0)\le2\sqrt2\,aL\sqrt m.
$$

The averaged size stays $a$, while the derivative gains a factor of order $\sqrt m$. We call this addition **coherence**: selected contributions have the same sign or direction at the measurement point. Orthogonality concerns a spatial average, so it is entirely compatible with coherence at one point. Reversing a sine's sign leaves the averaged square unchanged but reverses its contribution to $\phi'(0)$.

The chosen one-dimensional band has only order $L$ available frequencies. To use order $L^3$ modes, we must pass to three dimensions and arrange the vector coefficients to satisfy incompressibility.

## Where the extra power comes from

Now let $M$ count the nonzero complex Fourier coefficients of a vector field, including both signs of each wavevector. Each sine in the scalar example contributes two such coefficients. Cauchy–Schwarz gives

$$
\sum_k|\widehat U_0(k)|
\le\sqrt M\left(\sum_k|\widehat U_0(k)|^2\right)^{1/2}
=a\sqrt M,\qquad \|U_0\|_{2,\mathrm{av}}=a.
$$

In the vector construction, $L$ denotes the upper frequency cutoff; the scalar example used the interval $[L,2L]$. Differentiation now adds at most $L$, giving a gradient upper bound $La\sqrt M$. A three-dimensional band of fixed relative width contains order $L^3$ lattice frequencies, suggesting the size $aL^{5/2}$: one power from differentiation and three halves from the square root of the mode count.

Attaining that size requires the phases and vector directions to add in the desired component. Each coefficient must also be perpendicular to its wavevector. The [concentrated-packet construction](../../references/navier-stokes/concentrated-packet.md) makes these choices explicitly, verifies the norm, and obtains

$$
\nabla U_0(0)=\operatorname{diag}(-\sigma,\sigma,0),
\qquad \frac{aL^{5/2}}{18}\le\sigma\le L\overline W.
$$

Here $\overline W=a\sqrt M$ bounds the construction's Wiener norm, the sum of its Fourier amplitudes. The displayed matrix has trace zero, as incompressibility requires: compression along one axis balances stretching along another. This is initially a statement at one point. The source also follows the true NS evolution and shows how long this geometry persists in a neighborhood carried by the fluid.

## Compare two actual evolutions

To turn strain into a statement about evolution, compare two solutions. Let $U$ be the smooth reference solution and write the perturbed solution as $u=U+w$. The initial difference is divergence-free and small in $L^2$. Both fields solve unforced NS on the same periodic box with the same viscosity. We first calculate while both are smooth; the weak–strong version described below extends the estimate to rougher perturbed solutions. Subtract the equations and write $\pi$ for the pressure difference:

$$
\partial_t w+(U\cdot\nabla)w+(w\cdot\nabla)U
 +(w\cdot\nabla)w+\nabla\pi=\nu\Delta w,
\qquad \nabla\cdot w=0.
$$

For this derivation, $\|w\|_2^2=\int|w|^2$ is the ordinary, unnormalized spatial integral. The averaged norm obeys the same growth factor because its normalization is a fixed constant. Multiply the difference equation by $w$ and integrate. The two transport terms with $w$ as the transported field vanish by incompressibility and periodicity, as does the pressure term. In the remaining quadratic form, the antisymmetric part of $\nabla U$ contributes zero. Thus

$$
\frac12\frac{d}{dt}\|w\|_2^2+\nu\|\nabla w\|_2^2
=-\int w^TS(U)w
\le\|S(U)\|_{\mathrm{op},\infty}\|w\|_2^2.
$$

Write $K(t)=\|S(U(t))\|_{\mathrm{op},\infty}$, the largest absolute eigenvalue of the reference strain, maximized over space. Dropping the nonnegative dissipation term and applying an integrating factor gives

$$
\|w(t)\|_2^2\le\|w(0)\|_2^2
\exp\left(2\int_0^t K(s)\,ds\right).
$$

Equivalently, and without squaring the norm,
$$
\|w(t)\|_2\le\|w(0)\|_2
\exp\left(\int_0^t K(s)\,ds\right).
$$

The quantity $\int_0^tK(s)\,ds$ is **accumulated strain**. It is dimensionless: a rate has been integrated over time. A constant rate $K=100$ acting for time $1/100$ gives the same upper growth factor $e$ as $K=1$ acting for time one. Increasing the instantaneous rate helps only to the extent that the flow sustains it.

To see what information the upper bound has lost, return to the constructed matrix. At a point where
$S(U)=\operatorname{diag}(-\sigma,\sigma,0)$, the exact integrand is
$-w^TS(U)w=\sigma w_1^2-\sigma w_2^2$. Its sign depends on the perturbation's direction. Replacing it by $K|w|^2$ is useful for an error bound, but loses the information needed to prove amplification.

The source proves the same relative-energy inequality for a Leray–Hopf weak solution compared with the smooth reference $U$. This permits arbitrary divergence-free $L^2$-small perturbations without assuming their smoothness persists. Throughout, $U$ is a separately specified solution; it has its own nonlinear evolution and frequencies.

With additional frequency-separation and seed-size hypotheses, the source uses this bound to exclude its specified distant high-pass activation during $0\le t\le1/(6L\overline W)$. That conclusion includes the generated modes and feedback. The short accumulated clock is what makes the estimate useful despite the large initial strain.

## Worked example: turn the clock into an error certificate

For the constructed background, the source bounds the accumulated strain by

$$
\int_0^t K(s)\,ds\le\frac{z}{1-3z},
\qquad z=L\overline Wt,\quad 0\le z<\frac13.
$$

At $t=1/(6L\overline W)$, the dimensionless time is $z=1/6$, so the clock is at most $1/3$. An initial error of norm $10^{-3}$ therefore obeys

$$
\|w(t)\|_2\le10^{-3}e^{1/3}<1.396\times10^{-3}.
$$

Thus the difference cannot reach $2\times10^{-3}$ within this window, whether it grows or decays. To measure the high-frequency part of the total velocity $u=U+w$, we must add the reference field's contribution. Exercise 3 carries out that last step.

This window should not be confused with the shorter material-ball result. The source proves its specific persistent strain directions for $z\le1/512$, with an additional Reynolds condition; that interval has clock at most $1/509$. A proof that a background exists, an estimate for a perturbation, and persistence of a particular geometry can have different time intervals.

## Exercises

### 1. Count the waves, then check their signs

For a positive integer $L$, compare $\phi_\pm(x)=\sin(2Lx)\pm2\sin(Lx)$. Calculate their averaged squared norms and their derivatives at zero. Does the number of waves and the averaged norm determine the derivative there?

<details markdown="1"><summary>Hint</summary>

Orthogonality removes the sign from the integral of the square. Differentiation at zero retains it.

</details>

<details markdown="1"><summary>Solution</summary>

Both averaged squared norms equal $(1+4)/2=5/2$. But $\phi_+'(0)=4L$, while $\phi_-'(0)=0$. The same frequencies and averaged size can give different pointwise derivatives. A concentration lower bound must establish constructive addition in the component being measured.

</details>

### 2. Strain times lifetime

If strain has size $aL^{5/2}$ and the controlled lifetime has size $1/(aL^{5/2})$, does increasing $L$ alone make the integrated strain arbitrarily large?

<details markdown="1"><summary>Hint</summary>

In the error estimate, a constant rate $K$ enters through $Kt$, not through $K$ alone.

</details>

<details markdown="1"><summary>Solution</summary>

No. Their product has order one. Large strain over a correspondingly short interval does not by itself produce an unbounded Gronwall exponent. A longer-lived reference or a sharper dynamical mechanism is needed.

</details>

### 3. Include the background in the measured output

At a specified time, suppose $\int_0^t K\le1/3$, $\|w(0)\|_2\le10^{-3}$, and the background has high-pass norm $\|P_{>R}U(t)\|_2\le2\times10^{-4}$. Here $P_{>R}$ keeps only Fourier modes with frequency above $R$; orthogonality makes it an $L^2$ contraction. Prove or reject the certificate $\|P_{>R}u(t)\|_2<0.002$. What breaks if the background bound is omitted?

<details markdown="1"><summary>Hint</summary>

Apply the projection to $u=U+w$, then use the triangle inequality. A bound on the difference $w$ is not a bound on $u$ itself.

</details>

<details markdown="1"><summary>Solution</summary>

The hypotheses imply

$$
\|P_{>R}u(t)\|_2
\le\|P_{>R}U(t)\|_2+\|P_{>R}w(t)\|_2
\le0.0002+0.001e^{1/3}<0.001596<0.002.
$$

The certificate is valid. Without the first term's bound, the background alone could exceed the target. One cannot declare $P_{>R}U(t)=0$ merely because its initial datum used lower frequencies: nonlinear evolution can create new ones.

</details>

### 4. A finite sum of lifetimes is not a singular trajectory

For each $n$, suppose a separate smooth NS solution starts from a datum $U_{L_n}(0)$, where $L_n=2^n$, has strain of order $aL_n^{5/2}$, and is controlled for time $c/(aL_n^{5/2})$. Show that these durations have a finite sum. Does placing the intervals next to each other construct a solution with infinite strain before a finite time? State the missing mathematical requirements.

<details markdown="1"><summary>Hint</summary>

Sum a geometric series, then examine the velocity at a join. Compare the terminal state of one interval with the prescribed initial state of the next.

</details>

<details markdown="1"><summary>Solution</summary>

Starting from $n=1$, the sum is

$$
\frac ca\sum_{n=1}^\infty2^{-5n/2}
=\frac ca\frac{2^{-5/2}}{1-2^{-5/2}}<\infty.
$$

These are intervals belonging to different initial data. Their endpoint fields need not match, so concatenating them need not even give a continuous velocity. A single trajectory would require compatible endpoint states evolving from one smooth original datum, all intervening nonlinear interactions, and estimates valid on that same sequence. The stated strain sizes also supply no proof of increasing strain along such a trajectory. Adding a force to perform the joins would require its complete smoothness budget through the proposed accumulation time.

</details>

## Further reading

Peter Woit's [Fourier analysis course notes at Columbia](https://www.math.columbia.edu/~woit/fourier-analysis-2019/) give a route from orthogonality and Fourier series to the analytic tools used here. While reading, distinguish identities about spatial averages from estimates at one point.

For the fluid energy method, see Majda and Bertozzi's [*Vorticity and Incompressible Flow*, Chapter 3](https://www.cambridge.org/core/books/abs/vorticity-and-incompressible-flow/energy-methods-for-the-euler-and-the-navierstokes-equations/E5489F542D15DFDC03F96046A8E05265). The relative-energy calculation above is part of this classical method; the selected Fourier packet and its explicit persistence interval are the project-specific construction.

Full construction, constants, material-ball estimates, and seed hypotheses: [the concentrated-packet note](../../references/navier-stokes/concentrated-packet.md). The [registered claim](../claims.md#nse-concentrated-packet-local) records its precise scope. Continue to [a steady reference flow](steady.md) to seek a longer comparison interval.
