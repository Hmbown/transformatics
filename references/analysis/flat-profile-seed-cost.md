# Flat periodic profiles do not remove the full-support seed cost

Independent bounded analytic audit, 8 September 2026. No DNS. Inputs are the [flat-core check](viscous-flat-core.md), [sinusoidal seed-cost proof](smooth-seed-supply.md), and sections 4–5 of the [original-time theorem](../navier-stokes/original-nonlinear-handover.md).

**Result.** For the actual prepared phase chart and transported plateau, replacing the sinusoid by any fixed smooth periodic profile F that equals s near zero retains the original C3 lower bound somewhere inside the plateau. A center-only test misses that point. Confining the entire support to the flat phase interval transfers this cost to localization, provided the prescribed central strain is retained. These are kinematic results with explicit support hypotheses, not an extension of the nonlinear handover theorem to arbitrary F or an obstruction to all generated/inherited seeds.

## 1. Initial geometry and the generalized curl packet

Use the original theorem's rescaled coordinates y and

    ell=sqrt(log(1/h)), k=h^(3/2), d=h^(5/4),
    a_h=k ell^(-13/8), E_h=exp(C ell)=h^(-o(1)).

At the original central point y0, S(y0)=0, xi=grad S, |xi(y0)| comparable to ell, and the real tangent amplitude satisfies |b(y0)| comparable to a_h. The transported bump equals one on a neighborhood of y0. Quantitatively, the final fixed bump has a plateau ball of radius c d, and the actual q flow and inverse flow have Lipschitz bounds E_h. Its initial plateau therefore contains a ball of radius c d/E_h around y0. Enlarge C finitely as needed. This inner inclusion follows from the flow map, not just the upper bound on support diameter.

On this initial chart the fixed jets give

    |D^r b| <= a_h d^(-r) E_h (0<=r<=4),
    |D^r xi| <= h^(-r) E_h (1<=r<=4),
    |xi|+|xi|^(-1)<=E_h.

Using a_h instead of k in the first bound absorbs a power of ell into E_h. The sharp central nonzero amplitude estimate remains separate.

Let F be fixed, real, smooth, odd and P-periodic, with F(s)=s on |s|<a<P/2. Let Q be a fixed periodic primitive, Q'=F, with any fixed additive constant. Put

    theta=S/k+theta0, C=-(xi cross b)/|xi|^2,
    Z=k curl[C Q(theta)] = b F(theta)+k (curl C)Q(theta).       (1)

Extend the potential by zero from the same embedded chart. This identity is exact, including cutoff derivatives; it ensures divergence freedom only. Set D_c=curl C, with |D^r D_c|<=a_h d^(-1-r)E_h for r<=3.

## 2. A non-flat phase is reached inside the actual plateau

Some phase theta_* has F'''(theta_*)!=0. Otherwise F is a quadratic polynomial, and periodicity forces it to be constant, contradicting F'=1 in the core. Choose such a phase with a representative |theta_*-theta0|<=P. Constants depending on this choice are fixed before h tends to zero.

Freeze e=xi(y0)/|xi(y0)|. On y=y0+t e, |t|<=C_F k/ell,

    xi(y).e=|xi(y0)|+O(h^-1 E_h k/ell)
            =|xi(y0)|(1+o(1)).

Thus theta is strictly increasing. Taking C_F sufficiently large, the intermediate value theorem supplies y_* on this segment with theta(y_*)=theta_* modulo L. The segment stays in the plateau since

    (k/ell)/(d/E_h)=h^(1/4)E_h/ell ->0.

Also |b(y_*)-b(y0)|<=a_h d^-1 E_h O(k/ell)=o(a_h), and xi(y_*).e is comparable to ell. The amplitude is nonzero at the selected non-flat phase. This is an argument about the actual transported phase and amplitude, not an affine replacement. Even the guaranteed inner plateau covers increasingly many phase periods.

## 3. Exact third derivative and errors

Primes denote derivatives in the fixed direction e; q=theta'. At y_* exact differentiation gives

    (b F(theta))''' = b F''' q^3
       +3 b' F'' q^2 +3 b F'' q theta''
       +3 b'' F' q +3 b' F' theta''
       +b F' theta''' +b''' F.                              (2)

The full curl term is

    (k D_c Q(theta))''' = k [D_c''' Q+3D_c'' F q
       +3D_c'(F' q^2+F theta'')
       +D_c(F'' q^3+3F' q theta''+F theta''')].               (3)

All profile derivatives and Q are bounded fixed numbers. For v=b(y_*)/|b(y_*)|, the leading scalar magnitude is comparable to

    a_h ell^3/k^3=k^-2 ell^(11/8).                           (4)

The six nonleading terms in (2), in printed order, have relative h-power factors

    h^(1/4), h^(1/2), h^(1/2), h^(3/4), h, h^(3/4),

up to E_h and fixed powers of ell. For example the first is (k/d)/ell and the phase-curvature term is k h^-1/ell^2. The seven expanded terms in (3), in printed order, have factors

    h, h^(3/4), h^(1/2), h, h^(1/4), h^(3/4), h^(5/4),

again up to E_h and powers of ell. The last factor is k^3 d^-1 h^-2. The total relative error is O(h^(1/4)E_h)=o(1), after enlarging C. A small but fixed nonzero F'''(theta_*) is harmless. Consequently

    ||D^3 Z||_infinity >= |v.partial_e^3 Z(y_*)|
                         >= c_F k^-2 ell^(11/8).            (5)

The flat center and a fixed phase shift do not remove the full-support bound. Phase coverage and nonvanishing amplitude are essential hypotheses; (5) is not a claim about arbitrary envelopes chosen to avoid all nonlinear phases.

## 4. Confining the entire descendant to the flat core

A general localization lemma bypasses small-error approximations. Let Z be C3 and vanish beyond an exit point y0+w e on a straight segment, with first and second derivatives zero there. If a unit v satisfies |v.partial_e Z(y0)|=g>0, Taylor's formula for f'=partial_e(v.Z) about the exit gives

    g <= (w^2/2) sup_segment |v.partial_e^3 Z|,
    ||D^3 Z||_infinity >= 2g/w^2.                           (6)

Smooth compact support supplies the zero derivatives at the exit. This argument does not separate the curl correction from the leading wave.

Suppose the whole support lies in one flat phase slab |S/k|<a, S(y0)=0, and xi.e>=c ell out to distance C a k/ell. The ray must leave the slab by w<=C a k/ell, where Z vanishes. Retaining g>=c a_h ell/k therefore forces

    ||D^3 Z||_infinity >= c a_h ell^3/k^3
                         =c k^-2 ell^(11/8).               (7)

An anisotropic envelope does not evade this: its phase-normal thickness suffices. For the natural primitive gauge Q(0)=0 and phase theta=S/k, F(0)=0 and F'(0)=1. Differentiating (1) at the center yields exactly

    partial_e Z(y0)=b(y0)(xi(y0).e)/k.

The curl correction and its first derivative vanish there because Q(0)=Q'(0)=0. Thus the required g is exact in this gauge. A different primitive constant changes the localized velocity and can affect g; the gauge-independent statement is (6) for the actual retained strain. Canceling g does not evade the lemma while preserving its hypothesis.

At width w~k/ell the ordinary small-envelope parameter k/(|xi|w) is order one. Discarding the curl correction by the old broad-envelope estimate is invalid. Formula (6) remains exact and shows where the derivative cost moves.

If only the observed descendant region lies inside a flat core while the full parent extends beyond it, no cutoff need occur inside that observation. Then (6) need not apply to that observed region. The complete parent's transitions still count toward a global initial-data norm, or a new larger-scale/global construction must be supplied. A local affine jet alone has D3=0 and implies no such lower bound.

## 5. Scope, attenuation and common coordinates

For translated/rotated copies in one common compact domain, either (5) or (7) gives the previous restricted obstruction: a disjoint superposition, or one satisfying explicit quantitative noncancellation at the selected points, cannot be C3 when the individual lower bounds diverge. Local equality in each packet interior suffices; no termwise differentiation of an infinite series is assumed. Arbitrary mutual cancellation and centers escaping compact sets on R3 are not excluded.

Attenuation eta compatible with bounded C3 necessarily satisfies

    eta <= C k^2 ell^(-11/8).

If a separate transfer theorem retains the existing polynomial terminal strain eta ell^(11/8), this makes it at most C k^2. This conditional comparison does not extend the sine-wave nonlinear proof automatically to a general profile or core-sized cutoff: extra harmonics and the changed localization budget require proof.

For W(x)=A Z(s(x-x0)), the lower bound becomes A s^3 k^-2 ell^(11/8), while strain gains A s. The original physical conversion A=h^-14, s=h^-10 again gives h^-47 ell^(11/8). Time, viscosity and support must be transformed consistently; separately rescaled finite solutions are not one fixed datum.

A fixed flat profile thus repairs neither the broad prepared packet's global smoothness cost nor a compact core-confined packet retaining its initial strain. Generated or inherited flat regions may still help dynamically, but their construction, full-support norms and transfer estimates are separate obligations. No universal cascade impossibility or ROOT conclusion follows.


## Review provenance

[Independent review record](profile-extension-review.md). Original reviewed source `nse-flat-profile-seed-cost-20260908.md`, SHA-256 `23f71b2879984651f720986481f749f8516a25b35718aba6610846418bff70b1`. Archival changes resolve links and current-scope wording; they do not replace a formal PDE certificate.
