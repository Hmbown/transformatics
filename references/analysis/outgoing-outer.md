# The outgoing receiver beyond its focus: a nonzero outer connection

8 September 2026. Bounded analytic calculation for the **full central
polarization ODE**, including its pressure projection, on one fixed actual
Gavrilov profile. The signed matching and full outgoing perturbation passed
a separate AI-agent derivation review. This note continues the original
incoming branch; it does
not select a new outgoing datum. It does not by itself prove a nonlinear
Navier–Stokes continuation, generate a seed, or close ROOT or FORCED-D.
No DNS is used.

## 1. Precise central statement

Use the profile, primary Floquet normalization and original receiving branch
of [the outer matching note](outer-matching.md). Write

\[
 t_f=(2/\mu)\log\ell-\ell^{-3/4},\quad
 \tau=t-t_f,\quad s_*=e^{\mu t_f}/\ell\asymp\ell,
 \quad D_h\asymp\ell^{5/2}.
\]

The symbol \(D_h\) is the incoming inner normalization in that note, not a
new choice of amplitude. Fix one sufficiently thin **unscaled** actual
profile before taking \(h\to0\). There are fixed numbers \(\delta>0\),
\(\tau_0>\delta\), and positive constants independent of \(h\), such that
its continued central solution satisfies

\[
 |\xi(t_f+\tau)|\asymp s_*(1+\tau)e^{\mu\tau},\qquad
 |b(t_f+\tau)|\asymp \frac{D_h}{1+\tau},
 \quad \delta\le\tau\le L_\ell,                         \tag{1}
\]

where \(L_\ell=C_0\log\ell\) for any fixed \(C_0>0\). The constants in
(1) may depend on \(\delta,C_0\) and the fixed profile. The first comparison
on the bounded interval \([\delta,1]\) incorporates the fixed factor
\(\delta^2\); the sharper small-time covector size is \(s_*\tau^2\).

For the original physical normalization of this receiving packet,
\(b_c=(k\ell^{7/8}/N_h)b\), \(N_h\asymp D_h\), the consequence is

\[
 \frac{|\xi_c(t_f+\tau)||b_c(t_f+\tau)|}{k}
       \asymp \ell^{15/8}e^{\mu\tau},
       \qquad \delta\le\tau\le L_\ell.                \tag{2}
\]

Multiplying the unit terminal covector used in the calculation by four, as
in the packet construction, changes only fixed constants. The lower bound
in (2) concerns the whole polarization. Its growing Floquet coordinate
changes sign, so a claim that this one coordinate stays positive is false.

For any fixed \(0<\eta\le1\), set

\[
 L_{\ell,\eta}=\frac{\log\ell}{8\mu}+\frac{\log\eta}{\mu}.
                                                               \tag{3}
\]

For sufficiently large \(\ell\) it is positive and exceeds \(\tau_0\).
The central endpoint strain is then between \(c\eta\ell^2\) and
\(C\eta\ell^2\). Its whole central strain history obeys

\[
 \int_0^{t_f+L_{\ell,\eta}}
       \frac{|\xi_c(t)||b_c(t)|}{k}\,dt
       \le C\eta\ell^2+C\ell^{15/8}.                  \tag{4}
\]

The constants in (4) can be chosen independently of \(\eta\in(0,1]\);
the threshold for \(\ell\) may depend on \(\eta\). This dependence matters
if a separate full-PDE argument spends a small multiple of \(\ell^2\) in
its stability exponent. Equation (4) is not itself that argument.

## 2. Exact outer equation and future profile geometry

All following equations are for

\[
 \overline A=A_0-\ell^{-1}\beta\otimes N,\qquad
 \xi=C-fN,\qquad C=F(t_f,t)^Tr_*,
 \quad f'=-\ell^{-1}C\cdot\beta,
 \quad f(t_f)=0.
\]

Retain the exact lift \(L_t\), transverse basis \(B=(B_+,B_-)\), and
the full remainder \(R_t\) in equations (6)–(9) of the incoming outer
note. With \(b=L_tB(y_1,y_2)^T\), the exact system is

\[
 y_1'=(\mu-f'/f)y_1+b_{12}y_2+R_{11}y_1+R_{12}y_2,
 \quad y_2'=-\mu y_2+R_{21}y_1+R_{22}y_2,             \tag{5}
\]

\[
 b_{12}=s_*e^{\mu\tau}(C\cdot B_-)/f.
\]

In particular the stable coordinate is present. Discarding its forcing of
\(y_1\) discards the leading outgoing connection.

The exact action-angle shear formula (12) in
[the seed-cost note](actual-seed-cost.md), now with signed
time difference \(-\tau\), gives uniformly in both orbital phases
the following bounds, derived in full in
[the future-covector note](future-covector.md):

\[
 |C|\le C(1+\tau),\quad
 C\cdot B_+=2\tau+O(r_j\tau),\quad
 C\cdot B_-=2\tau-2/3+O(r_j(1+\tau)).                 \tag{6}
\]

Here \(r_j\to0\) is the thin-profile parameter; it is fixed, not sent to
zero with \(h\). These are coefficient estimates from the exact nilpotent
action shear, not the integration of an \(O(r_j)\) coefficient error over
a growing interval. The primary exponent is \(\mu=2/3+O(r_j)\).
For the first estimate of a vanishing pairing, \(C\cdot B_+(0)=0\)
exactly, and the bounded nonshear contribution has size
\(O(r_j\min(\tau,1))\). Thus the error in that pairing has the displayed
\(\tau\) factor even near zero. It follows by integrating \(f'\) that

\[
 f<0\ (\tau>0),\qquad
 |f|\asymp s_*\tau^2\quad(0<\tau\le1),\qquad
 |f|\asymp s_*(1+\tau)e^{\mu\tau}\quad(\tau\ge1).
                                                               \tag{7}
\]

The model profile proof uses the one fixed sufficiently thin member. No
uncontrolled straight-column approximation over \(\log\ell\) is used.

## 3. The inner connection supplies a stable outgoing component

Use [the through-focus calculation](longer-host-attempt.md),
with \(a=a_{21}(t_f)<0\), \(\Lambda\asymp\ell\), and let \(Y_+\) be
its infinity-normalized solution \(Y_+(+\infty)=1\). Define

\[
 \mathfrak b=|a|\left[-\lim_{z\to-\infty}Y_+'(z)\right]>0.
\]

The factor \(|a|\) is essential: the incoming outer coefficient is
\(V(R)\sim D_h/R^2\), so its inner scalar solution is
\(|a|D_hY_+\), as recorded in equation (16) of the inner matching note.
The coefficient \(\mathfrak b\) is uniformly bounded above and below as
the terminal phase varies. In the overlap
\(\ell^{-1/2}\ll\tau\ll1\), its signed
asymptotics, retaining the covector and transversality, give

\[
 b_p=\frac{\mathfrak bD_h}{|a|\tau}(1+O(\tau)+o(1)),
 \quad
 b_n=-\frac{\mathfrak bD_h}{|a|\Lambda\tau^2}
                                      (1+O(\tau)+o(1)),
 \quad b_r=-\mathfrak bD_h(1+O(\tau)+o(1)).            \tag{8}
\]

For the last identity, the exact covector expansion is
\(x=-2a\tau+O(\tau^2)\),
\(w=-a\Lambda\tau^2(1+O(\tau))+O(\tau)\), \(y=1+O(\tau)\).
The identity \(b_r=-(xb_p+wb_n)/y\) combines the leading terms
\(2\mathfrak bD_h\) and \(-\mathfrak bD_h\). Their sum does not vanish.
The \(O(\tau)\) errors in (8) follow from the outgoing weighted Volterra
norm and its differentiated equation; using only an unweighted amplitude
bound would not suffice for the signed \(b_n\) estimate.

Normalize the thin stable vector as

\[
 B_-=(1,-1/3,-c/6),\quad c=1/\sqrt2.
\]

In the primary orthonormal frame, \(r\cdot B_-=-2/3\); for the actual
profile it is \(-2/3+O(r_j)\), uniformly in phase. Since \(B_+\) is
parallel to \(p\) and the lift adds only a normal component, (8) implies
at any fixed sufficiently small \(\delta>0\)

\[
 y_2(\delta)=D_h\big[\tfrac32\mathfrak b
                    +O(\delta)+O(r_j)+o(1)\big]>cD_h,
 \quad |y_1(\delta)|\le C D_h/\delta.                 \tag{9}
\]

The order of choices is: choose a sufficiently thin fixed profile, then a
sufficiently small fixed \(\delta\), then sufficiently large \(\ell\).
There is no new polarization selected at \(\delta\).

## 4. Exact thin calculation: the signed coefficient is nonzero

This section calculates a coefficient, whose persistence for the actual
profile and full equation is established below. In the thin reduced system
\(\mu=2/3\), \(C=r_0+2\tau e_1\), and

\[
 C\cdot B_-=2\tau-2/3,\qquad
 f=-\frac92s_*[1+(\mu\tau-1)e^{\mu\tau}].
\]

The outgoing initial trace is
\(y_2=M e^{-\mu\tau}\), \(M=(3/2)\mathfrak bD_h\), and
\(f e^{-\mu\tau}y_1\to0\) as \(\tau\downarrow0\). Thus (5), with
\(R=0\), gives exactly

\[
 f e^{-\mu\tau}y_1=s_*M I(\tau),\qquad
 I(\tau)=\int_0^\tau(2s-2/3)e^{-\mu s}\,ds
 =\frac72-(3\tau+\tfrac72)e^{-2\tau/3}.               \tag{10}
\]

In particular \(I(\infty)=7/2>0\). It first decreases, then increases,
and has one positive zero after \(\tau=1/3\). At that zero \(y_1=0\)
but \(y_2=M e^{-\mu\tau}>0\); the full velocity does not vanish.
At large \(\tau\),

\[
 y_1=-\frac{7}{4}\frac{\mathfrak bD_h}{\tau}(1+o(1)),
 \qquad y_2=\tfrac32\mathfrak bD_h e^{-2\tau/3}.        \tag{11}
\]

The inverse-linear outgoing velocity and exponential covector growth
therefore coexist. The mechanism for (2) is compression, not exponential
velocity growth.

## 5. Full pressure is a controlled perturbation on the outgoing interval

All terms of the exact remainder (8) in the incoming outer note remain
present. On a fixed \([\delta,1]\), their coefficients obey
\(\|R\|\le C_\delta/\ell\). On \(\tau\ge1\), (6)–(7),
\(|\beta|\le C\ell^2e^{\mu\tau}\), and \(|d_f|\asymp|f|\) give

\[
 |R_{ij}(\tau)|\le C\ell^{-1}e^{-\mu\tau}.           \tag{12}
\]

For example the first rank-one term costs
\(|\beta||C|^2/(\ell|f|^2)\le C\ell^{-1}e^{-\mu\tau}\),
the normal-lift term costs \(C|C|/|f|\), and the first pressure term costs
the same. The remaining pressure terms have the smaller bound
\(C\ell^{-2}e^{-2\mu\tau}\). This estimates the entire pressure
projection, not just the principal rank-one term.

Introduce the outgoing weights

\[
 Z=\frac{f e^{-\mu\tau}y_1}{s_*D_h},\qquad
 V=\frac{e^{\mu\tau}y_2}{D_h}.
\]

Equation (5) becomes exactly

\[
 Z'=R_{11}Z+
 \left[(C\cdot B_-)e^{-\mu\tau}
       +\frac{f e^{-2\mu\tau}}{s_*}R_{12}\right]V,
\]
\[
 V'=R_{22}V+\frac{s_*e^{2\mu\tau}}{f}R_{21}Z.          \tag{13}
\]

For \(\tau\ge1\), the principal coefficient in the first equation is
bounded by \(C(1+\tau)e^{-\mu\tau}\), integrable on the whole half-line.
Its additional coefficient is at most
\(C\ell^{-1}(1+\tau)e^{-2\mu\tau}\). The coefficient of \(Z\) in the
second equation is bounded by
\(C/[\ell(1+\tau)]\). Consequently, for \(L\le C_0\log\ell\), the
total perturbation of this triangular integrable system is at most

\[
 \varepsilon_\ell=C_{\delta,C_0}
                       \frac{1+\log(1+L)}{\ell}=o(1). \tag{14}
\]

Variation of constants and a two-component Gronwall estimate bound the
**full two-dimensional propagator** in these weights:
\(\sup(|Z|+|V|)\le C(|Z(\delta)|+|V(\delta)|)\), for arbitrary initial
coordinates at \(\delta\). Applying that estimate to the selected branch
and its difference from the reduced triangular solution gives

\[
 |Z|+|V|\le C,\quad V(\tau)=V(\delta)+O(\varepsilon_\ell),
\]
\[
 Z(\tau)=Z(\delta)+V(\delta)
       \int_\delta^\tau(C(s)\cdot B_-(t_f+s))e^{-\mu s}ds
       +O(\varepsilon_\ell).                         \tag{15}
\]

The initial values from (9) satisfy \(|Z(\delta)|\le C\delta\) and
\(V(\delta)\ge c>0\). Equations (6) and (10) show uniformly in terminal
phase

\[
 \int_\delta^\infty(C\cdot B_-)e^{-\mu s}ds
          =\frac72+O(\delta)+O(r_j).                  \tag{16}
\]

Thus the limiting connection in (15) is bounded below by a positive
constant after the stated choices of profile and \(\delta\). Its tail is
uniformly exponentially small. Choose one fixed \(\tau_0\) so that
\(Z(\tau)\ge c\) for \(\tau_0\le\tau\le L\). Also
\(V(\tau)\ge c\) throughout \([\delta,L]\) for large \(\ell\).
The bounded lift and Floquet basis now give the second part of (1): use
the stable coordinate on the compact interval \([\delta,\tau_0]\) and
the growing coordinate thereafter. This proves a lower bound even through
the coordinate sign change.

## 6. History, viscosity, and the remaining PDE task

The pre-focus history is the original incoming branch. The through-focus
note bounds the additional central strain by
\(C\ell^{11/8}(1+\sqrt\ell\,\tau)\) on \([0,\delta]\). Combining it
with (2) and integrating the exponential proves (4). At the same endpoint,
the primary gradient clock is only
\(O(\ell e^{\mu L_{\ell,\eta}})=O(\eta\ell^{9/8})\), which is
\(o(\ell^2)\).

For the principal viscous factor, \(\epsilon/k^2=\nu h\) and (1) give

\[
 \frac{\epsilon}{k^2}\int_0^{t_f+L_{\ell,\eta}}|\xi_c(t)|^2dt
 \le C_\nu h\left[\ell^2\log\ell+
              \eta^2\ell^{9/4}(1+\log\ell)^2\right]=o(1).       \tag{17}
\]

This excludes principal central heat damping as an obstruction at this
finite endpoint. It is not a residual estimate for the complete packet.
Likewise, (4) controls one central history; passing to a whole transported
envelope, all phase and amplitude derivatives, pressure/mean/harmonic
corrections, and a separate strong-solution continuation remains a distinct
full-PDE obligation. A proof of those obligations may use the explicit
small factor \(\eta\) in (4). This note does not assume them in order to
claim an actual nonlinear solution.

Even if that finite lifting succeeds, the receiving velocity at large
\(\tau\) is \(O(k\ell^{7/8}/\tau)\), while its physical wave number
increases. There is still one already supplied receiver in a family whose
initial data vary with \(h\); no infinite cascade follows.

## 7. Reproduction and review boundary

The thin vectors and coefficients above were independently recomputed by
exact SymPy algebra: diagonalization of
\(-A_0-\Omega_0+2NN^TA_0/|N|^2\), the pairings
\(C\cdot B_\pm\), \(r\cdot B_-\), and the integral (10). The geometry
agent independently obtained the same stable vector, forcing integral and
large-time coefficient. That agent also separately audited the signed
inner-to-outer normalization, all terms in (12), both weighted equations
(13), the logarithmic perturbation cost, and the full-vector lower bound
through a zero of the growing coordinate; the central proof passed within
its stated scope. These checks certify the displayed finite algebra;
the estimates (12)–(16) are the written analytic perturbation argument.
Neither algebra checks nor this central proof constitute a formal NS
certificate.
