# Continuing the same supplied receiver through its polarization focus

8 September 2026. Restricted written analytic continuation, independently
reviewed by a separate AI agent. This note extends the
existing finite construction, with the same original datum and fixed physical
viscosity. It does not generate a new seed, prove an infinite trajectory, or
close ROOT or `(E′)`. The estimates below concern the full actual unforced
solution, except where a central ODE or comparison model is explicitly named.
No DNS or formal PDE certificate is used.

## 1. The longer finite statement

Keep all profile, bump, phase-profile and viscosity choices in
[the localized-profile theorem](../navier-stokes/localized-profile.md),
including its original datum

\[
Q_h(0)=V+Z_{1,h}(0)+Z_{2,h}(0),\qquad
h=L^{-1/10},\quad k=h^{3/2},\quad d=h^{5/4},\quad
\epsilon=\nu h^4,\quad \ell=\sqrt{\log(1/h)}.
\]

Let \(T=(2/\mu)\log\ell\) and \(t_f=T-\ell^{-3/4}\), exactly as before.
There is a fixed sufficiently small \(\delta>0\), chosen independently of
\(h\), for which the **same** actual solution continues smoothly through
\(t_f+\delta\). At the particle of the same first-stage solution \(q_h\)
used in the original construction, its already supplied receiving wave has

\[
 |S(Q_h-q_h)(t_f+\delta,Y_h(t_f+\delta))|_F
       \ge c_\delta\ell^{15/8}.                         \tag{1}
\]

The construction supplies the upper bounds

\[
 \int_0^{t_f+\delta}\|\nabla Q_h(t)\|_\infty\,dt
       \le C_\delta\ell^{15/8},\qquad
 \|Q_h\|_{H^{12}}\le h^{-117/8}G_h^+,
 \quad \log G_h^+=O(\ell^{15/8})=o(\ell^2),              \tag{2}
\]

and its complete corrected approximation \(U_h^+\) obeys

\[
 \sup_{[0,t_f+\delta]}\|Q_h-U_h^+\|_2
       \le h^{31/8}G_h^+,
 \qquad
 \sup_{[0,t_f+\delta]}\|Q_h-U_h^+\|_{C^1}
       \le h^{1/48}G_h^+.                               \tag{3}
\]

Here, and in (2), increasing \(G_h^+\) by fixed powers of \(\ell\) is
permitted. The powers of \(h\) are unchanged. Constants may depend on the
one fixed Gavrilov profile, fixed profile norms, \(\nu\), and \(\delta\).

The additional clock is of order \(\ell^{15/8}\) in the reference
construction; it remains strictly below the order \(\ell^2\) needed for a
fixed positive activation at the previously proposed finer cutoff. The
receiving velocity amplitude decreases after the focus while its covector
grows. This is continued compression of the supplied wave, not a new
independent amplifier or a new velocity blow-up mechanism.

The moving almost-affine radius-\(ck\) conclusion of
[the earlier short continuation](later-flow-attempt.md) is
**not** asserted on this longer interval. That core need not remain affine.
The argument instead continues the complete oscillatory profile with its
actual phase, envelope, pressure and global corrections.

## 2. Extend the first-stage state, without changing its original datum

The first-stage proof in
[the log-log handover](../navier-stokes/loglog-handover.md) uses
\(m_h(t)=1+\ell^{-1}e^{\mu t}\). On \([0,T+\delta]\), with fixed \(\delta\),

\[
 \sup m_h\le C_\delta\ell,\qquad
 \int_0^{T+\delta}m_h(t)\,dt\le C_\delta\ell,\qquad
 e^{C(T+\delta)}\le C_\delta\ell^{2C/\mu}.               \tag{4}
\]

Every amplitude/phase/mean/harmonic equation in that construction is solved
forward from its original data. Its support transport, spatial-jet hierarchy,
residual powers, relative energy inequality and separate high-Sobolev
bootstrap therefore hold on this enlarged interval, with changed fixed
constants. In particular, the fixed high orders used to obtain the actual
\(C^{24}\) bound in the original nonlinear handover give

\[
 \|D_x^r q_h(t)\|_\infty\le C_{r,\delta}m_h(t)h^{1-r},
 \quad 1\le r\le24.                                    \tag{5}
\]

The actual \(q_h\)-particle still tracks the reference \(V\)-particle with
the same positive-power errors: the proof's velocity and phase-drift
estimates only incur another \(e^{C_\delta\ell}\). Thus the central gradient
is within \(h^\gamma e^{C_\delta\ell}\), for a fixed \(\gamma>0\), of

\[
 \overline A(t)=\nabla V(X_V(t))-\ell^{-1}\beta(t)\otimes N(t)          \tag{6}
\]

through \(T+\delta\). This statement uses the full old \(V\) and its
pressure-corrected primary evolution; it does not replace them by two
stationary plane shears. Uniqueness identifies the extended state with the
previously constructed \(q_h\) on the common interval.

## 3. The inner connection has a different outgoing asymptotic

Use the exact moving-frame equations and all conventions in
[the inner matching calculation](inner-matching.md). In this
section \(e=\Lambda^{-1/2}\) is an inner parameter, not viscosity. Put

\[
 \Lambda=|\beta(t_f)||N(t_f)|/\ell\asymp\ell,
 \qquad z=(t_f-t)/e,
 \qquad a=a_{21}(t_f)<0,\quad c=a_{31}(t_f)<0.
\]

The pair \((a,c)\) stays in the same fixed compact negative coefficient
set as in the incoming proof. With
\(P(z)=1+a^2z^4\), its leading inner system is

\[
 V'=-W,\qquad
 W'=\frac{2a^2z^2+2c}{P}V-\frac{4a^2z^3}{P}W.
\]

The substitution \(V=P^{-1/2}Y\) gives, on the whole real line,

\[
 Y''=q(z)Y,\qquad
 q(z)=\frac{4a^2z^2-2cP(z)}{P(z)^2}>0.                  \tag{7}
\]

Here \(q\) is even and \(q(z)=O((1+|z|)^{-4})\). Let \(Y_+\) be the
incoming solution already selected by \(Y_+(+\infty)=1\),
\(Y_+'(+\infty)=0\). At zero it has \(Y_+(0)\ge1\) and
\(-Y_+'(0)\ge c_0>0\). Set \(s=-z\ge0\) and
\(\widetilde Y(s)=Y_+(-s)\). Its equation and initial slope imply

\[
 \widetilde Y(s)\ge c_1(1+s),\qquad
 c_1\le\widetilde Y'(s)\le C_1,
 \qquad \widetilde Y(s)\le C_1(1+s).                   \tag{8}
\]

For the upper bounds, use the Volterra equation from zero and
\(\int_0^\infty(1+s)q(s)\,ds<\infty\), followed by its differentiated
form. All constants are uniform on the specified compact coefficient set.
In particular there is \(b>0\) such that

\[
 Y_+(z)=a_0-bz+O(|z|^{-1}),\quad
 Y_+'(z)=-b+O(|z|^{-2})\qquad (z\to-\infty).            \tag{9}
\]

Indeed \(b=\widetilde Y'(0)+\int_0^\infty q(s)\widetilde Y(s)ds\), and
\(q\widetilde Y=O(s^{-3})\). Consequently the outgoing leading branch has

\[
 V(z)=\frac{b}{|a||z|}+O(|z|^{-2}),\qquad
 W(z)=-\frac{b}{|a|z^2}+O(|z|^{-3}).                    \tag{10}
\]

The incoming \(z^{-2}\) decay of \(V\) cannot be copied onto this side.
The sign change of \(W\) is also retained. This is a scattering statement
for the actual coefficient-dependent inner ODE, not an affine Kelvin
estimate for arbitrary three-dimensional errors.

## 4. Uniform passage to a fixed small time after the focus

The full moving-frame cotangent Taylor formulas also hold for
\(-\delta\le t_f-t\le0\). Their expansions are algebraic in the signed
variable \(z\):

\[
 x=2ae z+O(e^2z^2),\quad y=1+O(e|z|),\quad
 w=-az^2+O(e|z|+e|z|^3),\quad
 s_{\rm primary}=\Lambda[1+O(e|z|)].                    \tag{11}
\]

Choose \(\delta\) so small that \(|y|\ge1/2\) and
\(|\eta|^2\asymp1+z^4\) throughout \(-\delta/e\le z\le0\).
Insert (11) in the exact rational matrix from the incoming proof,
including its pressure denominator. The same cancellations, now with
\(|z|\), give

\[
 |E_{11}|+|E_{22}|\le Ce,\quad
 |E_{12}|\le Ce(1+|z|),\quad
 |E_{21}|\le\frac{Ce}{1+|z|},
\]

\[
 |E_{11}'|\le\frac{Ce}{1+|z|},\qquad |E_{12}'|\le Ce.    \tag{12}
\]

In particular the cancellation in the exact (3,1) numerator is unchanged
by allowing negative \(z\); no \(e|z|\) term is introduced into \(E_{21}\).
Eliminating \(W\), exactly as in the incoming calculation, gives

\[
 Y''=qY+r_1Y'+r_0Y,\qquad
 |r_1|\le Ce,\quad |r_0|\le Ce/(1+|z|).                 \tag{13}
\]

Here \(1/\beta\) in the elimination is bounded because
\(\beta=-1+E_{12}\) and \(e(1+|z|)\le e+\delta\).

The appropriate **outgoing** norm on \(0\le s\le R=\delta/e\) is

\[
 \|Y\|_{X_-}=\sup\frac{|Y(-s)|}{1+s}
                       +\sup|\partial_sY(-s)|.         \tag{14}
\]

The unperturbed Volterra resolvent is uniformly bounded in this norm,
again by \(\int_0^\infty(1+s)q(s)ds<\infty\).
The perturbing source \(r_1Y'+r_0Y\) is at most
\(Ce\|Y\|_{X_-}\) pointwise. One and two integrations, the latter divided
by \(1+s\), therefore have norm at most
\(CeR\|Y\|_{X_-}=C\delta\|Y\|_{X_-}\). Neumann inversion gives a uniform
full propagator and an \(O(\delta)\) relative error. For sufficiently small
fixed \(\delta\), it preserves both inequalities in (8) with smaller
positive constants. The previously proved incoming matching error at zero
is \(o(1)\), and remains such under this bounded outgoing propagator.

Let \(D_h\asymp\ell^{5/2}\) be the selected incoming normalization.
Reconstruction via the exact first row and transversality yields, uniformly
for \(0\le\tau=t-t_f\le\delta\), \(s=\sqrt\Lambda\tau\),

\[
 |\eta|\asymp1+s^2,\qquad
 b_p\asymp\frac{\sqrt\Lambda D_h}{1+s},\qquad
 |b_n|\le\frac{CD_h}{(1+s)^2},\qquad |b_r|\le CD_h.      \tag{15}
\]

For the \(b_n\) bound, differentiate \(V=P^{-1/2}Y\) and use
\(|\partial_sY|\le CD_h\); the extra \(E_{11}V\) term costs
\(eD_h/(1+s)\le C\delta D_h/(1+s)^2\).
For \(b_r\), use \(b_r=-(x\sqrt\Lambda V+w b_n)/y\).
By making \(\delta\) smaller once, the positive \(p\) component dominates
these other components. Thus

\[
 |b||\eta|\asymp\sqrt\Lambda D_h(1+s).                 \tag{16}
\]

This calculation retains the full old-flow matrix \(\nabla V\), its frame
rotation and its pressure correction. The terms involving \(a,c\) are
essential to (7)--(10).

## 5. Transfer to actual q, then to its whole packet

The comparison of unit covector directions, logarithmic covector magnitudes
and polarizations with (6) has coefficient \(C|\overline A|\).
On the longer interval its integral is still \(O(\ell)\) by (4).
The actual central ODE therefore differs by at most
\(h^{\gamma'}e^{C_\delta\ell}\), after reducing a fixed positive exponent
\(\gamma'\) if necessary. It is negligible against every fixed power of
\(\ell\). This is a finite central-ODE comparison only; no arbitrary-error
polynomial estimate is being used for the full PDE.

In the construction's actual normalization,
\(b_c=(k\ell^{7/8}/N_h)v_h\), where \(N_h\asymp D_h\), and the terminal
covector has length four. Equations (15)--(16) give

\[
 \frac{|b_c(t)||\xi_c(t)|}{k}
    \asymp\ell^{11/8}(1+\sqrt\ell\,\tau),
 \qquad 0\le\tau\le\delta.                             \tag{17}
\]

The receiving amplitude \(b_c\) here is the rescaled velocity
amplitude, not its gradient. In particular at fixed \(\delta\),
\(|b_c|\asymp_\delta k\ell^{7/8}\), whereas
\(|\xi_c|\asymp_\delta\ell\). The final strain exponent \(15/8\) comes
from covector growth rather than velocity growth. The central wave number
in these rescaled coordinates is `|xi_c|/k`, so its local phase length is
`k/|xi_c|`, of order `k/(ell delta^2)` at fixed delta. The full phase period
has the additional factor `2pi`.

At \(t_f\), the terminal profile has exactly constant phase gradient and
\(b=k\ell^{7/8}\chi_d c_h\). Continue these already specified data forward
by the exact actual-\(q_h\) phase and polarization equations. No backward
redesign of the original seed occurs. On its transported support, (4)--(5)
give

\[
 \operatorname{diam}(\operatorname{supp}b)\le d e^{C_\delta\ell}=o(h),
 \quad |\nabla q_h(x)-\nabla q_h(Y_h)|
                 \le h^{1/4}e^{C_\delta\ell}.            \tag{18}
\]

The same direction/log-magnitude comparison, now between a support
trajectory and the central trajectory, costs another \(e^{C_\delta\ell}\).
Thus its error in the product \(|b||\xi|/k\) is at most
\(h^{1/4}e^{C_\delta\ell}\), times fixed powers of \(\ell\), after
factoring out the transported bump. This proves the whole-support bound

\[
 \sup_{\operatorname{supp}b}\frac{|b||\xi|}{k}
    \le C_\delta\ell^{11/8}(1+\sqrt\ell\,\tau),
 \quad
 \int_{t_f}^{t_f+\delta}\sup\frac{|b||\xi|}{k}\,dt
    \le C_\delta\ell^{15/8}.                            \tag{19}
\]

The derivative hierarchy is triangular with top coefficient
\(C_r m_h\), as before. Through the same fixed orders, all slow jets of
\(b,\xi\) obey the old \(k d^{-r}e^{C_\delta\ell}\),
\(h^{-r}e^{C_\delta\ell}\) bounds, respectively. Support volume remains
\(O(d^3)\) by incompressibility. No higher jets of the **actual Q endpoint**
are inferred from its C1 closeness: these are jets of the independently
constructed phase and amplitudes on the known \(q_h\).

## 6. Full pressure, heat, errors and strong continuation

Continue all equations (8)--(23) of the localized-profile note from their
original initial conditions, using the extended \(q_h,b,\xi\).
Specifically, keep the complete periodic profile, its solenoidal curl lift,
central heat clock, pressure-bearing global mean and general forced-profile
correction. The identities are differential identities, so nothing changes
at \(t_f\); there is no temporal cutoff or restart residual.

By (15), (17), the central heat clock still obeys

\[
 0\le\tau_c(t)=\epsilon k^{-2}\int_0^t|\xi_c|^2ds
    \le C_{\nu,\delta}h\ell^2\log\ell=o(1).             \tag{20}
\]

The spatially nonconstant diffusivity mismatch is retained exactly as in
the original residual identity. From (18) and the fixed-order jet bounds,
its old estimate \(\nu h^{37/8}e^{C_\delta\ell}\) remains valid.
All other residual entries have the same powers of \(h\), because the
spatial scales and derivative orders are unchanged and the extended time
has length \(O(\log\ell)\). The global mean is estimated with its global
Sobolev norms; its pressure tail is not assigned compact volume. Hence

\[
 \int_0^{t_f+\delta}\|R_{\rm tot}\|_2dt
        \le h^{31/8}e^{C_\delta\ell}\operatorname{poly}(\ell),
 \qquad
 \int_0^{t_f+\delta}\|\nabla U_h^+\|_\infty dt
        \le C_\delta\ell^{15/8}.                       \tag{21}
\]

The first estimate uses the old residual table with enlarged finite
constants; the second uses (19), rather than exponentiating a coarse
\(e^{C\ell}\) bound for the primary gradient. Both include all profile
Fourier modes and the longitudinal pressure terms.

The exact relative-energy inequality therefore proves the L2 estimate in
(3) on the strong lifetime. Independently bootstrap
\(\|\nabla(Q_h-U_h^+)\|_\infty\le1\). The integer H12 energy estimate and
(21) give the bound (2). Uniform expanding-torus interpolation then yields

\[
 \|\nabla(Q_h-U_h^+)\|_\infty
 \le C(h^{31/8}G_h^+)^{19/24}
       (h^{-117/8}G_h^+)^{5/24}+Ch^{31/8}G_h^+
 \le h^{1/48}\widetilde G_h^+\longrightarrow0.          \tag{22}
\]

Since \(15/8<2\), the last factor is subpower in \(h\). The bootstrap
improves, and the separate H12 continuation alternative extends the actual
strong solution through \(t_f+\delta\). This proves (2)--(3).

At the central actual-\(q_h\) particle, \(S=0\) throughout. The fixed odd
profile's heat-rounded derivative at zero tends to one by (20). Its leading
gradient is \(-b_c\otimes\xi_c/k\), with \(b_c\perp\xi_c\); its symmetric
Frobenius norm is \(|b_c||\xi_c|/(\sqrt2 k)\). Every slow/curl/mean/profile
correction has C1 size at most \(h^{1/4}e^{C_\delta\ell}\), and (22) bounds
the actual error. Equation (17) therefore proves (1). Integrating this
central lower bound also shows that the added strain clock of the actual
solution has a lower bound \(c_\delta\ell^{15/8}\), since the base gradient
is \(O_\delta(\ell)\). This is still an observation on a \(q_h\)-particle,
not an identification of that particle with an actual \(Q_h\)-particle.

There is also a new **endpoint**, rather than persistence, core. At
\(t_+=t_f+\delta\), put \(x_+=Y_h(t_+)\) and choose

\[
 R_+=c_F k/|\xi_c(t_+)|\asymp_\delta k/\ell,
 \qquad A_+=\nabla q_h(t_+,x_+)-b_c(t_+)\otimes\xi_c(t_+)/k.
\]

For one sufficiently small fixed \(c_F\), the ball \(B_{R_+}(x_+)\)
lies in the transported bump plateau: the plateau has radius at least
\(c d e^{-C_\delta\ell}\), much larger than \(R_+\).
Slow differentiation gives
\(\|\nabla(b\otimes\xi/k)\|_\infty\le d^{-1}e^{C_\delta\ell}\)
and \(\|D^2S\|_\infty\le h^{-1}e^{C_\delta\ell}\).
Hence the matrix variation on this ball is
\(O(h^{1/4}e^{C_\delta\ell})\), and its phase remains inside the fixed
flat interval. The heat-rounding error, even after the additional inverse
powers of \(k\) from differentiation, is smaller than every fixed power
of \(h\) by (20). Including all corrections and (22) yields

\[
 \sup_{B_{R_+}(x_+)}|\nabla Q_h(t_+,x)-A_+|
       \le h^{1/48}\widehat G_h^+,
 \qquad \log\widehat G_h^+=O(\ell^{15/8}).             \tag{22a}
\]

This radius is smaller than the old \(ck\) by order \(\ell\), with
fixed \(\delta\)-dependent constants. Equation (22a) supplies no higher
actual-Q jets or future persistence on this new ball.

## 7. Why this does not yet reach an order-ell-squared clock

For a small fixed constant \(c_*>0\), the first-stage primary alone reaches
\(m_h\sim c_*\ell^2\) at

\[
 T_*=(3/\mu)\log\ell+(\log c_*)/\mu.
\]

Its further duration is only \((\log\ell)/\mu+O(1)\), shorter
asymptotically than the \(\ell^{1/16}\) duration suggested by holding the
frozen two-shear coefficients fixed. Its primary energy factor would be
\(\exp(Cc_*\ell^2)=h^{-Cc_*}\), which can fit inside a fixed positive
residual margin if \(c_*\) is chosen small enough.

That observation does **not** extend the two-seed theorem to \(T_*\).
The sharp outgoing comparison above uses
\(|t-t_f|\le\delta\), where the full coefficient error has norm
\(C\delta<1\). At \(t-t_f\asymp\log\ell\), this perturbation argument
no longer applies. The supplied receiver and all its evolved covectors
must be bounded on that entire later interval with the changing full
\(V\)-frame and primary coefficient. Its growth cannot be estimated by
reusing the incoming \(z^{-2}\) asymptotic or freezing (10).

The available generic polarization inequality gives only

\[
 \sup\frac{|b||\xi|}{k}
    \le C\ell^{11/8}\exp\!\left(C\int_{t_f}^{T_*}m_hdt\right)
    \le \operatorname{poly}(\ell)h^{-C c_*}.             \tag{23}
\]

Inserting this bound into the **full** nonlinear relative-energy exponent
would give a factor of the form
\(\exp(\operatorname{poly}(\ell)h^{-C c_*})\).
For every fixed \(c_*>0\), it exceeds every inverse power of \(h\), so the
present finite residual \(h^{31/8}\) cannot close that comparison. This is
an exact failure of the available estimate, not a proof that the actual
receiver grows that fast or that the same flow cannot be continued.

The next substantive task is an outgoing **outer** polarization and
whole-envelope estimate on the actual first-stage flow after this new
fixed-time endpoint. It must bound the complete strain history and full
phase/pressure corrections on the interval reaching \(T_*\), or locate a
signed new source with a different useful geometry. The computation here
removes the immediate post-focus gap; it does not turn the remaining
order-\(\ell^2\) estimate into a theorem.

The exact deformation formula in
[the seed-cost calculation, section 4](actual-seed-cost.md)
gives a concrete starting point for that outgoing outer calculation.
For the thin comparison profile and \(\tau=t-t_f>0\),

\[
 f(t)=-s_T g(-\tau),\qquad
 g(-\tau)=\frac92[1-(1-\mu\tau)e^{\mu\tau}]>0.
\]

This is quadratic near zero and comparable to
\((1+\tau)e^{\mu\tau}\) for \(\tau\ge1\). The exact actual-profile
formula uses the linear action shear and bounded periodic Floquet factors;
the next calculation should first establish the corresponding uniform
future lower bound for that fixed profile, then use the full outgoing
outer equations and their stable-to-growing coupling. The outgoing
\(V\sim|z|^{-1}\) branch has a nonzero stable component and is not the
old incoming selected column. Establishing a nonzero final coefficient
and a whole-envelope history remains necessary. This paragraph identifies
a calculation; it does not assert that outgoing outer matching or an
order-\(\ell^2\) interval has been completed.


## Review and exact controls

The independent agent `audit_continuation_and_3d` reviewed sections 1--7
at the restricted fixed-small-delta scope, before the endpoint-core
paragraph (22a) was added. That paragraph is a separate written deduction
awaiting its final independent check. Its review checked the signed-z
coefficient estimates and denominator, the outgoing weighted Volterra
inversion, reconstructed central amplitudes, whole-support strain history,
full-profile correction budgets and the separate H12 continuation. It found
no load-bearing flaw. This is AI-agent review, not external mathematical
acceptance or a full formal certificate.

An exact SymPy calculation independently verified the scalar conjugation
in (7) and the evenness of its potential. Exact rational arithmetic checked
`11/8 + 1/2 = 15/8`, the H12 interpolation exponent `1/48`, and `15/8 < 2`.
These controls check the displayed algebra; the analytic propagation and
continuation estimates are the written argument above.
