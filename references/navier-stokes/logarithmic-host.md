# Continuing the supplied receiver beyond its focus

8 September 2026. **PROVED at the restricted written analytic scope below.**
The central arguments and the full assembly passed separate AI-agent
derivation reviews, including first-stage high derivatives, whole-support
history, pressure, nonlinear continuation and endpoint errors.
The assembly below concerns the same original datum at
each scale, with fixed physical viscosity. It is not an infinite trajectory,
a new seed, a formal PDE certificate, or external expert acceptance.
ROOT, `(E′)` and FORCED-D remain OPEN. No DNS is used.

## 1. Statement and order of choices

Use the unscaled fixed Gavrilov profile, original receiving branch and fixed
smooth periodic phase profile of the
[original-time theorem](original-nonlinear-handover.md) and
[full-profile extension](localized-profile.md). The latter
profile is odd and equals its argument on one fixed interval about zero.
Keep their full curl datum, including both waves at original time zero:

\[
 Q_h(0)=V_j+Z_{1,h}(0)+Z_{2,h}(0),\qquad
 h=L^{-1/10},\quad \ell=\sqrt{\log(1/h)},
 \quad k=h^{3/2},\quad d=h^{5/4},\quad \epsilon=\nu h^4.
\]

Here \(\nu>0\) is fixed physical viscosity. The rescaled domain is the
torus of side \(2\pi L\); all L2 norms use unnormalized Lebesgue measure.
Choose one sufficiently thin fixed \(j\), with \(f_j(P_j)=1\), before
\(h\to0\). Write its exact positive Floquet exponent as \(\mu\), and set

\[
 t_f={2\over\mu}\log\ell-\ell^{-3/4},\qquad
 L_{\ell,\eta}={\log\ell\over8\mu}+{\log\eta\over\mu},
 \qquad t_\eta=t_f+L_{\ell,\eta}.                    \tag{1}
\]

There is a sufficiently small fixed \(\eta_0>0\), depending on the fixed
profiles, viscosity and finite derivative orders, such that for each fixed
\(0<\eta\le\eta_0\) and sufficiently small \(h\), the conclusions
are:

* The same full unforced solution \(Q_h\) is smooth through \(t_\eta\).
* The original second seed still has C1 size \(O(\ell^{-5/8})\).
* At the base-flow particle \(Y_h(t_\eta)\), its added symmetric strain is
  between \(c\eta\ell^2\) and \(C\eta\ell^2\), and
  \(\int_0^{t_\eta}\|\nabla Q_h\|_\infty dt
      \le B\eta\ell^2+o(\ell^2)\).
* The complete profile approximation \(U_h\), continued without a restart,
  obeys \(\sup_{[0,t_\eta]}\|\nabla(Q_h-U_h)\|_\infty\le h^{1/96}\).

The constants \(c,C,B\) can be fixed independently of \(\eta\in(0,\eta_0]\);
the threshold on \(h\) may depend on \(\eta\). The limit is always taken
with \(\eta\) fixed. The observation point is a particle of the first-stage
solution \(q_h\), not necessarily of \(Q_h\). Neither endpoint strain nor
the long rescaled interval supplies one datum with an infinite sequence of
transfers. Returning to physical variables multiplies gradients by
\(h^{-24}\) and times by \(h^{24}\), as in the original theorem.

## 2. What changes in the first-stage construction

Let \(m_h=1+\ell^{-1}e^{\mu t}\). On the extended interval,

\[
 \sup m_h+\int_0^{t_\eta}m_hdt
       \le C(\log\ell+\eta\ell^{9/8})
       \le C\ell^{9/8}.                              \tag{2}
\]

The first-stage proof uses this clock in its differentiated transport and
energy equations. Its initial powers of \(h\) are unchanged. Applying its
separate high-order continuation argument with (2) retains the C24 estimate

\[
 \|D^r q_h(t)\|_\infty\le C_r m_h(t)h^{1-r},\qquad 1\le r\le24. \tag{3}
\]

For clarity, the scaled first-stage C-r error from H128 interpolation has
power \(1/4-(r+3/2)/128\), at least \(13/256>0\) for \(r\le24\).
This strict margin absorbs the enlarged subpower factor.
The fixed order budget remains background H128, primary phase/amplitude
through 160, mean H132 and harmonic amplitudes through 129. In particular
(3) is obtained from the first-stage error and H128 interpolation, not by
differentiating a final C1 comparison for \(Q_h\). All earlier strictly
positive error powers remain positive: \(\exp(C\ell^{9/8})=h^{-o(1)}\).
The primary pointwise gradient and its sharp clock have order (2); the
generic high-order bound is not inserted into that clock.

In the remaining sections, \(E_h\) denotes a fixed power of \(\ell\) times
\(\exp(C\ell^{9/8})\), with its constants enlarged finitely many times.
All such constants can be chosen uniformly for \(0<\eta\le\eta_0\le1\).
The logarithm of \(E_h\) is \(o(\ell^2)\). The reference-particle phase
drift, gradient error, and model comparison remain \(h^\gamma E_h\) for
some fixed \(\gamma>0\). Unit covector directions and log magnitudes use
Lipschitz coefficient \(C|A|\); this avoids exponentiating small covector
denominators.

## 3. The selected wave and its whole support

The [through-focus calculation](../analysis/longer-host-attempt.md)
and its [separate review](../analysis/postfocus-review.md)
continue the originally selected incoming branch. The
[future covector proof](../analysis/future-covector.md)
uses exact action shear on the fixed profile. The
[outgoing polarization proof](../analysis/outgoing-outer.md)
retains the complete pressure projection and the stable component. For any
fixed small \(\delta>0\), they give, with \(\tau=t-t_f\),

\[
 |\xi_c|\asymp\ell(1+\tau)e^{\mu\tau},\qquad
 |b_c|\asymp {k\ell^{7/8}\over1+\tau},\qquad
 {|\xi_c||b_c|\over k}\asymp\ell^{15/8}e^{\mu\tau},
 \quad \delta\le\tau\le L_{\ell,\eta}.              \tag{4}
\]

The sign-changing growing coordinate cannot supply a lower bound alone.
The full vector stays nonzero: its outgoing stable trace is positive, and
its weighted transfer to the growing coordinate has nonzero thin limit
\(\int_0^\infty(2s-2/3)e^{-2s/3}ds=7/2\). Perturbation to the fixed
profile preserves this coefficient. These are central-model facts; the
following comparisons are needed for their use in the PDE.

First compare that central model with the actual \(q_h\) central particle
through \(t_\eta\). The integrated coefficients are bounded by (2).
Variation of constants for the full polarization and covector systems costs
\(E_h\), so the normalized difference is \(h^\gamma E_h\). The original
terminal normalization at \(t_f\), \(N_h\asymp\ell^{5/2}\), is kept.
No new datum is selected at a later time.

Next compare each label of the transported packet with its central label.
The support diameter is at most \(dE_h=o(h)\). By (3), its gradient
coefficient difference is bounded by \((d/h)m_hE_h\); integrating the
direction, magnitude and amplitude comparison gives \((d/h)E_h\).
Factor out the transported bump before this comparison. The unweighted
initial polarization and phase jets already differ from their central
values by at most \((d/h)E_h\), from the original terminal preparation.
Multiplication by the original amplitude and normalization changes only
fixed powers of \(\ell\). Thus the error in the leading strain product,
uniformly over the entire support, is bounded by \(h^\sigma E_h\) for
some fixed \(\sigma>0\). No lower bound is claimed at the bump boundary.
This yields the sharp whole-support estimate

\[
 \int_0^{t_\eta}\sup_{\operatorname{supp}b}
              {|b(t,x)||\xi(t,x)|\over k}\,dt
       \le B_0\eta\ell^2+C\ell^{15/8}+h^\sigma E_h. \tag{5}
\]

Crucially, the exponential \(E_h\) multiplies the vanishing comparison
error; it does not multiply the leading \(\eta\ell^2\) in (5).
The coefficient \(B_0\) comes from integrating the exponential in (4)
and is independent of \(\eta\). The earlier incoming history and bounded
through-focus interval contribute at most \(C\ell^{15/8}\).

## 4. Complete profile, pressure and residual

Continue exactly equations (11)--(23) of the full-profile extension from
time zero: the spatially constant central heat clock, divergence-free curl
lifts, full Fourier profile correction, and the global solenoidal mean.
Their forcings use actual \(q_h\). No endpoint cutoff, force or frequency
truncation is introduced. The pressure includes its longitudinal forcing
term \(\xi\cdot H\); the mean has global tails.

The central heat time is bounded by

\[
 {\epsilon\over k^2}\int_0^{t_\eta}|\xi_c|^2dt
 \le C_\nu h[\ell^2\log\ell+
             \eta^2\ell^{9/4}(1+\log\ell)^2]=o(1).  \tag{6}
\]

At fixed derivative orders, triangular transport has diagonal rate
\(C_r m_h\). Lower-order products enlarge \(E_h\) finitely many times.
Retain q C24, primary b and xi C18, mean H16, correction spatial order 13,
and the fixed profile A80 Fourier norm. The same bounds now hold through
\(t_\eta\):

\[
 |D^r b|\le k d^{-r}E_h,\quad |D^r\xi|\le h^{-r}E_h,
\]
\[
 \|D^r m\|_2+\|D^r g\|_{L^2_x A_M}\le k^2d^{1/2-r}E_h,
 \quad
 \|D^r m\|_\infty+\|D^r g\|_{L^\infty_x A_M}
                       \le k^2d^{-1-r}E_h.           \tag{7}
\]

For the mean, scaled coefficient products are
\(d^{r-1}\|D^r q_h\|_\infty\le C_r m_h(d/h)^{r-1}\).
Global solenoidal energy and Sobolev interpolation give (7) without an
L-infinity bound for the Leray projection. Only compact wave factors
receive the volume \(O(d^3)\); the q transport preserves their volume.

The exact residual formula (23) of the source and its listed powers are
therefore unchanged. In particular,

\[
 \int_0^{t_\eta}\|R_h\|_2dt\le h^{31/8}E_h,
 \qquad
 \|Q_h(0)\|_{H^{12}}+\sup\|U_h\|_{H^{12}}
                           \le h^{-117/8}E_h.       \tag{8}
\]

The central/actual diffusivity mismatch has order \(h^{37/8}E_h\).
Mean-to-correction fast advection and normal curl terms remain in the
residual. The slow wave-lift, mean and profile-correction gradients are bounded by
\(h^{1/4}E_h\). Combining (2), (5), and the fixed heat-profile derivative
norm gives

\[
 I_h:=\int_0^{t_\eta}\|\nabla U_h\|_\infty dt
          \le B\eta\ell^2+o(\ell^2),                \tag{9}
\]

where \(B\) is independent of \(\eta\). Equations (7)--(8) alone would
not justify (9); the sharp whole-support argument in section 3 is essential.

## 5. Spending a small fixed part of the nonlinear error budget

On the strong lifetime let \(e=Q_h-U_h\), with \(e(0)=0\). Relative energy
gives \(\|e\|_2\le h^{31/8}E_he^{I_h}\). Separately bootstrap
\(\|\nabla e\|_\infty\le1\). The integer H12 NS energy inequality and
(9) then give

\[
 \|Q_h\|_{H^{12}}+\|U_h\|_{H^{12}}
       \le h^{-117/8}E_h\exp(C_{12}I_h+C_{12}t_\eta).
\]

Uniform expanding-torus interpolation has gradient powers 19/24 and 5/24.
The original positive power and the new loss are

\[
 {31\over8}{19\over24}-{117\over8}{5\over24}={1\over48},
 \qquad
 \|\nabla e\|_\infty\le h^{1/48-C_*\eta-o(1)},       \tag{10}
\]

where one may choose \(C_*>B(19+5C_{12})/24\). One way to justify the
gradient interpolation is to split Fourier space at \(R\ge1\): the low
part is at most \(CR^{5/2}\|e\|_2\), the high part at most
\(CR^{-19/2}\|e\|_{H^{12}}\), and optimization gives the stated powers.
This does not invoke the false endpoint embedding H5/2 into W1,infinity.
The inhomogeneous interpolation also has a harmless \(C\|e\|_2\) term.
Choose \(\eta_0\)
so that \(C_*\eta_0<1/192\); then for sufficiently small \(h\), (10)
improves the bootstrap to \(h^{1/96}\). In fact the available exponent is
strictly greater than \(1/64-o(1)\); this reserves room to absorb fixed
constants and the additional endpoint errors below. The finite H12 bound and the
strong continuation alternative rule out an earlier terminal time.
This supplies strong lifetime, not merely a relative L2 comparison.

The same estimate adds only \(O(t_\eta h^{1/96})\) to (9) for actual
\(Q_h\). At the center, the symmetric norm of the transverse rank-one
matrix \(-b_c\otimes\xi_c/k\) is \(|b_c||\xi_c|/(\sqrt2 k)\).
The background gradient is \(O(\eta\ell^{9/8}+1)\), smaller than
\(\eta\ell^2\). Heat rounding, slow jets, correction gradients and (10)
give the stated endpoint strain bounds for both \(Q_h-q_h\) and \(Q_h\).

## 6. Endpoint core and remaining frequency exclusion

The phase is zero on the central q particle. Define

\[
 A_\eta=\nabla q_h(t_\eta,Y_h(t_\eta))
                     -b_c(t_\eta)\otimes\xi_c(t_\eta)/k,
 \qquad R_\eta=c_F k/|\xi_c(t_\eta)|.
\]

For fixed \(\eta\),
\(R_\eta\asymp k/[\eta\ell^{9/8}(1+L_{\ell,\eta})]\).
The transported bump plateau contains a ball of radius \(cd/E_h\),
and \(R_\eta/(d/E_h)\to0\). Taylor's formula gives phase variation
at most \(c_F+C R_\eta^2h^{-1}E_h/k\). The second term vanishes, so the
ball remains in a fixed smaller linear part of the phase profile.
The leading matrix varies by at most \(R_\eta d^{-1}E_h=h^{1/4-o(1)}\).
The base gradient varies by at most \(R_\eta h^{-1}m_hE_h\), also vanishing
with a larger positive power than (10). The clock (6) makes heat rounding
smaller than every fixed power of h on this interval. Consequently

\[
 \sup_{|x-Y_h(t_\eta)|\le R_\eta}
                 |\nabla Q_h(t_\eta,x)-A_\eta|\le h^{1/96}. \tag{11}
\]

This is a new endpoint ball, with a smaller radius; it asserts neither
persistence of the old radius-ck ball nor higher actual-Q jets for a
descendant's full lifetime.

The independent H12 bound also controls every generated Fourier mode:

\[
 \|\nabla P_{>h^{-\beta}}Q_h\|_\infty
       \le h^{(19/2)\beta-117/8-C_{12}B\eta-o(1)}.    \tag{12}
\]

Reduce \(\eta_0\) further if needed so \(C_{12}B\eta_0<1\). At
\(\beta=9/4\), the exponent is \(27/4-C_{12}B\eta-o(1)>0\).
Thus the proposed dominant strain at scale \(h^{9/4}\) remains excluded
through this longer interval. This is a rescaled estimate, not absolute
smallness after the physical gradient multiplier \(h^{-24}\).

## 7. What this adds, and what it cannot supply

The extension follows the same supplied receiver while its velocity
amplitude has size comparable to \((1+\tau)^{-1}\) times its fixed
normalization, its covector grows in the stated scale, and its
strain reaches a small fixed multiple of \(\log(1/h)\). The adjustable
coefficient allows the existing nonlinear comparison to survive that
larger clock. This is a finite varying-data construction.
The two-sided amplitude estimate does not assert pointwise monotonicity.

The original receiver still has the previously proved C3 preparation cost.
There is no new independent phase, no uniform infinite-depth control and
no one-datum cascade. A next argument must identify an actual generated
or inherited component, with its signed full pressure-corrected source,
and follow its coupling on the complete time-dependent Q_h state. A
fresh externally supplied wave would be another finite-data construction.
The separate smoothly forced target still requires a full physical force
smooth through the prospective terminal time.

## 8. Independent checks

The [full PDE review](../analysis/logarithmic-host-review.md)
rederived the first-stage C24 margin, original-data compatibility, sharp
whole-support clock, fixed-order mean/profile hierarchy and full residual.
The [error and endpoint review](../analysis/logarithmic-error-review.md)
independently checked the uniform Fourier interpolation, H12 continuation,
small-coefficient loss, shrinking endpoint ball, physical conversion and
all-mode frequency exclusion. Both passed at this finite scope.

The [exact controls](../analysis/checks/check-postfocus.py)
check the thin pressure generator and both eigenvectors, action shear,
stable forcing integral with omission controls, signed inner scalar
conjugation, and the rational scale and interpolation powers. They are
algebra checks, not a proof of the analytic PDE estimates. The source and
review hashes are recorded in the
[review index](next-transfer-review.md).
