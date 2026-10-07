# Independent agent reviews of the original-time matching

8 September 2026. These are mathematical derivation audits by separate agents. They are not external expert acceptance or formal certificates. ROOT remains open.

---

## Seed reduction and profile normalization

Original source: `nse-seed-reduction-independent-review-20260908.md`; SHA-256 `c109ff1f0ab4758e38d961a2c2e4874bb9981d028868016d7056f538c65d6d36`.

# Independent review of the actual seed reduction, sections 2–5

8 September 2026. Reviewer: fluid_lean_audit. This is an independent mathematical read of `references/analysis/actual-seed-cost.md`, sections 2–5, together with the geometric oblique-carrier and first-stage log-log/outgoing results it uses. No DNS, canonical mutation, or formal proof certificate is involved. Later matching claims are outside this review.

## Verdict and quantifiers

The reduction in sections 2–5 is valid. I found no remaining load-bearing gap. One normalization convention was checked with the parent and is now explicit in the source: use the **unscaled geometric** fixed profile `V=V_j`, with `f_j(P_j)=1`. The limits `A0`, `Omega1 -> 1`, `mu -> 2/3`, and `Gamma -> -1/2` are for this family. They cannot silently be combined with a separate, j-dependent L2 normalization from an older note. The first-stage comparison theorem permits the unscaled fixed profile with changed profile-dependent constants.

The order of quantifiers is essential: choose a sufficiently thin profile index j once, then hold that profile, its positive physical-time Floquet exponent mu_j, and nu fixed while h tends to zero. All PDE constants may depend on this fixed j. The argument does not require j=j(h), and it does not replace mu_j by 2/3 on a growing time interval. The primary terminal time uses mu_j itself.

The main conclusions independently checked are the exact nilpotent deformation formulas, the double terminal zero, the all-time covector-size law, and relative comparison of the actual-q cost with the same fixed profile's matrix-model cost. These do not by themselves prove the proposed powers for the polarization transfer.

## 1. Cross-product and Euler-compatible matrix identities

Use the convention A_ij=partial_j V_i and omega=curl V. The pressure-corrected amplitude equation and the cotangent equation give, for alpha=N cross beta,

    alpha' = A0 alpha + (omega_V dot N) beta.

This is the trace-free cross-product identity; the pressure term does not contribute to N cross beta'. Along a steady Euler trajectory, omega_V'=A0 omega_V and N'=-A0^T N, so Gamma=omega_V dot N is constant. The selected thin family has Gamma nonzero for all sufficiently large fixed j.

For Abar=A0-beta tensor N/ell, its antisymmetric vector is omega_V-alpha/ell. Differentiating this expression and using N dot alpha=0 gives

    (omega_V-alpha/ell)' = Abar(omega_V-alpha/ell).

Thus the model has precisely the stated vorticity transport identity. This is a compatibility property of a matrix history along a trajectory. It neither constructs nor assumes another global Euler solution.

## 2. Exact rank-one deformation

Let F(t)=D Phi_V(t,0). Since N(t)=F(t)^(-T)N0, the interaction representation Jbar=F Z obeys

    Z' = -v(t) tensor N0 Z,
    v(t)=F(t)^(-1) beta(t)/ell.

For every s, N0 dot v(s)=N(s) dot beta(s)/ell=0. Hence the product of any two interaction generators, even at different times, vanishes. It follows by direct differentiation that

    Z=I-kappa tensor N0,
    kappa=int_0^t v(s) ds,
    Z^(-1)=I+kappa tensor N0.

Also (F^(-1)alpha)'=Gamma F^(-1)beta. This proves the endpoint formula for kappa exactly. There is no Gronwall or exponential-in-ell loss in this step.

The same calculation from an intermediate time t to t* gives

    Jbar(t*,t)=F(t*,t)
       -[alpha(t*)-F(t*,t)alpha(t)] tensor N(t)/(ell Gamma).

Applying its transpose to the terminal covector gives exactly the stated C-fN formula. At t=0, with xi*=4 alpha(t*)/|alpha(t*)|, the coefficient of N0 is

    -4|alpha(t*)|/(ell Gamma)+O((1+t*)/ell).

The remaining term F(t*)^T xi* is O(1+t*). Since |alpha(t*)| is comparable to exp(mu_j t*) and exp(mu_j t*)/ell is comparable to ell, the original covector has size comparable to ell. Its angle to the appropriate sign of N0 is O(log ell/ell). This logarithmic cone is not contained in a cone of width h^beta for fixed beta>0.

## 3. Double terminal zero and its sign

Differentiate C=F(t*,t)^T xi* with respect to t: C'=-A0^T C. The formula for f gives

    f'=-beta dot C/ell,
    f''=(2/ell)[C dot A0 beta
       -(N dot A0 beta)(C dot N)/|N|^2].

At t=t*, C=xi* is perpendicular to both beta(t*) and N(t*). Therefore f(t*)=f'(t*)=0 and

    f''(t*)=2 xi* dot A0(t*) beta(t*)/ell.

The backward Taylor expansion has the plus coefficient in the source: f(t*-u)=u^2 xi* dot A0 beta/ell+O(exp(mu_j t*)u^3/ell). The sign is not changed by reversing the time variable because this is a second derivative.

In the stated thin normalization, c=1/sqrt(2),

    beta0=(1,1/3,c/6), alpha0=(-3/4,2,c),
    A0 beta0=(-1/3,-1,-c), |alpha0|=9/4.

Thus alpha0 dot A0 beta0=-9/4 and the unit terminal receiver rho0=alpha0/|alpha0| satisfies rho0 dot A0 beta0=-1. The quadratic zero is negative for f, as asserted. Continuity of the finite-angle derivatives gives the same sign for sufficiently thin fixed profiles uniformly in the terminal angle.

The source uses length 4 for the receiver initially and length 1 when displaying the thin formula. This harmless fixed rescaling is explicitly stated there. One must use the same length on the two sides of an actual/model comparison; the polarization equation and strain ratio themselves are unchanged by scaling the whole covector.

## 4. Action coordinates and uniformity over the growing interval

The scaling in the action-coordinate formula is correct. In an infinitesimal coordinate displacement, write

    z1=delta I/r_j, z2=r_j delta sigma, z3=delta beta_angle.

Then physical displacement in the E frame is C_j z, where C_j has columns r_j Phi_I, Phi_sigma/r_j, Phi_beta in that frame. The exact variation equations are

    z1'=0, z2'=r_j^2 Omega1' z1, z3'=r_j Omega2' z1.

Thus D_j has exactly the entries stated in the source, D_j^2=0, and

    F_E(t*,t)=C_j(t*)[I+uD_j]C_j(t)^(-1).

The analytic angular expansion gives C_j=I+O(r_j), including every fixed angular derivative needed here. The two shear coefficients tend to -2 and -c. Consequently F_E and its inverse are bounded by C(1+u) uniformly over all sufficiently thin profiles and all u>=0. This exact formula is stronger than integrating an O(r_j) coefficient approximation over a long time.

For the primary polarization, apply Floquet theory on the fixed poloidal-angle period 2pi. The simple expanding eigenvalue and eigenvector of the limiting hyperbolic 2 by 2 system persist. After the indicated normalization,

    beta_E(t)=exp(mu_j t) b_per,j(sigma(t)),
    b_per,j=beta0+O(r_j),
    alpha_E(t)=exp(mu_j t) a_per,j(sigma(t)),
    a_per,j=alpha0+O(r_j), N_E=k0+O(r_j).

The bounds also hold for the fixed derivatives required in the terminal Taylor expansion. They are uniform in the angle. The exponent here is the physical-time exponent, incorporating the angular frequency Omega1,j. The geometric expansions give Omega1,j -> 1.

Here is an explicit way to make the source's uniform comparison argument. Put sT=exp(mu_j t*)/ell and rho*=a_per,j(t*)/|a_per,j(t*)|. For a unit receiver, f/sT is exactly

    [a_per,j(t*)-exp(-mu_j u)
       C_j(t*) (I+uD_j) C_j(t)^(-1) a_per,j(t)]
       dot rho* / Gamma_j.

All the bounded angular factors converge uniformly to constants, so no angular phase drift accumulates. The polynomial tail is multiplied by exp(-mu_j u). The exponential is controlled uniformly with mu_j bounded below by a fixed positive constant.

The thin expression is -g(u), where

    g(u)=(9/2)[1-(1+(2/3)u)exp(-(2/3)u)],
    g'(u)=2u exp(-(2/3)u), g(u)=u^2+O(u^3).

To obtain the lower bound uniformly:

1. On a fixed small interval 0<=u<=u0, use the exact equalities f=f'=0 at u=0 and C2 convergence of f/sT. The discrepancy from -g has size O(r_j u^2), so -f/sT is comparable to u^2.
2. On [u0,U], use strict positivity of g and uniform convergence.
3. Choose a fixed U large enough that the tail (1+u)exp(-mu_min u) is small. The nonzero terminal term then controls every u>=U uniformly.

Choose u0 and U first, then j sufficiently large, and finally h small. This proves |f| comparable to ell min(u^2,1), including its sign, on the whole interval. It does not exchange the thin-profile and small-h limits.

## 5. Lower bound for the full covector

Near u=0, C(t) has a uniformly nonzero projection onto N(t)^perp because C(t*)=xi* is perpendicular to N(t*). Thus the same projection of C-fN gives a positive uniform lower bound for |xibar|. Combining this with

    |C-fN| >= |f||N|-|C|

shows |xibar| comparable to 1+|f| on a fixed small interval. For example, split into bounded |f| and sufficiently large |f|; the transverse projection handles the first case and the reverse triangle inequality handles the second.

For u bounded below by that fixed small constant, |f|>=c ell, whereas |C|<=C(1+u)<=C log ell on the allowed interval. Therefore fN dominates. This proves uniformly

    |xibar(t)| comparable to 1+ell min((t*-t)^2,1).

No cancellation of the longitudinal and transverse parts has been assumed away. In particular the minimum ray norm stays bounded below at the endpoint transition.

## 6. Actual particle, phase, and gradient comparison

The canonical first-stage estimates give

    ||e||inf <= h^(9/8) E_h,
    ||grad e||inf <= h^(1/24) E_h,

where E_h may be enlarged finitely many times and has log E_h=O_j(ell)+O_j(log ell)=o(log(1/h)). The unweighted geometric and amplitude derivatives on the fixed-profile time interval are powers of ell.

Let a(t)=Phi_V(0,t,Y(t)). The identity

    a'=D Phi_V(0,t,Y(t)) [q-V](t,Y(t))

and ||q-V||inf<=h poly(ell) give |a(t)-x0|<=h poly(ell) on the whole interval. The velocity error h^(9/8)E_h is smaller than h eventually. Fixed-profile flow derivatives over O(log ell) are powers of ell. Consequently the bump remains near chi(0)=1; its relative error is O(h/delta poly(ell))=O(h^(1/2)poly(ell)). Unweighted primary directions at Y are close to their reference values by a positive power of h times a power of ell. Uniform nonvanishing of the expanding Floquet factor justifies taking unit directions.

For the phase, use D_q S=(q-V) dot xi. The leading primary amplitude is tangent to xi. Its exact curl correction has normal component -h div(b) sin(phi), bounded by h^2/delta times a power of ell. The mean has the same upper order, higher harmonic normal terms are smaller, and the true velocity error contributes h^(9/8)E_h. Dividing by h and integrating gives

    phi(t,Y(t))-pi/2 = O(h^(1/8) E_h)

uniformly from time zero. This uses the velocity error, not the weaker C1 bound. In particular the phase claim is genuinely along the actual particle.

The rapidly varying part of the primary gradient is

    -(b tensor xi/h) sin(phi).

The bump and initial-point drift replace b/h by beta/ell with h^(1/2)poly(ell) error after including its at-most-ell size. Covector drift is smaller; sin(phi)-1 is quadratic in the phase error. Slow primary derivatives and mean/harmonic gradients are h^(1/2)poly(ell) or smaller. The change A_V(Y)-A_V(X) is h poly(ell) with fixed-profile constants. The true gradient error h^(1/24)E_h dominates these terms. Thus

    sup_t |A_q(t,Y(t))-Abar(t)| <= h^(1/24) E_h.

Both integrated gradient norms are O_j(ell). For Abar, this follows directly by integrating exp(mu_j t)/ell up to t*; for actual q it is also part of the first-stage bound. The terminal receiving frames differ by the same admissible positive-h-power error. The frame directions are the primary amplitude/covector directions; one is not trying to normalize the primary velocity at its phase pi/2 zero.

## 7. Relative cost comparison does not require the unproved matching

For a cotangent solution, first use the unit direction n=xi/|xi|. Its equation is

    n'=-A^T n+(n dot A^T n)n.

It is Lipschitz on the sphere with constant C|A|. Backward Gronwall over the O(ell) integrated gradient, including the small terminal frame difference, gives actual/model direction error h^(1/24) exp(C_j ell). Next compare

    (log |xi|)'=-n dot A^T n.

The logarithmic magnitude-ratio error has the same type of bound. No small covector magnitude enters a second coefficient denominator. The model magnitude is already bounded below, so the all-time covector norm law transfers to q.

The amplitude generator is G(A,n)=-A+2n tensor n A. Its difference is bounded by C|Delta A|+C|Abar||Delta n|, and each propagator and inverse has norm at most exp(C_j ell). Duhamel therefore gives the same h^(1/24) exp(C_j ell) absolute difference of the 3D amplitude propagators. Identify the initial and final tangent planes by the small orthogonal rotations of their normals; these endpoint identifications preserve this error bound. They introduce no derivative cost from a moving coordinate frame.

The adjoint row formula for the cost then gives

    |C_h-Cbar_h| <= h^(1/24) exp(C_j ell).

Because the plane map is invertible and its inverse has norm at most exp(C_j ell), Cbar_h=|Mbar^*p|>=exp(-C_j ell). Dividing the absolute error by this generic lower bound proves C_h/Cbar_h -> 1. No conjectured polynomial bound for Mbar is used here: all fixed exp(C ell) factors are h^(-o(1)).

Finally, |xi|<=C ell and t*=O(log ell) imply

    (epsilon/k^2) int |xi|^2 dt <= C_nu h ell^2 log ell -> 0.

This is only the principal viscous attenuation bound. The separate forward preparation theorem must still account for the curl, envelope, pressure, and Laplacian residuals.

## Boundary of the result

Sections 2–5 are usable inputs to a new matching proof for this fixed profile. They do not show that the thin limiting inner or outer polarization equation approximates the full transfer in the required growing weighted norms. That remaining matching needs its own independent proof and review. They also give no nonlinear original-time compatibility, uniform transfer-depth theorem, or Navier–Stokes regularity/singularity conclusion.

---

## Outer matching

Original source: `nse-outer-independent-review-20260908.md`; SHA-256 `1830f902fd1d7bc0768f3b63f73093a2ec0aa29e72c421e09ac1cc0e842ba7d1`.

# Independent review of the full outer polarization matching

8 September 2026. Reviewer: textbook_site / inner-matching lane.
Reviewed `outer-matching.md` in full against the exact
central model, and checked its interface with the separately derived
inner equation. No canonical edits or DNS.

**Verdict:** the outer estimate closes at its stated central matrix-ODE
scope. I found no missing term, unstable-kernel loss, sign mismatch, or
normalization gap in the selected-column proof. The full-propagator
extension also follows from the same bounds. This review accepts the
fixed-profile geometric/Floquet inputs previously established in
actual seed cost; it does not independently reprove the Gavrilov
construction or the actual-q/finite-wave/nonlinear assembly.

## 1. Exact lift and remainder, equations (6)-(8)

Let v=Pb, l=(C.v)/d_f, so b=v+Nl. From N'=-A0^T N,

    P'v=N(N.A0 v)/|N|^2,
    P'N=P A0^T N.

Therefore P'v-P A0v=G_N v, while the normal-lift contribution is
l P(A0^T-A0)N=lH. The shear term is

    beta |N|^2(C.v)/(ell d_f)
      =beta(C.v)/(ell f)
         +beta(C.N)(C.v)/(ell f d_f).

Finally Pxi=PC=c_T, xi.beta=C.beta, and

    xi.Abar b=xi.A0v+l xi.A0N
                 -|N|^2(C.beta)(C.v)/(ell d_f).

These identities reproduce every term and sign in (8). In particular
there is no omitted derivative of C or f: the differentiation used is
v'=P'b+Pb', not a differentiation of an assumed approximation to b.
The first remainder term has exactly beta range and hence zero second
row in the primary Floquet basis.

An independent symbolic check, using a nontrivial trace-free A0,
N=(1,2,3), C=(3,-1,2), beta=(2,-1,0), and symbolic f and inverse ell,
verified the lift, tangency of R, and all three projected equation
components for two independent tangent vectors. Ten scalar identities
passed. Script: `support/check_outer_lift_2026_09_08.py`. This checks the
algebra; the analytic estimates are checked separately below.

## 2. Entrywise remainder, equation (11)

In the terminal outer range let F=ell u^2. Then |d_f| and |xi| are
comparable to F, while C.N and C.B_+ are O(u). The first, range-beta
term of R gives column-one O(ell^-1 u^-2) and column-two
O(ell^-1 u^-3), with exactly zero row two.

The H term on B_+ is O(ell^-1 u^-1), and on B_- is
O(ell^-1 u^-2), both within the claimed bounds. The first pressure
term, using |xi.A0B|<=CF, is O(ell^-1 u^-2) for both columns.
The lifted-normal pressure term is O(ell^-2 u^-3) on B_+ and
O(ell^-2 u^-4) on B_-, also absorbed because ell u^2 tends to infinity.

The final pressure term uses C.beta=O(ell^2 u), and its sizes are

    B_+: O(ell^-2 u^-4),
    B_-: O(ell^-2 u^-5).

The first is absorbed in O(ell^-1 u^-2), including its possible second
row; the second must remain in R22. It is absorbed in the stated R12
bound since ell u^2 tends to infinity. Thus all four estimates in (11)
are valid for every fixed a<1/2. It would be wrong to retain only the
range-beta cancellation and discard the second-row pressure term, but
the note explicitly retains and bounds it.

For u>=1 the shear-containing contributions acquire e^(-mu u), while
|C|<=C(1+u), |f|~ell. Polynomial factors times that exponential give
(12); the remaining normal and pressure terms are at most
C(1+u)/ell. Since u<=O(log ell), the terms with two inverse powers
of ell are smaller than the stated bound.

## 3. Stable kernel and bootstrap, equations (13)-(19)

Dividing by A=e^(mu t)f0/f gives exactly

    w'=(-2mu+f'/f+R22)w+R21X.

Thus its homogeneous kernel is (14), with f(t)/f(s), not its inverse.
The integral of the retained R22 term is O(ell^-2 u_m^-4); together
with O(ell^-1 u_m^-1) and the logarithmic far part, it is o(1) for
a<1/2. The signed f is negative throughout this range, so its ratio
is positive and comparable to theta(u_t)/theta(u_s). There is no
uncontrolled sign crossing in this kernel.

For u<=1, the near-terminal forcing bound is exactly

    C M u^2/ell * integral_u^1 v^-4 dv <= C M/(ell u).

The far contribution is O(Mu^2/ell), and for u>=1 the exponential
convolution gives O(M(1+u)/ell). This verifies (18).

In X', the three near-terminal terms are bounded by

    M/(ell u^2), M/(ell u^3), M/(ell^2 u^4).

Their integrated bounds are dominated by CM/(ell u^2); the last
ratio to that bound is O(1/(ell u)), which tends to zero uniformly.
The far integrals are bounded by CM(1+t*)^2/ell. Hence (19) gives a
uniform small multiple of M, and continuity implies M<=2 and X=1+o(1).
The note does not substitute an uncontrolled unweighted Gronwall
bound for the triangular stable system.

## 4. Full propagator, equations (20)-(21)

For arbitrary w0, its homogeneous contribution is K(t,0)w0. On the
far range K(s,0)<=C exp(-2mu s), while b12(s) is at most
C(1+t*) exp(mu s) ell^-2. Its contribution to X is therefore
O((1+t*)ell^-2). The R12 term contributes at most
O((1+t*)ell^-1).

On the terminal range s=t*-u with u<=1, exp(-2mu s)=O(ell^-4).
The factor theta(u)=u^2 cancels b12's u^-2; the R12 integral leaves
only ell^-5 log(1/u_m). These verify (20). Repeating the same small
feedback absorption then gives (21), including for x0=0. There is
no need to assume the second input vanishes in this extension.

## 5. Overlap coefficient, sign, and inner interface

Because C'=-A0^T C and beta'=G_N beta,

    (C.beta)'=-2 C.A0 beta
                   +2(C.N)(N.A0 beta)/|N|^2.

At t*, C=r_* and C.N=C.beta=0. Thus the derivative is
-2 a_*|beta(t*)|, giving the backward expansion
C.beta=2a_*|beta(t*)|u+O(|beta(t*)|u^2). Integrating f'=-C.beta/ell
from the terminal zero gives the sign and coefficient in (22):
f=ell^-1 a_*|beta(t*)|u^2[1+O(u)]. In particular f and f0 are negative.

The lift is parallel to N and does not change b_p. Its B_- contribution
to b_p has relative size O(w)=O(ell^-1/u). This is included in E.
Consequently b_p=(ell f0/a_*)u^-2[1+O(u+E)], with positive coefficient.
For the exact lifted normal component, the B_- correction has relative
size O(w/u)=O(ell^-1u^-2), again in E. Division by
f|N|^2[1+O(ell^-1/u)] then gives

    b_n/b_p=2/(Lambda u)[1+O(u+E)].

This checks both signs and the factor 2 in (23)-(24). With
V=b_p/sqrt(Lambda), W=b_n and R=sqrt(Lambda)u_m, it is precisely

    V(R)=D_h/R^2(1+O(delta_m)),
    W(R)=2D_h/R^3(1+O(delta_m)),
    D_h=ell f0 sqrt(Lambda)/a_*>0 ~ ell^(5/2).

These are the same frame, unit covector, scale, and normalization used
in `inner-matching.md`. No derivative matching is
silently assumed: W comes from the exact outer lift. Relative
O(delta_m)=o(1) is sufficient for the inner weighted estimate; the
stronger R delta_m ->0 at a=3/10 is harmless but unnecessary.

## 6. History and final review boundary

The selected X remains bounded and w=o(1); the lift and Floquet frame
are bounded. Hence |b|<=C e^(mu t)/theta(u), while
|xi|<=C ell theta(u). Their product is at most C ell e^(mu t), with
integral O(ell^3) and maximum O(ell^3). This uses the same exact
selected solution, not a reduced outer ansatz. Its initial vector is
bounded and nonzero, because it is the bounded transverse lift of
B_+(0). Combining it with the independently reviewed inner estimate
is therefore consistent.

I approve the outer central-ODE implication as written, conditional on
its named fixed-profile geometry/Floquet inputs. This review does not
turn those ODE estimates into a nonlinear NS construction, a claim of
novelty, a formally certified proof, or an infinite cascade. Those
remaining transfers retain their separate proof obligations.

---

## Inner matching and whole envelope

Original source: `nse-inner-matching-independent-review-20260908.md`; SHA-256 `04d1e785c98788c5c5dabae3b1cf9de72e91abd1a7b7f679f160701fe25b6a26`.

# Independent review: growing inner matching and envelope extension

8 September 2026. Reviewer: fluid_lean_audit. Sources reviewed in full:

- `inner-matching.md`;
- section 8 of `references/analysis/mixed-seed-nonlinear-budget.md`;
- the independently reviewed fixed-profile reduction in sections 2–5 of `actual-seed-cost.md`.

No canonical file was changed. No DNS, numerical ODE integration, or formal proof checker was used. A small independent SymPy computation checked the exact rational matrix numerator, the absence of shear in K21, all four leading matrix entries, and the scalar conjugation identity. The analytic estimates below were reviewed separately from those algebra checks.

## Verdict

Both implications pass independent mathematical review. I found no load-bearing gap in the growing-interval inner transfer or in the central-to-envelope extension. The inner theorem remains conditional on the outer incoming branch and its relative weighted error; the envelope theorem remains conditional on the actual central bounds E4. This memo does not independently verify those outer inputs or assemble a new nonlinear theorem.

The profile must remain the unscaled geometric fixed V_j, with sufficiently large j chosen before h tends to zero. The inner equation uses the actual terminal coefficients a=a21(t*) and c=a31(t*), which may vary with terminal phase. Their compact negative coefficient range is the source of uniformity. There is no integration of an O(r_j) error over a growing inner interval.

One harmless notation correction was sent to the parent: the phrase “At a=3/10” in section 6 should name the *overlap exponent* rather than a, which already denotes the negative terminal coefficient a21. None of the estimates depends on that naming error.

## 1. Moving frame and exact matrix

For Q=(p,r,n), p=beta/|beta|, n=N/|N|, r=n cross p, direct differentiation of the primary pressure-corrected equations gives

    p' dot r=-a21, p' dot n=a31,
    n' dot p=-a31, n' dot r=-a32.

Hence the displayed skew matrix Omega=Q^T Q' is correct. The cotangent equation in the moving frame uses A-Omega, whereas reversing time in the polarization equation produces A+Omega. In particular the lower-left two entries of D=A-Omega vanish exactly. This triangular structure is what removes the large shear from the first two cotangent equations.

Writing eta=(x,y,w), eliminating b_r by eta dot b=0, and scaling b_p=V/e, b_n=W, z=u/e gives exactly

    K=diag(e,1) [H B]_{rows 1,3} diag(1,e),
    B=[[1,0],[-x/y,-w/y],[0,1]].

Thus the entries are e(HB)11, e^2(HB)12, (HB)31, e(HB)32. The factors of e in the source are correct; no factor from reversing time or rescaling b_p is missing.

An independent symbolic construction of H and B verifies the stated (HB)31 numerator:

    -2[a11*x*y*w-a12*x^2*w+a21*y^2*w-a22*x*y*w
       -a31*x^2*y-a31*y^3+a32*x^3+a32*x*y^2]

over y(x^2+y^2+w^2). Its derivative with respect to s is exactly zero. This is structural: the first column of B has zero n component, so both the shear and its pressure correction vanish on that input column. The other entries retain the shear and full pressure as required.

Substituting x=2aez, y=1, w=-az^2, s=e^(-2) and taking e to zero gives exactly

    K0=[[0,-1],[(2a^2*z^2+2c)/P,-4a^2*z^3/P]],
    P=1+a^2*z^4.

The thin a and c are negative, and a compact range bounded away from zero persists uniformly in terminal phase for sufficiently thin fixed profiles.

## 2. Cotangent estimates are uniform up to the growing endpoint

The first two backward equations form a closed, bounded-coefficient 2 by 2 system, independent of Lambda. Starting at (x,y)=(0,1), their fixed-time Taylor estimates give x=2au+O(u^2), y=1+O(u). Inserting these in the integrating-factor formula for w gives

    w=-a Lambda u^2+O(u+Lambda u^3).

This is a parameter-dependent estimate, not a compact-z asymptotic. With u=ez and Lambda=e^(-2), it gives the error ez+ez^3 throughout 0<=z<=R, provided eR=u_m is small. The differentiated versions follow from the same exact equations with bounded fixed-profile coefficient derivatives.

For z<=1, |y|>=1/2 controls the denominator. For z>=1, the relative error in w/(-az^2) is O(ez+e/z), so it is small uniformly if eR is small. Therefore |eta|^2 is comparable to P throughout the growing interval. This justifies every rational denominator estimate in the next step.

## 3. Coefficient and derivative error bounds

The stated bounds

    |E11|<=Ce, |E12|<=Ce(1+z),
    |E21|<=Ce/(1+z), |E22|<=Ce

are consistent with the exact rational entries, including the potentially dangerous pressure terms.

For E21, the leading numerator is -2aw+2c after y is replaced by 1. Perturbing w and the denominator gives O(e/(1+z)). The remaining xw/P term has the same size, since x=O(ez), w=O(z^2), P comparable to 1+z^4. Terms of size x^2 w/P are O(e^2), which are also bounded by Ce/(1+z) on e(1+z)<=C. There is no uncancelled shear term to enlarge this error.

For E12, its scaled shear is

    -e^2 s (1-2x^2/|eta|^2).

It differs from -1 by O(ez)+O(e^2). The remaining background terms after multiplication by e^2 are at most Ce^2(1+z^2), which is bounded by Ce(1+z) when eR is small.

For E22, the scaled shear is 2esxw/|eta|^2. Its leading value is -4a^2z^3/P. Relative geometric errors cost O(ez) times an O(1/z) large-z term, hence O(e). The background rational numerator has no a32*w^2 term after pressure cancellation. It is bounded after division by its denominator by C(1+|x|), so multiplication by e costs at most Ce.

The same denominator structure makes the background E11 entry bounded by Ce(1+|x|). Differentiating the exact expressions, with coefficient derivatives carrying a factor e in z time, gives

    |E11'|<=Ce/(1+z), |E12'|<=Ce.

At large z the rational derivatives decay; derivatives of the slowly varying coefficient factors are O(e^2), which obey the first bound because e(1+z) is small. At bounded z the direct differentiated estimates suffice. No unpriced q_t bound is imported here: these are derivatives along the fixed smooth reference profile and its finite-dimensional frame.

## 4. Frozen connection and positivity

The frozen system reduces to

    (P V')'+(2a^2 z^2+2c)V=0.

The exact symbolic conjugation V=P^(-1/2)Y gives

    Y''=qY,
    q=[4a^2 z^2-2cP]/P^2.

Since c is uniformly negative, q>0. It is bounded near zero and is O((1+z)^(-4)) at infinity uniformly over the compact coefficient set. Its first moment is uniformly finite.

The backward Volterra series with limiting data Y(infinity)=1, Y'(infinity)=0 converges and has 1<=Y<=C. Differentiation gives -Y'(0)=int_0^infinity qY, bounded below uniformly by integration over a fixed small interval. Since g(0)=1, g'(0)=0, both V(0) and W(0)=-V'(0) have the required positive lower bounds. The large-R expansion follows by integrating q=O(R^(-4)): Y-1=O(R^(-2)), Y'=O(R^(-3)), then differentiating V=gY. This proves the stated relative O(R^(-2)) incoming asymptotics.

## 5. The weighted error is O(eR), not an uncontrolled exponential

Write V'=alpha V+beta W, W'=gamma V+delta W. Because E12=O(e(1+z)), beta stays bounded away from zero. Eliminating W gives exactly the source's scalar equation. Inserting the coefficient estimates and V=gY yields

    Y''=qY+r1Y'+r0Y,
    |r1|<=Ce, |r0|<=Ce/(1+z).

The potentially dangerous product E12*gamma0 is O(e/(1+z)), since gamma0=O((1+z)^(-2)). The alpha*delta terms obey the same bound, using e(1+z) small for the O(e^2) contribution. The derivative alpha' has precisely the decay required for r0.

In X with norm sup|Y|+sup(1+z)|Y'|, the q-Volterra resolvent is uniformly bounded independently of R. One may first estimate its undifferentiated series by exp(int_0^infinity s q(s)ds), then differentiate the equation; sup_z(1+z)int_z^infinity q is finite.

For the perturbation operator

    T_rY(z)=int_z^R (s-z)[r0(s)Y(s)+r1(s)Y'(s)] ds,

its sup norm is bounded by CeR||Y||_X. Its differentiated norm is bounded by

    Ce sup_z (1+z) log((1+R)/(1+z)) ||Y||_X
       <= Ce C(1+R)||Y||_X.

This single bound handles both terms; no stronger integrability assumption on r1 is needed. A Neumann inversion around the q-resolvent therefore has norm independent of R when eR is small. It gives an O(e(1+R)) operator difference from the frozen terminal transfer.

The X norm is uniformly equivalent to the smooth V,W weights in the source. In converting back, W=(V'-alpha V)/beta; the extra alpha V term is controlled because e(1+z) stays small. Thus the upper bounds for all three components and for |eta||b| follow on the entire inner interval.

## 6. Terminal conversion and branch matching

The outer data must provide V(R)=D R^(-2)(1+O(delta_ell)) and W(R)=2D R^(-3)(1+O(delta_ell)), with delta_ell->0. Converting them to Y,Y' using the *actual* first row V'=alpha V+beta W gives terminal discrepancy

    C D[delta_ell+R^(-2)+e(1+R)]

in |Y(R)|+(1+R)|Y'(R)|. In particular alpha V and E12 W each produce a term of order eR in this norm. The source includes that cost. Omitting it would be an error, but it is included and tends to zero.

Combining this with the X transfer estimate preserves the positive frozen endpoint connection for large ell. There is no requirement delta_ell R->0, and no multiplication of the error by an unbounded frozen condition number is necessary in these weights.

At u_m=ell^(-3/10), R is comparable to ell^(1/5), so eR=O(ell^(-3/10)) and R^(-2)=O(ell^(-2/5)). If D is comparable to ell^(5/2), the resulting terminal b_p and b_n scales are ell^3 and ell^(5/2), respectively. The same implication accepts the stated small fixed exponent losses.

The whole inner history bound also checks. Transversality gives |b_r|<=CD/(1+z), while |eta|<=C(1+z)^2. Since e(1+R) is small,

    |eta||b|<=C D/e=C sqrt(Lambda)D.

The b_r term does not exceed this because 1+z<=C/e. This bound is compatible with the outer matching but does not replace the missing outer history estimate.

## 7. Independent review of the whole-envelope extension, E1–E5

Section 8 of the mixed-budget note prescribes a final affine phase on a radius-d ball and prepares the real unweighted tangent amplitude B backward by the inviscid ODE. This is legitimate finite-dimensional preparation, not inverse viscous evolution. The bump is factored separately as a function of final-ball labels. A constant phase shift pi/2 ensures the desired central gradient at every time without changing xi or the transport equations.

Differentiating the actual-q flow and polarization equations in h-scaled coordinates gives fixed-order bounds exp(C ell); q C24 provides room for the required derivatives through 18. Uniform inverse covector magnitude follows from the backward cotangent flow with terminal magnitude 4. The final amplitude c_h is polynomially bounded and is absorbed in the same factors.

At each time the support has exactly its original volume by incompressibility, so its L2 volume factor is d^(3/2), without an exp(C ell) volume loss. Its diameter may grow to d exp(C ell), but this is still o(h). Differentiating with respect to final-ball labels, or using a slightly enlarged phase chart, therefore gives

    sup_support(|B-B_c|+|xi-xi_c|)<=(d/h)exp(C ell).

Finite products of B and xi conditioning factors only enlarge C. This proves E1 and E2 with d/h=h^(1/4). It does not assume the bump itself is relatively constant.

Bump derivatives cost d^(-r)exp(C ell). Combining them with the unweighted jets and the exact volume bound yields all the pointwise and L2 amplitude hypotheses of the nonlinear criterion. In the C1 norm of the real curl lift, the non-leading terms are bounded by (k/d)exp(C ell)+(k/d)^2 exp(C ell), including the oscillatory derivative of the curl correction. Since k/d=h^(1/4), these vanish. Integration over O(log ell) only enlarges the subpower factor. This verifies E3.

For E4, normalize by N_h=n dot v_h(t_f), which is nonzero by assumption. The backward preparation exactly recovers B_c=v_h/N_h. Transversality to terminal xi*=4r leaves only p,n components, and the history upper bound also controls the full terminal vector. Hence |c_h|<=C ell^(1/2+2eta).

The three decisive exponent computations are

    initial strain: 7/8 + 1 -(5/2-eta) = -5/8+eta,
    history:        7/8 +(3+eta)-(5/2-eta) = 11/8+2eta,
    final strain:   7/8 +(3-eta)-(5/2+eta) = 11/8-2eta.

Thus initial strain tends to zero for eta<5/8; the history is o(ell^2) for eta<5/16; and the final strain dominates the host O(ell) for eta<3/16. The last margin is indeed restrictive. The small curl correction cannot change the terminal lower bound, because the central phase is pi/2 and the residual slow terms vanish in C1. The mean, harmonic, and true nonlinear-error bounds are handled by the previously reviewed conditional criterion, once E4 is supplied.

## Final scope

The two reviewed arguments remove the growing-inner-interval and whole-envelope obstacles at the level of explicit mathematical implications. Their conjunction with a independently validated outer matching and actual central history would justify applying the existing finite nonlinear criterion. This memo does not substitute numerical limiting-jet behavior for that outer proof, and does not establish iteration, original-viscosity uniformly small data, ROOT, or full Lean formalization.


---

## Full assembly and smooth seed supply

Original review: `nse-original-nonlinear-assembly-review-20260908.md`; SHA-256 `0d8fcd845c983e7f5b7de4c48bcb5b81c092a336484ba3521e382530df2f1b65`.

# Independent full assembly review: original-time nonlinear handover

8 September 2026. Reviewer: fluid_lean_audit.

**Completed independent full read.** I read `../original-nonlinear-handover.md` end to end, including the subsequent explicit primary-pressure completion, and checked its interfaces with the reviewed constituent arguments. **Verdict: no remaining load-bearing mathematical gap found at the stated finite original-time supplied-seed scope.** This is a written derivation audit, not independent expert acceptance or a formal-kernel PDE certificate.

## Inputs read for this review

- The full outer source `outer-matching.md` and Boole's independent review the recorded local calculation.
- The full inner source `inner-matching.md`; my completed review is the recorded local calculation.
- Sections 2–5 of `references/analysis/actual-seed-cost.md`; my completed review is the recorded local calculation.
- The nonlinear criterion and new whole-envelope section 8 in `references/analysis/mixed-seed-nonlinear-budget.md`.
- The original first-stage theorem and physical rescaling in `references/navier-stokes/loglog-handover.md`, together with the original-time preparation's higher-jet argument.

The interface checks found no missing sign, receiving-frame change, carrier scaling, or outer normalization. The analysis below records the end-to-end estimates used by the assembled draft. No canonical files or DNS were changed.

## 1. Quantifiers and base trajectory

Choose one sufficiently thin unscaled geometric Gavrilov profile V_j with f_j(P_j)=1, fix j and nu>0 before h tends to zero, and use its actual physical-time Floquet exponent mu_j in T=(2/mu_j)log ell. Do not silently impose the older, j-dependent L2 normalization or substitute the limiting exponent 2/3 on a growing time interval.

The base q is the actual first-stage smooth NS solution through T, at epsilon=nu h^4. Its primary approximation and true errors give the all-time actual-particle phase and coefficient control used in the seed reduction. The endpoint of the receiving branch is t_f=T-ell^(-3/4), inside that established lifespan. The theorem needs no extension of q beyond its known interval.

## 2. Selected outer/inner column

The exact outer lift maps the primary tangent plane to the receiver's plane, without truncating pressure. Its remainder retains the second-row pressure contribution O(ell^(-2)u^(-5)). The stable-kernel ratio is f(t)/f(s), as required by differentiating the exact factor exp(mu t)f0/f(t). These estimates give one real, bounded, nonzero initial polarization whose terminal overlap values have a common positive coefficient D_h comparable to ell^(5/2).

In the common frame (p,r,n), with the unit terminal ray r and Lambda=|beta(t_f)||N(t_f)|/ell, the overlap data are exactly

    V(R)=D_h R^(-2)(1+o(1)),
    W(R)=2D_h R^(-3)(1+o(1)),
    V=b_p/sqrt(Lambda), W=b_n.

The independently reviewed inner proof handles this relative mismatch in a norm with O(eR), e=Lambda^(-1/2), error. It keeps the actual terminal coefficients of the fixed profile, and its positive connection is uniform in terminal phase. At u_m=ell^(-3/10), both R^(-2) and eR tend to zero. Thus it provides terminal components of orders ell^3 along p and ell^(5/2) along n, with positive lower bounds, for this exact model solution.

The outer history satisfies |xi||b|<=C ell exp(mu t)<=C ell^3, and its time integral is at most C ell^3 by direct exponential integration. The inner weighted bound also gives sup |xi||b|<=C ell^3 over an interval of length u_m. Thus the combined time integral is C ell^3, without an additional log ell factor. The initial vector may be divided by its uniformly bounded and bounded-below norm to have norm one; this changes only fixed constants. Multiplying the complete ray by 4 gives terminal magnitude 4 and only multiplies the ray/history norms by a fixed factor.

## 3. Transfer of this selected branch to actual q

The coefficient reduction gives sup|A_q-Abar|<=h^(1/24)exp(C ell), up to harmless fixed powers of ell; both integrated gradient norms are O(ell). Unit-direction comparison on the sphere and then log-magnitude comparison preserve this error form. The actual and model terminal receiving frames differ by the same admissible small amount.

To compare a selected column, rotate its unit initial tangent vector by the small orthogonal rotation between the model and actual initial cotangent normals. Propagate forward using the actual pressure-corrected 3D amplitude equation. Duhamel and the generic exp(C ell) bounds for the two amplitude propagators show a uniform absolute selected-solution difference h^(1/24)exp(C ell). This is negligible compared with every fixed power of ell, even negative ones. Endpoint frame rotations preserve that conclusion.

Hence the actual branch v_h can retain norm-one initial data, terminal p and n orders ell^3 and ell^(5/2), and whole-history product supremum and integral at most C ell^3, with initial covector size at most C ell. This is a selected-column argument. It needs no new asymptotic for the full operator's adjoint row or smallest singular value. It also does not assume a polynomial generic linearized PDE propagator.

## 4. Final-ball preparation and the whole support

Normalize the actual central branch by its nonzero final normal component N_h=n dot v_h(t_f). Set B_c=v_h/N_h. Prescribe c_h=B_c(t_f) on a final radius-d ball, with an affine phase gradient xi*=4r and a fixed real bump chi with chi(0)=1. Prepare the unweighted amplitude and the phase by the actual-q inviscid flow/ODE, and take

    b=k ell^(7/8) chi_t B,
    k=h^(3/2), d=h^(5/4).

This recovers precisely the chosen central branch and produces |c_h|<=C ell^(1/2). It is a finite-dimensional inverse preparation of the initial amplitude, not backward viscous evolution. The primary receiving phase S/k+pi/2 is constant pi/2 on the central q particle.

The q-jet estimate through order 24 has coefficient m(t)=1+ell^(-1)exp(mu t), with integral O(ell). Fixed-order flow and polarization derivatives consequently cost exp(C_r ell). In h-scaled coordinates the differentiated coefficients have this same top integrable coefficient, with a triangular lower-order hierarchy. The final-ball support has diameter at most d exp(C ell)=o(h), and exact volume O(d^3) by incompressibility.

Thus, for the unweighted amplitude and ray, uniform variation across the support is at most (d/h)exp(C ell)=h^(1/4-o(1)). Products of conditioning factors only enlarge C. The bump itself is not relatively constant; it is factored separately. Its derivatives cost d^(-r)exp(C ell), and its support contributes d^(3/2) in L2, without a growing-domain volume factor.

This gives

    ||Z(0)||C1<=C ell^(-5/8)+h^(1/4-o(1)),
    integral_0^t_f sup_support |b||xi|/k dt
        <=C ell^(11/8)+h^(1/4-o(1))=o(ell^2).

The curl correction and slow envelope derivatives in C1 have orders (k/d)exp(C ell) and (k/d)^2 exp(C ell), so they vanish. This is the explicit whole-support history estimate required for the nonlinear criterion; a central bound alone would not suffice.

## 5. Nonlinear mean, pressure, and harmonic corrections

For real b and S, the exact real curl wave has the quadratic split Q0+Re(F2 exp(2iS/k)). The apparent |b|^2/k term cancels by xi dot b=0. Its nonoscillatory mean must be solved with the full global pressure and cannot be projected away locally. The first oscillatory forcing includes the linear curl/pressure residual F1.

The global solenoidal mean m solves the linearized inviscid Euler equation about actual q, forced by -Q0, with zero initial data. The first harmonic must also cancel (i/k)(m dot xi)b. This term is necessary because the pressure-generated mean need not be tangent to xi. The tangent harmonic ODEs and the displayed longitudinal pressure amplitudes cancel all leading forcing components, including the component parallel to xi. Exact curl lifts make the corrected fields solenoidal. All added corrections are zero at time zero.

For the weighted mean estimates, pressure disappears from every differentiated solenoidal L2 pairing. Weighted q commutators satisfy

    d^(j-1)||D^j q||inf<=C_j m(t)(d/h)^(j-1).

Global weighted Sobolev estimates control the nonlocal mean in L-infinity; no L-infinity Leray bound or compact support of the mean is assumed. Harmonic transport has ||G||<=3||A|| independently of the ray magnitude. Differentiated G coefficients cost positive powers (d/h)^r exp(C ell), which tend to zero for fixed r>=1; the top coefficient remains C_r m(t), rather than exp(C ell). Thus the correction estimates avoid a second exponential of the generic jet bound.

At the fixed derivative orders needed for the construction, the mean and harmonic amplitudes are bounded by k^2 d^(-1-r)E_h pointwise and k^2 d^(1/2-r)E_h in L2, with log E_h=O(ell) after fixed products. The mean need not be supported in the patch; only its products with oscillatory packets use their volume factor.

## 6. Full residual and independent strong continuation

After the exact cancellations, the worst remaining L2 order is k^3 d^(-1/2)E_h. It includes the corrected curl residual, slow interactions, and fast mean/harmonic interactions of amplitude (k^2/d)^2/k on a volume O(d^3). Tangent harmonic interactions have no unpriced 1/k principal term. The leading viscosity error is epsilon k^(-1)d^(3/2)E_h, which is smaller. The resulting time-integrated residual is h^(31/8-o(1)).

The explicit history, not a generic PDE propagator assertion, gives

    integral ||grad U||inf <= C ell+C ell^(11/8)+o(1)
       =o(ell^2).

Since log(1/h)=ell^2, exponentiating this coefficient costs h^(-o(1)). The exact L2 energy of w=Q-U cancels its quadratic self-advection and yields ||w||2<=h^(31/8-o(1)), starting from w(0)=0.

Smooth existence cannot be inferred from that L2 estimate alone. Under the separate bootstrap ||grad w||inf<=1, the H12 energy of exact Q has the same integrable coefficient. The initial perturbation and the approximate solution have H12 size at most

    k d^(3/2) k^(-12)E_h=h^(-117/8-o(1));

the first-stage q contribution is smaller. The uniform expanding-torus GN inequality then gives

    ||grad w||inf
      <=C||w||2^(19/24)||w||H12^(5/24)+C||w||2
      <=h^(1/48-o(1)).

This strictly improves the gradient bootstrap. H12 remains finite for each fixed h through the desired time, so the strong solution continues. Uniformity of GN follows from local Euclidean inequalities with a low-frequency L2 term; the torus side lengths are bounded below and grow. The corresponding velocity error is h^(25/16-o(1))=o(k). No small physical H12 norm is being claimed.

## 7. Final observable and physical scope

At the central reference q particle, the receiving phase is pi/2 and the leading symmetric strain is

    -sym(b tensor xi)/k,
    |sym(b tensor xi)|=|b||xi|/sqrt(2),

because b is tangent to xi. After normalization the p amplitude supplies strain at least c ell^(11/8), while the n amplitude has order ell^(7/8). The original host strain is O(ell); slow terms, mean and harmonic corrections, and the true nonlinear error vanish in C1. Therefore the stated total strain handover at that spatial point follows. At the final time the phase is affine and the unweighted amplitude and bump are constant near the center, so d_b and its derivatives vanish there; the primary gradient identity is exact. The observation at the q particle location suffices for a spatial supremum; it is not automatically a trajectory statement for Q.

For physical fixed viscosity, A_L=L^(7/5), y=Lx and tau=A_L L t. The rescaled viscosity is nu L/A_L=nu h^4. Strain multiplies by A_L L=L^(12/5), physical time is t_f/L^(12/5), and unnormalized rescaled L2 becomes physical averaged L2 by the factor h/(2pi)^(3/2).

Thus rescaled initial perturbation C1 tending to zero is not a uniformly small physical C1 perturbation. The initial data change with L. The receiving branch is finer than the primary h wave, but its own ray magnitude decreases from order ell to 4; its own wavelength grows from order k/ell to order k. This is amplification of an initially supplied fine seed, not creation of an initially absent frequency or monotone forward frequency growth. No infinite cascade, one-data blow-up, global regularity, or complete formalization follows.

## Arithmetic receipt

Fourteen independent exact rational checks passed: residual 31/8, principal viscosity 35/8, H12 exponent -117/8, GN gradient exponent 1/48, velocity exponent 25/16 and gap 1/16 above k, coherence d/h exponent 1/4, curl k/d exponent 1/4, initial ell exponent -5/8, history and final ell exponents 11/8, physical L2 exponent -1/10, physical strain exponent 12/5, and viscosity exponent -2/5 in L. These are arithmetic controls, not proofs of the analytic estimates.

## Final assembled-draft verdict

The assembled theorem passes at its stated finite scope after making the primary pressure explicit. I verified the added formula directly in the revised draft:

    pi_Z=2 i k (xi dot A b) exp(i theta)/|xi|^2,
    Pi_h=pi_q+pi_m+Re(pi_Z+pi_1+pi_2).

The gradient of pi_Z cancels the parallel leading primary amplitude term and leaves exactly the slow pressure contribution in F1. Omitting this pressure would invalidate the claimed residual expression; it is now explicitly included. No change to the velocity construction or exponents was required.

The stronger integral claimed in the final draft is justified: the outer product integrates to C ell^3, the inner product contributes at most C ell^3 u_m, and the actual-q comparison and envelope variation contribute only positive-h-power errors. After division by the final normal component ell^(5/2) and multiplication by ell^(7/8), this gives C ell^(11/8) with no logarithm. Hence the final loss factor can indeed be taken as a fixed power of ell times exp(C ell^(11/8)). The weaker logarithmic bound from the earlier conditional criterion is unnecessary.

The optional endpoint-row corollary also checks. For arbitrary bounded initial outer coordinates, the homogeneous stable term contributes y2=O(ell^(-2)) near the overlap. The full-matrix outer bounds give R^2|V(R)|+R^3|W(R)|<=C ell^(5/2). The inner weighted operator estimate therefore bounds the p and n rows by C ell^3 and C ell^(5/2), respectively; the selected column supplies matching lower bounds. Using the exact plane determinant r_h comparable to ell yields the stated pure cost of order ell^3 and optimized scalar normal-output cost of order ell^(-3/2). The nonlinear construction uses the explicit selected column and is not contingent on uniqueness or a characterization of the optimizer.

The derivative budget in the final draft is sufficient. For first-stage C24, fixed H128 is above the interpolation threshold 4(24+3/2)=102; the scaled error has positive exponent13/256. The specified phase/amplitude order160, mean H132 and harmonic order129 cover the derivatives of the first approximation needed for H128. For the receiving correction, b and xi through order18 (phase19) cover the mean source through H16; q C24 and g through13 cover the curl-lift H12 estimate. The phase-derivative index has not been confused with the covector index.

The remaining residual table also checks: quadratic/global-mean products k^4 d^(-3/2) have exponent33/8, oscillatory viscosity epsilon d^(1/2) has37/8, and slow-mean viscosity epsilon k^2 d^(-3/2) has41/8. Each is smaller than the31/8 leading residual. Normal mean/harmonic feedback and global pressure tails are included. The exact NS energy does not invoke a polynomial bound for an arbitrary error propagator.

Every datum in the theorem is real, smooth, divergence-free and mean-zero. The primary and harmonic packets are exact compactly supported vector-potential curls. Q0 is a sum of divergences: its first two terms are div(b tensor b), and d_b is solenoidal, so its last term is also a divergence. Its spatial mean is zero. The solenoidal mean equation about q has divergence-form transport/stretching, hence preserves zero mean. The final field solves the full unforced NS equation; mean/harmonic forcing is only an ingredient of the auxiliary approximation.


Reviewed assembled-source SHA-256 after the primary-pressure completion: `3d25dbcc64620ad6d7323c18b2760c7c832fabe9fb9518d9a3a8ac7db1171f94`.

## Additional independent review: the restricted smooth-seed supply obstruction

I independently read `references/analysis/smooth-seed-supply.md` in full. It passes at its explicit common-coordinate, compact-domain, disjoint-or-quantitatively-noncancelling scope. It is not a universal cascade obstruction.

Freeze e=xi(y_h)/|xi(y_h)| as a constant direction when differentiating. At theta=pi/2, with q=theta', direct threefold differentiation gives

    (b cos theta)'''=b(q^3-theta''')-3b' theta''-3b''q,
    (-k d_b sin theta)'''=-k d_b'''+3k d_b' q^2
                                      +3k d_b q theta''.

I checked this combined identity independently with SymPy; it passes exactly. The leading projection onto v=b/|b| is |b|(|xi|/k)^3. With a_h=k ell^(-13/8) and |xi| comparable to ell, its size is k^(-2)ell^(11/8). The six remainder ratios have respective positive h powers 1,3/4,1/2,1,1/2,3/4, with fixed powers of ell and exp(C ell). They all vanish. The use of xi derivatives through order4 is correct: d_b''' differentiates the vector potential four times, so phase derivatives through order5 cover the stated jet bound. Phase order3 alone would not cover it.

For pairwise disjoint closed supports, a neighborhood of each designated interior center contains only its own packet. If the total field were C3, that local equality would force an unbounded sequence of third-derivative tensor norms on a compact domain, contradicting continuity. No interchange of an infinite derivative series is required. The specified quantitative noncancellation condition gives the same conclusion. For a noncompact domain with centers escaping every compact set, unbounded global derivatives do not contradict local smoothness; the source correctly excludes that inference.

Under the same support/noncancellation assumptions, attenuation eta requires eta k^(-2)ell^(11/8)<=C for bounded C3, hence eta<=C k^2 ell^(-11/8). The principal matched terminal strain then is at most C k^2 and the normal strain at most C k^2 ell^(-1/2), both tending to zero. The fixed finite-transfer remainder estimates remain small uniformly for 0<=eta<=1; they cannot restore host-dominating strain within that same mechanism and window. By contrast dominance of the order-ell host requires eta bounded below by a constant multiple of ell^(-3/8). These bounds are incompatible.

The physical derivative conversion is also correct: A_L L^3=h^(-44), so the receiver's physical third derivative has size at least h^(-47)ell^(11/8). General changes of coordinate and amplitude obey their own multipliers and the condition epsilon=nu s/A for fixed physical viscosity. The note does not treat arbitrary rescaling, cancellation, generated seeds, or nonlinear superposition as already excluded.
