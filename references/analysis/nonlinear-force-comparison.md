# A nonlinear unforced comparison on a growing local-clock window

8 September 2026. Restricted written proof, independently reviewed at the
scope recorded below. For each sufficiently late restart of the actual forced reference,
this note constructs and continues the unforced solution with exactly the
same restart datum on a specified interval. The velocity error tends to
zero, and its integrated gradient tends to zero, while the reference's
local centrifugal clock tends to infinity. The restart datum still varies
with the remaining time. No single unforced trajectory approaching the
external singularity is constructed.

The reference is the fixed construction in
[OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538),
on its unit torus at viscosity one. The source is its
[paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
SHA-256 `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
The [global strain-cost note](global-strain-cost.md)
supplies the first-derivative starting point. The argument below derives
the additional **fixed spatial** derivatives it needs directly from the
same construction, rather than using the larger combined space/time jet
loss.

## 1. Sharp fixed spatial derivatives of the complete reference

Fix the source's \(0<h<1/100\), and write
\[
t_0=1-\tau,\qquad L=1+\log(1/\tau),\qquad
K=\tau^{-(1+h)/2}.
\tag{1}
\]
There are constants \(C_j\), depending on the fixed construction, such
that for sufficiently small \(\tau\),
\[
\sup_{t_0\le t\le t_0+\tau/2}
\|\nabla^jU(t)\|_\infty
\le C_j K^{j+1}\sqrt L,
\qquad 1\le j\le4.
\tag{2}
\]
There is no assertion of a uniform constant as \(j\) grows. The index
four suffices for the comparison below. Notice also that (2) is not
stated at \(j=0\): the leading base velocity has a different amplitude
normalization, and its supremum does not enter the highest-order energy
coefficient.

Here is the source calculation proving (2). In a physical chart put
\(\varepsilon=Q^h\), \(A=1/2+h\), and
\(k_{\rm src}=\lceil\varepsilon^{-1/2}\rceil\), with \(Q\asymp q\).
The physical carrier scale is
\(K_Q=Q^{-1/2}\varepsilon^{-1/2}\).
The primary wave has amplitude bounded by
\[
C Q^{-A}\sqrt\varepsilon\,S_*^{1/4},
\qquad S_*\asymp(1+|\log q|)^2.
\tag{3}
\]
This uses the actual amplitude bound (7.29), the bounded pulse value
(7.21), and bounded cutoff factors. Equation (7.9) bounds the actual
phase normal by a constant, so \(|\nabla\Phi|\le C Q^{-1/2}\),
without a logarithmic factor. The term in \(\nabla^j\) where all
derivatives fall on the exponential as first phase derivatives is
therefore bounded by
\[
C_j Q^{-A}\sqrt\varepsilon\,S_*^{1/4}K_Q^j
=C_j K_Q^{j+1}S_*^{1/4}.
\tag{4}
\]

All other terms have a strict power margin. The amplitude rules (6.32)
charge at most \(Q^{-1/2}\varepsilon^{-\kappa_s}\) per spatial
coefficient derivative, where \(\kappa_s=10^{-5}<1/2\), times a
polynomial in \(S_*\) at every fixed order. In Lemma 9.8's proof,
before its coarser consolidated estimate, the actual phases satisfy
\[
|\nabla^a\Phi|\le C_a Q^{-a/2}S_*^{P_a},\qquad a\ge1.
\tag{5}
\]
In a term with \(d\) derivatives on the coefficient and \(b\) phase
factors, the remaining derivative orders sum to \(j-d\), so
\(b\le j-d\). Compared with (4), its extra power of \(\varepsilon\)
is at least
\[
\frac{j-b}{2}-d\kappa_s.
\tag{6}
\]
If \(d>0\), this is at least \(d(1/2-\kappa_s)>0\). If \(d=0\)
but a higher phase derivative occurs, then \(b\le j-1\), giving a
gain of at least \(1/2\). Frame derivatives have the same or smaller
cost. Every fixed polynomial logarithm in these terms is absorbed by
that positive power. Smooth shell-edge extensions are included in the
coefficient classes; their flat weights absorb inverse edge factors.
Bounded pointwise overlap of labels introduces no new logarithm into
the leading term (4).

For one fixed complete finite correction state, (9.9) gives the
cumulative remainder \(w-w_0^{\rm tan}\in\mathcal W^{17/25}\).
The same derivative accounting bounds it by
\[
C_{J,j}K_Q^{j+1}Q^{(9/50)h}(1+|\log q|)^{P_{J,j}}.
\tag{7}
\]
The gain \((17/25-1/2)h=(9/50)h\) is independent of the fixed
derivative order. The tangential means in \(\mathcal M^{9/10}\)
have the positive relative margin
\[
h\left(\frac{j+1}{2}-\frac1{10}-j\kappa_s\right)>0
\quad(j\ge1),
\tag{8}
\]
and the radial mean in \(\mathcal M^{19/10}\) has a still larger
margin. All primary curl corrections and later harmonics are included
in these cumulative classes.

The base estimates (5.42), with the normalized tail bounds (5.46),
give \(C_j q^{-(j+1)/2-h}\) for fixed spatial derivatives, including
the smooth Cartesian profiles at the axis. This is no larger than
\(C_j q^{-(j+1)(1+h)/2}\) when \(j\ge1\). In the exact heat
exterior, \(r\ge c\sqrt q\) gives the same estimate directly from
\(K_{\rm swirl}=\kappa r^{-1-2h}H(4(1-t)/r^2)\).

Finally choose one sufficiently long but fixed finite state after
fixing derivative ceiling four. The diagonal estimate (5.35), charging
the curl derivative that recovers velocity, makes the entire remaining
\(C^4\) tail bounded for small \(q\). The finite state already obeys
(4), (7) and (8). The fixed cutoff region away from the origin has
bounded terminal derivatives, and periodization adds no small scale.
Since \(q\ge1-t\ge\tau/2\), these estimates prove (2) for the
complete actual reference. They do not sum the coarse derivative bound
of every separate stage.

The complete force is smooth through terminal time. We may therefore
fix, independently of \(\tau\),
\[
F_*\ge1+\sup_{t\text{ near }1}\|f(t)\|_{H^3(\mathbb T^3)}.
\tag{9}
\]

## 2. Weighted energy for the full nonlinear difference

For each fixed \(\tau\), let \(V\) be the classical local unforced
solution with the single prescribed initial datum
\[
V(t_0)=U(t_0).
\tag{10}
\]
Set \(E=V-U\) on its initial lifespan. Its exact equation is
\[
E_t=\nu\Delta E-
\mathbb P\big((U\cdot\nabla)E+(E\cdot\nabla)U\big)
-\mathbb P((E\cdot\nabla)E)-\mathbb P f,
\quad \operatorname{div}E=0,\quad E(t_0)=0.
\tag{11}
\]
Here \(\nu=1\). The physical pressure difference is recovered, up to
its spatial mean, from
\[
\Delta\Pi=-\operatorname{div}f-
\partial_i\partial_j(U_iE_j+E_iU_j+E_iE_j).
\tag{12}
\]
Thus the pressure and complete quadratic error are retained. The force
is not assumed to be small in a terminal norm; its short duration is
part of the estimate.

With \(K\) fixed by (1) for the entire interval, define
\[
X(t)^2=\sum_{j=0}^3K^{-2j}\|\nabla^jE(t)\|_2^2.
\tag{13}
\]
This is equivalent, with constants independent of \(K\ge1\), to the
Fourier norm \(\|(1-K^{-2}\Delta)^{3/2}E\|_2\). Lattice
Cauchy–Schwarz gives
\[
\|E\|_\infty\le C K^{3/2}X,
\qquad \|\nabla E\|_\infty\le C K^{5/2}X.
\tag{14}
\]
For example the second inequality uses
\(\sum_{n\in\mathbb Z^3}|n|^2(1+|n|^2/K^2)^{-3}\le C K^5\).
The zero Fourier mode is included; no mean subtraction is required.

Differentiate (11) through order three and use the corresponding
weighted energy. Transport of the top derivative by \(U\) cancels,
and pressure drops against each differentiated solenoidal field.
Every remaining linear term has the form
\(\nabla^aU\,\nabla^{j+1-a}E\), with \(1\le a\le j+1\).
By (2), multiplying by \(K^{-j}\) bounds it by
\[
C_j K^{-j}K^{a+1}\sqrt L\,
K^{j+1-a}X=C_j K^2\sqrt L\,X.
\tag{15}
\]
Only derivatives of \(U\) through order four occur.

For the nonlinear term, first estimate each homogeneous derivative order
separately, before introducing its weight. At order zero the energy
pairing with \((E\cdot\nabla)E\) vanishes. At orders one and two,
subtracting the skew top transport leaves products bounded by
\(C_j\|\nabla E\|_\infty\|\nabla^jE\|_2^2\). At order three,
the only additional product to check is
\(\nabla^2E\,\nabla^2E\), paired with \(\nabla^3E\). The periodic
interpolation inequality
\[
\|\nabla^2E\|_4^2
\le C\|\nabla E\|_\infty\|\nabla^3E\|_2
\]
gives the same bound. One direct proof puts \(F=\nabla E\), integrates
\(\int|\nabla F|^4\) by parts on the torus, and obtains
\(\int|\nabla F|^4\le C\|F\|_\infty
\|\nabla F\|_4^2\|\nabla^2F\|_2\); cancel the middle factor
when it is nonzero. Periodicity removes boundary terms. Thus for each
\(1\le j\le3\) the homogeneous transport energy bound has a fixed
constant \(C_j\), with no \(K\) in it. Multiplying these bounds by
\(K^{-2j}\) and summing gives precisely
\(C\|\nabla E\|_\infty X^2\). Equation (14) supplies the resulting
quadratic term \(C K^{5/2}X^2\) in the norm inequality.

Leray projection commutes with derivatives and is an orthogonal
contraction in every weighted Fourier norm. The lattice estimates in
(14), the finite homogeneous norm equivalence, and all the preceding
energy constants are uniform for \(K\ge1\). Consequently,
in the upper-Dini or regularized-norm sense,
\[
D^+X\le A_0K^2\sqrt L\,X+B_0K^{5/2}X^2+F_0,
\qquad X(t_0)=0,
\tag{16}
\]
where fixed constants \(A_0,B_0,F_0>0\) absorb the source and norm
constants, and \(F_0\le C F_*\). No high Sobolev norm of \(U\)
appears in an uncontrolled exponential coefficient.

## 3. A growing clock and a closing nonlinear margin

Choose
\[
\theta=\frac{1+h}{16},\qquad
0<c\le\frac{\theta}{A_0},\qquad
d_\tau=cK^{-2}\sqrt L=c\tau^{1+h}\sqrt L.
\tag{17}
\]
All these choices are fixed before \(\tau\) tends to zero. For
sufficiently small \(\tau\), \(d_\tau\le\tau/2\), so all source
bounds apply. Set \(a=A_0K^2\sqrt L\), \(b=B_0K^{5/2}\). Then
\[
e^{a d_\tau}\le e^\theta\tau^{-\theta},\qquad
bF_0d_\tau^2e^{a d_\tau}
\le C\tau^{3(1+h)/4-\theta}L\longrightarrow0.
\tag{18}
\]
The second expression is the complete quadratic bootstrap cost.

For completeness, comparison with the linear integral equation gives
\[
X(t_0+s)\le F_0s e^{as}
+b\int_0^s e^{a(s-r)}X(t_0+r)^2\,dr.
\]
Under the bootstrap \(X(t_0+r)\le2F_0r e^{ar}\), the second term
is at most
\[
\frac43 bF_0^2s^3e^{2as}.
\]
Its ratio to \(F_0s e^{as}\) is bounded by
\((4/3)bF_0d_\tau^2e^{a d_\tau}\), which is less than one half
for small \(\tau\). Continuity closes the bootstrap and proves
\[
X(t_0+s)\le2F_0s e^{as},\qquad 0\le s\le d_\tau.
\tag{19}
\]
This argument initially applies only up to the unforced solution's
maximal lifespan. It also proves that this lifespan exceeds the desired
endpoint: for fixed \(\tau\), (19) bounds \(\|E\|_{H^3}\le C K^3X\),
and the actual reference has bounded \(H^3\) norm on this compact
preterminal interval. Thus \(V=U+E\) remains bounded in \(H^3\).
The usual local strong-solution continuation theorem then extends it
through any purported earlier endpoint. This is a continuation proof
for the same datum (10), not a sequence of replacement restarts.

Combining (14), (17) and (19) yields the explicit bounds
\[
\boxed{\quad
\sup_{[t_0,t_0+d_\tau]}\|V-U\|_\infty
\le C\tau^{3(1+h)/16}\sqrt L\longrightarrow0,
\quad}
\tag{20}
\]
\[
\sup_{[t_0,t_0+d_\tau]}\|\nabla(V-U)\|_\infty
\le C\tau^{-5(1+h)/16}\sqrt L,
\tag{21}
\]
\[
\boxed{\quad
\int_{t_0}^{t_0+d_\tau}\|\nabla(V-U)(t)\|_\infty\,dt
\le C\tau^{11(1+h)/16}L\longrightarrow0.
\quad}
\tag{22}
\]
The absolute gradient upper bound (21) need not tend to zero. Its ratio
to the exterior reference scale \(\tau^{-1-h}\) is at most
\(C\tau^{11(1+h)/16}\sqrt L\), which does tend to zero.

## 4. What this continuation achieves, and what it does not

The exact heat exterior has local centrifugal scale
\(\gamma=c_\gamma\tau^{-1-h}\). On the interval (17),
\[
\gamma d_\tau=c_\gamma c\sqrt L\longrightarrow\infty.
\tag{23}
\]
The heat-profile coefficients vary by \(o(1)\) relative to their initial
values on this interval because
\(d_\tau/\tau=c\tau^h\sqrt L\to0\). Its symmetric strain at the
chosen exterior circle is bounded below by a fixed positive multiple
of \(\tau^{-1-h}\); in cylindrical coordinates its off-diagonal
entry is \((K_r-K/r)/2=-(1+g)\Omega\). Equations (21)–(22) therefore
also give
\[
\int_{t_0}^{t_0+d_\tau}\|S(V)(t)\|_\infty\,dt
\ge c_1\sqrt L-o(1)\longrightarrow\infty,
\tag{24}
\]
for a fixed \(c_1>0\). Thus a growing local clock is compatible with
an actual unforced comparison and a vanishing error-gradient clock.
The reference speed at its growing core is of order
\(\tau^{-1/2-h}\), so (20) is also a vanishing relative velocity error
there. It does not assert a pointwise relative error wherever \(U\)
vanishes.

Every \(\tau\) selects a different large smooth datum \(U(1-\tau)\).
For each selected datum, one unforced solution covers its whole interval;
as \(\tau\to0\), these are different solutions on shrinking physical
intervals. Their initial norms are not uniformly bounded. Consequently
(23)–(24) are not an infinite strain history of one solution, and this
argument does not establish velocity amplification from bounded data.

The comparison is shorter than the previous linear logarithmic flight
\(O(\tau^{1+h}L)\). On that longer interval, the plain global energy
cost \(e^{C L^{3/2}}\) would defeat the polynomial nonlinear margin in
(18). The localized linear band estimate does not repair that nonlinear
estimate automatically. Nor can the error be reset to zero at the next
interval without changing the datum. Extending the present comparison
to one terminal trajectory requires controlling inherited nonlinear
error and its pressure through subsequent windows, or a different
initial-data selection argument. Those steps remain open.

## 5. A quantitative allowance for an inherited initial error

There is a modest extension that makes one next-window obligation
explicit. Keep \(\tau,K,d_\tau\) fixed as above, and replace (10) by
\(V(t_0)=U(t_0)+E_0\), with a smooth solenoidal \(E_0\). Define
\[
\beta_0=\left(\sum_{j=0}^3K^{-2j}
\|\nabla^jE_0\|_2^2\right)^{1/2}.
\]
For any fixed constant \(C_{\rm in}\), the allowance
\[
\beta_0\le C_{\rm in}d_\tau
\tag{25}
\]
preserves continuation and bounds (20)–(22), with constants now allowed
to depend on \(C_{\rm in}\). This is a separate stability statement;
the original same-datum theorem takes \(E_0=0\).

Indeed the scalar integral inequality now starts with
\((\beta_0+F_0s)e^{as}\). Under the bootstrap
\(X(t_0+s)\le2(\beta_0+F_0s)e^{as}\), its nonlinear integral is at
most \(4b s(\beta_0+F_0s)^2e^{2as}\). Its ratio to the linear upper
bound is at most
\[
4b d_\tau(\beta_0+F_0d_\tau)e^{a d_\tau}
\le C b d_\tau^2e^{a d_\tau}\longrightarrow0.
\tag{26}
\]
The same bootstrap and \(H^3\) continuation argument therefore apply.

Condition (25) has to be verified for the actual inherited difference
at a later restart, in that window's new weighted norm. The present
same-datum upper bound at the first endpoint is only
\(C d_\tau\tau^{-\theta}\), rather than \(C_{\rm in}d_\tau\).
For adjacent windows of the same form, the remaining times and scales
are asymptotically equal because \(d_\tau/\tau\to0\). Thus the
current upper bound does not itself verify (25) for the next window;
an upper bound too large for a sufficient condition is not a lower
bound or an impossibility theorem. In particular, this extension supplies
no infinite concatenation and no license to erase inherited error.

**Review record.** The coordinating agent independently read the complete
argument. A source-audit agent checked §1 against the relevant paper
estimates and passed the sharp spatial derivative hierarchy, including
the Bell/Leibniz margins, cumulative correction classes, base and fixed
tail. A separate analysis agent checked §§2–5 and passed the weighted
Sobolev estimates with constants uniform in \(K\), nonlinear energy,
bootstrap, same-datum continuation, inherited-error allowance and scope.
These independent reads covered body SHA-256
`cc9c7091c443fbdbd211e4adf10f72cc5133bf0a3a781c67dc4737cdc893ffb9`.
Exact rational calculations checked the exponent identities and all
derivative margins through order four; local links, 26 numbered equations,
mathematical delimiter balance and whitespace were also checked. These
algebra checks do not certify the analytic source hierarchy or the PDE
continuation argument. The result remains an independently AI-reviewed
written theorem, not a formal PDE certificate, external expert acceptance,
or one unforced singular trajectory.
