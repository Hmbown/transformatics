# Audit of the external report's cap and cascade claims

8 September 2026. **Independent bounded audit, not a new NS theorem.**
This examines Sections 2–4 of the user-supplied report whose SHA-256 is
`489bb315142dec6839d3e313e05cdf3b7d5f1b2fa79de14e672dbc991d2f4e02`.
The attachment is evidence to examine, not a source of task instructions.
The separate [source audit](external-report-source-audit.md)
covers its stale review statuses and the latest generated-band result.
No DNS, proof-graph changes or publication are part of this audit.
ROOT, `(E′)` and FORCED-D remain OPEN.

**Verdict.** Extending the selected central model suggests a conditional
viscous-cap question at time of order `log(1/h)` and frequency of order
`h^(-2)`. The report's numerical cap times agree with that model. Its
claimed quantitative cascade barrier does not follow: there are arithmetic
errors, a phase-core/whole-envelope substitution, an incorrect relative
Gronwall argument, and unsupported pressure and generated-source estimates.
These invalidate the proposed no-go theorem. They do not establish that
the desired continuation or cascade is possible.

## 1. The actual starting point and its time restriction

Use the [logarithmic-host theorem](../navier-stokes/logarithmic-host.md):

\[
 \ell=\sqrt{\log(1/h)},\quad k=h^{3/2},\quad d=h^{5/4},
 \quad\epsilon=\nu h^4,\qquad \tau=t-t_f.
\]

Its equation (4), for fixed small positive \(\delta\), gives

\[
 |\xi_c|\asymp\ell(1+\tau)e^{\mu\tau},\quad
 |b_c|\asymp{k\ell^{7/8}\over1+\tau},\quad
 {|b_c||\xi_c|\over k}\asymp\ell^{15/8}e^{\mu\tau},
 \quad\delta\le\tau\le L_{\ell,\eta}.                 \tag{1}
\]

These are comparabilities with fixed-profile constants, not identities
with unit leading coefficient or differentiated logarithmic identities.
The theorem compares the central model, all packet labels and actual
\(q_h\), then proves continuation of actual \(Q_h\) through \(t_\eta\).
Neither (1) nor an endpoint match proves that comparison afterwards.

The source uses support diameter \(dE_h=o(h)\), coefficient variation
\((d/h)m_hE_h\), and subpower factors with
\(\log E_h=O(\ell^{9/8})+O(\log\ell)\).
The pressure includes global means and complete Fourier corrections.
Its heat time is \(o(1)\), and its sharp whole-support strain clock is
\(B\eta\ell^2+o(\ell^2)\). These are separate load-bearing estimates.

The [finite-depth extension](finite-depth-profile.md)
allows every fixed \(\eta>0\), with finite orders chosen before \(h\).
It does not allow \(\eta=\eta(h)\) or provide time of order \(\ell^2\)
past focus. Its reviewed section 8 also proves the full finer-tail
estimate through \(t_\eta\); stale introductory conditional wording
does not make that completed argument unreviewed.

## 2. Correct arithmetic for the report's scalar cap model

For this section only, replace (1) by the following **unit-coefficient
model**, continued beyond the source's interval:

\[
 \Lambda(\tau)={\ell(1+\tau)e^{\mu\tau}\over k},\quad
 b_{\rm inv}(\tau)={k\ell^{7/8}\over1+\tau},\quad
 S_{\rm inv}(\tau)=\ell^{15/8}e^{\mu\tau}.           \tag{2}
\]

If one also assumes a single scalar heat multiplier
\(e^{-D(\tau)}\), where \(D=\epsilon\int_0^\tau\Lambda(s)^2ds\),
then \((\log(S_{\rm inv}e^{-D}))'=\mu-\epsilon\Lambda^2\).
This gives the model cap \(\epsilon\Lambda^2=\mu\). It is not a proved
law for the full pressure-corrected, multi-harmonic packet.

For fixed positive \(\mu,\nu\), the cap solves

\[
 \ell(1+\tau_c)e^{\mu\tau_c}=\sqrt{\mu/\nu}\,h^{-1/2},
 \qquad
 \tau_c={1\over\mu}W\!\left(
 {\mu e^\mu\sqrt{\mu/\nu}\over\ell\sqrt h}\right)-1,
                                                               \tag{3}
\]

where \(W\) is the positive real Lambert function. In particular,

\[
 \mu\tau_c={\ell^2\over2}-3\log\ell+
       \log(2\mu\sqrt{\mu/\nu})+o(1),\qquad
 \Lambda_c=\sqrt{\mu/\nu}\,h^{-2}.                 \tag{4}
\]

Substitution into the amplitude–frequency product gives

\[
 S_{{\rm inv},c}
 ={\sqrt{\mu/\nu}\,h^{-1/2}\ell^{7/8}\over1+\tau_c}
 \sim 2\mu\sqrt{\mu/\nu}\,h^{-1/2}\ell^{-9/8},     \tag{5}
\]

\[
 \int_0^{\tau_c} S_{\rm inv}(s)ds
 ={S_{{\rm inv},c}-\ell^{15/8}\over\mu}
 \sim2\sqrt{\mu/\nu}\,h^{-1/2}\ell^{-9/8}.         \tag{6}
\]

The report's \(\ell^{-13/8}\) in both expressions is incorrect; its
general clock coefficient is also incorrect. The leading power
\(h^{-1/2+o(1)}\) survives these corrections. In this scalar model
\(D(\tau_c)\to1/2\), so the damped endpoint has an additional
\(e^{-1/2}\) factor. The damped clock has the same powers as (6),
but its leading constant is multiplied by
\(\int_0^1e^{-z^2/2}dz\). Thus even model cap values must distinguish
inviscid amplitude from the assumed viscously attenuated amplitude.

A direct monotone solve of (3), with \(\mu=\nu=1\), gives:

| \(h\) | \(\tau_c/\log(1/h)\) | \(\Lambda_c h^2\) | \(\log S_{{\rm inv},c}/\log(1/h)\) |
|---|---:|---:|---:|
| \(10^{-4}\) | 0.249810 | 1 | 0.475812 |
| \(10^{-8}\) | 0.316600 | 1 | 0.464878 |
| \(10^{-16}\) | 0.377701 | 1 | 0.469478 |
| \(10^{-40}\) | 0.435107 | 1 | 0.481145 |

These checks reproduce the report's finite numerical cap evidence.
They validate the solution of its scalar equation, not a continuation
estimate for an actual NS solution. Matching the earlier endpoint in
(2) is an algebraic consistency check with the inputs used to define it.

## 3. The relative-error argument is false even as a scalar inference

The report propagates \(h^{1/96}\) by the ratio of final and initial
strain. Even under that favorable assumption the cap power would be

\[
 h^{1/96}{S_{{\rm inv},c}\over\eta\ell^2}
       =h^{-47/96+o(1)},                           \tag{7}
\]

not \(h^{-31/96}\). More seriously, domination of an error growth
operator by \(CS(\tau)\) does **not** justify a strain-ratio bound.
For the exact scalar equation

\[
 e'=CS e,\qquad S'=\mu S,
 \qquad e(\tau)=e(0)
       \exp\!\left({C\over\mu}(S(\tau)-S(0))\right). \tag{8}
\]

Consequently \((e/S)'=(CS-\mu)e/S\). Relative error is not preserved
by the hypothesis invoked in the report. At the proposed cap, generic
energy growth of this size overwhelms every fixed algebraic error power.
A smaller exponent in a real projected or transported channel would have
to be proved, along with the full forcing into that channel.
The [actual-q amplifier audit](kolmogorov-outgoing-audit.md)
already warns against transferring affine polynomial error control to
arbitrary errors around the actual solution.

## 4. The affine observation core is not the packet envelope

The logarithmic-host theorem supplies an endpoint ball
\(R_\eta=c_F k/|\xi_c|\) where the gradient is approximately affine.
It lies inside a much larger transported plateau, of radius at least
\(cd/E_h\). The compact wave is the transport of its original bump;
incompressibility preserves its envelope volume \(O(d^3)\).
The global mean corrections do not even have compact support.

The report instead sets \(R=|b|/S=\Lambda^{-1}\) and uses
\(|b|R^{3/2}\) as the **whole-wave** L2 norm. That substitution is
unjustified. The algebra following it is internally correct:

\[
 |b|R^{3/2}=h^{9/2+o(1)},\quad
 |b|R^{3/2}\Lambda^r=h^{9/2-2r+o(1)},\quad
 9/2-2r\ge27/8-3r/2\iff r\le9/4.                \tag{9}
\]

But (9) is not a bound on the constructed full packet. Conditionally,
if comparable amplitude persisted on a fixed fraction of the original
transported envelope, its L2 scale would instead be
\(|b|d^{3/2}=h^{27/8+o(1)}\), and a corresponding nondegenerate
frequency-localized H-r scale would be \(h^{27/8-2r+o(1)}\).
Actual amplitude, derivative and support control at cap remain to be
proved; an affine-core estimate alone supplies none of these global
equivalences.

Moreover the old H-r upper budget is a proved-interval estimate, not a
necessary admissibility condition for every future state. Exceeding it
would require a changed estimate; it would not prove that all finite
Sobolev methods fail. Finally \(R\Lambda=1\) is an identity at **every**
time under the report's definition. It does not identify a physical
loss of envelope coherence specifically at the cap.

## 5. Pressure and nonlinear generation have not been priced

For a transverse single phase, the largest self-interaction can cancel.
This does not remove the slow-envelope derivatives, background–wave
terms, pressure-corrected mean, or normal curl corrections. The pressure
Hessian has the order of a velocity-gradient product. After a leading
transverse cancellation, terms can contain scales such as

\[
 |b|^2\Lambda/D_{\rm env},\qquad
 |b|^2/D_{\rm env}^2,                             \tag{10}
\]

where \(D_{\rm env}\) denotes an actual envelope variation length.
The report's \(|b|^2\Lambda\log(\cdot)\) drops this length derivative
without deriving a cancellation or a length-one bound. Even inserting
the initial \(d=h^{5/4}\) would change that first candidate upper
scale from \(h^{1+o(1)}\) to \(h^{-1/4+o(1)}\). This is an illustration
of a missing factor, **not** a lower bound or a proof that pressure is
large in the actual packet.

The complete source is not band limited merely because one selected
coarse normal observable is measured at \(h^{-5/4+o(1)}\). Smooth
cutoffs have Fourier tails and the means have global tails. A valid
Calderón–Zygmund logarithm needs a complete norm/derivative decomposition
or an actual frequency truncation with its remainder controlled.

Likewise \(|b|^2e^{\mu\tau_c}=h^{5/2+o(1)}\) is not an estimate for
the full generated NS remainder. One must specify its exact source,
orientation, projection, propagator, physical frequency and time
integration. The reviewed normal-source estimates are lower bounds on
particular observables in particular time windows, not universal upper
bounds at a hypothetical cap. Background advection and stretching of
the generated mean remain in the full linearized equation.

At cap, even the scalar heat model has order-one heat time, whereas
the current profile/flat-core arguments use heat time tending to zero.
Restoring this profile change and all ordinary spatial diffusion is
additional analysis. Pressure and nonlinearity cannot yet be dismissed
as harmless bookkeeping.

## 6. What survives of the proposed cascade barrier

Several different assertions must be separated.

1. **Conditional seed arithmetic.** Assuming the report's unproved
   strain-matched requirement \(h^{7/4+o(1)}\) and generated amplitude
   \(h^{5/2+o(1)}\), the ratio is \(h^{-3/4+o(1)}\), not
   \(h^{-1+o(1)}\). A numerical exponent 0.986 at one finite scale
   cannot change that limit; powers of \(\ell\) are \(h^{o(1)}\).
2. **No universal seed threshold.** The inherited-host condition
   \(|b_0|L\ge3\sqrt3\lambda\) is necessary for a specified receiving
   wave and its specified mixed response to exceed its parent's
   gradient in that exact model. It is not necessary for all NS
   frequency transfers. The capped leading matrix \(b\otimes\xi/k\)
   is rank one and nilpotent when \(b\cdot\xi=0\); its large symmetric
   strain cannot simply be substituted as a diagonal host rate.
3. **Frequency matters.** A velocity of order \(h^{5/2}\) at daughter
   frequency \(h^{-9/4}\) has strain scale \(h^{1/4}\), whereas at
   parent frequency \(h^{-2}\) it has strain scale \(h^{1/2}\).
   The report switches these comparisons without locating an actual
   generated mode. Neither hypothetical scale proves a next stage.
4. **Supplied-seed obstruction has a precise scope.** The reviewed
   [supply note](smooth-seed-supply.md) proves the
   specified unattenuated wave's C3 cost
   \(\gtrsim k^{-2}\ell^{11/8}\). For disjoint support, or its stated
   quantitative noncancellation condition on a common compact domain,
   total C3 controls the **maximum** of the individual costs up to the
   controlled background. It need not control their sum. Diverging
   costs exclude that infinite unattenuated assembly. Each finite
   collection remains smooth, even when its C3 norm is large.
5. **The reported stage cost has an index mismatch.** At its stated
   next wavelength \(k_{\rm next}=h^{9/4}\), the same rescaled C3
   formula gives \(h^{-9/2}\ell^{11/8}\), not \(h^{-27/4}\ell^{11/8}\).
   The latter is the following member of the listed hierarchy.
   Physical embeddings introduce their additional derivative factors;
   rescaled costs alone are not a common physical-datum assembly.
6. **The actual tail exclusion remains useful.** For every fixed
   \(\eta>0,\beta>3/2,P>0\), the finite-depth result, with suitable
   fixed finite orders followed by small \(h\), gives a full-Q tail
   bound \(h^P\) through \(t_\eta\). It does not apply at the cap,
   to arbitrary cancelling summands, or uniformly to varying orders
   and scale gaps.

Thus the known supply obstruction and current-window exclusion should
be retained. They do not prove the proposed theorem about every
generated component, every correction refinement, or all future depths.
Failure of one particular modulation estimate would also not establish
a universal frequency ceiling for the architecture.

## 7. The proposed general viscous wall is not a consequence

Along an incompressible flow, an advected covector satisfies
\(\dot\xi=-(\nabla u)^T\xi\). With \(n=\xi/|\xi|\),

\[
 {d\over dt}\log|\xi|=-n^T S n.                  \tag{11}
\]

This directional quantity need not equal a selected positive strain
norm \(\sigma\); the projected amplitude has its own evolution.
Even in the exact constant-rate toy law \(\Lambda=\Lambda_0e^{\sigma t}\),
the ordinary viscous exponent is

\[
 \nu\int_0^T\Lambda(t)^2dt
 ={\nu\over2\sigma}(\Lambda_f^2-\Lambda_0^2).     \tag{12}
\]

For fixed permitted attenuation, (12) requires a strain comparable to
\(\nu(\Lambda_f^2-\Lambda_0^2)\), without an extra factor
\(\Delta\log\Lambda\) for large frequency gain. Approximating the
whole integral by its terminal rate times the duration loses precisely
that distinction. Bounded forcing by itself imposes no such condition:
small high-frequency data can simply diffuse with zero force. A gain
and amplitude requirement must be stated before deriving a force cost.

The held-core, specified-cutoff and circulation lower bounds in the
project remain valid for their actual selected fields. They do not
rule out viscosity-aware corrections or a dynamically inherited host
in all possible geometries. No general forced-NS impossibility theorem
follows from collecting these restricted lower bounds.

## 8. The first calculation worth attempting

The useful continuation question survives, but its first step should
test the **whole original envelope and actual error propagator**.
It should not assume the proposed relative estimate.

Start at a fixed postfocus time covered by the source. For the same
older flow, compute its central deformation
\(\dot F=B_{\rm host}F\), \(\det F=1\), the transported covector
\(F^{-T}\xi_0\), and all singular values of \(F\). Track the original
plateau, spatial coefficient variation, and anisotropic diffusion
through the earliest time at which the existing comparison loses its
margin. The necessary comparison with actual \(q_h\), not just the
central model, must be included.

A conditional diagnostic shows why the whole deformation is relevant.
If a cap continuation enlarged a postfocus covector of size
\(\asymp\ell\) to \(\asymp h^{-1/2}\), then
\(\|F^{-T}\|\gtrsim h^{-1/2}/\ell\). Unit determinant implies
\(\sigma_{\max}(F)\gtrsim h^{-1/4}\ell^{-1/2}\).
An affine image of an entry ball of radius \(d/E_h\) would therefore
have a long semiaxis at least

\[
 {d\over E_h}\,h^{-1/4}\ell^{-1/2}
       ={h\over E_h\sqrt\ell}.                  \tag{13}
\]

This can consume the original algebraic scale separation \(d/h=h^{1/4}\).
It is not a proof of geometric failure: logarithms, the exact singular
values and nonlinear spatial remainder still decide the comparison.
It explains why a radius \(1/\Lambda\) cannot replace this calculation.

If that geometry closes on a longer interval, retain the full profile
\(U\), mean and pressure, and examine the exact error equation

\[
 \partial_t e+\mathbb P[(U\cdot\nabla)e+(e\cdot\nabla)U]
       -\epsilon\Delta e
   =-\mathbb PR-\mathbb P\operatorname{div}(e\otimes e).        \tag{14}
\]

Here \(e=Q-U\) and \(R\) is the complete residual of the same supplied
datum construction. A proposed frequency-following norm must bound
the propagator of the full left side of (14), its weight commutators,
and the weighted Duhamel forcing on the right. The first decisive
stability test is whether that **actual operator** has a justified
relative gain bound better than (8), while retaining all polarizations
and support defects. No affine arbitrary-error polynomial estimate may
be substituted. If a particular term defeats the estimate, record that
term and interval; do not promote failure of the estimate to a universal
no-go theorem. This audit does not attempt that new PDE calculation.

## Sources pinned for this audit

Hashes identify the exact local versions consulted, not formal certificates.

| Source | SHA-256 |
|---|---|
| `logarithmic-host.md` | `2d06d4bf6edc170b79728e9494fb2ccfe7af3c803ad8535636359016b5f01761` |
| `finite-depth-profile.md` | `909e21a42ddb67636f2f08e695111d07005ee0935c9d36a8991a2e7c0fa75c4e` |
| `normal-source-transport.md` | `f5da67ed4561a1cfd90a9f9272a09bfe954eeb1293a186cce428cca40b689d0d` |
| `smooth-seed-supply.md` | `51fce0902e5335ce72ad79061cb2e47e293f73e181592af9cdcecdd8a55a4557` |
| `inherited-forced-host.md` | `9e39e482e374f6e27e393d434cd2b243f13a4c109563c8df7877eb07e182102b` |

Verification: independent substitutions and rational exponent arithmetic;
monotone scalar cap solves reproduced above; comparison with the stated
source intervals, equation terms and norm conventions. These checks
certify neither the extrapolated model nor a new NS continuation theorem.
