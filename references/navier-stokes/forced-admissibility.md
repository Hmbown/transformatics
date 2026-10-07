# Smooth forcing: exact admissibility and an all-order physical budget

Independent agent review: [scope and corrections](../analysis/forced-stage-review.md). These reviews do not certify a complete Navier–Stokes proof.

8 September 2026. Independent analysis of the newly authorized smoothly forced NS lane, alongside the unchanged unforced lane. **Reviewed written analysis; no forced breakdown theorem is claimed.** Ordinary physical viscosity nu>0 remains fixed. This note distinguishes the exact finite approximation residual, its physical scaling, and the additional obligations for one force through a finite accumulation time.

## 1. Official target, including the pressure erratum

Fix nu>0 in three dimensions. **Clay C** requests smooth divergence-free initial data u0 on R3 and smooth f on R3 times [0,infinity), satisfying, for every multiindex alpha and integers m,K>=0,

\[
|\partial_x^\alpha u_0(x)|\le C_{\alpha K}(1+|x|)^{-K},\qquad
|\partial_x^\alpha\partial_t^m f(x,t)|\le C_{\alpha mK}(1+|x|+t)^{-K},
\]

for which no global smooth (u,p) solution has uniformly bounded kinetic energy.

**Clay D** requests smooth divergence-free, unit-periodic u0 and a smooth unit-periodic force with

\[
|\partial_x^\alpha\partial_t^m f(x,t)|\le C_{\alpha mK}(1+t)^{-K},
\]

for which no global smooth periodic (u,p) solution exists. The PDF's erratum explicitly requires periodic pressure. An affine, spatially nonperiodic pressure cannot be used to absorb a prescribed mean force. Neither alternative requires f=0. [Fefferman's official problem, pp. 1-2 and errata p. 6](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).

## 2. Exact scaling of the complete force

Write the rescaled approximation and its chosen pressure as

\[
\partial_\tau U+(U\cdot\nabla_y)U+\nabla_y\Pi-\epsilon\Delta_y U=R,
\qquad \operatorname{div}_y U=0.                    \tag{1}
\]

For a constant velocity factor A and spatial factor s, set

\[
y=sx,\quad \tau=As(t-t_0),\quad u=A U,\quad p=A^2\Pi.
\]

Then the ordinary-viscosity physical equation has exactly the force

\[
f=A^2s R,
\qquad \epsilon=\nu s/A.                          \tag{2}
\]

All advection, pressure, and time derivative terms have the common factor A squared s; the viscous term has factor nu A s squared. Thus the rescaled viscosity is determined by the physical viscosity and this scaling. It cannot be reset independently at each stage.

For the existing packet family s=L=h^(-10), A=L^(7/5)=h^(-14), so

\[
As=h^{-24},\quad \epsilon=\nu h^4,\quad f=h^{-38}R,
\]

and, with r=|alpha|,

\[
\partial_x^\alpha\partial_t^m f
=h^{-38-10r-24m}
 (\partial_y^\alpha\partial_\tau^m R)(As(t-t_0),sx). \tag{3}
\]

This is Eulerian time differentiation. A bound for material derivatives alone does not establish (3)'s right side; the transport term and the derivatives of its velocity must be included.

The current source torus has period 2pi L and the target torus period 2pi. Lebesgue L2 norms are unnormalized. The volume and time Jacobians give

\[
\|\partial_x^\alpha\partial_t^m f\|_{L_x^2}
=h^{-23-10r-24m}\|\partial_y^\alpha\partial_\tau^m R\|_{L_y^2},
\]

\[
\|\partial_x^\alpha\partial_t^m f\|_{L_t^1L_x^2}
=h^{1-10r-24m}\|\partial_y^\alpha\partial_\tau^m R\|_{L_\tau^1L_y^2}. \tag{4}
\]

Passing from the 2pi convention to Clay's unit torus uses one additional fixed NS scaling, with its corresponding velocity and time factors. It changes constants, not h exponents or ordinary nu.

## 3. What the existing finite residual actually proves

The [original nonlinear handover](original-nonlinear-handover.md), equation (24), proves

\[
\|R_h\|_{L_\tau^1L_y^2}\le h^{31/8}E_h,\qquad E_h=e^{C\ell},\quad
\ell=\sqrt{\log(1/h)}.
\]

Equation (4) therefore yields the **small physical force norm**

\[
\boxed{\|f_h\|_{L_t^1L_x^2}\le h^{39/8}E_h=h^{39/8-o(1)}.} \tag{5}
\]

Ignoring the volume or time Jacobian would give the wrong conclusion. The force multiplier alone is not the scaling of this integrated norm.

The same explicit coefficient bounds yield the following coarse *pointwise* orders for the complete residual, with one fixed E_h factor enlarged finitely many times:

| Residual contribution | Pointwise upper bound | h power |
|---|---:|---:|
| Remaining curl and primary/correction products | k^3 d^(-2) E_h | 2 |
| Quadratic mean/correction products | k^4 d^(-3) E_h | 9/4 |
| Primary viscosity | epsilon k^(-1) E_h | 5/2 |
| Oscillatory correction viscosity | epsilon d^(-1) E_h | 11/4 |
| Mean viscosity | epsilon k^2 d^(-3) E_h | 13/4 |

Here k=h^(3/2), d=h^(5/4), and fixed nu is absorbed into constants. These bounds follow from the global pointwise estimates for m,g and their derivatives, not by dividing a global L2 norm by a presumed support volume. In particular the mean pressure tails have not been removed. For example m dot grad m is bounded by (k squared/d)(k squared/d squared), while the leading viscous correction has size epsilon |g|/k squared. Material-curl commutators require only the already priced spatial derivatives in this zeroth-order residual computation.

Thus the current coarse bound is

\[
\|R_h\|_\infty\le C h^2E_h,
\qquad \|f_h\|_\infty\le C h^{-36}E_h.             \tag{6}
\]

**The second upper bound diverges. It neither proves that the actual force diverges nor rules out cancellations.** It simply supplies no uniform C0 control for a proposed accumulating family. Each fixed h still gives a smooth finite force. No smallness assumption on the finite constants in Clay's conditions forbids a large, smooth force.

Nor does (5) imply terminal continuity. For an independent functional counterexample, choose a fixed compact smooth vector bump phi, time bump chi, t_n=1-2^(-n), and

\[
f_n(t,x)=2^n\chi(2^{4n}(t-t_n))\phi(2^n x).
\]

The time supports can be chosen disjoint. The L1_t L2_x norms are O(2^(-9n/2)), hence summable, while the force peaks tend to infinity near (0,1). One may choose phi solenoidal and mean-zero if desired. This is a counterexample to an implication between force norms, not an NS blowup construction.

The existing finite proof establishes many fixed spatial derivatives of its coefficients. It does not establish the required increasing-order Eulerian space-time derivative bounds for its complete physical force. Simply replacing spatial derivative indices by mixed derivative indices is not a proof: time differentiation also hits transport coefficients, pressure reconstruction, activation functions, and the physical scaling factors in (3).

## 4. Pressure and spatial support must be audited for the chosen force

Equation (1) defines one actual force, for its chosen pressure. On the torus, if R=PR+grad psi with periodic psi, the equivalent choice Pi_new=Pi-psi has force PR. Smoothness and periodicity are preserved by this change. The force need not be divergence-free in Clay's conditions, and its spatial mean need not vanish. Periodic pressure does require

\[
\frac{d}{dt}\int u\,dx=\int f\,dx.                \tag{7}
\]

The current mean-zero curl/mean construction satisfies this with zero force mean. A nonperiodic affine pressure is not an admissible way to bypass (7).

For Clay C, periodizing or unwrapping the current torus construction does not create Schwartz data or Schwartz forcing on R3. Leray projection of a compactly supported field can create algebraic spatial tails, so compact support of a curl residual is not by itself compact support of an admissible recovered vector force. One must inspect the complete vector force and all its weighted derivatives, with one pressure choice.

There is no kinematic impossibility here: any compact smooth solenoidal velocity path with a smooth time cutoff and pressure zero defines a compact smooth force by its momentum defect. That generally loses the small-residual cancellations used in the current proof. If compact-support force is claimed while exploiting those cancellations, the pressure/force reconstruction and its bounds must be proved together. Keeping all states and forces in one fixed compact spatial set is a sufficient way to meet the spatial decay part of C, but it is not a property established for the current periodic q and global mean tails.

For any one finite smooth packet path, a smooth continuation followed by a smooth time cutoff can likewise give an admissible periodic force for all future times. The resulting velocity is then a globally smooth forced path, not a counterexample. The new difficulty is preserving force regularity while one velocity actually loses smoothness at one finite time.

## 5. Exact accounting when stages are activated or glued

Let U_old be an already defined solenoidal physical field. Adding a solenoidal w and pressure increment pi changes its complete force by

\[
\delta f=\partial_t w-\nu\Delta w
 +(U_{old}\cdot\nabla)w+(w\cdot\nabla)U_{old}
 +(w\cdot\nabla)w+\nabla\pi.                       \tag{8}
\]

This telescoping increment is what must be budgeted. It is not the isolated NS defect of w: old/new interactions remain.

For a time cutoff chi, replace w by chi w and pi by chi pi. If the uncut increment is (8), the exact new increment is

\[
\delta f_{\chi}=\chi\delta f+(\chi^2-\chi)(w\cdot\nabla)w+\chi' w. \tag{9}
\]

At mixed order (r,m), Leibniz's rule includes all terms chi^(j) partial_t^(m-j) partial_x^alpha(delta f), and corresponding derivatives of the two extra terms. A transition of width delta_t contributes factors delta_t^(-j); the last term includes delta_t^(-m-1) times the velocity. Flatness at an individual endpoint makes that one zero extension smooth, but does not give uniform control as infinitely many transition widths shrink.

The force may create new waves after original time zero in the authorized forced lane. This avoids requiring those waves in the original datum, but it does not erase (9). Inserting a nonzero velocity jump would instead create an impulsive force. The proposed smooth construction must supply the actual activation history and its derivative budget.

Choose times t_n increasing to T<infinity. A possible one-datum setup has increments w_n flat before t_n, so the velocity and force sums are locally finite on every [0,T') with T'<T. The common initial datum is then fixed. The complete f_n must still be the telescoping increments (8), including every older state and the same fixed nu. It is not enough to assemble unrelated finite solutions with different initial data or to reset their rescaled viscosity independently.

## 6. A usable one-sequence, all-orders criterion

The following is a sufficient force-admissibility criterion, independent of the unresolved dynamical construction.

Fix one sequence of actual physical increments f_n on [0,T), with periodic spatial dependence for D, or one common compact spatial support for C. Require:

1. Each fixed f_n is smooth with bounded mixed derivatives of every order on the whole half-open slab; its activation extension is smooth.
2. Choose nondecreasing integers q_n tending to infinity, and one summable positive sequence e_n, before defining the infinite controlled evolution.
3. For every r+m<=q_n, the complete increments satisfy

\[
\sup_{t<T}\|\partial_x^\alpha\partial_t^m f_n(t)\|_\infty
\le C_{r,m}e_n.                                   \tag{10}
\]

Then f=sum f_n is smooth through T, with all mixed derivatives and the same spatial support/periodicity. To prove this, fix derivative order q. The head with q_n<q is finite, and the remaining derivative series converges uniformly by (10). Repeat at q+1: the time derivative of every order-q derivative is uniformly bounded, so these derivatives have uniform terminal limits. The fundamental theorem of calculus identifies those limits as the derivatives of the extension. Repeating for every q proves the claim. The finite-head all-order bound is necessary in this argument; a fixed early term cannot be ignored at the terminal time.

Smooth extension beyond T does not require the force's terminal jet to vanish. Let J_m(x)=partial_t^m f(T,x). For t=T+s, s>=0, use

\[
\widetilde f(T+s,x)=\sum_{m\ge0}\frac{J_m(x)s^m}{m!}\chi(s/\delta_m), \tag{11}
\]

where chi is smooth and equals one near zero. Choose delta_m decreasing to zero, all at most one, so that for m large the mth term is bounded by 2^(-m) in every mixed derivative order <=m-1. This is possible because a time derivative of order b<=m-1 leaves a positive factor delta_m^(m-b), and only finitely many spatial orders are requested at each m. Every fixed-order tail then converges uniformly, and the terminal derivatives are exactly J_m. The construction preserves periodicity or common compact spatial support and is zero for t>=T+1 after choosing the cutoff support accordingly. Together with the preterminal force, it meets rapid time decay. For common compact support it also meets the required space-time decay.

A stronger but simpler special case is a sequence of disjoint time pulses, all flat at their endpoints, whose every fixed mixed derivative supremum tends to zero as their supports approach T. Then the force is flat at T and may be extended by zero. General overlapping or persistent increments require the summability argument above, or another proved convergence mechanism; endpoint flatness of individual activations is insufficient.

## 7. The physical threshold the present hierarchy would have to reach

For a scaled stage n with factors A_n,s_n, the direct sufficient version of (10), taking e_n=2^(-n), is

\[
\|\partial_y^\alpha\partial_\tau^m R_n\|_\infty
\le 2^{-n} A_n^{-(2+m)}s_n^{-(1+r+m)},
\qquad r+m\le q_n,\qquad \epsilon_n=\nu s_n/A_n.   \tag{12}
\]

The residual here includes activation, reset, pressure reconstruction, mean and harmonic terms, and ordinary viscosity. No derivative order may select a different underlying infinite sequence.

For the existing factors, (12) reads

\[
\boxed{\|\partial_y^\alpha\partial_\tau^m R_n\|_\infty
\le 2^{-n}h_n^{38+10r+24m},\qquad r+m\le q_n.}     \tag{13}
\]

A concrete first target is therefore a full zeroth-order residual bound h_n^39 times a controlled subpower factor, including the activation terms, instead of the present h_n^2 upper bound. After fixing all constants, h_n can be chosen so that the extra positive power pays 2^(-n). The next targets are the mixed bounds in (13), not just a stronger integrated L2 estimate.

For illustration only, suppose a proposed higher-order construction proved

\[
\|\partial_y^\alpha\partial_\tau^m R_{n,J}\|_\infty
\le C_{n,r,m,J}h_n^{N_J-\sigma(r,m)}e^{C_{n,J}\ell_n^a},\qquad a<2.
\]

A sufficient finite-order margin would be

\[
N_J>38+10r+24m+\sigma(r,m)\quad(r+m\le q_n).        \tag{14}
\]

If both derivative types cost the carrier factor h^(-3/2), this becomes N_J>38+(23/2)r+(51/2)m. That derivative rule, the availability of such N_J, and its constant control are hypotheses to prove, not consequences of the current two-correction construction. Even a formal additional factor k/d=h^(1/4) per correction cannot be assumed without checking every mean, pressure, and viscous interaction.

An actionable diagonal schedule would first fix q_n, prove a physical bound C_n lambda_n^(-c) through that order for the complete actual stage, and choose lambda_n large enough to pay 2^(-n), all lifetime/support conditions, and all previous-stage dependencies. The entire recursively specified sequence must be fixed before invoking the infinite trajectory. The unresolved load-bearing input is that stage theorem for ordinary NS, including its activation/reset and all-order physical forces.

## 8. Released comparison: what is transferable and what is not

The released [Alpöge–Buckmaster Boussinesq paper](https://cims.nyu.edu/~tristanb/boussinesq.pdf) concerns an inviscid two-dimensional system, with forces in both equations. Its Theorem 7.3, equation (7.24), printed p. 63, bounds the **complete physical** scalar and recovered vector force increments by lambda_n^(-1/2) through mixed order q_n. Activation terms, phase means, remainders, and compact vector-force recovery are included. Theorem 8.2, pp. 67-68, selects one common frequency/derivative schedule for the actual layers before evolution. Lemma 9.3, pp. 71-72, obtains terminal smoothness from a summable derivative tail, an all-order finite head, and next-order control. These are the comparison points for (8)-(14), not an ordinary-viscosity NS theorem.

The transferable target is a complete-force estimate after reconstruction and physical scaling. Our current L1 L2 estimate is useful but answers a different question. An analogue for the new forced NS lane must add the full nu Delta term, maintain one nu, and prove the actual infinite-stage dynamics. No private OpenAI proof or unreleased force estimate has been used.

## 9. What would constitute a forced breakdown result

A successful construction must produce one smooth initial datum and one force satisfying section 1 on the entire future time axis, then a solution on [0,T) that cannot extend smoothly through a finite T. The argument must rule out every global admissible solution with those data, normally by uniqueness on each preterminal smooth interval. For C, the spatial decay and finite-energy comparison class must also be verified. Large peaks along varying finite data, a singular chosen path with a nonsmooth force, or merely a force defined before T does not meet that conclusion.

The extension (11) concerns the force only. It does not continue a velocity through its proposed singular time, and does not need to. Conversely, a smooth force extension without an actual nonextendible velocity proves admissibility but not breakdown.

The useful next bounded calculation is now specific: establish the full mixed physical force bound (13), first at order zero including the new-stage activation and reset, for one actual higher-order ordinary-NS stage. If no such bound is obtained, record the uncancelled term and the available norm, without treating a divergent upper estimate as a lower-bound obstruction. ROOT and the newly authorized smoothly forced breakdown target remain OPEN.

## 10. Evidence and exact checks

The official Clay PDF was read live on 8 September 2026, including its sixth-page erratum. The current web reader failed to reopen the Boussinesq PDF; the stated theorem locations were checked against the complete primary PDF downloaded earlier this same session, SHA-256 `895a628d1783bcb039374686f50b895b5f450f53b8ef8aa173523487a7a4a21b`, and its extracted pages. This is a source audit, not a new verification of that paper's full proof or formalization.

The force scaling, norm Jacobians, pointwise residual exponents, and the cutoff identity were independently derived above. No DNS, canonical edit, external message, or formal PDE certificate was produced.
