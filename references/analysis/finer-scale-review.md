# Independent review of the fixed finer-power Fourier-tail consequence

8 September 2026. **PASS as a consequence of the reviewed fixed finite-depth
construction and its stated upstream analytic estimates.** This is a separate
AI-agent mathematical review. It is not a full formal PDE certificate,
external expert acceptance, or a solution of ROOT, `(E′)` or FORCED-D.
No DNS was used and the reviewer did not edit the source.

Reviewed source: section 8 of
[the finite-depth profile note](finite-depth-profile.md),
including its dependence on sections 1–7. Exact source SHA-256:

```text
8496abb26b5247a7afed95a16b9237ff07f153956231e255fe56fa6d58dd2615
```

The [earlier independent review](finite-depth-profile-review.md)
checks the recurrence and original-data compatibility. The present review
independently checks the additional high-derivative accounting, Fourier
normalization, projection of the actual error and order of choices. It does
not claim a new independent derivation of every upstream first-stage estimate.

## 1. The statement and its quantifiers

For every fixed eta>0, beta>3/2 and P>0, the source claims

```text
sup_[0,t_eta] ||grad P_(>h^(-beta)) Q_h||infinity <= h^P
```

for sufficiently small h, with its threshold allowed to depend on all three
parameters. The family Q_h has the same original datum for every choice of
proof indices; that datum still varies with h. The sufficient correction
depth J and derivative order r are finite and fixed before taking the limit.

This is a valid superalgebraic tail statement if the displayed proof closes:
the phrase means that each fixed power P has its own estimate and threshold.
It does not require a bound uniform in P, a convergent infinite correction
series, or one approximation of infinite depth. Conversely it supplies none
of those stronger conclusions.

## 2. Finite high-order construction without changing the datum

The source enlarges the terminal finite spatial/phase order to
max(30,r+4), retaining eight further orders for each earlier correction
round. This supplies the derivatives of evaluated profiles, their curl
lifts, and the Sobolev bounds used below. Only finitely many profile norms
are used for fixed r and J. A smooth fixed F has each required finite
Fourier A_M norm, although no uniform estimate in M is asserted.

The same actual first-stage q can be controlled with a larger fixed
background Sobolev index M. Its scaled C^r comparison retains a positive
power when M>4(N+4+3/2), as specified in the source. Increasing this proof
index does not alter the initial datum or define a new background flow.
The q gradient clock is O_eta(ell^(9/8)), so each fixed high-order energy
constant contributes exp(C_(r,eta) ell^(9/8))=h^(-o(1)). No high-order
norm is substituted for that sharp gradient clock in an exponential.

All corrections start at zero. Thus changing J changes U_J, the constructed
approximation, but not Q_h(0). Strong uniqueness identifies the actual
solutions on their common smooth intervals. The source's separate C1/H12
bootstrap supplies the full interval for a sufficiently large fixed J;
the Fourier-tail argument does not assume extra actual-Q derivatives in
order to prove that lifetime.

## 3. The H^r powers

The original primary packet has amplitude O(h/ell), volume O(h^(3/2))
and derivative cost h^(-1). Its H^r scale is therefore at most
h^(7/4-r) times a subpower factor. The fixed compact background contributes
a bounded norm. The actual-q H^r energy inequality then proves source (10)
with the already available q gradient clock.

For the receiving packet, amplitude k, volume d³ and derivative cost k^(-1)
give

```text
k^(1-r) d^(3/2) = h^(27/8-3r/2).
```

Higher derivatives of the phase do not upset this count. For a phase block
with j>=1 derivatives, the coefficient k^(-1) D^j S costs at most
k^(-1) h^(1-j) E. Relative to k^(-j), the ratio is
(k/h)^(j-1)=h^((j-1)/2), at most one. Slow amplitude derivatives cost
d^(-1), also smaller than k^(-1). Products of finitely many such factors
enlarge only E. The finite phase Fourier weights cover the corresponding
fixed powers of the mode number.

The means must use their global norms. Their stated size gives

```text
k rho d^(3/2-r) = h^(29/8-5r/4).
```

No compact volume is attributed to a mean tail in this calculation: this
factor follows from the scaled global Sobolev norm definition. Comparing
exponents with the receiving packet gives

```text
(7/4-r) - (27/8-3r/2) = r/2-13/8,
(29/8-5r/4) - (27/8-3r/2) = (r+1)/4.
```

Both are positive for r>=12. The bounded background is smaller as well.
This verifies source (11), including its r=12 value -117/8.

## 4. Uniform Fourier bounds on the expanding torus

Use frequencies k_n=n/L on the torus of side 2pi L, and coefficients
normalized by (2pi L)^(-3). Parseval then gives the factor
(2pi L)^(-3/2) multiplying the physical, unnormalized H^r norm in
Fourier Cauchy–Schwarz. For R>=1,

```text
||grad P_(>R) v||infinity
 <= (2pi L)^(-3/2)
    [sum_(|n/L|>R) |n/L|² (1+|n/L|²)^(-r)]^(1/2)
    ||v||H^r.
```

In the dyadic shell 2^j R<|n/L|<=2^(j+1)R, the number of lattice points
is at most C(L 2^j R)³ because LR>=1. The weighted sum is bounded by

```text
C_r L³ R^(5-2r) sum_(j>=0) 2^(j(5-2r)).
```

The series converges for r>5/2. The volume factor cancels L^(3/2) after
taking the square root. This proves (12) with constants independent of
L>=1. Fixed equivalence constants between the derivative and Fourier
definitions of H^r are harmless.

Using r=3 and including the low-frequency part also proves
||grad P_(>R)e||infinity <= C||e||H^3 uniformly in R>=1 and L>=1.
This is an absolute Fourier-sum estimate. It does not assume that a sharp
Fourier projection is bounded on L-infinity.

## 5. Actual error and the two fixed index choices

Applying (12) to U_J gives the exponent

```text
A_r(beta)=r(beta-3/2)+27/8-5beta/2.
```

For each fixed beta>3/2, its coefficient of r is strictly positive. A
finite r can therefore make A_r(beta)>P+2.

The actual-error L2 exponent before the clock loss is (29+2J)/8.
Interpolating with the separate H12 estimate, whose exponent is -117/8,
uses weights 3/4 and 1/4 for H3. It gives

```text
[(29+2J)/8](3/4) - (117/8)(1/4) = (3J-15)/16.
```

Relative energy pays I in L2 and the H12 energy inequality pays C12 I,
where I<=B eta ell²+o(ell²). Their interpolated leading loss is exactly
B eta(3+C12)/4. Thus any fixed larger C3 yields source (14). The
finite-order constants for constructing U_J remain subpower factors;
they do not multiply B eta ell² in the leading clock.

A sufficiently large fixed J makes this H3 exponent exceed P+2 and also
makes the source's C1 exponent (19J-17)/96-C_* eta strictly positive.
The latter is the independent strong-continuation condition. There is no
need to control the actual Q_h in H^r for the r chosen to estimate the
approximation tail; actual H12 and L2 error are sufficient.

After those choices, reduce h to absorb the subpower factors, fixed
constants and the sum of the two contributions. The triangle inequality
then proves the claimed h^P bound. Exact rational checks verified all the
displayed scale and interpolation exponents.

## 6. Boundaries that must accompany the corollary

At beta=3/2, A_r(beta)=-3/8 for every r. This argument cannot give the
same conclusion at the receiving wave's own power scale. It gives no
uniform bound as beta decreases to 3/2 and no assertion for beta(h),
eta(h), J(h) or r(h).

The estimate bounds the full generated tail through the specified finite
time, but does not make it identically zero. A sufficiently small tail
could require a separate later amplification analysis. The coarser envelope
source at h^(-5/4+o(1)) is outside the cutoff being excluded. The statement
therefore cannot replace a signed source calculation at that scale.

All estimates here use rescaled gradients and the stated expanding torus.
Physical gradients acquire the existing h^(-24) multiplier; a physical
comparison must convert both the cutoff and the norm. Since P is arbitrary,
one may choose a larger fixed rescaled power before such a conversion, but
this still concerns the same finite varying-data family.

The corollary passes at these quantifiers and with its reviewed finite-depth
prerequisites. It strengthens a frequency exclusion; it does not supply a
new seed, an infinite trajectory or a full Navier–Stokes solution.
