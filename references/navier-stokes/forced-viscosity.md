# Ordinary viscosity, smooth forcing, and a possible recursive wave stage

Independent agent review: [scope and corrections](../analysis/forced-stage-review.md). These reviews do not certify a complete Navier–Stokes proof.

Bounded analysis, 8 September 2026. This note treats smoothly forced NS as a valid separate target alongside unforced NS. It does not claim either target is solved. The direct Euler transfer below is excluded; a redesigned viscous construction remains open. No flow simulation or formal-certification claim.

## 1. Primary sources and the force contract

The [official Fefferman problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), equations (1), (8)--(9) and alternative D on printed pp. 1--2, uses

    partial_t u+u.grad u+grad p=nu Delta u+f, nu>0.            (1)

For the periodic breakdown alternative, u0 must be smooth and solenoidal, and the prescribed periodic force must be smooth for all t>=0, with every mixed spatial/time derivative decaying faster than any inverse power of t. On a finite candidate interval [0,T], this in particular requires bounded, compatible terminal limits of every such derivative. A force smooth only for t<T is insufficient. A force constructed smoothly through T can be extended smoothly and cut off at a later time; extending the force does not require extending a singular solution. R3 alternative C additionally requires rapid spatial decay. A force with one fixed compact spatial support can meet that spatial requirement.

The released [Alpöge--Buckmaster Euler manuscript](https://cims.nyu.edu/~tristanb/euler.pdf), Theorem 1.1, p. 2, states bounded velocity, fixed compact spatial support, smooth terminal forcing and divergent full vorticity. The support of the complete velocity is explicitly established in section 13.2, p. 107, and the bounded velocity/energy in Proposition 13.3, p. 108. Proposition 12.3, equations (12.16)--(12.17), pp. 104--105, controls the complete physical force in mixed norms with one increasing-order sequence. Lemma 13.2, p. 108, supplies the terminal extension. These are statements of the released paper, not a replay of its entire proof.

Live retrieval in this task confirmed the unchanged PDF SHA-256 `97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8`, 1,105,306 bytes, Last-Modified 8 September 2026 03:58:12 UTC. The [Boussinesq companion](https://cims.nyu.edu/~tristanb/boussinesq.pdf) remains at SHA-256 `895a628d1783bcb039374686f50b895b5f450f53b8ef8aa173523487a7a4a21b`. No ordinary-viscosity theorem is attributed to either document.

## 2. Literal Euler-to-NS conversion: sign and zeroth-order failure

Suppose on t<T the same smooth velocity and pressure obey

    partial_t u+u.grad u+grad p_E=f_E, div u=0.

Keeping that velocity and that pressure in (1) requires exactly

    f_NS=f_E-nu Delta u.                                    (2)

The sign is minus, since viscosity is on the right of (1). Thus

    partial_x^alpha partial_t^m f_NS
      =partial_x^alpha partial_t^m f_E
                   -nu Delta partial_x^alpha partial_t^m u. (3)

At each fixed preterminal time (2) is a legitimate smooth force. It does not automatically have a smooth extension to T.

Here is an elementary obstruction for the released compact velocity. Enclose its fixed support in B_R after translating the origin. For each component use the Newton potential for Delta; since u is smooth and compactly supported at every t<T,

    u=Delta^(-1)Delta u,
    omega(x)=curl u(x)=integral grad G(x-y) cross Delta u(y)dy,
    |grad G(z)|=1/(4pi |z|^2).

For x in B_R, the integration region lies within distance 2R. Outside B_R, omega=0. Consequently

    ||omega(t)||_infinity<=2R ||Delta u(t)||_infinity.         (4)

The released vorticity limit therefore implies ||Delta u||infinity->infinity. Because f_E is uniformly bounded through T, (2) satisfies the explicit lower bound

    ||f_NS(t)||_infinity
      >=nu/(2R)||omega(t)||_infinity-||f_E(t)||_infinity
      ->infinity.                                           (5)

Thus the direct same-pressure transfer already fails the force's zeroth-order terminal bound. There is no need to estimate its higher time derivatives to reject this proposal. Shrinking support of individual waves does not help a supremum norm.

## 3. A pressure change cannot repair smooth force for that same velocity

Allow p_NS=p_E+phi. Then

    f_NS=f_E-nu Delta u+grad phi,
    nu Delta omega=curl f_E-curl f_NS.                       (6)

An arbitrary gradient cannot remove the second identity. On the same fixed compact support, Newton inversion for omega gives

    ||omega||infinity<=2R^2 ||Delta omega||infinity.           (7)

Indeed |G(z)|=1/(4pi |z|), whose integral on B_(2R) is 2R^2. Combining (6),(7),

    ||curl f_NS||infinity
      >=nu/(2R^2)||omega||infinity-||curl f_E||infinity.      (8)

Every possible pressure choice therefore fails at least a first spatial force-derivative bound. This does not assert that every such gauge fails in C0; (5) is specifically the same-pressure claim, while (8) is gauge independent.

There is an equivalent fixed-torus argument: omega has zero mean, the inverse Laplacian on that fixed torus has an integrable Green kernel, and ||omega||infinity<=C_T ||Delta omega||infinity. Alternatively, Leray projection gives nu Delta u=P(f_E-f_NS); smooth bounded all-order force norms bound this expression by fixed-torus elliptic estimates. The mean of u is separate and does not affect vorticity. Thus the obstruction is not an artifact of the particular Newton kernel or pressure normalization.

This excludes retaining the released Euler velocity with an admissible smooth NS force. It is not an obstruction to a different viscous velocity whose evolution absorbs diffusion.

## 4. A viscous adaptation must also change the bounded-velocity conclusion

There is a second useful boundary. A smooth finite-energy NS solution with bounded velocity and smooth force on a finite interval cannot have a classical breakdown there. In fact, pairing (1) with -Delta u yields, by incompressibility and Young's inequality,

    d||grad u||_2^2/dt+nu||Delta u||_2^2
       <=(C/nu)||u||infinity^2||grad u||_2^2
                                      +(C/nu)||f||_2^2.     (9)

Uniform velocity and force bounds give a finite H1 bound through T. The standard local strong H1 continuation alternative then extends the solution. The same conclusion is noted on printed p. 3 of [Fefferman's statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). This argument applies to a fixed torus or R3 with the stated finite-energy and force norms.

Thus a successful ordinary-NS redesign cannot simultaneously preserve the released Euler theorem's uniformly bounded velocity and retain a smooth admissible force. It must allow velocity to become unbounded as well as its derivatives. In particular, an infinite construction with summable uniform velocity increments, as in the released Euler Lemma 13.1, cannot be copied unchanged. Large strain alone is not the terminal NS objective. This is consistent with finite-energy concentration: a velocity amplitude can increase while its spatial L2 mass decreases.

## 5. Heat absorption: exact affine wave and explicit controls

Let U=A(t)x be a trace-free affine background, xi'=-A^Txi, b.xi=0, and k=1/K. Put

    b'=-Ab+2xi c+r, c=(xi.Ab)/|xi|^2, xi.r=0,
    s=xi.x/k,
    partial_t F(t,s)=nu |xi|^2 k^(-2)F_ss(t,s)+gamma(t,s).

Here r is a tangent amplitude control and gamma is a zero-mean phase-profile control. Let Q_s=F with the fixed zero-mean primitive convention. The exact affine NS field and pressure are

    u=A x+b F(t,s),
    p=-x.sym(A'+A^2)x/2-2k c Q(t,s),
    f=skew(A'+A^2)x+r F(t,s)+b gamma(t,s).                  (10)

The self-interaction of the transverse wave vanishes exactly. Equation (10) follows by direct differentiation and includes the principal pressure cancellation. In the unforced-compatible case A'+A^2 symmetric, r=gamma=0, it is an exact unforced affine solution, although not finite energy or generally periodic. This is the mechanism established in [the viscous flat-core note](../analysis/viscous-flat-core.md).

With r=gamma=0,

    F(t)=exp(D(t)partial_s^2)F(0),
    D(t)=nu k^(-2)integral_0^t |xi(s)|^2 ds.                 (11)

For any nonzero phase Fourier mode n, its attenuation is exp(-n^2 D). The factor is scalar, hence commutes with the pressure-corrected amplitude propagator. If G_b is its inviscid velocity-amplitude gain and r_xi=|xi_out|/|xi_in|, the gain of that harmonic's strain is exactly G_b r_xi exp(-n^2 D). A fixed zero-mean profile also satisfies ||F_s(t)||infinity<=exp(-D)||F(0)||A1, where A1 is its weighted Fourier l1 norm. Heat absorption removes the rough force in (2) by changing the velocity; it does not remove diffusion's cost to the gain.

If the fixed initial profile equals s for |s|<a, then on |s|<=a/2,

    |partial_s^m(exp(D partial_s^2)F-s)|
      <=2D ||F^(m+2)||infinity exp(-a^2/(16D)).              (12)

For a required physical spatial jet order m, this must still be multiplied by |b_out|(K|xi_out|)^m. Mixed time derivatives carry their own material/physical phase and clock rates. Neither a small D nor a flat core alone proves bounded physical all-order forcing.

For one packet in the already completed finite handover, take the central clock instead of a spatially varying one. Its fully derived profile residual is in [the localized-profile calculation](localized-profile.md). In its rescaled units,

    epsilon=nu h^4, k=h^(3/2), d=h^(5/4),
    D_c<=C_nu h ell^2 log ell,
    ||clock mismatch||L2<=nu h^(37/8)E_h,
    integral ||complete residual||L2<=h^(31/8)E_h.           (13)

All phase Fourier modes, the nonlocal mean, pressure and curl corrections were retained. This is a genuine finite calculation, independently reviewed. It is not an all-order physical-force gluing estimate. Taking the approximation rather than the exact unforced comparison solution and calling its residual a force changes the required proof norm.

## 6. The released Euler two-field principal reset survives scalar damping

There is a more specific possible import than an arbitrary affine control. The axisymmetric NS variables

    Gamma=r u_phi, Xi=omega_phi/r, v=(u_z,r u_r), y=(z,r^2/2)

satisfy the exact equations

    D_v Gamma=nu L_Gamma Gamma+r f_phi,
    D_v Xi=nu L_Xi Xi+r^(-4)partial_z(Gamma^2)
                                      +(curl f)_phi/r,
    L_Gamma=partial_z^2+partial_r^2-r^(-1)partial_r,
    L_Xi=partial_z^2+partial_r^2+3r^(-1)partial_r.            (14)

These follow from the cylindrical vector Laplacian and the vorticity equation. Transforming to the volume coordinate gives

    L_Gamma=partial_1^2+2y2 partial_2^2,
    L_Xi=partial_1^2+2y2 partial_2^2+4partial_2.             (15)

Compare [released Euler equations (2.1)--(2.6), p. 3, and (3.2)--(3.4), p. 7](https://cims.nyu.edu/~tristanb/euler.pdf). For a material phase N p.A_old and covector zeta, both variables have the SAME principal viscous symbol

    d_visc=nu N^2(zeta_1^2+r^2 zeta_2^2)
           =nu N^2 r^2 kappa,
    kappa=zeta_2^2+r^(-2)zeta_1^2.                          (16)

The phase profile for Xi is differentiated once relative to the circulation profile, which does not change that scalar symbol. For a Fourier index n!=0 in the general periodic phase profile, the symbol is n^2 d_visc. On a fixed supplied older state, its normalized two-component principal amplitude law is therefore

    R_NS,n'=(B(t)-n^2 d_visc(t) I)R_NS,n,
    R_NS,n(t)=exp(-n^2 integral d_visc)R_Euler,n(t).         (17)

In particular the principal return condition Omega_out=0 at the selected material center is unchanged for every phase Fourier mode, and the direction of each pair is unchanged. For a single fundamental harmonic its retained amplitude is reduced by exp(-D); for general F the retained circulation profile is T_Euler,out exp(D partial_s^2)F, rather than one scalar times F. Equivalently one can retain the inviscid amplitude pair and evolve the common profile by heat. This is an actual algebraic reason to examine the released reset in viscous NS: its two channels have matching principal diffusivity. It is not enough to add -nu Delta u to their old force, and no two-harmonic truncation is being assumed.

The obligations left by (17) are precise. The extra drift 4nu partial_2 Xi, the two operators' variable coefficients, envelope derivatives, the mean and complete force recovery all survive at lower order. The older field and its feedback control will themselves change under viscosity. Consequently (17) is a fixed-older-state principal identity, not a theorem that the released infinite selected history persists. Its force reconstruction must be redone for the complete viscous residuals, with all mixed derivative costs.

## 7. One-stage amplitude, frequency, and activation budget

Work now in one common physical coordinate system with fixed nu>0. On stage j let K_j be the phase frequency parameter, d_j the envelope scale, Delta_j the duration, a_in,j and a_out,j the velocity amplitudes, and let D_j=nu integral |K_j xi_j(t)|^2 dt. A mere coordinate rescaling cannot change D_j.

If the central covector lies between fixed positive bounds and the inviscid amplitude exponent is G_j=log(||M_j||), then a necessary principal gain budget for a selected scalar branch with gain at most exp(G_j) is

    a_out,j<=C_0 a_in,j exp(G_j-D_j),
    D_j>=c nu K_j^2 Delta_j.                               (18)

Replace ||M_j|| by the actual selected gain for an equality on that branch. The covector endpoint ratio must also be retained when the desired output is strain rather than velocity.

For a smoothly forced construction the new packet may be activated from zero after time zero, provided the activation force itself is admissible. Let an activation take duration Delta_act,j and use a fixed flat time cutoff. For its complete physical derivative orders through p, suppose the known older-flow/phase/shape rates are bounded by a number Omega_j>=1. This number must include K_j, d_j^(-1), Delta_act,j^(-1), Eulerian phase rates K_j||q||infinity and the finitely many derivatives actually differentiated; it is not just an inverse material time.

Direct differentiation of the leading tangent activation force gives the sufficient bound

    ||f_act,j||C^p_(x,t)
       <=C_p a_in,j Delta_act,j^(-1) Omega_j^p.             (19)

Curl localization and its required pressure may enlarge C_p and Omega_j; their full contributions must be included before applying (19). Here a_in,j must bound the complete activated profile, and Omega_j must bound its normalized mixed derivatives; a leading amplitude alone is insufficient. If the per-stage force budget is eta_j, choose

    a_in,j<=eta_j Delta_act,j/(C_p Omega_j^p).               (20)

Then attaining a prescribed velocity a_out,j requires at least

    G_j-D_j>=log[a_out,j C_p/(C_0 eta_j Delta_act,j)]
                                                        +p log Omega_j. (21)

This is the gain required under the sufficient activation policy (20). Since (19) is an upper estimate, (21) is not a lower cost theorem for every activation whose actual force satisfies the budget. For all-order gluing, one sequence must have p=p_j->infinity, summable eta_j, bounded all-order norms for every fixed old increment, and compatible time joins. Choosing an independent frequency anew for each derivative order does not meet this contract.

For a host producing inviscid growth rate at most Gamma_j, (18),(21) imply

    (Gamma_j-c nu K_j^2)Delta_j
       >=log[a_out,j C_p/(C_0 eta_j Delta_act,j)]+p log Omega_j. (22)

This formula is a restriction on the stated stage mechanism and source bounds, not a universal NS inequality. It shows why arbitrarily increasing a child's frequency is no longer a free way to make force residuals small.

If a flat core must be preserved to a negative power of K_j through order p, (12) typically imposes D_j<=C/(p log K_j+log eta_j^(-1)+other fixed-order logarithms). If the same stage needs a positive gain logarithm of order p log K_j, the simple constant-rate, bounded-covector model then demands

    Gamma_j/(nu K_j^2)>=c (p log K_j)^2.                    (23)

Equation (23) records the additional cost of requiring BOTH very small interior heat rounding and very large gain. It is not necessary for every possible profile or reset scheme; it is the transparent budget for this particular heat-flat-core design. A more efficient actual covector history should be charged by its full D_j in (21), rather than by replacing it with K_j^2 Delta_j.

## 8. Reset controls: what shrinking a support does not buy

It is tempting to restore an unheated F by adding gamma=-nu K^2|xi|^2 F_ss. In (10) that control has physical spatial derivatives of order m with size

    nu |b| K^(m+2)|xi|^(m+2)

on a region containing its nonzero profile derivatives. The exact coefficient is the appropriate fixed F^(m+2) norm; it is nonzero for the required transition of a periodic flat profile. The inner core may avoid this region, but the force's global supremum cannot. This is the original rough-force problem moved to the profile transition, not a smooth terminal reset.

Likewise an arbitrary prescribed affine matrix history produces the core forcing M(t)x with M=skew(A'+A^2). Its force gradient has size |M|, independent of the radius of the core. Localizing the affine velocity inside a radius d makes the force value smaller there but does not make its C1 norm small.

For a particularly transparent reset test, let A=lambda p tensor n with p.n=0 and |p|=|n|=1. Then A^2=0, omega_A=lambda n cross p and A omega_A=0. The exact affine vorticity equation is

    omega_A'=curl f,                                       (24)

so changing this vector by order lambda during a time Delta necessarily costs

    integral ||curl f||infinity dt>=|omega_A(out)-omega_A(in)|,
    sup ||curl f||infinity>=c lambda/Delta                  (25)

when those endpoints differ by c lambda. Such an increasing-vorticity reset cannot be performed solely by a bounded smooth body force on shrinking intervals. This is a test of the specified nilpotent affine path, not a claim that every orientation change has this cost. For example p,n can rotate together around their fixed cross product without changing omega_A; then the displayed lower bound is zero. General ambient stretching can also change vorticity without curl force.

The useful requirement is consequently a dynamically produced return with small complete force defect, such as the scalar-damping-compatible two-field return in (17), rather than a freely prescribed rotation or profile reconstruction. A proof must also charge the cutoff annulus and its nonlocal pressure in physical coordinates.

## 9. Smallest decisive next calculation for the forced route

The most focused next task is a single axisymmetric viscous insertion on a supplied older NS state, using the exact operators (14)--(16). For the selected periodic D target, its local axisymmetric chart and cutoff must be embedded in one fixed periodic domain with periodic pressure and full force compatibility. Global whole-space axisymmetry cannot simply be imposed on a torus; switching to alternative C would also require its spatial decay bounds. Keep the common heat clock in the two-component profile equation, and compute the controlled return map and complete physical force through a fixed correction depth J. The deliverable should contain, simultaneously:

1. A selected principal gain and Omega_out=0 return with its attenuation D_j and error tolerance stated quantitatively.
2. The surviving 4nu partial_2 Xi term, all variable-symbol and cutoff terms, both phase means and a compact physical-force recovery, with no residual replaced by its curl alone.
3. Mixed physical force bounds through order p at every correction level, including activation and reset joins. Identify exactly how the remainder improves with J when viscosity is fixed and K grows.
4. A nonempty set of one-stage parameters satisfying (21), a target output with increasing velocity rather than only vorticity, and the force bounds. Only after this calculation should one attempt a single all-order infinite sequence.

This has a sharper success/failure test than asking whether forcing can reproduce a desired velocity path. The existing finite heat-profile calculation discharges the leading viscosity cancellation and gives a workable all-profile correction operator in one short regime; the released Euler construction supplies an explicit projective return mechanism and an all-orders source bookkeeping design. The missing assertion is that these can be made compatible with ordinary viscosity, unbounded terminal velocity, and one admissible force schedule.

The forced target is independent of the repository's unforced ROOT. A valid smoothly forced periodic breakdown would address Clay alternative D; it would not prove unforced breakdown, nor establish the project's unforced regularity claim. Both targets remain open here.
