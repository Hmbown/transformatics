# What the existing outgoing waves actually generate

8 September 2026. Independent signed-source calculation. This note establishes exact identities for the frozen two-wave model and consequences of the already registered finite-time bounds. It does not extend the actual solution beyond its proved lifetime, establish a third handover, or exclude other geometries.

## 1. Outcome and conventions

The leading cross-interaction is nonzero, but its output is directed along the existing streamwise polarization p. Its two formal sidebands have the same asymptotic wavelength k as the second wave. On the actual localized second packet they are not separated from that packet's envelope bandwidth: this is the amplitude transfer already used in the second handover, not an independent third carrier.

The envelope does generate a pressure-bearing mean and a second harmonic. They are the zero-initial corrections already present in the original-time theorem. Their proved gradient bounds tend to zero. The mean can have a normal component, but is slower than the donor. This is a concrete high-high-low output, with neither the direction/scale nor the size needed for the proposed next fine handover at the current endpoint.

Sources in the repository are [the original nonlinear handover](../navier-stokes/original-nonlinear-handover.md), especially (13), (17)-(25), (28). Fix the profile j and viscosity nu before taking h to zero, and retain

\[
\ell=\sqrt{\log(1/h)},\quad k=h^{3/2},\quad d=h^{5/4},\quad \epsilon=\nu h^4.
\]

At the terminal reference point use the orthonormal frame (p,r,n), where r=n cross p. Coordinates (x,y,z) are in these directions. Fixed bounded geometric constants are retained as alpha h and beta k when necessary. The frozen waves are

\[
u_1=A p\cos(\alpha z),\qquad
u_2=(B p+C n)\cos(\beta y),                         \tag{1}
\]

where

\[
A\asymp h\ell,\quad \alpha\asymp h^{-1},\quad
C=k\ell^{7/8},\quad B=C P_h\asymp k\ell^{11/8},\quad
\beta=4/k.                                         \tag{2}
\]

Constant phase shifts do not change the conclusions; the actual central phases are pi/2. Equation (1) is an uncut periodic model when its frequencies belong to the torus lattice, or an exact local Euclidean model. The actual compact packets have envelopes and curved transported phases. No assertion that their global pressure vanishes is made.

## 2. Exact sign and full pressure projection

For divergence-free complex Fourier amplitudes a at P and b at Q, with P dot a=Q dot b=0, the complete cross contribution to the velocity time derivative at K=P+Q is

\[
\widehat{\mathcal N}_{P,Q}(K)
=-i\mathbb P_K\big[(a\cdot Q)b+(b\cdot P)a\big],\qquad
\mathbb P_K=I-K\otimes K/|K|^2.                     \tag{3}
\]

This follows by expanding minus div(u tensor u). Both ordered products are included. It includes pressure rather than projecting one selected tensor component. Real cosines contribute a factor 1/2 to each signed input Fourier mode.

For (1), let K1=alpha n and K2=beta r. Then

\[
(Ap)\cdot K2=0,\qquad (Bp+Cn)\cdot K1=C\alpha,
\qquad p\perp K1\pm K2.
\]

Consequently the exact real cross source is

\[
-\mathbb P\big[(u_1\cdot\nabla)u_2+(u_2\cdot\nabla)u_1\big]
=A C\alpha\,p\sin(\alpha z)\cos(\beta y)
=\frac{AC\alpha}{2}p\{\sin((K1+K2)\cdot X)+\sin((K1-K2)\cdot X)\}. \tag{4}
\]

If the second phase is instead named K2-K1, its sine coefficient has the opposite sign. No B term survives. The vector on the right is divergence-free because it is p-directed and independent of x, so Leray leaves it unchanged. Both self-interactions in (1) vanish identically. Thus (4) is the entire nonlinear term for this model, and the pressure can be constant.

At the common pi/2 phase the full gradient is

\[
\mathcal A=-\Lambda p\otimes n-H(n+P_h p)\otimes r,
\quad \Lambda=A\alpha,\ H=C\beta.
\]

It has rank two, not rank one, and

\[
\mathcal A^2=\Lambda H p\otimes r,\qquad \mathcal A^3=0.
\]

The extra shear chain is real. Nevertheless \(\mathcal A p=0\). Therefore a p-polarized shortwave remains neutral in the full pressure-corrected amplitude equation

\[
\dot b=-\mathcal A b+2\xi\frac{\xi\cdot\mathcal A b}{|\xi|^2},
\]

provided initially b is proportional to p and xi dot p=0. The covector evolution preserves xi dot p=0, since \(\mathcal A p=0\). The generated p output does not supply the r component that the outgoing r-normal shear would act on. This is an exact statement about this common invariant geometry, not a universal non-amplification claim for rank-two gradients.

## 3. Why the cross sideband is already the receiving amplitude

The formal sidebands obey

\[
|K1\pm K2|=\beta\sqrt{1+(\alpha/\beta)^2}
=\beta[1+O(h)],\qquad \alpha/\beta=O(h^{1/2}).       \tag{5}
\]

There is no scale comparable to h^(-9/4) at quadratic order. Even the distinction between K2 and K2 plus/minus K1 is not a resolved carrier distinction for this particular packet:

\[
\alpha d\asymp h^{1/4}\to0,\qquad
\beta d=4h^{-1/4}\to\infty.
\]

The sideband separation 1/h is smaller than the envelope bandwidth 1/d. On the final support, sin(alpha z plus its central phase) is a slowly changing coefficient multiplying the second oscillation. On the plateau at central primary phase pi/2, it equals 1+O((d/h)^2) in the affine model.

In the actual construction Z2 is propagated by D_q b=Gb, with A=grad q including the first wave. The leading term minus (Z2 dot grad)Z1 in (4) is precisely the corresponding part of minus A b, and the other cross term is in D_q. It was already paid for in the selected receiving polarization's growth from a small original datum to B p+C n. Calling (4) a newly generated third seed would count that same mechanism twice.

Smooth cutoffs have Fourier tails, so (5) is not a literal claim that the actual Fourier support contains only four points. It is a statement about the leading oscillatory phases. Fixed-order derivative estimates control the tails; they do not turn them into a new large carrier.

## 4. Exact finite-time generation and donor heat timing

The frozen inviscid problem can be solved without inserting any sideband:

\[
u(t,x,y,z)=\big[B\cos(\beta y)+A\cos(\alpha[z-Ct\cos(\beta y)]),\ 0,\ C\cos(\beta y)\big]. \tag{6}
\]

Direct differentiation proves divergence-free Euler with constant pressure. The p component is a scalar transported by a transverse shear. All generated modes remain p-directed. Expanding the transported exponential gives phases K1+m K2 with mixing parameter

\[
\zeta(t)=\alpha Ct.
\]

For positive viscosity the exact reduction remains equally explicit at the equation level:

\[
u_r=0,\quad u_n=C e^{-\epsilon\beta^2t}\cos(\beta y),\quad
u_p=B e^{-\epsilon\beta^2t}\cos(\beta y)+f(t,y,z),
\]

\[
\partial_t f+C e^{-\epsilon\beta^2t}\cos(\beta y)\partial_z f
=\epsilon(\partial_y^2+\partial_z^2)f,\quad f(0)=A\cos(\alpha z). \tag{7}
\]

The pressure is still constant. This invariant reduction prevents any generated r velocity. Its smoothness is the smoothness of a linear parabolic transport equation with a given smooth shear.

Writing the positive-z Fourier sector as

\[
f=\operatorname{Re}\left[A e^{i\alpha z}\sum_m c_m(t)e^{im\beta y}\right]
\]

gives the exact ladder

\[
\dot c_m+\epsilon(\alpha^2+m^2\beta^2)c_m
=-\frac{i\alpha C e^{-\epsilon\beta^2t}}2(c_{m-1}+c_{m+1}),\qquad c_m(0)=\mathbf1_{m=0}. \tag{8}
\]

The first Duhamel coefficient, retaining both donor heat factors, is exactly

\[
c_{\pm1}^{[1]}(t)=-\frac{i\alpha C t}{2}
 e^{-\epsilon(\alpha^2+\beta^2)t}.                    \tag{9}
\]

Orthogonality gives \(|K1\pm K2|^2=|K1|^2+|K2|^2\), explaining the exact factor t. This is not a claim that (9) is the full coefficient: further odd interaction orders contribute. Iterating (8), whose diagonal heat propagators are contractions, bounds an m-sideband by

\[
|c_m(t)|\le e^{Z(t)}\frac{Z(t)^{|m|}}{|m|!},\qquad
Z(t)=\alpha|C|\int_0^t e^{-\epsilon\beta^2s}\,ds.     \tag{10}
\]

Indeed reaching m takes at least |m| nearest-neighbor interactions, and the sum of the absolute coupling strengths is alpha |C(t)|. This also proves a small-Z expansion without relying on an asymptotic Bessel formula.

For a **frozen-model** duration \(\Delta=\ell^{-3/4}\), starting from (1)-(2),

\[
Z(\Delta)\asymp h^{1/2}\ell^{1/8}\ll1,
\quad \epsilon\beta^2\Delta=16\nu h\ell^{-3/4}\ll1. \tag{11}
\]

The first generated sine amplitude in (4), integrated over this duration, is of order

\[
A Z(\Delta)\asymp k\ell^{9/8};
\quad \text{its strain is of order }\ell^{9/8}.
\]

It is smaller by \(\ell^{-1/4}\) than the already present second p strain \(\ell^{11/8}\). The m=2 sideband strain is at most

\[
C\frac{A}{k}Z(\Delta)^2=O(h^{1/2}\ell^{5/4}),        \tag{12}
\]

and successive m cost further powers of Z. These are exact model time comparisons. The registered actual-Q theorem ends at t_f; it does not authorize identifying the future interval [t_f,t_f+Delta] with this model.

For the literal next wavelength k3=h^(9/4), one would need |m| of order k/k3=h^(-3/4). Such a mode is far beyond the fixed-time interaction ladder. Even over all future time in the heat-shear model,

\[
Z(\infty)=\frac{\alpha|C|}{\epsilon\beta^2}
\asymp\nu^{-1}h^{-1/2}\ell^{7/8},\qquad
\frac{Z(\infty)}{h^{-3/4}}\to0.
\]

Equation (10) then gives a faster-than-algebraic upper bound at the required m, uniformly in time. Equivalently, the constant-shear time to reach that m would be h^(-5/4)ell^(-7/8), exceeding the donor heat lifetime of order nu^(-1)h^(-1). The target's own diffusion rate is \(\epsilon/k3^2=\nu h^{-1/2}\), also larger than any of the current logarithmic strain rates. These are obstructions to this exact sinusoidal passive-shear model and that literal wavelength choice. They do not exclude other receiving scales or other interacting geometries.

## 5. A genuinely generated normal mean exists, but it is low and small

The exact single-packet identity in the original theorem is

\[
(Z2\cdot\nabla)Z2=Q0+\operatorname{Re}(F2 e^{2i\theta_2}),
\]

with its complete curl corrections included. The nominal fast self-interaction a2 squared divided by k cancels because the leading amplitude is tangent to its phase. Only envelope/geometry derivatives survive. The theorem constructs the resulting global mean and the first/second harmonic corrections from zero original data; they are genuinely generated fields.

There is no pressure-based reason for the mean to remain tangent. For a constant c perpendicular to r and a frozen envelope b=a chi c, the leading phase-average stress is \(R_0=a^2\chi^2 c\otimes c/2\). Its signed mean force has r component

\[
r\cdot[-\mathbb P\operatorname{div}R_0]
=\frac{a^2}{2}\partial_r\Delta^{-1}(c\cdot\nabla)^2\chi^2. \tag{13}
\]

The unprojected term has zero r component; the displayed term is entirely pressure. It can be nonzero away from a symmetric center. Its scale is the envelope scale d, which is larger than k. Formula (13) is an actual candidate normal **low-frequency** source, not a tangent high-frequency source. It makes no signed lower-bound assertion after transport and integration for the prescribed bump.

The original theorem's global bounds, which retain pressure tails, imply

\[
\|m\|_{C^1}\le C k^2d^{-2}E_h=C h^{1/2}E_h,
\quad
\|\operatorname{Re}C_1[g_1]+\operatorname{Re}C_2[g_2]\|_{C^1}
\le C(k/d)E_h=C h^{1/4}E_h,\qquad E_h=e^{C\ell}.    \tag{14}
\]

Thus all these generated additions have o(1) strain through the proved interval. The actual nonlinear tracking error is also o(1) in C1. None supplies another dominant component by t_f. The second harmonic's principal polarization is perpendicular to r because its phase is 2 theta2; in the pure outgoing r-normal shear it has no normal r input to amplify. Lower-order pressure/curl effects are not discarded; they are covered by (14).

A still stronger current-window exclusion follows directly from the registered H12 estimate \(\|Q_h\|_{H^{12}}\le h^{-117/8}G_h\). Uniform Fourier Cauchy-Schwarz on the expanding torus gives

\[
\|\nabla P_{>M}Q_h\|_\infty\le C M^{-19/2}\|Q_h\|_{H^{12}},\quad M\ge1.
\]

The exponent comes from the three-dimensional integral of |xi|^2(1+|xi|^2)^(-12) over |xi|>M. With M=h^(-9/4),

\[
\sup_{0\le t\le t_f}\|\nabla P_{>h^{-9/4}}Q_h(t)\|_\infty
\le h^{27/4}G_h=h^{27/4-o(1)}.                    \tag{15}
\]

This uses the full solution and therefore covers cutoff tails and every interaction. It says nothing about an interval after t_f without a new strain/continuation budget.

## 6. What can actually be reused from Palasek

[Palasek, arXiv:2509.18595v1](https://arxiv.org/html/2509.18595v1), submitted 23 September 2025, proves finite arbitrary norm growth for globally regular unforced NS solutions. Section 1.2 describes high-high-low transfer, with donors of frequency N decaying on time N^(-2). Theorem 1.1 is not a singularity theorem.

The reusable construction is the **signed stress design** in Lemma 2.7, equations (20)-(21): prescribed slow receiver geometry is encoded in amplitude squares of separated Mikado donors. Proposition 2.10 shows that its projected low stress cancels the receiver's activation derivative and controls all remaining errors. The transfer coefficient is proportional to lower frequency times donor amplitude squared divided by donor frequency squared. It is an inverse transfer; its direction cannot be reversed by changing terminology. Constant plane-wave self-interactions vanish there too: the designed spatial amplitudes carry the transfer.

Our calculation supplies no corresponding signed design identity for a finer output from the current donors. Its nonzero pressure mean (13) is low, and the current donor heat rate is only O(nu h), so there is no donor reset on the proved logarithmic interval. Reusing Palasek requires a new stress design and a paid time/diffusion budget, not importing its theorem as forward-cascade growth.

## 7. Precise next boundary

There is no adequate third carrier generated by the current leading cross geometry. The positive output is the explicit normal low mean (13), with the inadequate size (14). The first cross sideband (4) is already part of the second receiving amplitude. Neither can be renamed as a successful fine-to-finer transfer.

A concrete next source calculation would have to retain the first nonzero departure from the p-independent geometry: the actual slowly varying frame, pressure-bearing envelope mean, and any p-dependent profile coupling. It must extract a specified new carrier/polarization from the signed source after subtracting the existing theta2 amplitude equation, and prove a lower bound on its transported Duhamel integral. If the proposed wavelength is h^(9/4), (15) forces that work outside the already proved time window; the fixed viscosity also imposes the rate described after (12). A different wavelength or profile must be stated explicitly.

This is not a universal obstruction to dynamically generated receivers, and it does not treat a non-sinusoidal profile's preinstalled harmonics as newly generated energy.

## 8. Independent exact checks

[the preserved algebra controls](checks/check-profile-extension.py) was executed with the repository's `.venv/bin/python`. Exact SymPy identities checked (4), both signed Leray projections, absence of B, the divergence of the nonlinear term, solution (6), the rank-two nilpotent chain, p-polarization neutrality, and the donor-heat Duhamel coefficient (9). Fraction arithmetic checked all five h/ell timing exponents in (11)-(12). All passed. These checks pin algebra; they do not certify PDE estimates or extend the theorem's lifetime.

## 9. Exact strain-growth identity for a viscous Kelvin ray

Independent check of the proposed ray bound: **valid for the principal, unforced amplitude ODE**. Let A(t) be any real trace-free 3 by 3 matrix, let S(A)=(A+A transpose)/2, and fix kappa>0. For nonzero real xi,b satisfying

\[
\dot\xi=-A^T\xi,\qquad
\dot b=-Ab+2\xi\frac{\xi\cdot Ab}{|\xi|^2}
        -\frac{\epsilon|\xi|^2}{\kappa^2}b,
\qquad \xi\cdot b=0,                              \tag{16}
\]

put \(n=(\xi\mathbin{\times}b)/(|\xi||b|)\). Initial orthogonality is preserved, since its derivative is minus epsilon |xi| squared / kappa squared times xi dot b. On any finite smooth interval the two nonzero vectors remain nonzero by their linear ODEs. The three vectors xi/|xi|, b/|b|, n are therefore an orthonormal frame.

Taking the two logarithmic norm derivatives gives

\[
\frac{d}{dt}\log|\xi|=-\widehat\xi^T S(A)\widehat\xi,
\qquad
\frac{d}{dt}\log|b|=-\widehat b^T S(A)\widehat b
                         -\frac{\epsilon|\xi|^2}{\kappa^2}.
\]

The pressure term has zero pairing with b. Summing and using trace S(A)=0 yields the exact identity

\[
\boxed{\frac{d}{dt}\log(|\xi||b|)
       =n^T S(A)n-\frac{\epsilon|\xi|^2}{\kappa^2}.} \tag{17}
\]

In particular, if throughout [s,t] the ray frequency |xi|/kappa is at least K0 and the strain operator norm is at most M, then

\[
\frac{|\xi(t)||b(t)|}{|\xi(s)||b(s)|}
\le\exp\{(M-\epsilon K0^2)(t-s)\}.                \tag{18}
\]

With time-dependent bounds, the exponent is the integral of M(t)-epsilon |xi(t)| squared / kappa squared. The quantity |xi||b|/kappa is the principal oscillatory gradient amplitude; its symmetric Frobenius strain amplitude is smaller by exactly sqrt(2). Thus (18) directly bounds this strain amplitude. For a complex polarization, the single real unit normal in (17) is not defined in this form; (18) still holds by applying it separately to the real and imaginary tangent polarizations and summing their squared norms.

For the current actual Q_h trajectory, the original theorem gives the uniform bound

\[
\sup_{[0,t_f]}\|S(Q_h)\|_{\mathrm{op},\infty}
\le C\ell^{11/8}.
\]

Fix any beta>2 and any principal ray remaining at frequency at least h^(-beta) during a subinterval of this proved lifetime. Since

\[
\epsilon K0^2=\nu h^{4-2\beta}\gg C\ell^{11/8},
\]

its strain amplitude strictly decreases, and for sufficiently small h its gain over duration Delta is at most

\[
\exp[-(\nu/2)h^{4-2\beta}\Delta].                 \tag{19}
\]

At beta=9/4 the damping rate is nu h^(-1/2), as asserted. This conclusion requires the ray to remain that fine throughout the compared interval. It does not extend the actual-Q lifespan or assert the same strain bound after t_f.

Equations (17)-(19) are principal ODE identities and inequalities. They omit any additive generated source, envelope residual, or coupling between rays. They are consequently not an estimate for a sourced full Fourier projection. A new source can replenish a damped receiver, and a ray can leave the prescribed frequency range; either mechanism needs its own quantitative argument. The full-PDE current-window estimate remains the separate bound (15).


## Review provenance

[Independent review record](profile-extension-review.md). Original reviewed source `nse-generated-receiver-check-20260908.md`, SHA-256 `8cec50deb4996ef4706f1064e3f93a04e782938c975e1709029b3d0a3b5830fd`. Archival changes resolve links and current-scope wording; they do not replace a formal PDE certificate.
