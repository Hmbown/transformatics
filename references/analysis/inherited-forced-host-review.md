# Independent review of the inherited forced-host calculation

8 September 2026. Reviewer: separate AI agent outgoing_outer.
**PASS at the stated finite-construction and unchanged-field scope.**
This is an independent written mathematical review, not external expert
acceptance, a formal certificate, or a proof of ROOT or FORCED-D.

## Pinned source

[inherited-forced-host.md](inherited-forced-host.md),
SHA-256:

    33b99003fe91d9112b61b42350106ddf6145a1b2144ea2c86dfc9c191281e42a

The reviewer read the complete source, the earlier finite affine-core
construction, and the final added vertical-amplitude inequality (26a).
No source or canonical file was changed by this reviewer.

The positive result is a real finite-wavelength nonnormal receiver gain.
The obstruction is the full nonlinear force required by the exact
specified two-wave velocity. A changed velocity may change that force.
The review does not infer absence of amplification from eigenvalues.

## 1. Older state, actual trajectories and coordinate changes

The old state is the full compact H+W with its previously specified
pressure and complete force. On its plateau, the gradient
\(A+sE_{31}\) has the same eigenvalues as A, but the antisymmetric
part has Frobenius norm \(|s|/\sqrt2\). The stated lower bound on its
distance from every symmetric matrix follows from the orthogonal
symmetric/antisymmetric decomposition. It does not give a bound on its
nonnormal propagator.

Direct integration of the plateau particle equations gives the source's
flow map (7): the quantity \(\kappa(t)x_1(t)=KX_1\) is constant, while
the vertical coordinate has the additional integral I(t). Differentiation
and inversion give (8),(10), including the off-diagonal shear and its
cosine factor. The plateau test (9) evaluates the actual particle inside
the older cutoff, which follows A rather than the full velocity.
An entire central ball must pay the displayed shear displacement; the
central particle alone does not certify a ball.

The lower heat clock for a receiver with nonzero initial third covector
component follows just from \(\xi_3=e^{3\lambda t}\xi_{03}\).
The remaining shear term in \(\xi_1\) is not discarded from the full
clock. A generic descendant cannot reuse the parent's contracting
frequency history.

The nonorthogonal similarity in (12) was independently checked:
\(PAP^{-1}=A+4\lambda cE_{31}\), with \(c=s/(4\lambda)\), and
\[
 P^{-1}P^{-T}
 =\begin{pmatrix}1&0&-c\\0&1&0\\-c&0&1+c^2\end{pmatrix}.
\]
Differentiating \(u(t,x)=P(t)v(t,P^{-1}x)\) gives both the moving-frame
drift \(-Cy\) and the extra term Cv. Pressure and diffusion acquire the
same metric. The source does not identify this coordinate change with
an orthogonal physical frame or preserve isotropic viscosity by fiat.

## 2. Principal gain versus the actual finite-wavelength receiver

For the central principal receiver with covector parallel to e2, b2
stays zero and the full principal pressure term vanishes. The selected
solution (14) follows by integrating
\[
 \int_0^t s(v)e^{-4\lambda v}\,dv
   ={s_0\over\nu K^2}\bigl(1-e^{-D_1(t)}\bigr).
\]
Its gain can be large even though the eigenvalues did not change.

The actual finite-wavelength mixed mode must also diffuse in x1. The
reviewer independently substituted the complete three-component interior
velocity into ordinary NS with the stated quadratic pressure. Using
the amplitude equations (16), every term cancels except
\[
 -bc\kappa\sin(\kappa x_1)\sin^2(\ell x_2)e_3.
\]
In particular:

- receiver-on-parent transport is exactly the source \(-ba\kappa\)
  in the c equation;
- the mixed mode pays \(\nu(\kappa^2+\ell^2)\), not just
  \(\nu\ell^2\);
- parent-on-receiver transport and parent self-advection vanish in the
  plateau geometry;
- the displayed residual is the receiver's full remaining self-advection.

The explicit c formula solves this full equation. Omitting its x1 heat
cost would replace it by the central principal calculation and can
change the gain by an order-one factor when \(\nu K^2\) is comparable
to \(\lambda\).

The velocity and gradient ratios (20) were checked separately. Maximizing
\(e^{-\Theta}(1-e^{-2\Theta})\) gives \(2/(3\sqrt3)\) at
\(\Theta=(\log3)/2\), so a descendant gradient at least as large as the
parent's indeed requires the supplied gradient \(|b_0|L\ge3\sqrt3\lambda\).
The source explicitly treats b0 as input and c as its generated response.

## 3. Compact realization and mixed derivative budget

Taking the curl of the potentials in (21), without a cutoff, gives
exactly the stated b and c modes, with both signs correct. Multiplication
by the transported compact bump before taking curl makes the full
periodic receiver solenoidal and mean zero. All new cutoff terms are
included by evaluating (22) on that exact curl.

The source keeps the old pressure and specifies the force directly.
Consequently no periodic Leray tail or pressure reconstruction is
missing from this finite forced construction. The interior residual
above and the cutoff defects are parts of the same actual force.

The deliberately coarse bound (23) is sufficient. Each extra spatial
derivative is covered by
\(M_x=K_*+L_*+\rho^{-1}\). Eulerian time differentiation of the phases
costs \(\lambda(K+L)r\); it is not bounded merely by the material
derivative. The inverse covectors cost \(\lambda\), and the profile
cutoff also has that time scale. The term \(a_*K_*\) in M_t controls the
source of c, including the initial time when c=0. Higher fixed time
derivatives of its coefficients are bounded inductively from (16).

The braces in (23) cover, respectively, V's time derivative and viscosity,
H-on-V and V-on-H transport, both parent/receiver interactions, and the
receiver self-interaction. Activation contributes precisely
\(\alpha'V\), in addition to the scaled linear and quadratic terms.
The old complete force and any separate host ramp still have to be
added. No finite collection of these derivative estimates is asserted
to give an infinite smooth terminal-force sequence.

## 4. Pressure-independent cost and the stronger additive bound

On the specified surviving rectangle, the two vertical sides see
opposite constant values of the residual force. Its circulation has
magnitude \(2|bc|\kappa h_3\); its perimeter is
\(2h_3+2\pi/\kappa\). With \(\kappa h_3\ge\pi\), this yields
\[
 \|f\|_\infty\ge |bc|\kappa/2.
\]
The host force and all cutoff defects vanish on this loop. A smooth
pressure change has zero circulation, so the lower bound concerns the
total actual force and is independent of the chosen pressure.

Substituting the exact a,b,c formulas gives
\[
 |bc|\kappa/2={\lambda|c|^2\over a(e^{2\Theta}-1)}.
\]
The transition inequalities (25),(26) therefore follow with the stated
constants. Their bounded clock is the **base clock**
\(\Theta=\lambda\tau\), not the possibly much larger integral of the
full shear gradient. This wording was clarified during review.

The refinement (26a) is also correct. The rectangle contains a full
interval of length pi in \(\kappa x_1\), with \(\sin(\ell x_2)=1\).
That interval attains the absolute amplitude
\(A_{\rm new}=\sqrt{a^2+|c|^2}\) of the vertical oscillatory part.
Since
\[
 {|c|^2\over a}
  ={(A_{\rm new}-a)(A_{\rm new}+a)\over a}
  \ge2(A_{\rm new}-a),
\]
one obtains
\[
 A_{\rm new}-a
 \le {F(e^{2\Theta}-1)\over2\lambda}
 \le e^{2\bar\Theta}F\tau.
\]
This pays for a small relative descendant as well. It excludes the
affine part Ax and the independently supplied horizontal receiver b.
Adding these inequalities along a putative single solution still
requires actual matching of its full mixed outgoing profiles, supports
and older fields; the source does not assume that matching.

## 5. Negative controls and remaining scope

The following distinctions are necessary and preserved by the source:

- Changing only pressure cannot cancel the loop circulation. Changing
  the interior velocity can change the residual and is outside this
  obstruction.
- If the stated loop does not fit, its lower bound is unavailable.
  An exterior cutoff cannot cancel its circulation when the loop does fit.
- Unbounded base clocks, different geometry, or a different nonlinear
  completion require a new estimate; unchanged eigenvalues do not
  exclude their nonnormal dynamics.
- Splitting one unchanged parent flight into new labels does not alter
  its frequency, cutoff shape or finite \(\lambda\) growth clock.
- The exact passive-scalar completion (28) has the stated maximum
  principle for bounded smooth v on the affine interior model. It is
  not a global theorem for the compact three-dimensional periodic field,
  where localization creates additional components and feedback.

The positive finite amplifier, its required supplied receiver, the
restricted force obstruction and the remaining full nonlinear inheritance
problem are therefore separated correctly.

Eight bounded independent symbolic checks passed: the full nonlinear
residual, incompressibility, curl realization, exact transition force
identity, derivative and value at the gradient-ratio maximum, and the
nonorthogonal similarity and metric. The analytic force-product,
periodization, circulation and maximum-principle arguments were checked
directly. No DNS, publication, git mutation or canonical status edit
was performed.
