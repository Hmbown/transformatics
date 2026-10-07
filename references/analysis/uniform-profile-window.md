# A quantitative growing-depth profile window

8 September 2026. **PROVED at the restricted written analytic scope below.**
The quantitative Gevrey background, uniform operators and recurrence,
and sharp-history/continuation assembly passed separate AI-agent reviews
and root reads. These are not external expert acceptance or a formal PDE
certificate. The reviews pin the version before this introductory status
and final standing update; no estimate was changed.

This discharges the operator package in the
[growing-depth budget](growing-depth-budget.md), conditional
on the fixed Gevrey-2 profile choice constructed in the reviewed
[growing-order background](growing-window-background.md).
The [background review](growing-window-background-review.md),
[operator review](uniform-profile-window-review.md), and
[assembly review](uniform-profile-assembly-review.md)
state their separate scopes. Their combined inputs were checked at integration.
ROOT, E-prime and FORCED-D remain OPEN. No DNS is used.

## 1. Choice of data and order

Choose one sufficiently thin fixed Gavrilov profile and the two original
packets with quantitative Gevrey-2 cutoffs and phase profile, as specified
in the background note. This is a subclass of the previous smooth-profile
construction. It does not assert that an unspecified old smooth cutoff
was Gevrey. The choices are fixed before h tends to zero; no proof order
changes the datum at a given h.

Use k=h^(3/2), d=h^(5/4), rho=k/d, epsilon=nu h^4,
ell²=log(1/h), eta=ell^(1/16), and

    T=t_f+3 log(ell)/(16mu),  J=ceil(K eta),
    N=N0+8J,  W=1+T+log(N+2).

Here N0 is a sufficiently large fixed integer, and K is selected once
by the continuation inequality. Reserve a fixed larger multiple of N
in the background lemma. This only enlarges fixed constants.

The background input is actual q through T, with

    I_q:=integral_0^T m_h dt <= C eta ell^(9/8)+C log ell,
    ||grad q||infinity <= C m_h,
    ||D^r q||infinity <= C m_h h^(1-r) K_N^(r-1)(r!)²,
    log K_N <= C N² W.                                      (1)

Its full weighted derivative comparison, not differentiation of a C1
error, supplies these jets. Also retain the background's actual comparison

    ||q-U_app||infinity <= h^(5/4) exp(C P_N),
    ||grad(q-U_app)||infinity <= h^(1/4) exp(C P_N),           (1b)

where P_N is bounded by the logarithmic budget below. These errors and the
primary wave's zero leading velocity on the reference Euler particle are
inputs to section 5; abstract jet upper bounds alone would not suffice.
The background's phase, inverse phase, original preparation
and flow estimates have logarithmic loss bounded by

    H_N=C[N²(I_q+1)+N^4 W].                                 (2)

Enlarge C finitely and put D=exp(H_N)>=2. All uses of D below permit a
fixed power of D independent of N,J,h. A factor exp(CN log(N+2)), N^C,
T, or a fixed power of ell is already a fixed power of D.

The smallness used to handle coefficient derivatives is stronger than
merely h tending to zero: for every fixed c,

    rho D^c N^c -> 0.                                       (3)

Indeed H_N=O_K(ell^(21/16)+ell^(1/4)log ell)=o(ell²).

## 2. Norms and the global mean solver

Use the finite-depth source's scaled spatial norms

    S_r(v)=sum_(j=0)^r d^(j-3/2)||D^j v||2,

with full derivative tensors. For a phase profile use

    S_(r,M)(v)=sum_n (1+|n|)^M S_r(v_n).

Every phase index is retained. At round j reserve spatial and phase
orders N-8j. Norms at two additional spatial orders control pointwise
products; no compact-support assertion is made for any mean.

The Hilbert norm Y_(r,d) of the background note is equivalent to
d^(3/2)S_r within sqrt(r+1), absorbed in D. Leibniz differentiation,
scaled Sobolev embedding and the phase convolution inequality give

    S_(r,M)(fg) <= D^c S_(r+2,M)(f) S_(r+2,M)(g),             (4)

whenever both factors have global norms; for coefficients use their
scaled pointwise derivative norms instead. The phase inequality costs
at most 2^M and the spatial tensor count at most exp(Cr log(r+2)).
Phase averaging is contractive and the zero-mean phase primitive is
contractive on A_M. Evaluation at s=S/k has L2 bound by the phase sum;
no spatial Fourier cutoff or assumed phase orthogonality is used.

For the mean equation

    (partial_t+q.grad)v+(v.grad)q+grad p=f, div v=0, v(0)=0,

differentiate in global L2. Pressure vanishes only in the solenoidal
pairing. Transport at top order cancels. The order-i>=2 coefficient
in the commutator is bounded by

    binomial(r,i) d^(i-1)||D^i q||infinity
       <= C m_h binomial(r,i)(rho K_N)^(i-1)(i!)².            (5)

The corresponding stretching coefficients contain one more derivative
of q and one more factor d. Since rho K_N N² tends to zero, their
geometric sums, and the sums over derivative levels, are bounded by
C N² m_h. Consequently

    sup_t S_r(v(t)) <= D^c integral_0^T S_r(f(t))dt.           (6)

The same bound holds when v has nonzero prescribed initial data, with
its initial norm added. This includes all global pressure tails and
requires no L-infinity estimate for Leray. A support radius and a
derivative weight have not been identified.

## 3. Phase and polarization solver

Write xi=grad S and n=xi/|xi|. On the transported packet chart, the
background's triangular flow estimates give, through the reserved orders,

    |xi|+|xi|^(-1) <= D^c,
    d^r |D^r n| + d^r |D^r log|xi|| <= rho^r D^c,
                                                     1<=r<=N+4. (7)

Here the single D covers the largest reserved order, including factorial
and flow factors; rho^r comes from the h-scale phase jets. The phase was
prepared by transporting a linear terminal phase through actual q.
Thus its derivatives have the h scale, whereas the bump has the d scale.
Formula (7) is not a claim about derivatives of the bump.

The bookkeeping behind (7) must retain the per-order flow bounds until
composition is finished. One may use logarithmic majorants of size
C[(r+1)²(I_q+1)+(r+1)log K_N+(r+1)^4 W] at derivative order r.
In a chain-rule partition, the positive orders sum to at most N+4;
their squares and fourth powers sum to at most a fixed multiple of
N² and N^4. Inverse magnitudes add at most O(N I_q). Thus all partition
terms fit (2) after counting exp(CN log(N+2)) partitions. Multiplying
the largest order-N bound once per factor would instead produce a
spurious D^N; that is not the estimate used here.

For G=-A+2n tensor(n^T A), A=grad q, (1),(7) imply

    |G| <= C m_h,
    d^r |D^r G| <= m_h rho^r D^c,  1<=r<=N+2.               (8)

The normalized variables avoid placing |xi|^(-1) in the top growth
coefficient. Gevrey product and composition counts fit (2). Even after
binomial summation, every differentiated coefficient in (8) is small
relative to m_h by (3); the undifferentiated coefficient is C m_h.

For zero phase mean g, solve the exact equation

    (partial_t+q.grad-kappa(t)partial_s²)g=Gg-Pi_xi H,

with the tangency constraint xi.g=0 and kappa>=0 the central clock.
Apply the differentiated L2 estimate to each phase Fourier mode.
The term -kappa n² is nonpositive, and all spatial derivatives of
kappa vanish. Summing the mode estimates with the A_M weights gives

    sup_t S_(r,M)(g(t))
       <= D^c [S_(r,M)(g(0))+
                         integral_0^T S_(r,M)(H(t))dt].     (9)

Multiplication by Pi_xi is covered by (7). The amplitudes vanish smoothly
before the material chart's boundary, so extension by zero introduces
no boundary term. The global mean equation was treated separately in (6).

The full pressure and lift remain

    p_g=-k partial_s^(-1)[(2xi.Ag+xi.H)/|xi|²],
    V_g=-xi cross partial_s^(-1)g/|xi|²,
    W_g=g+k curl_x V_g.                                    (10)

Their coefficient, product and derivative bounds cost a fixed power of
D and at most the derivatives reserved by the finite-depth recurrence.
For example the slow curl costs d^(-1), and an evaluated fast derivative
costs k^(-1) times a coefficient bounded by D^c. Material derivatives in
the residual are eliminated by Dxi=-A^Txi and the exact profile equation,
including xi.H in the pressure. No time derivative of q is needed.

## 4. Uniform recurrence with a fixed total number of derivatives

Use exactly equations (3)--(7) of the
[finite-depth profile source](finite-depth-profile.md).
In particular cancel the new mean's fast advection of the old profile
before estimating it. Let F_j be the supremum normalized residual norm
at the reserved orders, with a harmless factor 1+T incorporated in D.
The primary receiving amplitude has S_(N,N) size at most k D^c. Its
transported bump contributes d-scale derivatives, and the fixed
Gevrey-2 F contributes exp(CN log(N+2)), both covered by D.

Equations (4),(6),(9),(10), and the exact remainder identity give fixed
b>=1,C such that

    F_0 <= C k rho D^b,
    ||delta m_j||scaled+||delta a_j||scaled <= C D^b F_j,
    F_(j+1) <= C rho D^b F_j+C D^b F_j²/k.                  (11)

The same increment bound, divided by k, controls evaluated gradients
after increasing b once. This uses two reserved spatial derivatives and
the phase derivative; they are not counted for free.

For completeness, the small factors in the exact linear residual are
k/d, epsilon/k², epsilon/(kd), and epsilon/d². They are bounded by a
fixed multiple of rho. Leading tangent/tangent fast products vanish
exactly; normal curl products cost k/d. An existing mean's fast
advection costs ||m_j||/k, and the new mean's fast advection of the new
wave is the quadratic term in (11). Global mean-mean products use (4).
The complete central/actual diffusion mismatch is bounded by
(epsilon/k²)D^c, and all Fourier modes in its phase derivatives are
charged to the reserved A_M orders.

No source differentiation needs more than the eight reserved orders per
round: the linear lift remainder uses at most three slow derivatives
and two phase derivatives, products require two extra spatial orders for
embedding, and the remaining allowance covers the pressure/lift inputs.
Only the known q and phase require the larger fixed order reservation.

To verify that the constants do not grow by repeated substitution, put
A=C D^b>=1, g_j=F_j/k and z=2 A² rho. If z<=1/2, induction gives

    g_j <= A rho z^j,
    sum_j ||delta m_j,delta a_j||scaled <= 2k A²rho.          (12)

Indeed g_j<=A rho, so A rho g_j+A g_j²<=2A²rho g_j.
The summed evaluated gradients are at most 2A²rho after the fixed
enlargement of b. They tend to zero, and the old amplitude and mean
bounds used in deriving (11) therefore hold at every round. Enlarging
D a fixed number of times pays them; no enlargement occurs recursively
inside its exponent.

Evaluation and time integration of the last residual yield

    integral||R_J||2dt
       <= k rho^(J+1)d^(3/2) exp(C(J+1)H_N),               (13)
    ||Q_h(0)||H12+sup||U_J||H12
       <= h^(-117/8) exp(C(J+1)H_N).                       (14)

For (14), the leading receiver costs k k^(-12)d^(3/2), the global
mean costs at most k rho d^(-12)d^(3/2) times D powers, and the
first-stage H12 norm has smaller h power. The initial increments vanish
exactly, so U_J(0) is the fixed chosen two-wave datum.

## 5. Sharp history must be kept separate from the derivative bound

The outgoing central ODE is uniform on delta<=t-t_f<=C0 log ell for
any one fixed C0. Choose C0=1/(4mu)>3/(16mu). It gives

    |b_c||xi_c|/k comparable to ell^(15/8)exp(mu(t-t_f)).

Its previously established through-focus integral is O(ell^(15/8)).
The primary's leading velocity vanishes on the reference Euler particle.
Equation (1b) and the smaller primary mean/curl velocities therefore give
a q-particle displacement h^(5/4)exp(C H_N). Multiplication by the q
Hessian scale h^(-1), together with its gradient comparison, leaves
h^(1/4)exp(C H_N) in the central coefficient matrix. Normalized cotangent
and polarization comparison costs exp(C I_q). Whole-label comparison
adds (d/h)exp(C H_N) after factoring out the transported bump. Thus the
comparison to actual q and then over the whole envelope has error
h^gamma exp(C H_N) for a fixed gamma>0. This tends to zero, even after all fixed
normalization powers. The central leading term is not multiplied by D.
The heat clock is at most h D^c and tends to zero. Hence the full fixed
profile has bounded first derivative and preserves F'(0)=1 up to a
vanishing error. The exact curl lift and every summed new gradient in
(12) have vanishing time integral. Thus

    integral_0^T ||grad U_J||infinity
       <= B eta ell²+C ell^(15/8)+C I_q+o(1),               (15)

where B is independent of J,h. At the chosen first-stage particle,
the endpoint leading symmetric strain is between c eta ell² and
C eta ell². Tangency makes the rank-one gradient's symmetric part
have Frobenius norm |b||xi|/(sqrt(2)k). The background gradient,
slow derivatives and correction gradients are smaller.

The error statement in this section uses the existing central and
whole-envelope equations with explicit finite-order constants from
the background input. A general upper bound D on the primary amplitude
alone would not imply (15), and would not suffice for continuation.

## 6. Conditional assembly and its boundary

Take in the growing-depth budget

    L_h=C[(J+1)^3(I_q+1)+(J+1)^5 W+ell^(15/8)+1].           (16)

This bounds (13)--(15), since N=O(J). With a=1/16 and J=ceil(K eta),

    L_h/(eta ell²)
       =O_K(ell^(-11/16)+ell^(-7/4)log ell+ell^(-3/16))
       ->0.                                                (17)

The additional ell^(15/8) is essential: it is the earlier central
history and cannot be omitted from the approximation package. If desired
(16) fits its sufficient condition (2) with p=11<14.

Select K once so that 19K/96>Gamma B+2, with the fixed H12 energy
constant in Gamma. The conditional continuation argument then gives

    sup_[0,T]||grad(Q_h-U_J)||infinity <= h^eta,

and a smooth actual unforced Q_h through T. This establishes an
explicit eta=ell^(1/16) version for the fixed Gevrey-2 subclass under
the separately reviewed background, operator and assembly estimates.
The endpoint added symmetric strain is comparable to eta ell².
It concerns a finite time for each member of a changing-data
family. It supplies no infinite one-datum cascade, terminal smooth force,
new receiving phase, or resolution of either Navier--Stokes target.
