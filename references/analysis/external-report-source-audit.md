# Source audit of the external report's continuation proposal

8 September 2026. **Bounded source and quantifier review.** The complete
user-supplied report was read, with emphasis on section 8 and its claimed
inputs to cap tracking. Its attachment SHA-256 is
`489bb315142dec6839d3e313e05cdf3b7d5f1b2fa79de14e672dbc991d2f4e02`.
This note complements the separate cap/stability audit. It does not
verify the report's literature claims, reprove every upstream analytic
lemma, or assert a continuation beyond the present theorem. No DNS or
canonical source edits were made.

The useful proposal is to seek a longer, frequency-following estimate for
the same actual solution. The report does not yet establish its claimed
Sobolev ceiling or generation barrier. Its source-status table is also
behind the current written results.

## 1. What section 8 must update

The current inputs are the
[finite-depth construction](finite-depth-profile.md),
[separate finer-tail review](finer-scale-review.md),
[initial-time normal transport](normal-source-transport.md),
[postfocus signed source](postfocus-normal-source.md), and
[full-flow coarse-band comparison](actual-coarse-band.md).
Each has a linked independent AI-agent review. These are written analytic
results with their stated prerequisites, not external expert acceptance
or kernel-checked PDE certificates.

**Tail bound (9).** The words “predicts” in section 8 and “if validated”
in section 6 of the finite-depth note are stale drafting language. The
current introduction records the separate review, and section 8 actually
finishes the proof. Its order of quantifiers is

    fix eta>0, beta>3/2 and P>0;
    choose finite r and J depending on these;
    then take h sufficiently small.

It obtains, for the full actual Q_h with unchanged original data,

    sup_[0,t_eta] ||grad P_(>h^(-beta)) Q_h||infinity <= h^P.       (1)

The proof chooses r to control the finite approximation's tail and J to
control its actual error and the separate continuation bootstrap. It
does not require an infinite correction limit. Thus “only fixed finite
J was validated” is not a gap in this particular quantified conclusion.
It remains correct that the estimate is not uniform in beta approaching
3/2, in P, or in h-dependent eta, J or r; it says nothing after t_eta.

**The normal pair.** The cited bounds (5)–(6) in the initial-time normal
note are now reviewed. They concern 0<t<=t_0 for one fixed sufficiently
small initial rescaled time, not a focus interval. The distinct reviewed
postfocus note transports a different endpoint row through focus. The
later full-Q comparison then bounds q and the exact linear receiver
separately, so its generated band is observable in the full solution.
The report's list omits these last two mathematical steps.

The logarithmic host's h^(1/96) C1 comparison remains a restricted
written result. In particular its constants and actual lifetime cannot
be extended to a time of order ell squared by matching an endpoint
power. The asymptotic formulas there use comparability constants, not
identities with unit coefficient.

## 2. Exactly what the generated normal result says

Let q be the actual first-stage solution, Z its exact viscous
linearization from the original receiver z_0, and

    W=Q-q, N=W-Z, N(0)=0.

With B_q v=P(q.grad v+v.grad q), the exact equation is

    (partial_t+B_q-epsilon Delta)N
             =-P div(W tensor W).                              (2)

Thus q times every generated mean remains in the full linear propagator.
It cannot be discarded from a total-stress calculation. The source on
the right includes all actual relative mean-wave and mean-mean terms.

The initial-time result tests the original receiving normal e_n. The
postfocus result tests r(t_eta), transverse to the primary normal N_p,
in a shrinking angular cone about N_p. The two letters N and N_p here
distinguish the nonlinear remainder from the primary covector. The
postfocus sign comes from a special pressure-correct stable channel,
not generic positivity of an instantaneous projected stress.

For a smooth annular multiplier B_h around
kappa_h=h^(-5/4)H_h^(-A), where log H_h=o(log(1/h)), the latest result is

    ||B_h[r(t_eta).Q(t_eta)]||infinity
            >= c eta^(-1) h^(7/4) ell^(9/8) H_h^(-4A-4M),
    ||S(B_h Q(t_eta))||infinity
            >= c eta^(-1) h^(1/2) ell^(9/8) H_h^(-5A-4M).         (3)

The initial band has velocity at most h^2 H_h^C and gradient at most
h^(3/4)H_h^C. Leakage from exact q and Z has been bounded individually.
The full generated remainder also satisfies

    sup_[0,t_eta] ||N||C1 <= C h^(1/96),
    integral_0^t_eta ||grad N||infinity dt = o(1).                 (4)

These are compatible lower and upper bounds with different powers.
The lower strain scale h^(1/2+o(1)) in (3) is not an upper bound on
every generated component. Nothing here gives a cap-time upper bound
on generated amplitude, let alone one at a different fine frequency.
The report's proposed comparison with h^(5/2+o(1)) at cap therefore
does not follow from the latest source.

Equation (1) does exclude an algebraic-size **full tail** at every
fixed finer power scale during the proved interval. It does not bound
arbitrarily chosen cancelling summands. Equation (3) lies at a coarser
scale and is outside that exclusion. Equation (4) gives a useful
present-window limitation: the identified remainder alone does not
accumulate an order-one strain clock there. It does not exclude later
amplification by q, Z or their nonlinear combination.

## 3. Fourier normalization and the asserted Sobolev ceiling

On the expanding torus of side 2pi L, use frequencies K_n=n/L and
normalized Fourier coefficients

    vhat(n)=(2pi L)^(-3) integral v(x) exp(-iK_n.x) dx.

Parseval and Fourier Cauchy–Schwarz give, for R>=1 and r>5/2,

    ||grad P_(>R)v||infinity
      <= (2pi L)^(-3/2)
         [sum_(|K_n|>R) |K_n|²(1+|K_n|²)^(-r)]^(1/2) ||v||H^r
      <= C_r R^(5/2-r) ||v||H^r.                               (5)

Here H^r uses unnormalized spatial L2. Lattice counting supplies L³,
which cancels the inverse-volume factor. Inhomogeneous H3 therefore
controls the absolute Fourier-summed gradient uniformly in L. This
assertion in the finite-depth source is correct; it does not assume
that a sharp projector is bounded on L-infinity.

The approximation bound through t_eta is

    ||U_J||H^r <= h^(27/8-3r/2) E_(J,r,eta), r>=12.              (6)

It comes from the actual transported envelope volume d³, amplitude k
and evaluated derivative cost k^(-1), with global mean tails treated
separately. Combining (5),(6) gives
r(beta-3/2)+27/8-5beta/2, the exponent used in (1). The actual error is
projected using H3 interpolation, with exponent
(3J-15)/16-C_3 eta-o(1). This is the explicit final step behind (1).

By contrast, the report's purported ceiling r<=9/4 is obtained by
substituting a ball radius R=|b|/strain=Lambda^(-1) into a **whole-wave**
L2 estimate. The logarithmic host supplies a small ball on which the
gradient is close to an affine matrix. That is an observation core,
not the support radius of the receiver. The transported bump plateau
contains a much larger ball, and its whole advected envelope has volume
of order d³ because q is incompressible. The complete compact curl
packet extends outside the affine core. Pressure corrections may have
global tails as well.

Thus an inferred core contribution |b|R^(3/2) neither supplies nor
equals the whole packet L2 norm. A C1 affine-core estimate does not
by itself provide its H^r derivative profile either. Conditionally,
if the same envelope retained a comparable leading amplitude |b|
through a proposed later time, its leading whole-envelope L2 scale
would be |b|d^(3/2), not |b|Lambda^(-3/2). Whether it does so at cap
is precisely an unproved geometric/viscous question.

Even a valid later lower bound exceeding the **old** upper bound (6)
would show that this old bound cannot persist there. It would not show
that ordinary finite Sobolev regularity or all finite-order methods
fail. A frequency-following weighted norm is a reasonable tool to try,
but r<=9/4 is not a proved source-level obstruction to alternatives.
Likewise R Lambda=1 under the report's definition is a tautology,
not evidence that the whole envelope has shrunk to one wavelength.

## 4. Physical scaling is mostly correct, with essential comparisons

The exact conversion is

    y=h^(-10)x, s=h^(-24)t, u(t,x)=h^(-14)Q(s,y).

Consequently rescaled velocity, gradient, frequency, time and unnormalized
L2 acquire factors h^(-14), h^(-24), h^(-10), h^24 and h, respectively.
For the derivative-L2 term of order r the multiplier is h^(1-10r).
The report correctly gives the receiver's physical frequency
h^(-23/2) and the invariant gradient-time clock. The same invariance
applies to N's clock in (4); pointwise physical smallness does not follow.

For reference, the current generated band's physical frequency is
h^(-45/4+o(1)). The lower velocity and symmetric-strain scales in (3)
become h^(-49/4+o(1)) and h^(-47/2+o(1)); the corresponding initial
upper scales are h^(-12+o(1)) and h^(-93/4+o(1)). Ratios are unchanged.
These belong to a varying-data family at fixed physical viscosity.

The physical cutoff corresponding to (1) is h^(-10-beta), and its
gradient bound is h^(P-24). Since P is arbitrary and fixed, a larger
rescaled P can pay this conversion. It still gives no later-time bound.
The report's hypothetical cap frequency h^(-2) is rescaled and would
mean physical frequency h^(-12); it is not the physical h^(-2) scale.

Finally, the selected sufficiently thin actual profile has
mu=2/3+O(r_j), as recorded in the outgoing matching source. The profile
is fixed before h tends to zero. Thus its positive exponent is bounded
away from zero in this selected class, rather than being an unspecified
exponentially small quantity in the profile index. Profile-dependent
constants remain fixed; this fact does not extend the actual-q time
window or justify an arbitrary choice mu=1 for that actual profile.

## 5. What can be concluded about the proposed seed deficit

Even accepting the report's model-level amplitudes temporarily, its
displayed leading powers imply

    required/supplied = h^(7/4)/h^(5/2) times subpower factors
                      = h^(-3/4+o(1)),                         (7)

not h^(-1+o(1)). A fixed polylogarithmic factor cannot change the limiting
power -3/4 to -1. A finite-h numerical effective exponent is not an
asymptotic exponent. Neither quantity in (7) is currently an actual
cap-time source theorem or a necessary threshold for every unforced
next-stage mechanism.

The forced ansatz's strain-matched seed condition is not a universal
lower bound on useful seeds. Before declaring a deficit one needs a
specified actual outgoing state, an identified receiving phase and
polarization, a duration, damping, and a proved gain/output requirement.
A smaller seed may in principle require a larger later gain; no such
gain is supplied here, but it is also not excluded by that analogy.

The separate full-support preparation theorem does prove

    ||D³ Z_2,h(0)||infinity >= c_F k^(-2) ell^(11/8)              (8)

for the stated fixed-profile prepared receiver and its phase-coverage
hypotheses. For k=h^(3/2), its physical counterpart is
h^(-47)ell^(11/8), including the h^(-44) derivative conversion.
The theorem excludes the specified disjoint or quantitatively
noncancelling direct preloading on a common compact domain when these
costs diverge. It does not prove a sum lower bound on the L-infinity
C3 norm of an arbitrary overlapping superposition. Even for disjoint
supports the automatic lower bound is the supremum of individual
costs, not their sum. That supremum already diverges in the restricted
construction, so no unsupported sum is needed.

Reusing (8) at hypothetical later stages requires their actual
preparation geometry and common physical scaling, not just replacing
k by successive powers of h. Arbitrary cancellation, changed geometry,
generated seeds and inherited states retain their stated open scope.

## 6. An actionable next estimate without assuming its conclusion

Keep the same q, Q and original datum. Fix a proposed later time T_h
and state the result initially as an a priori estimate on their common
smooth lifespan up to T_h; continuation must then be proved separately.
The report's cap time can be a **model target**, not an assumed actual
lifetime or actual coefficient history.

First extend actual q and its finite spatial jets, deformation and
cotangent/polarization comparison on that interval. Its present
subpower clock is an input to every existing profile estimate. An
inviscid multiplier along the steady reference profile does not replace
this actual-q estimate at the proposed longer time.

Next define a complete packet approximation W_app from that transported
phase, including its curl, full mean and pressure corrections. Specify
its whole envelope and viscous clock. A precise candidate relative bound
is

    sup_[0,T_h] ||grad[Q-q-W_app](t)||infinity / Sigma_h(t)
                         <= h^a,  a>0,                        (9)

with Sigma_h an explicitly chosen positive carrier-strain scale and
with a separately stated velocity estimate. This is a proposed theorem,
not a consequence of the current C1 bound. The accompanying weighted
Sobolev norm must specify its spatial localization, frequency width,
finite derivative order and commutators. A scalar center frequency
alone does not control an anisotropically deformed envelope.

For generated output, retain (2). At a proposed endpoint use an explicit
band and a real solenoidal adjoint test Psi_T. The signed source to
estimate is exactly

    <N(T),Psi_T>
      =integral_0^T integral (W tensor W):grad Psi(t) dx dt,     (10)

where Psi is the full backward adjoint of B_q-epsilon Delta with
endpoint Psi_T. The original sign result evaluates one such special
pairing through t_eta. A new estimate must either extend it or name a
different actual source, with all changing covectors and row norms paid.
It must also compare against exact q and Z before asserting an
observable generated band of full Q.

Only after specifying the next receiver can (10), or a proved upper
bound on it, be compared with that receiver's necessary/sufficient seed
size. This preserves the report's productive idea—follow the actual
state farther—without turning a model extrapolation into a no-go result.
No claim that pressure or nonlinear feedback is negligible is an input
to this contract; both must be estimated in it.

## 7. One further exact correction in the report

The recommended formalization target in its section 6 prints
|tr S³|<=2|S|_F³/(3sqrt(6)). This is false for S=diag(2,-1,-1):
the left side is 6 and the stated right side is 4. The sharp coefficient
is 1/sqrt(6). The repository's c_B=4/(3sqrt(6)) includes the separate
Betchov factor 4/3; it is not the cubic inequality's coefficient.
This finite-dimensional negative control should precede formalization.

## Source pins at this read

| Source | SHA-256 |
|---|---|
| Finite-depth profile | `909e21a42ddb67636f2f08e695111d07005ee0935c9d36a8991a2e7c0fa75c4e` |
| Initial-time normal transport | `f5da67ed4561a1cfd90a9f9272a09bfe954eeb1293a186cce428cca40b689d0d` |
| Postfocus normal source | `1682477e11fb3dedaa1bec477e921dd0dfe7373e2a10488d158c9244b6a7e320` |
| Actual coarse band | `2b2f6aeeef78374ff91b72322163f637d90e7b416e84a427d264c46c8f6740ea` |
| Logarithmic host | `2d06d4bf6edc170b79728e9494fb2ccfe7af3c803ad8535636359016b5f01761` |

Existing review files pin earlier mathematical source versions; their
later introductory review labels are documented separately. This note
does not silently promote those AI-agent reviews to external acceptance.
