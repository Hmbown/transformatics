# Evolution of the actual pressure response

8 September 2026. Restricted written analysis. This note differentiates
the pressure functional along the prescribed zero-data linear response.
It gives an exact global moment hierarchy and identifies a cancellation,
followed by a meridional coupling, for its contribution from the actual
heat exterior. The hierarchy is valid on every compact preterminal
interval. It does not give a small-response estimate up to the terminal
time or an unforced singularity.

The reference is the fixed viscosity-one construction on the unit torus
in [OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
has SHA-256 `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
The full pressure decomposition is from
[the global pressure note](global-pressure-feedback.md).
The exact heat region and actual terminal force moment are established
at their stated source scope in
[the force-coupling note](exterior-force-coupling.md).
All parameters of the reference, including \(0<h<1/100\), remain fixed.

## 1. Differentiate the complete pressure functional

Use the actual equations
\[
 U_t+U\cdot\nabla U=\nu\Delta U-\nabla P+f,
 \qquad
 e_t=\mathcal A(t)e+w,\quad e(t_0)=0,
 \tag{1}
\]
where
\[
 \mathcal A e=\nu\Delta e-
 \mathbb P\big(U\cdot\nabla e+e\cdot\nabla U\big),
 \qquad w=\mathbb P f=f-\nabla\phi,
 \quad\phi=\Delta^{-1}\operatorname{div}f.
 \tag{2}
\]
Both velocities are solenoidal. Set
\[
 T=U\otimes e+e\otimes U,
 \qquad \pi=-\Delta^{-1}\partial_i\partial_jT_{ij},
 \qquad q=\pi+\phi.
 \tag{3}
\]
Thus \(e_t+U\cdot\nabla e=\nu\Delta e-e\cdot\nabla U-\nabla q+f\).
Here \(P\) is the reference pressure, \(q\) is the complete response
pressure, and the inverses have zero spatial mean.

Let \(W(t,y)\) be any smooth symmetric periodic tensor. The particular
tensor of interest is the angularly averaged remote axial-Hessian
kernel from the preceding note. In the local chart it is
\[
 W_{ij}(t,y)=-\frac1{2\pi}\int_0^{2\pi}
 \left[(1-\chi(t,y))\partial_{zzij}G_E(x_\vartheta(t)-y)
       +\partial_{zzij}H(x_\vartheta(t)-y)\right]d\vartheta,
 \tag{4}
\]
on a neighborhood of the compact support of \(U\). Here

* \(G_E(x)=-1/(4\pi|x|)\), and \(G_{\mathbb T}=G_E+H\) is the exact
  local torus Green decomposition;
* \(x_\vartheta\) runs over the target circle;
* \(\chi=1\) near that circle, so the first kernel is nonsingular.

Extend (4) smoothly to the torus. The extension outside the support
of \(U\) does not change the functional. All images are retained in
\(H\); no replacement of the periodic projection is made. Holding the
circle and cutoffs fixed is allowed. If they move, their derivatives
remain in \(W_t\).

Define
\[
 J_W(t)=\int_{\mathbb T^3}W:T\,dy
       =2\int(WU)\cdot e\,dy.
 \tag{5}
\]
For (4), this is the remote Euclidean contribution plus the complete
image contribution to \(\overline{\pi_{zz}}\). The near contribution
must still be added to obtain the whole Hessian.

Differentiating the tensor equation, transporting the weight, and
integrating the Laplacian by parts gives the exact identity
\[
\begin{aligned}
 J_W'={}&\int(W_t+U\cdot\nabla W+\nu\Delta W):T\,dy\\
 &-4\nu\int W_{ij}(\partial_kU_i)(\partial_ke_j)\,dy
   -2\int(WU)\cdot(e\cdot\nabla U)\,dy\\
 &-2\int(We)\cdot\nabla P\,dy
   -2\int(WU)\cdot\nabla q\,dy\\
 &+2\int(Wf)\cdot e\,dy+2\int(WU)\cdot f\,dy.
\end{aligned}
 \tag{6}
\]
Every integral is over the complete torus. In particular, the pressure
terms are
\[
 2\int P\operatorname{div}(We)\,dy
 +2\int q\operatorname{div}(WU)\,dy.
 \tag{7}
\]
Harmonicity of the remote Green kernel only eliminates its Laplacian
away from cutoff transitions. It does not eliminate
\(\operatorname{div}(WU)\): even where \(\operatorname{div}W=0\),
that expression contains \(W_{ij}\partial_iU_j\). The mixed viscous
term in (6) also survives. These are exact terms, rather than error
terms estimated using a scalar strain clock.

The core, annular waves and localization terms occur through the full
\(U\) in every product. Angular means contain opposite harmonics, as
in \(\overline{U_a e_b}=\sum_n(U_a)_n(e_b)_{-n}\). Differentiating
does not justify replacing this by the product of the two means.
The image term keeps the lattice-allowed harmonics described in the
preceding pressure note.

## 2. The zero-data condition gives an exact adjoint hierarchy

Put \(a_0=2\mathbb P(WU)\). On solenoidal fields the complete adjoint is
\[
 \mathcal A^*a=
 \mathbb P\big(\nu\Delta a+U\cdot\nabla a-(\nabla U)^Ta\big).
 \tag{8}
\]
Consequently (6) is equivalently
\[
 J_W'=\langle a_1,e\rangle+\langle a_0,f\rangle,
 \qquad a_1=(\partial_t+\mathcal A^*)a_0.
 \tag{9}
\]
The inner products are real \(L^2\) products. The projection retains
the constant mode. In particular,
\(J_W(t_0)=0\) and \(J_W'(t_0)=\langle a_0(t_0),f(t_0)\rangle\);
there is no independently supplied initial pressure moment.

Writing \(a_{j+1}=(\partial_t+\mathcal A^*)a_j\) gives
\[
 \frac{d}{dt}\langle a_j,e\rangle
 =\langle a_{j+1},e\rangle+\langle a_j,f\rangle.
 \tag{10}
\]
This is a spatial moment hierarchy along the actual response. A finite
linear closure would require the new solenoidal weights to lie in the
span of retained weights, with controlled coefficients, or another
estimate on their actual pairings. Formula (10) does not assert that
such a closure is impossible for every conceivable choice of moments.

There is also an exact form with no hierarchy truncation. Let
\(S(t,s)\) be the full periodic linear propagator. For each fixed
preterminal \(t\),
\[
 J_W(t)=\int_{t_0}^t
 \left\langle S(t,s)^*a_0(t),f(s)\right\rangle ds.
 \tag{11}
\]
Existence and smoothness on compact preterminal intervals follow from
the smooth reference there. Equation (11) is a prescribed-force
response identity, not an arbitrary-error estimate. Any claim of small
pressure feedback on a longer interval must control this specific
backward weight against the actual force. Estimating the weight by its
unrestricted norm discards the cancellation proved next.

## 3. An exterior contribution has no direct force injection

Fix \(t_0=1-\tau\), \(R=\sqrt\tau\), a source annulus of radius and
axial width comparable to \(R\), and a separated target circle
\(r=LR,z=0\), with \(L\) fixed and sufficiently large. Choose a
nonnegative smooth axisymmetric cutoff
\(\alpha(r/R,z/R)\), not identically zero, compact in the source
annulus and even in \(z\). Its radial support lies strictly beyond
the source's exterior threshold.

For small \(\tau\), both regions lie in the actual heat exterior with
all cutoffs one. The source coordinate obeys
\(q_{\rm src}-z^2q_{\rm src}^{2h}=1-t\). At the initial time,
\(q_{\rm src}/\tau=1+O(\tau^{2h})\) on the annulus, and it decreases
as \(t\) increases. Thus the fixed annulus remains an exact source-free
heat region for \(t_0\le t<1\). On it,
\[
 U=K(r,t)e_\theta,
 \quad K_t=\nu\mathcal L_0K,
 \quad B=K_r+K/r<0,
 \quad\mathcal L_0=\partial_r^2+r^{-1}\partial_r-r^{-2}.
 \tag{12}
\]

Take only this annulus's contribution to the Euclidean part of the
pressure functional. Its symmetric tensor kernel is
\[
 W^{\rm ann}_{ij}(y)=-\frac{\alpha(y/R)}{2\pi}
       \int_0^{2\pi}\partial_{zzij}G_E(x_\vartheta-y)\,d\vartheta.
 \tag{13}
\]
The scalar averaged kernel is axisymmetric. Its Hessian has no
\(r\theta\) or \(z\theta\) components. Therefore
\[
 a_0=2W^{\rm ann}U=\eta(r,z,t)e_\theta,
 \qquad \eta=2K W^{\rm ann}_{\theta\theta}.
 \tag{14}
\]
This is an exactly compact solenoidal field, so no projection is needed
in (14). It follows for the actual force, throughout the interval, that
\[
 \langle a_0,w\rangle=\langle a_0,f\rangle=0.
 \tag{15}
\]
This cancellation uses both actual source absence and exact
solenoidality. Smoothness of the force alone would not give it.

Let \(b=\bar e_\theta\), \(v_r=\bar e_r\), and use the measure
\(dV=2\pi r\,dr\,dz\). The actual averaged azimuthal equation gives
the following all-time moment identity, with no boundary terms because
the weight is compact:
\[
 \boxed{\quad
 J_{\rm ann}'=
 \int(\eta_t+\nu\mathcal L\eta)b\,dV
 -\int B\eta v_r\,dV,
 \qquad\mathcal L=\mathcal L_0+\partial_z^2.
 \quad}
 \tag{16}
\]
The ordinary viscosity and the derivatives of the physical weight
remain in \(\mathcal L\eta\). This is a weighted equation for the
actual pressure contribution, not an equation for a prescribed swirl
profile.

## 4. The next weight is meridional and has a global pressure tail

Directly applying (8) to (14) gives
\[
 a_1=(\eta_t+\nu\mathcal L\eta)e_\theta
        -B\eta e_r-\nabla\psi_1,
 \qquad
 \psi_1=\Delta_{\mathbb T}^{-1}
          \operatorname{div}(-B\eta e_r).
 \tag{17}
\]
All raw terms are supported in the source-free annulus, but the last
term is a global periodic pressure projection. The factor in the
meridional coupling is \(B=K_r+K/r\); the angular advection term and
the transpose gradient term must both be included to obtain it.

The meridional part cannot be discarded as a gradient. Its curl has
the exact angular component
\[
 \left[\nabla\times(-B\eta e_r)\right]_\theta
       =-\partial_z(B\eta).
 \tag{18}
\]
The weight is nonzero and compact in \(z\), and \(B\) is independent
of \(z\) and nonzero. Hence (18) is not identically zero. A Leray
projection changes no curl. The first new observation therefore lies
outside the space of purely azimuthal axisymmetric weights. In
particular, azimuthal pressure moments alone do not form an invariant
family for the actual adjoint, even on this exact exterior contribution.

Pairing (17) with the actual force makes the nonlocal mechanism
explicit:
\[
 \langle a_1,f\rangle
 =-\int_{\mathbb T^3}\nabla\psi_1\cdot f\,dy
 =\int B\eta\,\bar\phi_r\,dV.
 \tag{19}
\]
The compact raw terms pair to zero because \(f=0\) there. Integration
by parts and the complete periodic inverse Laplacian give the second
equality. Thus a force located outside the annulus re-enters through
the pressure tail of the *next* weight. Neither pressure projection
nor zero initial data removes this coupling.

Following the new radial moment produces the actual radial response
equation
\[
 (v_r)_t=\nu\mathcal L v_r+2(K/r)b
                  -\partial_r\overline{\pi+\phi}.
 \tag{20}
\]
Its last term contains the entire core, all matching wave harmonics
and periodic images from (4)–(7), together with the near contribution.
Equations (16) and (20) therefore identify the precise missing spatial
input. They do not justify prescribing a local \(p_{zz}\) or closing
the radial moment using \(J_{\rm ann}\) alone. A cancellation with
other regions in the *total* pressure has not been excluded or proved.

## 5. The actual terminal quadrupole fixes the first possible return

The all-time statements above imply
\[
 J_{\rm ann}(t_0)=J_{\rm ann}'(t_0)=0,
 \qquad
 J_{\rm ann}''(t_0)=\int B\eta\,\bar\phi_r(t_0)\,dV.
 \tag{21}
\]
Indeed \(b_t(t_0)=0\), while \((v_r)_t(t_0)=-\bar\phi_r(t_0)\).
This uses the actual zero-data equation; no independently supplied
perturbation has been introduced.

Let
\[
 M=\phi_{zz}(1,0)
   =\sum_i\int_{\mathbb T^3}
         \partial_{zzi}G_{\mathbb T}(-y)(F_0)_i(y)\,dy,
 \qquad F_0=f(1,\cdot).
 \tag{22}
\]
This is the actual global moment from the force-coupling note. Its
integral is well defined because \(F_0\) is flat at the terminal
origin. Smoothness and angular Taylor expansion give
\[
 \bar\phi_r(t_0,r,z)=-\frac r2M
             +O\big(r(\tau+|z|+r^2)\big).
 \tag{23}
\]
Only terminal flatness at the origin is used to identify the trace in
(23). Harmonicity at the preterminal axis is not assumed.

There is no oscillatory cancellation in the present weight. Put
\(\rho=r/R,Z=z/R\). At \(t=t_0\), the exact heat profile gives
\[
 K=R^{-1-2h}\mathcal K(\rho),\qquad
 B=R^{-2-2h}\mathcal B(\rho),\qquad
 \mathcal K>0,\quad\mathcal B<0.
 \tag{24}
\]
Write
\(W^{\rm ann}_{\theta\theta}=R^{-5}\alpha(\rho,Z)w_L(\rho,Z)\).
At the center of the rescaled source coordinates, angular averaging
over the target ring gives
\[
 w_L(0,0)=-\frac9{8\pi L^5},\qquad
 w_L(\rho,Z)=-\frac9{8\pi L^5}+O(L^{-7})
 \tag{25}
\]
uniformly on the fixed source support. The second relation follows by
the even Cartesian Taylor expansion of the averaged kernel. Fixing
\(L\) large makes \(w_L<0\) on that support.

Substitution into (21) yields the actual limiting coefficient
\[
 \boxed{\quad
 \tau^{2+2h}J_{\rm ann}''(t_0)
       =-C_L M+O(\sqrt\tau),
 \qquad
 C_L=\int\alpha\mathcal B\mathcal K w_L\rho\,dY>0,
 \quad}
 \tag{26}
\]
where \(dY=2\pi\rho\,d\rho\,dZ\). The extra factor \(\rho\) in
\(C_L\) comes from the radial gradient in (23). Constants are fixed
before \(\tau\downarrow0\).

Unlike the earlier oscillatory coefficient, this scalar multiplier of
\(M\) is strictly nonzero. The value and sign of the **actual \(M\)**
remain undetermined by the available source estimates. If \(M=0\),
(26) gives no nonzero leading return. If \(M\ne0\), it determines the
sign of this initial curvature for sufficiently late restarts. Neither
case supplies a time-uniform Taylor remainder or controls the sum of
the pressure contributions from the other regions.

## 6. What has and has not closed

The source-free annulus eliminates the direct force injection in its
pressure moment exactly. The next adjoint weight develops a
meridional component with nonzero curl and a global pressure tail;
that tail pairs with the actual force through (19). This is a concrete
failure of closure within azimuthal pressure moments, rather than a
norm-only counterexample involving freely chosen response fields.

The complete zero-data pressure response is still given by (11).
Controlling it beyond the established comparison window requires an
estimate on that actual backward weight against \(f\), or on the
coupled meridional/global-pressure moments. Smooth force and zero data
supply the cancellation and the fixed input (22), but do not by
themselves control these later moments. The identities hold beyond
the finite comparison window on every compact interval before time
one; no smallness bound on that longer interval has been established.

For the unforced nonlinear difference \(E=V-U\), the force input is
\(-\mathbb P f\), and the equation also contains the full quadratic
error. The pressure has the additional \(E\otimes E\) stress, which
need not be supported where \(U\) is. This linear response hierarchy
does not remove those terms or construct one initial correction valid
at all later times.

## Review boundary

The integration reviewer and the outgoing agent independently reviewed the complete
argument. Their checks include the tensor evolution and mixed viscous
factor, the full adjoint projection, the source-free annular cancellation,
the meridional curl, the periodic force-potential pairing, and the sign,
normalization and remainder in (26). Both reviews passed at the stated
written scope. A third agent independently checked (6), (17), (19) and
(26), including the terminal-only Taylor expansion and its remainder,
and also passed these claims. The Newtonian angular-average coefficient and adjoint
swirl-coupling factor were also checked by exact symbolic algebra.
These are independent AI reviews and algebra checks, not a new formal
verification or external expert review.
