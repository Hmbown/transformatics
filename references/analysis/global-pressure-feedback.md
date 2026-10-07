# Global pressure feedback into the slow exterior response

8 September 2026. Restricted written analysis. The pressure identities
below apply to the actual linear force response. A separate family of
instantaneous test fields proves a limitation of norm-only pressure
estimates; those tests are not asserted to be the actual response.
Neither an unforced singularity nor closure of the slow exterior system
is established.

The reference is the fixed viscosity-one, unit-torus construction in
[OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
has SHA-256 `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
All profile choices and \(0<h<1/100\) are fixed. The
[slow exterior equations](low-axial-response.md)
identify the missing harmonic pressure trace; this note specifies its
dependence on the complete global response.

## 1. The actual pressure functional

Let \(e\) solve the complete periodic linear equation
\[
 e_t=\nu\Delta e-\mathbb P\big((U\cdot\nabla)e+(e\cdot\nabla)U\big)
       +\mathbb P f,\qquad e(t_0)=0,\qquad\operatorname{div}e=0.
 \tag{1}
\]
Put
\[
 T_{ij}=U_i e_j+e_iU_j,\qquad
 \pi=-\Delta^{-1}\partial_i\partial_jT_{ij},\qquad
 \phi=\Delta^{-1}\operatorname{div}f,
 \tag{2}
\]
with zero spatial means for the potentials. On a source-free exterior
tube, the physical pressure in the local homogeneous equation is
\(\pi+\phi\), not \(\pi\) alone. In particular the coefficient
needed by the local affine family is
\[
 \partial_z^2\overline{\pi+\phi}(r,z,t).
 \tag{3}
\]
An overline denotes angular averaging in the local Euclidean chart.
The force potential is smooth through terminal time; the response
pressure is the bilinear functional (2) of the actual \(U,e\).
Initially \(\pi(t_0)=0\), but this does not prescribe its later Hessian.

The fixed spatial construction is supported in
\(K=\{r\le1/4,\ |z|\le1/4\}\), strictly inside one period cell.
Thus \(T\) is supported there even though \(e\) need not be. This follows
from the actual curl/direct-field localization in
[MixedPeriodicAssembly](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedPeriodicAssembly.lean#L27)
and the support cylinder in
[SpatialLocalization](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/SpatialLocalization.lean#L73).

Let \(G_{\mathbb T}\) be the mean-zero unit-torus Green function,
\(\Delta G_{\mathbb T}=\delta_0-1\). On a fixed ball containing all
differences \(x-y\), with \(x\) in a sufficiently small neighborhood
of the origin and \(y\in K\),
\[
 G_{\mathbb T}(x-y)=G_E(x-y)+H(x-y),\qquad
 G_E(\xi)=-\frac1{4\pi|\xi|}.
 \tag{4}
\]
The ball has radius less than one, so contains no other lattice point.
The function \(H\) is smooth there, with \(\Delta H=-1\), and has
the cubic lattice symmetries. This is an exact local decomposition of
the periodic Green function; no conditionally convergent image sum is
discarded. With derivatives interpreted distributionally at the
diagonal, (2) becomes
\[
 \pi=\pi_E+\pi_H,
 \qquad
 \pi_E(x)=-\int\partial_i\partial_jG_E(x-y)T_{ij}(y)\,dy,
 \quad
 \pi_H(x)=-\int_K\partial_i\partial_jH(x-y)T_{ij}(y)\,dy.
 \tag{5}
\]
All integrals involving \(H\) are ordinary smooth-kernel integrals.
In particular,
\[
 \|\nabla^2\pi_H\|_{L^\infty(\text{near }0)}
 \le C\|U\|_2\|e\|_2.
 \tag{6}
\]
This retains every periodic-image contribution to the pressure Hessian.

## 2. Which angular components enter?

Euclidean convolution in (5) commutes with rotations. Consequently the
angular mean \(\overline{\pi_E}\) depends exactly on the equivariant
angular mean of \(T\): average its cylindrical components before
recovering the scalar pressure. Write these components as
\(\bar T_{rr},\bar T_{r\theta},\bar T_{rz},\bar T_{\theta\theta},
\bar T_{\theta z},\bar T_{zz}\). The double divergence is
\[
 \operatorname{div}\operatorname{div}\bar T
 =\left(\partial_r^2+\frac2r\partial_r\right)\bar T_{rr}
  -\frac1r\partial_r\bar T_{\theta\theta}
  +2\left(\partial_r+\frac1r\right)\partial_z\bar T_{rz}
  +\partial_z^2\bar T_{zz}.
 \tag{7}
\]
Thus the \(r\theta\) and \(z\theta\) stresses do not contribute to
this mean scalar source. The formula follows by taking the divergence
of the cylindrical tensor twice; the curvature terms are retained.

For cylindrical Fourier coefficients of the complete fields, the exact
mean stresses are
\[
 \bar T_{ab}=\sum_{n\in\mathbb Z}
 \big((U_a)_n(e_b)_{-n}+(e_a)_n(U_b)_{-n}\big).
 \tag{8}
\]
At each preterminal time all fields are smooth, so this identity is
legitimate with convergent Fourier products. It distinguishes the
source regions as follows.

| Region of the actual reference | Components supplying the Euclidean mean pressure |
|---|---|
| Axisymmetric core and base | The mean response paired with all present radial, axial and angular base components, through the four stresses in (7) |
| Active correction annulus | Those mean products, plus opposite angular harmonics of the actual waves and response in (8) |
| Exact heat exterior \(U=K(r,t)e_\theta\) | Only \(\bar T_{\theta\theta}=2K\bar e_\theta\) survives in (7) |
| Fixed localization region | All actual localized products, including curl-cutoff terms; they remain in (5) |

In the exact exterior, setting \(b=\bar e_\theta\) gives the local
identity
\[
 \Delta\bar\pi=\frac2r\partial_r(Kb).
 \tag{9}
\]
Mean radial or axial response supplies \(r\theta,z\theta\) stresses
there, and hence no local scalar source in (9). This does not remove
the harmonic pressure arriving from outside the tube. Core and annular
sources, as well as matching nonzero harmonics, remain in the global
formula (5).

For the image term \(\pi_H\), continuous rotational selection is not
valid. Rotation by \(\pi/2\) does preserve the lattice, its Green
function, \(K\), and the target circle. Therefore the angular-mean
axial Hessian \(\overline{\partial_z^2\pi_H}\) annihilates tensor modes
whose cylindrical angular index is not in \(4\mathbb Z\).
Modes in \(4\mathbb Z\) are allowed;
they need not contribute, but symmetry does not eliminate them. For the
products in (8), the corresponding allowed total indices are
\(n+m\in4\mathbb Z\), rather than just zero. This statement uses equivariant
tensor rotation, including the rotation of the cylindrical basis.
There is no assumption that the actual global \(U,e\) have a lattice
rotation symmetry.

## 3. A spatially weighted bound for the missing harmonic part

Choose a smooth axisymmetric cutoff \(0\le\chi\le1\), equal to one near the
target exterior circle and supported in a slightly larger source-free
annular cylinder. Split \(T=\chi T+(1-\chi)T\) in (5). The near
Euclidean pressure has the exactly specified source
\[
 \Delta\overline{\pi_{E,\mathrm{near}}}
 =\frac2r\partial_r(\chi Kb).
 \tag{10}
\]
The remote Euclidean pressure is harmonic in the region where
\(\chi=1\). The image pressure is also harmonic there, since
\(\Delta\partial_i\partial_jH=0\). Their Hessians supply the missing
harmonic boundary data for the local Poisson equation. No boundary
condition has been imposed by this splitting.

For a target point \(x\) at distance at least \(d>0\) from the remote
stress support, the fourth derivative of \(G_E\) gives the actual bound
\[
 \begin{aligned}
 |\partial_z^2\pi_{E,\mathrm{remote}}(x)|
 &\le C\int\frac{|1-\chi(y)|\,|U(y)|\,|e(y)|}{|x-y|^5}\,dy\\
 &\le C\left(\int_{\mathrm{remote}}
               \frac{|U(y)|^2}{|x-y|^{10}}\,dy\right)^{1/2}\|e\|_2.
 \end{aligned}
 \tag{11}
\]
The same estimate can be angularly averaged on the target circle.
It keeps the physical distance weight and the actual core, annular,
exterior and cutoff contributions. The singular kernel is used only
off the diagonal; a \(d^{-5}\) kernel is not an integrable bound for
the unsplit near pressure.

For a simpler norm consequence, the same source estimates used in
[the global strain-cost lemma](global-strain-cost.md)
give
\[
 \|U(t)\|_\infty\le C\tau^{-1/2-h}
 \quad(1-\tau\le t\le1-\tau/2).
 \tag{12}
\]
Indeed the base has this amplitude; the primary waves have an extra
\(q^{h/2}\sqrt{1+|\log q|}\), the remaining cumulative wave and mean
classes have positive powers, and a fixed \(C^0\) diagonal tail is
bounded. Exact heat and fixed localization complete the global bound.
Using \(\int_{|x-y|\ge d}|x-y|^{-10}dy\le Cd^{-7}\), (11) gives
\[
 |\partial_z^2\pi_{E,\mathrm{remote}}(x)|
 \le C\tau^{-1/2-h}d^{-7/2}\|e\|_2.
 \tag{13}
\]
At a separation \(d\asymp R=\sqrt\tau\), this is
\[
 |\partial_z^2\pi_{E,\mathrm{remote}}(x)|
 \le C\tau^{-9/4-h}\|e\|_2.
 \tag{14}
\]
This is a genuine bound on the actual response pressure contribution.
It does not assign its sign. In particular, a small unweighted response
norm must be compared with this derivative and distance cost before
being interpreted as a small harmonic strain input.

## 4. A nonzero actual-reference test at separated exterior rings

The power in (14) cannot be improved for general \(L^2\) fields with
this separation scale, even if they are solenoidal, mean zero and
vanish in a neighborhood of the target. Here the reference \(U\)
remains the actual constructed field; only the response test is varied.

Fix \(t_0=1-\tau\), \(R=\sqrt\tau\), and choose a nonnegative,
nonzero smooth function \(\beta(\rho,Z)\), even in \(Z\), supported
in
\[
 a<\rho<b,\qquad |Z|<c,
 \qquad a>\sqrt{2X_{\rm ext}}.
\]
All of \(a,b,c\) are fixed. Normalize
\(2\pi\int\beta^2\rho\,d\rho\,dZ=1\). Define the real field
\[
 e_\tau(r,\theta,z)=R^{-3/2}\beta(r/R,z/R)e_\theta,
 \tag{15}
\]
extended by zero and then periodized. It is exactly solenoidal and
mean zero, and \(\|e_\tau\|_2=1\).

For sufficiently small \(\tau\), its entire support lies in the
actual heat exterior with all physical cutoffs one. To check this,
use \(q-z^2q^{2h}=\tau\): on \(z=RZ\) with bounded \(Z\),
\(q/\tau=1+O(\tau^{2h})\) uniformly. Hence
\(X=r^2/(2q)=\rho^2/2+o(1)>X_{\rm ext}\).
The exact exterior formula is
\[
 K(r,t_0)=R^{-1-2h}\mathcal K(\rho),\qquad
 \mathcal K(\rho)=\kappa\rho^{-1-2h}H(4/\rho^2)>0.
 \tag{16}
\]
The absence of corrections here is an actual support property,
not an approximation by the leading background.

The stress \(T_\tau=U\otimes e_\tau+e_\tau\otimes U\) is supported
only in this test annulus. Thus no unseen core or active-wave stress
is present in this test. Angular integration gives
\[
 \int T_\tau(y)\,dy=\operatorname{diag}(m_\tau,m_\tau,0),
 \quad
 m_\tau=\int K(e_\tau)_\theta\,dy
       =c_\beta R^{1/2-2h}>0,
 \tag{17}
\]
where \(c_\beta=2\pi\int\mathcal K\beta\rho\,d\rho\,dZ\).
Every first Cartesian moment of \(T_\tau\) vanishes: it is even
under \(y\mapsto-y\), using the even axial bump and the angular
tensor \(e_\theta\otimes e_\theta\).

Choose a fixed sufficiently large \(L\), exceeding several times
the rescaled support radius, and take the target ring
\(r=LR,\ z=0\). It too is in the actual exact exterior, with
fixed \(X_e=L^2/2>X_{\rm ext}\), for sufficiently small \(\tau\).
It is separated from the test support by a fixed multiple of \(R\).
Taylor expansion of the smooth remote kernel in (5), including the
vanishing first moments, gives on that entire ring
\[
 \partial_z^2\pi_E
 =m_\tau\,\partial_z^4G_E(LR,0,0)
   +O\left(\frac{m_\tau R^2}{(LR)^7}\right).
 \tag{18}
\]
The leading contraction uses
\(-m_\tau(\partial_{x_1}^2+\partial_{x_2}^2)G_E
=m_\tau\partial_z^2G_E\) away from the origin. Direct
differentiation gives the nonzero coefficient
\[
 \partial_z^4G_E(r,0,0)=-\frac9{4\pi r^5}.
 \tag{19}
\]
The implicit constant in (18) depends on the fixed test profile but
not \(L,R\) once \(L\) exceeds its support radius by a fixed factor.
Choosing \(L\) large once makes the remainder less than one quarter
of the leading magnitude. The periodic-image contribution satisfies
\(|\partial_z^2\pi_H|\le C\|T_\tau\|_1=C' m_\tau\), by
(5), and is smaller by a factor \(O((LR)^5)\). Therefore, for
sufficiently small \(\tau\), the full periodic pressure obeys
\[
 \overline{\partial_z^2\pi_{\mathbb T}[U(t_0),e_\tau]}(LR,0)
 \le -c_L\tau^{-9/4-h}<0.
 \tag{20}
\]
The notation makes explicit that this is the pressure functional of
the actual reference and the displayed test. All constants are fixed
before the remaining-time limit.

Replacing \(e_\tau\) by \(-e_\tau\) reverses (20). The two fields
have identical global norms of every Sobolev order, identical norm
data with any fixed positive spatial weight, and zero velocity jets
through every order in the target tube. They give opposite nonzero
harmonic pressure feedback there. More generally, multiplying (15)
by any scalar multiplies the pressure by the same scalar; its fixed
Sobolev costs are \(\|e_\tau\|_{H^s}\asymp_s R^{-s}\) for
nonnegative fixed integers \(s\).

This proves sharpness of the remaining-time power in the general
remote \(L^2\) estimate at comparable shrinking annular scales. It
also excludes a signed closure from local tube jets and norm values
alone. It does **not** show that the actual response (1) equals
either test, has this pressure sign, or obeys a matching lower bound.
The evolution and its prescribed force distinguish those possibilities.

## 5. What must be supplied to close the slow response

Equations (5), (7)–(11) isolate the data still needed: the actual
signed products of the response with the reference, weighted by the
remote pressure kernel, together with the near mean swirl and its
boundary trace. The known smooth force potential adds its own
harmonic component through (3). No adjustable \(p_{zz}\) has been
substituted for these fields.

Current unweighted response estimates can be inserted into (13),
but do not by themselves turn it into a bounded or signed harmonic
strain coefficient. The test (15) explains the derivative loss and
sign issue using the same actual heat geometry. Opposite angular
harmonics in the active annulus, core meridional response and the
smooth periodic-image term have not been silently discarded.

For the nonlinear comparison \(E=V-U\), with \(V\) unforced, the removed
force has the opposite sign to (1), and the pressure also contains the
stress \(E\otimes E\). That stress may occupy the full torus. The compact
support reduction and the linear signed functional above apply to the
cross stress \(U\otimes E+E\otimes U\); they do not replace the complete
nonlinear pressure.

The next estimate would have to control one of these actual signed
spatial integrals, or solve a global response problem that supplies
the required radial and axial traces. A local affine or single axial
mode calculation can then use those traces. The pressure functional
and the remote norm obstruction here do not supply them.

## Review boundary

The integration reviewer independently reviewed the complete argument, actual
exterior geometry and scope, and reproduced the four pressure controls in
the [shared symbolic companion](checks/check-force-removal.py):
Newtonian harmonicity, the fourth-derivative sign, the stress-mass
exponent and the final pressure exponent. The outgoing agent separately
reviewed the complete pressure decomposition, cylindrical source,
periodic angular selection, annular test, parity cancellation and
nonzero coefficient. Both reviews passed at the stated written scope.
The final clarifications restrict the lattice selection to the axial
Hessian and explicitly retain the extra nonlinear stress. These are
independent AI reviews of a written calculation, not a new Lean
verification, an external expert review or a proof that the actual
response excites the test fields.
