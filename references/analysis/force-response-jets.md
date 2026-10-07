# Smooth forcing and finite response jets at the exterior packet

8 September 2026. Restricted written analysis. The result concerns every
**fixed finite order**, with constants allowed to depend on that order.
It does not estimate the complete forced response on the logarithmic
amplification interval and does not remove the force from the external
construction.

The actual reference and packet are those of the
[exterior quasimode note](exterior-quasimode.md), based on
[OpenAI/NavierStokesAndEuler at
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
The domain is its unit torus, the terminal time is one, and viscosity is
one. We retain the symbol \(\nu\) in operator identities.

## 1. The two different kinds of regularity used

Put \(t_0=1-\tau\), fix the source's \(0<h<1/100\), and set
\[
r_0=\sqrt{2X_e\tau},\qquad
\ell=\tau^{1/2+h/8},\qquad
k=\tau^{-1/2-h/4},\qquad k\ell=\tau^{-h/8}.
\tag{1}
\]
All profile choices, including \(X_e\), are fixed before \(\tau\) tends
to zero. Write \(I_\tau=[t_0,t_0+\tau/2]\).

On the fixed exterior tube from the quasimode note, throughout this time
interval the complete reference has the exact form
\[
U=K(r,t)e_\theta,\qquad
\operatorname{curl}U=B(r,t)e_z,\qquad f=0,
\quad B=K_r+K/r.
\tag{2}
\]
In particular, \(K\) and \(B\) have no axial dependence. On any fixed
smaller tube, with spatial scale \(R=r_0\), the heat profile gives
\[
R^m|\nabla_x^m\partial_t^b U|
 \le C_{m,b}\tau^{-1/2-h-b},\qquad
|\partial_r^m\partial_t^b B|
 \le C_{m,b}\tau^{-1-h-b}R^{-m}.
\tag{3}
\]
The derivatives in the first estimate are Cartesian; derivatives of the
cylindrical basis cost \(R^{-1}\) because the tube stays away from its
axis. These bounds hold for every fixed pair \((m,b)\).

The complete physical force extends smoothly through terminal time on
the compact torus. Consequently, for
\[
w=\mathbb P f=f-\nabla\pi_f,\qquad
\Delta\pi_f=\operatorname{div}f,
\tag{4}
\]
every fixed global space/time derivative of \(w\) is uniformly bounded
on a fixed terminal neighborhood. One can obtain this from the bounded
Sobolev action of \(\mathbb P\) and Sobolev embedding. No boundedness of
\(\mathbb P:L^\infty\to L^\infty\) is used. On the tube,
\(w=-\nabla\pi_f\), \(\operatorname{curl}w=0\), and \(\Delta w=0\).

For the higher-order result we also use the following, weaker, **global**
bound on the reference: for every fixed pair of nonnegative integers
\((s,b)\), there are finite constants \(C_{s,b},p_{s,b}\) such that
\[
\sup_{t\in I_\tau}\|\partial_t^b U(t)\|_{H^s(\mathbb T^3)}
 \le C_{s,b}\tau^{-p_{s,b}}.
\tag{5}
\]
No restriction on the growth of \(p_{s,b}\) with derivative order is
imposed. This is the fixed-order consequence of the source's finite-stage
jet bounds and diagonal tail estimates, explained in
[the source extraction, §4](external-modulation-source.md#4-actual-oscillatory-derivative-costs).
More precisely, paper Lemma 9.8 bounds each fixed partial sum by
\(C_{j,m}q^{-K_m}(1+|\log q|)^{P_{j,m}}\), and Proposition 9.9,
Step 1, includes the base and initialization. For each requested order,
take a sufficiently long but fixed prefix in Lemma 5.4's tail estimate
(5.35), charging the additional curl derivative when recovering
velocity. The corresponding formal tail declarations are
[potential_tail_jet_bound and exists_potential_tail_order](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/DiagonalJetBounds.lean#L196).
The tail has a prescribed nonnegative power, and the prefix has a
polynomial bound. The source coordinate obeys \(q\ge1-t\). The heat
exterior has \(r\ge c\sqrt q\ge c\sqrt{1-t}\); the fixed cutoff
region away from the origin has bounded jets by Theorem 3.1(ii).
Absorb logarithmic losses into an additional fixed power, then use
compactness of the torus to obtain (5). This is a derived consequence
of those estimates, not a separately exported global Sobolev theorem.
It uses one prefix for each fixed order, not one prefix uniform over
all orders.

In particular, (5) alone is not the local estimate (3). Substituting
its high-order powers directly into repeated oscillatory integration
could lose more than the oscillation gains. The argument below uses
global estimates only at a fixed low order for each operator word.

## 2. Exact first coupling and its smallness

Use a Hermitian inner product linear in its first argument. With fixed
real smooth bumps, let
\[
\chi=\eta_r((r-r_0)/\ell)\eta_z(z/\ell),\qquad
c_\theta=\sqrt{g(2/X_e)}>0.
\]
The unnormalized solenoidal packet has components
\[
v_r=(\chi+\chi_z/(ik))e^{ikz},\quad
v_\theta=c_\theta\chi e^{ikz},\quad
v_z=-(\chi_r+\chi/r)e^{ikz}/(ik).
\tag{6}
\]
It is compactly supported in the tube. Put
\(\mathcal N_\tau=\|v\|_2\asymp r_0^{1/2}\ell\) and
\(v_\tau=v/\mathcal N_\tau\). All three components, including the curl
correction, are retained. Compact support makes a noninteger \(k\)
compatible with the torus chart.

Work in the full solenoidal space and define
\[
\mathcal A(t)a=\nu\Delta a-
\mathbb P\big((U\cdot\nabla)a+(a\cdot\nabla)U\big).
\tag{7}
\]
The packet is mean zero; the proof does not require a mean-zero assumption
on the force. We do not discard the spatial mean of \(w\) before applying
\(\mathcal A\). For the actual assembly, the
[first-coupling source check](exterior-force-coupling.md#1-a-global-pressure-potential-on-a-source-free-tube)
also gives zero mean of the force.
The direct coupling is exactly zero:
\[
\langle \partial_t^b w(t),v_\tau\rangle
=\langle \partial_t^b f(t),v_\tau\rangle=0.
\tag{8}
\]
Here the packet and its support are fixed once \(\tau\) is chosen.

For curl-free \(w\), the local identity
\[
(U\cdot\nabla)w+(w\cdot\nabla)U
=\nabla(U\cdot w)+(\operatorname{curl}U)\times w
\tag{9}
\]
shows exactly which pressure-mediated term remains. The gradient drops
against the solenoidal test, as does \(\Delta w\). Moreover
\(\int_0^{2\pi}w_\theta\,d\theta=0\), since \(w\) is a gradient of
a single-valued scalar on the tube. Hence
\[
\langle\mathcal A(t)w(t),v_\tau\rangle
=-\frac{2\pi c_\theta}{\mathcal N_\tau}
\int B(r,t)\overline w_r(r,z,t)\chi(r,z)e^{-ikz}r\,dr\,dz,
\quad
\overline w_r=\frac1{2\pi}\int_0^{2\pi}w_r\,d\theta.
\tag{10}
\]

Smoothness at the axis supplies an additional small factor. Angular
Taylor averaging, using global smoothness rather than harmonicity at
the axis, gives
\[
\overline w_r(r,z,t)
=\frac r2(\partial_{x_1}w_1+\partial_{x_2}w_2)(t,0,0,z)+O(r^3)
=-\frac r2\partial_z w_3(t,0,0,z)+O(r^3).
\tag{11}
\]
Every fixed axial or time derivative satisfies the corresponding
estimate. The constant transverse term and all odd angular moments
vanish. In particular, \(|\partial_z^m\partial_t^b\overline w_r|
\le C_{m,b}r_0\) on the packet support. The physical force need not
vanish at the axis at preterminal times.

Integrating (10) by parts \(m\) times in \(z\) now proves
\[
\left|\partial_t^b
 \langle\mathcal A(t)w(t),v_\tau\rangle\right|
\le C_{m,b}\tau^{-1-h-b}r_0^{3/2}\ell(k\ell)^{-m}
\le C_{m,b}\tau^{1/4-7h/8-b+mh/8}.
\tag{12}
\]
There are no boundary terms. Axial derivatives of \(B\) vanish; the
cutoff costs \(\ell^{-m}\). For every fixed \(b\) and every prescribed
\(P>0\), choose a finite \(m\) making the last exponent exceed \(P\).
Thus this coefficient and its fixed time derivatives are
\(O(\tau^P)\), uniformly on \(I_\tau\). No axial reflection symmetry
of the source is assumed, and (10) need not vanish exactly.

## 3. A local elliptic estimate that permits fixed iteration

Here is the step that controls repeated pressure projections without
assuming they preserve support. Let \(D'\Subset D\) be two fixed
domains in scaled Cartesian coordinates, with a positive separation.
Suppose the smooth periodic vector fields \(Q,C\) obey
\(\Delta Q=\nabla\operatorname{div}C\) on \(RD\). For every fixed
integer \(m\ge0\), interior elliptic regularity and Sobolev embedding
give
\[
\|Q(R\cdot)\|_{C^m(D')}
\le C_{m,D,D'}\left(
 \|C(R\cdot)\|_{C^{m+4}(D)}
 +R^{-3/2}\|Q\|_{L^2(\mathbb T^3)}\right).
\tag{13}
\]
A translated coordinate chart works equally well. To see the scaling,
the equation in \(y=x/R\) is exactly
\(\Delta_y Q(Ry)=\nabla_y\operatorname{div}_y C(Ry)\).
The interior \(H^{m+2}\) estimate uses the source through order \(m\),
the low-order \(L^2\) norm, and two derivatives already present on
\(C\); using \(C^{m+4}\) is more than sufficient. On the fixed scaled
domain, \(H^{m+2}\) embeds into \(C^m\). A finite ball cover gives
the estimate on annular cylinders. The domain separation is fixed;
only the constant, not a power of \(R\), depends on \(m\).

For the actual pressure term
\[
Q=\nabla\Delta^{-1}\operatorname{div}C
\]
the global estimate is simply \(\|Q\|_2\le\|C\|_2\). Thus the
nonlocal part in (13) costs one global \(L^2\) bound. It does not
require global \(C^m\) control for arbitrarily large \(m\).

**Fixed-word proposition.** Choose any fixed finite word formed from
operators \(\partial_t^b\mathcal A(t_i)\), with fixed nonnegative
integers \(b\) and times \(t_i\in I_\tau\), applied to
\(\partial_t^a w(t_*)\), with \(t_*\in I_\tau\) and fixed \(a\).
Let its value be \(H_\tau\). Under (3)–(5), for every \(P>0\),
\[
|\langle H_\tau,v_\tau\rangle|\le C_{\mathrm{word},P}\tau^P.
\tag{14}
\]
The constant is uniform over the indicated times. The word and \(P\)
are fixed before \(\tau\) tends to zero.

*Proof.* For a word of length \(j\), choose \(j+1\) nested annular
cylinders of radial and axial width comparable to \(R\), inside the
exact exterior tube. Their separations may depend on \(j\), but not
on derivative order. The packet lies in the smallest cylinder for
sufficiently small \(\tau\), since \(\ell/R\to0\).

Inductively, the field after each prefix satisfies, on its cylinder,
\[
\sup_{0\le q\le m}R^q|\nabla^q H|\le C_{\mathrm{prefix},m}
\tau^{-B_{\mathrm{prefix}}},
\tag{15}
\]
where \(B_{\mathrm{prefix}}\) is independent of \(m\). This is true
initially by the global smoothness of \(w\). For one new factor with
time-derivative order \(b\), let
\[
C=(\partial_t^b U\cdot\nabla)H
 +(H\cdot\nabla)\partial_t^b U.
\]
Its scaled \(C^m\) norm is at most
\(C_m\tau^{-B_{\mathrm{prefix}}-1-h-b}\), for every fixed \(m\),
by (3). The new field is \(-C+Q\), with the additional term
\(\nu\Delta H\) precisely when \(b=0\). The latter costs \(R^{-2}\).

For this fixed prefix, ordinary global Sobolev product estimates,
boundedness of \(\mathbb P\) on Sobolev spaces, and (5) give
\(\|C\|_2\le C\tau^{-G_{\mathrm{prefix},b}}\) for some finite
exponent. Only finitely many global derivatives are needed: applying
a fixed number of second-order operators to a smooth input requires
a finite derivative ceiling depending on the word, not on \(m\).
Apply (13), using this global bound. Its second term costs
\(R^{-3/2}=O(\tau^{-3/4})\). One may therefore choose the next
exponent to be the maximum of
\[
B_{\mathrm{prefix}}+1+h+b,\qquad
G_{\mathrm{prefix},b}+3/4,
\tag{16}
\]
which also covers diffusion when present. This exponent is independent
of \(m\). The induction may use (15) at order \(m+5\), since it was
asserted simultaneously for every fixed order. It does not enlarge
the number of nested domains with \(m\).

Finally integrate the pairing with (6) by parts \(m\) times in \(z\).
Field derivatives cost \(R^{-q}\le C\ell^{-q}\); cutoff derivatives
cost \(\ell^{-q}\). The two curl corrections carry bounded extra
factors \((k\ell)^{-1}\) and \((kr_0)^{-1}\). The support has volume
comparable to \(r_0\ell^2\), so normalization gives
\[
|\langle H_\tau,v_\tau\rangle|
\le C_{\mathrm{word},m}\tau^{-B_{\mathrm{word}}}
r_0^{1/2}\ell(k\ell)^{-m}
\le C_{\mathrm{word},m}
\tau^{-B_{\mathrm{word}}+3/4+h/8+mh/8}.
\tag{17}
\]
Choose \(m\) sufficiently large after fixing the word and \(P\).
This proves (14). ∎

## 4. Actual Taylor coefficients, with their order fixed

For the linear response
\[
z_t=\mathcal A(t)z+w(t),\qquad z(t_0)=0,
\tag{18}
\]
define \(J_n=\partial_t^n z(t_0)\). Smooth preterminal coefficients
and input make these well defined to every fixed order. Differentiating
the equation gives the exact recursion
\[
J_1=w(t_0),\qquad
J_{n+1}=w^{(n)}(t_0)+
\sum_{j=0}^{n-1}\binom nj\mathcal A^{(j)}(t_0)J_{n-j}
\quad(n\ge1).
\tag{19}
\]
For example,
\[
J_2=\mathcal A w+w',\qquad
J_3=\mathcal A^2w+2\mathcal A'w+\mathcal A w'+w''.
\tag{20}
\]
These are noncommuting sums, not powers of a scalar formal expression.
Equations (8) and (14) imply
\[
\forall n\ge1\ \forall P>0:\quad
|\langle J_n,v_\tau\rangle|\le C_{n,P}\tau^P.
\tag{21}
\]
Changing the input to \(-w\), as in the force-removal error equation,
only changes these linear coefficients' sign. Equation (21) concerns
the linear response; it does not include the nonlinear error term.

## 5. Why support cannot simply be propagated through the adjoint

In the full solenoidal space write
\[
\mathcal A^*=\mathbb P\mathcal L^*,\qquad
\mathcal L^*v=\nu\Delta v+(U\cdot\nabla)v-(\nabla U)^Tv.
\tag{22}
\]
For compactly supported solenoidal \(v\), the unprojected
\(\mathcal L^*v\) is supported in the same set. But, putting
\(q=\Delta^{-1}\operatorname{div}(\mathcal L^*v)\),
\(\mathcal A^*v=\mathcal L^*v-\nabla q\) has a global pressure
tail. At the next iteration,
\[
\mathcal L^*\nabla q
=\nabla(\nu\Delta q+U\cdot\nabla q)
-2(\nabla U)^T\nabla q,
\]
and therefore
\[
(\mathcal A^*)^2v
=\mathbb P(\mathcal L^*)^2v
+2\mathbb P\big((\nabla U)^T\nabla q\big).
\tag{23}
\]
The last term is a global interaction, not a gradient identity. Even
locally, divergence-free \(U=(x_2,0,0)\) and harmonic
\(q=(x_1^2-x_2^2)/2\) give
\((\nabla U)^T\nabla q=(0,x_1,0)\), whose curl is nonzero.
This local algebraic check is not a claim that this \(q\) is the
pressure generated by the actual packet. It shows why the term cannot
be discarded merely from harmonicity and incompressibility.

Thus one adjoint step is local modulo a gradient; this observation does
not iterate for free. The elliptic argument in §3 controls the resulting
nonlocal terms at every fixed order, without asserting exact support
preservation or exact cancellation with the actual source.

## 6. The remaining finite-window question

The quasimode's interval has length
\[
\Delta_\tau=O\big(\tau^{1+h}\log(1/\tau)\big)
\ll\tau.
\]
All estimates above are uniform on an interval containing it. This
still does not bound
\[
\left\langle\int_{t_0}^{t_0+\Delta_\tau}
\mathcal S_U(t_0+\Delta_\tau,s)w(s)\,ds,
v_\tau\right\rangle.
\tag{24}
\]
Finite-order coefficient estimates give no uniform control of the
Taylor remainder. The constants in (13)–(21), global derivative orders,
and exponents \(B_{\mathrm{word}}\) may grow with word length. No
analyticity estimate, summable expansion, or order growing with
\(\tau^{-1}\) has been established. Nor has a suitable upper bound on
the actual propagator been supplied. A response estimate for (24) needs
one of these additional mechanisms, with its quantitative costs.

The result is therefore a source-specific obstruction to inferring
excitation from the packet's operator-norm growth: the direct forcing
pairing vanishes, and every fixed response jet has superalgebraically
small pairing. It is neither an excitation lower bound nor a stability
theorem. It leaves unforced continuation and force removal open.

**Review record.** The source-audit agent independently reviewed the
mathematical body at SHA-256
`e6bdf6224e454b38ad1184edb9af49ab692d51b4ae8107511d4c6ca6f49c3980`
and passed the actual-source input, local elliptic induction, fixed-word
quantifiers, time recursion, and adjoint identity. The coordinating agent
separately checked those steps and passed the same bounded claims.
The subsequent mean-zero clarification and cross-reference changed no
formula. Exact scaling arithmetic, local links, mathematical delimiter
balance, and whitespace were checked. These are independent AI-agent
reviews of a written finite-order argument, not a formal PDE certificate,
external expert acceptance, or a bound for (24).
