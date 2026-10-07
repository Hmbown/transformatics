# Identifying the generated intermediate band in the full actual flow

8 September 2026. **Reviewed bounded actual-flow calculation.** The
[independent coarse-band review](actual-coarse-band-review.md)
and a separate coordinating-agent read passed. The review pins the
mathematical source before this introductory label changed; no equation
or estimate changed. These are AI-agent reviews, not external expert
acceptance or formal PDE certification.
This note separates the signed postfocus output from the exact background
and linear receiver. It gives a lower bound in the full actual Q, while
also showing that the generated remainder's total strain clock vanishes
on this finite interval. The original data and physical viscosity are
unchanged. No DNS, new donor, infinite iteration, or solution of ROOT or
FORCED-D is claimed.

The inputs are the
[reviewed postfocus remainder calculation](postfocus-normal-source.md),
its [independent review](postfocus-normal-source-review.md),
the [full profile identity](../navier-stokes/localized-profile.md), and
the [actual logarithmic host](../navier-stokes/logarithmic-host.md).

## 1. Observable and conclusion

Keep all parameters and choices of the postfocus note, in particular
\[
 k=h^{3/2},\quad d=h^{5/4},\quad \rho=k/d=h^{1/4},
 \quad\epsilon=\nu h^4,\quad L=h^{-10},
\]
\[
 R_h=dH_h^A,\quad \kappa_h=R_h^{-1},\quad
 \delta_h=H_h^{-M},\quad
 \log H_h=O(\ell^{9/8})+O(\log\ell)=o(\log(1/h)).
\]
All powers, derivative orders, eta and the actual fixed profile are
chosen before h tends to zero. The endpoint t_eta is unchanged, as
is the exact receiving focus t_c=t_f. Put
\[
 W=Q-q,\qquad \mathcal N=W-Z,
\]
where Z is the exact homogeneous viscous linearization about actual q
with the existing original receiver datum z_0.

Let \(\mathcal B_h\) be a real even smooth radial Fourier multiplier,
equal to one on the support of the signed cone test in the postfocus
note and supported in a slightly larger fixed-ratio annulus
\(c\kappa_h\le|K|\le C\kappa_h\).
Its symbol is a fixed smooth function of K/kappa_h; its L1 kernel
bound is uniform on the expanding torus. It is an observation filter,
not a change to the datum.

The exact linear comparison fields satisfy
\[
 \sup_{0\le t\le t_\eta}\|\mathcal B_h q(t)\|_\infty
                      \le h^{23/8}H_h^C,\qquad
 \sup_{0\le t\le t_\eta}\|\mathcal B_h Z(t)\|_\infty
                      \le h^2H_h^C.                  \tag{1}
\]
Consequently the full actual endpoint obeys
\[
 \|\mathcal B_h(r(t_\eta)\cdot Q(t_\eta))\|_\infty
       \ge c\,\eta^{-1}h^{7/4}\ell^{9/8}
                            H_h^{-4A-4M},            \tag{2}
\]
\[
 \|S(\mathcal B_hQ(t_\eta))\|_\infty
       \ge c\,\eta^{-1}h^{1/2}\ell^{9/8}
                            H_h^{-5A-4M}.            \tag{3}
\]

The corresponding full initial band is smaller:
\[
 \|\mathcal B_h Q(0)\|_\infty\le h^2H_h^C,\qquad
 \|\nabla\mathcal B_h Q(0)\|_\infty
                              \le h^{3/4}H_h^C.      \tag{4}
\]
Thus this is actual intermediate-band generation in each member of
the existing family, with an unbounded endpoint-to-initial upper-bound
ratio as h tends to zero. The band is coarser than the already supplied
receiver carrier. It is not production above the finest original scale.

At the same time,
\[
 \sup_{0\le t\le t_\eta}\|\mathcal N(t)\|_{C^1}
                                  \le C h^{1/96},\qquad
 \int_0^{t_\eta}\|\nabla\mathcal N(t)\|_\infty dt
                       \le C h^{1/96}\log\ell=o(1).   \tag{5}
\]
The generated remainder is identifiable, but its own current-window
strain clock is vanishing. Nothing in (5) excludes later amplification
or interaction with the much larger q and Z.

## 2. One complete linear profile correction

Write \(D=\partial_t+q\cdot\nabla\), \(A_q=\nabla q\),
\(\xi=\nabla S\), and let kappa_c(t) be the spatially constant central
phase heat rate from the full-profile construction. This heat rate is
distinct from the observation frequency kappa_h. The primary profile a
has zero phase mean, is tangent to xi, and satisfies
\[
 (D-\kappa_c\partial_s^2)a=G_\xi a,\qquad
 G_\xi=-A_q+2\xi(\xi^TA_q)/|\xi|^2.
\]

For a zero-mean tangent profile v define its exact curl lift
\[
 V_v=-{\xi\times\partial_s^{-1}v\over|\xi|^2},\qquad
 r_v=\operatorname{curl}_xV_v,\qquad
 W_v=v+kr_v.
\]
Evaluation at s=S/k is denoted by E. Then E[W_v] is exactly
solenoidal, with zero spatial mean. The prescribed primary datum is
\(z_0=\mathcal E[W_a](0)\), including the full curl correction.

Use the exact residual R[v;H] in equations (13)--(15) of the
full-profile construction. Define only
\[
 H_{\rm lin}=R[a;0].
\]
This is linear in the zero-mean phase profile a. All its coefficients
are independent of the auxiliary phase, so its phase mean is exactly
zero. Solve
\[
 (D-\kappa_c\partial_s^2)g_{\rm lin}
        =G_\xi g_{\rm lin}-\Pi_\xi H_{\rm lin},
 \quad g_{\rm lin}(0)=0,
\]
\[
 p_g=-k\partial_s^{-1}
       {2\xi\cdot A_q g_{\rm lin}+\xi\cdot H_{\rm lin}\over|\xi|^2}.
                                                        \tag{6}
\]
The longitudinal term xi dot H_lin is required. With the corresponding
primary pressure p_a, the exact evaluated identity is
\[
 (D+A_q-\epsilon\Delta)\mathcal E[W_a+W_{g_{\rm lin}}]
       +\nabla\mathcal E[p_a+p_g]
            =\mathcal E[R[g_{\rm lin};H_{\rm lin}]].
                                                        \tag{7}
\]
The primary residual and the forced term cancel exactly. There is no
quadratic interaction or phase-independent mean equation in this
linear approximation. It must not be confused with the nonlinear
profile correction used to approximate Q.

Set
\[
 Z_{\rm app}=\mathcal E[W_a+W_{g_{\rm lin}}].
\]
Tangency, reality and zero phase mean persist for g_lin, and every
correction vanishes at zero. Hence Z_app(0)=z_0 exactly. The profile
and its potential stay in the transported compact chart. No extra
wave has been supplied.

## 3. Full residual size and exact linear error

The residual identity includes:
\[
 R[g;H]=(\kappa_c-\epsilon|\xi|^2/k^2)\partial_s^2W_g
 +k\left[(D+A_q-\kappa_c\partial_s^2)r_g
       -\nabla_x\partial_s^{-1}
          {2\xi\cdot A_qg+\xi\cdot H\over|\xi|^2}\right]
\]
\[
 \hspace{8mm}
 -\epsilon\Delta_xg-(\epsilon/k)L_1g
 -\epsilon k\Delta_xr_g-\epsilon L_1r_g,\qquad
 L_1v=2(\xi\cdot\nabla_x)v_s+(\operatorname{div}\xi)v_s.
                                                        \tag{8}
\]
The material derivative of the curl is expanded using the exact
commutator with D. The central heat rate has no spatial derivative.
Thus no unestimated time derivative of q or unknown pressure is hidden
in (8).

In the scaled global profile norms used in the existing construction,
the primary has size k H_h^C, its residual H_lin has size
k rho H_h^C, and g_lin has size k rho H_h^C. The last assertion follows
from its forced profile equation, retaining the nonnegative heat
damping of every Fourier mode and spending only the q clock.

Every term in (8) then has size k rho^2 H_h^C. The curl/slow-pressure
terms gain k/d=rho. The slow q coefficients have scale h, so k/h is
smaller than rho. The ordinary viscous ratios
\(\epsilon/k^2,\epsilon/(kd),\epsilon/d^2\) have respective h powers
1, 5/4 and 3/2, all smaller errors. The central-versus-local heat-rate
difference uses the existing whole-envelope covector comparison and
also has a positive extra h power.

No all-order assertion is needed: the available q C24, primary
amplitude and phase orders through 18, and phase Fourier A80 norms
cover two residual expansions and the two integrations by parts
below. Material derivatives in (8) are eliminated by (6) and the
commutator before counting spatial derivatives.
It follows that
\[
 \int_0^{t_\eta}
   \|\mathcal E[R[g_{\rm lin};H_{\rm lin}]]\|_2dt
       \le k\rho^2d^{3/2}H_h^C=h^{31/8}H_h^C.        \tag{9}
\]

The pressure of the exact linear solution Z may have global tails.
Let E_Z=Z-Z_app. Subtracting (7) from its exact equation and pairing
with the global solenoidal E_Z removes the full pressure difference.
Leray is an L2 contraction, and the remaining growth coefficient is
\(\|\nabla q\|_\infty\), not the full Q clock. Thus
\[
 \sup_{0\le t\le t_\eta}\|E_Z(t)\|_2
                  \le h^{31/8}H_h^C.                \tag{10}
\]
This estimates the complete error, including any low-frequency or
global pressure-generated part. It does not assign compact support to
Z, its pressure, or E_Z.

## 4. High regularity of the exact linear solution without a large clock

Use the finite weighted norm
\[
 \mathcal H_{k,12}(Z)=
       \sum_{j=0}^{12}k^j\|D^jZ\|_2.
\]
The sharp actual-q estimates give
\(\|D^rq\|_\infty\le C_rm_hh^{1-r}\) through r=13.
In a differentiated transport term, a q derivative of order j>=1
has weighted coefficient at most
\[
 m_h(k/h)^{j-1}.
\]
In a differentiated stretching term its coefficient is at most
\(m_h(k/h)^j\). Both are bounded by m_h because k/h=h^(1/2)<1.
The top undifferentiated transport cancels, pressure pairs to zero,
and diffusion is nonpositive at every derivative order. Therefore
\[
 {d\over dt}\mathcal H_{k,12}(Z)
       \le C m_h\,\mathcal H_{k,12}(Z).
\]
The full original curl datum has weighted norm at most
k d^(3/2)H_h^C=h^(27/8)H_h^C. It follows that
\[
 \|Z\|_{H^{12}}+\|Z_{\rm app}\|_{H^{12}}
                      \le h^{-117/8}H_h^C.          \tag{11}
\]
The second term also follows directly from the fixed profile jets.
All constants are uniform on the expanding torus; no unnormalized
volume is inserted into a pointwise coefficient.

Apply the previously proved uniform Fourier-split interpolation to
E_Z, using (10),(11):
\[
 \|\nabla E_Z\|_\infty
   \le C\|E_Z\|_2^{19/24}\|E_Z\|_{H^{12}}^{5/24}
                       \le h^{1/48}H_h^C,            \tag{12}
\]
\[
 \|E_Z\|_\infty
   \le C\|E_Z\|_2^{7/8}\|E_Z\|_{H^{12}}^{1/8}
                       \le h^{25/16}H_h^C.           \tag{13}
\]
This is a separate exact-linear estimate. There is no eta times ell
squared loss in its energy exponent.

## 5. The linearized receiver has negligible coarse-band output

For the error in (10), expanding-torus Fourier Cauchy-Schwarz gives
\[
 \|\mathcal B_hE_Z\|_\infty
    \le C\kappa_h^{3/2}\|E_Z\|_2
                       \le h^2H_h^C.                \tag{14}
\]
Indeed \(\kappa_h^{3/2}\) has h power -15/8, leaving
31/8-15/8=2. The reciprocal torus volume in Fourier inversion cancels
the frequency-counting volume.

It remains to control the actual evaluated zero-mean profiles in
Z_app, rather than their formal phase means. For every Fourier mode
n!=0 and every K in the observation annulus, the complete phase is
\[
 nS(x)/k-K\cdot x.
\]
The exact cotangent history is nonzero; its inverse and all needed
finite slow jets are bounded by H_h^C on the transported chart.
Since k kappa_h H_h^C tends to zero for every fixed exponent C,
\[
 |n\xi/k-K|\ge |n|/(2kH_h^C).
\]
Thus there is no stationary point. Integrate twice by parts with the
gradient of this full phase. The envelope and coefficients cost
d^(-1)H_h^C per slow derivative, and q derivatives cost the smaller
h^(-1) scale. The exact curl terms and all inverse-covector derivatives
are included. Summing the nonzero modes using the fixed profile
Fourier norms gives, in the unnormalized Fourier convention,
\[
 |\widetilde Z_{\rm app}(K)|
        \le C k d^3(k/d)^2 H_h^C.                   \tag{15}
\]
The amplitude and support-volume estimates are uniform through the
whole flight. g_lin has smaller size and satisfies the same bound.

There are O((L kappa_h)^3) lattice modes in the annulus. Fourier
inversion divides by the torus volume (2pi L)^3, so (15) yields
\[
 \|\mathcal B_hZ_{\rm app}\|_\infty
       \le C\kappa_h^3 k d^3(k/d)^2H_h^C
       \le h^2H_h^C.                                \tag{16}
\]
Combining (14),(16) proves the Z part of (1). In particular no
phase-independent component of the exact Z was silently set to zero:
all such possible leakage is bounded by the global error (10).

## 6. Background band and the unchanged initial data

The existing first-stage H12 estimate, or its ordinary H12 energy
inequality with the sharp q clock, gives
\[
 \sup_{0\le t\le t_\eta}\|q(t)\|_{H^{12}}
             \le h^{7/4-12}H_h^C=h^{-41/4}H_h^C.
\]
The initial exponent comes from the primary packet amplitude h,
its radius h^(1/2), and its h-scale derivatives, including the full
curl correction. The fixed smooth V contributes only a fixed norm.
The same subpower factor covers the later q evolution and its global
pressure tails.

On the annulus, Fourier Cauchy-Schwarz now gives
\[
 \|\mathcal B_hq\|_\infty
  \le C\kappa_h^{3/2-12}\|q\|_{H^{12}}
  \le h^{(5/4)(21/2)-41/4}H_h^C
  =h^{23/8}H_h^C.                                   \tag{17}
\]
This proves the other half of (1).

At original time zero, Z_app(0)=z_0, with g_lin=0. Equation (15)
therefore applies directly to the full original receiver, without
an error term. Together with (17), it proves the velocity estimate
in (4). Differentiation of the annular Fourier multiplier costs one
factor kappa_h, giving the h^(3/4) gradient estimate.
These estimates use the exact original datum, not a truncation which
removes its Fourier tails.

## 7. Passing the signed pairing to full Q

The reviewed postfocus result supplies a real scalar cone kernel f_h,
centered at the existing q-particle, with
\(\|f_h\|_1\le C\delta_h^{-4}\), and the signed lower bound
\[
 \langle r(t_\eta)\cdot\mathcal N(t_\eta),f_h\rangle
       \ge c\,\eta^{-1}h^{7/4}\ell^{9/8}H_h^{-4A}.
                                                        \tag{18}
\]
Here the kernel already includes its physical-in-rescaled-coordinates
kappa_h^3 scaling and periodization. Its support in Fourier space
lies where the symbol of B_h equals one.

The q and Z contributions to this scalar pairing have absolute size
at most
\[
 C\delta_h^{-4}(h^2+h^{23/8})H_h^C.
\]
This is o of the right side of (18): the positive h power 1/4
dominates every displayed fixed subpower cost, including the cone.
Since Q=q+Z+N exactly, the signed pairing for Q is at least half
(18) for sufficiently small h. Scalar duality gives (2). Applying
the same band-supported inverse-Laplacian strain duality as in the
reviewed postfocus note gives (3).

No full-flow lower bound is inferred merely from a lower bound on a
cancelling summand. The actual q and Z bands have been estimated
separately before taking this step.

## 8. The generated remainder's own strain clock vanishes

The nonlinear approximation already established in the logarithmic
host is
\[
 U_1=q+\mathcal E[W_a]+m_1+\mathcal E[W_{g_{\rm nl}}],
 \qquad \|\nabla(Q-U_1)\|_\infty\le h^{1/96}.
\]
Its correction bounds, in actual evaluated norms, are
\[
 \|m_1\|_{C^1}\le h^{1/2}H_h^C,\qquad
 \|\mathcal E[W_{g_{\rm nl}}]\|_{C^1}
       +\|\mathcal E[W_{g_{\rm lin}}]\|_{C^1}
                              \le h^{1/4}H_h^C.      \tag{19}
\]
The first inequality permits global mean tails. The velocity parts
are smaller than the displayed gradient bounds.

The exact decomposition is
\[
 \mathcal N=(Q-U_1)+m_1+\mathcal E[W_{g_{\rm nl}}]
                 -\mathcal E[W_{g_{\rm lin}}]-E_Z.
\]
Equations (12),(19) thus bound its gradient by
\[
 h^{1/96}+h^{1/48}H_h^C+h^{1/4}H_h^C+h^{1/2}H_h^C
                              \le C h^{1/96}.        \tag{20}
\]
The velocity error Q-U1 is also smaller than h^(1/96). This follows
from its known small L2 norm and gradient bound, using the uniform
local interpolation inequality
\[
 \|v\|_\infty\le C\left(\|v\|_2+
            \|v\|_2^{2/5}\|\nabla v\|_\infty^{3/5}\right)
\]
on tori with side at least 2pi. One may prove this by optimizing the
radius of a ball of radius at most one. All other velocity terms are
controlled by (13),(19). This proves the C1 assertion in (5).
Finally t_eta=O_eta(log ell), so integration gives its stated
vanishing clock.

The small generated component therefore contributes only o(1) to
standard deformation or energy growth bounds through its own strain
on the present interval. The full Q clock can still be large because
the existing q and supplied linearized receiver Z are retained.
Equation (5) is neither a later-time exclusion nor a prohibition on
coupling the component to a different part of the actual flow.

## Verification and remaining task

[The bounded algebra checks](../../experiments/nse_coarse_band_linear_checks.py)
verify the longitudinal-pressure cancellation, weighted q coefficients,
interpolation and band powers, and the positive margin separating the
full endpoint band from its original value. They are not an analytic
PDE certificate.

The actual intermediate band is now distinct from both its initial
tails and the chosen linear comparison. Its later shape, feedback and
useful coupling remain to be established. A detectable generated
component with a vanishing present strain clock does not itself
produce another amplification stage or an infinite trajectory.
