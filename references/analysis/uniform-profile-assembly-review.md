# Independent review of the growing-window history and continuation assembly

8 September 2026. **PASS conditionally for sections 5–6 and their use of
the stated approximation package.** The growing-order background and
sections 2–4 of the operator construction are separately audited inputs
to this verdict. This review does not itself establish those inputs or
promote the explicit window to a registered theorem. It is an AI-agent
review of written analysis, not external expert acceptance or a formal
PDE certificate. ROOT, E-prime and FORCED-D remain OPEN. No DNS was used.

Reviewed source:
[uniform-profile-window.md](uniform-profile-window.md),
SHA-256:

    08e137749fe30db52751ac4553e82d7ba1e0842b80367d3ebfc0dafe6b2bcb90

This is the version after the author added actual-background comparison
(1b) and the particle/whole-label derivation in section 5. The reviewer
requested that clarification and did not edit the source.

## 1. Conditional inputs and exact scope

The [background note](growing-window-background.md) is
used at SHA
3004a6cd9b1de908d3cf75bcb079140f7cba7de943b5ac9c2586b249096e064f.
Its required inputs include actual q through T, the gradient clock,
weighted derivative estimates, and specifically its q-minus-U_app
comparison. Abstract jet upper bounds alone would not imply a central
lower bound or proximity to the selected model.

The [growing-depth budget](growing-depth-budget.md),
SHA 2a7b8ff6258eb003652d3a3334b41aa135330d21ee1776b9c021b2d9a8977505,
is used for its ordinary relative-energy/H12 implication. This review
independently rechecks its substitution. The other inputs are the
outgoing central theorem and original-time, logarithmic-host and
localized-profile constructions: their particle comparison, normalization,
transported bump, heat profile and sharp clock are used explicitly.

Here eta=ell^(1/16), J=ceil(K eta), N=O(J), with fixed K. The stipulated
logarithmic budget gives

    I_q = O(ell^(19/16)),
    H_N = O_K(ell^(21/16)+ell^(1/4) log ell) = o(ell²).

Thus h^gamma exp(C H_N) tends to zero for fixed gamma>0 and C. Fixed
powers of time, ell and the normalizations are absorbed by a fixed
enlargement of C. An uncontrolled recursive enlargement with J would
not be allowed; the separate operator review must supply the fixed-power
bounds used in this assembly.

## 2. The central comparison keeps a fixed positive h power

Let X(t) be the reference Euler particle through the primary center,
and Y(t) the actual-q particle from that same point. At X(t), the primary
leading velocity vanishes because the phase offset places it at a strain
maximum. Its slow curl and constructed mean/harmonic velocities have size
at most h^(3/2) exp(C T); the steady-background mismatch is smaller.

Together with (1b), this gives

    |q(t,X(t))-V(X(t))| <= h^(5/4) exp(C H_N).

The particle difference equation and actual-q Lipschitz clock then give

    sup |Y-X| <= h^(5/4) exp(C H_N).

At X, the primary leading gradient is precisely
Abar=A_0-ell^(-1) beta tensor N_p. Slow derivatives, mean and harmonic
gradients have smaller positive h powers. The actual gradient comparison
costs h^(1/4) exp(C P_N), with P_N<=C H_N. Moving from X to Y costs the
q Hessian times their displacement. Its h^(-1) changes h^(5/4) to h^(1/4);
the m_h and K_N factors fit exp(C H_N). Hence

    sup |grad q(t,Y(t))-Abar(t)| <= h^(1/4) exp(C H_N).

Unit covector directions and log magnitudes have Lipschitz coefficient
C|A|. The full pressure-corrected polarization equation is linear with
norm controlled by the same clock. Their comparison therefore costs
exp(C I_q), a fixed factor in exp(C H_N). It does not exponentiate a loose
inverse-covector bound. Initial frame rotation, inverse finite preparation
and normalization add fixed factors of this type or fixed powers of ell.
Any smaller fixed gamma, such as 1/8, suffices in the final comparison.

This explains the use of background (1b), rather than trying to recover a
central lower bound from derivative upper bounds. Y is not assumed to be
a particle of the full two-wave Q.

## 3. Whole-envelope history and endpoint strain

The outgoing theorem holds on delta<=tau<=C_0 log ell for one fixed
C_0=1/(4mu). The endpoint tau=3 log ell/(16mu) is inside this horizon.
Its full-vector amplitude/covector comparison has constants independent
of N,J,h. A sign-changing coordinate is not used as a lower bound.

Factor the transported bump out of the unweighted polarization B.
The envelope diameter is at most d exp(C I_q), while the first spatial
derivatives of B and xi cost h^(-1) exp(C H_N). Every label therefore
differs from the center by at most

    (d/h) exp(C H_N) = h^(1/4) exp(C H_N).

Products retain this form after a fixed enlargement of C. The bump is
bounded by its fixed supremum; it is not relatively constant near its
boundary. Thus the whole-support leading strain is bounded by a fixed
multiple of the sharp central signal plus a vanishing absolute error.
The leading signal is not multiplied by exp(H_N).

For the fixed phase profile, heat contraction gives
||F_theta'||infinity<=||F'||infinity. The central heat time
theta<=h exp(C H_N) tends to zero, so F_theta'(0)=1+o(1). The phase stays
zero and the transported bump stays one at the central label. These
fixed profile bounds do not depend on the proof orders.

The slow primary derivatives and exact curl-lift gradient cost at most
rho exp(C H_N)+rho² exp(C H_N). The recurrence's summed new gradients
are at most rho exp(C H_N), with fixed C. Their time integrals vanish
because T=O(log ell). Global means retain their separate global norms.

The outgoing central integral gives B eta ell². The earlier through-focus
history contributes O(ell^(15/8)); it is smaller but does not vanish.
Adding the background clock gives precisely

    integral_0^T ||grad U_J||infinity
      <= B eta ell²+C ell^(15/8)+C I_q+o(1).

At the endpoint the leading symmetric matrix has Frobenius norm
|b_c||xi_c|/(sqrt(2) k), comparable to eta ell². The background gradient
is O(eta ell^(9/8)), with relative size O(ell^(-7/8)). Heat rounding,
slow derivatives and corrections preserve the two-sided comparison.
The location used is the stated q particle.

## 4. Complete loss and ordinary continuation

Conditionally on the uniform recurrence and residual/H12 estimates in
sections 2–4, their logarithmic losses are bounded by C(J+1)H_N. Since
N=O(J), a common valid package loss is

    L_h=C[(J+1)^3(I_q+1)+(J+1)^5 W+ell^(15/8)+1].

The added ell^(15/8) is necessary to include the preceding history in
that package. Direct exponent arithmetic gives

    (J+1)^3 I_q /(eta ell²) = O_K(ell^(-11/16)),
    (J+1)^5 W /(eta ell²)   = O_K(ell^(-7/4) log ell),
    ell^(15/8)/(eta ell²)   = ell^(-3/16).

All vanish. The auxiliary p-form of the sufficient budget can use p=11:
(J+1)^11 eta ell^(9/8) has ell exponent 11/16+19/16=15/8 and dominates
the added history and lower-degree terms. Its condition ap<7/8 is
11/16<14/16. The source's p=11 claim is correct.

The residual exponent (29+2J)/8 and H12 exponent -117/8, interpolated
with weights 19/24 and 5/24, give (19J-17)/96. Writing
Gamma=(19+5C12)/24, the ordinary comparison yields

    log ||grad(Q-U_J)||infinity
      <= -[(19J-17)/96]ell²+Gamma B eta ell²
         +(1+Gamma)L_h+(5C12/24)T+O(1).

For fixed K with 19K/96>Gamma B+2, the terms
L_h=o(eta ell²), T=o(eta ell²), and 17ell²/96 leave the claimed
||grad(Q-U_J)||infinity<=h^eta margin for small h. The extra low-frequency
L2 term has a stronger negative J coefficient. C12 is the fixed H12
energy constant, not a growing derivative-order constant.

The approximation uses independently known q and does not assume
the longer Q lifespan. Its comparison improves a gradient-error bootstrap
on the local strong lifespan; the finite H12 bound for each h supplies
strong continuation through T. This uses ordinary energy growth paid by
a smaller residual, not an assumed polynomial or relative stability bound
for arbitrary PDE errors.

## 5. Datum and review boundaries

The Gevrey-2 fields are chosen once as a subclass of the earlier smooth
construction. This does not certify an unspecified earlier cutoff.
The receiver is prepared using the unchanged t_f and independently
known q. Varying proof order does not alter q or the prepared datum at
a fixed h. Every new correction starts at zero, including its curl lift.

No load-bearing defect was found in sections 5–6 under the explicit
background and uniform-operator inputs. Whether those inputs have been
discharged belongs to their separate reviews. This verdict remains
conditional and does not itself promote eta=ell^(1/16). Even a completed
window is finite for each varying-data member and provides no new phase,
infinite one-datum trajectory or terminal smooth force.

The reviewer independently checked the central comparison, whole-envelope
rather than core estimate, heat and slow-curl terms, all three loss powers,
p=11, the fixed-H12 interpolation and same-datum requirement. Exact
rational arithmetic reproduced the displayed exponents.

