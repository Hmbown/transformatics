# Independent error and endpoint audit for the logarithmic host

8 September 2026. Separate derivation review of the conditional error
margin in [the post-focus review](postfocus-review.md),
section 4, and of the proposed logarithmic endpoint consequences.
The interpolation, conditional nonlinear closure and frequency estimate
below pass their stated hypotheses. The complete
[logarithmic host assembly](../navier-stokes/logarithmic-host.md) also passed
this separate review within its stated finite scope, as recorded in
section 5.
No DNS, formal PDE certificate or solution claim is made.

## 1. The interpolation exponents are valid, including on the large torus

Use unnormalized Lebesgue measure on the torus of side \(2\pi L\),
\(L\ge1\), and the full inhomogeneous \(H^{12}\) norm. If
\(A=\|w\|_2\), \(H=\|w\|_{H^{12}}\), then

\[
 \|\nabla w\|_\infty\le C A^{19/24}H^{5/24},           \tag{1}
\]

with \(C\) independent of \(L\). This is a Gagliardo–Nirenberg estimate;
it does **not** require the false endpoint embedding
\(H^{5/2}(\mathbb T^3)\subset W^{1,\infty}\).

Here is a direct proof retaining the volume factors. For a Fourier
coefficient normalized by the reciprocal volume, Parseval is
\(A^2=(2\pi L)^3\sum_n|\widehat w(n)|^2\). Physical frequency is
\(\zeta=n/L\). Splitting at any \(R\ge1\), Cauchy–Schwarz gives

\[
 \|\nabla w_{\le R}\|_\infty
 \le \left[(2\pi L)^{-3}\sum_{0<|n/L|\le R}|n/L|^2\right]^{1/2}A
 \le C R^{5/2}A,
\]

\[
 \|\nabla w_{>R}\|_\infty
 \le \left[(2\pi L)^{-3}\sum_{|n/L|>R}
       \frac{|n/L|^2}{(1+|n/L|^2)^{12}}\right]^{1/2}H
 \le C R^{-19/2}H.                                   \tag{2}
\]

The lattice bounds are uniform for \(L,R\ge1\); their density factor
\(L^3\) cancels the volume normalization. Since \(H\ge A\), the choice
\(R=(H/A)^{1/12}\) is admissible and proves (1). If \(A=0\), the result
is immediate. The zero Fourier mode is absent from the gradient.

The same split without a gradient gives
\(\|w\|_\infty\le C A^{7/8}H^{1/8}\). Since \(H\ge A\), (1)'s
right side bounds that quantity too. Thus the full \(C^1\) norm can be
estimated with (1), up to one larger uniform constant. No torus-size
Poincaré constant enters.

## 2. Conditional nonlinear closure and its dependence on eta

Suppose the full real, solenoidal approximation \(U_h\) is defined on
\([0,T_h]\), agrees exactly with the original datum of \(Q_h\), and its
full periodic-pressure NS residual is \(R_h\). Assume

\[
 T_h=O(\log\ell),\quad
 \int_0^{T_h}\|R_h\|_2dt\le h^{31/8}E_h,\quad
 \|Q_h(0)\|_{H^{12}}+\sup_t\|U_h(t)\|_{H^{12}}
                   \le h^{-117/8}E_h,
\]

\[
 I_h=\int_0^{T_h}\|\nabla U_h\|_\infty dt
          \le B\eta\ell^2+o(\ell^2),\qquad
 \log E_h=o(\ell^2),\quad \ell^2=\log(1/h).            \tag{3}
\]

For the claimed adjustable margin, \(B\) and the constants in these
estimates must be independent of fixed \(0<\eta\le\eta_0\). The
threshold for sufficiently small \(h\) may depend on \(\eta\).

On the actual strong lifetime, the full difference equation and
solenoidality give

\[
 \|Q_h-U_h\|_2\le h^{31/8}E_he^{I_h}
                 \le h^{31/8-B\eta-o(1)}.             \tag{4}
\]

The coefficient is the sharp \(\|\nabla U_h\|_\infty\) history.
The cubic difference term integrates to zero. Any noncompact mean and
its pressure are already part of \(U_h,R_h\); they cannot be discarded
in applying (4).

Independently bootstrap \(\|\nabla(Q_h-U_h)\|_\infty\le1\). The
integer Sobolev energy estimate for the actual unforced equation is

\[
 \frac{d}{dt}\|Q_h\|_{H^{12}}
       \le C_{12}\|\nabla Q_h\|_\infty\|Q_h\|_{H^{12}}.
\]

The constant is uniform on \(L\ge1\); viscosity contributes a
nonpositive term. Under the bootstrap,
\(\int\|\nabla Q_h\|_\infty\le I_h+T_h\). Therefore

\[
 \|Q_h\|_{H^{12}}+\|Q_h-U_h\|_{H^{12}}
       \le h^{-117/8-C_{12}B\eta-o(1)}.               \tag{5}
\]

Equations (1), (4) and (5) yield

\[
 \|Q_h-U_h\|_{C^1}
 \le h^{1/48-C_*\eta-o(1)},\qquad
 C_*\ge B(19+5C_{12})/24,                             \tag{6}
\]

after increasing a fixed constant if necessary. The base exponent is
exactly
\((31\cdot19-117\cdot5)/(8\cdot24)=1/48\).
Choosing \(C_*\eta<1/192\) leaves more than the required margin for
\(h^{1/96}\) once subpower terms and fixed constants are absorbed.
The estimate improves the gradient bootstrap. The bounded actual
\(H^{12}\) norm, not (4) alone, supplies strong continuation to and
through the finite endpoint.

This verifies the conditional implication in the post-focus review. It
does not supply a missing whole-support version of \(I_h\), nor permit
the generic slow-jet bound \(E_h\) to replace that sharp history.

## 3. The high-frequency bound and its scale

The high-frequency part of (2) also proves, for a uniformly bounded smooth
high-pass multiplier supported on \(|\zeta|\gtrsim R\),

\[
 \|\nabla P_{\ge R}Q_h\|_\infty
           \le C R^{-19/2}\|Q_h\|_{H^{12}}.
\]

At \(R=h^{-9/4}\), (5) gives

\[
 \|\nabla P_{\ge h^{-9/4}}Q_h\|_\infty
       \le h^{27/4-C_{12}B\eta-o(1)},                 \tag{7}
\]

since \((9/4)(19/2)-117/8=27/4\). The constant multiplying \(\eta\)
in (7) need not equal the one in (6). A sufficiently small common choice
works for both. This is a high-pass exclusion for the actual solution on
the proved finite interval, not a prohibition against all later creation
of high frequencies.

## 4. Conditional endpoint-core calculation

At \(T_h=t_f+L_{\ell,\eta}\), suppose the full first-stage and slow-jet
estimates have the uniform factor \(E_h\) in (3), and the central
covector has
\(|\xi_c|\asymp\eta\ell^{9/8}(1+\log\ell)\). Choose

\[
 R_*=c_Fk/|\xi_c|\asymp
       \frac{k}{\eta\ell^{9/8}(1+\log\ell)},\qquad
 A_* =\nabla q_h(T_h,x_*)-b_c(T_h)\otimes\xi_c(T_h)/k.
                                                               \tag{8}
\]

Here \(x_*\) is the prescribed **first-stage** particle, and \(c_F>0\)
is chosen inside the fixed phase profile's linear interval. It is not
claimed to be a particle of \(Q_h\).

For a plateau transported by the incompressible first-stage flow, the
original radius-\(cd\) plateau contains at time \(T_h\) a ball of radius
\(cdE_h^{-1}\), after enlarging \(E_h\) to include the integrated
first-stage gradient. Since

\[
 \frac{R_*}{dE_h^{-1}}
       \le \frac{C h^{1/4}E_h}
                    {\eta\ell^{9/8}(1+\log\ell)}\longrightarrow0,
\]

the smaller ball lies in that plateau. The slow estimates
\(|\nabla(b\otimes\xi/k)|\le d^{-1}E_h\),
\(|D^2S|\le h^{-1}E_h\) give matrix variation bounded by
\(h^{1/4-o(1)}\) there, for each fixed \(\eta>0\), and phase variation

\[
 \frac{|S(x)-S(x_*)|}{k}
 \le c_F+\frac{C k h^{-1}E_h}
                    {\eta^2\ell^{9/4}(1+\log\ell)^2}
       =c_F+h^{1/2-o(1)}.                             \tag{9}
\]

Thus it stays in a fixed smaller linear interval. The base gradient
variation is bounded by \(R_*\|D^2q_h\|_\infty=h^{1/2-o(1)}\).
These estimates are valid because \(\log E_h=o(\ell^2)\); powers of
\(1/\eta\) are fixed after choosing \(\eta\), not powers of \(1/h\).

The central heat time obeys

\[
 \theta_c\le C_\nu h[\ell^2\log\ell+
             \eta^2\ell^{9/4}(1+\log\ell)^2].          \tag{10}
\]

On a smaller linear subinterval, a periodic heat kernel averages a
locally affine function exactly except for its exponentially small
tails reaching the nonlinear part of the profile. Its difference from
the affine function, with any fixed number of phase derivatives, is
bounded by a polynomial in \(1/\theta_c\) times
\(e^{-c/\theta_c}\). Since (10) is \(h\) times a fixed polynomial in
\(\ell\), this remains smaller than every fixed power of \(h\), even
after the finite inverse powers of \(k\) in physical derivatives.

Adding the complete curl/mean/profile correction bound
\(h^{1/4}E_h\) and the actual nonlinear error (6) therefore gives
\(\sup_{B_{R_*}(x_*)}|\nabla Q_h-A_*|\le h^{1/96}\), with a little
strict margin reserved in (6) to absorb the additional terms.
This is an endpoint ball with a smaller radius. It gives no persistence
of an earlier ball, no higher actual-\(Q_h\) jets, and no next seed.

## 5. Full-source audit and physical units

The reviewer subsequently read the complete
[new host assembly](../navier-stokes/logarithmic-host.md), independently of
its other review, and checked its sections 2–6 against the incoming,
through-focus and full-profile source equations. The following obligations
are met within the imported finite-construction hypotheses.

* The first-stage construction is extended on its own. Its clock increases
  from \(O(\ell)\) to \(O(\ell^{9/8})\), and every previously strictly
  positive error power survives multiplication by
  \(\exp(C\ell^{9/8})=h^{-o(1)}\). Its C24 estimate comes from the
  separate H128 hierarchy; it is not a differentiated C1 result for the
  two-wave solution.
* The central-to-support comparison uses actual first-stage characteristics
  and its gradient difference \((d/h)m_hE_h\). Direction, logarithmic
  magnitude and full amplitude equations cost only finitely many factors
  \(E_h\). Because the transported bump is factored out, this comparison
  does not divide by a vanishing envelope at its boundary. The resulting
  \(h^\sigma E_h\) error preserves the leading whole-support clock
  \(B_0\eta\ell^2\), with \(B_0\) independent of \(\eta\).
* The mean, forced profile and curl potentials continue from their original
  zero or prescribed initial data. The full identities (11)–(23) of the
  localized-profile source remain exact, including longitudinal pressure,
  all profile Fourier modes, the central diffusivity mismatch and the
  noncompact global mean. No temporal splice changes the datum or inserts
  a new residual.
* The finite jet hierarchy retains diagonal rate \(C_rm_h\). For example,
  the mean equation's scaled coefficient at derivative order \(j\) is
  bounded by \(C_jm_h(d/h)^{j-1}\); its nonlocal pressure is eliminated in
  the solenoidal L2 energy identity, rather than estimated by an invalid
  L-infinity Leray bound. Derivatives of the polarization projection enter
  lower-order source terms, so their subpower bounds are not put into a
  new exponential. The original C24/C18/H16/13 and A80 order budget
  remains sufficient.
* The residual table still has smallest exponent \(31/8\), and the full
  approximation H12 exponent remains \(-117/8\). Support volume is used
  only for compact profile factors. The global mean uses its global norms.
  The residual estimate is thus independent of the separate sharp
  whole-gradient estimate, as required for the bootstrap in section 2.

In particular \(E_h\) can be chosen as one fixed power of \(\ell\)
times \(\exp(C\ell^{9/8})\), with constants independent of
\(0<\eta\le\eta_0\le1\). The fixed small coefficient of the
order-\(\ell^2\) history is therefore available to (6), rather than
hidden inside an uncontrolled constant. The strict gap between the
exponent left by \(C_*\eta<1/192\) and \(1/96\) also absorbs the
additional endpoint-core errors in section 4.

The physical conversions independently check as follows. With the original
concentration factor \(L=h^{-10}\) and velocity amplitude \(h^{-14}\),

\[
 x_{\rm phys}=h^{10}x,\quad
 t_{\rm phys}=h^{24}t,\quad
 u_{\rm phys}=h^{-14}Q_h,\quad
 \nabla_{\rm phys}u_{\rm phys}=h^{-24}\nabla Q_h.
\]

The transformed viscosity is \(\nu L/h^{-14}=\nu h^4\), as required.
The new endpoint ball therefore has physical radius

\[
 R_{\rm phys}\asymp
 \frac{h^{23/2}}{\eta\ell^{9/8}(1+\log\ell)}.
\]

The high-pass estimate (7) is in rescaled gradient units. Its absolute
physical gradient bound acquires \(h^{-24}\), and generally does not tend
to zero; its size relative to the endpoint strain still tends to zero.
The new source explicitly keeps this distinction.

The parameter \(\eta\) chooses a later observation/stopping time. It
changes neither original seed, fixed phase profile nor original datum for
a given \(h\). The datum still varies with \(h\); this extension does
not produce an infinite trajectory for one datum. The endpoint ball is
located at the specified first-stage particle and supplies only C1
closeness to its stated affine matrix. It does not provide an actual-Q
higher-jet hierarchy or a next transfer.

**Verdict:** the full finite logarithmic-host assembly, its error margin,
endpoint core, physical conversion and high-frequency exclusion pass this
independent written review, conditional only on the already stated finite
source hypotheses. This is AI-agent mathematical review, not external
expert acceptance or a formal PDE certificate. ROOT and FORCED-D remain
open.

Final clarification check: the canonical source explicitly records the
first-stage minimum margin \(13/256\), the strict \(1/64-o(1)\) reserve
before the advertised \(1/96\) endpoint error, the Fourier-split proof,
and the scope of the slow wave-lift remainder. These agree with the
independent calculations above. Reviewed canonical source SHA-256:
`2d06d4bf6edc170b79728e9494fb2ccfe7af3c803ad8535636359016b5f01761`.
