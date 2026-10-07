# Growing correction depth: the quantitative continuation budget

8 September 2026. **Reviewed conditional continuation estimate.** The
[budget review](growing-depth-budget-review.md) checks
this implication. The separate [uniform-profile theorem](uniform-profile-window.md)
now discharges its approximation package for the specified fixed Gevrey-2
subclass. The conditional argument below remains useful independently.
The estimate in sections 1–3 is conditional on explicitly stated
approximation bounds. It does not substitute growing indices into the
previous fixed-index theorem. The section 4 hypotheses were subsequently
derived in the separately linked theorem; this abstract implication alone
does not supply them. No DNS, infinite trajectory or global solution claim. ROOT,
E-prime and FORCED-D remain OPEN.

## 1. A sufficient quantitative approximation package

Use the original expanding torus, epsilon=nu h^4 and ell²=log(1/h).
Let eta=ell^a, J=ceil(K eta), with fixed a,K>0. The intended time is

    T_h=t_f+(1/8+a)log(ell)/mu=O(log ell).

For every sufficiently small h suppose a smooth real solenoidal
approximation U_J, with complete pressure, has been constructed on
[0,T_h] from the prescribed original datum. Its spatial mean is zero.
Its complete momentum residual R_J and its actual gradient history satisfy

    U_J(0)=u_h,0,
    integral_0^T ||R_J||2 dt <= h^((29+2J)/8) exp(L_h),
    ||u_h,0||H12+sup_[0,T]||U_J||H12 <= h^(-117/8) exp(L_h),
    I_h:=integral_0^T ||grad U_J||infinity dt
                                  <= B eta ell²+L_h.             (1)

All norms use unnormalized spatial L2. B is fixed independently of h,J.
L_h>=1 is an explicit loss, not unspecified fixed-index notation.
For example, suppose fixed C,p>=0 give

    L_h <= C (J+1)^p eta ell^(9/8)
           +C (J+1)^p log(ell+J+2)+C,                            (2)

and require

    a p < 7/8.                                                   (3)

The construction of U_J must not assume existence of the exact full
solution through T_h. A previously established actual background can be
an input only after its own longer lifetime has been proved.

## 2. Conditional continuation by ordinary energy estimates

The exact local strong NS solution Q_h starts from u_h,0. Put e=Q_h-U_J.
Pressure drops only in the solenoidal L2 pairing; all pressure and
projection terms remain in the field equation. Since e(0)=0,

    ||e(t)||2 <= exp(I_h) integral_0^T ||R_J||2 dt.                (4)

Bootstrap ||grad e||infinity<=1 on the common strong lifespan. The fixed
integer H12 energy inequality gives

    sup||Q_h||H12 <= ||u_h,0||H12
                            exp(C12[I_h+T_h]).

Here C12>=1 is a fixed constant, uniform on tori of side 2pi L, L>=1.
The inhomogeneous version may enlarge the harmless T_h term. It does
not depend on J. Therefore

    ||e||H12 <= 2h^(-117/8) exp(L_h+C12[I_h+T_h]).                 (5)

Fourier splitting/Gagliardo–Nirenberg on these tori gives, with uniform C,

    ||grad e||infinity <= C ||e||2^(19/24)||e||H12^(5/24)
                         +C||e||2.                              (6)

The additive low-frequency term also has the small exponent below.
Combining (1),(4)–(6), and putting Gamma=(19+5C12)/24,

    log||grad e||infinity
      <= -[(19J-17)/96]ell²
         +(1+Gamma)L_h+Gamma B eta ell²
         +(5C12/24)T_h+O(1).                                    (7)

For J=ceil(K eta), condition (3) implies

    L_h/(eta ell²)=O(ell^(ap-7/8))+o(1) -> 0.

Choose once

    19K/96 > Gamma B+2.                                         (8)

Then (7) yields, for sufficiently small h,

    sup_[0,T]||grad(Q_h-U_J)||infinity <= exp(-eta ell²)
                                               =h^eta.         (9)

This improves the bootstrap. The resulting bound on the integral of
||grad Q_h||infinity and the finite H12 bound prevent an earlier strong
endpoint. Thus Q_h exists smoothly through T_h. The velocity error
also tends to zero: the analogous interpolation has H12 weight 1/8,
and its negative coefficient of J is larger than the one in (7).
No affine arbitrary-error bound or relative-stability shortcut is used.

This proves an a posteriori implication from the uniform package (1)–(3).
It is not a reduction of global regularity, nor a proof that the package
holds for the proposed packet.

## 3. What this says about the proposed eta=ell^(1/16) window

For a=1/16, every fixed loss degree p<14 is acceptable in (2).
In particular a bound polynomial in J inside log of the approximation
constant can leave a large margin. Factorial derivative constants by
themselves contribute O(J log J) to that logarithm and need not defeat it.

By contrast, a bound of the form

    log C_(J,h) <= exp(cJ) eta ell^(9/8)

is not covered: for J proportional to ell^(1/16), its right side
eventually dominates J ell². That upper bound's failure is not a
necessary obstruction to the actual solution or to sharper estimates.

Thus a genuinely better full-Q propagator is one possible route, but
not a logically necessary one. A sufficiently accurate, quantitatively
controlled growing-depth approximation can pay the ordinary propagator.
The old theorem had neither a quantitative bound of form (2) nor
permission to assume it.

## 4. Uniform recursive estimate still to discharge

The exact recurrence is already derived in the
[finite-depth source](finite-depth-profile.md).
Its phase mean, longitudinal pressure, normal curl, fast mean advection
and all quadratic products must remain unchanged.

A possible uniform implementation reserves N=N0+8J slow and phase
derivatives and uses one finite hierarchy with orders N-8j at round j.
Let D_(N,h)>=2 bound the following known operators and coefficients in
specified scaled global L2/phase-Wiener norms:

1. Actual-q transport and the solenoidal global mean solver, with their
   differentiated commutators and complete nonlocal pressure.
2. The actual transported phase, its nonzero inverse covector, and the
   pressure-corrected polarization solver with central nonnegative heat.
3. The primary amplitude, curl lift and full smooth phase profile,
   including the original transported envelope.
4. Products, phase averaging, zero-mean phase primitives, up to three
   slow derivatives in a residual round, and pointwise recovery.

Means use global L2 and receive no fictitious compact support. A radius
used to weight derivative norms is not the support radius. Its Sobolev
recovery cost must be included in D_(N,h).

Suppose these explicit operator bounds yield, with fixed b,C,

    F_0 <= C k rho D^b,
    increments at round j <= C D^b F_j,
    F_(j+1) <= C rho D^b F_j + C D^b F_j²/k,                    (10)

where rho=h^(1/4), F_j is the normalized residual amplitude at the
reserved order. Increments in (10) use scaled amplitude norms, before
evaluation at the fast phase. Evaluated velocity gradients cost k^(-1)
times the corresponding coefficient and phase bounds, which are included
in D^b after a fixed enlargement of b>=1. Thus the summed gradient
increments have size O(rho D^(2b)), not O(k rho D^(2b)).
If rho D^(3b) is sufficiently small,
induction absorbs the quadratic term and gives

    F_J <= C k rho^(J+1) (C D^(3b))^(J+1).                      (11)

The same geometric-series estimate keeps the accumulated corrections
small relative to the fixed primary amplitude, so their coefficients
in later rounds do not acquire uncontrolled repeated powers of D.
The step from that estimate to the sharp total gradient clock in (1)
still requires the primary whole-envelope strain history.

For example, the desired coefficient accounting would follow from

    log D_(N,h) <= C[N² I_q+N⁴(1+T_h+log(N+2))],
    I_q <= C eta ell^(9/8)+C log ell,                            (12)

with N=O(J), constants independent of J,h, and the required sharp
primary history. Equations (11)–(12) then give losses bounded by

    C[J³ eta ell^(9/8)+J⁵(1+log ell+log(J+2))],                 (13)

which are o(eta ell²) for a=1/16. This is a quantitative target,
not a bound established by copying fixed-order subpower factors.

The companion
[growing-window background analysis](growing-window-background.md)
examines (12) for a fixed Gevrey-2 choice of the old profiles.
Arbitrary smooth profiles do not automatically satisfy those assumptions.
Those actual-q estimates, the four operator items above, the recurrence
constants and sharp primary history were subsequently checked in the
separate uniform-profile theorem and its linked reviews. This establishes
the finite growing window for that Gevrey subclass, without proving any
global Navier--Stokes target or covering arbitrary smooth cutoffs at this rate.
