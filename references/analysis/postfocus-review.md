# Independent post-focus review and the available error margin

8 September 2026. Root's separate read of the
[longer-host argument](longer-host-attempt.md), including its
previously unreviewed endpoint-core deduction (22a). The finite fixed-small-time
extension passes within its stated scope. This review also records a
conditional quantitative error lemma for the proposed longer outer interval.
It does not itself establish that interval's polarization estimates.
ROOT, E-prime and FORCED-D remain open. No DNS or formal PDE certificate.

## 1. What the finite continuation uses

The earlier endpoint is \(t_f=(2/\mu)\log\ell-\ell^{-3/4}\).
Keep the same original data, fixed physical viscosity, fixed Gavrilov profile,
and fixed periodic phase profile. The additional duration \(\delta>0\) is
chosen small independently of \(h\).

The first-stage rate \(m_h=1+\ell^{-1}e^{\mu t}\) still has supremum and
integral \(O_\delta(\ell)\) through \(t_f+\delta\). The fixed-order
first-stage construction therefore retains its estimates with enlarged
constants. In particular, the H128 interpolation used for the actual
first-stage C24 bound is an independent high-order argument; C24 is not
inferred from the final C1 error for the two-packet solution.

For the receiving cotangent, the first two moving-frame equations are
independent of its third component and of the large primary coefficient.
Ordinary signed-time Taylor estimates therefore continue to negative
\(u=t_f-t\). The third equation is linear and gives
\[
x=2ae z+O(e^2z^2),\quad y=1+O(e|z|),\quad
w=-az^2+O(e|z|+e|z|^3),\qquad e=\Lambda^{-1/2}.
\]
For \(e|z|\le\delta\) and small fixed \(\delta\), \(y\) stays away from zero
and \(|(x,y,w)|^2\) is comparable to \(1+a^2z^4\).

In the exact pressure-corrected matrix, the potentially dangerous (3,1)
entry has numerator
\[
-2[a_{11}xyw-a_{12}x^2w+a_{21}y^2w-a_{22}xyw
-a_{31}x^2y-a_{31}y^3+a_{32}x^3+a_{32}xy^2].
\]
Its estimate depends on \(|z|\), not the sign of \(z\). In particular
\(|xw|/(1+z^4)\le Ce/(1+|z|)\). The full signed-time Taylor remainder and
bounded denominator give the four error entries and differentiated first
row used in the source. No pressure term or frame rotation is removed.

The scalar potential
\[
q(z)=\frac{4a^2z^2-2c(1+a^2z^4)}{(1+a^2z^4)^2}
\]
is positive and even for the stated \(a,c<0\). On the outgoing side put
\(s=-z\). The incoming branch continued across zero has positive value
and positive \(s\)-derivative. Its Volterra equation then gives
\(c(1+s)\le Y(-s)\le C(1+s)\) and
\(c\le\partial_sY(-s)\le C\); the upper estimates use
\(\int_0^\infty(1+s)q(s)\,ds<\infty\).

The perturbation is estimated in
\[
\sup_{s\le R}\frac{|Y(-s)|}{1+s}
+\sup_{s\le R}|\partial_sY(-s)|,\qquad R=\delta/e.
\]
Its source \(r_1Y'+r_0Y\), with \(|r_1|\le Ce\) and
\(|r_0|\le Ce/(1+s)\), is bounded pointwise by \(Ce\) times this norm.
One integration costs \(CeR\); two integrations divided by \(1+s\) cost
at most the same order. The unperturbed Volterra resolvent is uniformly
bounded, so choosing \(C\delta<1\) closes the perturbation. The incoming
bounded-\(Y\) norm would fail to represent the outgoing branch.

Reconstructing the complete polarization gives
\[
|\xi|\asymp 1+s^2,\qquad
|b_p|\asymp\frac{\sqrt{\Lambda}D_h}{1+s},\quad
|b_n|\le\frac{CD_h}{(1+s)^2},\quad |b_r|\le CD_h.
\]
Since \(s\le\delta\sqrt{\Lambda}\), the latter two components remain a
small fixed fraction of the first after reducing \(\delta\).
The normalized wave strain is therefore of order
\(\ell^{11/8}(1+\sqrt{\ell}\tau)\). Its added integral is
\(O_\delta(\ell^{15/8})\).

## 2. Why the whole packet and the nonlinear error remain controlled

The comparison from the central model to actual \(q_h\), and from its
central particle to other packet particles, uses coefficients integrating
to \(O_\delta(\ell)\). It therefore costs \(\exp(C_\delta\ell)\), rather
than an unproved polynomial bound for arbitrary perturbations. The
transported diameter \(d\exp(C_\delta\ell)\) is still \(o(h)\).
The bump is factored out before comparing polarizations; no lower bound
is asserted for the bump at its support boundary.

The derivative hierarchies for the phase, amplitudes and global mean have
top rate \(C_r m_h\). Their lower-order products only enlarge
\(\exp(C_\delta\ell)\) finitely many times. This retains the C24/C18/H16
order budget in the [profile proof](../navier-stokes/localized-profile.md).
Its exact equations (13), (17), (20)--(23) continue from the same original
data. There is no new endpoint cutoff or source installation.

Consequently the integrated residual remains
\(h^{31/8}\exp(C_\delta\ell)\operatorname{poly}(\ell)\), with the central
diffusivity mismatch at the smaller order \(h^{37/8}\exp(C_\delta\ell)\).
Global mean pressure tails use global Sobolev norms. Only the compact
wave factors receive the volume factor \(d^{3/2}\).

The full relative-energy inequality uses the **sharp** wave strain history
\(O_\delta(\ell^{15/8})\). Inserting the generic exponential jet bound
in that exponent instead would not prove the result. A separate H12
bootstrap and expanding-torus interpolation give
\[
\frac{31}{8}\frac{19}{24}
-\frac{117}{8}\frac5{24}=\frac1{48}>0.
\]
Because \(15/8<2\) and \(\log(1/h)=\ell^2\), the resulting factors
\(\exp(C_\delta\ell^{15/8})\) are subpower in \(h\). The gradient-error
bootstrap improves strictly, and the H12 continuation theorem supplies
the strong lifetime. This is not continuation inferred from relative L2
energy alone.

## 3. Separate verification of the new endpoint core

At \(t_+=t_f+\delta\), the central covector has magnitude
\(\asymp_\delta\ell\). Choose \(R_+=c_Fk/|\xi_c|\), with \(c_F\) smaller
than a fixed fraction of the phase profile's flat interval.

The transported bump plateau contains a ball of radius at least
\(cd\exp(-C_\delta\ell)\). Since
\[
\frac{R_+}{d\exp(-C_\delta\ell)}
\le C_\delta h^{1/4}\ell^{-1}\exp(C_\delta\ell)\longrightarrow0,
\]
the smaller ball lies inside that plateau for sufficiently small \(h\).
The source's slow derivative estimates give
\[
|\nabla(b\otimes\xi/k)|\le d^{-1}\exp(C_\delta\ell),\qquad
|D^2S|\le h^{-1}\exp(C_\delta\ell).
\]
Fixed powers of \(\ell\) are absorbed in the exponential here.
Thus the leading-matrix variation is at most
\(C_\delta h^{1/4}\exp(C_\delta\ell)\). The phase variation obeys
\[
\frac{|S(x)-S(x_+)|}{k}
\le c_F+C_\delta h^{1/2}\ell^{-2}\exp(C_\delta\ell),
\qquad |x-x_+|\le R_+.
\]
It stays in a fixed smaller flat interval.

The central heat clock is \(O_{\nu,\delta}(h\ell^2\log\ell)\).
On a fixed inner subinterval of the linear profile, the periodic heat
kernel makes its rounding error exponentially small in the reciprocal
clock. Every fixed derivative and every fixed inverse power of \(k\)
remain smaller than any prescribed power of \(h\).

The base gradient variation is bounded by
\(R_+\|D^2q_h\|_\infty\le h^{1/2}\exp(C_\delta\ell)\).
The curl, mean and forced-profile corrections have C1 size
\(h^{1/4}\exp(C_\delta\ell)\). Adding the actual nonlinear error proves
the claimed uniform gradient approximation on the radius-\(R_+\) ball.
This verifies (22a) independently. It supplies an endpoint ball of radius
\(\asymp_\delta k/\ell\), not persistence of the old radius-\(ck\) ball,
higher actual-Q jets, or another seed.

## 4. Conditional margin for the next outer interval

This subsection is a reusable implication, not an assertion that its
new hypotheses have been established. Suppose the same construction
extends on an interval of length \(O(\log\ell)\), with all its required
slow-jet and full residual estimates bounded by factors \(E_h\) satisfying
\(\log E_h=o(\ell^2)\). Suppose its sharp full approximation-gradient
history obeys
\[
I_h=\int\|\nabla U_h\|_\infty\,dt
\le B\eta\ell^2+o(\ell^2)
\]
for one constant \(B\) independent of the fixed small \(\eta>0\).
Keep residual order \(31/8\), H12 initial/approximation order \(-117/8\),
and all the full pressure and support assumptions used above.

Then the exact same relative-energy and H12 arguments give
\[
\|\nabla(Q_h-U_h)\|_\infty
\le h^{1/48-C_*\eta-o(1)}
\]
for some fixed \(C_*\). To see the constant's origin, the L2 error costs
\(\exp(I_h)\), while the H12 norm costs \(\exp(C_{12}I_h)\) under the
gradient bootstrap. Interpolation raises these to powers \(19/24\) and
\(5/24\). One may take a larger \(C_*\) than
\(B(19+5C_{12})/24\); the \(O(\log\ell)\) bootstrap time cost is subpower.

Choosing \(C_*\eta<1/192\) leaves room for a bound \(h^{1/96}\) after
absorbing the subpower term and fixed constants for sufficiently small
\(h\). Hence an order-\(\ell^2\) clock with a sufficiently small fixed
coefficient is compatible with the existing error powers.

What remains to prove is the new sharp outgoing polarization and
whole-envelope history. An estimate \(I_h\le C\ell^2\) with an unspecified
large coefficient is insufficient. So is a generic bound
\(\exp(C\int m_h)\) on the receiver inserted into the final nonlinear
exponent. The new outer calculation must retain the adjustable
\(\eta\) in its endpoint and integrated estimate.
