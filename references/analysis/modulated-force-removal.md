# Force removal modulo time and spatial translation

8 September 2026. Exact identities, a conditional comparison lemma and
two explicit examples. No unforced Navier–Stokes singularity is proved.
This supplements the
[fixed-terminal stability criterion](force-removal-stability.md):
failure of that sufficient criterion does not imply failure of singularity
persistence with a shifted time or location.

## 1. General translated reference, with every source term retained

Work on the fixed torus \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\),
at fixed viscosity \(\nu>0\). Let
\[
\partial_sU+(U\cdot\nabla_y)U+\nabla_yP-\nu\Delta_yU=f,
\qquad \nabla_y\cdot U=0,
\tag{1}
\]
on a reference interval ending at \(T\).
For a physical time interval \([t_0,S)\), choose
\[
\theta(t)=t+\sigma(t),\qquad
y=x+a(t),\qquad
W(t,x)=U(\theta(t),x+a(t))+b(t).
\tag{2}
\]
Here \(a,b\in\mathbb R^3\), with \(a\) a lift of a torus translation.
Assume enough differentiability for the formulas used below and
\(\theta(t)\) in the domain of \(U\). For an increasing time
reparameterization also require \(\theta'=1+\sigma'>0\).
The chain-rule identity itself does not require that last inequality.
Use the periodic pressure
\(\Pi(t,x)=P(\theta(t),x+a(t))\).

For any field \(H\), write \(\widetilde H(t,x)=H(\theta(t),x+a(t))\).
Direct differentiation gives
\[
\boxed{\
\partial_tW+(W\cdot\nabla)W+\nabla\Pi-\nu\Delta W
=\mathcal F
=\widetilde f+\sigma'\widetilde{U_s}
 +(a'+b)\cdot\widetilde{\nabla U}+b'.\ }
\tag{3}
\]
Indeed \(W_t=(1+\sigma')\widetilde{U_s}
+a'\cdot\widetilde{\nabla U}+b'\);
the transport term is
\(\widetilde{(U\cdot\nabla)U}+b\cdot\widetilde{\nabla U}\).
Spatial translations preserve derivatives, the torus and divergence.
The Laplacian remains exactly \(\nu\widetilde{\Delta U}\).

Thus time reparameterization is not a free symmetry at fixed viscosity.
Its defect is \(\sigma'\widetilde{U_s}\), and expanding this derivative
with (1) includes the viscous, nonlinear, pressure and force terms:
\[
\sigma'\widetilde{U_s}
=\sigma'(\nu\widetilde{\Delta U}
-\widetilde{(U\cdot\nabla)U}-\widetilde{\nabla P}+\widetilde f).
\]
Keeping it as \(U_s\) does not discard any of them.

The Leray projection commutes with torus translations and spatial
derivatives. Since \(U_s,\partial_iU\) and constants are divergence free,
\[
\mathbb P\mathcal F
=\widetilde{\mathbb P f}+\sigma'\widetilde{U_s}
 +(a'+b)_i\widetilde{\partial_iU}+b'.
\tag{4}
\]
No pointwise locality of \(\mathbb P\) is assumed.

To compare with the **same** unforced initial datum \(V(t_0)=U(t_0)\),
it is sufficient to impose
\[
\theta(t_0)=t_0,\qquad a(t_0)=0,\qquad b(t_0)=0.
\tag{5}
\]
Other choices are possible only with their resulting initial error
explicitly included. The terminal time \(S\) is allowed to differ from
\(T\), with \(\theta(t)\uparrow T\) as \(t\uparrow S\).

## 2. Two legitimate spatial gauges, which cannot be combined silently

**Translated shape.** Set \(b=0\). Then
\[
\mathcal F=\widetilde f+\sigma'\widetilde{U_s}
 +a'_i\widetilde{\partial_iU}.
\tag{6}
\]
This gives four explicit tangent directions: a time tangent and three
translation tangents. The translated field is a reference in the original
coordinates; (6) pays for moving its shape.

**Moving frame with velocity correction.** Set \(b=-a'\). Then
\[
W=\widetilde U-a',\qquad
\boxed{\ \mathcal F=\widetilde f+\sigma'\widetilde{U_s}-a''.\ }
\tag{7}
\]
This is the Galilean velocity correction with the sign appropriate to
\(y=x+a(t)\). The translation-advection terms cancel, but the uniform
acceleration force remains. Condition (5) additionally requires
\(a'(t_0)=0\).
For constant \(\sigma\) and affine \(a\), (7) reduces to the ordinary
time/space translation and Galilean symmetry.

A nonzero constant vector is not the gradient of a periodic scalar:
integrating such a gradient over the torus gives zero. Consequently
\(-a''\) cannot be hidden in a nonperiodic linear pressure.
Nor can one use (7) while retaining the three translation-force directions
from (6); the velocity correction has already canceled them.

Force derivatives also contain the parameter derivatives. In gauge (7),
put \(\mathcal D=\theta'\partial_s+a'\cdot\nabla_y\). Then
\[
\partial_t\mathcal F
=\widetilde{\mathcal D f}
 +\sigma''\widetilde{U_s}
 +\sigma'\widetilde{\mathcal D U_s}-a'''.
\tag{8}
\]
The notation means evaluation after applying the displayed operator with
the time-dependent coefficients. At order \(k\), the force requires
derivatives of \(a\) through \(k+2\), of \(\sigma\) through \(k+1\),
and the corresponding composed derivatives of \(U,f\).
Smoothness or flatness of the original force alone supplies no such
parameter bounds.

## 3. Exactly removing the spatial mean force

Let bars denote normalized spatial means. Equation (1) gives
\(\overline U_s=\overline f\). Any unforced torus solution preserves
its mean \(m_0=\overline U(t_0)\).
In the moving-frame gauge choose
\[
a'(t)=\overline U(\theta(t))-m_0,\qquad a(t_0)=0.
\tag{9}
\]
Then \(a'(t_0)=0\), \(\overline W=m_0\), and
\(a''=\theta'\overline f(\theta)\). Substituting into (7) yields
\[
\boxed{\
\mathcal F=(\widetilde f-\overline f(\theta))
 +\sigma'(\widetilde{U_s}-\overline f(\theta)),\qquad
\overline{\mathcal F}=0.\ }
\tag{10}
\]
This removes the mean force exactly, without a stability assumption.
It does not remove its mean-zero spatial component.
If \(U\) has constant mean, imposing this mean-matching moving frame
fixes \(a'=0\); its translation is then constant. A freely moving shape
can instead be described using (6), with its tangent source retained.

A different acceleration may cancel the value of the projected force at
a chosen point. For example, with \(\sigma=0\), choosing
\(a''(t)=(\mathbb P f)(t,a(t))\) makes
\[
\mathbb P\mathcal F(t,x)
=(\mathbb P f)(t,x+a(t))-(\mathbb P f)(t,a(t)).
\]
Locally this is bounded by
\(|x|\sup|\nabla\mathbb P f|\).
It is not generally the mean-matching choice (9). Moreover the estimate
uses the full nonlocal projected force, and does not control its previous
accumulation or the response of the singular reference.

## 4. What instantaneous tangent removal actually proves

Use the translated-shape gauge (6). At a fixed parameter value, set
\[
Z_0=\widetilde{U_s},\qquad Z_i=\widetilde{\partial_iU}\ (1\le i\le3),
\quad F=\widetilde{\mathbb P f},\quad
v=(\sigma',a'_1,a'_2,a'_3).
\]
The projected residual is \(F+\sum_i v_iZ_i\).
In the global \(L^2\) inner product let
\[
G_{ji}=\langle Z_i,Z_j\rangle,\qquad
g_j=\langle F,Z_j\rangle.
\]
If \(G\) is positive definite, its least-squares minimizer is exactly
\[
v=-G^{-1}g,\qquad
\mathbb P\mathcal F=(I-\mathcal P_Z)F,
\tag{11}
\]
where \(\mathcal P_Z\) is orthogonal projection onto the four tangents.
This follows by expanding the squared norm as
\(\|F\|_2^2+2v^Tg+v^TGv\).
Thus the normal component of \(F\) cannot be removed by these four
instantaneous parameter velocities. If the tangents are dependent, work
with an independent subfamily; do not assume an invertible four-dimensional
matrix for a symmetric profile.

Formula (11) is a reference-only parameter ODE, not a shadowing theorem.
To use it over an interval one still needs existence of that ODE,
control of the Gram inverse, \(\theta'>0\), all necessary parameter
derivatives and \(\theta(t)<T\). The projected residual may be large.
No norm of the transverse error has yet been estimated.

In particular, minimizing the source is not the same as keeping the error
orthogonal to the tangents. Let \(e=V-W\), write
\[
L_W e=\mathbb P((W\cdot\nabla)e+(e\cdot\nabla)W)-\nu\Delta e,
\quad B(e,e)=\mathbb P\nabla\cdot(e\otimes e),
\]
and impose \(\langle e,Z_j\rangle=0\).
Differentiating this condition using (6) gives the exact system
\[
\sum_{i=0}^3
\left(G_{ji}-\langle e,D_iZ_j\rangle\right)v_i
=-\langle F+L_We+B(e,e),Z_j\rangle
 +\langle e,D_0Z_j\rangle,
\tag{12}
\]
where \(D_0=\partial_s\) and \(D_i=\partial_{y_i}\) act on the
uncomposed tangents and are then evaluated at \((\theta,x+a)\).
Indeed \(\partial_tZ_j=D_0Z_j+\sum_i v_iD_iZ_j\).
Equation (12) includes the evolving tangents, transport, diffusion and
quadratic error. It reduces to (11) at \(e=0\), but its later inversion
requires an error-dependent matrix bound. Treating it as automatically
invertible would assume part of the missing stability.

## 5. Conditional modulation lemma with a movable terminal time

Choose parameters satisfying (2), (5) and the stated domain conditions,
smooth on every compact subinterval of \([t_0,S)\), where \(S<\infty\).
Let \(\mathcal F\) be the complete residual (3).
For the unforced solution with the unchanged initial datum, the exact
error equation is
\[
\partial_te+(W\cdot\nabla)e+(e\cdot\nabla)W
 +(e\cdot\nabla)e+\nabla(p-\Pi)-\nu\Delta e=-\mathcal F.
\tag{13}
\]
Its pressure satisfies
\[
\Delta(p-\Pi)=-\nabla\cdot\mathcal F
-\partial_i\partial_j(W_i e_j+e_i W_j+e_i e_j).
\]
Relative energy consequently gives
\[
\tfrac12\partial_t\|e\|_2^2+\nu\|\nabla e\|_2^2
=-\int e^TS(W)e-\langle\mathbb P\mathcal F,e\rangle.
\tag{14}
\]

Here is one explicit sufficient criterion, depending only on the chosen
reference and parameters. Fix integer \(s\ge3\), and set
\[
a_s(t)=C_s\|W(t)\|_{H^{s+1}},\qquad
F_s(t)=\|\mathbb P\mathcal F(t)\|_{H^s},\qquad
\Phi_s(t)=\int_{t_0}^t
e^{\int_r^t a_s(q)\,dq}F_s(r)\,dr.
\]
If
\[
4C_s\int_{t_0}^S\Phi_s(t)\,dt<1,
\tag{15}
\]
then \(V\) exists smoothly on every compact subinterval before \(S\)
and \(\|V-W\|_{H^s}\le2\Phi_s\).
The proof is the differentiated energy inequality
\[
\partial_t\|e\|_{H^s}
\le a_s\|e\|_{H^s}+C_s\|e\|_{H^s}^2+F_s
\]
and the first-crossing argument in the fixed-terminal note; it applies
to this exact residual without changing viscosity or discarding pressure.
If, along a sequence \(t\uparrow S\),
\[
\|W(t)\|_\infty\longrightarrow\infty,\qquad
2C_{\rm emb}\Phi_s(t)\le\kappa\|W(t)\|_\infty,\quad \kappa<1,
\tag{16}
\]
then this same unforced solution cannot extend smoothly through \(S\).
This is a sufficient, explicitly conditional modulation lemma.
It makes no assertion that the coarse Sobolev estimate is sharp enough
for the external construction.

For example, if \(\theta(t)\uparrow T\),
\(\|U(\theta(t))\|_\infty\to\infty\), and
\(|b(t)|=o(\|U(\theta(t))\|_\infty)\), then
\[
\|W(t)\|_\infty\ge\|U(\theta(t))\|_\infty-|b(t)|\to\infty.
\]
The full-pressure propagator criterion in the earlier note can likewise
be applied to \(W,\mathcal F\) with a weight built from
\(T-\theta(t)\), provided its response and nonlinear bounds are actually
proved. Time and location modulation removes no obligation to prove those
bounds on the transverse error.

## 6. Exact periodic NS example: mean forcing is removable

Choose a smooth scalar \(m(t)\), a primitive \(M'=m\), an integer
\(k\ge1\), and a constant \(A\). Define
\[
U(t,x)=m(t)e_1+
A e^{-\nu k^2t}\cos(k[x_1-M(t)])e_2,\qquad P=0.
\tag{17}
\]
This is divergence free. Transport by \(m e_1\) cancels the moving
phase's time derivative, and the heat factor cancels viscosity.
The complete force is exactly \(f=m'(t)e_1\).

Fix \(t_0\), put \(m_0=m(t_0)\), and choose
\[
\sigma=0,\qquad
a(t)=\big(M(t)-M(t_0)-m_0(t-t_0)\big)e_1,\qquad b=-a'.
\]
Then (5) holds, \(a''=f\), and the residual in (7) is zero.
The modulated reference is exactly
\[
W(t,x)=m_0e_1+
A e^{-\nu k^2t}
\cos(k[x_1-M(t_0)-m_0(t-t_0)])e_2.
\tag{18}
\]
It is the smooth unforced solution with the same initial datum.
The fixed-coordinate difference \(W-U\) contains both a mean-velocity
difference and a phase drift; the modulated error is identically zero.
This example verifies the force and Galilean signs within ordinary
viscous NS. It is nonsingular and does not remove a general mean-zero
spatial force.

## 7. Exact scalar example: persistence with a different blow-up time

For \(\varepsilon>0\) and \(u_0>0\), compare
\[
U'(s)=U(s)^2+\varepsilon,\quad U(t_0)=u_0,
\qquad
V'(t)=V(t)^2,\quad V(t_0)=u_0.
\]
Their explicit solutions are
\[
U(s)=\sqrt\varepsilon
\tan\!\left(\arctan\frac{u_0}{\sqrt\varepsilon}
                +\sqrt\varepsilon(s-t_0)\right),
\qquad
V(t)=\frac{u_0}{1-u_0(t-t_0)}.
\]
The blow-up times satisfy
\[
T_U=t_0+\frac{\arctan(\sqrt\varepsilon/u_0)}{\sqrt\varepsilon}
<T_V=t_0+\frac1{u_0}.
\tag{19}
\]
As \(t\uparrow T_U\), \(U(t)\to\infty\) while \(V(t)\) stays finite;
therefore \((V-U)/U\to-1\). A fixed-terminal relative-error margin
strictly below one fails, even though the unforced solution also blows up.
The smooth constant force has changed the time.

Define, for \(t<T_V\),
\[
\theta(t)=t_0+
\frac{\arctan(V(t)/\sqrt\varepsilon)
      -\arctan(u_0/\sqrt\varepsilon)}{\sqrt\varepsilon}.
\]
Then \(\theta(t_0)=t_0\), \(\theta(t)\uparrow T_U\), and
\[
U(\theta(t))=V(t),\quad
\theta'=\frac{V^2}{V^2+\varepsilon}>0,\quad
\sigma'=-\frac{\varepsilon}{V^2+\varepsilon}.
\tag{20}
\]
The scalar counterpart of (3) is exactly
\[
\varepsilon+\sigma' U'(\theta(t))=0.
\]
Thus a nontrivial time modulation removes the force completely in this
model. This proves that fixed-time shadowing is a sufficient strategy,
not a necessary feature of singularity persistence. It is not an NS
example: a scalar force can lie in its one-dimensional time-tangent
space for reasons unavailable to a general spatial vector field.

## 8. Connection to the actual external reference and remaining task

The source's
[FinalSlowBase.origin](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/FinalSlowBase.lean#L361)
gives an exact axial value
\[
U_{\rm base}(s,0)=j_{\rm axis}(1-s)^{-A_h}e_3,\qquad
A_h=\tfrac12+h,\quad j_{\rm axis}>0.
\]
The actual assembly uses
[GermCandidateAssembly.origin_eventually_base](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/GermCandidateAssembly.lean#L109)
and origin_blowup, followed by
[MixedPeriodicAssembly.periodicVelocity_origin](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedPeriodicAssembly.lean#L87),
to preserve the origin signal in the stated assembly. The completed
[external modulation source note](external-modulation-source.md)
pins that identification, distinguishes the axial signal from the shrinking
azimuthal circle, and derives a full-gradient lower bound. Its centrifugal
calculation is explicitly a frozen local symbol, not an actual unstable
mode or propagator estimate. No new formal replay is performed here.

Already at the exact base signal,
\(\partial_sU_{\rm base}(s,0)=
A_hj_{\rm axis}(1-s)^{-A_h-1}e_3\).
A small time shift can therefore produce a large fixed-time error in
the direction of this tangent. Under (2), the reference signal is
observed at \(x=-a(t)\), with velocity \(U(\theta(t),0)+b(t)\).
Neither this point nor the unshifted origin is automatically a material
particle. Pointwise profile identities do not determine a Lagrangian
trajectory or establish transverse stability.

The next meaningful estimate is consequently a full-pressure stability
bound after explicit parameter selection, including a controlled Gram
matrix or another justified gauge, the normal residual, nonlinear
couplings and all parameter derivatives. The scalar example rules out
interpreting failure of a fixed-terminal test as a no-go theorem.
The exact moving-frame identities also rule out treating translation
or time reparameterization as cost-free removal of a general force.
