# Leading geometry, symmetry parameters, and a coarse stability obstruction

8 September 2026. Bounded source extraction and a new consequence of the
reported inner geometry. No unforced singularity or perturbative stability
theorem is asserted.

Primary sources: OpenAI's [*Finite time blowup for
Navier–Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
§§3.1, 7.1, 9.4–9.5 and 10.4, and the
[formal source at commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
PDF SHA-256:
8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81.
This task inspected sources; it did not run a build or simulation.

**Concrete result.** The complete localized velocity in the paper satisfies
\[
\|\nabla U(t)\|_\infty\ge c(1-t)^{-1-h}
\tag{1}
\]
for all sufficiently late \(t<1\). Consequently the coarse coefficient
\(C_s\|U(t)\|_{H^{s+1}}\), \(s\ge3\), in the earlier
[force-removal criterion](force-removal-stability.md)
has a nonintegrable terminal history. With a nonzero projected forcing
input on a late subinterval, that criterion's scalar response grows at
least exponentially in \((1-t)^{-h}\). This concerns one norm estimate,
not symmetric strain, the actual linearized propagator, or the error
after modulation.

## 1. Two growth observables in the actual sources

At viscosity one set
\[
\tau=1-t,\quad A=\tfrac12+h,\quad D=\tfrac12-h,\quad 0<h<1/100,
\qquad
\tau=q(1-\eta^2),\quad z=q^D\eta,\quad X=\frac{r^2}{2q}.
\tag{2}
\]
On compact inner similarity regions, \(q\asymp\tau\). The leading field
in paper (3.2)–(4.3) is axisymmetric:
\[
u_\theta^{(0)}=q^{-A}E(X,\eta),\qquad
u_z^{(0)}=q^{-A}Z(X,\eta),\qquad
r u_r^{(0)}=V_0(X,\eta).
\tag{3}
\]
Here \(Z\) denotes the paper's axial profile \(U\). The radial and axial
core sizes are \(\tau^{1/2}\) and \(\tau^D\). Both leading tangential
components have size comparable to \(\tau^{-A}\) on suitable inner
regions; the radial component has size \(O(\tau^{-1/2})\). “Tangential”
includes the axial direction: both \(e_\theta\) and \(e_z\) are tangent
to a cylinder. These leading estimates do not classify every derivative
of the full corrected field.

**Azimuthal growth on a shrinking circle.** Paper Theorem 3.1(iv),
Proposition 9.9's Step 5, and (10.20)–(10.21) choose fixed
\(X_{\rm in}\in(0,X_a)\), \(e_0>0\), and prove
\[
r_\tau=\sqrt{2X_{\rm in}\tau},\qquad
U_\theta(r_\tau,\theta,0,1-\tau)
=\tau^{-A}\bigl(e_0+O(\tau^{2h})\bigr).
\tag{4}
\]
All annular wave and mean corrections vanish in this inner region.
The remaining background is axisymmetric. Thus (4) holds on the entire
circle, not only at the displayed representative \(\theta=0\).
The final cutoffs equal one there for small \(\tau\).

**Axial growth at the fixed origin.** The formal source uses an additional
exact observation. [FinalSlowBase.origin](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/FinalSlowBase.lean#L361)
gives
\[
U_{\rm base}(t,0)=j_{\rm ax}(1-t)^{-A}e_z,\qquad j_{\rm ax}>0.
\tag{5}
\]
[GermCandidateAssembly.origin_eventually_base and origin_blowup](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/GermCandidateAssembly.lean#L114)
retain it for the summed local velocity at all sufficiently late times.
[MixedPeriodicAssembly.periodicVelocity_speed_unbounded](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedPeriodicAssembly.lean#L322)
uses equality at the origin after localization and periodization.
Late time activation is one. The vanishing of positive-order axial
coefficients at the origin is retained in
[BaseResidual.baseVelocity_at_origin](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/BaseResidual.lean#L59).

Neither observation is a stated material particle trajectory. In
particular, (5) gives nonzero axial velocity at the origin; it is not
a stationary fluid particle. Smooth cylindrical swirl vanishes on the
axis, so (5) must not be called azimuthal growth. It also gives the exact
late identity \(\partial_tU(t,0)=A j_{\rm ax}\tau^{-A-1}e_z\).

## 2. Exact symmetries and construction parameters

Constant translations give
\[
U_{a,\sigma}(t,x)=U(t+\sigma,x+a),\quad
P_{a,\sigma}(t,x)=P(t+\sigma,x+a),\quad
f_{a,\sigma}(t,x)=f(t+\sigma,x+a).
\tag{6}
\]
They preserve the equation and viscosity, including on the fixed torus.
The terminal time becomes \(1-\sigma\), the singular point becomes
\(-a\), and (4) translates with remaining time \(1-\sigma-t\).
Infinitesimal velocity directions are \(\partial_tU,\partial_{x_i}U\).
This is an exact family of **forced** solutions with transformed forces
and generally transformed restart data. It does not preserve a specified
unforced datum merely by choosing these parameters.

On \(\mathbb R^3\), constant orthogonal rotations give
\(U_R(t,x)=R U(t,R^Tx)\), \(P_R(t,x)=P(t,R^Tx)\), and
\(f_R(t,x)=R f(t,R^Tx)\).
Only lattice-preserving orthogonal maps are isometries of a fixed torus.
Rotating a compact local construction and then periodizing it is a
different step, with support to be checked.

A constant Galilean boost is \(U_v(t,x)=U(t,x-vt)+v\), with translated
pressure and force. On the torus it changes the spatial mean. On
\(\mathbb R^3\), \(v\ne0\) destroys finite energy for a localized velocity.
Continuous spatial dilation changes the period lattice and is not a
continuous symmetry of a fixed torus. None of these transformations
removes a nonzero projected force.

The exponent \(h\), axial datum \(j_{\rm ax}\), profile normalization,
cone-loop choices and label phases are construction parameters, not
additional exact symmetries. Changing them requires retaining the
profile equations, moments, pressure, integer angular frequencies and
all residual estimates. Files named ParametricModulation or
RadialModulation concern such constructions; they do not supply
perturbative stability of the singular solution.

Time-dependent parameters contribute additional momentum terms.
Removing translation or time-shift components of an error therefore
requires modulation equations and a remaining-error estimate.

## 3. A gradient bound for the complete field

On the inner circle, axisymmetry gives
\[
(e_\theta\cdot\nabla)U
=\frac1r\partial_\theta(U_r e_r+U_\theta e_\theta+U_z e_z)
=\frac1r(U_r e_\theta-U_\theta e_r).
\tag{7}
\]
The basis derivatives are \(\partial_\theta e_r=e_\theta\) and
\(\partial_\theta e_\theta=-e_r\). Consequently
\[
\|\nabla U(t)\|_\infty
\ge\frac{|U_\theta(r_\tau,0,t)|}{r_\tau}
\ge\frac{e_0}{2\sqrt{2X_{\rm in}}}\tau^{-A-1/2}
=c_0\tau^{-1-h}.
\tag{8}
\]
This uses the actual complete field where nonaxisymmetric corrections
vanish. Use the Euclidean operator norm for the gradient; other fixed
finite-dimensional conventions change only the constant.

For integer \(s\ge3\), Sobolev embedding on the fixed domain yields
\[
a_s(t):=C_s\|U(t)\|_{H^{s+1}}\ge\kappa_s\tau^{-1-h},\qquad
\int_{t_1}^t a_s(r)\,dr
\ge\frac{\kappa_s}{h}
\bigl(\tau^{-h}-(1-t_1)^{-h}\bigr)
\tag{9}
\]
for sufficiently late \(t_1<t<1\). This applies on the whole space and
to the periodized field.

For the earlier coarse criterion's scalar response,
\[
\Phi_s(t)=\int_{t_0}^t e^{\int_r^t a_s(\xi)d\xi}
                 \|\mathbb P f(r)\|_{H^s}\,dr,
\]
a nonzero projected force norm on a subinterval before a late \(t_1\)
gives \(\Phi_s(t_1)>0\). Positivity and (9) imply
\[
\Phi_s(t)\ge\Phi_s(t_1)
 \exp\!\left[\frac{\kappa_s}{h}
 \bigl(\tau^{-h}-(1-t_1)^{-h}\bigr)\right],
\qquad \int_{t_0}^1\Phi_s(t)\,dt=\infty.
\tag{10}
\]
That criterion's integral smallness condition therefore fails under the
stated nonzero-input hypothesis. The separate
[terminal-force calculation](terminal-force-nonzero.md)
discharges it for every late restart of the external flow.

Equation (8) is **not** a comparable lower bound on symmetric strain.
Rigid rotation \(U=\Omega(-x_2,x_1,0)\) has
\(|U_\theta|/r=|\Omega|\) and \(S(U)=0\).
Equation (10) concerns a positive norm majorant; it does not prove
exponential growth of the actual linearized flow or exclude an estimate
retaining rotation and other cancellations.

## 4. Actual oscillatory derivative costs

The annular waves have three velocity components. Their radial–azimuthal
and radial–axial covariances realize the two tangential stress components.
Paper (7.3) uses label phases
\[
\Phi=p\theta+p_z Z/\varepsilon+x_0R-v(pF+p_zG),
\qquad kp\in\mathbb Z\setminus\{0\}.
\tag{11}
\]
Here \(Z\) is a normalized axial coordinate, and \(F,G\) describe the
label's angular and axial background velocities. The two phase families
give different stress directions. At nonzero profile values the wave
amplitude and wavelength scale as \(q^{-1/2-h/2}\) and \(q^{1/2+h/2}\),
up to logarithmic and envelope factors. Small amplitude relative to the
core does not give small physical derivatives.

Lemma 9.8 makes the costs precise. On a chart with \(q\asymp Q\), its
conservative phase estimates use
\[
s_x=\tfrac12+2h,\quad s_t=1+\tfrac32h,\qquad
|\nabla_x^a\partial_t^b e^{ikm\Phi}|
\le C_{a,b,m}Q^{-a s_x-b s_t}S_*^{P_{a,b,m}}.
\tag{12}
\]
For the stage tuple \(Z_j=(\text{potential},\text{direct swirl},\text{pressure})\)
and velocity increment \(\Delta u_j\), it proves
\[
|Z_j|_m+|\Delta u_j|_m
\le C_{j,m}q^{g_j-\ell_m}(1+|\log q|)^{P_{j,m}},\quad
g_j=\frac h{10}j,\quad
\ell_m=2A+(m+1)(1+3h/2).
\tag{13}
\]
The loss \(\ell_m\) is independent of stage; constants and logarithmic
powers need not be. Recovery of velocity by an additional curl derivative
is charged. The finite harmonic range can grow with stage.
These upper bounds do not themselves prove instability.

The formal [PhysicalResidualJetBounds.mode_jet_bound_local](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PhysicalResidualJetBounds.lean#L78)
retains amplitude and phase derivative factors.
[DiagonalJetBounds](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalJetBounds.lean#L196)
bounds an actual tail by \(2^{-J}q^{g(J+1)-L(m)}\), with a sufficiently
large prefix for the requested derivative order and decay power.
All-order residual flatness does not place the entire velocity in a
small fixed Sobolev ball.

The definite new consequence is (8)–(10). A subsequent stability estimate
must preserve the actual rotation/transport and annular corrections,
while treating exact translation and time-shift directions appropriately.
Neither derivative bookkeeping nor the existence of symmetry parameters
supplies that estimate.

## 5. A competing effect: negative centrifugal discriminant in the heat exterior

The large rotational contribution in (8) is not, by itself, a reason
to expect damping. The actual uncut heat exterior has
\[
K(r,t)=\kappa r^{-1-2h}H(\zeta),\qquad
\zeta=\frac{4\tau}{r^2},\quad \kappa>0,\quad
\Omega=\frac Kr.
\tag{14}
\]
This is paper (10.7) and
[RadialHeatProfile.radialProfile_source_formula](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/RadialHeatProfile.lean#L694).
The source proves \(H>0\), \(H'<0\), and
\(0<-\zeta H'/H<h\) for \(\zeta>0\):
[profile_derivWithin_neg and profile_logSlope_lt](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/RadialHeatProfile.lean#L423).
Consequently
\[
\partial_r\log(rK)=-\frac2r\left(h+\frac{\zeta H'}H\right),\qquad
\mathcal D:=\frac1{r^3}\partial_r(rK)^2
=-4\left(h+\frac{\zeta H'}H\right)\Omega^2<0.
\tag{15}
\]
Here \(\mathcal D\) is the centrifugal discriminant, distinct from
the coordinate exponent \(D\) in (2).

There is also a separate **actual exterior strain** estimate. Put
\(g=h+\zeta H'/H>0\). Then \(K_r=-(1+2g)\Omega\), and the
cylindrical gradient block in the \((e_r,e_\theta)\) plane is
\(\left(\begin{smallmatrix}0&-\Omega\\K_r&0\end{smallmatrix}\right)\).
Thus \(S_{r\theta}=-(1+g)\Omega\), and the three strain eigenvalues
are \(-(1+g)\Omega,0,(1+g)\Omega\). At fixed
\(X_e>X_{\rm ext}\), \(z=0\), \(r^2=2X_e\tau\), this gives
the actual energy coefficient
\(a_2(t)=\|\max(0,\lambda_{\max}(-S(U(t))))\|_\infty
\ge c\tau^{-1-h}\).
Together with the [nonzero projected terminal force](terminal-force-nonzero.md),
the same positive-integral argument as (10) makes the coarse \(L^2\)
energy majorant grow at least exponentially in \(\tau^{-h}\).
This additional conclusion uses the exact exterior heat profile;
it did not follow from the inner-circle gradient estimate alone.
It still does not lower-bound the actual perturbation error.

One can inspect its **frozen principal symbol**, including its leading
pressure projection. At a fixed positive radius and time, take a
meridional covector \(k=(k_r,0,k_z)\ne0\). Write the leading
divergence-free meridional velocity as
\[
(u_r,u_z)=w(k_z,-k_r)/|k|,\qquad \chi_k=k_z/|k|,
\quad B=K_r+K/r.
\]
The locally frozen axisymmetric equations give
\[
(\partial_t+\nu|k|^2)
\begin{pmatrix}w\\u_\theta\end{pmatrix}
=
\begin{pmatrix}0&2\Omega\chi_k\\-B\chi_k&0\end{pmatrix}
\begin{pmatrix}w\\u_\theta\end{pmatrix},
\quad
\lambda_\pm=-\nu|k|^2\pm\sqrt{-\mathcal D}\,\frac{|k_z|}{|k|}.
\tag{16}
\]
Indeed \(2\Omega B=\mathcal D\). The factor \(|k_z|/|k|\) is required
by pressure projection; it is not obtained by discarding pressure.
When \(k_z=0\) this particular coupling vanishes.

The source's exterior permits a concrete scaling for this symbol.
Fix \(X_e>X_{\rm ext}\), set \(z=0\), \(r=\sqrt{2X_e\tau}\).
Then \(\zeta=2/X_e\) is fixed, the annular corrections vanish, and the
final cutoffs equal one for late time. There are fixed positive
constants \(C_e,\gamma_e\) such that
\[
\Omega=C_e\tau^{-1-h},\qquad
\sqrt{-\mathcal D}=\gamma_e\tau^{-1-h}.
\]
For fixed \(|k|=M\tau^{-1/2}\) and fixed
\(0<\chi_0=|k_z|/|k|\le1\), the symbol has
\[
\lambda_+=\gamma_e\chi_0\tau^{-1-h}-\nu M^2\tau^{-1}>0
\quad\hbox{when}\quad
\tau^h<\frac{\gamma_e\chi_0}{\nu M^2}.
\tag{17}
\]
The actual source here has \(\nu=1\); (16) displays the viscosity
dependence of the frozen algebra. Choose fixed large \(M\) if a
short-wavelength interpretation is intended.

Equations (16)–(17) are not an actual unstable NS mode or a lower
bound on its propagator. They omit coefficient variation in time and
radius, envelope/localization effects, cylindrical divergence \(u_r/r\),
the curvature terms \(-\nu u_r/r^2,-\nu u_\theta/r^2\), and the other
corrections to a flat Fourier model. The condition \(|k|r\gg1\) alone
does not control their accumulated effect. Nor has the actual
projected force been shown to excite this channel.
The sign (15) and the symbol (16) were independently checked by another
AI agent; no mode realization or formal certificate is claimed.

This source-specific channel gives a concrete test for a future
modulated estimate: it must handle the centrifugal coupling in the
heat exterior, in addition to separating exact symmetry directions
and retaining the annular wave errors.
