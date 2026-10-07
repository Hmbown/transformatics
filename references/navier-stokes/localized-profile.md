# Localized heat-rounded phase profiles in the actual NS background

Independent bounded derivation, 8 September 2026. This is a reviewed finite-packet extension of the written original-time handover argument. The coordinating agent and a separate reviewing agent checked the complete identities, estimate assembly and endpoint region. This is AI-agent review, not external expert acceptance. It is not a formal certificate, an infinite cascade, or a solution of ROOT or `(E')`. No DNS is used.

The useful conclusion is that one general periodic-profile corrector replaces the old first/second-harmonic pair. A spatially constant central heat clock is enough for this finite extension and is preferable: its diffusion mismatch has L2 order h^(37/8), below the h^(31/8) comparison budget. The complete material-clock formula, including its additional curl term, is also given.

## 1. Inputs and conventions

All spatial derivatives of a profile in this note hold its independent phase variable s fixed. The phase variable has period 2pi. Spatial integration uses unnormalized Lebesgue measure on the expanding torus of side 2pi L. Constants may depend on the one fixed unscaled Gavrilov profile, the bump, the fixed phase profile, the finitely many derivative orders and fixed viscosity nu, but not on h or L.

Use the actual smooth first-stage NS solution q from [the original-time finite handover](original-nonlinear-handover.md), and exactly its prepared receiving phase S and real amplitude b. Thus

    h=L^(-1/10), epsilon=nu h^4, ell=sqrt(log(1/h)),
    k=h^(3/2), d=h^(5/4), t_f=(2/mu)log ell-ell^(-3/4),
    D=partial_t+q.grad_x, A=grad q, xi=grad S,
    D S=0, D xi=-A^T xi,
    D b=G b, G=-A+2xi tensor (xi^T A)/|xi|^2,
    xi.b=0.                                                     (1)

The phase exists on one slightly larger transported chart. The amplitude and its vector potential vanish smoothly before that chart's boundary. The central covector xi_c is the value on the prescribed base-q particle. This is the independently known q, not the final solution with both packets.

The existing proof supplies, after enlarging E_h=exp(C ell) finitely many times,

    |xi|+|xi|^(-1)<=E_h,
    |D_x^r xi|<=h^(-r)E_h,
    ||D_x^r b||_infinity<=k d^(-r)E_h,
    ||D_x^r b||_2<=k d^(3/2-r)E_h, r<=18,
    |xi-xi_c|<= (d/h)E_h on the support,
    volume(support)<=C d^3, diameter(support)<=d E_h=o(h),
    ||D_x^r q||_infinity<=C_r m_h(t)h^(1-r), 1<=r<=24,
    m_h(t)=1+ell^(-1)exp(mu t), integral m_h<=C ell.             (2)

The sharper history and initial estimates are essential:

    sup_t,support |b||xi|/k <=C ell^(11/8),
    integral_0^t_f sup_support |b||xi|/k dt<=C ell^(11/8),
    sup_support |b(0)||xi(0)|/k<=C ell^(-5/8).                  (3)

These are whole-support estimates proved in sections 3--5 of that note, not assumptions inferred from a central value. No exponential of the generic quantity E_h may replace (3) in the final error energy inequality.

Fix a real smooth odd periodic F with F(s)=s on |s|<a for one fixed 0<a<pi. Let Q be its unique zero-phase-mean periodic primitive, Q_s=F. Write

    f_tau=exp(tau partial_s^2)F,
    Q_tau=exp(tau partial_s^2)Q.

For the same sign of the outgoing rank-one matrix as the original sine packet, use

    a(t,x,s)=-b(t,x) f_tau(t,x)(s).                            (4)

The original packet equals -b sin(S/k) to leading order. Choosing +b f_tau instead would preserve an absolute strain estimate but reverse that outgoing rank-one sign. Every formula below is linear in a where appropriate, so one can use either convention consistently. In formulas which display b and C explicitly, a=b f_tau is used for readability; applying them to (4) means replacing b and C by their negatives. The quadratic mean is unchanged by this simultaneous sign change.

Unlike a cosine, F has infinitely many Fourier modes in general. Nothing below truncates them, treats them as only two harmonics, or gives their unproved tail a zero value.

## 2. Exact differentiated profile calculus

For any smooth profile v(t,x,s), let E[v]=v(t,x,S(t,x)/k). Then

    D E[v]=E[Dv],
    grad_physical E[v]=E[grad_x v+(xi/k)partial_s v],
    Delta_physical E[v]=E[Delta_x v+k^(-1)L1 v
                                      +|xi|^2 k^(-2)partial_s^2 v],
    L1 v=2(xi.grad_x)partial_s v+(div xi)partial_s v.           (5)

Set grad^k=grad_x+(xi/k)partial_s and use Delta^k for (5). Products and all coefficients on the right are evaluated before applying E. In particular slow derivatives differentiate tau(t,x) when it is variable.

Let

    rho=epsilon |xi|^2/k^2, kappa=D tau, omega=kappa-rho,
    Dcal_kappa=D-kappa partial_s^2.                            (6)

Two choices will be used:

* Material clock: tau(0,x)=0 and D tau=rho, so omega=0.
* Central clock: tau=tau_c(t)=epsilon k^(-2) integral_0^t |xi_c(r)|^2 dr, so kappa=rho_c(t), grad_x tau=grad_x kappa=0, and omega=rho_c-rho.

Both clocks are nonnegative. Since D b=G b and partial_tau f_tau=partial_s^2 f_tau, the primary a in (4) satisfies exactly

    Dcal_kappa a=G a.                                        (7)

## 3. Exact solenoidal lift, including grad tau

If a has zero phase mean and xi.a=0, let partial_s^(-1) denote the unique zero-phase-mean periodic primitive and define

    V_a=-(xi cross partial_s^(-1)a)/|xi|^2,
    r_a=curl_x V_a,
    W_a=a+k r_a.                                              (8)

The triple-product identity and curl xi=0 give

    k curl_physical E[V_a]=E[W_a],
    div_x r_a=0,
    xi.r_a=-div_x(partial_s^(-1)a).                            (9)

Thus E[W_a] is exactly divergence-free and has zero spatial mean after extending the compact potential smoothly by zero to the torus. The scalar phase needs no global periodic extension. Also the phase means of a, V_a, r_a and W_a all vanish.

For a=b f_tau, put

    C=-(xi cross b)/|xi|^2,
    c=curl_x C, e=(grad_x tau) cross C.

Then (8) is the explicit exact identity

    V_a=C Q_tau,
    r_a=c Q_tau+e partial_s f_tau,
    W_a=b f_tau+k c Q_tau+k e partial_s f_tau.                 (10)

The e term is necessary for the material clock; dropping it generally destroys solenoidality. For the central clock e=0 exactly. A constant added to Q changes the localized curl velocity by a multiple of k curl C. Our zero-mean primitive convention is fixed throughout. In particular the heat-generated constant tau in the affine-core approximation to Q_tau is not silently discarded inside (10).

## 4. One forced-profile pressure identity

Let H be any real, smooth, zero-phase-mean forcing profile. Solve, along the actual-q material flow and periodically in s,

    Dcal_kappa g=Gg-Pi_xi H,
    Pi_xi=I-xi tensor xi/|xi|^2,
    g(0)=0.                                                  (11)

Both xi.g=0 and the zero phase mean are preserved: differentiate xi.g using Dxi=-A^Txi, and note that xi is independent of s. Define V_g,r_g,W_g by (8). Set

    J[g,H]=(2xi.Ag+xi.H)/|xi|^2,
    p_g=-k partial_s^(-1)J[g,H].                              (12)

Then the exact forced linearized NS identity is

    (D+A-epsilon Delta^k)W_g+grad^k p_g=-H+R[g;H],             (13)

where

    R[g;H]=omega partial_s^2 W_g
       +k[(D+A-kappa partial_s^2)r_g
                                -grad_x partial_s^(-1)J[g,H]]
       -epsilon Delta_x g-(epsilon/k)L1 g
       -epsilon k Delta_x r_g-epsilon L1 r_g.                (14)

This is a profile identity, followed by E. Its proof expands Delta^k in (5). The non-slow portion of grad p_g is -xi J[g,H]. Since

    (D+A-kappa partial_s^2)g=2xi (xi.Ag)/|xi|^2-Pi_xi H,

these two leading terms sum to -H. In particular the +xi.H in (12) is required, even when H has a longitudinal component. For a Fourier mode exp(i n s), -k partial_s^(-1)=i k/n, which recovers the existing forced-harmonic pressure exactly for every nonzero integer n.

For the primary a, use H=0, (7), and

    p_a=-k partial_s^(-1)(2xi.Aa/|xi|^2).

The resulting residual is R[a;0]. For a=b f_tau this pressure is -2k(xi.Ab)|xi|^(-2)Q_tau, matching the exact affine heat-profile calculation.

There is no hidden time derivative of q or pressure in (14). For any V,

    [D,curl_x]V_i=-epsilon_ijk (partial_j q_l)partial_l V_k,
    Dcal_kappa(curl_x V)=curl_x(Dcal_kappa V)
                +[D,curl_x]V+(grad_x kappa) cross V_ss.       (15)

The symbol epsilon_ijk in (15) is the alternating tensor, not viscosity. Also, writing T_x v=-(xi cross v)/|xi|^2,

    Dcal_kappa V_g=(D T_x)partial_s^(-1)g
                            +T_x partial_s^(-1)(Gg-Pi_xi H).

D T_x uses only Dxi=-A^Txi. Thus (15) expresses every material derivative in (14) using spatial jets of q, xi, g and H. For the central clock the last commutator in (15) vanishes; for the material clock it must be retained.

## 5. Exact quadratic interaction and its full phase mean

For W_a=a+k r_a, tangency xi.a=0 gives the exact expansion

    N(a):=W_a.grad^k W_a
      =a.grad_x a+(xi.r_a)a_s
       +k[r_a.grad_x a+a.grad_x r_a+(xi.r_a)(r_a)_s]
       +k^2 r_a.grad_x r_a.                                 (16)

There is no remaining 1/k term of size |a|^2/k. The normal component xi.r_a generally does not vanish and is part of (16).

With phase average <.> over one period, the exact mean is particularly simple:

    Q0=<N(a)>=div_x <W_a tensor W_a>.                         (17)

Indeed E[W_a] is solenoidal, so its quadratic advection is the physical divergence of W_a tensor W_a. The average of the additional phase derivative in that divergence is zero. Equation (17) is a phase-average identity; it does not identify phase average with spatial average. Integrating (17) in space nevertheless gives zero, since its stress is compactly supported.

There is also a useful closed formula for odd F. Let

    M0(tau)=<f_tau^2>, MQ(tau)=<Q_tau^2>, M1(tau)=<(f_tau)_s^2>.

f_tau is odd; Q_tau and (f_tau)_s are even. Therefore the a/r cross stresses have zero average and

    <Q_tau(f_tau)_s>=-M0,
    M0'(tau)=-2M1(tau), MQ'(tau)=-2M0(tau),
    Q0=div_x{M0 b tensor b
       +k^2[MQ c tensor c-M0(c tensor e+e tensor c)
                                      +M1 e tensor e]}.     (18)

This formula includes the full profile, not only its lowest Fourier modes. For material tau, the outer divergence differentiates the three moments as functions of tau(x). For the central clock e=0 and these moments depend only on time; then

    Q0=M0 div_x(b tensor b)+k^2 MQ div_x(c tensor c).           (19)

The sign convention (4) changes neither formula.

## 6. Full one-packet approximation and exact remainder

Solve the global forced linear Euler mean about the actual q:

    Dm+A m+grad p_m=-Q0, div m=0, m(0)=0.                     (20)

Keep its pressure and its nonlocal spatial tails. Its viscosity is left in the eventual residual; no compact-support claim for m is made.

Define the known zero-phase-mean forcing

    H=R[a;0]+N(a)-Q0+(m.xi/k)a_s.                            (21)

Every summand has zero phase mean. This forcing is spatially compact in the transported chart, including the last term, even though m is not compactly supported. Apply (11)--(14) to this H, thereby defining one general profile g, with all its Fourier modes included. Set

    U_app=q+m+E[W_a+W_g],
    P_app=p_q+p_m+E[p_a+p_g].                                (22)

This gives a real, smooth, solenoidal approximation. At time zero g=m=0 exactly, so its original datum is q(0)+E[W_a(0)]. Its spatial mean equals that of q: the added wave fields are curls, and (20) preserves the mean of m because Q0 has zero integral and, for divergence-free q,m, both integral q.grad m and integral m.grad q vanish.

Writing every profile term below under E, the exact NS residual is

    R_tot=R[g;H]-epsilon Delta m+m.grad m
       +m.grad_x W_a+(m.xi)(r_a)_s+W_a.grad m
       +W_a.grad^k W_g+W_g.grad^k W_a
       +W_g.grad^k W_g
       +m.grad^k W_g+W_g.grad m.                             (23)

For the purely spatial terms, no E is needed. To verify (23), the primary linear equation supplies R[a;0], its self-interaction supplies N(a), and (20) subtracts Q0. Equation (13) subtracts their sum plus (m.xi/k)a_s. The only remaining part of m.grad^k W_a is m.grad_x W_a+(m.xi)(r_a)_s, as displayed. Thus normal mean advection is retained rather than removed through an incorrect transversality assumption.

For a and g the apparently fast leading mixed interactions vanish because both are transverse. Their normal curl corrections, all profile products, the mean/primary fast interaction in (21), and the remaining mean/g fast interaction in (23) are included. There is no assumption that a real general profile closes on two harmonics.

## 7. Clock estimates and the simpler finite construction

For the material clock, differentiated transport and (2) imply, at every fixed required order r,

    ||D_x^r tau||_infinity<= (epsilon/k^2)h^(-r)E_h,
    d^r||D_x^r tau||_infinity
                           <=nu h(d/h)^r E_h, r>=0.          (24)

The integral over the logarithmic time interval is absorbed into E_h. These inequalities follow by a triangular derivative hierarchy with top coefficient C_r m_h, not by exponentiating a generic spatial jet bound. The right side in the second line tends to zero at every fixed r. In particular d|grad tau|=o(1), although the unweighted first derivative need not be O(h).

Consequently the extra e term in (10) fits below the usual envelope derivative: |e|<=k E_h, whereas |c|<=k d^(-1)E_h. Every further derivative of the heat profile contributes two additional phase derivatives but no inverse power larger than the available d^(-1) envelope weight. The term k(grad kappa) cross (V_a)_ss from (15) has L2 size at most

    (epsilon/h)d^(3/2)E_h=nu h^(39/8)E_h.                   (25)

It is below the main residual budget. For fixed smooth F one can therefore keep a finite hierarchy of extra phase derivatives and control this material-clock construction as well. Section 8 states the hierarchy explicitly.

For the recommended central clock, all spatial clock derivatives vanish. The central covector bound from the existing matching calculation gives

    0<=tau_c(t)<=C_nu h ell^2 log ell=o(1).                   (26)

The coarse bound nu h E_h=o(1) alone would also suffice for small heat time. Whole-support comparison in (2) gives

    |omega|=|rho_c-rho|
           <=(epsilon/k^2)(d/h)E_h.                         (27)

The primary diffusion mismatch, which is the first term of (14), therefore has L2 size

    ||omega (W_a)_ss||_2
       <=(epsilon/k^2)(d/h)k d^(3/2)E_h
       =epsilon k^(-1)d^(5/2)h^(-1)E_h
       =nu h^(37/8)E_h.                                   (28)

The same term for g is smaller:

    ||omega (W_g)_ss||_2
       <=(epsilon/k^2)(d/h)k^2 d^(1/2)E_h
       =nu h^(39/8)E_h.                                   (29)

Spatial derivatives of omega do not need to retain the extra factor d/h in order to estimate the forcing hierarchy: d^r|D_x^r omega|<=nu h E_h for all fixed r>=1, and actually have the stronger factor (d/h)^r. The zeroth-order improvement (28) is enough for the residual estimate.

Thus using a central clock for one packet is not an uncontrolled replacement of the material heat equation. Its omitted spatial variation is an explicit smaller residual, and it avoids every grad tau and grad kappa term in the implemented approximation.

## 8. Full Fourier control, support, and derivative orders

For a scalar or vector phase profile v write

    ||v||_{A_M}=sum_n (1+|n|)^M |v_hat(n)|.

The norm is an algebra up to a constant depending only on M. Heat evolution is a contraction for tau>=0. The zero-mean primitive is bounded on this space because every retained integer frequency satisfies |n|>=1; there is no shrinking spatial-frequency divisor in this operation.

Along a q material label, (11) gives for every nonzero integer n

    d g_hat(n)/dt=(G-kappa n^2)g_hat(n)-Pi_xi H_hat(n).

The scalar dissipative factor commutes with the matrix transport. If P_G(t,s) is its matrix propagator, the exact variation-of-constants formula is

    g_hat(n,t)=-integral_0^t exp(-n^2 integral_s^t kappa)
                          P_G(t,s) Pi_xi(s)H_hat(n,s) ds,
    ||P_G(t,s)||<=exp(3 integral_s^t |A|).                   (30)

This is a forward construction from zero original data. Reality is preserved by the Fourier conjugacy relation. The phase heat operator does not propagate support in x; forcing and amplitudes remain in the transported chart. This is different from the global tails of m.

For the central clock, differentiating the profile transport in space creates no n^2 partial_x kappa commutators. For the material clock, use a triangular mixed hierarchy: when spatial derivatives of total order j are estimated, assign them phase weight M+2(r-j), for a fixed maximum spatial order r. A commutator with a spatial derivative of kappa times two phase derivatives of a lower spatial derivative fits within this hierarchy. Weighted coefficients satisfy (24), so the lower-order terms enlarge E_h finitely many times rather than put E_h into an exponential. The diagonal term -kappa n^2 remains nonpositive.

A sufficient nonminimal order budget is the already available q C24 and primary b,xi C18, mean H16, and g through spatial order 13. The primary residual contains at most three slow derivatives of a, so its source derivatives through order 13 use at most 16 primary slow derivatives. The full phase-mean source through order 16 uses at most 18 primary slow derivatives. Fixed phase regularity is an independent budget: take F smooth with its Fourier A_80 norm finite and include the finitely many such profile constants in C. This comfortably covers both the central clock and the material clock's two-extra-phase-derivatives-per-slow-derivative hierarchy; no limiting analyticity or uniform-in-profile theorem is asserted. One can instead assume F is C-infinity and specify all finite norms appearing in (5)--(30), without seeking a minimal integer.

The source bounds from (14),(16),(18),(21) give, through the orders needed here,

    ||D_x^r Q0||_2<=k^2 d^(1/2-r)E_h,
    ||D_x^r m||_2+||D_x^r g||_{L2_x A_M}
                              <=k^2 d^(1/2-r)E_h,
    ||D_x^r m||_infinity+||D_x^r g||_{Linfty_x A_M}
                              <=k^2 d^(-1-r)E_h.           (31)

For m use the differentiated solenoidal energy identities in (20), including its pressure. The coefficients d^(j-1)||D^j q||_infinity are bounded by C_j m_h(d/h)^(j-1); their time integral is O(ell). Global L2-to-Linfinity Sobolev interpolation yields the pointwise estimate without asserting Linfinity boundedness of the Leray projector. For g, (30) and its weighted spatial derivative hierarchy apply. In particular the forcing (m.xi/k)a_s is of the same principal size k^2/d, using (31) for m; it does not form a feedback loop in solving for m because m is defined first from Q0 alone.

All torus constants are uniform in L>=1: the estimates use the inhomogeneous global L2 norm and uniform Fourier splitting, not a Poincare inequality with smallest frequency 1/L. Products involving mean tails use their global L2 derivative bound times a pointwise bound; they are never assigned the compact volume d^3 without justification.

## 9. Residual powers at the existing scales

Equation (23), tangency, and (31) give the same leading L2 residual as the sine construction:

    k^3 d^(-1/2)E_h = h^(31/8)E_h.                         (32)

For clarity the point-amplitude sizes are |a|<=k E_h, |r_a|<=k/d E_h, |g|<=k^2/d E_h, |r_g|<=k^2/d^2 E_h and |m|<=k^2/d E_h. A primary/correction interaction after fast tangency cancellation is therefore k^3/d^2 pointwise on volume O(d^3), giving (32). The residual m.grad^k W_g has fast part of this same size and has not been omitted.

The complete larger categories in (23) have the following L2 orders, with E_h and fixed nu factors suppressed:

| Contribution | Order | h exponent |
| --- | --- | --- |
| Remaining linear curl, derivative of H in the pressure/lift, primary/g interactions, and mean-to-g fast advection | k^3 d^(-1/2) | 31/8 |
| Mean/g quadratic and normal-curl quadratic terms | k^4 d^(-3/2) | 33/8 |
| Central-clock primary mismatch (included in H) | epsilon k^(-1)d^(5/2)/h | 37/8 |
| Primary mixed viscous derivative (included in H) | epsilon d^(1/2) | 37/8 |
| Primary slow viscosity (included in H) | epsilon k d^(-1/2) | 39/8 |
| Corrector central-clock mismatch | epsilon d^(3/2)/h | 39/8 |
| Corrector leading mixed viscosity | epsilon k d^(-1/2) | 39/8 |
| Corrector slow viscosity, curl mixed viscosity, and global mean viscosity | epsilon k^2 d^(-3/2) | 41/8 |
| Material-clock curl commutator, when that option is used | epsilon d^(3/2)/h | 39/8 |

Some entries are source terms in H rather than surviving terms of R_tot; listing them makes the cost of replacing the profile explicit. Their slow derivative in (14) costs at most k/d in the final residual, with positive h margin. One may retain the older coarser epsilon d^(1/2) upper bound for the oscillatory viscous remainder without changing (32). The physical fast Laplacian epsilon |xi|^2 k^(-2) a_ss has already been paid by the heat clock; it is not separately counted as zero without the mismatch (28).

Time integration and the finitely many profile norms are absorbed in E_h. Hence the intended conclusion of this bookkeeping is

    integral_0^t_f ||R_tot||_2 dt <= h^(31/8)E_h.             (33)

This is not obtained by simply replacing sin by F in the old two-harmonic equation. It uses the complete corrector (11),(21), the pressure (12), and the exact mean (17).

## 10. Finite nonlinear comparison, initial normalization, and endpoint

For the central clock, heat is contractive on each derivative norm of the fixed F. From (3), the leading gradient satisfies

    integral ||(b tensor xi/k)(f_tau)_s||_infinity
                                              <=C_F ell^(11/8).

All other primary curl gradients have size at most (k/d)E_h+(k/d)^2 E_h, and the mean/g corrections have C1 size at most (k/d)E_h. Together with the q history this gives

    integral ||grad U_app||_infinity<=C_F ell^(11/8),
    ||E[W_a(0)]||C1<=C_F ell^(-5/8),
    sup ||U_app-q-E[W_a]||C1<=h^(1/4)E_h=o(1).              (34)

The initial datum is a direct real curl with the fixed signed profile (4). No choice of a tiny real quadrature, no division by an unproved lower L2 norm, and no Fourier-band normalization is used. The amplitude b is precisely the previously prepared original-time amplitude. In the material-clock option the additional terms from (24) also fit below the errors in (34).

Start actual unforced NS Q with datum U_app(0). On its strong lifetime the exact relative-energy inequality gives, for e=Q-U_app,

    d||e||_2/dt<=||S(U_app)||_infinity||e||_2+||R_tot||_2.

With G_h=ell^K exp(C_F ell^(11/8))=h^(-o(1)), (33),(34) give

    sup ||e||_2<=h^(31/8)G_h.                               (35)

This energy estimate by itself does not prove strong lifetime. Separately bootstrap ||grad e||_infinity<=1 and use the standard integer H12 NS energy inequality. The phase Fourier bounds above and k<d give

    ||Q(0)||H12+sup ||U_app||H12<=h^(-117/8)E_h.

Under the bootstrap the integrated H12 growth coefficient is O(ell^(11/8)), so

    ||Q||H12+||U_app||H12<=h^(-117/8)G_h,
    ||grad e||_infinity<=C||e||_2^(19/24)||e||H12^(5/24)
                                                       +C||e||_2
                            <=h^(1/48)G_h.                 (36)

The exponent is (31/8)(19/24)-(117/8)(5/24)=1/48>0. The velocity exponent is 25/16. Uniform expanding-torus constants and the finite H12 continuation alternative close this separate bootstrap through t_f for sufficiently small h. This is the same comparison argument as the canonical sine result, now dependent on the complete profile residual proved above; a weak relative-energy statement alone is not being promoted to smoothness.

At the final base-q particle the terminal phase is affine and b is constant in a neighborhood, while the central clock is spatially constant. Thus r_a and every local derivative of it vanish there. Since S=0,

    grad E[W_a](t_f,Y_q(t_f))
                    =-b_*(Y_q(t_f)) tensor xi*/k
                                      times (f_tau_c)_s(0). (37)

The heat-rounded core estimate in [the affine note](../analysis/viscous-flat-core.md) gives (f_tau_c)_s(0)=1+O_F(tau_c exp(-a^2/(16tau_c))). Together with (26), (34),(36), this preserves the final added strain lower bound c_F ell^(11/8). The sign in (37) agrees with the original outgoing rank-one matrix. This is an evaluation at the reference base-q particle, not a claim about an actual-Q material trajectory.

There is a stronger spatial endpoint conclusion that uses the flat core. Fix c_0>0 with 4c_0<a/2. Since k/d tends to zero, the ball |y-Y_q(t_f)|<=c_0 k is contained in the terminal bump plateau for all sufficiently small h. There b and xi are constant, r_a vanishes identically, and |S/k|<=4c_0<a/2. Thus the heat estimate is uniform throughout that ball. Define the actual endpoint matrix

    A_*=grad q(t_f,Y_q(t_f))-ell^(7/8)c_h tensor xi*.

The base gradient variation is at most

    C k ||D_x^2 q(t_f)||_infinity<=h^(1/2)E_h.

The mean/profile correctors contribute h^(1/4)E_h, and the nonlinear error contributes h^(1/48)G_h. The heat-rounding gradient error is exponentially smaller than every fixed power of h because tau_c<=C_nu h ell^2 log ell. Consequently the finite solution constructed above obeys

    sup_|y-Y_q(t_f)|<=c_0 k |grad Q(t_f,y)-A_*|
                              <=h^(1/48-o(1)).              (38)

Equivalently its velocity after subtracting its actual center value differs from A_*(y-Y_q(t_f)) by at most C k h^(1/48-o(1)) on this ball, by integrating the gradient bound on line segments. This is a finite-energy almost-affine interior at one endpoint. It is not exact affine NS on a patch, does not identify A_* with the infinite-energy model matrix, and supplies no persistence of that interior or descendant trajectory over a further time interval.

## 11. Exact boundary and next calculation

The algebra identifies a concrete finite extension, with a complete general-profile pressure and corrector, and the existing h,k,d power margin survives. It does not make the localized solution exactly affine: q, the mean and corrector tails, and the nonlinear tracking error remain. To claim a usable affine core for a descendant one must additionally bound the relevant spatial and time jets of their sum on that descendant's complete transported support. A pointwise final C1 estimate does not supply that stronger statement.

The [full-support seed-cost proof](../analysis/flat-profile-seed-cost.md) now shows that a fixed flat profile retains the C3 cost: another phase inside the actual plateau has a nonzero third derivative, while confining the whole packet to the flat slab moves the cost into its cutoff. This is a restricted kinematic obstruction. This calculation supplies neither one smooth datum for infinitely many stages nor a uniform infinite-order seed budget. It supplies no unsupplied finer carrier: the receiving component still starts at scale k/ell and ends near k, both below the original h scale.

The independent review rederived (13)--(18), including a variable clock and nontransverse forcing, and checked every term of (23) against the corrected table. The next estimate must establish a usable time-dependent outgoing state and genuinely new seed production, subject to the bounds in the [next-seed analysis](next-seed-analysis.md). The construction deliberately avoids a new flow simulation, frequency truncation, and a claim that the old two-harmonic instrument certifies this new full-profile PDE estimate.

References are to already reviewed repository calculations and their classical energy/heat calculus. No claim of novelty or priority is made. The canonical inputs are linked above.


## Review provenance

[Independent review record](../analysis/profile-extension-review.md). Original reviewed source `nse-localized-profile-calculus-20260908.md`, SHA-256 `77e66606f3c5d8bf47ec42d474e1febead5657120b6bb5c7793e2b02124c5417`. Archival changes resolve links and current-scope wording; they do not replace a formal PDE certificate.
