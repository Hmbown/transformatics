# Signed future covector on one fixed Gavrilov profile

8 September 2026. Restricted exact central-model calculation. This concerns
the full primary deformation and its receiving covector on one fixed actual
Gavrilov profile. It does not, by itself, continue an NS solution, control
its receiving polarization, or generate another seed. ROOT, (E′) and
FORCED-D remain open. No DNS is used.

## 1. Setting and statement

Use the unscaled profile and primary normalization of
[the exact seed-cost reduction](actual-seed-cost.md),
sections 2–4, and
[the outer matching argument](outer-matching.md).
One sufficiently thin profile \(V_j\), with \(f_j(P_j)=1\), is fixed
before \(\ell\) tends to infinity. Write its positive relative Floquet
exponent as \(\mu=\mu_j\), its thin parameter as \(r_j\), and its
primary solutions as

\[
 N'=-(\nabla V_j)^T N,\qquad
 \beta(t)=e^{\mu t}B_+(t),\qquad
 \alpha(t)=N(t)\times\beta(t).
\]

The periodic factors are expressed below in the equivariant orthonormal
frame \(E\). The physical factors return by the exact axial rotation;
no approximation over a growing number of circuits is made.

Let \(t_f\) denote the receiving focus: the time called \(t_*\) in the
seed-cost and outer-matching notes. Set

\[
 r_*={\alpha(t_f)\over|\alpha(t_f)|},\quad
 s_*={e^{\mu t_f}\over\ell},\quad
 t=t_f+\tau,\quad \tau\ge0.
\]

In the present construction \(t_f=(2/\mu)\log\ell-\ell^{-3/4}\), so
\(s_*\asymp\ell\). The exact central model is

\[
 \overline A(t)=\nabla V_j(X(t))-\ell^{-1}\beta(t)\otimes N(t),
 \quad \xi'= -\overline A^T\xi,\quad \xi(t_f)=r_*.
\]

Let \(F(t_f,t)\) be the exact Euler-particle deformation from \(t\) to
\(t_f\). The exact model deformation gives

\[
 C(t)=F(t_f,t)^T r_*,\qquad
 \xi(t)=C(t)-f(t)N(t),\qquad
 f(t_f)=0,\qquad
 f'(t)=-\ell^{-1}\beta(t)\cdot C(t).                 \tag{1}
\]

For every sufficiently thin fixed profile, uniformly over the terminal
orbital phase and **all** \(\tau\ge0\),

\[
 C(t_f+\tau)\cdot B_+(t_f+\tau)=2\tau+O(r_j\tau),     \tag{2}
\]

and consequently

\[
 f(t_f+\tau)<0\quad(\tau>0),\qquad
 \left|f(t_f+\tau)+2s_*H_\mu(\tau)\right|
       \le C r_j s_*H_\mu(\tau),                     \tag{3}
\]

where

\[
 H_\mu(\tau)=\int_0^\tau s e^{\mu s}\,ds
     ={1+(\mu\tau-1)e^{\mu\tau}\over\mu^2}.           \tag{4}
\]

The constant in (3) is independent of \(\tau,\ell\), and the terminal
phase, throughout a fixed sufficiently thin range of profiles. Thus

\[
 |f(t_f+\tau)|\asymp
 \begin{cases}
 s_*\tau^2,&0\le\tau\le1,\\
 s_*(1+\tau)e^{\mu\tau},&\tau\ge1,
 \end{cases}                                        \tag{5}
\]

and, for sufficiently large \(\ell\),

\[
 |\xi(t_f+\tau)|\asymp 1+s_*H_\mu(\tau).             \tag{6}
\]

There is no second zero of \(f\) in this future central geometry.
These estimates hold, in particular, through \(\tau=O(\log\ell)\)
with the **same fixed** \(j\). They are not a conclusion about the
exact receiving polarization or the nonlinear solution on that interval.

## 2. Exact action shear and the signed scalar pairing

To distinguish it from the covector \(C\), write the action-coordinate
matrix called \(C_j\) in the seed-cost note as

\[
 \mathcal C_j(t)=E(t)^T
   [\,r_j\Phi_I,\ \Phi_\sigma/r_j,\ \Phi_\beta\,].
\]

The analytic coordinates and the exact steady action flow give

\[
 \mathcal C_j=I+O(r_j),\qquad
 D_j=\begin{pmatrix}
 0&0&0\\ r_j^2\Omega'_1&0&0\\r_j\Omega'_2&0&0
 \end{pmatrix},\qquad D_j^2=0,
\]

\[
 E(t_f)^TF(t_f,t_f+\tau)E(t_f+\tau)
   =\mathcal C_j(t_f)(I-\tau D_j)
                   \mathcal C_j(t_f+\tau)^{-1}.       \tag{7}
\]

Equation (7) is exact for either sign of the time difference. Moreover,

\[
 D_j=D_0+O(r_j),\quad
 D_0=\begin{pmatrix}0&0&0\\-2&0&0\\-c&0&0\end{pmatrix},
 \quad c=1/\sqrt2.
\]

In the \(E\) frame the normalized primary factors and unit receiver obey

\[
 N=k_0+O(r_j),\quad k_0=(0,-c,2),\quad
 B_+=b_++O(r_j),\quad b_+=(1,1/3,c/6),
\]
\[
 r_*=r_0+O(r_j),\qquad r_0=(-1/3,8/9,4c/9).
\]

The errors and their fixed time derivatives are uniform over all angles.
This follows from the analytic coordinate estimates and the simple
hyperbolic relative monodromy on one fixed poloidal circuit, as in the
incoming matching proof. In particular the derivatives of the \(E\)-frame
periodic factors are \(O(r_j)\). Periodicity bounds their values for
arbitrarily many circuits without an accumulating coefficient error.

For any primary factor \(B\), (7) gives exactly

\[
 C\cdot B=a_B(\tau)-\tau b_B(\tau),                    \tag{8}
\]
\[
 a_B=r_{*,E}^T\mathcal C_j(t_f)
             \mathcal C_j(t_f+\tau)^{-1}B_E(t_f+\tau),
\]
\[
 b_B=r_{*,E}^T\mathcal C_j(t_f)D_j
             \mathcal C_j(t_f+\tau)^{-1}B_E(t_f+\tau).
\]

For \(B=B_+\), the thin pairings are

\[
 r_0\cdot b_+=0,\qquad r_0\cdot D_0b_+=-2.
\]

Consequently \(a_+=O(r_j)\), \(a_+'=O(r_j)\), and
\(b_+=-2+O(r_j)\), uniformly for all future time. Exact terminal
orthogonality gives \(a_+(0)=r_*\cdot B_+(t_f)=0\). Therefore

\[
 |a_+(\tau)|\le Cr_j\min(\tau,1),\qquad
 |b_+(\tau)+2|\le Cr_j.
\]

Equation (8) proves (2), including the relative error near zero.
An additive \(O(r_j)\) error without this terminal vanishing would
not determine the near-zero sign.

## 3. Integration, ray size, and central attenuation

Retain the exact \(\mu_j\) inside the long exponential. Equations
(1) and (2) give

\[
 -f'(t_f+\tau)=s_*e^{\mu\tau}[2\tau+O(r_j\tau)].       \tag{9}
\]

Choose \(j\) once so that the relative error is less than \(1\).
Integrating proves (3) and the strict sign. Since \(\mu_j\) lies in a
fixed compact subset of \((0,\infty)\), elementary estimates of the
positive integral (4) give (5).

For (6), (7) gives \(|C|\le C(1+\tau)\). Near zero the projection
of \(C\) onto \(N(t_f+\tau)^\perp\) has a positive lower bound because
it equals the unit vector \(r_*\) at zero. This gives a lower bound
when \(|f|\) is bounded; when \(|f|\) exceeds a sufficiently large
fixed constant, the term \(fN\) gives the lower bound by the triangle
inequality. Outside that fixed small time interval, (5) and
\(s_*\to\infty\) imply \(|f|\gg|C|\) uniformly. The upper bound follows
directly from (1).

A useful consequence for the central ray alone is

\[
 \int_0^\tau|\xi(t_f+s)|^2\,ds
 \le C\{1+\tau+s_*^2(1+\tau)^2e^{2\mu\tau}\}.          \tag{10}
\]

At \(\tau=(\log\ell)/(8\mu)+(\log\eta)/\mu\), with fixed
\(\eta>0\) and sufficiently large \(\ell\),

\[
 |\xi|\asymp\eta\ell^{9/8}(1+\tau),\qquad
 {\epsilon\over k^2}\int_0^\tau|\xi|^2\,ds
 \le C_\nu h\{1+\tau+
                  \eta^2\ell^{9/4}(1+\tau)^2\}=o(1).
\]

Here \(\epsilon=\nu h^4\) and \(k=h^{3/2}\). This checks only the
added central principal attenuation. Spatial phase derivatives, the
whole packet, pressure-corrected amplitudes and nonlinear residuals
require separate estimates.

## 4. Stable pairing and its nonzero integrated coefficient

Normalize the contracting primary factor by

\[
 B_-(t)=b_-+O(r_j),\qquad b_-=(1,-1/3,-c/6).
\]

The exact thin moving-frame amplitude generator is

\[
 G_0=-A_0-O_0+2k_0k_0^TA_0/|k_0|^2
 =\begin{pmatrix}0&2&0\\2/9&0&0\\c/9&0&0\end{pmatrix}.
\]

Direct multiplication gives \(G_0b_\pm=\pm(2/3)b_\pm\). Equation
(8) similarly gives

\[
 C\cdot B_-=2\tau-2/3+O(r_j(1+\tau)),\qquad
 |C\cdot N|\le Cr_j\tau.                              \tag{11}
\]

No fixed sign is claimed for \(C\cdot B_-\): its thin value changes
sign at \(\tau=1/3\). Its exponentially weighted future integral,
however, is uniformly nonzero. Define

\[
 I_j(\tau)=\int_0^\tau e^{-\mu_j s}
                 C(t_f+s)\cdot B_-(t_f+s)\,ds.
\]

Then, uniformly in terminal phase,

\[
 I_j(\infty)=7/2+O(r_j),\qquad
 |I_j(\infty)-I_j(\tau)|
       \le C(1+\tau)e^{-\mu_j\tau}.                   \tag{12}
\]

Indeed the error in (11) is integrable against \(e^{-\mu_j s}\).
The elementary integral changes by \(O(r_j)\) when its exponent
changes from \(2/3\) to \(\mu_j=2/3+O(r_j)\). The same
polynomial-exponential bound gives the tail estimate. Hence
\(I_j(\tau)\) is uniformly positive for sufficiently large fixed
\(\tau\); an earlier cancellation is not excluded.

At the exact thin limit,

\[
 I_0(\tau)=\frac72-\left(\frac72+3\tau\right)e^{-2\tau/3}.
\]

For the reduced triangular outgoing amplitude equation only, put
\(y_2(\tau)=y_{2,0}e^{-\mu\tau}\). Its exact integrating factor obeys

\[
 {d\over d\tau}\{f e^{-\mu\tau}y_1\}
       =s_* (C\cdot B_-)y_2.                         \tag{13}
\]

If its homogeneous constant at the focus is zero, then
\(f e^{-\mu\tau}y_1=s_*y_{2,0}I_j(\tau)\). The coefficient in (13)
is \(s_*=e^{\mu t_f}/\ell\) with this **relative-time** integrating
factor. Using \(1/\ell\) would omit \(e^{\mu t_f}\).
At the thin limit \(y_{2,0}=3bD/2\), the small-time behavior
\(y_1\sim bD/\tau\) and the late behavior \(y_1\sim-7bD/(4\tau)\)
are consistent. This check does not justify discarding the full
outer remainders; the inner matching and their perturbation must be
proved separately.

## 5. Checks and scope

The exact thin matrix, both eigenvectors, the future covector
\(C=r_0+2\tau e_1\), and all pairings in (2) and (11) were checked by
symbolic matrix multiplication with rational coefficients and
\(c=\sqrt2/2\). The stable integral and its endpoint normalization
were independently derived by the outgoing-polarization agent.
These are bounded exact algebra checks, not fluid simulations.

The essential geometric result is (2): a signed linear pairing with a
relative error uniform for arbitrary future time. It uses the fixed
profile's exact nilpotent action shear and periodic factors. This rules
out a second zero in the future central ray and supplies a nonzero
weighted stable coupling. Full outgoing polarization, actual-\(q_h\)
comparison, nonlinear continuation and an infinite construction remain
separate obligations.

**Separate review:** the outgoing-polarization agent independently checked
the signed exact action shear, the terminal pairing vanishing and derivative
bound, the all-future sign and ray size, and the stable integral. No gap was
found in this central-model statement. In the reverse review, this note's
author independently checked the inner normalization, signed stable trace,
and weighted full-pressure perturbation in
[the outgoing outer proof](outgoing-outer.md).
Neither review is an audit of the separate nonlinear PDE lifting.
