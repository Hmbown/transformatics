# Independent review of the conditional growing-depth budget

8 September 2026. **PASS for the conditional continuation implication and
the conditional scalar recurrence.** This does not establish the proposed
uniform packet/operator estimates. It supplies no explicit longer-window
theorem until those hypotheses are proved. ROOT, E-prime and FORCED-D
remain OPEN. No DNS, canonical edits or formal PDE certification.

Reviewed source: sections 1--4 of
[growing-depth-budget.md](growing-depth-budget.md),
at SHA-256

```text
2a7b8ff6258eb003652d3a3334b41aa135330d21ee1776b9c021b2d9a8977505
```

The initially reviewed version was
`5f2c01bba7df4e9fd4042cfe02d63233e24852044b3b58f29543807e18de9a26`.
The author then explicitly chose C12>=1 and clarified that increments
use scaled amplitude norms with a separate k^(-1) conversion for evaluated
gradients. Both changes were reread at the source hash above. They leave
the estimates unchanged and resolve the two presentation findings.

## 1. Conditional strong continuation

The hypotheses specify a smooth solenoidal U_J constructed independently
of the full exact solution's future lifespan. Its original datum is the
prescribed u_(h,0); selecting J does not select new data. With e=Q_h-U_J,
the exact energy identity cancels the divergence-free transport and
quadratic e-advection pairings. The remaining transport term is bounded by
||grad U_J||infinity ||e||2². The full residual is paired with e, so the
source's L2 relative-energy inequality follows. No assumption that the
unprojected residual is solenoidal is needed.

On the bootstrap interval ||grad e||infinity<=1, the exact solution's
gradient clock is at most I_h+T_h. The standard integer H12 energy bound
therefore gives (5), including the approximation's H12 contribution.
C12 belongs to the fixed derivative order 12 and has no dependence on J.
Any cost of constructing increasingly accurate approximations has to be
placed in the explicitly assumed L_h, not in an unspecified constant here.

The tame Sobolev energy constants are uniform on tori of side 2pi L,
L>=1. One can obtain them from the periodic derivative product inequalities
with the inhomogeneous low-order terms retained. The mean-zero assumption
is compatible with the source, but does not justify ignoring low Fourier
modes or using a Poincare constant independent of L.

For the gradient interpolation, a Fourier split at R>=1 gives

    low frequencies <= C R^(5/2) ||e||2,
    high frequencies <= C R^(-19/2) ||e||H12.

Normalized Fourier coefficients supply (2pi L)^(-3/2), canceling the
L^(3/2) lattice-counting factor. Optimization gives weights 19/24 and
5/24, with uniform constants. The stated additive L2 term is harmless.
There is no use of the false endpoint embedding H^(5/2) into W^(1,infinity).

The exact pre-clock interpolation exponent is

    (19/24)(29+2J)/8 - (5/24)(117/8) = (19J-17)/96.

The L2 clock contributes 19/24 of I_h and the H12 clock contributes
5C12/24. This verifies Gamma=(19+5C12)/24 and the coefficient
(1+Gamma)L_h in (7). Taking C12>=1 makes Gamma>=1, so the additive L2
term is bounded by the same displayed upper exponent: its negative
pre-clock exponent is larger by (365+5J)/96, while its L_h and clock
coefficients are no larger. The energy constant can always be enlarged
this way without affecting its uniformity.

For eta=ell^a and J=ceil(K eta), the first proposed loss divided by
eta ell² has order ell^(ap-7/8). The second has order
ell^(a(p-1)-2) log ell, which tends to zero when ap<7/8. Thus (3)
really implies the required o(eta ell²), including that second term.
The ceiling in J changes only lower-order terms. Under (8), the negative
coefficient has more than two units of margin before the vanishing loss;
the factor h^eta in (9) follows after reducing h.

This strict improvement closes the C1 bootstrap. For each fixed h the
H12 bound and gradient integral remain finite through the prescribed
finite T_h, excluding an earlier strong endpoint. Smooth initial data
then retain smoothness by the standard higher-order energy estimates.
This is a conditional actual-flow continuation theorem, not merely an
estimate on a hypothetical error after the solution has already ceased
to exist.

The velocity interpolation uses H12 weight 1/8 and has pre-clock exponent
(7J+43)/32. Its clock coefficient is (7+C12)/8, no larger than Gamma
when C12>=1. Its stronger negative J coefficient verifies the claimed
vanishing velocity error as well.

## 2. Explicit loss degrees and the scalar recurrence

At a=1/16, ap<7/8 is exactly p<14. This is a sufficient condition, not
a proof of failure when p>=14. Factorial factors that enter an approximation
constant multiplicatively contribute O(J log J) to its logarithm. They
must still be distinguished from a factorial coefficient multiplying a
transport clock inside an exponential.

For the recurrence, enlarge fixed constants so A=C D^b>=1 with b>=0,
and put g_j=F_j/k. Then (10) gives

    g_0 <= A rho,
    g_(j+1) <= A rho g_j + A g_j².

Set q=2A²rho. If q<=1/2, induction gives

    g_j <= A rho q^j.

Indeed g_j<=A rho implies A(rho+g_j)<=2A²rho=q, and the estimate
therefore propagates. This supplies the sharper bound

    F_J <= k A rho (2A²rho)^J,

which implies the deliberately looser (11) after fixed enlargements of C.
The assumption rho D^(3b) sufficiently small implies q<=1/2. No repeated
squaring of D or unspecified depth-dependent constant is needed in this
conditional scalar argument.

Summing the assumed increments gives the scaled amplitude bound

    sum_j increment_j <= k A²rho/(1-q).

For a receiving wave, evaluation at phase S/k gives a gradient factor
k^(-1); slow d^(-1) costs are smaller, with the phase/curl coefficient
factors charged in D. Thus the corresponding unscaled gradient bound is
of order A²rho/(1-q), not k A²rho/(1-q). It is still small under the
proposed coefficient estimates. The source now distinguishes these scaled
increment norms from evaluated gradients; putting k^(-1) itself into D
would destroy the intended smallness condition and is unnecessary.

This controls the accumulated correction gradients only. The leading
primary whole-envelope clock remains an additional hypothesis, as the
source explicitly says. Similarly residual amplitudes must be converted
to unnormalized L2 with their stated d^(3/2) factor and time integration.
The resulting finite powers and log T_h costs fit within the proposed
loss once the underlying normalized operator bounds are proved.

With N=O(J), log of (11)'s coefficient has order J log D. Substituting
(12) gives the claimed J³ eta ell^(9/8) and J⁵ logarithmic terms in (13).
At a=1/16, dividing by eta ell² gives respectively

    O(ell^(-11/16)),
    O(ell^(-7/4) log ell).

Both vanish. Also (12) itself gives

    log D = O(ell^(21/16) + ell^(1/4) log ell) = o(ell²).

Therefore rho D^(3b) tends to zero, so the scalar contraction condition
does follow from these proposed coefficient bounds. Exact rational
arithmetic independently checked the interpolation and power identities.

## 3. What remains outside this verdict

None of the above derives the four operator bounds defining D, the actual
background's longer lifetime, its high-order differentiated estimates,
the full pressure solvers, inverse-phase control, or the primary sharp
history. The scalar recurrence assumes they imply (10); it does not prove
that implication from a formal profile expansion. Approximation H12 and
residual norm conversions must both retain the uniformity required by (1).

A Gevrey choice is a substantive assumption on fixed profiles. Arbitrary
smooth profiles need not have such quantitative bounds. A later choice
of new profiles must be identified as a change of the family unless those
profiles were already part of its allowed fixed original-data choice.

The conditional implication and scalar exponent accounting pass. The
explicit eta=ell^(1/16) theorem remains OPEN until the uniform coefficient
and sharp-history hypotheses are independently established. This review
does not promote that theorem or any global Navier--Stokes target.
