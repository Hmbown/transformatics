# Mixed terminal polarization: a conditional nonlinear preparation criterion

**Current application:** the [original-time nonlinear theorem](../navier-stokes/original-nonlinear-handover.md) now combines this note with the completed matching and whole-envelope estimates. Its full finite supplied-seed assembly passed a separate agent review. Historical conditional and unfinished-matching statements below retain their local derivation scope; they do not describe the current finite theorem. Infinite compatibility and ROOT remain open.

8 September 2026. Bounded independent budget audit. No DNS. This research appendix remains outside the registered proof graph; an independent mathematical review accepted the conditional implication after the real-amplitude and central-envelope conventions below were made explicit.
The criterion below is a written analytic implication. Its sharp hypotheses
have NOT been verified for the actual fixed Gavrilov profile. The limiting
jet diagnostic is not that verification. ROOT,
original-time nonlinear compatibility for the actual family, and iteration
remain open.

**Later matching checkpoint, 8 September:** [outer matching](outer-matching.md), [inner matching](inner-matching.md), and section 8's whole-envelope extension have passed separate agent reviews. The conditional criterion is preserved below; its hypotheses are discharged in the separately reviewed original-time nonlinear theorem. Earlier statements that the matching remains open concern the original checkpoint.

## 1. Outcome

The proposed mixed branch is not excluded by the nonlinear WKB budget.
A uniform whole-history leading strain bound O(ell^(11/8)) would suffice:
over T=O(log ell), its integral is O(ell^(11/8) log ell)=o(ell^2).
The initial and terminal exponents suggested by the limiting map therefore
have enough room for a one-mean/two-harmonic construction, a full NS error
estimate, and a separate strong-existence bootstrap. One does not need the
sharper conjectured integral O(ell^(7/8)) to close this finite transfer.

However, endpoint map powers alone do not prove a bound on this integral,
or on the preparation over the entire envelope. The required condition is
an actual-q history estimate on the prepared branch. Generic exp(C ell)
ODE estimates are sufficient for coefficient jets but insufficient for the
leading strain integral: exponentiating exp(C ell) again is fatal.

The larger p component also changes the conclusion: the new fine-scale
strain already dominates the host at the receiving time t*. Its subsequent
late shear increment is smaller than that existing p component. This is a
candidate original-time strain handover, not an additional late-time gain
ratio of ell^(1/4) for the mixed vector.

## 2. Precise sufficient hypotheses

Set epsilon=nu h^4, ell=sqrt(log(1/h)), k=h^(3/2), d=h^(5/4),
T=(2/mu)log ell. All spatial norms below are unnormalized on the expanding
periodic torus. q is the actual smooth first-stage NS flow. Write
D=partial_t+q.grad and A=grad q. Assume the actual first-stage bounds

    ||D_y^r q(t)||_infinity <= C_r m(t) h^(1-r), r=1,...,24,
    integral_0^T m(t) dt <= C ell,
    m(t)=1+ell^(-1) exp(mu t).

The fixed higher Sobolev bounds used in the existing first-stage proof are
retained. Prescribe one real receiving phase and a real tangent mixed amplitude at
t*, then transport its phase by q and its amplitude by

    D S=0,  xi=grad S,
    D b=G b, G=-A+2 xi tensor xi A/|xi|^2, xi.b=0.

Here S and b are real, and b includes the real transported envelope;
the harmonic correctors below may be complex. The construction is forward
geometric optics with an ODE-prepared initial amplitude, not backward
viscous evolution. Phase and amplitude can be smoothly extended from the
transported patch through their compactly supported vector potential.

Require the following uniform bounds for this PARTICULAR prepared branch.
For the finitely many derivatives used below (up to 18 suffices for the
mean and harmonic construction), there are positive factors E_{r,h} with
log E_{r,h}=o(ell^2), closed under finite products, such that

    ||D_y^r b||_infinity <= k d^(-r) E_{r,h},
    ||D_y^r b||_2 <= k d^(3/2-r) E_{r,h},
    |xi|+|xi|^(-1) <= E_{0,h},
    ||D_y^r xi||_infinity <= h^(-r) E_{r,h} (r>=1).

The transported patch has volume O(d^3). Derivatives and inverse-map
constants may lose subpowers of h; they need not be polynomial in ell.
The q-flow jet estimates exp(C_r ell) in the original preparation draft
satisfy this part. The envelope factorization must be uniform across the
whole pulled-back support, not just at its central particle.

The additional, decisive condition is

    I_h := integral_0^T sup_patch |b(t,y)| |xi(t,y)|/k dt
          = o(ell^2).                                      (H)

For a small-strain original datum require separately

    ||Z(0)||_{C^1}=o(1),
    Z=Re[(b+i k curl(xi cross b/|xi|^2)) exp(i S/k)].

Condition (H) cannot be replaced by a bound on b(T), on an endpoint singular
value, or by log E_h=o(ell^2). It is a history norm of the oscillatory lift.
It permits polynomial strain ell^a over logarithmic time for every a<2.
This is a sufficient criterion, not a necessary condition for nonlinear
stability.

## 3. Exact cancellations and the pressure-bearing corrections

This section gives the mechanism rather than assuming an envelope-rate
stability theorem for arbitrary errors. Put d_b=curl(xi cross b/|xi|^2),
so div b=xi.d_b. With phi=S/k, the exact identities are

    Z.grad Z=Q0+Re(F2 exp(2i phi)),
    Q0=1/2[(b.grad)b+(div b)b+k^2(d_b.grad)d_b],
    F2=1/2[(b.grad)b-(div b)b-k^2(d_b.grad)d_b
       +i k((d_b.grad)b+(b.grad)d_b-(div b)d_b)],
    F1=i k[(D+A)d_b+grad(2 xi.A b/|xi|^2)].

In particular the apparent |b|^2/k self-interaction cancels because xi.b=0.
This does not cancel the strain coefficient seen by an arbitrary error.

Solve the global, pressure-corrected linear Euler mean equation

    Dm+A m+grad pi_m=-Q0, div m=0, m(0)=0.

Keep its nonlocal pressure tails. Then solve tangent amplitude equations

    H1=F1+(i/k)(m.xi)b, H2=F2,
    Dg_n=Gg_n-Pi_xi Hn, g_n(0)=0, n=1,2.

The term (i/k)(m.xi)b is essential: pressure can produce a normal mean,
so tangency of the primary b does not remove mean-driven phase feedback.
Use exact solenoidal lifts

    C_n[g]=(g+(i k/n)curl(xi cross g/|xi|^2)) exp(i n phi)

and pressure amplitudes

    pi_n=(i k/n)(2 xi.A g_n+xi.Hn)/|xi|^2 exp(i n phi).

These cancel the entire leading forcing, including its parallel part. Set
U=q+m+Z+Re C_1[g1]+Re C_2[g2]. Every correction is initially zero.

Weighted d-Sobolev estimates for the mean have coefficient C_r m(t), since

    d^(j-1)||D^j q||_infinity <= C_j m(t)(d/h)^(j-1).

Pressure vanishes in each differentiated solenoidal L2 pairing. Global
Sobolev interpolation, not an L-infinity bound for Leray projection,
controls the mean pointwise. The triangular differentiated amplitude
transport estimates have the same integrable top coefficient; finite
lower-derivative products enlarge E_h without exponentiating it again.
Factors (d/h)^r E_h for differentiated covectors vanish for fixed r>=1.

Consequently, at the required fixed orders,

    ||D^r m||_infinity + ||D^r g_n||_infinity
         <= k^2 d^(-1-r) E_h,
    ||D^r m||_2 + ||D^r g_n||_2
         <= k^2 d^(1/2-r) E_h.

The mean-to-primary forcing has the same bound because
(k^2/d)*k/k=k^2/d. Its cumulative phase effect is small:
T ||m||_infinity/k <= (k/d) E_h=h^(1/4-o(1)).
The constants and time integrals are absorbed in a new subpower E_h.

## 4. Full residual and continuation budget

After the displayed cancellations, each leading uncancelled interaction
is bounded in L2 by k^3 d^(-1/2) E_h. This includes the remaining curl-lift
linear residual, slow primary/harmonic interactions, Z.grad m, and the
mean interaction with corrected harmonics. A genuine fast mean/harmonic
term has size (k^2/d)^2/k times support factor d^(3/2), exactly
k^3 d^(-1/2). Quadratic corrected terms are smaller by k/d. Products of
tangent harmonics do not recover a bare 1/k leading derivative.

The principal viscous term has L2 norm

    epsilon k^(-1) d^(3/2) E_h = h^(35/8-o(1)),

and the mean and harmonic viscous terms are smaller. Thus with the full
pressure above and a possibly enlarged E_h,

    integral_0^T ||partial_t U+U.grad U+grad Pi-epsilon Delta U||_2 dt
          <= k^3 d^(-1/2) E_h = h^(31/8-o(1)).            (R)

No Fourier truncation, discarded mean tail, or viscosity reversal enters
(R). The extra harmonic correction matters: leaving an O(k^2/d) source
uncancelled loses the h^(1/4) that makes the eventual C1 interpolation
positive.

Also

    integral_0^T ||grad U||_infinity dt
       <= C ell + C I_h + h^(1/4-o(1)) = o(ell^2).

Indeed the curl-lift derivatives other than b tensor xi/k are bounded by
(k/d)E_h=o(1), while gradients of m and the lifted g_n are bounded by
(k/d)^2 E_h and (k/d) E_h respectively. Time T is harmless.

Let Q solve exact unforced NS with Q(0)=U(0). On its strong existence
interval w=Q-U is solenoidal and initially zero. Its exact energy estimate is

    d||w||_2/dt <= ||S(U)||_infinity ||w||_2 + ||R||_2.

The w.grad w term cancels in this L2 pairing; this is not a small-gradient
assumption on Z. By (H) and (R),

    ||w||_2 <= h^(31/8-o(1)).

For a separate continuation bootstrap assume ||grad w||_infinity<=1.
The ordinary NS H12 estimate then has accumulated coefficient
C integral ||grad Q|| <= o(ell^2). The initial data and U obey

    ||Q(0)||_{H12}+sup_t ||U(t)||_{H12}
         <= k d^(3/2) k^(-12) E_h = h^(-117/8-o(1)).

The existing first-stage H12 contribution is smaller. Thus Q has the same
H12 bound while the bootstrap holds. Uniform expanding-torus GN gives

    ||grad w||_infinity
       <= C ||w||_2^(19/24)||w||_{H12}^(5/24)
            + C ||w||_2
       <= h^(1/48-o(1)),

since (31/8)(19/24)-(117/8)(5/24)=1/48. Uniform constants follow by applying
unit-scale local Euclidean inequalities on a fixed-size cover, plus the
L2 low-frequency term; the periods are bounded below and grow. This closes
the gradient bootstrap and prevents finite H12 breakdown before T.
The corresponding velocity exponent is 25/16, hence the velocity error is
o(k). This argument proves a finite supplied original-time datum theorem
IF the listed hypotheses on the prepared actual-q branch hold.

## 5. What the mixed target does and does not hand over

At t*, let xi*=4 m*, where (p*,m*,n*) is an orthonormal frame and

    b*/k = P_h p* + N_h n*,  P_h,N_h real,
    |P_h| asymptotic to ell^(11/8),
    |N_h| asymptotic to ell^(7/8).

Here b* is the actual central amplitude, including the envelope, whose
central value is fixed and nonzero; the central real phase is pi/2.
Both components are tangent to xi*. Their combination remains a single
phase, so none of the exact cancellations above changes. At a receiving
particle with phase pi/2 and nonvanishing envelope, its leading symmetric
strain has norm

    |b*| |xi*|/(sqrt(2) k)

for the Frobenius convention S=(grad u+grad u^T)/2. (A smaller fixed
constant is sufficient.) There is no cancellation between orthogonal
p* and n* components in this norm. It is at least c ell^(11/8), larger
than the host O(ell); the correction and tracking errors tend to zero.
The observation is at the reference q particle, not automatically at a
particle of the perturbed Q.

For the ideal late shear, in the (p,n) polarization basis,

    (P,N) -> (P-Theta N,N), |Theta|=O(ell^(1/4)).

Its added p component is only O(ell^(9/8)), compared with pre-existing
ell^(11/8); the relative change is O(ell^(-1/4)). Thus this mixed branch
has no ell^(1/4) relative amplification in that late interval. The normal
component itself remains ell^(7/8), below the host ell. If 'normal handover'
means a normal component larger than the host, these proposed exponents
do not provide it. If it means a transverse finer packet with total strain
larger than the host, they do, already at t*.

Any fine-packet high-pass formulation additionally needs the actual
covector lower bound on its full support and the usual real normalization
and low-frequency leakage estimate. The pointwise strain statement does
not by itself certify a particular spectral cutoff.

## 6. Exact remaining verification line

The limiting outer/inner ODE and its nonzero mixed connection may select
a promising initial branch. They do not yet supply, for one fixed actual
Gavrilov profile as h tends to zero, the following joint assertion:

    ||Z_h(0)||C1=o(1),
    integral_0^T sup_patch |b_h||xi_h|/k = o(ell^2),
    terminal |P_h|>=c ell^(11/8), |N_h|>=c ell^(7/8),

with the uniform finite-jet/envelope bounds in section 2 and a coherent
nonzero real phase. A central small preparation cost is insufficient
without extension across the pulled-back envelope. A uniform actual
history bound O(ell^(11/8)) would settle the difficult integral with room;
there is no need to claim the sharper ell^(7/8) integral now.

Conversely, the generic exp(C ell) history estimate gives only
I_h<=exp(C ell), whose error Gronwall factor is exp(exp(C ell)); it fails
this criterion. This is the precise unresolved line, not an inference
that the mixed branch is impossible. The present result is a nonlinear
budget criterion conditional on actual-profile matching and uniform
history control, not a completed nonlinear compatibility proof.


Source artifact: `nse-mixed-seed-nonlinear-budget-20260908.md`; original SHA-256 `f73cad9f0328f5a0265358d620a7e52b895389e584fe81ee0a09e5104a582ba2`. Local scratch paths and archival status were updated for this copy.


## 7. Independent review record

A separate reviewer rederived the whole-flight mean and harmonic estimates,
full residual, and H12 continuation. A sufficient fixed derivative budget
is q C24, primary b and xi C18 (hence S C19), mean H16, and harmonic
amplitudes C13/H13. The global mean self-product is controlled by its
pointwise norm times its global gradient L2 norm; its tails are retained.
All principal remaining terms are k^3 d^(-1/2); the smaller quadratic
correction and mean terms cost k^4 d^(-3/2). The leading viscous powers
are h^(35/8), h^(37/8), and h^(41/8), all smaller than the main residual.

The review accepted the implication with real primary S,b and a specified
central amplitude at phase pi/2, which are now explicit. It did not prove
small original strain or the history condition for the actual profile.
The [central seed-cost reduction](actual-seed-cost.md) identifies
weighted matching as the remaining task. This is a conditional written
analytic result, not a formal certificate or an actual compatible cascade.

## 8. Transferring a central history bound to the full envelope

**Independently reviewed implication.** See the [inner and envelope review](matching-review.md). The implication in
sections 1–7 requires a whole-support history bound. The positive power
d/h=h^(1/4) permits that bound to be deduced from the central branch once
the fixed-jet estimates of the original preparation have been established.
This section does not assume or prove the missing central matching.

Let t_f=t* and retain the actual q on [0,t_f]. Prescribe at t_f a fixed
real affine phase gradient xi*, with |xi*|=4, and a real tangent vector
c_h satisfying |c_h|<=ell^K for a fixed K. Its normal component will be
one in the application below. On the final radius-d ball define

    S_*(y)=xi*.(y-Y(t_f)),
    b_*(y)=k ell^a chi((y-Y(t_f))/d)c_h,

where chi is fixed, smooth, compactly supported and chi(0)=1. Pull back
S_* by the actual q flow and prepare the tangent amplitude by the inverse
finite-dimensional ODE. At every earlier time write

    b(t,y)=k ell^a chi_t(y) B(t,y),
    chi_t(y)=chi((Phi_q(t_f,t,y)-Y(t_f))/d),
    B(t_f,y)=c_h.

The phase in the real curl lift is theta=S/k+pi/2. Thus its central
phase is pi/2 at every time. Denote central values by B_c(t),xi_c(t).
No inverse viscous evolution occurs in these definitions.

The q-jet hypothesis and integral of m(t) imply, for each fixed required
order, bounds E_h=exp(C ell), with C enlarged finitely many times:

    |B|+|xi|+|xi|^(-1)<=E_h,
    |D^r B|+|D^r xi|<=h^(-r) E_h, 1<=r<=18.

Fixed powers of ell from c_h are absorbed in E_h. These are bounds for
the unweighted polarization B, rather than for the bump times B. They
follow by differentiating the finite-dimensional flow and polarization
equations in the h-scaled coordinates, as in the independently reviewed
original preparation. q C24 has room for these fixed orders. The support
at any time has volume O(d^3) and diameter at most d E_h, by
incompressibility and the integrated Lipschitz bound. In particular it
stays in an embedded local chart because d E_h=o(h).

The mean value theorem on a slightly larger transported phase chart,
or differentiation in final-ball labels, therefore gives

    sup_support(|B-B_c|+|xi-xi_c|)<=(d/h) E_h,
    sup_support ||B||xi|-|B_c||xi_c||<=(d/h) E_h.       (E1)

Every finite product of conditioning factors was absorbed in E_h in
the second line. The transported bump itself is not relatively constant.
Using its fixed supremum, (E1) implies

    sup_support |b||xi|/k
       <=C ell^a |B_c(t)||xi_c(t)|+h^(1/4) E_h.        (E2)

The derivative estimates of chi_t cost d^(-r)E_h. Thus the full amplitude
has exactly the finite pointwise and L2 jet bounds required in section 2;
the L2 support factor is d^(3/2), independent of its distortion. The
slow gradient and curl terms in the real lift Z are at most
(k/d)E_h+(k/d)^2 E_h. Consequently

    ||Z(0)||C1<=C ell^a |B_c(0)||xi_c(0)|+h^(1/4)E_h,
    I_h<=C ell^a integral_0^t_f |B_c||xi_c|dt
                                      +h^(1/4)E_h.   (E3)

The factor t_f=O(log ell) in the second error is again absorbed in E_h.
In particular, a central polynomial history bound is sufficient for this
specific prepared envelope: it is accompanied by an explicit whole-support
comparison, not substituted for one. At t_f the central leading strain
of Z is ell^a|c_h||xi*|/sqrt(2), up to an error tending to zero.

### A sufficient margin for a selected growing branch

Exact row asymptotics of the entire transfer operator are more than is
needed to construct one datum. Suppose an actual central polarization
v_h(t), with |v_h(0)|=1 and the required covector history, satisfies for
some fixed 0<=eta<3/16

    c ell^(3-eta)<=|p.v_h(t_f)|<=C ell^(3+eta),
    c ell^(5/2-eta)<=|n.v_h(t_f)|<=C ell^(5/2+eta),
    sup_[0,t_f] |xi_c(t)||v_h(t)|<=C ell^(3+eta),
    |xi_c(0)|<=C ell.                                (E4)

Let N_h=n.v_h(t_f), take B_c=v_h/N_h, and prescribe
c_h=v_h(t_f)/N_h at the final ball. These vectors are real; N_h need not
be positive, and it is nonzero by (E4). The finite-dimensional inverse
preparation therefore recovers exactly this central branch. It obeys
|c_h|<=C ell^(1/2+2eta), as required above. With a=7/8, (E3) gives

    ||Z(0)||C1<=C ell^(-5/8+eta)+o(1) ->0,
    I_h<=C ell^(11/8+2eta)log ell+o(1)=o(ell^2).       (E5)

At the final center the p component supplies strain at least
c ell^(11/8-2eta)-o(1), which dominates the host's O(ell) strain because
eta<3/16. The history margin only requires eta<5/16 and initial smallness
only eta<5/8; the host comparison is the restrictive one. Exact exponents
without losses are not necessary for this finite nonlinear implication.

Applying sections 1–7 on [0,t_f] would then give an actual smooth NS
solution with the prescribed original seed and the displayed finite
handover. Its initial data still vary with h, and the small C1 statement
concerns the perturbation in rescaled coordinates. These are not small
physical data uniformly at the original viscosity, an infinite cascade,
or a solution of ROOT. The central hypothesis (E4) remains unproved here.
