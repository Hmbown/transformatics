# Removing a late force: a precise shadowing criterion and its missing estimate

8 September 2026. Restricted analytic note; no new unforced singularity
claim. The external construction supplies a smoothly forced singular
reference. This note derives sufficient conditions under which **one**
unforced restart would inherit its growth, and identifies why smooth
forcing or flatness at one point does not verify those conditions.

**Subsequent result.** The [terminal-force calculation](terminal-force-nonzero.md)
proves that condition (8) below fails for the actual reference at every
fixed late restart. The conditional implication remains valid. The
[modulation note](modulated-force-removal.md) allows the
reference singular time and position to move; its estimates still require
verification for the actual error.

The external source is [OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The [source assessment](../navier-stokes/openai-result-bridge.md)
records the distinction between smooth terminal forcing and local
residual flatness. No perturbation theorem removing that force is imported.

## 1. Exact equation and quantifier order

Work on the fixed three-dimensional torus, or on \(\mathbb R^3\) with
the regularity and decay needed for the displayed global norms and
integrations. Fix \(\nu>0\), a time \(t_0<T\), and a smooth reference
\[
\partial_tU+(U\cdot\nabla)U+\nabla P-\nu\Delta U=f,
\qquad \nabla\cdot U=0,\qquad t_0\le t<T.
\]
Let \(V\) be the maximal smooth **unforced** solution with
\(V(t_0)=U(t_0)\). Set \(e=V-U\) and \(\pi=p-P\). On their common
interval of smooth existence,
\[
\partial_te+(U\cdot\nabla)e+(e\cdot\nabla)U
 +(e\cdot\nabla)e+\nabla\pi-\nu\Delta e=-f,
\quad \nabla\cdot e=0,\quad e(t_0)=0.
\tag{1}
\]
Equivalently, the first and third transport terms are \(V\cdot\nabla e\).
The pressure difference obeys
\[
\Delta\pi=-\nabla\cdot f
-\partial_i\partial_j(U_i e_j+e_i U_j+e_i e_j).
\tag{2}
\]
All spatial cutoffs, mean corrections and localization errors already
belong to the reference's complete physical \(f\).

The proposed implication must hold with **one fixed \(t_0\) and one
initial datum**. Restarting closer to \(T\) for each requested terminal
accuracy produces a family of solutions and is not a singular trajectory.
If the maximal unforced solution fails before \(T\), it already supplies
the sought finite-time failure for this datum. Otherwise estimates below
can be used to continue it on every compact subinterval of \([t_0,T)\).

## 2. Relative energy: exact and insufficient by itself

Write \(S(U)=(\nabla U+\nabla U^T)/2\). Pairing (1) with \(e\),
\[
\frac12\frac d{dt}\|e\|_2^2+\nu\|\nabla e\|_2^2
=-\int e^TS(U)e-\int f\cdot e.
\tag{3}
\]
Pressure and \(V\cdot\nabla e\) cancel by divergence freedom; the
quadratic error has not been omitted. Put
\[
a_2(t)=\|\max(0,\lambda_{\max}(-S(U(t))))\|_\infty,\quad
F_2(t)=\|\mathbb P f(t)\|_2.
\]
Then, by regularizing the norm at zero,
\[
\|e(t)\|_2\le
\Phi_2(t):=\int_{t_0}^t
 \exp\!\left(\int_s^t a_2(r)\,dr\right)F_2(s)\,ds.
\tag{4}
\]
The Leray projection is harmless in \(L^2\), but not a pointwise local
operation. The coefficient in (4) is the actual reference strain; its
size is not inferred from the dimensions of the concentration region.

The reported reference scales, with \(\tau=T-t\), are
\[
\ell_r=\tau^{1/2},\qquad \ell_z=\tau^{1/2-h},\qquad
A=\tau^{-1/2-h},\qquad 0<h<1/6.
\tag{5}
\]
For a nondegenerate fixed-shape core with these dimensions, its volume
scales as \(\ell_r^2\ell_z=\tau^{3/2-h}\), so its \(L^2\) signal scale is
\[
A(\ell_r^2\ell_z)^{1/2}=\tau^{1/4-3h/2}\longrightarrow0.
\tag{6}
\]
This is a change-of-variables calculation, **not** a claim that the full
oscillatory reference has only those frequencies or obeys corresponding
gradient estimates.

To inherit a signed core average by an \(L^2\) error bound, one would
need an error small compared with (6), together with an actual
noncancelling core test. A fixed small absolute energy error is not enough.
Indeed, if \(F_2\) is nonzero on any earlier subinterval, the nonnegative
upper bound \(\Phi_2\) never tends to zero. Thus (4) cannot itself verify
that shrinking relative tolerance. This is an obstruction to that
norm-only extraction, not a lower bound on the true error.

## 3. An explicit strong-norm sufficient condition

For integer \(s\ge3\), standard differentiated product estimates applied
to (1), retaining the pressure through the \(H^s\)-bounded Leray
projection, give on the smooth interval
\[
\frac d{dt}E_s\le a_s(t)E_s+C_sE_s^2+F_s(t),\quad
E_s=\|e\|_{H^s},\quad
a_s=C_s\|U\|_{H^{s+1}},\quad F_s=\|\mathbb P f\|_{H^s}.
\tag{7}
\]
The leading \(U\cdot\nabla D^s e\) term cancels in energy;
commutators and \(e\cdot\nabla U\) are bounded by the stated
\(H^{s+1}\) norm. The error self-interaction is bounded by
\(C_s\|\nabla e\|_\infty E_s\le C_sE_s^2\).
Viscosity has nonnegative energy contribution and may be retained.
This deliberately coarse coefficient uses actual derivatives of \(U\).

Define quantities determined entirely by the reference and its force:
\[
\Phi_s(t)=\int_{t_0}^t
e^{\int_r^t a_s}\,F_s(r)\,dr,\qquad
4C_s\int_{t_0}^T\Phi_s(t)\,dt<1.
\tag{8}
\]
Then \(E_s(t)\le2\Phi_s(t)\). To see this, set
\(A_s(t)=\int_{t_0}^t a_s\) and
\(G_s(t)=e^{-A_s(t)}\Phi_s(t)\), which is nondecreasing.
Under the bootstrap \(E_s\le2\Phi_s\), the nonlinear Duhamel term is
at most
\[
4C_s e^{A_s(t)}
\int_{t_0}^tG_s(r)\Phi_s(r)\,dr
\le4C_s\Phi_s(t)\int_{t_0}^t\Phi_s(r)\,dr<\Phi_s(t).
\]
A first-crossing argument closes the bound. Finite reference norms on
every compact preterminal interval then prevent an earlier \(H^s\)
breakdown of \(V\).

If the actual reference has a peak lower bound \(A_{\rm ref}(t)\)
tending to infinity along a sequence, and
\[
2C_{\rm emb}\Phi_s(t)\le\theta A_{\rm ref}(t),\qquad 0<\theta<1,
\tag{9}
\]
along that sequence, the same \(V\) has unbounded speed and cannot
extend smoothly through \(T\).
Equations (8)–(9) are a sufficient test using only \(U,f\); they do not
assume that an unknown unforced solution stays close. The subsequent
[source-specific calculation](terminal-force-nonzero.md)
shows that (8) is **not satisfied** by the external reference. Its
nonzero terminal projected force and the inner-circle gradient lower
bound make the scalar majorant nonintegrable. This conclusion concerns
the coarse test, not the unknown unforced solution.

## 4. A sharper target: the actual linear propagator and a nonlinear budget

The coarse \(H^{s+1}\) coefficient can lose important cancellations.
Let \(\mathcal S_U(t,r)\) be the full viscous, divergence-free
linearized propagator about \(U\):
\[
\partial_tz+\mathbb P((U\cdot\nabla)z+(z\cdot\nabla)U)
-\nu\Delta z=0.
\]
This retains its complete pressure and deformation. On every compact
preterminal interval it is defined by the smooth reference. Equation (1)
has the exact representation
\[
e(t)=-\int_{t_0}^t\mathcal S_U(t,r)\mathbb P f(r)\,dr
-\int_{t_0}^t\mathcal S_U(t,r)\mathbb P\nabla\cdot(e\otimes e)(r)\,dr.
\tag{10}
\]
Set \(\alpha=1/2+h\). Define the actual linear-response number
\[
F_*=\sup_{t_0<t<T}\tau^\alpha
\left\|\int_{t_0}^t\mathcal S_U(t,r)\mathbb P f(r)\,dr\right\|_\infty.
\tag{11}
\]
Suppose a proved tensor-to-vector bound is available:
\[
\|\mathcal S_U(t,r)\mathbb P\nabla\cdot H\|_\infty
\le K(t,r)\|H\|_\infty.
\]
The required nonlinear number is
\[
B_*=\sup_{t_0<t<T}\tau^\alpha
\int_{t_0}^tK(t,r)(T-r)^{-2\alpha}\,dr.
\tag{12}
\]
All tensor norm constants can be included in \(K\).
If
\[
4B_*F_*<1,\qquad 2F_*<c,
\tag{13}
\]
and the actual reference has \(\|U(t)\|_\infty\ge c\tau^{-\alpha}\)
along a terminal sequence, then the same unforced restart is singular
by time \(T\).

Indeed, on each smooth interval, the weighted error supremum \(X\)
satisfies \(X\le F_*+B_*X^2\). Starting at zero, it cannot cross
\(2F_*\) under (13), so
\(\|e(t)\|_\infty\le2F_*\tau^{-\alpha}\).
On every compact preterminal interval this bounds \(V\) in \(L^\infty\);
the usual strong continuation criterion continues it there. The stated
peak margin proves terminal growth. If \(F_*=0\), uniqueness gives
zero error and the conclusion is immediate.

This criterion isolates two reference-only tasks: a **signed full linear
force response**, and a bilinear propagator bound. It does not replace
them by an assumption on \(V\). Neither is supplied by a covariance
identity, residual flatness or the geometric scales (5).

There is already a precise limitation on the ordinary heat estimate.
Even if one could use the favorable majorant
\[
K(t,r)\le C\nu^{-1/2}(t-r)^{-1/2}
       \left(\frac{T-r}{T-t}\right)^\beta
\tag{14}
\]
for some fixed \(\beta\), inserting its right side into (12) yields
an **infinite majorant** when \(h>0\).
Restricting its positive integral to \(T-r\in[3\tau/2,2\tau]\) gives
a constant times
\[
\tau^\alpha\,\tau\,\tau^{-1/2}\tau^{-2\alpha}
=\tau^{1/2-\alpha}=\tau^{-h}.
\tag{15}
\]
This proves failure of that unstructured majorant, not divergence of
the actual operator norm or impossibility of removal. Any successful
argument needs additional localization, cancellation, anisotropic
control or a different function space that improves this budget.
We have not inferred (14), or any gradient estimate, for the released
reference.

## 5. What flatness does and does not provide

Under the strong interpretation that \(f\) extends smoothly near
\((T,0)\) and every mixed derivative vanishes there, Taylor's theorem
does give
\[
|\partial^\gamma f(t,x)|\le C_{\gamma,M}(\tau+|x|)^M
\]
on a fixed sufficiently small neighborhood, for every fixed \(M\).
On a core obeying (5), \(|x|\lesssim\tau^{1/2-h}\), so this is
arbitrary-order smallness on that core. Mere statements about values
along \(x=0\) without joint smooth extension would be weaker.

However, the physical force need not be flat away from that point.
Both pressure and the linearized propagator are nonlocal.
For a concrete periodic example, take a nonzero smooth nonnegative even
\(\varphi(x_1)\) supported away from \(|x_1|<r\), and set
\(f=e_2\varphi(x_1)\sin x_2\).
The entire force vanishes near the origin. Let
\[
G(s)=-\frac{\cosh(\pi-|s|)}{2\sinh\pi},\quad
v=G*\varphi,\quad p=v(x_1)\cos x_2,
\]
using ordinary Lebesgue convolution on \([-\pi,\pi]\).
The derivative jump of \(G\) at zero is \(1\), so
\(v''-v=\varphi\), and \(\Delta p=\nabla\cdot f\).
Evenness gives \(v=-A\cosh x_1\) in the force-free neighborhood,
with \(A>0\). Therefore
\[
\mathbb P f=(A\sinh x_1\cos x_2,-A\cosh x_1\sin x_2,0)
\]
there, and its strain at the origin is \(\operatorname{diag}(A,-A,0)\).
Pointwise all-jet flatness of \(f\) does not imply local flatness of its
projected dynamical effect. The example is smooth, stationary in time
and nonsingular; it tests the proposed locality inference only.

Even **global** all-orders time flatness does not erase a previously
generated error. The scalar linear model
\[
z'=\frac{\beta}{T-t}z+g(t),\quad z(t_0)=0,\quad
g(t)=e^{-1/(T-t)^2},\quad\beta>0
\]
has the exact solution
\[
z(t)=\tau^{-\beta}
\int_\tau^{T-t_0}\sigma^\beta e^{-1/\sigma^2}\,d\sigma.
\tag{16}
\]
For fixed \(t_0\), the integral tends to a strictly positive constant,
while every jet of \(g\) vanishes at \(T\). This is an exact unstable
memory mechanism, not an NS counterexample.

Accordingly, bounded smooth force and point-flatness do not verify
(8)–(9) or (11)–(13). We do not claim a counterexample to every possible
NS force-removal theorem: exhibiting a forced singular reference with
a globally regular unforced restart would itself require additional
analysis. The precise conclusion is that the supplied force properties
leave the necessary reference stability estimates unproved.

## 6. Frozen next estimate

Choose one late time \(t_0\) and compute or bound the **complete**
linear response in (11), including force outside the shrinking core.
Then seek a structured replacement for the divergent majorant
(14)–(15). A successful estimate must retain the actual high-frequency
corrections, pressure and fixed initial datum. Moving \(t_0\) with the
observation time, discarding projected far-field force, or estimating
only the leading similarity profile does not discharge this task.

This note establishes error identities, sufficient criteria and the
stated obstructions to particular estimates. It supplies no verified
force-removal bound for the external construction and no solution of
unforced ROOT.
