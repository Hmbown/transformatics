# Review of the smoothly forced stage analysis

8 September 2026. Three independent agent reads of the written calculations, followed by root integration. All pass within the scopes stated below. This is analytic review by AI agents, not independent expert acceptance or a formal PDE certificate. Both unforced ROOT and FORCED-D remain OPEN.

## Canonical notes and changes incorporated

- [forced admissibility](../navier-stokes/forced-admissibility.md); final source SHA-256 `b03e82c8fd39f98352e53e7aecd4bd5a26138e57e53a7f64ba8cf2325a339115`.
- [forced viscosity](../navier-stokes/forced-viscosity.md); final source SHA-256 `4289c87fad83fbe9e779a1894aa9985f6879eaf43067cec5491c03a8144dd26a`.
- [forced reset](forced-reset.md); final source SHA-256 `584ea5661478866f00abcd1793909a4168ab55a42e7f29b89bb74419c9e5440a`.

The all-profile principal diffusion factor was corrected to `exp(-n^2 D)` for Fourier index n; a general profile evolves by heat. The selected material-center zero-return survives this principal correction. The finite-reset conclusion now says that the current estimates do not establish terminal force regularity; a diverging upper estimate is not an impossibility proof. Canonical copies replace machine-specific links with relative source links. Original review hashes below identify the version read; the final hashes above include those recorded amendments.

Root integration additionally made the activation-policy qualification explicit: an upper estimate for activation force is not a universal force lower bound. The next-stage contract also now requires a compatible embedding of a local axisymmetric chart into the fixed periodic domain, including periodic pressure. These clarifications narrow the application of the reviewed formulas; they add no construction theorem.

The [exact-control script](checks/check-profile-extension.py) passes all five groups. Two new groups check physical force/norm scaling and the full time-cutoff defect, both axisymmetric diffusion operators, the shared n² symbol, a principal heat return with a time-dependent noncommuting host, and the affine curl normalization. Deliberately omitting a Jacobian, either cutoff term, or the n² factor makes its corresponding control fail. These are finite algebra checks, not certification of a complete viscous stage.

## Force scaling and terminal extension

## Independent review of the forced-admissibility budget

8 September 2026. Reviewed `nse-forced-admissibility-budget-20260908.md`, SHA-256 `b03e82c8fd39f98352e53e7aecd4bd5a26138e57e53a7f64ba8cf2325a339115`. No DNS.

**Verdict: PASS as a sufficient force-admissibility and scaling analysis.** I found no mathematical correction needed. It does not construct an infinite NS trajectory, show that the current residual satisfies these force norms, or infer a lower bound from a diverging upper estimate.

### Exact force and norm scaling

I rederived the change of variables directly from the physical NS equation. With `u=A U`, `y=sx`, `tau=As(t-t0)`, the time, advection and pressure terms have factor `A^2 s`, while viscosity has factor `nu A s^2`. Thus `epsilon=nu s/A` and `f=A^2 s R`, with the displayed sign.

The unnormalized three-dimensional L2 Jacobian contributes `s^(-3/2)`, and time integration contributes `(As)^(-1)`. Consequently the physical `L1_t L2_x` factor is `A s^(-3/2)`, not `A^2 s`. At `A=h^(-14), s=h^(-10)` it equals `h`. The residual `h^(31/8)E_h` therefore gives physical force norm `h^(39/8)E_h`. This works on the complete expanding torus and does not assume compact support for the nonlocal mean.

I checked the five separate pointwise residual powers from amplitude/derivative products: `2,9/4,5/2,11/4,13/4`. Thus the coarse supremum residual is `h^2 E_h` and its physical force bound is `h^(-36)E_h`. The note correctly treats this as an uninformative diverging upper bound, not an actual blowup lower bound. There is no contradiction with the small integrated L2 bound.

Physical mixed derivatives multiply the force by `s^r(As)^m`, giving exactly `h^(-38-10r-24m)`. The resulting required residual threshold `h^(38+10r+24m)` and the illustrative derivative-cost exponents `23r/2+51m/2` are correct. The note explicitly labels the latter derivative rule and availability of deeper correction gains as unproved inputs.

The force-norm counterexample also checks: its point amplitude is `2^n`, spatial L2 factor is `2^(-3n/2)`, and time width is `2^(-4n)`, giving `2^(-9n/2)`. Supports can be disjoint while the pointwise peaks accumulate at the terminal time. It is used only to separate function-space norms.

I separately checked these exponents with exact rational arithmetic. This is bookkeeping evidence, not PDE certification.

### Pressure, activation, and telescoping

If the original residual is `R=P R+grad psi`, replacing `Pi` by `Pi-psi` yields residual `P R`; the pressure sign is correct. The fixed-torus pressure convention retains the mean-force/mean-velocity identity. The official Clay erratum requires periodic pressure, so an affine pressure is not a valid way to change that identity while retaining the same periodic problem.

Expanding the NS defect of `U_old+w` gives all five terms in (8), including both old/new interactions. Because a time-only cutoff commutes with the spatial operators, the defect of `U_old+chi w` with pressure increment `chi pi` is precisely

    chi delta f+(chi^2-chi)(w.grad w)+chi' w.

The nonlinear cutoff term and the activation derivative are both necessary. The discussion correctly charges shrinking time-transition derivatives and distinguishes later smooth-force creation of a packet from an impulsive insertion. No assumption of zero force is imposed on the newly authorized forced lane.

The R3 caution is also correct: a periodic field is not Schwartz, and a compact curl residual does not by itself establish compact or rapidly decaying physical force after a chosen pressure recovery. The compact smooth velocity-path example with pressure zero is a valid kinematic admissible-force construction, but it supplies no singular solution.

### All-orders terminal extension

The one-sequence criterion is sufficient. For any fixed order q, only finitely many indices fail the admitted-order condition. The all-order bounds on those fixed early increments handle that finite head. The remaining derivative series converges uniformly by summability. Repeating at order q+1 gives a uniformly bounded time derivative and hence uniform terminal limits for all order-q derivatives. Spatial and temporal fundamental-theorem-of-calculus identities identify them with the derivatives of the extended force. This also preserves a common compact support or periodicity.

The explicit extension (11) is a valid smooth-jet construction. For the mth term and a time derivative of order b<=m-1, its cutoff-scale bound contains a positive factor `delta_m^(m-b)`. At each m there are only finitely many requested spatial derivatives, so one can choose decreasing `delta_m` to make the term small in all total orders through m-1. Every fixed-order tail converges uniformly; the finitely many lower terms have their prescribed Taylor jets because the cutoff is constant near zero. All cutoffs can be supported before time `T+1`. The force, rather than the potentially singular velocity, is what extends.

The scalar schedule is properly conditional on a real stage theorem for the complete force. An independently chosen scale for each derivative order would not suffice, and the note does not make that inference. The requirement to meet all lifetime, support, ordinary-viscosity and previous-stage dependencies is essential: the displayed diagonal arithmetic does not prove those parameter constraints have a common solution.

### Scope

The exact scaling and sufficient force-gluing criterion are established at their stated level. The existing finite `L1 L2` estimate remains useful, but it does not discharge terminal smooth forcing. The unforced problem and the smoothly forced Clay-D target remain separate. In particular this review does not promote a forced result to an implication about the unforced ROOT.

## Finite steering and stationary holding

## Independent review of the forced reset budget

8 September 2026. Reviewed `nse-forced-reset-budget-20260908.md`, SHA-256 `39ff614c7c524bb393495ad24003294261d4f8aad1fc477c92ff17a963b569c7`. Full independent mathematical read of sections 1-6. No DNS.

**Verdict: passes at its stated exact finite-steering and restricted stationary-holding scope.** The product estimates, terminal pulse criterion, and stationary lower bound are correct. They do not establish a dynamically growing infinite forced cascade, and their upper estimates are not general force lower bounds.

### 1. Exact equations and derivative products

For u=V+eta z with time-independent z, expanding the momentum equation gives exactly

\[
f-f_V=\eta' z-\nu\eta\Delta z
+\eta[(V\cdot\nabla)z+(z\cdot\nabla)V]+\eta^2(z\cdot\nabla)z.
\]

No extra pressure is necessary when the entire displayed expression is retained as force. Divergence of this identity automatically supplies pressure compatibility. The compact support of every added term is preserved despite a noncompact base V, because each term contains z or a derivative of z. The existing f_V still needs its own admissibility bounds. A periodic Leray change of pressure is allowed; compact support of its whole-space force projection would require a separate proof.

For trace-free M,

\[
\operatorname{curl}[x\times(Mx)]=-3Mx.
\]

Thus the printed compact curl construction equals Mx in its inner ball and has spatial derivative size C_j |M| r^(1-j). Its force is (M'+M squared)x in that ball for pressure zero. The cutoff-zone diffusion and nonlinear terms have exactly the powers in (4). Bounds for time derivatives of M must match the fixed interpolation time scale, as stipulated.

The two cross-product sums in (5) are complete. Distributing m spatial derivatives on V dot grad z gives B_j a r^(-(m-j+1)); distributing them on z dot grad V gives B_(j+1) a r^(-(m-j)). Multiindex/binomial coefficients are covered by the fixed C_m. The pure insertion, viscous and nonlinear terms have powers a Delta^(-1)r^(-m), nu a r^(-m-2), and a squared r^(-m-1).

For p time derivatives, every term with l derivatives on V is bounded using B_j^[p] Delta^(-l), while the remaining derivatives on eta cost Delta^(-(p-l)). Their product is exactly Delta^(-p) B_j^[p]. Differentiating eta' adds the extra Delta^(-1), and derivatives of eta squared obey the same scale by Leibniz. Thus the proposed mixed estimate follows with C_(p,m), without dropping a base time derivative. It is correctly identified as an upper estimate.

### 2. Terminal-flat force pulses

For disjoint time intervals accumulating only at T, with smooth zero extensions at all individual endpoints, the printed hypothesis that every mixed derivative supremum tends to zero is sufficient. Away from T the sum is locally finite. At T the piecewise derivatives converge uniformly to zero. Applying the same hypothesis to the next time derivative and using the fundamental theorem of calculus identifies the derivative at T; induction establishes every mixed derivative and flatness. On a common compact spatial support this is compatible with space-time rapid decay after zero extension. On a torus it gives periodic forcing with compact time support.

The explicit super-exponentially attenuated example satisfies all the bounds for each fixed p,m, including the viscosity term. Its velocities and strains tend to zero, so it illustrates attainability of the force criterion without suggesting breakdown. The separate warning about persistent inserted seeds is essential: after a seed's ramp, its diffusion, nonlinear self-interaction, old/new cross terms and the cumulative state still exist. Disjoint ramp intervals do not by themselves make the full force a disjoint pulse sum.

For overlapping persistent increments, mixed-norm summability is sufficient together with the stated terminal regularity conditions. A fixed early increment must itself have terminal limits; the source explicitly retains this proviso. A smooth nonzero terminal force is allowed, so zero terminal jets are a convenient sufficient case rather than a necessary Clay condition.

### 3. Stationary compact holding really has a force lower bound

For z_r=a Z(x/r), the energy pairing on a stationary plateau is

\[
\int f\cdot z_r=\nu\|\nabla z_r\|_2^2.
\]

The advective pairing vanishes by incompressibility; the pressure pairing vanishes by integration by parts against compact solenoidal z_r. The scalings are

\[
\|\nabla z_r\|_2^2=a^2 r\|\nabla Z\|_2^2,
\qquad \|z_r\|_1=a r^3\|Z\|_1.
\]

They give the positive lower bound c_Z nu a/r squared. It is a bound on the complete force, so it cannot be evaded by cancellation between its viscous and nonlinear terms. The fixed nonzero profile is important.

With pressure zero, f is supported in a ball of radius C r. At a component attaining a fixed fraction of its supremum, follow a straight segment of length at most C' r to outside that support. All endpoint derivatives vanish. Taylor's integral remainder yields

\[
\|f\|_\infty\le C_m r^m\|D^m f\|_\infty.
\]

Combining it with the energy lower bound proves the source's higher derivative lower bounds. These higher bounds use compactness of the chosen pressure-zero force; the energy bound itself permits any legitimate pressure. The argument concerns holding that complete compact field stationary, not adding a perturbation to an evolving energy-supplying background. A time derivative can cancel the diffusion term in the latter problem.

For an affine-core amplitude a=M_*r this gives c nu M_*/r. Consequently a sequence of such stationary fixed-shape held cores with M_* increasing and r decreasing cannot have bounded force at its accumulation time. This is an actual restricted obstruction, distinct from the upper estimates in sections 2-3.

### 4. Physical powers and remaining scope

All printed h exponents in section 6 check:

- amplitude h^(-25/2)ell^(-13/8);
- initial wavelength h^(23/2)/ell;
- initial strain h^(-24)ell^(-5/8);
- naive viscous insertion size nu h^(-71/2)ell^(3/8);
- naive ramp size h^(-73/2)ell^(-13/8)/(log ell);
- outgoing stationary-core force lower bound nu h^(-71/2)ell^(11/8).

The first two force sizes are upper-budget terms for the manufactured ramp, not lower bounds for an actual unforced or dynamically corrected solution. The final one is a lower bound only under section 5's stationary fixed-shape replacement.

One wording adjustment is recommended in the concluding paragraph: change “the current data do not meet the all-derivative terminal-force criterion” to “the current estimates do not establish the all-derivative terminal-force criterion,” except when explicitly referring to the proved stationary-holding lower bound. The surrounding text already makes this mathematical distinction; this change would prevent the conclusion being read as an impossibility inference from a divergent upper bound.

The note supplies a concrete exact finite reset and a genuine all-orders target. Infinite dynamic compatibility, a growing velocity with a smooth common force, and the unforced zero-defect condition remain unproved.

## Ordinary viscosity and the principal return

## Independent review of the forced-viscosity route

8 September 2026. Reviewed `nse-forced-viscosity-route-20260908.md` and the locally saved released Euler manuscript text, especially its (3.3)–(3.4). No flow runs. This is an analytic review, not a formal certificate or independent verification of the entire released Euler paper.

**Verdict: PASS at the written obstruction/principal-identity/conditional-budget scope, after the author corrected the all-Fourier factor in (17) during review.** The correction preserves the proposed selected-center principal zero-return mechanism. It does not supply a complete viscous recursive stage.

### 1. Direct transfer and pressure obstruction

Keeping Euler velocity and pressure requires f_NS=f_E-nu Delta u, with the minus sign as printed. For a smooth velocity supported in a fixed ball B_R, Newton inversion and |grad G(z)|=1/(4 pi |z|^2) give

    ||omega||infinity <= 2R ||Delta u||infinity.

The integral is over B_(2R) when x lies in the support; outside the support omega=0. Thus the same-pressure C0 lower bound (5) follows from the released divergent-vorticity conclusion and bounded f_E.

Changing pressure gives nu Delta omega=curl f_E-curl f_NS. Applying Newton inversion to compact omega gives ||omega||infinity<=2R^2||Delta omega||infinity, since the Newton kernel integrates to 2R^2 over B_(2R). Therefore (8) correctly rules out bounded first spatial derivatives of any proposed smooth NS force, regardless of pressure gauge. It does not overclaim C0 failure in every gauge.

The fixed-torus Leray/elliptic alternative also checks. Smooth all-order force bounds control Delta u after projection; the spatial mean is separate and is controlled by its averaged evolution. On R3 the compact-support assumption avoids nondecaying harmonic ambiguities.

The bounded-velocity continuation boundary is valid: testing NS against -Delta u and applying Young gives (9), and bounded velocity with a smooth L2 force gives a finite H1 bound. Standard strong H1 continuation then excludes classical breakdown. Thus preserving the released bounded-velocity conclusion would itself defeat a singular ordinary-viscosity adaptation. This statement needs the finite-energy/force norms explicitly retained in the note.

### 2. Affine heat/control identity

For the prescribed affine wave, D_(Ax)(xi.x/k)=0, the transverse wave self-advection vanishes, and (b'+Ab)F=2xi c F+rF. The wave pressure cancels 2xi c F, while the profile heat equation cancels nu |xi|^2 b F_ss/k^2. The leftover terms are exactly rF+b gamma plus skew(A'+A^2)x. Hence (10) is correct, including the symmetric quadratic pressure and arbitrary trace-free A.

The heat clock and rounding bound are correct. A nonzero Fourier mode n is attenuated by exp(-n^2 D), so a single-mode strain gains its actual amplitude factor, its covector ratio, and that attenuation. Spatial jet factors and physical time derivatives must still be counted; the note expressly does so.

The finite localized-profile estimate (13) uses the previously independently reviewed complete residual. Its small L2 remainder is not a smooth all-order physical-force gluing theorem. Calling an approximate residual an external force would require stronger norms than the unforced comparison theorem used.

### 3. Axisymmetric operators and the required full-profile correction

Direct cylindrical differentiation gives

    D Gamma=nu(Delta_cyl-2r^-1 partial_r)Gamma+r f_phi,
    D Xi=nu(Delta_cyl+2r^-1 partial_r)Xi
                    +r^-4 partial_z(Gamma^2)+(curl f)_phi/r.

Since Delta_cyl=partial_z^2+partial_r^2+r^-1 partial_r, these are exactly (14). With y2=r^2/2, partial_r=r partial_2 and partial_r^2=partial_2+r^2 partial_2^2. Thus the first operator becomes partial_1^2+2y2 partial_2^2 and the second adds 4partial_2. Equations (15)–(16) therefore have the correct shared principal symbol and distinct lower-order drift.

The released wave uses Gamma increment T F and reduced-vorticity increment proportional to Omega F_s, with the primitive relation in its streamfunction. For Fourier index n, that differentiated-profile convention normalizes the two components so the principal coupling matrix B is the same; both components acquire diffusion n^2 d_visc. Accordingly the correct all-mode identity is

    R_NS,n'=(B-n^2 d_visc I)R_NS,n,
    R_NS,n(t)=exp(-n^2 integral d_visc) R_Euler,n(t), n!=0.   (A)

The original draft of (17) without n^2 was exact only for n=±1; the author has now corrected it. A general fixed flat profile is not restricted to those modes. An equivalent full-profile formulation keeps the inviscid two-component amplitude and evolves the common profile by H_D=exp(D partial_s^2); differentiation of that profile commutes with H_D.

Crucially, if the inviscid selected central branch has Omega_out=0, (A) makes every Fourier mode's corresponding output zero at that material center. Thus the full principal selected-center zero-return is preserved; a whole-envelope zero is not asserted. But the circulation profile becomes H_D F, not e^-D F. The correction changes the quantitative retained profile, not the useful projective return conclusion. Spatial variation of D and the metric still produces lower-order terms, as the note correctly lists. None of this certifies persistence of the old background or the complete selected history under viscosity.

I sent correction (A) to the author during review and confirmed its incorporation, together with the explicit selected-material-center qualification. This is the only substantive formula correction I identified.

### 4. Activation and gain budgets: their exact logical scope

Under the stated bounded-covector and supplied propagator assumptions, (18) is an upper bound on achievable principal amplitude, and D>=c nu K^2 Delta. Combining that upper gain with the deliberately chosen insertion bound (20) yields (21). The maximum inviscid rate G<=Gamma Delta then gives (22). These are conditional mechanism constraints, not universal inequalities for every externally forced NS solution.

In particular (19) is a sufficient cost estimate, not a lower bound on every possible activation force. Thus the claimed necessary gain is necessary within the policy a_in<=eta Delta_act/(C_p Omega^p), not a proof that every activation satisfying an actual force bound must pay that exact inverse estimate. The draft's wording and surrounding restrictions identify the chosen policy; this distinction should remain explicit in any canonical summary.

For a fully literal use of (19), a_in must bound the complete localized velocity/profile being activated, and Omega must bound its normalized mixed derivatives as well as the base-flow, phase, cutoff and pressure contributions. A leading amplitude alone with an arbitrarily narrow envelope would not give (19) at p=0. The draft already conditions application on inclusion of the full curl/pressure costs; no unconditional localization estimate is supplied there.

If a fixed-core rounding requirement forces D<=C/H and the desired logarithmic gain is at least cH, where H is comparable to p log K and positive, then Gamma Delta>=cH and nu K^2 Delta<=C/H imply Gamma/(nu K^2)>=c' H^2. This verifies the restricted model estimate (23). Other amplitude, tolerance and clock-history logarithms cannot be dropped when they dominate H. The note expressly allows those terms and does not claim (23) for every possible reset.

The simultaneous all-order schedule requirement is essential. A separate frequency choice for each derivative order does not construct one smooth terminal force. The written conditions remain an unproved construction target rather than evidence that the current stages meet it.

### 5. Reset witness

The profile-reconstruction control gamma=-nu K^2|xi|^2 F_ss is correct for keeping an unheated profile in the affine equation. On the profile's non-flat transition region, its mth spatial derivative has the stated nu |b|(K|xi|)^(m+2) factor. A small core avoids that region locally but not in a global forcing supremum.

For A=lambda p tensor n with p.n=0, A^2=0, omega=lambda n cross p, and A omega=0 identically, even if p,n vary in time. Since affine vorticity is spatially constant, transport and diffusion vanish. The exact vorticity equation is omega'=curl f, giving (24)–(25) by integration and the triangle inequality. The endpoint difference is indispensable: an orientation change preserving n cross p has zero lower bound, exactly as the author notes. General ambient stretching is not covered by this special path.

### Final scope

After correction (A), the note provides a valid obstruction to literal smooth-force Euler transfer, an exact fixed-background principal heat/return identity, and checkable conditional stage budgets. It establishes neither a complete ordinary-viscosity reset stage nor an admissible infinite terminal force. The proposed next task—full axisymmetric residual, compact force recovery, derivative-depth improvement and a nonempty parameter set—is appropriately narrower than claiming a forced NS solution.
