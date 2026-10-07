# Independent review of the non-effective diagonal window

8 September 2026. **PASS as a corollary of the cited fixed-parameter
analytic estimates, at the stated existential schedule and varying-data
scope.** No load-bearing mathematical flaw was found. This is a bounded
AI-agent review, not external expert acceptance, a formal PDE certificate,
or a fresh proof of every upstream construction. ROOT, E-prime and
FORCED-D remain OPEN. No DNS or canonical claim edits were performed.

Reviewed source:
[diagonal-window.md](diagonal-window.md),
SHA-256

```text
cbb40a0c45f15cfe88f8c2d4d8a4f75d7e768f41678c990ec34bed5f59909a85
```

The reviewer read its six pinned sources, including the full outgoing
central statement, its weighted pressure-corrected propagator, the
fixed-depth continuation and finer-tail steps, and the localized profile
identities needed for the central comparison. All six listed hashes
match the versions consulted. The source was not edited by this reviewer.

## 1. The indispensable fixed-parameter input is available

The original logarithmic-host theorem alone restricts eta to a small
fixed interval. Diagonalizing only that theorem would not allow eta to
diverge. The stronger input is sections 6 and 8 of the reviewed
[finite-depth note](finite-depth-profile.md): every fixed
eta>0 has a sufficiently large fixed finite depth J that closes the
actual C1/H12 bootstrap and the desired H3 error bound.

The approximation residual power is (29+2J)/8. Relative energy and
H12 interpolation give the stated C1 exponent (19J-17)/96; interpolation
to H3 gives (3J-15)/16. The losses C_* eta and C_3 eta come from the
leading sharp clock and the fixed H12 energy constant. They do not
inherit the higher derivative order used only to construct the
approximation. The source explicitly keeps B independent of J and eta;
all finite profile constants enter the fixed-parameter subpower factors.

Consequently, for each fixed n, one may first choose finite J_n and r_n
and then make every required error small by restricting h. This is the
correct sequence of choices. It assumes neither a uniform bound for the
profile constants nor an infinite correction expansion at one h.

The C1 estimate by itself in the source is primarily a gradient estimate.
The diagonal note correctly uses the inhomogeneous H3 error and uniform
embedding to obtain its full C1 norm, including the velocity value.
The higher profile corrections have both value and gradient bounded by
h^(1/4) times a finite-parameter subpower factor, so the comparison with
the fixed base approximation U_0 is justified too.

## 2. Uniform endpoint constants are obtained before diagonalization

A lower bound with an arbitrary positive constant c(n) would not imply
a uniform lower bound after choosing n(h). The diagonal note does not
make that invalid inference. The precise central input is equations
(1)–(2) of the [outgoing polarization note](outgoing-outer.md):
for **any fixed** C_0>0, the comparisons hold on
delta<=tau<=C_0 log ell, uniformly in h and terminal orbital phase.
Their constants depend on that one C_0, delta and the fixed profile.

Fixing C_0=1/(4mu), then requiring n<=ell^(1/8), gives exactly

```text
L_(ell,n) = log(ell)/(8mu) + log(n)/mu
         <= log(ell)/(4mu).
```

The central amplitude–covector product therefore has one common pair
of positive comparison constants across all fixed-n problems in the
eventual diagonal. Its endpoint model size is n ell². This uses the
full polarization vector, not its sign-changing growing coordinate.
The future-covector source and the outgoing weighted system both retain
the fixed actual Gavrilov profile and pressure projection.

Passing to the actual packet requires additional source inputs. The
logarithmic assembly supplies uniform-in-time central/actual-q comparison,
whole-label comparison, slow curl terms, and the small central heat clock.
The fixed-depth argument extends those estimates to each fixed eta=n.
Their constants can depend on n, because all their errors vanish for
that fixed n. The transported bump equals one on its central label;
the phase stays zero there. Its fixed odd profile is linear near zero,
and the central heat time tends to zero. Hence its central phase
derivative approaches the required nonzero value.

The leading symmetric matrix has Frobenius norm
|b_c||xi_c|/(sqrt(2) k). The source's background-gradient size on the
last unit interval is at most C_n(1+n ell^(9/8)); divided by n ell²,
this tends to zero for each fixed n. Small profile corrections and
the actual comparison errors can also be made smaller than a fixed
fraction of the common central lower bound. Thus choosing thresholds
does absorb **vanishing errors**, while the leading lower constant was
already made uniform by the common central horizon. The distinction is
essential and correctly respected.

## 3. The lower clock bound has an interval, not just an endpoint

For each fixed n and sufficiently small h, the final unit interval
lies in the central comparison region beyond delta. There,

```text
||grad Q_h(t)||infinity
    >= c_0 n ell² exp(mu [t-T(h,n)]).
```

The reference q-particle is only a location at which to test the spatial
supremum. It need not be a Q_h trajectory. Integrating on this entire
unit interval gives

```text
integral ||grad Q_h||infinity dt
    >= c_0 (1-exp(-mu))/mu * n ell².
```

This verifies the uniform positive lower clock constant. An endpoint
gradient bound alone would not have been enough. The upper bound uses
the independent sharp whole-support history B n ell²+o_(J,n)(ell²),
not a generic high derivative estimate. For fixed n the two remainder
thresholds can make the profile-clock error and integrated actual error
at most ell²/n each. The resulting upper coefficient B+2/n² is correct.

## 4. The Fourier conclusion uses the right monotone quantity

With unnormalized spatial H-r norm on the torus of side 2pi L and
normalized coefficients vhat(m), Fourier Cauchy–Schwarz bounds the
**absolute sum**

```text
A_R(v) = sum_(|m/L|>R) |m/L| |vhat(m)|
       <= C_r R^(5/2-r) ||v||H^r, r>5/2, R>=1.
```

The lattice count contributes L³ before its square root and Parseval
contributes (2pi L)^(-3/2). Their cancellation makes the estimate uniform
for L>=1. Inhomogeneous H3 controls the full Fourier-summed gradient and
the value of v as well; no expanding-domain Poincaré constant is needed.
This is the argument actually used by the reviewed finer-tail source,
so the diagonal note may legitimately use its stronger absolute-sum form.

For beta_n=3/2+1/n and r_n=12+n²+4n, direct substitution gives

```text
A_(r_n)(beta_n)
 = r_n/n - 3/8 - 5/(2n)
 = n + 29/8 + 19/(2n) > n+3.
```

Increasing J_n to satisfy both displayed strict margins in the source
also makes the actual H3 error small enough. After the fixed constants
and subpower factors are absorbed, the sum of the approximation and
actual-error tails is at most h^n. This uses the actual full Q_h and
does not assign separate smallness to arbitrary cancelling summands.

Absolute sums are monotone in the cutoff. For every fixed beta>3/2
and P>0, eventually beta_n<beta and n>=P, proving the final h^P bound.
The spatial L-infinity norm of a sharp Fourier projection need not be
monotone, but the note explicitly avoids that false step. There is still
no conclusion at beta=3/2 and no exclusion of the coarser generated band.

## 5. The single schedule preserves the same datum at each h

For each fixed n, all estimates give thresholds valid for **every**
sufficiently small admissible h. Recursively choose H_n below these
thresholds and with H_(n+1)<H_n/2. The staircase assignment

```text
H_(n+1)<h<=H_n  =>  eta(h)=n, J(h)=J_n, r(h)=r_n
```

then invokes only a proved fixed-parameter estimate at each selected h.
The sequence tends to arbitrarily large finite n as h tends to zero.
Every correction starts at zero, the primary data are independent of
the proof indices, and strong uniqueness identifies solutions on
overlapping intervals. Thus changing the proof schedule does not alter
Q_h(0) at the same h or add a later seed.

At the nth step, n,J_n,r_n are fixed numbers. Since ell(h) and any
prescribed G(h) tend to infinity, thresholds can additionally enforce

```text
max(n,J_n,r_n) <= ell(h)^(1/n),
max(n,J_n,r_n) <= G(h)
```

for every smaller h. G need not be monotone: its limiting divergence
already provides such a threshold. Therefore log eta, log J and log r
are o(log ell), as stated. This construction gives existence of a
sufficiently slow schedule, with no computable thresholds or prescribed
growth rate supplied by these inputs.

The conclusion I_h/log(1/h)->infinity follows from the lower clock
bound and eta(h)->infinity. The time identity also checks:
T_h=[17/(8mu)+o(1)]log ell. Thus the additive extension beyond each
fixed-eta endpoint diverges, while the leading lifetime coefficient
is unchanged along this chosen slow diagonal. Physical times still
carry h^24. The datum continues to vary with h.

## 6. Review limits and one wording precision

The earlier fixed-depth disclaimers were correctly cautious about an
arbitrary or prescribed growing schedule. Read literally as excluding
every possible schedule depending on h, they are stronger than the
fixed-parameter statements warrant. This note supplies the missing
non-effective diagonal corollary without proving quantitative high-order
constants. It does not validate eta=ell^(1/16), a convergent infinite
profile expansion, or continuation of one fixed datum to a singular time.

One non-load-bearing wording precision was reported to the coordinating
agent: the phrase “the original datum's exact focus” after source (1)
should refer to the designated exact **central-model** focus used in
the preparation. It should not be read as an exact focusing event of
the full actual Q_h. The subsequent argument consistently uses the
designated t_f and the q reference particle, so no estimate depends on
the stronger interpretation.

The review independently checked the scale arithmetic, all six source
hashes, the common-horizon constants, persistence needed for the clock,
the Fourier normalization and monotonicity, and the staircase quantifiers.
It relies on the already reviewed finite-depth construction and its
actual-q/profile estimates; it is not a new independent rederivation
of that entire PDE chain. No assertion about useful later feedback,
maximum-speed amplification or an infinite forced construction is added.
