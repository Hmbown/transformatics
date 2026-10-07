# Review record: localized profiles and the next-seed constraints

8 September 2026. These are separate AI-agent mathematical reviews, with a coordinating-agent read of all four constructions. They are not external expert acceptance or formal ODE/PDE certificates. The original-time finite theorem remains the input; ROOT and the newly authorized smoothly forced target remain open.

## Localized profile extension

Canonical [derivation](../navier-stokes/localized-profile.md). Reviewed source SHA-256 `77e66606f3c5d8bf47ec42d474e1febead5657120b6bb5c7793e2b02124c5417`.

8 September 2026. Reviewed `nse-localized-profile-calculus-20260908.md`, sections 1–11, including equations (1)–(38), against the prepared-phase/whole-support inputs of the original-time handover. No flow simulations.

**Verdict: PASS at the written finite supplied-seed scope.** I found no missing term in the residual, phase mean, pressure, or central-clock construction. The derivative hierarchy and h^(31/8) comparison margin close with the stated fixed smooth profile and existing geometric inputs. The material-clock identities also check; its extra finite phase-derivative hierarchy is sufficient as described. This review does not certify an infinite construction, arbitrary profiles with uniform constants, or a usable descendant reset. The endpoint conclusions reviewed here include (37) and the subsequently added radius-c_0 k spatial estimate (38), but no time-dependent affine-neighborhood theorem.

## 1. Exact identities rederived

### Differential calculus and lift

The evaluation operator E[v]=v(t,x,S/k) obeys D E[v]=E[Dv] because D S=0. Differentiating twice in x gives exactly the L1 operator in (5), including (div xi)v_s/k. All slow derivatives must continue to hold s fixed and differentiate a variable clock.

Let v=partial_s^(-1)a and V=-(xi cross v)/|xi|^2. Tangency implies xi cross V=v. Therefore k curl_physical E[V]=E[a+k curl_x V]. Also

    xi.curl V = div(V cross xi) = -div v,

using curl xi=0. This proves both identities in (9), including the sign of its longitudinal correction. Phase means commute with the slow derivatives; the zero-mean primitive makes all lifted profiles zero in phase mean.

For V=C Q_tau, spatial differentiation gives exactly

    curl V=(curl C)Q_tau+(grad tau cross C)(f_tau)_s.

The second term cannot be dropped for a material clock. The zero-mean primitive convention is consistent with the earlier observation that heating a quadratic core adds a time-dependent constant: that constant is retained in the localized potential, not discarded as a pressure gauge.

### Forced pressure and complete residual

The leading forced profile satisfies

    (D+A-kappa partial_s^2)g
      =2xi(xi.Ag)/|xi|^2-Pi_xi H.

The fast pressure gradient in (12) is

    -xi(2xi.Ag+xi.H)/|xi|^2.

Their sum is precisely -H, including a nontransverse H. There is no missing longitudinal pressure term. The difference between material phase diffusion and physical fast diffusion is omega partial_s^2 W_g, with the positive sign omega=kappa-rho. Expanding the remaining Laplacian produces all four slow/mixed viscous terms in (14). The k times slow gradient of the pressure primitive has the displayed negative sign.

The curl commutator in (15) also has the correct sign:

    (D-kappa partial_s^2)curl V
      =curl((D-kappa partial_s^2)V)
         +[D,curl]V+(grad kappa) cross V_ss.

Consequently Dcal r_g is expressible with spatial derivatives of g,H,xi,q and the clock. No material derivative of H, second time derivative of q, or pressure time derivative is silently required. This is important for the stated finite derivative count.

### Nonlinearity and mean

Expanding (a+k r).grad^k(a+k r) and using xi.a=0 gives exactly (16). The surviving fast terms are (xi.r)a_s and k(xi.r)r_s. They are not set to zero by tangency of a.

Since div^k W_a=0, its quadratic advection is div^k(W_a tensor W_a). Averaging in phase removes its phase derivative, yielding (17) as a pointwise identity in slow x. No spatial/phase-average identification is needed.

For odd f, Q and f_s are even. Thus the b/c and b/e cross moments vanish. Integration by parts gives <Q f_s>=-<f^2>, and the heat equation gives the two moment derivatives in (18). These facts reproduce the entire stress formula, including its negative c/e cross term and the derivatives of its variable-clock coefficients under div_x.

Substituting H from (21) cancels the primary linear residual, N(a)-Q0, and precisely the fast mean-to-primary term (m.xi/k)a_s. Expanding the remaining mean-to-primary term leaves m.grad_x W_a+(m.xi)(r_a)_s. All other primary/g, mean/g, and self-interactions appear once in (23). The global mean's viscous term is correctly left as -epsilon Delta m. I found neither an omitted interaction nor a double-counted cancellation.

## 2. All Fourier modes and the derivative hierarchy

For every n!=0, the scalar factor -kappa n^2 commutes with G along a material label; (30) is therefore the exact variation-of-constants formula. Kappa>=0 gives contraction, not growth. The primitive divides only by a nonzero integer phase index; there is no inverse small physical frequency. Reality follows from conjugacy. Spatial support remains transported because only phase diffusion occurs in this corrector equation.

The central-clock construction is particularly clean: slow differentiation creates no n^2 D_x kappa term. Differentiating the transport and G coefficients generates a triangular spatial hierarchy. Its top growth rate is controlled by the actual q gradient, while weighted lower coefficients involve powers of d/h or finite subpower factors. This does not exponentiate E_h itself.

For the material clock, assign spatial order j phase weight M+2(r-j). A commutator with j-l>=1 derivatives on kappa needs two more phase derivatives of the order-l field. Its available weight exceeds the requested weight by at least two, so the hierarchy closes. The top dissipative term remains negative. Fixed F in A_80 supplies ample phase regularity for the stated finite orders; no Fourier truncation or analyticity limit is being used.

The slow derivative count also checks:

* R[a;0] uses at most three slow derivatives of its primary potential; 13 source derivatives require at most 16 primary derivatives.
* Q0=div of the full stress requires at most 18 primary/clock derivatives for its H16 source estimate, since r_a already contains one derivative.
* An H12 norm of the lifted g needs g through spatial order 13. Pointwise forcing derivatives involving m are covered by mean H16 and the corresponding scaled interpolation.
* q C24 leaves room for these differentiated transport, mean and pressure estimates; b,xi C18 covers the source requirements. The material clock's finite jets follow from that same transport hierarchy.

The mean remains global. Its energy estimates use the Leray-projected equation and its differentiated pressure, not an L-infinity bound for Leray projection. The weighted coefficient d^(j-1)||D^j q||infinity is bounded by C_j m_h(d/h)^(j-1), with time integral O(ell). The global L2 estimates plus uniform Sobolev interpolation yield (31). Assigning the compact volume d^3 to m would be wrong, but the written product estimates use global mean L2 norms and do not do so.

## 3. Independent size checks

The main primary/corrector interaction after tangency cancellation has pointwise size k^3/d^2 and support volume O(d^3), giving k^3 d^(-1/2)=h^(31/8). The fast mean-to-g term has that same size and is retained. Global mean self-interaction instead uses

    ||m||infinity ||grad m||2
      <=(k^2/d)(k^2 d^(-1/2))E_h
      =k^4 d^(-3/2)E_h=h^(33/8)E_h.

For the central mismatch, |omega|<=(epsilon/k^2)(d/h)E_h, so multiplying by primary L2 size k d^(3/2) gives h^(37/8). Multiplying by corrector L2 size k^2 d^(1/2) gives h^(39/8). The mixed primary viscosity epsilon d^(1/2) is h^(37/8); the leading mixed g viscosity epsilon k d^(-1/2) is h^(39/8), while its slow/curl-mixed terms and mean viscosity epsilon k^2 d^(-3/2) are h^(41/8). The author corrected this distinction in the table during review; the leading residual exponent is unchanged. The material curl commutator has the stated h^(39/8) size for the primary and is smaller for g.

The exact expression Dcal r_g contains a slow derivative of H multiplied by k. For principal H size k^2/d this produces k^3/d^2 pointwise, agreeing with the leading residual rather than introducing a new loss. Derivatives of the improved zeroth-order omega bound need not preserve its d/h gain: their weaker bounds still fit the weighted H source hierarchy. This distinction is made explicitly in the note.

These checks validate (33) with a finitely enlarged E_h. Source terms placed in H are not independently added again to the final residual.

## 4. Strong continuation and endpoint scope

The leading gradient history is bounded by C_F times the existing whole-support integral |b||xi|/k. Heat contraction controls the required phase derivative norm. All envelope, mean and g C1 terms are subpower multiples of h^(1/4) or smaller. Thus the integrated coefficient in relative energy is O_F(ell^(11/8)), not E_h.

The primary H12 scale is

    k^(1-12)d^(3/2)=h^(-117/8),

up to E_h and fixed profile norms. Lifted corrections are smaller. Combining residual L2 exponent 31/8 with the separate H12 continuation bootstrap gives

    (31/8)(19/24)-(117/8)(5/24)=1/48>0,

and the corresponding velocity exponent is 25/16. The finite H12 bound closes the smooth lifetime bootstrap; relative energy is not being used alone to assert strong existence. The unnormalized expanding-torus norms and uniform interpolation constants are the same ones required in the original proof.

At the terminal reference q particle, b and xi are actually constant on an inner plateau and the central heat clock is spatially constant. Hence r_a vanishes there with its local derivatives. Equation (37), including its sign, follows exactly. The heat-rounded derivative at phase zero tends to one exponentially in inverse heat time, and the remaining mean/corrector/tracking C1 errors tend to zero. This proves the stated finite added-strain conclusion at that prescribed location.

The added endpoint ball corollary (38) also checks. The fixed terminal covector has length 4, so 4c_0<a/2 keeps the entire radius-c_0 k ball within the flat phase interval; k/d->0 places that ball in the bump plateau. Its leading curl correction vanishes throughout, not merely at the center. The base gradient varies by at most C k ||D^2 q||infinity<=h^(1/2)E_h. Mean/g corrections and the global nonlinear tracking error supply the stated h^(1/4)E_h and h^(1/48)G_h bounds. Multiplying the exponentially small heat-rounding error by the polynomial terminal amplitude still gives an error below every fixed h power. Integrating the uniform gradient estimate along straight segments proves the velocity approximation after subtracting the actual Q center value. Thus this is a valid almost-affine ball at one endpoint.

**No remaining gap found for these written conclusions.** The statement does not yet give control on an entire transported descendant support over an additional time interval. A future reset must state and verify its own spatial/time jet claims. The supplied original wave still starts finer than the original host; this construction does not generate an unsupplied frequency or resolve the common smooth-datum obstruction. Constants depend on the fixed profile, and there is no uniform theorem over arbitrary changing F.

## Full-support seed cost

Canonical [derivation](flat-profile-seed-cost.md). Reviewed source SHA-256 `23f71b2879984651f720986481f749f8516a25b35718aba6610846418bff70b1`.

8 September 2026. Reviewed source: `nse-flat-profile-seed-cost-20260908.md`, SHA-256 `23f71b2879984651f720986481f749f8516a25b35718aba6610846418bff70b1`. Independent full mathematical read of sections 1-5, including the complete curl third derivative and the narrow-support argument. No DNS.

**Verdict: passes at its stated kinematic scope.** I found no load-bearing gap. Neither a nonlinear extension to general profiles nor a universal seed/cascade obstruction is proved or needed for its conclusions.

## 1. Exact curl sign and hypotheses

For tangent b and xi=grad S, C=-(xi cross b)/|xi| squared satisfies xi cross C=b. Hence

\[
k\operatorname{curl}(C Q(S/k+\theta_0))
=b F(S/k+\theta_0)+k(\operatorname{curl}C)Q(S/k+\theta_0)
\]

is exact when Q'=F. Oddness and fixed periodicity of F imply zero mean, so a periodic primitive exists. Its additive constant must be fixed as stated; changing it changes the localized velocity. The derivative budget b through order four and xi through order four covers D_c through order three, including the fifth derivative of S. No phase derivative has been silently omitted.

The central amplitude size a_h=k ell^(-13/8) follows from the selected unit input divided by its terminal normal gain of order ell^(5/2), then multiplied by k ell^(7/8). The less sharp neighboring jet bounds absorb fixed ell powers into E_h; the central lower bound is retained separately. Forward flow Lipschitz control sends an initial ball of radius c d/E_h into the prescribed final plateau, proving the inner plateau inclusion used in section 2.

## 2. Reaching a non-flat phase

Fixed periodic nonconstant F cannot have F''' identically zero. The selected phase theta_* and its nonzero third derivative are independent of h. Along the fixed direction e=xi(y0)/|xi(y0)|, on distance O(k/ell), the relative variation of xi dot e is at most

\[
C k h^{-1} E_h/\ell^2=h^{1/2-o(1)}/\ell^2=o(1).
\]

The corresponding relative amplitude variation is at most

\[
C(k/d)E_h/\ell=h^{1/4-o(1)}/\ell=o(1).
\]

This segment fits into the guaranteed plateau, since its length divided by d/E_h tends to zero. Its phase is monotone and covers any fixed period when the constant in the segment length is large enough. Thus a point with F''' nonzero and |b| comparable to a_h really occurs inside the actual prepared plateau. This uses the true transported geometry, not an affine replacement.

## 3. Complete third derivative

Both printed differentiation formulas are correct. In the principal part, the leading vector is b F''' (theta')^3. Projecting onto b/|b| at the selected point gives its magnitude without requiring a spatially constant polarization.

I independently recomputed the six remaining relative h powers as

\[
1/4,\quad1/2,\quad1/2,\quad3/4,\quad1,\quad3/4.
\]

For the seven expanded curl terms they are

\[
1,\quad3/4,\quad1/2,\quad1,\quad1/4,\quad3/4,\quad5/4.
\]

The potentially largest curl contribution is k D_c F'' (theta') cubed: its relative size is k/d times E_h, not zero. It is nevertheless o(1). The final term containing theta''' has relative power k^3 d^(-1)h^(-2)=h^(5/4), as claimed. All finitely many products of E_h can be absorbed by enlarging its fixed exponent C. The resulting lower bound is therefore

\[
\|D^3 Z\|_\infty\ge c_F a_h\ell^3/k^3
=c_F k^{-2}\ell^{11/8}.
\]

No center-only inference or omission of cutoff/curl derivatives enters this conclusion.

## 4. Narrow localization argument

Set f(t)=v dot Z(y0+t e). If f'(w)=f''(w)=0, exact integration gives

\[
f'(0)=\int_0^w t f'''(t)\,dt,
\]

and hence |f'(0)| <= w squared times sup|f'''| divided by two. The argument needs no estimate comparing the curl correction to its leading amplitude.

When the entire support lies in one flat phase slab, the stated monotone phase condition guarantees an exit within C a k/ell. Smooth zero extension gives the necessary vanishing derivatives there. Retaining the actual directional gradient g comparable to a_h ell/k therefore enforces the same C3 lower bound. The natural gauge Q(0)=0 makes the claimed central gradient exact: Q(0)=F(0)=0 kills both the correction and its first derivative, while F'(0)=1 leaves b(theta').

The retained directional-gradient assumption is essential. A large arbitrary strain component would not by itself specify that direction. The source explicitly uses that assumption and verifies it in its natural gauge. Likewise an observed flat region inside a much larger parent does not satisfy the support-exit hypothesis; the source correctly exempts that case.

## 5. Attenuation and exact boundary

For individual copies in common coordinates, bounded C3 requires attenuation eta <= C k squared ell^(-11/8). The conclusion about an infinite superposition requires the stated local isolation or quantitative noncancellation; no arbitrary sum is excluded. Multiplying a separately established terminal transfer estimate by eta would reduce its polynomial strain to O(k squared), but this is correctly conditional on a transfer theorem for the changed profile.

The conversion W(x)=A Z(s(x-x0)) multiplies the third derivative by A s cubed. At A=h^(-14), s=h^(-10), the lower bound is h^(-47)ell^(11/8), as printed. Independently rescaled families do not become one original datum.

The broad-packet conclusion requires one fixed periodic profile. An h-dependent profile with an increasing flat phase range or degenerating non-flat derivative is outside this proof; the narrow-support lemma can still apply when its own hypotheses hold. For clarity in eventual publication, the profile's fixed period could be renamed P: the source's letter L is also used elsewhere for the varying physical rescaling parameter. The text already says that F is fixed, so this is a notation clarification rather than a missing hypothesis.

## Verification receipt

[the preserved exact controls](checks/check-profile-extension.py) passes exact SymPy checks of both full third derivatives and the curl sign, and Fraction checks of all thirteen relative h exponents and the physical exponent. An initial symbolic test failed because its replacement rule targeted SymPy's unused Subs representation; replacing the actual argument-derivative objects made the intended identity check pass without changing any mathematical formula. These are algebraic checks, not a formal PDE certificate.

## Full-solution frequency window

Canonical [derivation](../navier-stokes/next-seed-analysis.md). Reviewed source SHA-256 `a3e94f6809729eb7f7de9f8c3b34af3c2935fb3dc11a862d2e00d37bc2b826b9`.

8 September 2026. Direct analytic check against (27)–(28) and the initial H12 bound in the recorded local calculation. This was an analytic check.

**Verdict: the proposed consequence is valid.** It is an all-mode, full-PDE estimate for the existing smooth solutions, using their already established H12 bound. It excludes fixed positive rescaled high-pass strain above the specified finer cutoff during the proved interval. It does not exclude tiny fine seeds, later amplification, or fixed physical strain after an h-dependent coordinate conversion.

## 1. Torus convention and a uniform Fourier-tail estimate

Use T_L^3=(R/(2 pi L Z))^3, L>=1, volume V_L=(2 pi L)^3, frequencies kappa_n=n/L, and Fourier coefficients

    uhat(n)=V_L^-1 integral_TL u(x) exp(-i n.x/L) dx.

The Sobolev norm is the unnormalized spatial L2 norm:

    ||u||Hs^2=V_L sum_n (1+|kappa_n|^2)^s |uhat(n)|^2.

For integer s this is uniformly equivalent, with constants depending only on s and dimension, to the usual sum of unnormalized derivative L2 norms. Define P_{>K} using actual coordinate frequencies |n/L|>K, not integer mode indices |n|>K. This distinction is essential on expanding tori.

Absolute Fourier summation and Cauchy–Schwarz give

    ||grad P_{>K}u||infinity
      <= V_L^-1/2 [sum_|kappa|>K |kappa|^2
                         (1+|kappa|^2)^(-s)]^1/2 ||u||Hs.

For K>=1, bound the sum in dyadic shells. The number of lattice points with |n/L|<=2R is at most C(LR)^3 whenever LR>=1. Hence

    sum_|kappa|>K |kappa|^(2-2s)
       <= C L^3 sum_j>=0 (2^j K)^(5-2s)
       <= C_s L^3 K^(5-2s),       s>5/2.

The L^3 factor cancels V_L in the squared estimate. Thus, uniformly in L>=1 and K>=1,

    ||grad P_{>K}u||infinity <= C_s K^(5/2-s)||u||Hs.    (1)

The velocity tail has the stronger bound C_s K^(3/2-s)||u||Hs. Therefore (1) also bounds the full C1 norm up to a fixed constant when K>=1. This works for the sharp radial Fourier cutoff because the series converges absolutely; no uniform L-infinity multiplier bound for the sharp projector is being assumed. Rectangular frequency cutoffs give equivalent estimates with fixed constants.

If one instead uses volume-normalized Sobolev norms, an additional volume factor appears. The current theorem uses unnormalized norms, so (1) is the applicable convention.

## 2. Apply the existing full-PDE H12 bound

The proved window 0<=t<=t_f has

    sup_t ||Q_h(t)||H12 <= h^(-117/8) G_h,
    G_h=ell^M exp(C ell^(11/8)), ell=sqrt(log(1/h)).

Here M denotes a fixed polynomial exponent, distinct from the frequency cutoff K. In particular log G_h=o(log(1/h)), so G_h=h^(-o(1)). Set K=h^(-beta), with fixed beta>0. Equation (1) gives

    sup_t ||P_{>h^-beta}Q_h(t)||C1
       <= C h^(a_beta) G_h,
    a_beta=(19/2)beta-117/8.                            (2)

The exponent is positive exactly when beta>117/76. For beta=9/4,

    a_beta=171/8-117/8=27/4,
    sup_t ||P_{>h^-9/4}Q_h(t)||C1 <= h^(27/4-o(1)).      (3)

Thus no fixed positive rescaled high-pass strain at that cutoff occurs anywhere in the current window, including its endpoints. This is an upper bound on the actual total solution, not on an approximate packet, its leading phase, or selected Fourier modes. It also excludes fixed positive symmetric-strain norm for this high-pass velocity since |sym grad v|<=|grad v|.

The interpretation k3=k^(3/2)=h^(9/4) uses nominal reciprocal wavelength: fixed factors such as 2 pi or a fixed terminal covector length change only constants. It is not a claim that (3) excludes every frequency finer than the current k=h^(3/2). In fact 117/76 is slightly larger than 3/2; this particular H12 bound gives no vanishing conclusion at beta<=117/76. At equality the growing factor G_h is not controlled by a positive power of h.

## 3. Necessary accumulated strain for a later smooth extension

Suppose the same unforced solution has a smooth extension to time t beyond the registered window. Let

    I_h(t)=integral_0^t ||grad Q_h(r)||infinity dr.

The standard integer H12 energy estimate, with pressure removed by divergence freedom, is

    d/dt ||Q_h||H12 <= C12 ||grad Q_h||infinity ||Q_h||H12.

The viscosity contribution is nonpositive and may be dropped. The transport term cancels in each derivative energy; the remaining commutator is bounded by the displayed Lipschitz coefficient and H12 norm. Constants can be chosen independently of L: apply the homogeneous integer commutator estimate at each derivative order and rescale the torus; each order's powers of L match on both sides. The zeroth-order energy is nonincreasing. The numerical value of C12 depends on norm conventions and is not specified or optimized here.

The actual initial bound in the theorem is

    ||Q_h(0)||H12 <= C h^(-117/8) exp(C0 ell),

absorbing fixed powers of ell into the exponential. Consequently, throughout any such smooth extension,

    ||P_{>h^-beta}Q_h(t)||C1
       <= C h^(a_beta) exp(C0 ell+C12 I_h(t)).          (4)

For a fixed threshold rho>0 independent of h, reaching
||P_{>h^-beta}Q_h(t)||C1>=rho forces

    I_h(t) >= (a_beta/C12) log(1/h)
               -(C0/C12)ell +(log rho-log C)/C12.     (5)

This has content for a_beta>0. For beta=9/4 its leading coefficient is (27/4)/C12. The existing bound I_h(t_f)<=C ell^(11/8) is o(ell^2)=o(log(1/h)), so it cannot meet this necessary clock for sufficiently small h. This independently recovers the qualitative exclusion already quantified in (3).

This argument assumes a smooth extension while deriving (4). It does not construct that extension, guarantee that the threshold is ever reached, or identify a sufficient amplification mechanism. Constants and the initial-data family must be held fixed as h tends to zero. A threshold depending on h contributes log rho_h in (5); one cannot apply the fixed-threshold conclusion unchanged to arbitrarily tiny seeds.

## 4. Coordinate and mechanism boundaries

For the theorem's physical conversion u(t,x)=A Q(A L t,Lx), with A=h^-14 and L=h^-10, gradients multiply by A L=h^-24. The physical cutoff corresponding to rescaled K is L K. Thus (3) becomes a physical gradient bound of order h^(-69/4-o(1)); that upper bound does not exclude a fixed physical gradient. Only the rescaled conclusion (3), or a consistently rescaled threshold in (5), is asserted.

Accumulated strain itself is invariant under this conversion:

    integral_0^tphysical ||grad_x u||infinity dtphysical
      = integral_0^trescaled ||grad_y Q||infinity dtrescaled.

The threshold and spatial frequency still transform. A large affine/flat-core jet can coexist with the tail exclusion because large gradient does not imply substantial still-finer Fourier content. Likewise an extremely small high-frequency seed may exist below (3) and become relevant later. Neither the Fourier estimate nor the clock supplies the missing generated-seed/repeated-transfer construction or closes ROOT.

## Generated-source and additional algebra review

The coordinating agent independently rederived the signed cross interaction,
its Leray projection, the exact passive-shear reduction, the first donor-heat
Duhamel coefficient and the factorial sideband bound in the
[generated-receiver note](generated-receiver.md). The reviewer
independently checked the full-Q Fourier consequence and the coordinating
agent's real Kelvin-polarization strain identity. The latter is an ODE
statement without additive sources; it is not a full-Fourier decay theorem.

The [preserved executable controls](checks/check-profile-extension.py)
combine the independently run source and seed-derivative checks with a curved
phase/variable-clock curl fixture, an omitted-clock divergence mutation,
a longitudinal-pressure mutation, phase-mean stress products, the trace-free
Kelvin identity, and exact interpolation/frequency exponents. These three
profile/source control groups pass. Two additional forced-stage groups now
pass in the same script; see the [forced review](forced-stage-review.md).
These finite fixtures do not certify estimates for
all smooth phase profiles, full nonlinear continuation, or an infinite flow.

One substantive table correction arose during independent review: the leading
mixed viscosity term of the profile corrector has order
`epsilon k d^(-1/2)=h^(39/8)`, while its slow/curl and mean viscosity terms
have order `epsilon k^2 d^(-3/2)=h^(41/8)`. Both exceed the leading
residual exponent `31/8`; the corrected terms remain within the proof budget.
The signed profile is explicitly `-H_tau F`, preserving the original outgoing
gradient. The fixed profile period in the seed-cost proof is called P to
avoid conflict with the varying torus scale L.
