# A generated normal component survives a fixed initial time interval

8 September 2026. **Reviewed bounded written calculation.** The
[independent review](normal-source-transport-review.md) pins
the mathematical source at SHA-256
`4f32a640a675659b13838d80245271ad85524fdd3630124f0f6be9c51375022d`.
Root also independently read the argument. Later review-label edits do not
change its equations. This is AI-agent review, not external expert acceptance
or a formal PDE certificate.
The same actual unforced solution and the same original data as the
[logarithmic host](../navier-stokes/logarithmic-host.md) have a nonzero
normal nonlinear remainder after subtracting the exact viscous linearized
transport of their existing receiver. The lower bound holds through a
fixed sufficiently small rescaled time, independent of h. No third donor
is supplied. This does not propagate the component through focus, create
a new short-wave phase, or close ROOT, E-prime or FORCED-D. No DNS is used.

The subtraction matters: a total late-time Fourier stress contains
q times the generated mean, which can be larger than the receiver's own
stress. Here that entire linear interaction, including its pressure, is
retained in an exact propagator. It is not estimated as a small source.

## 1. Observable and conclusion

Use the original-data notation of
[the signed initial-source calculation](actual-third-source.md):

\[
 Q(0)=q(0)+z_0,
 \quad a_h=|b_c(0)|\asymp k\ell^{-13/8},
 \quad e_b=b_c(0)/a_h,\quad e_n=\xi_c(0)/|\xi_c(0)|,
 \quad e_b\perp e_n.
\]

Here q is the **actual** first-stage NS solution, not its affine model;
z_0 includes the original receiver's complete curl correction. Put

\[
 k=h^{3/2},\quad d=h^{5/4},\quad \epsilon=\nu h^4,
 \quad L=h^{-10},\quad
 M_h=\langle F^2\rangle\Big(\int\chi^2\Big)a_h^2d^3
       \asymp h^{27/4}\ell^{-13/4}.
                                                        \tag{1}
\]

Choose once a sufficiently large original-preparation majorant
\(\mathcal E_h=\ell^A\exp(B_0\ell)\), with fixed A and B_0, and set

\[
 R_h=d\mathcal E_h^2,\qquad \kappa_h=R_h^{-1}.
                                                        \tag{2}
\]

In particular \(R_h/h=h^{1/4}\mathcal E_h^2\to0\), whereas the
receiver's transported support diameter on a fixed initial interval is
at most \(Cd\mathcal E_h\). Let Y be the same q-particle as before.

Let Z solve the exact linearized viscous equation

\[
 \partial_t Z+\mathbb P(q\cdot\nabla Z+Z\cdot\nabla q)
          -\epsilon\Delta Z=0,
 \qquad Z(0)=z_0,\quad\operatorname{div}Z=0.
                                                        \tag{3}
\]

Define the actual nonlinear remainder

\[
 W=Q-q,\qquad N=W-Z.
                                                        \tag{4}
\]

Thus N(0)=0. The comparison flow Z is uniquely specified by existing q
and z_0. It adds no initial wave and introduces no applied force.

There is a fixed \(t_0>0\), depending only on the fixed profiles and
fixed constants, such that for all sufficiently small h and every
\(0<t\le t_0\),

\[
 \|e_n\cdot N(t)\|_\infty
       \ge c t M_h\kappa_h^4
       \asymp t h^{7/4}\ell^{-13/4}\mathcal E_h^{-8},
                                                        \tag{5}
\]
\[
 \|\partial_{e_n}(e_n\cdot N(t))\|_\infty
       \ge c t M_h\kappa_h^5
       \asymp t h^{1/2}\ell^{-13/4}\mathcal E_h^{-10}.
                                                        \tag{6}
\]

The second quantity is a diagonal strain component of N. Both bounds
are witnessed by a smooth cone filter at frequencies comparable to
\(\kappa_h\). They are endpoint bounds, not only initial accelerations
or integrals of an untransported source. The direction e_n remains the
original receiving normal; it is not a later outgoing polarization.

## 2. Exact subtraction retains every linear interaction and its pressure

Write \(A=\nabla q\) and
\(B_qv=\mathbb P(q\cdot\nabla v+Av)\). Subtracting the two actual
NS equations gives the exact identities

\[
 \partial_t W+B_qW-\epsilon\Delta W
       =-\mathbb P\operatorname{div}(W\otimes W),
\]
\[
 \partial_t N+B_qN-\epsilon\Delta N
       =-\mathbb P\operatorname{div}(W\otimes W),
 \qquad N(0)=0.                                      \tag{7}
\]

In particular q times every generated mean or oscillatory correction is
inside B_qN and B_qZ. There is no omission of q times the mean from a
total-stress Fourier calculation. The quadratic source still contains
all mean-mean, mean-wave and wave-wave products of the **actual** W.

The solenoidal energy identity also gives, on a fixed initial interval,

\[
 \|W(s)\|_2\le \|z_0\|_2
      \exp\!\left(\int_0^s\|A\|_\infty du\right)
      \le C a_h d^{3/2},                             \tag{8}
\]

using the unnormalized torus L2 norm. The nonlinear self-interaction
cancels in this estimate. No norm of the full Q is substituted for the
small relative norm in (8).

## 3. Resolving the actual relative stress

Let Z_a denote the existing primary receiving curl packet about actual q,
with the spatially constant central heat clock. The one-round corrected
approximation already used in the logarithmic host has

\[
 U_1=q+m_1+Z_a+Z_g,
 \qquad \|m_1\|_2+\|Z_g\|_2
                    \le k\rho d^{3/2}E_h,
 \quad \rho=k/d=h^{1/4},                             \tag{9}
\]

where \(\log E_h=o(\ell^2)\). These are global norms: neither m_1
nor its pressure is assigned compact support. The full curl part of Z_g
is included. The existing actual-solution comparison gives

\[
 \|Q-U_1\|_2\le h^{31/8-B\eta}E_h.
\]

Here B is the leading-clock constant in that theorem, not B_0 in (2).
Its permitted sufficiently small fixed eta can be taken to satisfy
\(B\eta<1/4\), independently of the datum. Consequently

\[
 \sup_{0\le s\le t_0}
 {\|W(s)-Z_a(s)\|_2\over a_h d^{3/2}}
 \le C\left(h^{1/4}\ell^{13/8}E_h
          +h^{1/2-B\eta}\ell^{13/8}E_h\right)=o(1).
                                                        \tag{10}
\]

Only the already available J=1 estimate is used; no unproved uniform
limit of the finite-depth recurrence is required. Cauchy-Schwarz, (8)
and (10) imply

\[
 \|W\otimes W-Z_a\otimes Z_a\|_1=o(M_h)
                                                        \tag{11}
\]

uniformly on this interval. Thus global pressure tails, all cross terms
and the actual-Q error are smaller **relative to the small stress mass**.
Using Q itself in this estimate would lose that property.

For completeness, the primary stress has a uniform small-time description.
Let \(\beta_h(s)=b_c(s)/a_h\), so \(\beta_h(0)=e_b\).
The exact pressure-bearing polarization generator obeys
\(|G|\le3|A|\), and the initial-interval q estimates give

\[
 |\beta_h(s)-e_b|\le Cs,
 \qquad |\xi_c(s)|\asymp\ell,
 \qquad \theta_c(s)
  ={\epsilon\over k^2}\int_0^s|\xi_c(u)|^2du
                       \le C\nu h\ell^2s=o(1).       \tag{12}
\]

The initial whole-envelope comparison propagates through fixed t_0 by
the actual characteristic and polarization equations. Its relative
error is \(h^\sigma\mathcal E_h\) for a fixed \(\sigma>0\), after
enlarging A and B_0 finitely. The transported bump has unchanged squared
integral \(d^3\int\chi^2\). Its support stays within
\(Cd\mathcal E_h\) of Y(s).

The phase-mean primary stress, with its full curl correction retained,
therefore has integral

\[
 \int\langle Z_a\otimes Z_a\rangle_{\rm phase} dx
       =M_h\beta_h(s)\otimes\beta_h(s)+o(M_h).
                                                        \tag{13}
\]

The bracket denotes the auxiliary periodic phase mean, not time averaging.
The heat change in \(\langle F^2\rangle\) is o(1). The curl stress and
its cross terms have relative L1 size at most
\((k/d)\mathcal E_h=o(1)\); the exact zero phase mean of F times its
periodic primitive could give a sharper bound but is unnecessary here.

The nonzero phase terms also integrate to o(M_h) against a fixed smooth
probe varying on scale R_h. Indeed \(|\xi|\ge c\ell\) on the support,
and integration by parts in each nonzero mode of F squared gives the
relative factor \((k/d)\mathcal E_h=o(1)\). Derivatives of the probe
cost only \(R_h^{-1}\le d^{-1}\); summation uses the existing fixed
smooth phase-profile norms. This argument includes the pulled-back
geometry and applies uniformly in s. No spatial phase mean is declared
equal to the actual field without this error estimate.

## 4. A real normal probe with a signed projected stress

Choose a smooth nonnegative function \(\psi_h(v)\), not identically
zero, supported in a fixed-opening cone-annulus

\[
 1<|v|<2,\qquad v\cdot e_b>c_*,\qquad v\cdot e_n>c_*.
\]

It can be chosen by rotation from a fixed reference function, so all
Schwartz bounds below and the positive constants are uniform in h.
Define real Schwartz functions on \(\mathbb R^3\)

\[
 f_h(y)=-\int\psi_h(v)\sin(v\cdot y)\,dv,
 \qquad \Phi_h(y)=\mathbb P_{\mathbb R^3}(e_nf_h)(y).
                                                        \tag{14}
\]

Their Fourier supports avoid zero. The full Leray symbol gives

\[
 (e_b\otimes e_b):\nabla\Phi_h(0)
   =\int\psi_h(v)
       {(e_b\cdot v)^2(e_n\cdot v)\over|v|^2}\,dv
   =:c_\psi>0.                                      \tag{15}
\]

The unprojected probe e_n f_h would have zero contraction in (15),
because \(e_b\perp e_n\). The positive normal output comes from the
pressure projection; dropping pressure would lose it.

Periodize f_h and Phi_h on the rescaled torus of side \(2\pi H_h\),
where \(H_h=L/R_h\to\infty\). Denote the periodizations by f_h^H and
Phi_h^H. Periodization commutes with this Fourier multiplier: the
periodic Leray projection of e_n f_h^H is exactly Phi_h^H. The zero mode
vanishes. Schwartz decay implies

\[
 \|f_h^H\|_1+\|\Phi_h^H\|_{H^6}
 +\sum_{r\le5}\|\operatorname{dist}_{\mathbb T_{H_h}}(y,0)
                             D^r\Phi_h^H\|_2\le C.  \tag{16}
\]

For example, sum translates of the fixed Schwartz tails over the central
fundamental cube. This proves (16) with C independent of the expanding
torus and also gives \(\nabla\Phi_h^H(0)=\nabla\Phi_h(0)+o(1)\).

For endpoint t, prescribe the solenoidal terminal test

\[
 \phi_t(x)=\kappa_h^3\Phi_h^H(\kappa_h(x-Y(t))).       \tag{17}
\]

Let phi(s,x), 0<=s<=t, solve the exact backward adjoint

\[
 \partial_s\phi
   =\mathbb P(-q\cdot\nabla\phi+A^T\phi)
           -\epsilon\Delta\phi,
 \qquad \phi(t)=\phi_t.                             \tag{18}
\]

Equation (18) is parabolic in backward elapsed time t-s. Leray is retained
on the entire vector equation, not replaced by a central symbol.

## 5. Uniform control of the transported adjoint

Set \(\sigma=t-s\), \(y=(x-Y(s))/R_h\), and write
\(\phi(s,x)=\kappa_h^3\Phi(\sigma,y)\). In these coordinates,

\[
 \partial_\sigma\Phi
  =\mathbb P[b_s\cdot\nabla_y\Phi-A_s^T\Phi]
       +\delta_h\Delta_y\Phi,
 \quad \Phi(0)=\Phi_h^H,
                                                        \tag{19}
\]
\[
 b_s(y)={q(s,Y(s)+R_hy)-q(s,Y(s))\over R_h},
 \quad A_s(y)=\nabla q(s,Y(s)+R_hy)=\nabla_y b_s,
 \quad \delta_h=\epsilon/R_h^2
              =\nu h^{3/2}\mathcal E_h^{-4}=o(1).
\]

The original q estimates on a fixed initial interval imply

\[
 \|D_y^r b_s\|_\infty
    \le C_r(R_h/h)^{r-1}\le C_r\quad(1\le r\le5),
 \quad |b_s(y)|\le C\operatorname{dist}(y,0),
 \quad\operatorname{div}_yb_s=0.                    \tag{20}
\]

The last bound is obtained by integrating the global Lipschitz bound
along a shortest torus segment. A uniform bound on b_s itself is neither
true nor needed. The derivatives of A_s through order four are uniform.

To avoid placing a weight on an unknown pressure tail, subtract the
**fixed** test: \(\Xi=\Phi-\Phi_h^H\). Its equation has the same
homogeneous operator as (19) and forcing

\[
 F_s=\mathbb P[b_s\cdot\nabla\Phi_h^H-A_s^T\Phi_h^H]
                         +\delta_h\Delta\Phi_h^H.
\]

Equations (16) and (20) give \(\|F_s\|_{H^4}\le C\). The only
weighted factor is b_s times a derivative of the prescribed Schwartz
test. For Xi use ordinary **unweighted** H4 energy. Leray commutes with
derivatives and is self-adjoint, the test Xi is solenoidal, the undifferentiated
transport term cancels by div b_s=0, and every commutator uses only the
bounded derivatives in (20). The viscous term is nonpositive. Therefore

\[
 {d\over d\sigma}\|\Xi\|_{H^4}
       \le C\|\Xi\|_{H^4}+C,
 \qquad \|\Xi(\sigma)\|_{H^4}\le C\sigma e^{C\sigma}.
                                                        \tag{21}
\]

The H4-to-C1 embedding is uniform on these expanding tori, as follows
directly from Fourier Cauchy-Schwarz and the integrability of
\(|v|^2(1+|v|^2)^{-4}\) in dimension three. Thus for t<=1,

\[
 \|\nabla_x\phi(s)
   -\kappa_h^4\nabla_y\Phi_h^H(\kappa_h(\cdot-Y(s)))\|_\infty
                  \le Ct\kappa_h^4.                 \tag{22}
\]

This controls the complete adjoint, including its global pressure tails.
It does not assume that an arbitrary actual-q propagator is polynomial
in a large accumulated strain. Only a fixed short interval with bounded
q gradient and bounded rescaled coefficient derivatives is used.

## 6. A signed endpoint integral and its norms

The primary support has \(\kappa_h|x-Y(s)|\le C\mathcal E_h^{-1}\).
Equations (12)--(16) and phase averaging therefore give

\[
 \int (Z_a\otimes Z_a):
  \kappa_h^4\nabla\Phi_h^H(\kappa_h(x-Y(s)))\,dx
       =M_h\kappa_h^4[c_\psi+O(s)+o(1)].            \tag{23}
\]

Now apply (11), (22) and the exact small relative-energy bound (8).
Uniformly for 0<=s<=t<=t_0,

\[
 \int (W\otimes W)(s):\nabla\phi(s)\,dx
       =M_h\kappa_h^4[c_\psi+O(t)+o(1)].             \tag{24}
\]

Choose a fixed t_0 sufficiently small that the absolute O(t) error is
at most c_psi/4. Then choose h small enough to bound all uniform o(1)
errors by c_psi/4. Neither choice changes the original datum.

Pair (7) with the exact adjoint (18). Integration by parts and N(0)=0
give the exact endpoint identity

\[
 \langle N(t),\phi_t\rangle
    =\int_0^t\int(W\otimes W):\nabla\phi\,dx\,ds
    \ge {c_\psi\over2}tM_h\kappa_h^4.              \tag{25}
\]

This is the full signed Duhamel output after q-linear transport. No
component of the interior adjoint is assumed to stay parallel to e_n.
At the endpoint alone, solenoidality and (14),(17) give

\[
 \langle N(t),\phi_t\rangle
   =\int(e_n\cdot N(t,x))
         \kappa_h^3 f_h^H(\kappa_h(x-Y(t)))\,dx.
                                                        \tag{26}
\]

The scalar kernel in (26) has uniformly bounded L1 norm. This proves
(5), including its asserted normal component rather than just a vector
norm.

For the gradient, use the **cosine antiderivative**

\[
 g_h(y)=\int{\psi_h(v)\over e_n\cdot v}\cos(v\cdot y)\,dv,
 \qquad \partial_{e_n}g_h=f_h.
                                                        \tag{27}
\]

It is Schwartz with uniform L1 norm because the support stays away from
e_n dot v=0. Periodize g_h as before. Integrating (26) by parts makes
its right side

\[
 -\int\partial_{e_n}(e_n\cdot N(t,x))
       \kappa_h^2 g_h^H(\kappa_h(x-Y(t)))\,dx.
\]

This scalar kernel has L1 norm at most C/kappa_h, proving (6).
Differentiating the odd sine test at its center instead would change the
parity and would not justify the same signed calculation.

## 7. Scope and the exact next missing estimate

At the fixed endpoint t_0, (5)--(6) improve the earlier h^7 time factor
to a constant. The result is an actual nonlinear normal output relative
to exact linearized evolution of the same receiver. It needs no q-squared
Fourier-tail estimate and does not drop the potentially larger q-mean
interaction. Such terms were incorporated exactly in (7),(18).

The output frequency is still \(\kappa_h=d^{-1}\mathcal E_h^{-2}\),
coarser than the original receiver and finer than the first packet. This
is an envelope/pressure contribution, not a proved independent rapidly
oscillating phase. The estimate is a filtered norm lower bound; it does
not locate a packet core or identify its sign at the original center.
It also does not assert that the nonlinear remainder dominates the
background and the linearized receiver in the total field.

The precise missing postfocus term is the signed pairing

\[
 \int_0^{t_\eta}\int(W\otimes W)(s):
       \nabla\big[U_q(t_\eta,s)^*\phi_{t_\eta}\big]\,dx\,ds.
                                                        \tag{28}
\]

For fixed short t the adjoint gradient is an O(t) perturbation of a probe
with a positive rank-one contraction. Through focus, the existing q
clock is large, the selected receiver polarization changes, and the
adjoint tensor in (28) need not retain that sign. A smaller actual-Q
tracking error from any fixed profile depth does not determine (28).
Thus this calculation identifies a genuinely generated component of
the actual flow for a useful finite interval, but does not yet provide
its postfocus polarization, amplification, or next-stage coupling.

In physical units the fixed observation time is h^24 t_0, the witnessed
wavelength is h^(45/4) times mathcal E_h squared, velocity is multiplied
by h^(-14), and gradient by h^(-24). These factors act on a family of
different smooth original data as h varies; they are not growth along
one datum toward a singular time.

## Checks

The signs in (15),(18),(19),(25),(27), all six scale conversions in
(1),(2),(5),(6),(10),(20), and the expanding-torus normalization were
checked directly. These finite algebra checks do not certify the analytic
argument. The separate review above checks the written argument and records
three omitted-term controls; its precise finite scope remains in force.
