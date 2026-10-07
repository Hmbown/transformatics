# Velocity gain, force control, and ordinary diffusion: an architecture audit

8 September 2026. Independent bounded analysis of the forced-stage proposal.
These are exact normalization identities, a principal-system control bound,
and a full-equation relative-energy estimate. They are **not** a completed
viscous insertion theorem or a Navier–Stokes breakdown result. ROOT and
FORCED-D remain OPEN. No DNS was run.

The [force contract](../navier-stokes/forced-admissibility.md),
[viscosity calculation](../navier-stokes/forced-viscosity.md), and
[reset bounds](forced-reset.md) govern the target. The question
here is whether higher frequency or large vorticity alone supplies the
missing **velocity** gain with a small complete physical force.

## 1. Recover physical velocity before measuring the gain

The released [Alpöge–Buckmaster Euler manuscript](https://cims.nyu.edu/~tristanb/euler.pdf),
printed pp. 3 and 7, equations (2.3) and (3.2)–(3.4), uses

\[
y=(z,r^2/2),\quad s=Np\cdot A(y,t),\quad
\zeta=\nabla_y(p\cdot A),\quad
\kappa=\zeta_2^2+r^{-2}\zeta_1^2,
\]
\[
\gamma=T F(s),\qquad \psi=B P(s),\qquad P'=F,\qquad
\Omega=N^2\kappa B,\quad \widehat\Omega=\sigma\Omega/N.
\tag{1}
\]

Suppress envelope and slow derivatives **only in this principal identity**.
The physical velocity coefficient multiplying the same profile \(F\) is

\[
a=\left(-NB\zeta_2,\; NB\zeta_1/r,\;T/r\right),
\qquad
|a|^2=\frac{|T|^2}{r^2}+\frac{|\Omega|^2}{N^2\kappa}
=\frac{|T|^2}{r^2}+\frac{|\widehat\Omega|^2}{\sigma^2\kappa}.
\tag{2}
\]

The physical phase frequency is

\[
K=N\sqrt{\zeta_1^2+r^2\zeta_2^2}=Nr\sqrt\kappa.
\tag{3}
\]

Thus recovery of a fundamental harmonic from a **fixed raw azimuthal
vorticity coefficient** \(r\Omega\) loses exactly \(1/K\). For harmonic
\(n\), the raw vorticity coefficient also carries \(|n|\), and its
recovery factor is \(1/(|n|K)\). There is no additional \(1/N\)
loss when the normalized coefficient \(\widehat\Omega\) is held fixed:
that coefficient already contains the inverse frequency. Applying both
losses would double-count the elliptic recovery. Conversely, increasing
\(\Omega\) like \(N\) at fixed \(\widehat\Omega\) does not increase
the recovered velocity at fixed geometry. All higher velocity derivatives
still pay their physical factors \(K^p\).

This calculation also identifies the correct amplitude norm. A gain of
\(|(T,\widehat\Omega)|\) is not automatically the same gain of velocity
if \(r,\kappa,\sigma\) change. Set

\[
H(t)=\operatorname{diag}\left(r^{-1},(\sigma\sqrt\kappa)^{-1}\right),
\qquad A_v=H(T,\widehat\Omega)^T.
\tag{4}
\]

Then \(|A_v|=|a|\). Endpoint factors in \(H\) must be retained in a
return estimate. On a fixed annulus and a fixed nondegenerate covector
history they are finite known constants, but not constants uniform over
an unproved infinite sequence approaching the axis.

## 2. Frequency does not increase this fixed-host growth rate

For a supplied older state the inviscid principal matrix is

\[
\mathcal B(t)=
\begin{pmatrix}0&-d/(\sigma\kappa)\\ \sigma c\zeta_1&0\end{pmatrix}.
\tag{5}
\]

On an interval with frozen coefficients and positive off-diagonal product,
its growing eigenvalue obeys

\[
\gamma^2=-dc\zeta_1/\kappa.
\tag{6}
\]

Neither \(N\) nor the normalization \(\sigma\) appears in (6).
The ordinary-viscosity principal system for harmonic \(n\ne0\) is instead

\[
R_n'=(\mathcal B-\nu n^2N^2q I)R_n+g_n,
\qquad q=\zeta_1^2+r^2\zeta_2^2=r^2\kappa.
\tag{7}
\]

Here \(g_n\) is the normalized principal control. This is the reviewed
fixed-older-state system, including its full \(n^2\) heat factor. It does
not retain lower-order drift, variable-metric remainders, slow derivatives,
pressure recovery or the change to the older field.

Transforming (7) by (4), define

\[
\mathcal C=H\mathcal B H^{-1}+H'H^{-1},\quad
\mu(t)=\lambda_{\max}\big((\mathcal C+\mathcal C^T)/2\big),\quad
h_n=Hg_n.
\]

Direct differentiation of the Euclidean norm gives the exact control bound

\[
|A_{v,n}(t)|\le e^{\int_s^t(\mu-\nu n^2N^2q)}|A_{v,n}(s)|
+\int_s^t e^{\int_\tau^t(\mu-\nu n^2N^2q)}|h_n(\tau)|\,d\tau.
\tag{8}
\]

No unproved lower bound on the force is used. For frozen \(r,\kappa\),
the off-diagonal entries of \(H\mathcal B H^{-1}\) are
\(-d/(r\sqrt\kappa)\) and \(rc\zeta_1/\sqrt\kappa\), so
\(\mu=|rc\zeta_1-d/r|/(2\sqrt\kappa)\). This logarithmic-norm bound
retains possible nonnormal transient growth; merely comparing eigenvalues
would not do so. For a changing history the \(H'H^{-1}\) term is required.

Suppose \(q\ge q_*>0\), \(\mu\le\mu_*\), and
\(\delta=\nu n^2N^2q_*-\mu_*>0\) on a stage of length \(\Delta\).
For zero incoming wave, (8) becomes

\[
\boxed{|A_{v,n}(t_1)|\le
\frac{1-e^{-\delta\Delta}}{\delta}\sup|h_n|.}
\tag{9}
\]

This is a genuine high-frequency obstruction **for a fixed supplied
principal host**: arbitrary correction depth cannot change the sign of
its leading physical dissipation exponent. A higher-order construction
could change the older state or the leading system, but would then need
a new estimate. A covector contracting with \(N\) can also evade the
assumption \(q_*>0\); in that case its actual physical frequency and
integrated heat clock must replace the nominal parameter \(N\).

## 3. What a small-force control bound does and does not prove

In a frozen single-mode system, suppose the *actual normalized principal
control* has a demonstrated estimate
\(|h_n|\le C_p\eta K^{-p}\). For a spatially pure Fourier force this
follows by integrating by parts \(p\) times in its wave direction from
an actual physical \(C^p\) bound \(\eta\), with the fixed coordinate
and projection constants included. The curl in the reduced-vorticity
source is canceled at principal order by the normalization \(\sigma/N\),
not charged as an extra uncontrolled frequency. For a transported,
localized wave this control estimate requires a separate complete-force
reconstruction; it is not a consequence of the leading amplitude alone.

Under precisely that input, (9) yields

\[
|A_{v,n}(t_1)|\le
C_p\eta K^{-p}\min(\Delta,\delta^{-1}).                 \tag{10}
\]

For an unstable constant scalar branch with
\(\lambda=\gamma-\nu n^2N^2q>0\), zero initial amplitude and a control
\(|h|\le\eta_p\), the exact corresponding formula is

\[
|a(t_1)|\le\eta_p\frac{e^{\lambda\Delta}-1}{\lambda}. \tag{11}
\]

The upper bound is attained by constant aligned control in the scalar
system; smooth ramps can approach it. Thus the **principal algebra alone**
does have nonempty gain regimes: choose a supplied host with
\(\gamma>\nu n^2N^2q\), then allow enough positive gain time. This does
not construct that host, bound its own force, keep its coefficient history
under feedback, or meet the complete stage's terminal jet conditions.
It would be incorrect either to assert that all such regimes are empty
or to promote (11)'s regime to a forced NS stage theorem.

If the older stage has velocity scale \(U\), length \(r\), and a proved
bound \(\mu_*\le C U/r\), then overcoming damping with physical child
frequency \(K\) requires, at this level,

\[
\mathrm{Re}_{\mathrm{old}}=Ur/\nu\gtrsim (Kr)^2.       \tag{12}
\]

This requirement concerns the same supplied host and the same child
frequency. One cannot hold its growth rate fixed, take frequency to
infinity to improve remainder estimates, and retain velocity gain.
Time shortening prevents large damping but shortens the same growth
integral. It does not remove their ratio in this bounded-rate case.

## 4. A full NS energy estimate with an actual frequency diagnostic

The following is not restricted to the principal system. On one fixed
torus let smooth \(U\) and \(U+w\) obey NS at the same \(\nu\), with
force difference \(\delta f\). Both fields are solenoidal and pressures
periodic. Put

\[
E=\|w\|_2,\quad
\kappa_w^2=\|\nabla w\|_2^2/\|w\|_2^2\quad(E>0),\quad
\sigma_U(t)=\sup_x\lambda_{\max}(-S_U(x,t)).
\]

Pairing the exact difference equation with \(w\) cancels older
transport, self-advection and pressure, and gives

\[
\frac12(E^2)' +\nu\|\nabla w\|_2^2
=-\int w^TS_Uw+\int\delta f\cdot w.
\]
Consequently
\[
E'\le(\sigma_U-\nu\kappa_w^2)E+\|\delta f\|_2.        \tag{13}
\]

The integrated form of (8) therefore holds with \(E,\sigma_U,
\kappa_w^2,\|\delta f\|_2\). Zeroes of \(E\) are handled by the usual
regularized norm or by integrating over components of \(\{E>0\}\).
The term \(\kappa_w\) is computed from the actual whole perturbation;
an initial carrier frequency does not give a lower bound for it later.
In particular generated means and low modes cannot be discarded to
manufacture a spectral gap. Equation (13) applies to the full nonlinear
difference, but does not itself give a continuation or cascade theorem.

An \(L^2\) gain bound also does not by itself bound pointwise velocity
under concentration. If an output of magnitude at least \(a\) occupies
volume at least \(v\), then and only with such a volume lower bound
\(E_{\rm out}\ge a\sqrt v\). A shrinking volume can accommodate growing
pointwise velocity with decreasing energy. This is why (13) cannot be
turned into an all-architecture exclusion using the energy budget alone.

## 5. The current finite handover spends local Reynolds number

For the present handover family, use the physical factors
\(A=h^{-14}\), \(s=h^{-10}\), \(k=h^{3/2}\). On the first host's
rescaled unit region, the velocity and length scales are \(A\) and
\(s^{-1}\), hence

\[
\mathrm{Re}_0=A/(\nu s)=\nu^{-1}h^{-4}.
\]

The added outgoing wave has strain scale
\(As\,g\), \(g\asymp\ell^{11/8}\), and central wavelength scale
\(r_1=k/s\). Its velocity scale is \(a_1=Akg\). Thus

\[
\frac{a_1}{A}=kg=h^{3/2}\ell^{11/8}\longrightarrow0,
\qquad
\mathrm{Re}_1=\frac{a_1r_1}{\nu}
=\frac{Asg\,r_1^2}{\nu}
=\nu^{-1}h^{-1}\ell^{11/8},
\]
\[
\frac{\mathrm{Re}_1}{\mathrm{Re}_0}
=k^2g=h^3\ell^{11/8}\longrightarrow0.                 \tag{14}
\]

These are the scale estimates for the added wave and its affine-core
strain, not a claim that the complete velocity on that ball equals this
increment or that the outgoing region persists. The total older
transport remains in the actual flow. Each fixed finite stage still has
\(\mathrm{Re}_1\to\infty\) as \(h\to0\), so (14) does not exclude
that reviewed stage. It does show that its strain gain has not supplied
a daughter velocity larger than its parent host, or an improved local
strain-to-diffusion ratio.

More generally, a *hypothetical* repeated architecture with daughter
radius \(k_jr_j\) and strain factor \(g_j\) would have
\(a_{j+1}/a_j=k_jg_j\) and
\(\mathrm{Re}_{j+1}/\mathrm{Re}_j=k_j^2g_j\).
Increasing daughter velocity requires \(g_j>k_j^{-1}\);
not decreasing this local Reynolds number requires \(g_j\ge k_j^{-2}\).
The current logarithmic \(g\) meets neither as \(k\to0\).
This is bookkeeping for that specified repeated geometry, not an
infinite-flow recurrence proved for the current solution and not an
obstruction to a different amplified, inherited or generated structure.

## 6. Decision and evidence

The finite-stage proposal must measure its selected output using (2),
include the actual host/covector diffusion margin (8), and produce the
complete force that yields its control input. Existing finite unforced
handover estimates do not meet the increasing-velocity requirement by
being renamed as forced stages. The fixed-host principal calculation
does not let arbitrarily high frequency discharge all these obligations.
Its finite algebraic gain regimes are nonempty, but no full physical
forced-stage force/gain regime has been established by this audit.

The source formulas were checked against the already retrieved full
primary Euler PDF, SHA-256
`97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8`.
The web reader failed to reopen its URL during this audit; no new version
claim is made. The velocity normalization, physical weight transformation,
scalar control integral and physical powers in (14) were checked by exact
algebra. These checks do not validate omitted PDE terms, an infinite
schedule, or any full formal certificate.

## 7. Review and algebra checks

The coordinating agent independently read and accepted the physical
normalization (2)–(4), the logarithmic-norm control bound (8)–(10), and
the full nonlinear relative-energy estimate (13), at their stated scopes.
An exact symbolic check verified the meridional velocity norm, the matrix
\(H\mathcal B H^{-1}\), both physical Reynolds ratios in (14), and the
integral \(\int_0^\Delta e^{-\delta(\Delta-s)}ds\) in (9). All passed.
This is AI-agent review and symbolic algebra, not external expert review
or formal verification of a PDE theorem.

As a separate prerequisite check for the
[later-flow note](later-flow-attempt.md), the earlier finite
construction does supply a **global** endpoint bound
\(\|\nabla Q_h(t_f)\|_\infty\le C_F\ell^{11/8}\), without a
multiplicative \(G_h\). Here is the complete estimate chain:

- The [original handover](../navier-stokes/original-nonlinear-handover.md),
  (7), bounds the entire base gradient by \(C m_h(t)\).
  Since \(t_f=(2/\mu)\log\ell-\ell^{-3/4}\),
  \(m_h(t)\le1+\ell\) throughout the existing interval.
- Its (E5), repeated as (3) in the
  [localized-profile extension](../navier-stokes/localized-profile.md),
  bounds \(\sup_{t,\mathrm{support}}|b||\xi|/k\) by
  \(C\ell^{11/8}\). The fixed-profile heat semigroup contracts
  \(\|F'\|_\infty\), so this gives the same global leading-gradient
  bound after the compact wave is extended by zero.
- The other primary curl gradients are at most
  \((k/d)E_h+(k/d)^2E_h\). The complete mean and oscillatory corrections
  have global \(C^1\) norm at most \(h^{1/4}E_h\), including the
  noncompact mean tail; see localized-profile (31), (34).
- The actual solution differs by at most \(h^{1/48}G_h\) in gradient,
  by localized-profile (36).

Thus the global bound is
\(C(1+\ell)+C_F\ell^{11/8}+C h^{1/4}E_h+h^{1/48}G_h\).
Both final terms tend to zero because their positive powers of \(h\)
dominate the specified subpower factors. Enlarge one fixed constant and
take sufficiently small \(h\) to obtain the claimed \(P_h\). This
checks that particular input to the later-flow argument; it does not
serve as an independent audit of all its subsequent continuation and
stochastic-representation steps.
