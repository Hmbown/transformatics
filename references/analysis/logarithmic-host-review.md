# Independent audit of the logarithmic future-host extension

8 September 2026. This review audits the proposed passage from the separately
reviewed outgoing central ODE to the full, actual, unforced Navier–Stokes
solution with its existing original datum. It is an analytic AI-agent review,
not external expert acceptance or a formal PDE certificate. ROOT, (E′), and
FORCED-D remain open. No DNS is used.

**Review status: PASS at the restricted finite analytic scope.** The
[complete theorem](../navier-stokes/logarithmic-host.md) was read after
checking its quantitative PDE inputs below, then read again after the
explanatory clarifications in section 7 were incorporated. No load-bearing
gap was found in its finite assembly. Neither this verdict nor the source
proves an infinite cascade.

Reviewed final theorem SHA-256:
7bf3ee6286b4d37529adc346365c625038b5f7cfe18c06271a945d0543534256.

## 1. Scope, fixed choices, and time horizon

The prior inputs inspected are:

- [First-stage finite theorem](../navier-stokes/loglog-handover.md),
  especially sections 3–7.
- [Actual high-order first-stage preparation](original-seed-compatibility-draft.md),
  section 5.
- [Original two-wave nonlinear theorem](../navier-stokes/original-nonlinear-handover.md),
  sections 2–7.
- [Full phase-profile extension](../navier-stokes/localized-profile.md),
  particularly its exact equations (13), (17), and (20)–(23), full phase
  Fourier hierarchy, residual table, and separate continuation argument.
- [Post-focus review](postfocus-review.md),
  including its conditional quantitative margin.

The new central inputs are
[the future covector](future-covector.md) and
[the outgoing polarization](outgoing-outer.md).
Their exact coefficient and weighted pressure arguments received reciprocal
independent reviews before this PDE audit. The present author did not derive
the outgoing polarization proof.

Fix the unscaled sufficiently thin profile, its full cutoff, the actual
initial packets, the real phase profile, all finite derivative orders,
viscosity, and small overlap time \(\delta\), before \(\eta\) and \(h\).
Use

\[
 h=L^{-1/10},\quad k=h^{3/2},\quad d=h^{5/4},\quad
 \epsilon=\nu h^4,\quad \ell=\sqrt{\log(1/h)},
\]
\[
 t_f=(2/\mu)\log\ell-\ell^{-3/4},\quad
 t_\eta=t_f+\frac{\log\ell}{8\mu}+\frac{\log\eta}{\mu},
 \qquad 0<\eta\le1.
\]

For any fixed \(\eta>0\), this is after the required overlap when \(h\)
is small enough. All these times are bounded by the common \(\eta=1\)
horizon of length \(C\log\ell\). Consequently the constants in the
estimates below can be chosen independently of \(\eta\); the sufficiently
small threshold for \(h\) may depend on \(\eta\).

## 2. The first-stage actual NS state extends independently

The primary packet remains transported by the one fixed Euler profile.
Its fixed-order geometric factors are \(e^{C t_\eta}\), hence fixed
powers of \(\ell\). The support width \(h^{1/2}\), its derivatives,
the full global mean, and the harmonic corrections retain their original
powers of \(h\). Increasing the constant multiplying \(\log\ell\) only
enlarges those fixed polynomial factors.

The sharp leading first-stage history remains

\[
 m_h(t)=1+\ell^{-1}e^{\mu t},\qquad
 \int_0^{t_\eta}m_h\,dt
 \le C\log\ell+C\eta\ell^{9/8}=O(\ell^{9/8}).           \tag{1}
\]

The small corrections in the first-stage approximation have positive
powers of \(h\) times fixed powers of \(\ell\), and hence contribute
\(o(1)\) to its gradient history. The original full residual estimate
has order \(h^{11/4}\) times a polynomial in \(\ell\). Relative energy
and the independent H12 bootstrap therefore incur
\(\exp(C\ell^{9/8})=h^{-o(1)}\), rather than the former
\(\exp(C\ell)\). The same positive C1 interpolation margin \(1/24\)
continues to close. This supplies actual strong existence of \(q_h\)
through \(t_\eta\) without using any statement about the second packet.

The fixed high-order construction is separate. Its indices remain
background H128, phase/amplitude order 160, mean H132, and harmonic
amplitude order 129. The approximation retains H128 size

\[
 h^{7/4-128}\operatorname{poly}(\ell).
\]

The actual H128 norm follows from its smooth original datum and the
now established sharp first-stage Lipschitz history (1). Interpolation
with the L2 error gives exactly

\[
 h^{r-1}\|D^r(q_h-U_{1,h})\|_\infty
 \le h^{\,1/4-(r+3/2)/128}\exp(C_r\ell^{9/8})
                  \operatorname{poly}(\ell).          \tag{2}
\]

For \(1\le r\le24\), the smallest exponent is \(13/256>0\).
The leading approximation derivatives have the sharper rate \(m_h\):
its principal wave has bounded primary covector on its transported
support, while every slow derivative substitutes \(h^{1/2}\)-scale
for \(h\)-scale variation and its excess carries a positive power of
\(h\). Thus (2) implies the actual state bound

\[
 \|D^r q_h(t)\|_\infty\le C_r m_h(t)h^{1-r},
 \qquad 1\le r\le24.                                  \tag{3}
\]

Using a generic exponential in place of \(m_h\) in (3), and then
exponentiating it to control the receiver, would not be valid. The
high-order interpolation is what preserves the needed rate.

The fixed-profile background comparison lifetime is much larger than
this \(O(\log\ell)\) interval, for every fixed high derivative order.
No new background datum or future-dependent normalization is required.

## 3. Model comparison and the whole receiving envelope

The original first-stage material-phase argument extends with (1).
Its velocity error \(h^{9/8}\exp(C\ell^{9/8})\), divided by the primary
wavelength \(h\), leaves positive margin \(h^{1/8}\); the primary
tangent velocity does not itself transport its phase. Slow curl and
mean terms remain smaller. Therefore the actual central gradient obeys

\[
 \sup_{[0,t_\eta]}|\nabla q_h(t,Y_h(t))-\overline A(t)|
       \le h^\gamma E_h,\qquad
 E_h=\operatorname{poly}(\ell)\exp(C\ell^{9/8}),         \tag{4}
\]

for some fixed \(\gamma>0\), with \(\log E_h=o(\ell^2)\).

Compare normalized covectors on the unit sphere and their log lengths
separately. Their coefficient integrates to \(C\ell^{9/8}\). The
full amplitude comparison has the same rate, after this direction
comparison and finitely many enlargements of \(C\). Consequently the
errors in the central cotangent and amplitude products are \(h^\gamma
E_h\). No small covector denominator is placed inside a second
exponential.

For each fixed spatial order, work in \(h\)-scaled coordinates moving
with the actual \(q_h\) particle and clock \(\int m_h\). Equation (3)
gives bounded scaled coefficient derivatives. At each derivative level
the unknown highest derivative enters linearly with rate \(C_r m_h\);
products of lower derivatives enlarge \(E_h\) a finite number of times.
This proves the same finite forward/inverse flow, normalized direction,
covector size, and amplitude jet hierarchy as before, with the enlarged
\(E_h\). It does not require a polynomial propagator bound for arbitrary
errors.

The phase and unweighted receiver amplitude are continued from their
existing original preparation. The volume of their transported chart
remains \(O(d^3)\), and its diameter is at most \(dE_h=o(h)\).
The original bump is factored out before comparison: it is allowed to
vanish at its boundary. The mean-value comparison then gives

\[
 \sup_{\mathrm{support}}
 \big||B||\xi|-|B_c||\xi_c|\big|\le(d/h)E_h.
\]

After restoring the receiving normalization and absorbing fixed powers
of \(\ell\),

\[
 \sup_{\mathrm{support}}\frac{|b||\xi|}{k}
 \le C\ell^{7/8}|B_c||\xi_c|+h^{1/4}E_h.              \tag{5}
\]

Thus the sharply proved central history passes to the whole support
with an additive error tending to zero even after time integration.
This is the required argument; a large generic amplitude bound alone
would not establish the whole-envelope history.

## 4. Full pressure, means, phase modes, and residual hierarchy

The exact profile identities need no smallness assumption on the new
time endpoint. Their coefficients are the independently known actual
\(q_h\). The mean and zero-mean profile correction are solved
sequentially, forward from their existing zero initial data:

\[
 Dm+(\nabla q_h)m+\nabla p_m=-Q_0,\qquad \operatorname{div}m=0,
\]

followed by the full forced tangent profile equation with its central
heat clock and exact pressure. The phase mean remains the full stress
divergence, including curl terms. The normal mean-to-primary forcing
is retained. The residual remains exactly the full formula (23) in
the localized-profile source; no newly generated harmonic is deleted.

For the global mean, the weighted derivative-energy coefficients obey

\[
 d^{j-1}\|D^j q_h\|_\infty
 \le C_j m_h(d/h)^{j-1}\le C_jm_h.
\]

This includes the differentiated \(m\cdot\nabla q_h\) terms. The
Leray projection is used in global L2 pairings, with its pressure
retained; no L-infinity bound for the projector or compact support
for the mean is assumed. H16 and uniform Sobolev interpolation give
the required mean derivatives. Only compact oscillatory factors
receive the volume \(d^{3/2}\).

The profile transport has diagonal generator \(G-\kappa n^2\) in each
phase frequency \(n\ne0\). Its dissipative factor is scalar and
commutes with the matrix flow. The central heat clock has no spatial
derivatives, so no new \(n^2\partial_x\kappa\) commutator occurs.
Primary C18, mean H16, profile spatial order 13, and the fixed A80
phase regularity are still sufficient. The differentiated hierarchies
have rate \(C_rm_h\); their finitely many products remain within
\(E_h\).

Consequently the original point and L2 sizes persist:

\[
 |a|\le kE_h,\quad |r_a|\le(k/d)E_h,\quad
 |g|+|m|\le(k^2/d)E_h,\quad |r_g|\le(k^2/d^2)E_h.
\]

All their required slow derivatives have the original \(d^{-r}\)
weights. The complete residual table therefore retains

\[
 \int_0^{t_\eta}\|R_{\mathrm{tot}}\|_2\,dt
                    \le h^{31/8}E_h.                 \tag{6}
\]

The central diffusion mismatch still has its extra \(d/h\) factor
from the actual whole-envelope covector comparison; its original
\(h^{37/8}E_h\) order remains below (6). The enlarged central
attenuation itself is \(O(h\,\ell^{9/4}\log^2\ell)=o(1)\).
Mean tails, full forced pressure, mixed profile interactions, and
viscosity are not omitted in these bounds.

## 5. The small coefficient in the full history survives

The sharp central theorem supplies, for fixed \(0<\eta\le1\),

\[
 \int_0^{t_\eta}\frac{|b_c||\xi_c|}{k}\,dt
      \le C\eta\ell^2+C\ell^{15/8},
\]

with \(C\) independent of \(\eta\). Apply (5), the fixed bound
\(\|(e^{\tau_c\partial_s^2}F)'\|_\infty\le\|F'\|_\infty\),
and the small curl/mean/profile C1 errors \(h^{1/4}E_h\).
Together with (1), this gives

\[
 \int_0^{t_\eta}\|\nabla U_h\|_\infty\,dt
       \le B\eta\ell^2+o(\ell^2),                     \tag{7}
\]

where \(B\) is fixed before \(\eta\). One may bound every coarse
factor by the common \(\eta=1\) horizon, making this independence
explicit. In particular the generic \(E_h\) is multiplied by a
positive power of \(h\); it is never the unweighted history used in
the final nonlinear exponent.

The finite-order approximation and original datum retain H12 order
\(h^{-117/8}E_h\). Equations (6)–(7), relative L2 energy and the
separate H12 continuation bootstrap then give

\[
 \|\nabla(Q_h-U_h)\|_\infty
       \le h^{1/48-C_*\eta-o(1)}.                    \tag{8}
\]

The number \(1/48\) is unchanged because

\[
 (31/8)(19/24)-(117/8)(5/24)=1/48.
\]

The coefficient \(C_*\) is fixed before \(\eta\), from the full
history constant and fixed H12 energy constant. Choosing a fixed
sufficiently small positive \(\eta\) leaves positive margin and
closes strong existence independently of the L2 estimate. This is
a finite family with changing initial data, not an infinite or
singular trajectory.

## 6. Complete theorem-source audit

The final source was checked against the following requirements:

1. The original datum and all its preparation choices; no fresh endpoint
   seed or mean/profile initialization.
2. The actual first-stage H128-to-C24 argument and sharp \(m_h\) rate.
3. Whole-support comparison (5), not an inference from a single central
   trajectory.
4. All phase modes, pressure and noncompact mean terms in (6).
5. The order of choices and \(\eta\)-independent constant in (7).
6. Separate strong continuation and the positive interpolation margin.
7. Finite changing-data scope, with no resulting claim of ROOT,
   FORCED-D, a generated seed, or an infinite cascade.

All seven are present in the inspected source. Its endpoint ball also
passes the finite geometric check: the radius is smaller than the
transported plateau by a positive power of \(h\); the phase Taylor error
and leading-matrix variation vanish; the full future curl correction is
bounded, rather than assumed to vanish as it did exactly at \(t_f\).
Its pressure/mean/profile contributions use their established C1 bounds.
The heat clock rounds the linear profile by an error smaller than every
fixed power of \(h\). The H12 Fourier tail exponent at
\(\beta=9/4\) is \(27/4-C_{12}B\eta-o(1)>0\) after the stated further
reduction of \(\eta_0\).

## 7. Incorporated clarifications and exact checks

Two clarifications were sent to the author and verified in the final source:

1. The first-stage scaled-C24 margin \(13/256\) is displayed, as in (2)
   above. Its positivity explains why the actual high-order rate (3)
   survives the enlarged first-stage history.
2. When adding the nonlinear error to the smaller endpoint-ball errors,
   the proof uses the strict available exponent
   \(1/48-1/192=1/64\), with its vanishing subpower loss. This absorbs
   the sum of all errors into \(h^{1/96}\) for sufficiently small \(h\).
   Merely adding other errors to an already saturated \(h^{1/96}\)
   upper bound would not by itself prove the same unit-constant bound.

The source now also specifies that its small slow-gradient terms are the
wave-lift, mean, and profile corrections. The leading base-flow gradient
is \(O(m_h)\) and is included separately.

Ten independent rational calculations passed: the first-stage C1 margin
\(1/24\), scaled-C24 margin \(13/256\), H12 order \(-117/8\), full
residual order \(31/8\), central mismatch order \(37/8\), final
interpolation margin \(1/48\), strict remaining margin \(1/64\),
first-stage endpoint power \(9/8\), receiving endpoint power \(2\),
and high-frequency tail power \(27/4\). These exact checks confirm
the arithmetic. The PDE inequalities and their hypotheses were reviewed
in the written derivations above; arithmetic checks do not replace them.
