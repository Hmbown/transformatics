# The natural-width radial response with explicit boundary input

8 September 2026. Restricted written analysis, independently reviewed at
the stated scope.
At the natural radial width, the low-axial-frequency problem has an exact
scaled viscous system. A constant weighted energy symmetrizes its two
couplings sufficiently to give a uniform finite-window estimate and an
explicit sufficient damping threshold. Both the heat-profile variation
and cylindrical curvature remain. Applying this estimate to the actual
global response requires its radial traces and axial matching input;
those data are not supplied by the local coefficient calculation.

The reference, unit torus, and fixed exterior tube are those of
[the quasimode note](exterior-quasimode.md). The
[low-axial note](low-axial-response.md) explains why a local
harmonic pressure coefficient does not determine its own boundary data.
This note addresses the natural radial scale, without shrinking the
radial annulus to freeze its coefficients. No new simulation is used.

## 1. Exact coefficient scaling and the conditional axial mode

Fix \(t_0=1-\tau\), a number \(0<\vartheta<1\), and a fixed interval
\(J=(\rho_-,\rho_+)\), \(0<\rho_-<\rho_+\), such that
\(r=\sqrt\tau\,\rho\), \(\rho\in J\), remains inside the source's
persistent heat tube. Its relative width is fixed, not tending to zero.
Put
\[
 s=(t-t_0)/\tau\in[0,\vartheta],\quad
 \varepsilon=\tau^h,\quad L=\tau^{1/2-h},\quad
 k_z=\alpha/L,\qquad \alpha>0\ \text{fixed}.
\tag{1}
\]
The exact exterior swirl is
\[
 K(t,r)=\kappa r^{-1-2h}H(4(1-t)/r^2).
\]
Define the dimensionless coefficients
\[
 \omega(\rho,s)=\kappa\rho^{-2-2h}
 H\!\left(\frac{4(1-s)}{\rho^2}\right),\qquad
 g(\rho,s)=h+\zeta H'(\zeta)/H(\zeta),
 \quad \zeta=4(1-s)/\rho^2.
\tag{2}
\]
Then, exactly,
\[
 \Omega=\tau^{-1-h}\omega,\qquad B=-2\tau^{-1-h}g\omega.
\tag{3}
\]
The source gives \(0<g<h\), and the compact \((\rho,s)\) rectangle gives
fixed finite constants
\[
 0<g_*:=\sup g<h,
 \qquad \omega_*:=\sup|\omega|<\infty.
\tag{4}
\]
These coefficients do not depend on \(\tau\). Viscosity is one for the
actual source; we retain a fixed \(\nu>0\) in the model formulas.

Consider a complex axial mode proportional to \(e^{ik_z z}\) in the
axisymmetric local linearized equations. This is an exact separation for
an auxiliary cylinder with matching periodic axial traces, or for a
specified whole-line exterior problem. It is not automatic for the
restriction of the actual torus solution to a short axial interval.
The physical tube contains \(|z|<c_z L\). Fitting a complete axial period
inside it requires \(\alpha>\pi/c_z\), with some margin for an interior
cell. The actual traces at the cell's end faces need not match.

One must therefore either prescribe such compatible axial data, or
subtract a divergence-preserving axial boundary lift with the required
matching traces, and retain its full residual when periodizing and taking
modes. Such an axial lift and its bound are additional inputs here, not
a construction already supplied for the actual response. The generic
source terms below can include
that residual. No zero axial matching cost is asserted for the actual
response. The radial boundary trace remains explicit as well.

## 2. Full meridional pressure reduced to a radial system

Use the exact divergence-free representation
\[
 v_r=-i\alpha\varepsilon f(\rho,s)e^{ik_z z},\qquad
 v_z=(\partial_\rho+\rho^{-1})f(\rho,s)e^{ik_z z},\qquad
 v_\theta=-i c(\rho,s)e^{ik_z z}.
\tag{5}
\]
Its physical Stokes streamfunction is
\(\psi=\tau\rho f(\rho,s)e^{ik_z z}\). Define
\[
 A_\varepsilon=-\partial_\rho^2-\rho^{-1}\partial_\rho
                  +\rho^{-2}+\alpha^2\varepsilon^2,
 \qquad q=A_\varepsilon f.
\tag{6}
\]
The physical meridional vorticity is
\(\omega_\theta=\tau^{-1/2}q e^{ik_z z}\).
Taking its exact curl equation and the azimuthal momentum equation gives
\[
 \boxed{\quad
 q_s=-\nu A_\varepsilon q+2\alpha\omega c+J_q,
 \qquad
 c_s=-\nu A_\varepsilon c+2\alpha g\omega f+J_c,
 \qquad q=A_\varepsilon f.
 \quad}
\tag{7}
\]
Here \(J_q,J_c\) denote specified scaled bulk inputs, if any. They vanish
for the separated homogeneous exterior problem. For a physical
axisymmetric body input \(F\) in velocity units, before any boundary
lifting, their modal values are
\[
 J_q=\tau^{3/2}\widehat{(\partial_zF_r-\partial_rF_z)},
 \qquad J_c=i\tau\widehat F_\theta.
\tag{8}
\]
A local potential force has neither of these contributions. Its influence
can still enter through the global meridional pressure and boundary data.

For the signs in (7), the physical curl equation is
\(\partial_t\omega_\theta-\nu(\mathcal L+\partial_z^2)\omega_\theta
=2\Omega\partial_z v_\theta\).
Substitution of \(v_\theta=-ic e^{ik_z z}\) gives the positive first
coupling. The equation
\((v_\theta)_t-\nu(\mathcal L+\partial_z^2)v_\theta=-Bv_r\)
gives the second. Thus no pressure projection factor has been set to one.
It is present in the elliptic relation \(q=A_\varepsilon f\).
Cylindrical viscosity contributes the explicit \(\rho^{-2}\) term.

Pressure can be recovered explicitly from the axial momentum equation.
Writing hats for physical modal amplitudes and
\(D_z=\partial_r^2+r^{-1}\partial_r-k_z^2\), it is
\[
 \widehat p=\frac{\widehat F_z-\partial_t\widehat v_z
                   +\nu D_z\widehat v_z}{ik_z}.
 \tag{8a}
\]
The exact curl equation makes its radial derivative agree with the radial
momentum equation. Indeed, if the radial and axial momentum residuals
before pressure are \(R_r,R_z\), that equation says
\(ik_zR_r-\partial_rR_z=0\); setting \(ik_zp=-R_z\) then gives
\(R_r+p_r=0\). This also proves local sufficiency of (7) for the full
meridional equations when its data and input are compatible.
The elliptic reconstruction needs the boundary values of
\(f\). Prescribing both velocity components on a radial boundary fixes
\(f\) and \(f'\): the normal component fixes \(f\), and the axial
component fixes \(f'+f/\rho\). Solving the local vorticity equation
without these data loses the irrotational meridional part. Accordingly,
(7) is fourth order in \(f\), with two endpoint conditions at each wall,
and second order in \(c\).

## 3. A uniform energy estimate with all radial variation retained

First impose homogeneous perturbation traces
\[
 f=f'=c=0\quad\text{at }\rho=\rho_-,\rho_+.
\tag{9}
\]
These are conditional no-slip traces for the response. They are not
asserted for the actual exterior restriction. Use
\(\langle u,v\rangle_\rho=\int_J\overline u v\,\rho\,d\rho\).
The Dirichlet quadratic form of \(A_\varepsilon\) satisfies
\[
 \langle f,A_\varepsilon f\rangle_\rho
 =\|f'\|_\rho^2+\|f/\rho\|_\rho^2
                   +\alpha^2\varepsilon^2\|f\|_\rho^2.
\tag{10}
\]
In particular it is bounded below by \(\lambda_0\|f\|_\rho^2\), with the
explicit, \(\tau\)-independent choice
\[
 \lambda_0=
 \frac{\rho_-}{\rho_+}\frac{\pi^2}{(\rho_+-\rho_-)^2}
       +\rho_+^{-2}>0.
\tag{11}
\]
This follows from ordinary Dirichlet Poincaré and the bounded radial
weight. The additional \(\alpha^2\varepsilon^2\) only improves the bound.

Define the fixed weighted energy
\[
 E=\langle f,A_\varepsilon f\rangle_\rho
                       +g_*^{-1}\|c\|_\rho^2.
\tag{12}
\]
The weight \(g_*\) is a constant over the entire time window. Therefore
no spatial or temporal derivative of \(g\) enters its differentiation.
Integrating (7) against \(f\) and \(c/g_*\), respectively, gives
\[
\begin{aligned}
 \tfrac12 E'={}&-\nu\|A_\varepsilon f\|_\rho^2
       -\nu g_*^{-1}\langle c,A_\varepsilon c\rangle_\rho\\
 &+2\alpha\operatorname{Re}\int_J
       \omega(1+g/g_*)\overline f c\,\rho\,d\rho\\
 &+\operatorname{Re}\langle f,J_q\rangle_\rho
       +g_*^{-1}\operatorname{Re}\langle c,J_c\rangle_\rho.
\end{aligned}
\tag{13}
\]
The fourth-order integration has no boundary remainder because both
\(f\) and \(f'\) vanish. It is not an assertion that
\(A_\varepsilon f\) has Dirichlet boundary values; those would be
different, additional boundary conditions.
The exact Green identity is
\[
 \langle f,A_\varepsilon q\rangle_\rho
 -\langle A_\varepsilon f,q\rangle_\rho
 =\left[\rho(\overline{f'}q-\overline f q')\right]_{\rho_-}^{\rho_+};
\]
its right side vanishes under (9), even if \(q\) is nonzero at a wall.

Put \(Y=\sqrt E\) and
\[
 \Gamma=-\nu\lambda_0+
              \frac{2\alpha\sqrt{g_*}\,\omega_*}{\sqrt{\lambda_0}},
 \quad
 \mathcal J(s)=\lambda_0^{-1/2}\|J_q(s)\|_\rho
                      +g_*^{-1/2}\|J_c(s)\|_\rho.
\tag{14}
\]
Cauchy–Schwarz and (10)–(11) imply
\[
 D^+Y\le\Gamma Y+\mathcal J(s),
 \qquad
 \boxed{\ Y(s)\le e^{\Gamma s}Y(0)+
          \int_0^s e^{\Gamma(s-\sigma)}\mathcal J(\sigma)\,d\sigma.\ }
\tag{15}
\]
For example, writing \(d=c/\sqrt{g_*}\), the coupling in (13) is at most
\(4\alpha\sqrt{g_*}\omega_*\|f\|_\rho\|d\|_\rho\), hence at most
\(2\alpha\sqrt{g_*}\omega_*\lambda_0^{-1/2}E\).
The two dissipation terms are at least \(\nu\lambda_0E\).
Regularizing \(Y\) at zero gives the stated norm inequality.

All constants in (15) are independent of \(\tau\). The heat profile
varies in \(\rho,s\) throughout the proof; its supremum bounds are taken
after retaining the full equations. At natural time length
\(t-t_0\le\vartheta\tau\), the conditional propagator has a fixed
energy bound, rather than an exponential in \(\tau^{-h}\).

For completeness, this also defines a well-posed conditional evolution,
rather than only an identity for assumed smooth solutions. Use the energy
space \(H_0^1(J)\times L^2(J)\), and the viscous form domain
\(H_0^2(J)\times H_0^1(J)\), where \(H_0^2\) has both zero value and
zero first derivative. The mass form in the first coordinate is (10), and
its viscous form is \(\langle A_\varepsilon f,A_\varepsilon\varphi\rangle_\rho\).
These forms are uniformly coercive for \(0<\varepsilon\le1\); the two
coefficient couplings are bounded on the energy space. Finite-dimensional
Galerkin approximations and (13) give a weak solution for energy initial
data and square-integrable \(J_q,J_c\); the same estimate for differences
gives uniqueness. Smooth compatible data give the displayed classical
solution. This auxiliary evolution has the specified wall and axial data.

A sufficient damping threshold is
\[
 2\alpha\sqrt{g_*}\omega_*<\nu\lambda_0^{3/2}.
\tag{16}
\]
If the left side is at most half the right side, (15) decays at rate
at least \(\nu\lambda_0/2\) in scaled time in the absence of input.
Failure of (16) proves no growth: it only makes this sufficient energy
test inconclusive. The inequality \(g_*<h\) displays a possible
small-\(h\) advantage, but the remaining source constants and admissible
axial cell size may depend on \(h\). The construction's stipulation
that \(h\) is small does not by itself verify (16). In particular,
compatibility of (16) with \(\alpha>\pi/c_z\) must be checked if the
entire separated cell is to lie in the source tube.

## 4. Physical norm and explicit radial boundary transfer

When (9) holds, integration of the cross term in
\(\|(\partial_\rho+\rho^{-1})f\|_\rho^2\) gives
\[
 \int_J (|v_r|^2+|v_z|^2+|v_\theta|^2)\,\rho\,d\rho
 =\langle f,A_\varepsilon f\rangle_\rho+\|c\|_\rho^2.
\tag{17}
\]
Thus, since \(0<g_*<1\), this modal physical energy lies between
\(g_*E\) and \(E\). For a complex field integrated over one axial
period and the complete azimuthal circle, the physical squared norm
has the extra factor
\[
 2\pi\tau\frac{2\pi}{k_z}=
                 \frac{4\pi^2\tau}{k_z}.
\tag{18}
\]
The same factor occurs at every time in this fixed-coordinate window.
Real parts have the usual factor one half over a full axial period.
No torus-volume factor or change of physical viscosity has been omitted.

For nonhomogeneous radial data, choose an explicit smooth lift
\(F(\rho,s),C(\rho,s)\) matching the four traces \(f,f'\) and the two
traces \(c\). A cubic Hermite polynomial in \(\rho\) suffices for \(F\),
and a linear interpolant for \(C\). Set
\(\widetilde f=f-F\), \(\widetilde c=c-C\). They satisfy (9), and their
system has the effective inputs
\[
 \widetilde J_q=J_q-A_\varepsilon F_s-\nu A_\varepsilon^2F
                         +2\alpha\omega C,
\]
\[
 \widetilde J_c=J_c-C_s-\nu A_\varepsilon C+2\alpha g\omega F.
\tag{19}
\]
Here \(A_\varepsilon^2F\) is the differential expression on the smooth
lift, not an operator domain condition. Estimate (15) applies to the
lifted remainder with these explicit inputs, and the norm of the lift
is then added to recover the original velocity.

For instance, the radial input budget is bounded by
\[
 \|\widetilde J_q\|_\rho
 \le\|J_q\|_\rho+C\big(\|F_s\|_{H^2(J)}
            +\nu\|F\|_{H^4(J)}+\alpha\omega_*\|C\|_{L^2(J)}\big),
\]
\[
 \|\widetilde J_c\|_\rho
 \le\|J_c\|_\rho+C\big(\|C_s\|_{L^2(J)}
       +\nu\|C\|_{H^2(J)}+\alpha g_*\omega_*\|F\|_{L^2(J)}\big).
\tag{20}
\]
The constants depend on the fixed annulus and fixed \(\alpha\), with
\(0<\varepsilon\le1\). For the displayed interpolants these norms are
controlled by the boundary values and their first scaled-time derivatives.
Converting actual physical modal traces into those values must also be
charged: at a wall,
\[
 F=\frac{i\widehat v_r}{\alpha\varepsilon},\qquad
 F'=\widehat v_z-F/\rho,\qquad C=i\widehat v_\theta.
 \tag{20a}
\]
Thus the radial trace may cost \(\varepsilon^{-1}=\tau^{-h}\), even
though the homogeneous modal evolution has uniform constants. Scaled-time
derivatives satisfy \(\partial_s=\tau\partial_t\) at the fixed wall.
No smallness of these trace data follows from (15).
This is a genuine finite-window boundary transfer estimate. It does not
replace the actual boundary values by zero or bound them using the local
heat profile.

## 5. What this resolves and what the global response still needs

The natural low-axial-frequency equations have order-one couplings in
scaled time. The large physical coefficient \(\Omega\) is compensated
by the divergence constraint and the pressure-bearing radial inverse.
Ordinary viscosity and radial curvature remain of order one as well.
Equations (7), (15), and (19) give an exact nonautonomous model with an
explicit boundary budget, and (16) is a sufficient damping condition
expressed in actual profile quantities.

For the actual torus response, the pending inputs are its radial traces,
its axial matching residual, and the associated global pressure data.
A smooth local potential force enters through that matching even though
its curl is zero in the tube. The global pressure computation cannot be
replaced by the homogeneous case of this lemma. No value or sign of the
first terminal pressure moment, no excitation of a growing channel, and
no nonlinear continuation estimate is established here. Unforced ROOT
remains open.


## 6. Verification record

The integration reviewer independently read the exact scaled equations, pressure
and coupling signs, energy identity, and boundary lift. A separate
pedagogy agent independently reviewed §§2–4, including the explicit
pressure recovery, clamped Green identity without a boundary condition
on q, the coercive weak formulation, the factor two in the energy
coupling, and the physical trace conversion. Both reviews passed without
a mathematical correction. The final clarifications charge the actual
radial trace cost and retain axial matching as an additional input.

Nine bounded exact symbolic controls separately passed: scaled divergence,
scaled meridional vorticity, radial/axial viscous-operator intertwinement,
both coupling signs, the weighted Green boundary identity, both boundary
lift residuals, and the normal-velocity trace conversion. These are
algebra checks supporting a written argument, not a formal PDE
certificate. No fluid simulation or full formal build was run.

The result is an exact separated local evolution with the uniform estimate
(15), conditional damping threshold (16), and explicit boundary transfer
(19)–(20a). No actual global response trace, damping condition for the
fixed source constants, or force-removing initial datum was established.
