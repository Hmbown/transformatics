# Slowly varying exterior response and the missing pressure boundary data

8 September 2026. Restricted written analysis; reviewed at the stated scope.
The lowest axisymmetric pressure moments admit an exact local response
family, including a nonlinear strained-vortex completion. Their meridional
strain rate is not determined by local equations: a harmonic pressure
coefficient and boundary traces remain free. A separate estimate for the
actual linearized operator shows that sufficiently thin radial packets
with slow axial variation are dissipative. Neither result computes the
actual global force response or removes the force.

The reference is the same viscosity-one solution on the unit torus as in
[the exterior quasimode note](exterior-quasimode.md).
The [force-coupling note](exterior-force-coupling.md)
identifies the global pressure moment used below but does not determine
its value or sign. Every local construction in this note remains inside
the source-valid heat exterior. No affine field is silently periodized.

## 1. The actual averaged local equations retain an unknown pressure

Fix \(t_0=1-\tau\), \(0<\theta<1\), and the interval
\(I=[t_0,t_0+\theta\tau]\). On the fixed source tube, write
\[
 U=K(t,r)e_\theta,\quad
 \Omega=K/r,\quad B=K_r+K/r,\quad
 K_t=\nu\mathcal L K,\qquad
 \mathcal L=\partial_r^2+r^{-1}\partial_r-r^{-2}.
\tag{1}
\]
Here \(\nu=1\) for the actual reference. The complete physical force
vanishes on this tube. Globally put
\(w=\mathbb P f=f-\nabla\phi\), with
\(\phi=\Delta^{-1}\operatorname{div}f\). Thus locally
\(w=-\nabla\phi\), and \(\phi\) is harmonic on the tube.

Consider the linear response with input \(+w\), zero at \(t_0\).
The force-removal error has the opposite linear input. Average cylindrical
components over complete Euclidean circles inside the chart, and write
the resulting velocity as \(v=(v_r,b,v_z)\), the averaged response
pressure as \(p\), and the averaged force potential as \(\bar\phi\).
The coefficients of (1) are independent of both \(z\) and angle;
averaged angular derivatives vanish. Consequently the actual angular
mean obeys the exact local system
\[
\begin{aligned}
 (v_r)_t-\nu(\mathcal L+\partial_z^2)v_r-2\Omega b+p_r
   &=-\bar\phi_r,\\
 b_t-\nu(\mathcal L+\partial_z^2)b+Bv_r&=0,\\
 (v_z)_t-\nu(\partial_r^2+r^{-1}\partial_r+\partial_z^2)v_z+p_z
   &=-\bar\phi_z,\\
 r^{-1}(rv_r)_r+(v_z)_z&=0.
\end{aligned}
\tag{2}
\]
This averaging is a local identity, not a claim that arbitrary rotations
are global symmetries of the unit torus.

The complete meridional pressure has not disappeared. Setting
\(\widehat p=p+\bar\phi\) makes the explicit right sides of (2) zero,
but then \(\widehat p\) has unknown boundary values inherited from the
global response. Since \(\Delta\bar\phi=0\) on the tube, its contribution
is a harmonic boundary datum for that local Poisson problem. Deleting
this contribution after moving it into pressure would delete the forcing
mechanism rather than estimate it.

For later use, the meridional vorticity and streamfunction satisfy
\[
 \omega=\partial_zv_r-\partial_rv_z,\quad
 v_r=-\Psi_z/r,\quad v_z=\Psi_r/r,
 \quad
 -r\omega=(\partial_r^2-r^{-1}\partial_r+\partial_z^2)\Psi,
\]
\[
 \omega_t-\nu(\mathcal L+\partial_z^2)\omega
   =2\Omega\partial_z b.
\tag{3}
\]
The elliptic equation for \(\Psi\) still needs its boundary data and
permits an irrotational meridional contribution. The coupled vorticity
and azimuthal equations do not by themselves fix that contribution.

## 2. The harmonic quadrupole leaves one strain function undetermined

For a prescribed harmonic polynomial force potential, let
\[
 \phi_2(t,r,z)=g(t)z+\frac{M(t)}2
                 \left(z^2-\frac{r^2}{2}\right).
\tag{4}
\]
Then \(-\nabla\phi_2=(Mr/2)e_r-(g+Mz)e_z\). On an open annular
cylinder, choose any smooth functions \(a(t),u(t)\), and set
\[
 v_r=a(t)r,\qquad v_z=-2a(t)z+u(t),\qquad b=b(t,r).
\tag{5}
\]
Divergence vanishes exactly; the meridional vorticity is zero. System (2)
with \(\bar\phi=\phi_2\) holds if
\[
 b_t-\nu\mathcal Lb=-a(t)\,rB(t,r),
\tag{6}
\]
and if its pressure is
\[
\begin{aligned}
 p(t,r,z)={}&\left(\frac{M}4-\frac{a'}2\right)r^2
       +\left(a'-\frac M2\right)z^2-(g+u')z\\
       &+2\int_{r_*}^{r}\Omega(t,\rho)b(t,\rho)\,d\rho+C(t).
\end{aligned}
\tag{7}
\]
The lower integration radius is any fixed interior reference radius.
Direct substitution verifies every component. In particular,
\[
 \Delta p=\frac2r\partial_r(r\Omega b).
\tag{8}
\]
All terms involving \(M\) and \(a'\) cancel in this Poisson equation.
Their difference is harmonic and therefore invisible to the local
Poisson source. The exact meridional relation is
\[
 a'=\frac12(p_{zz}+M).
\tag{9}
\]
It closes only when the global pressure or equivalent boundary data
supplies \(p_{zz}\). The axial translation similarly obeys
\(u'=-g-p_z(t,r,0)\) for this family.

The centrifugal term \(2\Omega b\) is radial and independent of \(z\).
It is exactly a gradient, the last integral in (7), and contributes
nothing to (3). Thus the lowest harmonic quadrupole does not create a
closed two-variable centrifugal feedback equation for \(a,b\). This is
a cancellation for this particular local ansatz, not a proof that the
actual angular mean stays in the ansatz.

With zero local initial response require \(a(t_0)=u(t_0)=b(t_0,r)=0\).
For consistency with the actual global restart, whose response pressure
is initially constant, one further needs
\(a'(t_0)=M(t_0)/2\), \(u'(t_0)=-g(t_0)\) in this polynomial model.
These initial constraints still leave the subsequent harmonic pressure
and the full boundary trace undetermined.

## 3. An explicit nonautonomous azimuthal response

Define \(\mathcal D=r\partial_r+1\). Since
\[
 rB=\mathcal D K,\qquad [\mathcal L,\mathcal D]=2\mathcal L,
\tag{10}
\]
the heat equation gives
\[
 (\partial_t-\nu\mathcal L)\mathcal D K=-2\nu\mathcal L K,
 \qquad
 (\partial_t-\nu\mathcal L)\mathcal L K=0.
\]
For the prescribed \(a\), put
\[
 A_1(t)=\int_{t_0}^t a(s)\,ds,\qquad
 A_2(t)=\int_{t_0}^t(t-s)a(s)\,ds,
\]
\[
 \boxed{\ b_p(t,r)=-A_1(t)\mathcal D K(t,r)
                         -2\nu A_2(t)\mathcal L K(t,r).\ }
\tag{11}
\]
As \(A_1'=a\) and \(A_2'=A_1\), differentiating (11) proves (6)
exactly. It starts at zero. No frozen-time approximation or omission of
viscosity has been made.

This is a local particular solution with its own boundary trace. Any
solution of the homogeneous azimuthal heat equation can be added if the
boundary data permit it. In particular, zero initial values on an open
annular region do not remove later boundary input. Formula (11) is not
asserted to be the actual global response.

One useful exact choice is
\[
 a(t)=\frac12\int_{t_0}^t M(s)\,ds,\qquad
 u(t)=-\int_{t_0}^t g(s)\,ds.
\tag{12}
\]
Then all polynomial terms in (7) vanish, leaving only the radial
centrifugal pressure. For bounded prescribed \(M,g\), (11) gives a
concrete finite-window response with no meridional feedback.

To quantify this choice, let \(R\asymp\sqrt\tau\) and
\(L=\tau^{1/2-h}\), and restrict to the fixed source tube on \(I\).
The exact heat-profile bounds give
\[
 |\mathcal D K|+\nu\tau|\mathcal L K|
 \le C\tau^{-1/2-h},
\]
with one extra radial derivative costing \(C/R\). Consequently, for
\(\sup_I|M|\le M_*\),
\[
 |a|\le C M_*\tau,\quad |b_p|\le C M_*\tau^{3/2-h},\quad
 |\partial_r b_p|+|b_p|/r\le C M_*\tau^{1-h}.
\tag{13}
\]
The varying part of \(v_z\) is \(O(M_*\tau L)\), the radial velocity
is \(O(M_*\tau R)\), and the separate uniform axial velocity is bounded
by \(\tau\sup_I|g|\). These estimates concern exactly (11)–(12).
They do not bound the actual response without matching its pressure
and boundary data.

For the actual smooth global \(\phi\), put
\(g(t)=\phi_z(t,0)\), \(M(t)=\phi_{zz}(t,0)\), and
\(D(t)=\Delta\phi(t,0)\). Terminal force flatness implies \(D(1)=0\),
so smoothness gives \(D(t)=O(\tau)\) on \(I\). Angular Taylor expansion
then gives
\[
 -\bar\phi_r=\frac{M(t)}2r+
 O\big(r(\tau+|z|+r^2)\big),\qquad
 -\bar\phi_z=-g(t)-M(t)z+O(z^2+r^2).
\tag{14}
\]
The harmonic quadrupole is therefore a precise candidate leading input.
The stated remainder is a source expansion, not a response estimate.
Inverting the global linearized equation with its unknown boundary
pressure is a further step, which (14) does not justify automatically.

## 4. The affine family has an exact nonlinear local completion

There is a classical nonlinear explanation for the cancellation. For an
arbitrary smooth prescribed \(a(t)\), define the full local velocity
\[
 V=a(t)r e_r-2a(t)z e_z+W(t,r)e_\theta.
\tag{15}
\]
It solves unforced ordinary Navier–Stokes on its open cylindrical domain
if and only if
\[
 W_t+a(t)(rW_r+W)=\nu\mathcal L W,
\tag{16}
\]
with pressure, up to a time-dependent constant,
\[
 P=-\frac{a'+a^2}{2}r^2+(a'-2a^2)z^2
       +\int_{r_*}^{r}\frac{W(t,\rho)^2}{\rho}\,d\rho.
\tag{17}
\]
Indeed, radial acceleration is \((a'+a^2)r-W^2/r\), axial acceleration
is \((-2a'+4a^2)z\), and both meridional viscous terms vanish. Their
pressure gradients cancel them exactly. The azimuthal equation is (16).
The pressure-controlled strain equation is
\(a'=2a^2+P_{zz}/2\); the local pressure does not select \(a\).

Equation (16) is reduced to radial heat by an exact change of variables.
Put
\[
 A(t)=\int_{t_0}^t a(s)\,ds,\qquad
 y=e^{-A(t)}r,\qquad
 s(t)=t_0+\int_{t_0}^t e^{-2A(q)}\,dq,
\]
\[
 W(t,r)=e^{-A(t)}\mathcal W(s(t),y),\qquad
 \partial_s\mathcal W=\nu\mathcal L_y\mathcal W.
\tag{18}
\]
Substitution leaves exactly
\(e^{-A}s'\mathcal W_s=\nu e^{-3A}\mathcal L_y\mathcal W\).
The heat solution must be defined throughout the transformed domain;
no extension past its lifetime is assumed. Differentiating (18) at zero
strain, with \(\mathcal W=K\), recovers (11), including its second term.

This strained-vortex change of variables belongs to the classical
Burgers/Lundgren setting. Lundgren's author-written
[A small-scale turbulence model, §2](https://web.stanford.edu/group/ctr/Summer/SP92/05_LUNDGREN.pdf)
describes the time-dependent strain transformation and the rescaled heat
time; his [1982 paper](https://ntrs.nasa.gov/citations/19830036139)
provides its earlier context. The equations here are checked directly;
no novelty claim for that transformation or imported stability theorem
is made.

The fields \(ar e_r-2az e_z\) and the quadratic pressure are not periodic.
These are exact local solutions and boundary prescriptions, not solutions
on the original torus with its datum. Choosing \(a\) singular merely
prescribes singular boundary/strain behavior. It is not a construction of
an admissible unforced singularity.

## 5. Slow axial variation conflicts with thin radial localization

There is also an obstruction involving the actual full operator, without
an artificial pressure closure. Let \(v\) be any smooth compactly supported
axisymmetric solenoidal vector field in the source tube. Suppose its radial
support lies in an annulus of width \(d\le\epsilon_0R\), with \(r\asymp R\),
and suppose its axial variation obeys
\[
 \|\partial_z v_z\|_2\le\frac QL\|v\|_2,
 \qquad L=\tau^{1/2-h},
\tag{19}
\]
for a fixed \(Q<\infty\). This is a derivative condition on the actual
compact field, not an incompatible assumption of both compact support
and strict Fourier support. Norms are on the original unit torus.

Incompressibility gives
\((rv_r)_r=-r\partial_zv_z\). Radial Poincaré, using compact support,
and \(r\asymp R\) imply
\[
 \|v_r\|_2\le C d\|\partial_zv_z\|_2
 \le C Q(d/L)\|v\|_2.
\tag{20}
\]
The same weighted radial Poincaré inequality gives
\(\|\nabla v\|_2^2\ge c d^{-2}\|v\|_2^2\). Derivatives of the
cylindrical basis add nonnegative terms to this dissipation.

For the actual full projected linearized generator,
\[
 \operatorname{Re}\langle v,\mathcal A(t)v\rangle
 =-\nu\|\nabla v\|_2^2+
 \int(2\Omega-B)\operatorname{Re}(\overline{v_r}v_\theta)\,dx.
\tag{21}
\]
Pressure cancels against the solenoidal field globally. The basis rotation
in \(U\cdot\nabla v\) and the curvature in \(v\cdot\nabla U\) are already
included: their net coupling is \(2\Omega-B=K/r-K_r\).
On \(I\), the exact local heat bounds imply
\(|2\Omega-B|\le C\tau^{-1-h}\). Therefore
\[
 \boxed{\quad
 \operatorname{Re}\langle v,\mathcal A(t)v\rangle
 \le\left(CQ\tau^{-1-h}\frac dL-\frac{c\nu}{d^2}\right)\|v\|_2^2.
 \quad}
\tag{22}
\]
Set \(d=\epsilon R\). Since \(R/L\asymp\tau^h\), this becomes
\[
 \operatorname{Re}\langle v,\mathcal A(t)v\rangle
 \le\tau^{-1}\left(CQ\epsilon-c\nu\epsilon^{-2}\right)\|v\|_2^2.
\tag{23}
\]
For fixed \(Q,\nu>0\) and sufficiently small \(\epsilon\), it is strictly
negative, uniformly on the full interval \(I\). In particular no such
unit field is a positive quasimode with relative defect less than one:
for \(\lambda>0\), (23) implies
\[
 \|[\mathcal A(t)-\lambda]v\|_2\ge\lambda\|v\|_2.
\tag{24}
\]
This rules out the tempting construction that keeps the natural slow
axial variation but shrinks radial support to make the background nearly
constant. Viscous radial cost then beats the possible energy coupling.
It does not assert that a true solution remains supported in this annulus
or preserves (19), and it supplies no decay theorem for the global response.

At \(d\asymp R\), the argument has no automatic sign: both competing
terms have size \(\tau^{-1}\), with fixed constants. The corresponding
frozen-symbol bookkeeping gives the same balance. With
\(k_z\asymp L^{-1}\), \(k_r\asymp R^{-1}\), the pressure factor is
\(\chi\asymp R/L=\tau^h\), the centrifugal rate has size
\(\tau^{-1-h}\chi\asymp\tau^{-1}\), and radial viscosity has size
\(\nu R^{-2}\asymp\nu\tau^{-1}\). But the coefficients and curvature
vary by order one across such a radial support. The frozen symbol alone
cannot decide that full radial problem.

## 6. The exact remaining low-frequency question

The leading angularly averaged global pressure moment supplies a harmonic
quadrupole candidate, not a closed meridional amplifier. Equations
(5)–(13) give an exact, time-dependent local realization with specified
pressure and boundary trace. Equations (15)–(18) explain its nonlinear
local completion. Neither identifies the actual global harmonic pressure.

To obtain a force-response conclusion one must solve or bound the full
radial/axial problem at radial scale \(R\), retaining its meridional
pressure boundary data and the global input. A nonzero axial derivative
of \(b\) can drive meridional vorticity through (3); that mechanism is
absent in the affine family and is not excluded for the actual response.
Even the sign or nonvanishing of the first global moment remains unknown.
The actual dissipativity obstruction (23) prevents repairing this gap by
arbitrarily thin radial localization while keeping slow axial variation.
No force removal or unforced singularity is proved here.


## 7. Verification record

The integration reviewer independently read the full note and passed the local
averaged equations, pressure signs, undetermined affine strain, heat
commutator response, nonlinear transformation, Taylor-input expansion,
and thin-annulus energy obstruction. Avicenna independently checked the
weighted radial Poincaré step, the exact cylindrical energy coupling,
all scale powers in (22)–(23), and the nonnegative viscous curvature.
No mathematical correction was requested.

Nine separate exact symbolic checks passed: the linear radial and axial
pressure equations; the pressure Poisson identity; the heat commutator;
the particular azimuthal response; the nonlinear radial and axial
equations; the nonlinear pressure/strain relation; and the strained heat
transformation. The author-written Lundgren reference was opened and
its §2 transformation read. These are written and algebraic checks,
not a formal PDE certificate. No simulation or full build was run.
The actual operator result is (22)–(24); the affine and nonlinear families
remain local solutions with prescribed boundary traces.
