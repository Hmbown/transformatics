# Local force flatness is not preserved by Leray projection

Date: 8 September 2026.

**Scope.** This note proves an elementary obstruction to inferring local
smallness of the dynamically active force from local smallness of the raw
force. It constructs a smooth, mean-zero force on the three-torus which
vanishes on an open neighborhood, although its Leray projection has
nonzero symmetric gradient there. It does not identify this example with
the force in the external Navier–Stokes construction, and does not exclude
unforced continuations obtained by changing the velocity.

## 1. Pressure convention

Work on \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), with ordinary
Lebesgue measure. For a smooth periodic vector field \(f\), let \(\pi\)
be the mean-zero solution of

\[
\Delta\pi=\nabla\cdot f,
\qquad \mathbb P f=f-\nabla\pi.
\]

The mean of \(f\) is retained by \(\mathbb P\). In the forced equation

\[
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad \nabla\cdot u=0,
\]

the force decomposition gives

\[
\partial_tu+(u\cdot\nabla)u-\nu\Delta u
             +\nabla(p-\pi)=\mathbb P f.
\]

Here \(\pi\) is the pressure potential of the force, not generally the
entire fluid pressure. The latter also contains the nonlinear contribution.
A force can be removed from a fixed velocity trajectory by changing only
periodic pressure precisely when \(\mathbb P f=0\). Local vanishing of
\(f\) is a different condition.

## 2. An explicit smooth force with a force-free neighborhood

Choose \(0<r<\pi\) and a nonzero, nonnegative, even smooth periodic
function \(\phi\) such that

\[
\phi(s)=0\quad\text{for }|s|<r,
\qquad -\pi\le s\le\pi.
\]

For a concrete choice, put \(r=\pi/4\), let

\[
\eta(s)=
\begin{cases}
\exp\!\bigl(-1/(1-(4s/\pi)^2)\bigr),&|s|<\pi/4,\\
0,&|s|\ge\pi/4,
\end{cases}
\]

and periodically extend
\(\phi(s)=\eta(s-\pi/2)+\eta(s+\pi/2)\).
The zero extension is smooth at the bump boundaries, and this formula
vanishes near the endpoints \(\pm\pi\), so the periodic extension is
smooth as well.

Define

\[
f(x)=\phi(x_1)\sin x_2\,e_2.
\]

This field has zero spatial mean and vanishes identically on the open
strip \(V=\{|x_1|<r\}\). In particular, every spatial derivative of
\(f\) vanishes on \(V\). Its divergence is
\(\phi(x_1)\cos x_2\).

Let \(v\) be the periodic solution of

\[
v''-v=\phi,
\qquad \pi(x)=v(x_1)\cos x_2.
\]

Then \(\pi\) has zero mean and
\(\Delta\pi=(v''-v)\cos x_2=\nabla\cdot f\), so it is exactly
the pressure potential in Section 1.

The periodic Green function for \(\partial_s^2-1\) is

\[
G(s)=-\frac{\cosh(\pi-|s|)}{2\sinh\pi},
\qquad -\pi\le s\le\pi.
\]

Indeed, \(G''-G=0\) away from zero, its derivative has jump
\(G'(0+)-G'(0-)=1\), and its values and first derivatives match at
\(-\pi\) and \(\pi\). Thus
\((\partial_s^2-1)G=\delta_0\) in periodic distributions. Consequently

\[
v(s)=\int_{-\pi}^{\pi}G(s-y)\phi(y)\,dy
\]

solves the equation. There is **no normalized-average factor** in this
convolution. The homogeneous periodic equation has only the zero solution:
multiplying it by \(v\) and integrating gives
\(-\int(|v'|^2+|v|^2)=0\). This also proves uniqueness. The convolution
is smooth because one can put any derivative on the smooth periodic
\(\phi\).

Both \(G\) and \(\phi\) are even. Set

\[
A=-v(0)=\frac1{2\sinh\pi}
       \int_{-\pi}^{\pi}\cosh(\pi-|y|)\phi(y)\,dy>0.
\]

On \((-r,r)\), the equation is \(v''=v\), with initial values
\(v(0)=-A\) and \(v'(0)=0\). Therefore

\[
v(s)=-A\cosh s\quad (|s|<r).
\]

This proves the following exact formula throughout the force-free strip:

\[
\boxed{\mathbb P f(x)=
\bigl(A\sinh x_1\cos x_2,
      -A\cosh x_1\sin x_2,0\bigr).}
\]

## 3. The effect includes strain

Although \(\mathbb P f(0)=0\), its gradient at the origin is

\[
\nabla\mathbb P f(0)=
\begin{pmatrix}A&0&0\\0&-A&0\\0&0&0\end{pmatrix}.
\]

For \(S(g)=(\nabla g+\nabla g^{\mathsf T})/2\), this gives

\[
S(\mathbb P f)(0)=\operatorname{diag}(A,-A,0),
\qquad |S(\mathbb P f)(0)|_F=\sqrt2 A>0.
\]

Writing \(M_\phi=\int_{-\pi}^{\pi}\phi(y)dy>0\), one has

\[
\frac{M_\phi}{2\sinh\pi}\le A
\le\frac{\cosh\pi}{2\sinh\pi}M_\phi.
\]

Thus the effect is quantitatively nonzero. Multiplying \(\phi\) by
any positive constant scales this strain by the same constant while
leaving every local derivative of \(f\) identically zero on \(V\).
There can be no bound for this strain solely in terms of those local force
derivatives. A spatially uniform acceleration has zero spatial gradient;
subtracting one cannot remove this example's strain. Its origin is not
the mean mode, since both \(f\) and \(\mathbb P f\) have mean zero.

Locally, \(\mathbb P f=-\nabla\pi\) is the gradient of a harmonic
function. This does not make it a removable global periodic gradient:
the original \(f\) has curl
\((0,0,\phi'(x_1)\sin x_2)\), which is not identically zero, and
\(\nabla\times\mathbb P f=\nabla\times f\). A globally periodic
gradient that is also divergence free would have harmonic periodic
potential and hence would vanish.

## 4. Spacetime flatness and the force-removal question

Fix any time \(T\) and take the time-independent force \(F(t,x)=f(x)\).
It is smooth, and is identically zero on an entire spacetime neighborhood
of \((T,0)\). All mixed derivatives vanish there: it satisfies a stronger
condition than merely being flat at that point. Nevertheless

\[
S(\mathbb P F)(T,0)=\operatorname{diag}(A,-A,0).
\]

One may instead multiply by a smooth time cutoff equal to one near \(T\)
without changing this conclusion. Leray projection acts at each time and
does not preserve local spacetime flatness. As a dynamical interpretation,
any smooth forced solution starting with zero velocity at a time when
this cutoff equals one necessarily satisfies
\(\partial_tu=\mathbb P f\) at that initial time. Its initial strain
derivative is the nonzero matrix above. This last statement is a direct
consequence of the equation, not an existence or singularity theorem.

The obstruction is narrow. It rules out the inference that raw force
flatness near a prospective singular point automatically makes the
projected forcing negligible there, or removable by pressure. It does
not rule out cancellation for a particular force, small global projected
force estimates, or constructing a different unforced trajectory by a
stability or correction argument. If a particular force is divergence
free, then \(\mathbb P f=f\), and its local vanishing is preserved.

To apply the obstruction to the external forced construction one must
inspect its actual force, its global pressure potential and the relevant
time-dependent estimates. No such identification is made here. Removing
its force would require a further argument about the dynamically active
part and its effect on the velocity; local flatness by itself supplies
neither that argument nor a contradiction to every possible unforced
continuation.

## Verification scope

The proof above is analytic and explicit. A separate AI-agent check
recomputed the Green-function derivative jump, the convolution
normalization, the projected field and the strain signs. No numerical
flow simulation, external-force calculation or formal proof certificate
is asserted.
