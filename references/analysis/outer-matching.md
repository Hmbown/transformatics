# Full outer polarization matching on one fixed Gavrilov profile

8 September 2026. Independent bounded analytic derivation. The complete central-ODE implication passed a separate agent review;
see the [review record](matching-review.md). No DNS.
ROOT and (E') remain open. It proves an outer ODE estimate, not by itself
an original-time nonlinear NS theorem.

## 1. Profile convention and result

Choose the **unscaled** geometric Gavrilov profile V_j in the oblique
note, with f_j(P_j)=1. Fix one sufficiently large j before sending h
to zero. The L2 normalization used in an older steady-background note
is not imposed here. All constants below may depend on this fixed
profile, but are uniform in terminal orbital phase and in ell.

Use the exact central model and notation of
`references/analysis/actual-seed-cost.md`:

    Abar=A0-ell^(-1) beta tensor N,
    xi=C-fN, C(t)=F(t*,t)^T r_*, r_*=n_* cross p_*,
    f'=-ell^(-1) C.beta, f(t*)=0,
    t*=(2/mu)log ell-ell^(-3/4), u=t*-t.

We use the unit terminal covector r_*; multiplying every covector by
4 changes neither the polarization equation nor any strain ratio.
Here N is the primary covector, beta its growing polarization, and
A0 is the gradient of the exact fixed Euler profile on its reference
particle. The equation being estimated is the full system

    b'=-Abar b+2xi(xi.Abar b)/|xi|^2, xi.b=0.          (1)

Fix any exponent 0<a<1/2, put u_m=ell^(-a), and consider
0<=t<=t_m=t*-u_m. There is a uniformly bounded initial polarization,
specified explicitly below, for which the full solution obeys

    b(t)=L_t B(t) (A(t)X(t), A(t)w(t))^T,
    A(t)=e^(mu t) f(0)/f(t),
    X(t)=1+O(E(t)),
    |w(t)|<=C ell^(-1) rho(u),                         (2)

where L_t is the exact transverse lift, B a bounded primary Floquet
basis, and

    E(t)=ell^(-1)[(1+t*)^2+min(u,1)^(-2)],
    rho(u)=1+u for u>=1, rho(u)=u^(-1) for u<=1.

In particular E(t_m)->0. The full two-dimensional propagator is
controlled in section 5, including the other initial polarization.

Let a_* = r_*.A0(t*)p_*<0, and

    Lambda=|beta(t*)||N(t*)|/ell, R=sqrt(Lambda)u_m.

At the overlap, in the moving primary orthonormal frame (p,r,n),
the solution has

    b_p=[ell f(0)/a_*] u_m^(-2) [1+O(delta_m)],
    b_n=2b_p/(Lambda u_m) [1+O(delta_m)],              (3)
    delta_m=u_m+ell^(-1)[(1+t*)^2+u_m^(-2)].

The common coefficient is positive. Equivalently, the inner variables
V=b_p/sqrt(Lambda), W=b_n satisfy

    V(R)=D_h/R^2 [1+O(delta_m)],
    W(R)=2D_h/R^3 [1+O(delta_m)],
    D_h=ell f(0)sqrt(Lambda)/a_*,
    c ell^(5/2)<=D_h<=C ell^(5/2).                    (4)

For a=3/10, delta_m=O(ell^(-3/10)+ell^(-2/5)) up to
the displayed smaller logarithmic term; R delta_m->0 as well.
Finally, on the entire outer interval,

    |xi(t)||b(t)|<=C ell e^(mu t),
    integral_0^t_m |xi(t)||b(t)|dt<=C ell^3.           (5)

These are estimates for one actual-profile central model, with no
straight-column approximation of its long-time polarization equation.
Only the signs and uniform nondegeneracy inherited by sufficiently thin
fixed profiles are used.

## 2. Exact lift to the receiving orthogonal plane

Write nu_N=|N|, P=I-N tensor N/nu_N^2, c_T=PC, and

    d_f=f nu_N^2-C.N.

On the outer region |C|/|f| is small, uniformly as ell tends to infinity.
Thus |d_f| is comparable to |f| and |xi| is comparable to |f|.
For v in N-perpendicular define

    L_t v=v+N(C.v)/d_f.                               (6)

Then xi.L_t v=0 and P L_t v=v exactly. The lift and its inverse
are uniformly bounded, with L_t-I=O(|C|/|f|).

Let G_N=-A0+2N tensor N A0/nu_N^2 and
H=P(A0^T-A0)N. Differentiating v=Pb in (1), using
N'=-A0^T N and P'N=P A0^T N, gives the exact equation

    v'=G_N v+[1/(ell f)] beta(C.v)+R_t v,              (7)

where

    R_t v = beta (C.N)(C.v)/(ell f d_f)
       +(C.v)H/d_f
       +2c_T/|xi|^2 [xi.A0 v
          +(C.v)(xi.A0 N)/d_f
          -nu_N^2(C.beta)(C.v)/(ell d_f)].             (8)

Every term in (8) lies in N-perpendicular. Formula (8) retains the
complete pressure correction. Its first term comes from the exact
identity nu_N^2/d_f-1/f=(C.N)/(f d_f). In particular that first
term has range precisely along beta, a fact needed below.

## 3. A bounded Floquet frame and the sharper remainder entries

The primary N-polarization system has expanding and contracting
relative Floquet solutions

    beta_+(t)=e^(mu t)B_+(t)=beta(t),
    beta_-(t)=e^(-mu t)B_-(t).

The two columns of B=(B_+,B_-) span N-perpendicular. They and the
inverse coordinate map on that plane are uniformly bounded. Their
physical full-period versions are periodic; in the equivariant E
frame the period is one poloidal circuit. The coefficients and the
fixed finite time derivatives used here are bounded. These statements
follow from the simple hyperbolic monodromy on a fixed poloidal
interval and exact rotational return. In particular no exponentially
ill-conditioned fundamental matrix is used as the coordinate frame.

Put v=B y. Equations (7)-(8) become exactly

    y1'=(mu-f'/f)y1+b12 y2+R11 y1+R12 y2,
    y2'=-mu y2+R21 y1+R22 y2,                         (9)
    b12=e^(mu t)(C.B_-)/(ell f),
    (Rij)=B^(-1) R_t B.

The first row of the reduced rank-one term has been simplified using
f'=-e^(mu t)(C.B_+)/ell. This triangular structure is exact before
estimating the remainder.

For 0<u<=1, the uniform actual-profile geometry gives

    |f| comparable to ell u^2, |xi| comparable to ell u^2,
    |C|<=C, |C.N|<=Cu, |C.B_+|<=Cu,
    |C.B_-|<=C, e^(mu t)/ell<=C ell.                  (10)

The two vanishing scalar products in (10) are exact at u=0, and their
derivatives are bounded. For u>=1, |f| and |xi| are comparable to ell,
|C|<=C(1+u), and e^(mu t)/ell<=C ell e^(-mu u).

Substitution into the exact formula (8) yields, for u_m<=u<=1,

    |R11|+|R21|<=C/(ell u^2),
    |R12|<=C/(ell u^3),
    |R22|<=C[1/(ell u^2)+1/(ell^2 u^5)],
    |b12|<=C/u^2.                                    (11)

To see the potentially dangerous entries, the first term of (8)
has **zero second row**. On B_+ it contains both C.N=O(u) and
C.B_+=O(u), giving O(ell^(-1)u^(-2)); on B_- it gives
O(ell^(-1)u^(-3)). The last pressure term of (8), on B_+, has size
O(ell^(-2)u^(-4)), absorbed into O(ell^(-1)u^(-2)) because ell u^2
tends to infinity throughout the outer interval. On B_- its size is
O(ell^(-2)u^(-5)), which is retained in R22 and is bounded by the
stated R12 bound. The other pressure and normal-lift terms satisfy
the remaining bounds directly.

For 1<=u<=t*, the simpler estimates are

    |Rij|<=C(1+u)/ell,
    |b12|<=C(1+u)e^(-mu u).                           (12)

These entrywise estimates improve the undifferentiated matrix bound
O(ell^(-1)u^(-4)). Discarding the range information in (8) would
hide the useful perturbative structure.

## 4. Exact stable kernel and a closed outer bootstrap

Let f0=f(0), A(t)=e^(mu t)f0/f(t), and set

    y1=A X, y2=A w.

Equation (9) is equivalent to

    X'=R11 X+(b12+R12)w,
    w'=(-2mu+f'/f+R22)w+R21 X.                       (13)

Its scalar stable kernel is explicit:

    K(t,s)=e^(-2mu(t-s)) f(t)/f(s)
                     exp(integral_s^t R22).           (14)

Let theta(u)=min(u^2,1). From (11)-(12), uniformly up to t_m,

    integral_0^t_m |R22|dt
      <=C[(1+t*)^2/ell+1/(ell u_m)+1/(ell^2 u_m^4)]
      =o(1),                                         (15)

because a<1/2. The signed f never vanishes in the outer region and
|f| is comparable to ell theta(u). Thus

    |K(t,s)|<=C e^(-2mu(t-s))theta(u_t)/theta(u_s).     (16)

Specify the initial datum by

    b(0)=L_0 B_+(0),                                  (17)

which is exactly transverse to xi(0), uniformly bounded, and has
coordinates X(0)=1,w(0)=0. Put M(t)=sup_[0,t]|X|. Variation of
constants in the second equation of (13) gives

    |w(t)|<=C ell^(-1)rho(u)M(t).                      (18)

For u>=1 this is exponential convolution of (1+u)/ell. For u<=1,
the earlier part of the integral contributes at most C u^2 M/ell,
and its near-terminal part is bounded by

    C u^2 M/ell integral_u^1 v^(-4)dv<=C M/(ell u).

Substitution of (18) into the first equation of (13) gives

    |X(t)-1|<=C M(t)[(1+t*)^2/ell
                         +1/(ell min(u,1)^2)].        (19)

For completeness, on u<=v<=1 the terms to integrate are bounded by

    M[1/(ell v^2)+1/(ell v^3)+1/(ell^2 v^4)].

The last integral is smaller than C M/(ell u^2), since ell u tends
to infinity. On v>=1, the R11 integral is O(M(1+t*)^2/ell),
the b12*w integral is O(M/ell), and R12*w is still smaller.

The bracket in (19) tends to zero uniformly on the entire outer
interval. Therefore M<=2 for sufficiently large ell, first by a
continuity bootstrap and then throughout the interval. This proves
(2) with constants independent of ell. In particular X is bounded
away from zero; the incoming coefficient cannot disappear.

## 5. Control of the full two-dimensional propagator

The same argument also controls arbitrary initial coordinates
X(0)=x0,w(0)=w0. The homogeneous stable term is K(t,0)w0. Its
contribution to X has the bound

    integral_0^t |b12+R12||K(s,0)|ds
                         <=C(1+t*)/ell.               (20)

Indeed K(s,0) is bounded by C e^(-2mu s)theta(u_s).
On u_s>=1, the R12 contribution is at most C(1+t*)/ell, while
b12 contributes O((1+t*)ell^(-2)). On u_s<=1 one has
e^(-2mu s)<=C ell^(-4), giving respectively the smaller bounds
O(ell^(-5)log(1/u_m)) and O(ell^(-4)).

Consequently, with the same E(t) as in (2),

    |X(t)-x0|<=C E(t)|x0|+C(1+t*)ell^(-1)|w0|,
    |w(t)-K(t,0)w0|
       <=C ell^(-1)rho(u)
                   [|x0|+(1+t*)ell^(-1)|w0|].         (21)

For example, this follows by bounding sup|X| using (20), absorbing
the same small multiple of sup|X| as in (19), and substituting back
into the exact stable-kernel formula. Thus (21) bounds the full
propagator rather than only a guessed leading column. At the
overlap K(t_m,0)=O(ell^(-4)u_m^2), so the normalized map has a
nonzero leading incoming functional converging to (x0,w0)->x0.

The selected column (17) suffices for the finite handover application;
optimization over the whole initial plane is not required.

## 6. Matching the actual moving-frame components

At t* set p_*=beta(t*)/|beta(t*)|, n_*=N(t*)/|N(t*)|,
r_*=n_* cross p_*, and a_*=r_*.A0(t*)p_*.
For the unscaled thin family a_* tends uniformly to -2sqrt(2)/3.
Therefore a_* is bounded above by a fixed negative number for the
chosen sufficiently thin profile, uniformly in terminal phase.

The exact zero C(t*).beta(t*)=0 and the equations for C and beta give

    C(t).beta(t)=2a_*|beta(t*)|u
                              +O(|beta(t*)|u^2),
    f(t)=ell^(-1)a_*|beta(t*)|u^2
                              [1+O(u)].               (22)

The first identity follows by differentiating C.beta:
at t*, its t derivative is -2r_*.A0 beta=-2a_*|beta(t*)|.
The second follows by integrating f'=-C.beta/ell and f(t*)=0.
They are expansions for the actual fixed profile, not the limiting
constant system. Also |beta(t)|/|beta(t*)|=1+O(u), and |N(t)|/|N(t*)|
=1+O(u), uniformly on a fixed short terminal interval.

For the selected solution, its p component in the moving primary
frame follows from (2), since the lift in (6) is parallel to N:

    b_p=(f0/f)|beta(t)|[1+O(E(t))]
                      [1+O(ell^(-1)/u)].

Using (22), this is

    b_p=[ell f0/a_*]u^(-2)
                  [1+O(u+E(t))].                    (23)

Its n component is exactly

    b_n=|N| [C.B_+ X+C.B_- w]A/d_f.

The B_+ contribution is nonzero of order u; the relative B_-
contribution is O(|w|/u)=O(ell^(-1)u^(-2)), already contained in E.
Furthermore d_f=f|N|^2[1+O(ell^(-1)/u)]. Equations (22)-(23)
therefore give

    b_n=[2/(Lambda u)] b_p[1+O(u+E(t))].              (24)

The signs of f0 and a_* are both negative. Hence (23)-(24) have
positive leading coefficients. Substituting u=u_m gives (3)-(4).
The formula supplies both incoming values, including their relative
normalization, rather than inferring W from a separately assumed
inner derivative.

## 7. Outer history and how to use the result

For the selected initial column, X is bounded and w=o(1) uniformly.
The bounded lift and Floquet frame give |b|<=C A. Since

    A is comparable to e^(mu t)/theta(u),
    |xi| is comparable to ell theta(u),

one obtains (5) directly. The corresponding maximum is C ell^3.
This uses cancellation between the covector size and the growing
amplitude's u^(-2) factor. Applying a generic exp(C ell) bound here
would lose the relevant history information.

The independent inner task receives precisely the data in (4), with
R tending to infinity and a common coefficient D_h comparable to
ell^(5/2). If its uniform actual-profile inner connection and history
bound are independently established, they combine with this note to
give one bounded initial polarization whose terminal components have
orders ell^3 along p and ell^(5/2) along n, and whose entire central
history has |xi||b| at most C ell^3. Normalizing its terminal normal
strain to ell^(7/8) would then yield original strain O(ell^(-5/8))
and integrated strain O(ell^(11/8)), with the appropriate additional
short terminal interval accounted for separately.

This final combination still requires the inner estimate, the
actual-q comparison, a uniform center-to-envelope argument, and the
reviewed nonlinear residual/strong-continuation implication. The
present note supplies the full missing outer polarization estimate;
it does not claim those other steps or any infinite cascade.

Six independent scratch symbolic controls checked (6)-(8) for both
vectors of a nontrivial tangent basis, with symbolic f and shear
strength and a nontrivial trace-free A0. The lift was exactly
transverse, the remainder was exactly tangent, and (7) agreed with
direct differentiation of Pb using the full pressure correction.
These are algebra controls; the integral estimates above require the
separate written mathematical review.


## Source and review scope

Original source: `nse-outer-matching-20260908.md`; SHA-256 `ddef81cff3c638061aa2b97250280f734ff3c618955775a7f2890feb703aaacf`. Archival wording and local links have been updated. Mathematical review here means a separate AI-agent derivation audit, not independent expert acceptance or a formal proof certificate.
