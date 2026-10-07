# A second supplied wave, present at original time zero, produces a finite smooth strain handover

8 September 2026. **PROVED at the restricted written-analytic scope below.**
The complete assembly and its technical inputs passed separate AI-agent
mathematical reviews, including full pressure and strong continuation.
This is not external expert acceptance or a formal PDE certificate.
ROOT and `(E′)` remain OPEN. No infinite cascade, novelty or new DNS claim.

## 1. The theorem and its quantifiers

Choose the **unscaled** compact geometric Gavrilov field V=V_j from
[the oblique-carrier theorem](gavrilov-oblique.md),
with f_j(P_j)=1, and fix one sufficiently large j. Use its selected real
expanding oblique carrier, with positive exponent mu. This choice is made
once, before h tends to zero. An older j-dependent L2 normalization is
not imposed. Fix physical viscosity nu>0.

For integers L sufficiently large, with threshold depending on this fixed
profile, nu, the fixed bump, and the fixed derivative orders below, set

    h=L^(-1/10), epsilon=nu h^4, ell=sqrt(log(1/h)),
    T=(2/mu)log ell, t_f=T-ell^(-3/4),
    delta_1=h^(1/2), k=h^(3/2), d=h^(5/4).             (1)

Work on the expanding torus (R/(2pi L)Z)^3 with unnormalized Lebesgue
L2 and inhomogeneous Sobolev norms. Let q_h be the first-stage exact
unforced NS solution from
[the log-log theorem](loglog-handover.md):

    q_h(0)=V+Z_{1,h}(0),
    ||Z_{1,h}(0)||C1<=C/ell.

It is smooth through T. There exists a real, smooth, mean-zero,
divergence-free curl packet Z_{2,h}(0), prescribed entirely at time zero,
such that the unforced NS solution Q_h of viscosity epsilon with

    Q_h(0)=V+Z_{1,h}(0)+Z_{2,h}(0)                    (2)

is smooth through t_f and satisfies

    ||Z_{2,h}(0)||C1<=C ell^(-5/8),                   (3)
    integral_0^t_f ||grad Q_h(t)||_infinity dt
                                  <=C ell^(11/8).     (4)

Let Y_h be the particle of the **base solution q_h** starting at the
first packet's center. At its location at t_f,

    |S(Q_h-q_h)(t_f,Y_h(t_f))|_F>=c ell^(11/8).        (5)

Here S(w)=(grad w+grad w^T)/2. The base gradient at that time is at most
C ell, so the total strain of Q_h there is also at least a fixed
positive multiple of ell^(11/8) for sufficiently large L. The observation
point is not asserted to be a particle of Q_h.

The explicit corrected approximation U_h in section 6 has

    sup_[0,t_f] ||Q_h-U_h||_2<=h^(31/8-o(1)),
    sup_[0,t_f] ||Q_h-U_h||C1<=h^(1/48-o(1)),           (6)
    sup_[0,t_f] ||Q_h-U_h||_infinity
                               <=h^(25/16-o(1))=o(k).

All constants are fixed before taking L large. The subpower factors in
(6) can be bounded by ell^K exp(C ell^(11/8)) for fixed C,K depending on
the stated choices and nu. Thus their logarithms are o(log(1/h)). A
separate H12 continuation argument proves smoothness; it is not inferred
from the L2 estimate alone.

## 2. The already available first-stage estimates

The base solution q_h and its reference Euler particle have the bounds
recorded in the log-log theorem and
[the reviewed original-time preparation](../analysis/original-seed-compatibility-draft.md).
Write

    m_h(t)=1+ell^(-1)e^(mu t).

For the fixed orders needed here,

    ||D_y^r q_h(t)||_infinity<=C_r m_h(t)h^(1-r),
       1<=r<=24, 0<=t<=t_f,
    integral_0^t_f m_h(t)dt<=C ell.                   (7)

A concrete construction fixes first-stage background H128, primary
amplitude and phase derivatives through 160, mean H132, and harmonic
amplitudes through 129. The existing first-stage error and H128
interpolation give the whole-interval scaled C24 bound in (7). These
are fixed indices, not indices increasing as h decreases. The first-stage
H12 norm is at most h^(7/4-12)exp(C ell) times a fixed power of ell.

The model central gradient is

    Abar=A0-ell^(-1)beta tensor N,                      (8)

where A0=grad V on the reference Euler particle, N is the returning
covector, and beta its growing polarization. The actual q_h particle
stays near this reference particle, including the phase needed for (8):
the primary phase is pi/2+o(1) along Y_h. For some fixed gamma>0,

    sup_[0,t_f] |grad q_h(t,Y_h(t))-Abar(t)|
                                  <=h^gamma exp(C ell),
    integral_0^t_f (|Abar|+|grad q_h(t,Y_h)|)dt<=C ell. (9)

The reference and actual terminal primary frames differ by the same
type of vanishing error. These estimates follow from the first-stage
C1 error h^(1/24-o(1)), velocity error h^(9/8-o(1)), phase drift
h^(1/8-o(1)), and the slow envelope/mean/harmonic bounds. Any smaller
fixed positive gamma suffices here.

The use of the unscaled V_j in (8) is consistent with every estimate:
the earlier small-viscosity comparison applies to any one fixed smooth
profile, with profile-dependent constants and threshold.

## 3. The selected central branch, from the full matched system to actual q_h

The following source notes supply the two halves of the full
pressure-corrected matching:

- [Outer proof](../analysis/outer-matching.md).
- [Inner proof](../analysis/inner-matching.md).

Their separate mathematical reviews are collected in
[the matching review](../analysis/matching-review.md).

Their notation and normalizations agree. To recall the load-bearing
content, for the unit terminal covector r_*=n_* cross p_* the exact model
covector has the form xi=C-fN, with

    C(t)=F(t_f,t)^T r_*, f'=-C.beta/ell,
    |f| comparable to ell min((t_f-t)^2,1).

The exact lift from N-perpendicular to xi-perpendicular is

    L_t v=v+N(C.v)/(f|N|^2-C.N).

In the bounded primary Floquet basis, the reduced growing scale is
A(t)=e^(mu t)f(0)/f(t). The full outer equation, including its exact
pressure-bearing remainder, has the selected column

    bbar(t)=L_t B(t) A(t)(X(t),w(t))^T,
    X=1+O(ell^(-1)[log^2 ell+(t_f-t)^(-2)]),
    w=O(ell^(-1)/(t_f-t))

near the overlap u_m=ell^(-3/10). The scalar stable kernel retains the
factor e^(-2mu(t-s))f(t)/f(s), avoiding an exponential loss in ell.
The full two-dimensional outer propagator obeys the accompanying upper
bounds for arbitrary bounded initial polarizations.

Let Lambda=|beta(t_f)||N(t_f)|/ell, R=sqrt(Lambda)u_m,
and a_*=r_*.A0(t_f)p_*<0. The incoming inner data are

    V(R)=D_h/R^2[1+o(1)], W(R)=2D_h/R^3[1+o(1)],
    D_h=ell f(0)sqrt(Lambda)/a_*,
    D_h comparable to ell^(5/2).                     (10)

The sign is positive because f(0) and a_* are negative. The inner
coordinates are b_p=sqrt(Lambda)V and b_n=W. The actual terminal
coefficients are retained in their inner equation. Its positive
Volterra connection and growing-interval weighted perturbation estimate
give positive terminal components and a uniform history bound. Combined
with the outer history integral, this proves, after a fixed bounded
normalization of bbar(0),

    |bbar(0)|=1,
    c ell^3<=p_* .bbar(t_f)<=C ell^3,
    c ell^(5/2)<=n_* .bbar(t_f)<=C ell^(5/2),
    sup_[0,t_f] |xibar||bbar|<=C ell^3,
    integral_0^t_f |xibar||bbar|dt<=C ell^3,
    |xibar(0)|<=C ell.                                (11)

In particular the integral here does not cost an extra log ell. The
outer part is bounded by C ell integral e^(mu t)dt; the inner part is
at most C ell^3 u_m.

Now use the actual terminal frame of q_h and choose xi*=4(n_* cross p_*).
Prepare its exact backward cotangent history along Y_h. Identify its
initial plane with the model initial plane by the small orthogonal
rotation between their unit normals, and use the rotated unit selected
initial polarization. Evolve the full pressure-corrected amplitude
equation along **actual q_h**, producing a real vector v_h(t).

For clarity, the comparison is made for unit covector directions on
the sphere and separately for log covector magnitudes. Their Lipschitz
coefficient is C|A|. Equation (9) therefore gives an error
h^gamma exp(C ell) in the cotangent and polarization maps, with C
enlarged finitely many times. No small covector denominator enters a
second exponential. The same bound holds for their products and for
their time integrals. It is smaller than every fixed power of ell.
Thus (11) transfers to the actual selected branch:

    |v_h(0)|=1,
    c ell^3<=p_* .v_h(t_f)<=C ell^3,
    c ell^(5/2)<=n_* .v_h(t_f)<=C ell^(5/2),
    sup |xi_c||v_h|<=C ell^3,
    integral_0^t_f |xi_c||v_h|dt<=C ell^3,
    |xi_c(0)|<=C ell.                                (12)

Subscripts * and c now refer to actual q_h. Constant rescaling of the
covector from unit length to length 4 has no effect on its polarization
equation and only changes fixed constants in these estimates.

Put N_h=n_* .v_h(t_f)>0, and normalize the terminal normal component:

    B_c(t)=v_h(t)/N_h,
    c_h=B_c(t_f)=n_*+P_h p_*,
    c ell^(1/2)<=P_h<=C ell^(1/2).                    (13)

This gives the exact central bounds

    |B_c(0)||xi_c(0)|<=C ell^(-3/2),
    sup |B_c||xi_c|<=C ell^(1/2),
    integral_0^t_f |B_c||xi_c|dt<=C ell^(1/2).         (14)

### Optional central transfer-cost corollary

Let M_h be the actual full transfer on the two receiving planes. The
outer full-matrix upper bound gives overlap weighted data of size at
most C ell^(5/2) for every unit initial polarization. The inner weighted
operator bound then gives row upper bounds C ell^3 and C ell^(5/2).
The selected column in (12) gives the corresponding lower bounds.
Consequently

    |M_h^*p_*| comparable to ell^3,
    |M_h^*n_*| comparable to ell^(5/2).                (15)

The exact determinant is r_h=|xi_c(0)|/|xi*|, comparable to ell by
the nilpotent deformation formula in
[the seed-cost note](../analysis/actual-seed-cost.md).
Its adjugate and least-norm identities therefore give

    C_pure=|M_h^*p_*| comparable to ell^3,
    C_opt=r_h/|M_h^*n_*| comparable to ell^(-3/2).      (16)

These are finite central-ODE costs. The nonlinear construction below
uses the explicit selected branch (13), so it does not require proving
anything further about the optimizing vector.

## 4. Define the second original datum through actual-q geometry

Fix a real nonnegative smooth bump chi, equal to one near the origin,
supported strictly inside the unit ball. On the final radius-d ball
around Y_h(t_f) define

    S_*(y)=xi*.(y-Y_h(t_f)),
    b_*(y)=k ell^(7/8)chi((y-Y_h(t_f))/d)c_h.           (17)

Pull S_* back by the known smooth q_h flow and evolve it by
D_q S=0. Prepare the initial tangent amplitude by the inverse finite
polarization ODE so that its subsequent **forward** evolution satisfies

    D_q b=G b,
    G=-A+2xi tensor xi A/|xi|^2,
    A=grad q_h, xi=grad S,
    b(t_f)=b_*.

This defines original data using the base solution q_h, which is known
independently of Q_h. It does not evolve viscous NS backward and does
not install a new wave at time t_f.

Write b=k ell^(7/8)chi_t B, where chi_t is the transported bump and
B(t_f,y)=c_h is the unweighted polarization. At the central q_h particle
the finite inverse preparation recovers exactly B_c in (13). The
transported phase obeys S(t,Y_h(t))=0 at every time. With

    theta=S/k+pi/2,
    F=xi cross b/|xi|^2, d_b=curl F,
    Z=Re[(b+i k d_b)e^(i theta)]
      =k Re curl[i F e^(i theta)],                    (18)

set Z_{2,h}(0)=Z(0). The real phase and primary amplitude are essential
to the quadratic identities in section 6. Harmonic correctors may be
complex.

The vector potential is supported strictly inside an embedded transported
phase chart and vanishes smoothly before its boundary. Extend that
potential by zero and take the periodic curl. This produces a real,
smooth, exactly divergence-free and mean-zero original datum. No global
periodic extension of the affine scalar phase is required. V itself
has zero mean by the compact solenoidal identity integral V_i=integral
div(x_i V)=0, and the first packet is also a curl.

## 5. Every central-to-envelope hypothesis is discharged

This section applies the independently reviewed section 8 of
[the mixed-seed nonlinear budget](../analysis/mixed-seed-nonlinear-budget.md)
to the now proved central estimates (12)-(14).

At each fixed required order let E_h=exp(C ell), with C enlarged
finitely many times to absorb fixed powers of ell and time length.
The q_h cell estimates (7) give, on a slightly larger transported chart,

    |B|+|xi|+|xi|^(-1)<=E_h,
    |D_y^r B|+|D_y^r xi|<=h^(-r)E_h, 1<=r<=18.       (19)

One derives these by differentiating flow, normalized-covector and
polarization equations in coordinates scaled by h, with time rate m_h.
Their top coefficients integrate to C ell; lower derivative products
enlarge E_h finitely many times. They do not put E_h inside a new
exponential. q_h C24 leaves room for these fixed orders.

Incompressibility gives support volume O(d^3). Its diameter is at most
d E_h=o(h), and it remains in a single embedded phase chart. Mean-value
comparison with the central branch gives

    sup_support(|B-B_c|+|xi-xi_c|)<=(d/h)E_h,
    sup_support ||B||xi|-|B_c||xi_c||<=(d/h)E_h.       (E1)

The bump itself is not relatively constant; it decreases to zero.
Using only its fixed supremum, (E1) gives

    sup_support |b||xi|/k
       <=C ell^(7/8)|B_c||xi_c|+h^(1/4)E_h.          (E2)

The finite amplitude bounds are consequently

    ||D^r b||_infinity<=k d^(-r)E_h,
    ||D^r b||_2<=k d^(3/2-r)E_h,
    |D^r xi|<=h^(-r)E_h,

through the stated orders. The unnormalized L2 volume factor d^(3/2)
has been retained despite any anisotropy of the transported support.

In the curl lift, every derivative except the leading b tensor xi/k
costs at most (k/d)E_h+(k/d)^2 E_h; its velocity is also smaller than
these upper bounds. Integrating (E2), including its subpower-small
error, gives

    ||Z(0)||C1<=C ell^(7/8)|B_c(0)||xi_c(0)|
                                               +h^(1/4)E_h,
    I_h:=integral_0^t_f sup_support |b||xi|/k dt
       <=C ell^(7/8)integral_0^t_f |B_c||xi_c|dt
                                               +h^(1/4)E_h. (E3)

Equation (12) is the previously open hypothesis (E4), now with zero
exponent loss. Substituting (14) gives the strengthened (E5):

    ||Z(0)||C1<=C ell^(-5/8),
    I_h<=C ell^(11/8),
    sup_support |b||xi|/k<=C ell^(11/8).              (E5)

The last line also uses the central supremum in (14). The positive
power h^(1/4) absorbs every fixed exp(C ell) error. The history bound
is therefore established on the whole support, not merely at its
center. Since 11/8<2 and ell^2=log(1/h), I_h=o(log(1/h)).

## 6. The full nonlinear approximation and residual

Put D=D_q. The real solenoidal curl packet (18) has the exact split

    (Z.grad)Z=Q0+Re(F2 e^(2i theta)),
    Q0=1/2[(b.grad)b+(div b)b+k^2(d_b.grad)d_b],
    F2=1/2[(b.grad)b-(div b)b-k^2(d_b.grad)d_b
       +i k((d_b.grad)b+(b.grad)d_b-(div b)d_b)],
    F1=i k[(D+A)d_b+grad(2xi.A b/|xi|^2)].             (20)

Here div b=xi.d_b, because xi is a gradient. This identity cancels
the apparent |b|^2/k leading self-interaction even though the strain
is large. It does not cancel the coefficient seen by a general error.

Solve the global forced linear Euler mean about the actual q_h:

    Dm+A m+grad pi_m=-Q0, div m=0, m(0)=0.

Keep its complete nonlocal pressure and tails. Define

    H1=F1+(i/k)(m.xi)b, H2=F2,
    Dg_n=Gg_n-Pi_xi Hn, g_n(0)=0, n=1,2,
    Pi_xi=I-xi tensor xi/|xi|^2.

The mean-to-primary term is retained because the pressure-bearing mean
can have a normal component. Use the exact forced curl lifts

    C_n[g]=(g+(i k/n)curl(xi cross g/|xi|^2))e^(in theta),
    pi_n=(i k/n)(2xi.A g+xi.Hn)e^(in theta)/|xi|^2.    (21)

The longitudinal forcing term +xi.Hn is necessary to cancel the
parallel part of the forcing. Set

    U_h=q_h+m+Z+Re C_1[g1]+Re C_2[g2].                (22)

If pi_q is the pressure of q_h, the complete approximation pressure is

    pi_Z=2 i k (xi.A b)e^(i theta)/|xi|^2,
    Pi_h=pi_q+pi_m+Re(pi_Z+pi_1+pi_2).

The primary pressure pi_Z is included when obtaining F1 in (20).
Every added correction other than Z is zero at time zero, so (22)
has exactly the original datum (2).

A sufficient fixed order budget is q_h C24, primary b and xi C18
(S C19), mean H16, and harmonic amplitudes C13/H13. Weighted global
L2 estimates for the mean have coefficient C_r m_h(t), because
d^(j-1)||D^j q_h||_infinity<=C_j m_h(t)(d/h)^(j-1).
The Leray projector is a global L2 contraction, uniformly in L, and
pressure disappears in the differentiated solenoidal pairings. Global
Sobolev interpolation then gives its pointwise bounds without asserting
an L-infinity bound for Leray. The triangular harmonic equations give
the same sizes:

    ||D^r m||_infinity+||D^r g_n||_infinity
                                   <=k^2 d^(-1-r)E_h,
    ||D^r m||_2+||D^r g_n||_2
                                   <=k^2 d^(1/2-r)E_h. (23)

Material derivatives of the curl lift use only
D partial_j F=partial_j DF-(partial_j q_m)partial_m F.
No independently bounded q_t or pressure Hessian is being assumed.

After (20)-(21) cancel the leading mean, first and second harmonics,
the complete remaining L2 orders are as follows, each multiplied by
E_h and with time integration absorbed in it:

    uncancelled linear/curl and primary/correction terms:
                          k^3 d^(-1/2)=h^(31/8),
    quadratic correction and global mean products:
                          k^4 d^(-3/2)=h^(33/8),
    primary viscosity: epsilon k^(-1)d^(3/2)=nu h^(35/8),
    oscillatory curl/correction viscosity:
                          epsilon d^(1/2)=nu h^(37/8),
    slow mean viscosity: epsilon k^2 d^(-3/2)=nu h^(41/8).

The estimates include mean advection of the higher harmonics, every
remaining phase interaction, and the global mean self-product.
Tangency cancels fast self-advection between leading tangent amplitudes;
normal curl corrections and the normal mean are explicitly accounted
for. The mean tails are estimated by a pointwise bound times their
global derivative L2 norm. None are removed by a support assumption.
Since q_h is itself exact NS, it has no residual in this calculation.

Thus, for the pressure supplied by these constructions,

    integral_0^t_f ||partial_t U_h+U_h.grad U_h
                     +grad Pi_h-epsilon Delta U_h||_2 dt
                                      <=h^(31/8)E_h.   (24)

Also (E5) and (23) give

    integral_0^t_f ||grad U_h||_infinity dt
       <=C ell+C I_h+h^(1/4)E_h<=C ell^(11/8),        (25)
    sup ||U_h-q_h-Z||C1<=h^(1/4)E_h=o(1).

The coefficient (25), rather than a generic exp(C ell) history bound,
is what makes the next nonlinear estimate close.

## 7. Full NS comparison and a separate strong continuation argument

For each h, start the local smooth unforced NS solution Q_h with datum
U_h(0), and let e_h=Q_h-U_h on its strong existence interval. Both
fields are solenoidal. Its exact L2 energy inequality is

    d||e_h||_2/dt<=||S(U_h)||_infinity||e_h||_2
                             +||R_h||_2,
    e_h(0)=0.                                        (26)

The self-advection e_h.grad e_h cancels in this pairing. No small
gradient hypothesis on the packet was used to obtain (26). From
(24)-(25), with G_h=ell^K exp(C ell^(11/8)),

    sup ||e_h||_2<=h^(31/8)G_h.                       (27)

Now separately bootstrap ||grad e_h||_infinity<=1. The integer NS
H12 energy inequality has coefficient C||grad Q_h||_infinity.
Equation (25) and the bootstrap make its integrated coefficient at
most C ell^(11/8). The initial datum and the approximation satisfy

    ||Q_h(0)||H12+sup ||U_h||H12
       <=k d^(3/2)k^(-12)E_h+h^(7/4-12)E_h
       <=h^(-117/8)E_h.

The mean and harmonic terms in this estimate are smaller than the
primary fine packet. Hence, while the bootstrap holds,

    ||Q_h||H12+||U_h||H12<=h^(-117/8)G_h.              (28)

Uniform Fourier splitting, or local Euclidean GN with its L2
low-frequency term, gives on the expanding torus

    ||grad e_h||_infinity
      <=C||e_h||_2^(19/24)||e_h||H12^(5/24)+C||e_h||_2
      <=h^(1/48)G_h,

after enlarging the fixed C,K in G_h. The exponent is exactly

    (31/8)(19/24)-(117/8)(5/24)=1/48>0.

The analogous velocity interpolation exponent is
(31/8)(7/8)-(117/8)(1/8)=25/16. Thus (6) holds and the
gradient bootstrap closes strictly below 1/2 for all sufficiently large
L. The finite H12 continuation alternative prevents a breakdown before
t_f; smoothness of the initial data and positive viscosity propagate
all higher smoothness. This proves the asserted strong lifetime.

The constants in these inequalities are uniform in the expanding
period: no shrinking-frequency Poincare constant is used. Dependence
on nu, the one fixed profile, and the finite derivative orders remains
in C,K and the lower threshold for L.

Finally (25) and the error gradient in (6) imply (4), since
t_f h^(1/48)G_h=o(1). The actual NS gradient integral therefore has
the same C ell^(11/8) bound as the approximation.

## 8. The final strain is observed at the prescribed base-q particle

At t_f the central envelope equals 1, S=0, and theta=pi/2. Since the
phase is affine and the bump is constant near the center, the curl
correction in (18) vanishes there and its leading gradient is exactly

    grad Z(t_f,Y_h(t_f))=-b_*(Y_h(t_f)) tensor xi*/k.

The two vectors are perpendicular and

    b_*(Y_h(t_f))/k=ell^(7/8)(n_*+P_h p_*),
    |xi*|=4, P_h comparable to ell^(1/2).

Consequently

    |S(Z)(t_f,Y_h(t_f))|_F
      =|b_*||xi*|/(sqrt(2)k)>=c ell^(11/8).            (29)

The orthogonal p_* and n_* components cannot cancel in this norm.
Equation (25) makes the mean and harmonic C1 contributions o(1),
and (6) makes the exact nonlinear tracking error o(1). Subtracting
the exact base solution q_h in (22) therefore gives (5).

No further interval [t_f,T] is needed or used. The finer packet already
has total strain larger than the host at t_f. Its terminal normal
component has size ell^(7/8), while its larger p component has size
ell^(11/8). This theorem concerns total added strain, not a normal
component exceeding the host or a new late-time relative gain ratio.
It makes no claim about a specified Fourier high-pass cutoff.

## 9. Physical rescaling and the exact boundary of the result

For the fixed original torus of period 2pi and viscosity nu, put
A_L=L^(7/5) and define

    u_L(t,x)=A_L Q_h(A_L L t,Lx),
    u_L^base(t,x)=A_L q_h(A_L L t,Lx).

Because nu L/A_L=nu L^(-2/5)=epsilon, these solve the original
unforced NS equation of viscosity nu. Their finite observation time
is t_f/(A_L L). Both strains acquire the common factor A_L L, while
the time integral of the gradient is invariant under this consistent
rescaling. Each datum is smooth and finite energy.

The initial data depend on L. In particular the small C1 bound (3)
is in the rescaled coordinates; its physical gradient is multiplied
by A_L L. This is not a fixed-viscosity theorem for a uniformly small
physical C1 perturbation of one fixed datum. It is not a single
trajectory with infinitely many compatible stages, and does not
imply blow-up, global regularity, ROOT, or (E'). Both packets were
supplied in the original data. No automatic generation of a finer
seed, no nonlinear spectral cascade, and no novelty or priority
claim is asserted.

The receiving carrier has |xi_c(0)| comparable to ell and terminal
|xi*|=4. Its central oscillation scale is therefore initially k/ell
and finally comparable to k, while both remain finer than the primary
scale h. The construction amplifies a finer component already supplied
at time zero; it does not generate a new finer frequency or establish
a monotone forward cascade. The separate
[smooth seed-supply note](../analysis/smooth-seed-supply.md)
records why a finite family does not automatically assemble into one
smooth initial datum for an infinite construction.

The finite theorem has a precise additional content beyond the older
late-seed results: its second packet is prepared at original time zero,
its initial C1 effect tends to zero in the stated coordinates, and the
full nonlinear solution remains smooth while its added finer-wave
strain becomes larger than the first-stage host. The proof pays for
its entire earlier feedback through (14), (E1)-(E5), and (25)-(28).


## Review and reproducible controls

The [matching and full-assembly reviews](../analysis/matching-review.md)
record the independent agent derivations and their precise boundaries.
The complete source reviewed before archival wording and link edits had
SHA-256 `3d25dbcc64620ad6d7323c18b2760c7c832fabe9fb9518d9a3a8ac7db1171f94`.

The [instrument](../../experiments/nse_original_handover.py),
[mutation and receipt tests](../../tests/test_nse_original_handover.py), and
[saved receipt](../../artifacts/enstrophy_sup/nse_original_handover.json)
verify 55 exact algebra/exponent controls and seven tests. They include
full pressure/frame identities, the inner conjugation, centered curl
derivatives, and the interpolation and viscosity powers. These finite
checks do not formally certify the growing-interval matching, nonlinear
PDE residual inequalities, strong existence, or the conclusion of ROOT.
