# Material phase of the primary wave and two averaging obstructions

8 September 2026. Restricted written source analysis, independently reviewed
at the scope recorded below. The primary
carrier's large spatial frequency does not supply a fast material-time
oscillation: its phase advances by a quantity tending to zero on the
currently studied windows, as long as the actual reference trajectory
remains in one valid label chart. Its leading gradient is nilpotent, but
a simple shear change and a pointwise normal-weighted energy each have a
specific additional cost. These are bounded obstructions to specified
estimates, not an instability theorem for the actual error or an exclusion
of every adapted norm. The
[nonlinear comparison](nonlinear-force-comparison.md)
has not been extended by this note.

The fixed source is
[OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538)
and its [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
SHA-256 `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
All source statements concern one fixed construction on the unit torus
at viscosity one.

## 1. Fix the physical material derivative and the label

Fix one label, one of its lifted rectangles, and its band \(Q\). Put
\[
\varepsilon=Q^h,\quad S_*=n^2\asymp(1+|\log Q|)^2,
\quad A=\tfrac12+h,\quad k=\lceil\varepsilon^{-1/2}\rceil.
\tag{1}
\]
Here \(n\) is the band index. Let \(\Phi\) be the phase (7.3),
\(n_\Phi=\nabla_*\Phi\), and \(\Theta=k\Phi\). In cylindrical
components, with the actual graph operators of (6.6), define
\[
\mathscr D=Q^{1+h}(\partial_t+U\cdot\nabla_x)
=t_*+u_{*,r}D_r+u_{*,\theta}R^{-1}\partial_\theta+u_{*,z}D_z,
\quad u_*=Q^AU,\quad R=r/\sqrt Q.
\tag{2}
\]
Its base part is
\(\mathscr D_B=t_*+bD_r+F\partial_\theta+GD_z\), with
\(u_{*,B}=(b,RF,G)\). These are physical derivatives after the source's
auxiliary evaluation, not derivatives with that variable held fixed.

Let \(X(t)\) be an actual reference trajectory starting at \(t_a\)
inside the label's valid enlarged slow box and lifted rectangle. Restrict
this domain, if necessary, so that the enlarged auxiliary rectangles of
all other labels with overlapping slow support are disjoint from it.
Lemma 6.1 supplies precisely this separation. Define \(t_{\rm exit}\)
as the first exit from this chosen chart, its allowed shell and its pulse
interval \(0<v<L_s\) from (6.11). All trajectory statements below hold only for
\[
t_b<\min\{1,t_{\rm exit}\},\qquad D=(t_b-t_a)Q^{-1-h}.
\tag{3}
\]
Lift the angle continuously when reading \(\Theta\) as a real phase
along the trajectory. Its exponential is already single valued by angular
integrality. No lower bound on the residence time is assumed, and no
phase is identified across different labels.

## 2. The carrier is nearly stationary in material time

The phase-defect estimate (7.9) gives
\[
\mathscr D_B\Phi=O(\varepsilon S_*^P).
\tag{4}
\]
For every fixed complete finite correction state, (9.9) gives
\[
u_*-u_{*,B}=(\beta,v,\gamma)+w,
\quad\beta\in\mathcal M^{19/10},\quad
v,\gamma\in\mathcal M^{9/10},\quad w\in\mathcal W^{1/2}.
\tag{5}
\]
The bound \(|n_\Phi|\le C\) is the actual value estimate (7.9).
Within the chart of §1 no other wave label contributes, by the exact
support separation (6.13), including after evaluation. This label's
harmonics all have the same \(\Phi\). Exact divergence and (7.39)
give, for each full curl amplitude \(a_m\),
\[
n_\Phi\cdot a_m\in\mathcal W^{1-\kappa_s},
\qquad \kappa_s=10^{-5}.
\tag{6}
\]
Indeed, divide the coefficient divergence by \(km\): its inverse gains
\(\varepsilon^{1/2}\), while a coefficient radial derivative loses
at most \(\varepsilon^{-\kappa_s}\). The transverse primary part
has zero normal component exactly; its curl correction retains the small
normal remainder. There are finitely many harmonics in a fixed state.

Thus the *full* material derivative satisfies
\[
|\mathscr D\Theta|
\le C\left(\varepsilon^{1/2}+\varepsilon^{2/5}
 +\varepsilon^{1/2-\kappa_s}\right)S_*^P
\le C\varepsilon^{2/5}S_*^P.
\tag{7}
\]
The mean corrections set the largest upper bound. For the completed
infinite sum, choose one fixed prefix whose physical velocity tail is
bounded by a prescribed \(q^N\), using (5.35) with the required curl
derivative. Its contribution to the physical derivative of \(\Theta\)
is at most \(CkQ^{-1/2}q^N\); multiply by \(Q^{1+h}\) to obtain
its contribution to \(\mathscr D\Theta\). Since \(q\asymp Q\), a sufficiently
large fixed \(N\) absorbs this into (7). This establishes the estimate
for the complete actual reference, with a fixed prefix and constants.

Integrating along the actual trajectory gives
\[
|\Theta(t_b,X(t_b))-\Theta(t_a,X(t_a))|
\le CD\varepsilon^{2/5}S_*^P.
\tag{8}
\]
It tends to zero for any \(D\) bounded by a fixed polynomial in
\(1+|\log Q|\). This includes both the nonlinear
\(D\asymp\sqrt{\log(1/Q)}\) window and the linear
\(D\asymp\log(1/Q)\) flight, provided the entire interval satisfies
(3). It does not prove that all trajectories have that residence time.

If initially \(|\sin\Theta|\ge c_0>0\), then during such a residence
interval it keeps its sign and magnitude at least \(c_0/2\) for small
\(Q\). This does not assert a lower bound on the wave amplitude there.
It shows why dividing a time integral by the large spatial frequency is
invalid: there is no lower bound on the material phase speed permitting
nonstationary time integration by parts.

## 3. Orientation has a different clock

Let \(v\) now denote the pulse coordinate, and \(L_s\asymp S_*\)
its full interval length. Equation (6.12) gives the exact identities
\[
D_rv=D_zv=\partial_\theta v=0,\qquad t_*v=1,
\qquad \mathscr Dv=1.
\tag{9}
\]
Thus the pulse advances by exactly \(D\), even when its carrier phase
hardly advances. At fixed slow and transverse coordinates, (7.9) gives
\(|\partial_vn_\Phi|\le C/S_*\), with \(|n_\Phi|\) bounded above
and away from zero. The frame \(B_\Phi\) in (7.8) therefore has
\(|\partial_vB_\Phi|\le C/S_*\). Write the real homogeneous primary
polarization as \(t^h=B_\Phi(z_+,z_-)^T\), and set \(r_-=z_-/z_+\).
Lemma 7.4 proves \(z_+>0\), \(|r_-|\le C/S_*\). Its Riccati
equation also gives \(|\partial_vr_-|\le C/S_*\), since its
off-diagonal coefficients are \(O(1/S_*)\). Hence
\[
\left|\partial_v(t^h/|t^h|)\right|\le C/S_*.
\tag{10}
\]
All other fixed coefficient derivatives of these unit vectors have
polynomial \(S_*\) bounds. In particular, the estimates
\(|D^It^h|\le C_IS_*^{P_I}P(v)\), \(|t^h|\ge cP(v)\), cancel
the pulse factor when differentiating its normalized direction.

The full normalized radial velocity is
\(O(\varepsilon^{1/2}S_*^P)\), while its base part is
\(O(\varepsilon)\); the full axial velocity is bounded for small
\(Q\). The coefficient rules (6.32) cost
\(\varepsilon^{-\kappa_s}S_*^P\) under \(D_r\) and
\(\varepsilon S_*^P\) under \(D_z\). The slow temporal derivative
also carries \(\varepsilon\). Consequently the cylindrical-component
unit vectors \(\widehat n=n_\Phi/|n_\Phi|\) and
\(\widehat t=t^h/|t^h|\) satisfy
\[
|\mathscr D\widehat n|_{\rm cyl}
+|\mathscr D\widehat t|_{\rm cyl}
\le C/S_*+C\varepsilon^{1/2-\kappa_s}S_*^P.
\tag{11}
\]
The actual velocity tail is absorbed by the same fixed-prefix procedure.
Their variation over (3) is at most the right side times \(D\), and
tends to zero when \(D=O(\log(1/Q))=O(\sqrt{S_*})\).

This statement uses a corotating cylindrical frame. Cartesian orientation
has the additional exact contribution
\[
\mathscr D q_{\rm cart}
=R_\theta\left(\mathscr D q_{\rm cyl}
 +\frac{u_{*,\theta}}{R}Jq_{\rm cyl}\right),
\quad J(a_r,a_\theta,a_z)=(-a_\theta,a_r,0).
\tag{12}
\]
Here \(R_\theta\) maps cylindrical to Cartesian components. The angular
speed is the base \(F\), up to small corrections, and is generally
order one in normalized time. Its accumulated angle can be large. An
orthogonal frame rotation alone does not decouple the full error PDE
or remove its pressure.

## 4. The nilpotent part and the cost of a shear change

The primary transverse wave on the label is
\[
U_{\rm pr}=Q^{-A}\sqrt\varepsilon\,
a\chi_{\rm slow}\chi_g\psi(v)t^h\cos\Theta,
\qquad n_\Phi\cdot t^h=0.
\tag{13}
\]
Its principal gradient, differentiating only the carrier, is
\[
\nabla U_{\rm pr}^{\rm carrier}=Q^{-1-h}N,
\quad N=-k\sqrt\varepsilon\,
a\chi_{\rm slow}\chi_g\psi(v)t^h\otimes n_\Phi\sin\Theta.
\tag{14}
\]
Pointwise \(\operatorname{tr}N=0\), \(N^2=0\), and
\(\|N\|\le CS_*^{1/4}\). Orthogonality also cancels the leading
carrier contribution to \((U_{\rm pr}\cdot\nabla)U_{\rm pr}\).
It does not cancel an arbitrary error's normal component interacting
with this wave.

The complete gradient includes the base term of size \(O(Q^{-1-h})\)
and further terms smaller by positive powers of \(Q\), allowing fixed
polynomial logarithms. The first-derivative proof in the
[global strain-cost note](global-strain-cost.md)
charges these terms: primary coefficient derivatives save
\((1/2-\kappa_s)h\), the cumulative \(\mathcal W^{17/25}\) remainder
saves \(9h/50\), means save more, and a fixed tail includes the complete
field. None may simply be removed from the subsequent error equation.

Even an exactly fixed nilpotent direction does not automatically yield
a near-identity coordinate change. For constant \(a\cdot n=0\), the
exact incompressible map
\[
\Psi_t(x)=x+d(t)a\cos(k n\cdot x)
\tag{15}
\]
has determinant one. Its Jacobian and inverse nevertheless contain
\(\mp d(t)k\,a\otimes n\sin(k n\cdot x)\). For velocity
\(d'(t)a\cos(k n\cdot x)\), the size of the coordinate derivative
is governed by \(k|d(t)|\), the accumulated shear, rather than by the
reciprocal frequency. On a constant-sign interval with non-negligible
amplitude it need not be small. This exact model identifies a cost;
it does not claim an actual lower bound on integrated primary amplitude.

## 5. Pressure defeats one simple normal-weighted metric

Consider the exact affine incompressible shear on \(\mathbb R^3\)
\[
U_{\rm sh}(x)=\sigma x_2e_1,
\quad N=\nabla U_{\rm sh}=\sigma e_1\otimes e_2,
\qquad \sigma>0.
\tag{16}
\]
This is a local model, not a compact finite-energy datum or the actual
reference. A Kelvin perturbation obeys the full-pressure equations
\[
\xi'=-N^T\xi,\qquad
b'=-Nb+2\xi\frac{\xi\cdot Nb}{|\xi|^2}-\nu|\xi|^2b,
\qquad \xi\cdot b=0.
\tag{17}
\]
With pressure convention \(p=\pi e^{i\xi\cdot x}\), its coefficient
is \(\pi=2i(\xi\cdot Nb)/|\xi|^2\). At one time take
\[
\xi=(e_1+e_2)/\sqrt2,\quad b=(-e_1+e_2)/\sqrt2,
\qquad H_\Lambda=\operatorname{diag}(1,\Lambda^2,1),\quad\Lambda\ge1.
\tag{18}
\]
The bare operator \(-N\) has norm \(\sigma/\Lambda\) in this
metric. But the inviscid part of (17) is \(b'=\sigma e_2/\sqrt2\),
and therefore the exact initial weighted rate is
\[
\frac12\frac d{dt}\log(b^*H_\Lambda b)
=\frac{\sigma\Lambda^2}{1+\Lambda^2}-\nu|\xi|^2
\ge\sigma/2-\nu.
\tag{19}
\]
The covector evolves as required by (17). The retained pressure restores
an order-\(\sigma\) coefficient after the unprojected matrix norm was
reduced. Thus this constant phase-normal penalty does not give a uniform
instantaneous cancellation over receiving covectors. It does not rule
out a metric depending on the receiving frequency and evolving with it,
nor prove growth of the actual forced or nonlinear error.

For a general pointwise symmetric metric \(H(x,t)\), the pressure
contribution to the energy equation is
\[
\int\pi\,\operatorname{div}(HE)\,dx.
\tag{20}
\]
Automatic preservation of every solenoidal field by multiplication with
\(H\) forces \(H\) to be a spatially constant scalar matrix: at the
principal-symbol level \(H\xi\) must be parallel to every \(\xi\),
so \(H=cI\); then \(\operatorname{div}(cE)=\nabla c\cdot E\)
forces \(c\) to be spatially constant. Special error classes or a
nonlocal metric can have additional structure. Equation (20) must be
estimated, not discarded from an arbitrary anisotropic energy.

## 6. The remaining obligation

The source supplies an almost material-stationary carrier and an almost
fixed nilpotent direction in a corotating frame during a valid residence.
It supplies no fast material-time averaging. A useful next estimate must
control a frequency-dependent or transported error norm with full pressure,
its time derivative, coordinate distortion, the base and cumulative
remainder, and transitions between labels. If it applies only to selected
polarizations, it must also prove that actual forcing and inherited
nonlinear error remain in that class.

No such invariant class or pressure-compatible estimate is proved here.
The \(\sqrt{\log}\) global strain loss is not removed, the nonlinear
window is not extended, and its restarts are not concatenated. Nothing
here contradicts the exterior quasimode obstruction to overly uniform
arbitrary-error stability bounds.

## Review boundary

The coordinating agent independently read the complete argument. A second
agent checked §§1–3 against the actual source's graph derivatives,
enlarged-label separation, coefficient classes, phase defect, homogeneous
polarization equation and full curl correction. A third agent independently
recomputed the shear map, Kelvin pressure, metric rate and solenoidal
multiplication statement in §§4–5. All three reviews passed at body
SHA-256
`41688c73ebad85844282df76a43e95474af4a27918b66e617ec474ee579a7c4c`.
The subsequent changes only identify the pulse interval explicitly,
spell out the normalization of the physical tail estimate, align its
interval notation, and record the reviews.

These are independent AI reviews of a restricted written source analysis,
not formal PDE certification or external expert acceptance. They establish
neither an invariant error class nor a comparison beyond the previously
proved finite window. No simulation or global continuation claim is made.
