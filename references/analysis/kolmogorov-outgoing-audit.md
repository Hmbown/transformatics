# Short-time Kolmogorov amplification on the actual outgoing NS flow

**Research appendix — 8 September 2026. Reviewed written result, outside the registered proof graph.** A complete independent mathematical review accepted the actual-q coefficient estimate, full affine/Piola and pressure residual, curl localization, real normalization, radial high-pass estimate and absolute error closure. The exact viscous **linearization**, supplied with data at a late time, gains a fixed positive power of ell over an interval of order log(ell)/ell. This excludes a scale-uniform arbitrary-error bound polynomial in accumulated strain for this family. It does not exclude estimates for more restricted error classes.

The frequency cutoff is a fixed multiple of 1/h, not h^(-3/2). Original-time seed supply, nonlinear evolution of this cell mode, uniform iteration, full formalization, ROOT and (E′) remain open. The historical proposal is preserved after the completed derivation. See the [review index](../navier-stokes/next-transfer-review.md).

**Review provenance.** Completed source `nse-kolmogorov-shorttime-completion-20260908.md`, SHA-256 `6969fa98fe198ac35058fe33b36fedacdfc0dd727868015b03ebf633dee2ad5c`. A separate reviewer rederived the estimates and checked eight exact scale margins. The primary [Lin–Xu spectral statement](https://arxiv.org/html/1707.00278#S4.SS2) was reopened independently. These are written analytic reviews and finite algebra checks, not a formal-kernel certificate. No research DNS was run.

## 1. Statement and fixed inputs

Use the actual first-stage solution q from [the log-log theorem](../navier-stokes/loglog-handover.md), with the additional fixed-order estimates in [the outgoing-wave theorem](../navier-stokes/outgoing-wave.md). Write

    lambda=ell=sqrt(log(1/h)), epsilon=nu h^4,
    delta=sqrt(h), r=h^(3/4),
    tau=kappa log(lambda)/lambda, t0=T_h−tau.

Here nu>0, the compact profile V, its orbit and all finite derivative orders are fixed before h tends to zero through the existing first-stage family. The positive constant kappa is chosen below from those fixed bounds. For small h, tau<lambda^(−3/4), so [t0,T_h] is inside the previously proved smooth lifespan and terminal gradient window.

**Result of this derivation.** There are fixed c,d>0 and real, smooth, mean-zero, exactly solenoidal unit-L2 data f_h prescribed at t0 such that the exact homogeneous viscous linearization about q has

    ||w(T_h)||_2 >= c lambda^d,
    w_t−epsilon Delta w+P[(q.grad)w+(w.grad)q]=0,
    w(t0)=f_h.                                            (1)

The datum is localized at width comparable to r and oscillates on the original outgoing cell scale h. Section 9 also gives a radial high-pass version with threshold comparable to 1/h. It is NOT the finer h^(−3/2) threshold of the registered outgoing-wave theorem. All norms are unnormalized on the expanding torus, and constants are independent of its size. The gain ratio is unchanged by the existing physical rescaling.

The independent review checked the coefficient comparison (4), exact residual (10), and real averaging argument. The proof uses the ordinary exponential error estimate, not the polynomial estimate it tests.

## 2. The imported cell mode, including regularity and pressure

The verified primary input is Lin–Xu, *Metastability of Kolmogorov flows and inviscid damping of shear flows*, https://arxiv.org/html/1707.00278 , §4, Proposition 4.1. For sin z, K2=1 and A0=−Delta−1. On a torus of periods (2pi/alpha,2pi), alpha=2/3, the negative non-shear directions are exactly horizontal sectors ±1 with zero normal Fourier index. Its unstable-eigenvalue count therefore gives an unstable Euler eigenmode in those sectors. Other horizontal sectors have positive energy form and no unstable eigenvalue. The alpha>=1 damping theorem is not used.

Fix one mode and write its smooth complex velocity and pressure as v(X,Z), Pi(X,Z), with horizontal dependence exp(i alpha X), independent of the third coordinate. There is a fixed rho with a=Re rho>0 such that, with U_c=sin Z e1,

    rho v+(U_c.grad)v+(v.grad)U_c+grad Pi=0,
    div v=0,
    v=curl(Psi e2).                                      (2)

The nonzero horizontal frequency supplies a periodic streamfunction. Its Rayleigh ODE has coefficient rho+i alpha sin Z bounded away from zero because a>0. Starting from its L2 vorticity eigenfunction, streamfunction inversion and that ODE bootstrap to every fixed derivative order. Pressure follows either from (2) or its periodic Poisson equation; it is smooth with the same horizontal sector. Thus the finite suprema used below are finite fixed constants. Normalize the periodic mean of |v|^2 to 2; the real part then has mean-square 1 for every complex phase.

Changing the sign of the shear is a reflection/phase change, not a change in this existence claim. No numerical eigenvalue or simplicity assumption is needed.

## 3. Local coordinates that remove the macroscopic drift exactly

Let Y(t)=X_V(t,x0) be the REFERENCE Euler trajectory. It is allowed to use this trajectory: the trial field is checked by its full PDE residual, rather than asserted to follow the actual NS particle. Set s=t−t0 and

    A(t)=grad V(Y(t)), F'=A F, F(t0)=I.

The fixed smooth V gives ||F||+||F^−1||<=C, ||F−I||<=Cs, and det F=1. Let b_c(t)=b(t,Y(t)) and N(t)=grad S(t,Y(t)) be the first-stage principal amplitude and phase covector. Choose an oriented orthogonal Q with

    Q e1=−b_c(t0)/|b_c(t0)|,
    Q e3=N(t0)/|N(t0)|,

and put M=FQ. Define

    y=Y(t)+M(t)z,
    H=h/|N(t0)|, a0=|b_c(t0)|, lambda0=a0/H.

There are fixed c0,C0>0 with H comparable to h and c0 lambda<=lambda0<=C0 lambda. The center lies at phase pi/2 in the first-stage construction, and M^T N(t)=|N(t0)|e3 exactly: differentiate F^T N using N'=−A^T N.

The affine drift is

    V_aff(t,y)=V(Y(t))+A(t)(y−Y(t)).

The derivative at fixed z of the coordinate map equals V_aff exactly. Define the locally used comparison field

    q0(t,y)=V_aff(t,y)+M(t)U0(z),
    U0(z)=a0 sin(z3/H)e1.                               (3)

This q0 is merely a local comparison formula. It is not asserted to be a periodic finite-energy NS solution. All trial fields and their pressures vanish before the moving chart boundary.

## 4. Quantitative actual-q coefficient comparison on the whole patch

The existing first-stage estimates, up to fixed order two on the principal phase/amplitude and the stated C1/velocity error, imply on |z|<=r:

    ||q−q0||infinity/H+||grad(q−q0)||infinity
                        <=C lambda s+h^gamma,            (4)

for any sufficiently conservative fixed gamma, for example gamma=1/64, and all sufficiently small h. Here is the complete source of that estimate.

The primary field is b cos(phi)−h d_b sin(phi), phi=S/h+pi/2. Taylor expansion about Y gives

    phi(t,Y+Mz)=pi/2+z3/H+E_phi,
    |E_phi|<=C r^2/h poly(lambda),
    |grad_y S(t,Y+Mz)−N(t)|<=C r poly(lambda).

The phase derivatives have these bounds because S is transported by the fixed smooth V on the log-log interval; fixed-order flow derivatives contribute only fixed powers of lambda. The affine chart stays within the transported first-stage phase patch: the inverse V-flow Lipschitz factor is only poly(lambda), and r poly(lambda)=o(delta).

The central amplitude solves its exact polarization ODE with bounded coefficients. Both b_c' and (F b_c(t0))' are bounded by C a0 on this short interval, so

    |b_c(t)−F(t)b_c(t0)|<=C a0 s.

The global envelope estimates give

    |b(t,Y+Mz)−b_c(t)|<=C h(r/delta)poly(lambda),
    |grad b|<=C h/delta poly(lambda).

Consequently the primary velocity difference divided by H and its gradient difference are bounded by

    C lambda s
      +C[(r/delta)+lambda r^2/h+lambda r+h/delta]poly(lambda).
                                                               (5)

The leading sin/cos gradient uses b tensor grad S/h; all its amplitude, phase and covector errors are explicitly in (5). The slow grad b term is also included. The sign in Qe1 makes −b_c sin(z3/H) agree with M U0 up to the central difference above.

The smooth background Taylor remainder contributes C(r^2/H+r). The actual NS background minus V contributes O(h^4 poly(lambda)) in W1,infinity, hence O(h^3 poly(lambda)) after division by H. The primary curl term, first-stage mean and harmonic corrections have velocity at most h^(3/2)poly(lambda) and gradient at most h^(1/2)poly(lambda); after division by H their velocity still tends to zero. Finally the true first-stage error has

    ||q−U_app||infinity/H<=h^(1/8−o(1)),
    ||grad(q−U_app)||infinity<=h^(1/24−o(1)).

All non-time powers listed are positive: r/delta=h^(1/4), r^2/h=h^(1/2), h/delta=h^(1/2). They dominate h^(1/64) after fixed constants and poly(lambda) are absorbed, by decreasing the threshold h. This proves (4). In particular the unacceptable term r/h does not occur: V_aff has already been transported exactly.

We shall also use the established global bound

    ||grad q||infinity<=C_q lambda                        (6)

on the whole terminal interval, not just on this patch.

## 5. Exact curl localization and its Euler residual

Choose a real compact bump chi supported in the unit ball, with ||chi||2=1, and set chi_r(z)=r^(−3/2)chi(z/r). Write

    V_*(z)=v(z1/H,z3/H), Psi_*(z)=Psi(z1/H,z3/H),
    Z0=curl_z[H chi_r Psi_* e2]
      =chi_r V_*+C_r,
    C_r=H grad chi_r cross(Psi_* e2),
    Z(t,z)=exp(rho lambda0 s) Z0(z),
    P_z(t,z)=exp(rho lambda0 s) a0 chi_r Pi(z1/H,z3/H).

Here C_r is a field, not an unspecified constant. Put L0 Z=(U0.grad)Z+(Z.grad)U0. Equation (2) gives the following EXACT localized residual:

    R_z := partial_t Z+L0 Z+grad_z P_z
       =exp(rho lambda0 s) {
          (U0.grad chi_r)V_*+a0 Pi_* grad chi_r
          +rho lambda0 C_r+(U0.grad)C_r+(C_r.grad)U0
        }.                                               (7)

No harmonic or cutoff pressure term has been discarded. Smoothness and bounded fixed cell derivatives give

    ||C_r||2<=C H/r,
    ||grad C_r||2<=C(1/r+H/r^2),
    ||R_z||2<=C exp(a lambda0 s) lambda H/r,
    ||Z||2<=C exp(a lambda0 s),
    ||grad_z Z||2<=C H^−1 exp(a lambda0 s),
    ||D_z^2 Z||2<=C H^−2 exp(a lambda0 s),
    ||grad_z P_z||2<=C lambda exp(a lambda0 s).            (8)

For example ||grad^j chi_r||2=C_j r^−j. These inequalities use H<r and bounded cell functions, not a count of Fourier modes. They are uniform in the expanding torus. Third derivatives of the fixed streamfunction suffice for the second derivative of Z; all are available from §2.

## 6. Exact affine pushforward, including the pressure metric

In the physical chart put

    W_app(t,y)=M(t)Z(t,z), pi_app(t,y)=P_z(t,z).

The Piola identity for a spatially constant determinant-one M gives

    M curl_z A_loc = curl_y(M^−T A_loc).

Thus W_app is exactly solenoidal and has zero periodic mean after zero extension. This remains true for a bump depending on all three coordinates. Its support stays in a fixed local torus chart, so arbitrary carrier orientation and the noninteger h frequency are permitted.

Since M'=A M, direct differentiation, without assuming q0 solves Euler, gives

    (partial_t+q0.grad)W_app+(W_app.grad)q0+grad_y pi_app
       =2A W_app+M R_z+(M^−T−M)grad_z P_z.               (9)

The factor 2A is intentional: one A comes from differentiating M, the other from (W_app.grad)V_aff. The two shear transport terms are precisely M L0 Z. The last term is the exact difference between the pushed model pressure gradient and a physical scalar gradient. At s=0 it vanishes because Q is orthogonal; ||M^−T−M||<=Cs afterwards.

Let d=q−q0 on the support. The full actual-q viscous residual is therefore exactly

    R_app=2A W_app+M R_z+(M^−T−M)grad_z P_z
             +(d.grad)W_app+(W_app.grad)d−epsilon Delta_y W_app.
                                                               (10)

The first three terms are (9); the next two change the comparison drift to the actual q. The physical Laplacian is M times the constant-in-space metric Laplacian in z with metric M^−1 M^−T. Its norm is bounded by the second-derivative estimate in (8). All formulas hold before applying the global Leray projector.

Combining (4), (8), and ||A||<=C yields

    ||R_app(t)||2
      <=C exp(a lambda0 s)
           [1+lambda s+lambda H/r+epsilon/H^2+h^gamma]
      <=C exp(a lambda0 s)[1+lambda s+h^gamma].           (11)

In the last line, decrease gamma to 1/64 if needed; lambda H/r=O(lambda h^(1/4)) and epsilon/H^2=O_nu(h^2). This is the requested estimate (R), now following from the exact identity (10).

The nonlocal pressure of the true equation has not been assumed compactly supported. Applying the exact global periodic Leray projection to (10) removes grad pi_app and does not increase the L2 norm. The projected residual can have nonlocal tails, which are covered by that global contraction and the global energy inequality below. No invariant Fourier support or compact support of the error is presumed.

## 7. Real mass and normalization on the expanding torus

For every phase theta, the cell function |Re(e^(i theta)v)|^2 has mean 1, because v has the single nonzero horizontal sector alpha and its conjugate pairs to form the real field. The zero-mean remainder admits a smooth periodic vector primitive of uniformly bounded norm (solve the fixed cell divergence equation, or integrate its Fourier series). Consequently integration by parts gives

    integral chi_r(z)^2 |Re(e^(i theta)V_*(z))|^2 dz
                       =1+O(H/r),                       (12)

uniformly in theta. The derivative bound used here is ||grad(chi_r^2)||1=O(1/r). The primitive is independent of the unused third cell coordinate, so multiplication by the full three-dimensional bump causes no volume loss.

Since det M=1 and its singular values are 1+O(s), (12) and ||C_r||2<=C H/r imply

    c exp(a lambda0 s)<=||Re W_app(t)||2
                         <=C exp(a lambda0 s).           (13)

In particular m_h=||Re W_app(t0)||2 is bounded above and below and tends to 1 with the chosen cell normalization. Set f_h=Re W_app(t0)/m_h. It is real, smooth, mean-zero, solenoidal, unit-L2 and localized in a radius-r chart about Y(t0). Temporal rotation of a complex eigenvalue does not destroy its real lower bound; (12) is uniform in that phase.

## 8. Exact linearized evolution and error closure

For each fixed h, q is already smooth on this interval. The linear equation (1) with smooth solenoidal datum has a unique smooth solution there, by the ordinary linear energy/Galerkin argument with its prescribed smooth coefficients. This requires no continuation claim for a second nonlinear solution.

First use unnormalized initial datum Re W_app(t0), and let E=w−Re W_app, initially zero. The full energy cancellation gives

    d||E||2/dt <= ||S(q)||infinity ||E||2+||Re R_app||2.

Use (6), (11), and c0 lambda<=lambda0<=C0 lambda. Choose a fixed

    C_* > max(C_q,a C0)+1,
    0<kappa<1/[4 C_*].

Duhamel gives

    sup_[t0,T_h] ||E(t)||2
      <=C tau(1+lambda tau+h^gamma) exp(C_*lambda tau)
      <=C lambda^(−3/4) log^2(lambda)=o(1).              (14)

One may harmlessly enlarge the constant for lambda>2. The initial normalization m_h merely divides all terms by a uniformly positive number. Equations (13)–(14) yield

    ||w(T_h)||2 >= c lambda^(a c0 kappa)−o(1),           (15)

which proves (1) with any fixed 0<d<=a c0 kappa after reducing c. Crucially, (14) is an ABSOLUTE error bound, so it does not conceal an assumption about favorable relative error propagation.

## 9. Optional radial high-pass statement at the correct cell scale

For the complex trial field, define L(t)=M(t)e1. Since every cell factor in its potential has horizontal sector alpha,

    ||(-i H L(t).grad_y−alpha)W_app||2
                   <=C exp(a lambda0 s) H/r.             (16)

The only failure of exact eigenfunction behavior is the horizontal derivative of chi_r and its curl correction. Bounds follow from the same cutoff derivatives as (8). For small h, ||L||<=2. On every actual torus Fourier mode with |k|<=alpha/(4H),

    |H L.k−alpha|>=alpha/2.

Parseval and (16) therefore bound the complex low-pass norm by C exp(a lambda0 s)H/r, independently of torus volume. The radial projector commutes with taking real parts, so its real low-pass norm is no larger. At t0 the normalized seed has high-pass norm 1−o(1). At T_h, this low-pass error and (14) are negligible, yielding the lower bound (15) also for P_{|D|>alpha/(4H)}w(T_h).

This cutoff is comparable to 1/h. It is not the finer h^(−3/2) cutoff and may be below the old 1/h threshold by a fixed factor. No unproved finer-frequency conclusion should be attached to it.

## 10. Consequence and its exact boundary

At the independently reviewed written scope, (15) disproves a scale-uniform bound

    ||S_q(t,s)||_{L2_sigma -> L2_sigma}
                <=C_m[1+integral_s^t ||grad q||infinity]^m

for this family, for ANY fixed finite m and C_m independent of h: on the selected interval the right side is O((log lambda)^m), while the left side is at least c lambda^d. The same applies to a bound polynomial in lambda(t−s). It does not contradict the earlier exact AFFINE Kelvin bound, since this packet spans many sinusoidal cells and retains the pressure coupling absent from affine shear.

This supplies a cell-scale late-seed linear amplifier and an arbitrary-error polynomial-budget obstruction. It gives no nonlinear amplification of this second seed, no compatibility with the original datum at time zero, no depth-uniform iteration, and no finite-time singularity. The profile threshold and all sufficiently-small-h statements remain existential. A fixed physical viscosity is preserved by rescaling, but the background initial data still vary with h.

## 11. Verification scope

This document supplies exact differentiations, a finite source-estimate ledger, normalization, and the error inequality. No numerical computation was used to infer its eigenvalue or growth. The imported instability theorem was verified in the preceding source audit; the remaining steps above are direct calculations for review. In particular (9) records both the doubled affine-gradient term and the nonorthogonal pressure-metric mismatch, the two terms most easily lost by treating a moving frame as a rigid rotation.

A separate exact SymPy substitution checked all components of (9) and the Piola curl identity with a nonorthogonal determinant-one shear M=I+t e1 tensor e3, a time-dependent polynomial vector potential, and nonconstant pressure. Every remainder simplified to zero. The independent reviewer also derived the identity directly, without relying on this symbolic fixture. This is a sign/transformation control, not an independent proof of the uniform PDE estimates or imported eigenvalue.


---

## Historical source audit and proposal — superseded by the proof above

The pending-review sentences below describe the earlier draft, not current standing.

# Kolmogorov instability and the actual outgoing-wave localization budget

**Research appendix — 8 September 2026.** **Review status:** the source audit below reports an inviscid unstable periodic shear mode. The proposed full actual-q residual (R), transported coefficient estimates, pressure-metric and curl terms, and real normalization are explicitly **UNDER REVIEW**. Consequently the proposed actual-q realization and any resulting polynomial-propagator obstruction remain unproved. This appendix does not promote a theorem for q.

All four appended derivations remain outside the registered proof graph; full formalization and ROOT / `(E′)` remain open. See the [next-transfer review index](../navier-stokes/next-transfer-review.md) for the common scope and remaining estimates.

The original derivation follows, with local references relocated. Its original drafting-status sentences are retained as historical text. Source artifact: `nse-kolmogorov-outgoing-audit-20260908.md`; SHA-256 `bb71bf9228e6bf60010ed2d47b8df4de83e115f660d0d899d6095e80581b74be`.

---

8 September 2026. Bounded independent audit. **Imported inviscid model instability verified. Proposed actual-q realization below is UNDER REVIEW, not a promoted theorem.** No repository changes, DNS, numerical eigenvalue inference, or publication. ROOT OPEN.

## 1. A primary inviscid statement with the needed aspect ratio

Lin–Xu, *Metastability of Kolmogorov flows and inviscid damping of shear flows*, arXiv:1707.00278v1, §4, Proposition 4.1, gives the unstable-eigenvalue count for class K+ shears through the negative index of A0=−Delta−K2. Their torus has x-period 2pi/alpha and y-period 2pi. For U=sin y, K2=−U''/U=1, hence A0=−Delta−1. On non-shear Fourier modes its eigenvalues are (m alpha)^2+n^2−1. Fix alpha=2/3: precisely the two modes (m,n)=(±1,0) are negative. Proposition 4.1 therefore supplies unstable Euler eigenvalues. Translation invariance places them in the horizontal sectors ±alpha. This is full inviscid linearized Euler, not the pressure-free passive transport approximation.

Source: https://arxiv.org/html/1707.00278 , equations (4.3)–(4.7), Proposition 4.1. Its main damping theorem assumes alpha>=1 and does not apply to this elongated cell. Proposition 4.2's online wording displays alpha>alpha_max; the argument here uses Proposition 4.1, avoiding reliance on that apparent typo.

The unstable mode has some fixed spectral value rho with Re rho>0; no numerical value is asserted. Its Rayleigh ODE has no real critical-layer pole, so a smooth sinusoidal coefficient gives a smooth periodic eigenfunction. Its velocity/pressure representation follows from the exact incompressible eigen-equation and the nonzero horizontal frequency. A real mode is obtained from the conjugate horizontal sectors. It can be normalized in velocity L2.

For comparison, Worthington–Dullin–Marangell, https://arxiv.org/html/1505.01667v4 , Theorem 3.5 and Lemma 3.6 provide a separate inviscid periodic-mode route with a positive real eigenvalue and an l2 eigenvector under their lattice conditions. No finite truncation alone is used here. Vasudevan's viscous steady-flow result and the alpha<<nu long-wave regime mentioned in the task are unnecessary for the fixed-alpha inviscid input; neither is silently imported as an unforced viscous theorem.

## 2. What this says about the shear model

For U=lambda h sin(z/h)e1, the cell variables X=x/h, Z=z/h, s=lambda t give the fixed unit-amplitude inviscid operator. Its growing mode has rate (Re rho)lambda. The horizontal wavelength is 2pi h/alpha and the normal-period scale is 2pi h. This is a mode on the FIRST wave's cell scale, not the finer wavelength h^(3/2) in the existing outgoing-wave theorem.

At Delta=lambda^(−3/4), model gain is exp(c lambda^(1/4)). This outgrows every fixed polynomial in lambda Delta. It decisively prevents extending the affine Kelvin polynomial bound to every sinusoidal shear merely because each pointwise gradient is nilpotent. The inverse-Laplacian/pressure coupling across cells is essential.

This model conclusion is inviscid. At epsilon=nu h^4, a fixed smooth cell mode has viscous residual epsilon/h^2=nu h^2. An unforced periodic sinusoidal NS background also decays by exp(−nu h^2 t); it must not be called a stationary positive-viscosity equilibrium. These residuals are small on the proposed intervals, but realizing growth on the actual localized q still requires the construction below.

## 3. Geometry and a useful localization radius

In the actual first-stage family, lambda=ell=sqrt(log(1/h)), the primary envelope width is delta1=sqrt(h), and its outgoing wave amplitude is comparable to lambda h near its selected center. Choose a mesoscopic radius

    r=h^(3/4).

Then r/h=h^(−1/4) tends to infinity (many cells), while r/delta1=h^(1/4) tends to zero. Taylor error in the transported primary phase divided by wavelength has scale r^2/h=h^(1/2), up to fixed powers of ell. Those are genuine positive powers of h and can absorb exp(C ell^(1/4)). The previous finer packet had width smaller than h; it could not contain these elongated-cell modes.

The subtle obstruction is the smooth macroscopic drift V. Freezing it at the center produces a velocity error O(r), hence a raw phase residual O(r/h)=h^(−1/4). Translating the center alone is therefore invalid. One must transport the cell lattice by V, or cancel its affine Taylor jet exactly.

## 4. Short interval that can beat a polynomial bound without a long adiabatic argument

A more manageable interval is

    tau=kappa log(lambda)/lambda,    t0=T_h−tau,

with one fixed sufficiently small kappa>0. It lies inside the existing terminal interval for sufficiently small h. A model eigenmode gains lambda^(c kappa), which already outgrows every fixed polynomial in the accumulated shear lambda tau=kappa log(lambda). Thus a short-window realization would refute the proposed polynomial-in-shear-time arbitrary-error bound without reaching exp(c lambda^(1/4)). It would still be a late-seed LINEARIZED result, not nonlinear second handover or time-zero seed compatibility.

## 5. Candidate affine-transported construction; exact residual line requiring review

Use the reference Euler trajectory Y(t)=X_V(t,x0), for t0<=t<=T_h. Let

    F'=A_V(t,Y(t))F,       F(t0)=I,
    y=Y(t)+F(t)Q0 z,

where Q0 is an oriented orthonormal frame aligned with the outgoing polarization and covector at t0. Then det F=1, F=I+O(t−t0), and this coordinate map cancels the affine drift

    V_aff(t,y)=V(Y(t))+A_V(Y(t))(y−Y(t))

exactly. The remaining V−V_aff is O(r^2), costing only r^2/h in a fast derivative. The normal phase covector obeys the exact frozen-V cotangent equation along Y, so F^T times that covector is constant; primary phase curvature remains O(r^2/h) in the transported coordinates.

Let hbar=h/|N(t0)|, comparable to h, a0=|b(t0,Y(t0))|, and lambda0=a0/hbar, comparable to lambda. Signs or a phase shift convert the leading outgoing cosine at phase pi/2 into the chosen sinusoidal cell shear. Freeze the cell eigenfunction at alpha=2/3 and growth rho lambda0. Extend it periodically on R^2, independent of the third cell direction.

Localize its STREAMFUNCTION/vector potential, not its velocity alone. Schematically, in z coordinates take

    A_loc=hbar r^(−3/2) chi(z/r) Psi(z1/hbar,z3/hbar)e2,
    w_loc=curl_z A_loc.

Then push it forward by FQ0 and multiply by exp[rho lambda0(t−t0)]. Equivalently curl the physical potential (FQ0)^(−T) A_loc. This is the exact Piola/curl transformation for determinant-one matrices. It makes the trial velocity exactly solenoidal and mean-zero after smooth zero extension on the expanding torus. The correction is relatively O(h/r). Localization may include the third coordinate without losing incompressibility.

The model pressure is localized with the same bump. Its cutoff gradient costs lambda h/r. Its pushed gradient is (FQ0)^(−T) grad_z pi, whereas the transformed model equation contains (FQ0) grad_z pi. Since F−I=O(t−t0), this metric mismatch costs O(lambda(t−t0)) in relative L2. The extra F' velocity and background-gradient terms cost O(1). They must be included; affine transport does not make those terms vanish.

The intended residual ledger for the full pressure-retaining linearization around ACTUAL q is

    ||R_app(t)||_2
      <= C exp[(Re rho)lambda0(t−t0)]
              [1+lambda(t−t0)+h^gamma],                 (R)

for some fixed gamma>0, for example a conservative gamma<1/24, after absorbing fixed powers of ell into positive h powers. Sources of the h term include:

- envelope and curl/pressure cutoffs: lambda h/r;
- primary envelope variation: lambda(r/delta1) times fixed powers of ell;
- phase curvature: lambda r^2/h times fixed powers of ell;
- V Taylor remainder: r^2/h;
- actual first-stage error: ||q−U_app||infinity/h <=h^(1/8−o(1)), and its gradient <=h^(1/24−o(1));
- mean/harmonic corrections and epsilon Delta of the localized eigenmode.

The frozen central amplitude/direction and the coordinate pressure metric contribute the displayed lambda(t−t0) term. Their derivatives along the fixed Euler profile are bounded relative to their sizes over this short interval. The pointwise compact-profile estimates must be applied on the transported radius-r patch, not only at its center. The retained reference-flow drift avoids the otherwise fatal r/h term.

The global exact Leray projection is an L2 contraction. Therefore an unprojected residual identity with the displayed local pressure, if (R) is proved, controls all nonlocal tails without assuming compact support of the true pressure or error.

## 6. Conditional closure from (R), and what is actually achieved

The existing outgoing-wave note gives ||grad q||infinity<=C_q lambda on the terminal interval. If (R) and the normalization below hold, Duhamel energy for the EXACT homogeneous viscous linearization gives

    ||w(T_h)−w_app(T_h)||_2
       <=C tau(1+lambda tau+h^gamma) exp(C_*lambda tau),

for fixed C_* dominating the energy and model growth constants. Taking kappa<1/(4C_*) makes this O(lambda^(−3/4)log^2(lambda))=o(1), while the model norm grows at least lambda^(c kappa). This is an absolute error bound; no hypothetical polynomial propagator is used to establish it.

Normalization is not supplied by evaluating one particle: under the determinant-one affine map, integration of the real cell eigenmode over the radius-r bump must give its nonzero cell-average velocity mass plus O(h/r). The nonzero horizontal sector allows periodic integration by parts, uniformly in the complex temporal phase. The curl correction has relative size O(h/r). Normalize by the actual initial L2 mass; it stays bounded above and below. This supplies a real unit solenoidal late-time datum if the estimates are completed. A high-pass conclusion would additionally need a cutoff below the mode's fixed horizontal frequency alpha/hbar; it is NOT automatically the earlier 1/h or 1/h^(3/2) threshold.

**Achieved:** a verified primary inviscid unstable cell, matching many-cell spatial scales, an explicit drift-canceling localization candidate, and a favorable short-window conditional error budget. **Not yet promoted:** the assembled exact residual bound (R), its full transported coefficient estimates and real normalization, and consequently actual-q exponential/polynomial-obstruction claims. The main remaining review line is (R), especially the pressure metric mismatch and the localized curl commutators. There is no conceptual license to omit those because their anticipated scales are favorable.

The longer Delta=ell^(−3/4) construction remains harder: frozen central/frame changes give only powers of ell, which a crude exp(C ell^(1/4)) energy factor cannot absorb. An adiabatic unstable-cell construction or a stronger error propagator would be needed there. The shorter tau avoids that issue and is the precise next bounded proof target if pursued.
