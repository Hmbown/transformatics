# Wave handover: exact cancellation, pressure feedback, and a stability obstruction

**8 September 2026. PROVED restricted identities and insufficiency result.
ROOT and (E′) remain OPEN.** These examples locate a missing estimate in
the next packet construction. They do not prove singularity or rule out
every prepared-packet method.

Pins: [exact Fourier algebra](../../experiments/nse_wave_handover.py),
[independent physical-space tests](../../tests/test_nse_wave_handover.py),
and [receipt](../../artifacts/enstrophy_sup/nse_wave_handover.json).
Node nse-wave-handover-obstruction, outside the critical path into ROOT.

The [preceding full-NS theorem](viscous-packet.md) amplifies
a supplied seed but keeps it small in rescaled H³. Its actual high-pass
norm remains below the earlier target throughout the controlled interval.
This note tests a different mechanism: small velocity with large
oscillatory strain. All norms below are on a fixed periodic torus unless
otherwise stated; averaged L² is used for the explicit integrals.

## 1. The self-interaction really does cancel

Let \(\xi=\nabla S\), \(\xi\cdot B=0\), and
\(W=aB\cos(S/h)\), with B varying on scale \(\delta\). Directly,

\[
(W\cdot\nabla)W
=a^2\cos^2(S/h)(B\cdot\nabla)B
-{a^2\over h}\cos(S/h)\sin(S/h)(B\cdot\xi)B
=a^2\cos^2(S/h)(B\cdot\nabla)B.
\]

An exact curl correction of size \(O(ah/\delta)\) also has cross-terms
of envelope size \(O(a^2/\delta)\), subject to the stated derivative
bounds. This calculation removes a large self-forcing term. It does not
bound the propagator for arbitrary errors.

Here a is a pointwise velocity amplitude. A packet occupying volume
\(\delta^3\) has L² size of order \(a\delta^{3/2}\). Thus with
\(\delta=h^{1/2}\), the window \(h\ll a\ll\delta\) corresponds to
\(h^{7/4}\ll\eta\ll h^{5/4}\) for the normalized L² coefficient \(\eta\).
Confusing these amplitudes changes the intended strain threshold.

## 2. A sharp obstruction to the generic envelope-rate energy estimate

Take positive integers \(M<N\), and define

\[
W=a\cos(Nz)e_1,\qquad
e=\left(\sin(Mx)\sin(Nz),\,0,\,
\sin(Mx)+{M\over N}\cos(Mx)\cos(Nz)\right).
\]

Both are real, divergence-free, and mean-zero. The field W has exactly
zero self-interaction. Nevertheless, direct integration gives

\[
-\langle e,(e\cdot\nabla)W\rangle_{\rm av}={aN\over4},\qquad
\|e\|_{2,\rm av}^2={3+(M/N)^2\over4},
\]

\[
\|\nabla e\|_{2,\rm av}^2
=M^2+{N^2\over4}+{M^4\over4N^2}.
\]

Pressure cannot remove this energy pairing: e is solenoidal and the
Leray projection is orthogonal. The exact NS background
\(W(t)=a e^{-\epsilon N^2t}\cos(Nz)e_1\) is an unforced heat shear.
For its linearized equation, the initial logarithmic norm-growth rate is

\[
{d\over dt}\log\|e(t)\|_{2,\rm av}\bigg|_{0}
={aN-\epsilon(N^2+4M^2+M^4/N^2)\over3+(M/N)^2}.
\tag{1}
\]

The same quadratic pairing governs the initial relative-energy change
for the full equation; its perturbation self-advection cancels in L².
This is an initial rate, not a sustained-growth theorem.

To exhibit the scale mismatch exactly, let
\(N=q^4,\ M=q^2,\ a=q^{-3},\ \epsilon=q^{-16}\) with integer \(q\to\infty\).
Then \(h=N^{-1}\), \(\delta=M^{-1}\), and \(h\ll a\ll\delta\).
The rate in (1) is asymptotic to \(q/3\), while
\(a/\delta=q^{-1}\to0\) and \(\epsilon/h^2=q^{-8}\to0\).
There is no constant independent of these scales bounding the initial
rate by \(C(1+a/\delta+\epsilon/h^2)\) for this class of arbitrary
solenoidal errors.

The missing term is

\[
(e\cdot\nabla)W
=-{a\over h}(e\cdot\xi)B\sin(S/h)
+O(a|e|/\delta).
\]

Divergence-free e need not satisfy \(e\cdot\xi=0\). In this example its
slow normal component is precisely what couples into the large term.
The example is an embedded two-dimensional flow, compatible with global
regularity. It disproves the proposed generic stability estimate, not
regularity or a more restrictive prepared-class estimate.

## 3. Pressure actually generates a normal mean component

The offending kind of component is not merely a hypothetical error.
Choose \(N\ge5M>0\), and let

\[
b=\bigl(\cos(Mz)\cos(My),-\cos(Mz)\cos(Mx),0\bigr),\qquad
w_0=a b\cos(Nz).
\]

This datum is exactly divergence-free and transverse to the fast
covector \(e_3\). Set

\[
p_0=\cos^2(Mz)\sin(Mx)\sin(My).
\]

Direct differentiation gives
\((b\cdot\nabla)b=\nabla_{x,y}p_0\). The zero fast harmonic of
\((w_0\cdot\nabla)w_0\) is therefore \((a^2/2)\nabla_{x,y}p_0\).
Its NS contribution is

\[
-{a^2\over2}\mathbb P\nabla_{x,y}p_0
={a^2\over2}\mathbb P(e_3\partial_zp_0).
\]

The derivative \(\partial_zp_0=-M\sin(Mx)\sin(My)\sin(2Mz)\) has only
wavevectors \((\pm M,\pm M,\pm2M)\). On these modes
\(\mathbb P_{33}=1-4/6=1/3\). Consequently the generated normal mean is

\[
-{a^2M\over6}\sin(Mx)\sin(My)\sin(2Mz).
\tag{2}
\]

This is the exact initial derivative of the third component of
\(P_{\le3M}u\) for the full unforced NS solution initialized at \(w_0\).
Indeed the initial datum has no modes below \(3M\), the other quadratic
harmonics lie above \(3M\), and viscosity contributes no initial low
modes. The existence of a local smooth solution is classical.

An independent physical-space check solves its slow pressure explicitly:

\[
p=-a^2\left({1\over4}+{\cos(2Mz)\over12}\right)
\sin(Mx)\sin(My).
\]

It obeys \(\Delta p=-\operatorname{div}[(a^2/2)\nabla_{x,y}p_0]\),
and \(-\partial_zp\) equals (2). Omitting pressure would give zero
normal mean, the wrong conclusion. This calculation proves generation
at the initial time; it supplies no persistence, amplitude handover,
or singularity.

## 4. What a corrected phase must account for

The mean source is generically
\(-\tfrac12 a^2\mathbb P[(B\cdot\nabla)B]\), together with exact curl
corrections. A mean velocity of size \(ta^2/\delta\) can change phase
divided by wavelength on the scale \(t^2a^2/(\delta h)\).
This is a size diagnostic, not a lower bound on drift for every profile.
For \(\delta=h^{1/2}\), \(a=h^\alpha\), the diagnostic is
\(t^2h^{2\alpha-3/2}\). Small \(a/\delta\) alone therefore does not
justify keeping the phase fixed.

An improved construction must evolve the mean flow and phase together,
or price their full residual. It must then control the actual generated
error class, including longitudinal mean velocity and second harmonics.
The self-cancellation in section 1 does not establish this stability.

## 5. Relevant literature and its hypothesis boundary

[Cheverry, Cascade of phases in turbulent flows (2006)](https://www.numdam.org/item/BSMF_2006__134_1_33_0/)
provides a useful phase hierarchy. Theorem 3.1 constructs high-order
Euler approximations, with corrected phases, on a fixed interval.
Its Theorem 6.1 uses a lifted system with adjusted anisotropic diffusion
and a sufficiently large diffusion coefficient. That stability theorem
does not supply the required result for isotropic physical
\(\epsilon=\nu h^4\). Shrinking envelopes and growing time also need
their own bounds.

[Friedlander–Pavlović–Shvydkoy (2005)](https://arxiv.org/html/math/0508173)
deduce nonlinear NS instability from viscous spectral instability around
a steady equilibrium. Our background is an unforced time-dependent NS
solution, and an inviscid polarization multiplier does not give the
required viscous eigenvalue. The
[vanishing-viscosity spectral theorem](https://arxiv.org/html/math/0509538)
preserves suitable inviscid eigenvalues beyond the essential-spectrum
growth bound; our present short-wave construction supplies no such
spectral-gap hypothesis.

These are specific applicability failures. The search did not establish
that no more specialized stability result exists.

## 6. Next mathematical question

Derive a full residual and an error propagator for a prepared mean/phase
construction that can reach strain comparable to the background.
An alternative under examination is to approach the handover more
slowly, over a log-log window, so the integrated large strain costs only
a subpolynomial factor. Such a construction still needs its actual
correction equations and a separate strong-continuation argument.
It is not proved by the identities in this note.

Even a finite successful strain handover does not make the outgoing
wave a new scaled Gavrilov profile or supply the next dormant seed.
One smooth initial datum, one viscosity, controlled interstage errors,
and a genuine infinite-stage conclusion remain unproved. No new DNS.
