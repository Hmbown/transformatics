# The first force coupling to the actual exterior packet

8 September 2026. Restricted written calculation using the released forced
reference. This identifies the first **possible** nonzero local response
coefficient and proves that its pairing with the specified oscillatory
packet decays faster than every fixed power of the remaining time. Its
nonvanishing and sign are not established. No conclusion about the complete
forced response or an unforced singularity follows.

The reference, fixed tube and normalized packet are those of
[the exterior quasimode note](exterior-quasimode.md), source
SHA-256 `22b6c1ef7cf542692dd2bd03b0a2c88c96ae4ab77b53085ff28beec29cc414d1`.
The external source is [OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The domain is its unit torus, the physical viscosity is one, and the
terminal time is one. No new simulation or formal build is used below.

## 1. A global pressure potential on a source-free tube

Write the actual reference equation as
\[
 U_t-\nu\Delta U+\mathbb P((U\cdot\nabla)U)=w,
 \qquad w=\mathbb P f,
 \qquad \phi=\Delta^{-1}\operatorname{div}f,
 \qquad w=f-\nabla\phi.
 \tag{1}
\]
The inverse Laplacian has zero spatial mean, and the Leray projection
retains the constant mode. The potential \(\phi\) is not the reference
pressure \(P\). The force has a smooth joint extension through time one;
therefore \(\phi\), too, has uniformly bounded derivatives of every fixed
order on a fixed late time interval. This follows from periodic elliptic
regularity, using the source's global force bounds, not from the size of
the singular velocity.

Let \(t_0=1-\tau\). On the fixed tube used for the quasimode and throughout
its subsequent preterminal flight,
\[
 f=0,\qquad U=K(r,t)e_\theta,\qquad
 w=-\nabla\phi,\qquad \Delta\phi=0,\qquad \Delta w=0.
 \tag{2}
\]
The tube does **not** include the axis. In particular, its harmonicity
statement does not assert \(\Delta\phi(t,0)=0\) at a preterminal time.
The exact exterior identity and persistence of this tube were checked in
the cited quasimode note against the actual correction supports.

The source gives zero spatial mean for the preterminal velocity as an
elementary consequence of its assembly: it is the sum of a periodic curl
and the periodization of a compact axisymmetric azimuthal field. The curl
integrates to zero; the latter integrates to zero around each full circle.
Time activation preserves this fact. Integrating its momentum equation
then gives \(\int f=0\) before time one, and smooth extension gives
\(\int F_0=0\), where \(F_0=f(1,\cdot)\). This is a consequence of the
displayed source construction, not an additional formal mean-zero export.
Neither a zero force mean nor the mean-zero normalization of \(\phi\)
controls its Hessian at the origin.

## 2. Exact full-pressure pairing

Use the linearized operator and complex inner product
\[
 \mathcal A(t)a=\nu\Delta a-
 \mathbb P\big((U\cdot\nabla)a+(a\cdot\nabla)U\big),
 \qquad \langle a,b\rangle=\int a\cdot\overline b\,dx.
 \tag{3}
\]
Let \(v_\tau\) be the unit packet. Its cylindrical components are
axisymmetric, and its angular component is
\[
 (v_\tau)_\theta=\frac{T}{N_\tau}\chi(r,z)e^{ikz},
 \qquad N_\tau=\|v\|_2\asymp\sqrt{r_0}\,\ell,
 \qquad T>0.
 \tag{4}
\]
Here \(\chi=\eta_r((r-r_0)/\ell)\eta_z(z/\ell)\), and \(v\) includes
both meridional curl corrections from the quasimode construction.

On the support, the symmetry of \(\nabla w\) gives the exact identity
\[
 (U\cdot\nabla)w+(w\cdot\nabla)U
 =\nabla(U\cdot w)+(\nabla\times U)\times w.
 \tag{5}
\]
All gradient terms pair to zero against the complete compact solenoidal
packet. The outer Leray projection can also be removed in this pairing,
by self-adjointness. With
\[
 \nabla\times U=B(r,t)e_z,
 \qquad B=K_r+K/r=-2g\Omega<0,
\]
we obtain
\[
 \langle\mathcal A(t)\mathbb P f(t),v_\tau\rangle
 =-\langle B e_z\times w,v_\tau\rangle
 =\langle B e_z\times\nabla\phi,v_\tau\rangle.
 \tag{6}
\]
Thus the viscous term and the full perturbation pressure have been
accounted for exactly. This is not a replacement of the Leray projection
by a local projection.

Define the local angular average
\[
 \bar\phi(r,z,t)=\frac1{2\pi}\int_0^{2\pi}
 \phi(r\cos\theta,r\sin\theta,z,t)\,d\theta.
\]
Since
\(e_z\times\nabla\phi=\phi_r e_\theta-r^{-1}\phi_\theta e_r\),
integration over the full circle cancels the radial term. Consequently
the exact coefficient is
\[
 \boxed{\quad
 C_\tau(t):=\langle\mathcal A(t)\mathbb P f(t),v_\tau\rangle
 =\frac{2\pi T}{N_\tau}
 \int B(r,t)\,\partial_r\bar\phi(r,z,t)
       \chi(r,z)e^{-ikz}\,r\,dr\,dz .\quad}
 \tag{7}
\]
This formula uses the actual global force through \(\phi\). It does not
assume that the full force or its periodic pressure projection is
axisymmetric. The angular averaging takes place only inside the local
Euclidean chart; arbitrary rotations are not symmetries of the unit
torus.

For completeness, consider the actual unforced solution \(V\) restarted
from \(U(t_0)\), on its classical local lifespan, and set \(E=V-U\).
Its exact projected equation is
\[
 E_t=\mathcal A(t)E-\mathbb P((E\cdot\nabla)E)-w,
 \qquad E(t_0)=0.
\]
Holding \(v_\tau\) fixed when differentiating, (2) gives
\[
 \begin{aligned}
 \langle E_t(t_0),v_\tau\rangle&=0,\\
 \langle E_{tt}(t_0),v_\tau\rangle&=-C_\tau(t_0).
 \end{aligned}
 \tag{8}
\]
Indeed \(E_{tt}(t_0)=-\mathcal A(t_0)w(t_0)-w_t(t_0)\), while
\(\langle w_t,v_\tau\rangle=\langle f_t,v_\tau\rangle=0\) on the
fixed source-free tube. The quadratic error term contributes nothing to
these two derivatives. Equation (8) is an exact initial jet for each
fixed restart; it gives neither a uniform Taylor remainder on the
quasimode flight nor a nonzero second derivative.

## 3. Which actual global moment enters first?

Smoothness and angular integration, without harmonicity at the axis,
give the transverse Taylor expansion
\[
 \partial_r\bar\phi(r,z,t)
 =\frac r2\Delta_\perp\phi(0,0,z,t)+O(r^3),
 \qquad \Delta_\perp=\partial_{x_1}^2+\partial_{x_2}^2.
 \tag{9}
\]
All fixed axial derivatives have the analogous uniform expansion. In
particular \(|\partial_z^j\partial_r\bar\phi|\le C_j r\) near the
axis. The linear transverse Taylor terms average to zero, as do all odd
transverse degrees.

At the terminal origin, the actual force is flat, so
\(\Delta\phi(0,1)=\operatorname{div}F_0(0)=0\). Define
\[
 M:=\partial_z^2\phi(0,1),\qquad
 \phi(\cdot,1)=\Delta^{-1}\operatorname{div}F_0.
\]
On the shrinking packet support and its time window, (9) gives
\[
 \partial_r\bar\phi(r,z,t)
 =-\frac r2 M+O\big(r(1-t+|z|+r^2)\big).
 \tag{10}
\]
Only here, at the terminal origin, has the transverse trace been
replaced by \(-\phi_{zz}\). More generally, the complete terminal
Taylor expansion of \(\phi\) has harmonic homogeneous terms because
every spatial derivative of \(\operatorname{div}F_0\) vanishes there.
Flatness of the source does not set those harmonic terms to zero.

Let \(G\) be the mean-zero Green function on the unit torus, with
\(\Delta G=\delta_0-1\). The first allowed axisymmetric quadrupole is
the following actual global force moment:
\[
 \boxed{\quad
 M=\sum_{i=1}^3\int_{\mathbb T^3}
       \partial_z^2\partial_{x_i}G(-y)\,(F_0)_i(y)\,dy .\quad}
 \tag{11}
\]
The sign follows by integration by parts in
\(\phi(x)=\int G(x-y)\operatorname{div}F_0(y)\,dy\).
The third derivatives of \(G\) have order \(|y|^{-4}\) near zero;
flatness of \(F_0\) makes this integral absolutely convergent. Higher
terminal pressure Taylor coefficients have the corresponding higher
Green derivatives paired with the same actual \(F_0\); their integrals
are also well defined by flatness.

Substitution of (10) into (7) identifies the quadrupole contribution
\[
 -\frac{\pi T M}{N_\tau}
 \int B(r,t)r^2\chi(r,z)e^{-ikz}\,dr\,dz.
 \tag{12}
\]
This is an identified contribution, **not** a proved leading asymptotic
term of \(C_\tau\). The axial Fourier transform of the bump can be
very small or zero; no lower bound on it, on \(M\), or on the remainder
relative to (12) has been supplied. Changing the packet's complex phase
also changes the phase of this scalar pairing. A signed physical response
requires a fixed real packet convention and control of the complete (7).

## 4. What the source symmetries actually determine

The relevant source checks are limited but decisive for interpreting
(11).

* The [paper's §2](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
  explicitly explains the broken axial reflection
  symmetry: the concentrating background has nonzero axial velocity on
  the middle plane. The formal
  [FinalSlowBase.origin](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/FinalSlowBase.lean#L361)
  fixes that signal, and `axis_tendsto` uses its positive coefficient.
  An odd-in-\(z\) scalar pressure cancellation cannot be assumed.
* The leading background and the direct angular means are axisymmetric.
  The complete construction also contains waves with nonzero angular
  harmonics; their stresses have angular means. Axisymmetry of the local
  exterior is not axisymmetry of the complete global source. In any case,
  an axisymmetric harmonic quadratic \(z^2-r^2/2\) permits \(M\ne0\).
  Even reflection symmetry would not remove this quadratic.
* The explicit cutoff is rotation-invariant about the designated axis,
  as proved by
  [SpatialLocalization.spatialCutoff_rotation](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/SpatialLocalization.lean#L61).
  The actual mixed curl/direct-field assembly is displayed in
  [MixedPeriodicAssembly](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedPeriodicAssembly.lean#L27).
  It yields the zero spatial mean discussed above, which removes only
  the zero Fourier mode and does not determine (11).
* The source's
  [terminal-force jets](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CandidateFromLimits.lean#L128)
  preserve the actual residual limits. Those limits are not freely
  chosen terminal data. The smoothness and flatness used here are the
  paper's Lemma 10.2 and the construction audited in
  [the force-removal source note](external-force-removal-source.md).
* The [nonzero terminal-force calculation](terminal-force-nonzero.md)
  detects an axisymmetric azimuthal component on the radial cutoff
  annulus. Such a component is divergence-free and makes no contribution
  to \(\operatorname{div}F_0\). Its nonzero circulation therefore does
  not determine \(M\). The poloidal cutoff terms and all other actual
  residual components still enter (11).

No inspected source statement fixes the value or sign of (11), nor
establishes that it vanishes. This is a bounded finding about the
displayed source facts; it is not a claim that all possible identities
of the external construction have been exhausted.

## 5. A quantitative bound for this first coupling

Equation (7) gives more than an unspecified coefficient. The heat
factor \(B\) is independent of \(z\), and \(|B|\le C\gamma\) on
the packet, where \(\gamma\asymp\tau^{-1-h}\). Integrate by parts
\(m\) times in \(z\). The compact bump has no boundary terms,
\(|\partial_z^j\partial_r\bar\phi|\le C_jr_0\), and the envelope
derivatives cost at most \(C_m\ell^{-m}\). Thus
\[
 \begin{aligned}
 |C_\tau(t)|
 &\le C_m\gamma r_0\sqrt{r_0}\,\ell\,(k\ell)^{-m}\\
 &\le C_m\tau^{\,1/4-7h/8+mh/8},
 \end{aligned}
 \tag{13}
\]
for the quasimode choices
\(r_0\asymp\tau^{1/2}\), \(\ell=\tau^{1/2+h/8}\) and
\(k=\tau^{-1/2-h/4}\). The estimate is uniform for the fixed packet
over its short preterminal flight. Constants depend on the fixed source,
bumps and derivative order, not on \(\tau\).

For every prescribed \(L>0\), choosing one sufficiently large fixed
integer \(m\) in (13) therefore gives
\[
 \sup_{t_0\le t\le t_1}|C_\tau(t)|\le C_L\tau^L.
 \tag{14}
\]
This uses smoothness, rather than analyticity, and gives no uniform
control as the derivative order grows. It also requires the specified
high axial frequency: the same conclusion is not asserted for every
direction whose amplification contributes to the propagator norm.

The smallest unresolved actual coefficient at this stage is the exact
global-pressure integral (7). The allowed terminal moment (11) helps
identify its source dependence, but computing that one number alone
would not settle the oscillatory integral or its subsequent evolution.
The independently reviewed [fixed response-jets extension](force-response-jets.md)
controls every fixed linear-response derivative using local elliptic
estimates; it does not give a remainder uniform in growing derivative order.
The remaining dynamical problem is the source pairing with an evolved
adjoint direction. A large operator norm and a nonzero terminal projected
force do not supply that pairing; neither does the smallness of this
fixed initial response coefficient give an upper bound on the complete
response.

## Verification scope

The integration reviewer independently checked the pressure-pairing identity, the
terminal Green integral and its sign, the distinction between preterminal
and terminal axis regularity, and the power in (13). A separate pedagogy
agent independently passed those same calculations, including convergence
of the Green integral and the first two error derivatives. The
[symbolic companion](checks/check-force-removal.py) checks the
curl identity and scale arithmetic, among other elementary controls. These
are written analysis and algebra checks, not a formal PDE certificate.
The actual global moment's value and the full dynamical response remain
uncomputed.
