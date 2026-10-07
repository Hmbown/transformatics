# Uniform growing-interval inner matching for the central polarization

8 September 2026. Bounded written derivation, independently reviewed by a separate agent;
see the [review record](matching-review.md). No DNS. This closes the inner matching estimate
conditional on the stated outer incoming data. It does not prove those
outer data, the full nonlinear theorem, or ROOT. The profile is the
unscaled geometric V_j with f_j(P_j)=1, not an older L2-normalized profile.
One sufficiently thin j is fixed before ell tends to infinity.

The key estimate is O(Lambda^(-1/2) R), uniformly on 0<=z<=R, rather than
fixed-z convergence. With u_m=ell^(-3/10), Lambda comparable to ell and
R=sqrt(Lambda)u_m, this error is O(ell^(-3/10)). The fixed-profile terminal
coefficients are retained in the inner limit; no O(r_j) coefficient error
is integrated over an interval that grows with ell.

## 1. Exact moving-frame reduction

Along the reference V_j particle use the primary real Floquet solution
beta and covector N, and the moving orthonormal frame

    Q=(p,r,n), p=beta/|beta|, n=N/|N|, r=n cross p.

Let A=Q^T grad V_j Q, a_ij=A_ij, and Omega=Q^T Q'. The exact primary
polarization and cotangent equations imply

    Omega=[[0,a21,-a31],[-a21,0,-a32],[a31,a32,0]],
    D=A-Omega=
       [[a11,a12-a21,a13+a31],
        [2a21,a22,a23+a32],
        [0,0,a33]].                                    (1)

In particular the lower-left two entries vanish exactly. The central
model gradient is A-s e1 tensor e3, where s=|beta||N|/ell. Let u=t*-t,
Lambda=s(t*), epsilon_i=Lambda^(-1/2), z=u/epsilon_i. (epsilon_i is an
inner expansion parameter and is NOT the NS viscosity.) Then

    s(u)=Lambda(1+O(u)),

with fixed-order differentiated versions. The fixed-profile coefficients
and finitely many time derivatives are uniformly bounded, also uniformly
in terminal phase and all sufficiently thin profiles. Lambda is comparable
to ell uniformly under the chosen primary normalization.

Use a unit receiving covector eta(0)=e2. Its backward frame equation is

    eta_u=D^T eta-s e3 eta_1.                           (2)

For the polarization b in this frame the backward equation is

    b_u=H b,
    H=A+Omega-s e1 tensor e3
       -2 eta tensor eta (A-s e1 tensor e3)/|eta|^2.     (3)

The distinction A+Omega versus A-Omega in these two equations is essential.
The entire pressure correction is present in (3).

Set a=a21(t*), c=a31(t*). For the thin limit, direct rotation of the given
matrix by Q gives a=-2sqrt(2)/3 and c=-2sqrt(2)/9. Consequently there is a
fixed sufficiently thin range with

    -C<=a<=-c0<0, -C<=c<=-c0<0                         (4)

uniformly in terminal phase. These actual terminal a,c, rather than their
thin limits, will define the inner equation.

## 2. Uniform cotangent Taylor bounds on the growing interval

Write eta=(x,y,w). The first two equations of (2) do not contain w or s:

    x_u=a11 x+2a21 y,
    y_u=(a12-a21)x+a22 y.

Ordinary fixed-interval Taylor estimates therefore give, throughout
0<=u<=u_m,

    x=2a u+O(u^2), y=1+O(u).

The third equation is linear in w:

    w_u=(a13+a31)x+(a23+a32)y+a33 w-s x.

Its integrating-factor formula gives the stronger parameter-dependent
Taylor estimate

    w=-a Lambda u^2+O(u+Lambda u^3).

These statements have their differentiated Taylor bounds through order
two. In inner coordinates, writing e=epsilon_i,

    x=2a e z+O(e^2 z^2),
    y=1+O(e z),
    w=-a z^2+O(e z+e z^3),
    s=Lambda[1+O(e z)].                                (5)

All constants are uniform as above. For eR=u_m sufficiently small,

    |y|>=1/2,
    |eta|^2 comparable to P(z)=1+a^2 z^4.               (6)

For z>=1 this follows from the relative O(ez) error in w; for z<=1 it
follows from y. Thus (5) is useful all the way to the growing endpoint
R; it is not an invocation of convergence on compact z intervals.

## 3. Full inner coefficient estimate

Eliminate b_r by transversality and set

    b_p=sqrt(Lambda)V, b_n=W,
    b_r=-(x sqrt(Lambda)V+w W)/y.

An exact compact formula for the two-dimensional matrix is

    B=[[1,0],[-x/y,-w/y],[0,1]],
    K=diag(e,1) [H B]_{rows 1,3} diag(1,e).

Equivalently its four entries are e(HB)11, e^2(HB)12,
(HB)31, e(HB)32. This formula specifies every coefficient without
truncating pressure. Substitution of (5) yields

    (V,W)'=(K0+E)(V,W),
    K0=[[0,-1],[(2a^2 z^2+2c)/P,-4a^2 z^3/P]],         (7)

and the following bounds on the entire interval:

    |E11|<=C e,         |E12|<=C e(1+z),
    |E21|<=C e/(1+z),   |E22|<=C e.                    (8)

For scalar reduction below one also has

    |E11'|<=C e/(1+z),  |E12'|<=C e.                   (9)

These bounds can be verified directly from the displayed exact rational
matrix. Here are the cancellations and sizes which avoid a spurious
large remainder. All denominators are y(x^2+y^2+w^2). The (3,1) numerator
is exactly

    -2[a11 x y w-a12 x^2 w+a21 y^2 w-a22 x y w
        -a31 x^2 y-a31 y^3+a32 x^3+a32 x y^2].

Its leading terms are -2a w+2c, divided by P. Every remaining term is
O(e/(1+z)); in particular xw/P=O(e/(1+z)). Thus no O(ez) contribution
survives in E21. The leading s term in the (1,2) entry is -s(1-2x^2/|eta|^2),
which, after multiplication by e^2, is -1+O(ez)+O(e^2). Its other terms
are bounded by C e^2(1+z^2)<=C e(1+z). The leading s term in the (3,2)
entry is 2s xw/|eta|^2, giving -4a^2z^3/P after multiplication by e;
its relative geometric error contributes O(e), not O(ez^2).
The background (3,2) terms are bounded after pressure cancellation:
terms involving a32 w^2 cancel and leave terms of size O(1+|x|).
The (1,1) background entry is also bounded by C(1+|x|).
Differentiating these rational expressions and (5) gives (9).
This verification uses |a| bounded below and eR small, not a profile
parameter tending to zero with ell.

## 4. Uniform frozen connection, for each actual terminal phase

The first row of K0 is V'=-W. Hence

    (P V')'+(2a^2 z^2+2c)V=0.                          (10)

Let g=P^(-1/2), V=g Y. Direct differentiation gives

    Y''=q(z)Y,
    q(z)=[4a^2 z^2-2cP]/P^2>0.                        (11)

Uniformly for the compact coefficient set (4), q is bounded near zero
and O((1+z)^(-4)) at infinity. The branch Y(infinity)=1,
Y'(infinity)=0 is the positive Volterra series

    Y(z)=1+integral_z^infinity (s-z)q(s)Y(s) ds.

Its kernel moment integral_0^infinity s q(s)ds is uniformly finite, so
1<=Y<=C. Moreover -Y'(0)=integral_0^infinity qY>=c1>0 uniformly: the
positive term -2c/P alone supplies a lower bound on any fixed small
interval. Since g(0)=1 and g'(0)=0, this selected branch satisfies

    V(0)>=1, W(0)=-V'(0)>=c1.                         (12)

At large R,

    Y(R)=1+O(R^(-2)), Y'(R)=O(R^(-3)),
    V(R)=1/(|a|R^2)[1+O(R^(-2))],
    W(R)=2/(|a|R^3)[1+O(R^(-2))].                     (13)

All constants, including the positive connection, are uniform in the
terminal phase of the fixed sufficiently thin profile.

## 5. Perturbation on 0<=z<=R, without losing powers of R

Write the full system (7) as V'=alpha V+beta W,
W'=gamma V+delta W. By (8), beta=-1+E12 stays bounded away from zero.
Eliminate W exactly:

    V''=(alpha+delta+beta'/beta)V'
          +(alpha'+beta gamma-alpha(delta+beta'/beta))V.

Using (8)-(9), (7), and g'/g=O((1+z)^(-1)), the substitution V=gY gives

    Y''=qY+r1 Y'+r0 Y,
    |r1|<=C e, |r0|<=C e/(1+z).                       (14)

For example E12 times the frozen gamma is O(e/(1+z)), because
|gamma0|<=C/(1+z)^2. The alpha delta term has the same bound. Thus an
unweighted exponential exp(C R), or an exponentiation of a growing
condition number, is unnecessary.

Use the norm on [0,R]

    ||Y||_X = sup |Y(z)| + sup (1+z)|Y'(z)|.

For the backward terminal problem, integrate twice from R. The free
terminal affine function has X norm bounded by
C(|Y(R)|+(1+R)|Y'(R)|). The Volterra resolvent for q is uniformly bounded
in X: its undifferentiated iterates are bounded by the exponential of
the finite kernel moment; differentiation and
sup_z (1+z) integral_z^infinity q(s)ds<infinity give the derivative bound.

The perturbing integral operators from r0 and r1 have X norm at most
C e(1+R). Indeed their undifferentiated bounds use

    integral_0^R s |r0(s)| ds <= C e R,
    integral_0^R s |r1(s)|/(1+s) ds <= C e R.

For derivatives use
(1+z) integral_z^R (1+s)^(-1)ds <= C(1+R), and the stronger
integrable kernel for the r1Y' term. A Neumann inversion around the
uniform q-resolvent is therefore valid for eR sufficiently small.
It proves uniform full transfer in X and an O(e(1+R)) difference from
the frozen transfer with the same terminal Y,Y'. Equivalently this is
a uniformly bounded backward propagator in the smooth amplitude weights
((1+z)^2 V,(1+z)^3 W).

This is the missing growing-interval estimate. It applies to arbitrary
terminal data in the weighted two-dimensional space, although only one
selected branch is needed for the construction.

## 6. Incoming data and the nonzero connection

Suppose the outer argument supplies a real selected branch and a positive
normalizing coefficient D_ell such that at the overlap

    V(R)=D_ell R^(-2)(1+O(delta_ell)),
    W(R)=2D_ell R^(-3)(1+O(delta_ell)),
    delta_ell ->0.                                    (15)

No separate full endpoint-row asymptotic is needed. The corresponding
terminal data for Y differ from the frozen infinity-normalized branch
multiplied by |a|D_ell by at most

    C D_ell[delta_ell+R^(-2)+e(1+R)]

in the terminal norm |Y(R)|+(1+R)|Y'(R)|. The eR term includes the
exact conversion V'=alpha V+beta W; it would be missed by replacing
V' with -W in the finite-parameter equation at R.

Combining sections 4 and 5 gives on the full inner interval

    ||(Y,Y')-|a|D_ell(Y_frozen,Y'_frozen)||_X
       <= C D_ell[delta_ell+R^(-2)+e(1+R)].             (16)

In particular, for all sufficiently large ell,

    c D_ell <= V(0) <= C D_ell,
    c D_ell <= W(0) <= C D_ell.                        (17)

The conversion from V'(0) to W(0) contributes only O(eD_ell).
At overlap exponent 3/10, R comparable to ell^(1/5), R^(-2)=O(ell^(-2/5)) and
eR=O(ell^(-3/10)). Thus an o(1) relative weighted overlap mismatch is
sufficient; no requirement delta_ell R ->0 occurs.

If the outer coefficient has D_ell comparable to ell^(5/2), (17) gives
terminal b_p comparable to ell^3 and b_n comparable to ell^(5/2), both
nonzero and with the selected positive sign. Bounds with small powers
ell^(+/-delta) transfer just as directly.

The full weighted upper bound also gives the needed inner history budget.
From (5), transversality, and (16),

    |b_p(z)| <= C sqrt(Lambda) D_ell/(1+z)^2,
    |b_n(z)| <= C D_ell/(1+z)^3,
    |b_r(z)| <= C D_ell/(1+z),
    |eta(z)| <= C(1+z)^2.

Since z<=R and R/sqrt(Lambda)=u_m->0, these imply

    sup_inner |eta| |b| <= C sqrt(Lambda) D_ell.        (18)

For D_ell~ell^(5/2) this is O(ell^3). After the proposed normalization
ell^(-13/8), it is O(ell^(11/8)). The inner time integral is smaller by
u_m, although the outer estimate must still control the preceding history.
The unit versus length-four terminal covector only changes fixed constants.

## 7. Scope and remaining assembly

This derivation proves an inner transfer implication with uniform actual
terminal coefficients and a growing overlap. It leaves the proof of (15)
and its initial normalization to the outer argument. The exact central
actual-q versus matrix-model comparison in actual seed cost has error
h^c exp(C ell); it can transfer polynomial bounds once the two regions
have been assembled. Root separately handles the uniform envelope
extension. Neither central matching alone nor the current note is a
nonlinear original-time compatibility theorem.

Independent exact algebra checks used during this derivation:
the recorded local calculation constructs (3), eliminates b_r, and prints
all four rational entries; direct symbolic rotation of the thin A matrix
by its (p,r,n) frame gives a=-2sqrt(2)/3 and c=-2sqrt(2)/9. These checks
support the written identities, not an independent audit of the analytic
bounds (8)-(16). No numerical integration or DNS was used.


## Source and review scope

Original source: `nse-inner-matching-20260908.md`; SHA-256 `4a6141c49776a9ab17d28121a9f602a2452f5f9fce46a1709ab428971962dcc8`. Archival wording and local links have been updated. Mathematical review here means a separate AI-agent derivation audit, not independent expert acceptance or a formal proof certificate.
