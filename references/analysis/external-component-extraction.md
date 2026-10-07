# Extracting an actual covariance component from the released construction

Date: 8 September 2026.

**Scope.** This note extracts one exported theorem from the released OpenAI
source and proves a phase-replacement corollary at its exact algebraic
interface. The inspected theorem uses actual periodized pulses, not just
the ideal two-column model. It controls two leading radial–tangential
covariance components. It does not certify a replacement for the full
curl-corrected velocity, its transport, the correction iteration or the
terminal force.

The inspected source is [OpenAI/NavierStokesAndEuler at commit
8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
This subtask read declarations and proofs; it did not perform a full Lean
replay. The separate replay lane owns that question.

## 1. Exported statement and complete packaged inputs

The selected theorem is
[NavierStokes.PartitionedCovariance.physical_primary_covariance](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/PartitionedCovariance.lean#L947).
Its declaration and proof occupy lines 947–977.

Here \(h\) is the external construction's exponent parameter and \(q>0\)
its physical similarity scale. This \(q\) is **not** the velocity called
\(q\) in this project's earlier work. Put
\[
a_h=\tfrac12+h,\qquad Q_n=2^{-n}.
\]
An unsigned label is \(U=(n,\ell)\in\mathbb N\times\mathbb Z^3\).
It has two distinct signed slots \(j=0,1\). The theorem takes:

1. Real \(D,h\), plane vectors \(v_r,v_t\) with
   \(\det(v_r,v_t)\ne0\), and a supplied SlotSystem.
   This contains a radius \(r>0\), quotient injectivity of every prescribed
   oriented slot in \(\mathbb R^2\to(\mathbb R/\mathbb Z)^2\), and
   disjointness of the prescribed covered slot supports whenever their
   labels satisfy the source's exact SlotColoring.Adj relation.
   Arbitrary disjoint sets cannot be substituted for these indexed maps.
2. An integer \(N\ge1\), and a family PairData at the tail labels
   \((n+N,\ell)\).
3. For each \(U,j\), a Pulse: continuous functions
   \(\psi,x:\mathbb R\to\mathbb R\) and
   \(t:\mathbb R\to\mathbb R^2\), with \(\psi\) compactly supported.
   Its positive transverse scale \(c_{Uj}\) obeys
   \[
   \operatorname{supp}\psi_{Uj}\subseteq[0,2r/c_{Uj}].
   \]
   Its angular mode \(m_{Uj}\) is a nonzero integer.
   Its phase \(\phi_{Uj}:\mathbb R^2\to\mathbb R\) is arbitrary:
   **the declaration assumes no regularity of this function.**
4. A scale \(0<q\le Q_N\), a position \(x\in\mathbb R^3\), a target
   \(T_0\in\mathbb R^2\), and, for every label with nonzero prescribed
   physical mask \(M_U(q,x)\), the condition
   \[
   \operatorname{StrictCone}(H_U,T_U),\qquad
   T_U=(Q_{n+N}/q)^{a_h+1/2}T_0.
   \tag{1}
   \]

SlotSystem and PairData are declared at lines 224 and 595. There is no
separate \(h\ge0\) hypothesis in this theorem once SlotSystem is supplied.
The theorem constructing a SlotSystem, exists_slotSystem, does assume
\(h\ge0\); later physical applications impose additional restrictions.

The matrix \(H_U\) uses actual native pulse integrals. With the source's
transverse cutoff \(\chi_r\),
\[
(H_U)_{ij}=
\frac{|\det(v_r,v_t)|}{2}
\left(\int_{\mathbb R}\chi_r(\xi)^2\,d\xi\right)c_{Uj}
\int_{\mathbb R}\psi_{Uj}(v)^2x_{Uj}(v)t_{Uj,i}(v)\,dv.
\tag{2}
\]
The StrictCone condition is equivalent to invertibility of \(H_U\) and
strict positivity of both entries of \(H_U^{-1}T_U\). The source expresses
it by the signs of the two Cramer numerators times \(\det H_U\).
The component amplitudes contain the positive square roots of these
weights. Signed columns and their separate supports remain essential.

## 2. Exact output and its proof

The auxiliary variables are \(Y\in(\mathbb R/\mathbb Z)^2\) and
\(\theta\in\mathbb R/(2\pi\mathbb Z)\).
The double average first takes \((2\pi)^{-1}\int_0^{2\pi}d\theta\),
then integrates over the unit square in \(Y\).

The native radial and tangential profiles are
\(\chi_r(\xi)\psi(v)x(v)\) and
\(\chi_r(\xi)\psi(v)t_i(v)\). They undergo the prescribed affine slot
map, transverse stretch, periodization and integer covering. The covering
is \(Y\mapsto(3Y_1+Y_2,Y_1+5Y_2)\).
Within a given slot both components use the **same** factor
\(\cos(m_{Uj}\theta+\phi_{Uj}(Y))\).
The assembled fields contain the exact physical masks and the factors
\[
O_U=Q_{n+N}^{-a_h},\qquad
\varepsilon_U=Q_{n+N}^{h},\qquad
T_U=(Q_{n+N}/q)^{a_h+1/2}T_0.
\]
Writing them as radial component \(R\) and tangential components \(T_i\),
the theorem returns
\[
\boxed{\ \langle R T_i\rangle_{Y,\theta}
 =q^{-a_h-1/2}(T_0)_i=q^{-1-h}(T_0)_i,\qquad i=0,1.\ }
\tag{3}
\]
It is not a statement about all entries of the full covariance tensor or
about the covariance after adding the solenoidal corrections.

The proof was inspected through these supporting steps:

- Pulse.wave_covariance (114–158) uses quotient injectivity to remove
  cross-copy products, takes the angular square average \(1/2\), and
  computes the affine Jacobian and transverse stretch giving (2).
- SlotSystem.finite_wave_covariance (651–693) kills distinct signed
  labels' cross terms **pointwise**. Overlap of nonzero physical masks
  supplies the exact adjacency hypothesis. Distinct slots do not need
  distinct angular modes.
- diagonal_pair_reconstruct (722) uses the positive inverse weights to
  recover \(T_U\). finite_pair_covariance (832–873) assembles both signs.
- assembled_covariance (890–932) uses local finiteness of the masks to
  reduce the sum to one finite set independent of \(Y,\theta\).
- Finally,
  \[
  O_U^2\varepsilon_UT_U
  =Q_{n+N}^{-2a_h+h+a_h+1/2}q^{-a_h-1/2}T_0
  =q^{-a_h-1/2}T_0,
  \]
  and the exact tail partition gives \(\sum_U M_U(q,x)^2=1\),
  using \(q\le Q_N\).

The angular integral removes each diagonal phase before the outer
integration. The remaining outer profiles are continuous and compactly
supported. Thus arbitrary phase functions are compatible with this
iterated-average identity; no regularity of the unaveraged field follows.

## 3. Phase-replacement corollary

**Corollary at the leading covariance interface.** Fix all inputs in
Section 1. For any functions \(\gamma_{Uj}:\mathbb R^2\to\mathbb R\),
replace
\[
\widetilde\phi_{Uj}(Y)=\phi_{Uj}(Y)+\gamma_{Uj}(Y)
\tag{4}
\]
in both radial and tangential components of each slot. The resulting
assembled leading fields satisfy exactly (3), with all targets, masks,
slots, modes, pulse profiles and weights unchanged.

**Proof.** Update only the phases field in each PairData record. Every
other field and its proof is unchanged. Its matrix is definitionally the
old matrix, because PairData.matrix does not use phases. Hence the strict
cones are unchanged, as are all remaining hypotheses. Apply the exported
theorem to the updated family. Its pointwise cross-term cancellation
also remains unchanged. \(\square\)

This gives distinct fields, rather than just new notation for one field.
Choose one active signed slot and shift it by a constant
\(\lambda\in(0,\pi)\). Its positive weight and the nonzero corresponding
column of the invertible matrix ensure a nonzero profile.
The two cosine factors differ at some angle. No other active slot
cancels that change because of the same support separation.

The corollary also holds pointwise in an additional time parameter when
all inputs and (1) are supplied at that time. It remains an algebraic
family, not a statement about time evolution.

The [Lean companion](../../formalization/phase_covariance/PhaseCovariance.lean)
states this corollary in the Transformatics.PhaseCovariance namespace;
its [verification record](../../formalization/phase_covariance/README.md)
distinguishes local module checking from a replay of the imported proof.

## 4. Concrete smooth modulation: localization and all fixed time jets

Suppose the physical profiles are smooth on a fixed compact preterminal
time window. Choose \(\chi\in C_c^\infty((t_0,t_1))\), and modify one
slot by \(\gamma(t,Y)=\lambda\chi(t)\), independent of \(Y\).
The leading covariance is unchanged at every time. The component and
all its time jets agree with the original near both time endpoints.
Spatial support, angular periodicity and slot geometry are unchanged.

Put \(v(t)=e^{i\lambda\chi(t)}\). For \(m\ge1\),
\[
v^{(m)}=v
\sum_{\substack{k_1,\ldots,k_m\ge0\\\sum r k_r=m}}
m!\prod_{r=1}^m
\frac{(i\lambda\chi^{(r)}/r!)^{k_r}}{k_r!}.
\tag{5}
\]
For \(|\lambda|\le1\), this yields
\(\|\partial_t^m(v-1)\|_\infty\le C_{m,\chi}|\lambda|\);
the same statement for \(m=0\) uses \(|e^{is}-1|\le|s|\).
For a full complex curl component \(W=\nabla\times\mathcal A\), including
its actual spatial cutoff and curl correction,
\[
\nabla\times(v\mathcal A)=vW,
\]
and every mixed derivative satisfies
\[
\|\partial_t^m\partial_x^\alpha((v-1)W)\|_\infty
\le|\lambda|\sum_{r=0}^m\binom mr C_{m-r,\chi}
 \|\partial_t^r\partial_x^\alpha W\|_\infty.
\tag{6}
\]
Thus cutoff and curl derivatives are counted in \(W\).
For harmonic \(j\), replace \(\lambda\) by \(j\lambda\); fixed finite
harmonic ranges give corresponding finite constants.

For a fixed base \(u\), define the full complex linearization
\[
\mathcal L_u(W,\pi)=
\partial_tW+(u\cdot\nabla)W+(W\cdot\nabla)u+\nabla\pi-\nu\Delta W.
\]
Time-only multiplication gives the exact identity
\[
\mathcal L_u(vW,v\pi)=v\mathcal L_u(W,\pi)+v'W.
\tag{7}
\]
The pressure has been retained and multiplied as well.
For a full real velocity change \(w=\operatorname{Re}((v-1)W)\),
keeping the original pressure, the complete required force increment is
\[
\Delta f=\partial_tw-\nu\Delta w+
(u\cdot\nabla)w+(w\cdot\nabla)u+(w\cdot\nabla)w.
\tag{8}
\]
On a fixed smooth window these terms are smooth, with bounds from (6)
and the product rule, and vanish off the window. They include all mixed
nonlinear terms. These are finite-window identities only: they neither
identify this altered field with the source's full assembly nor establish
the uniform terminal-scale estimates used in its iteration.

## 5. The precise downstream obstruction

Consider the periodic heat shear
\[
u_\gamma(t,x)=e^{-\nu K^2t}\cos(Kx_1+\gamma(t))e_2,
\qquad K\in\mathbb N,\quad K\ge1.
\]
It is divergence free, self-advection vanishes, and its full averaged
stress is \(e^{-2\nu K^2t}e_2\otimes e_2/2\), independent of phase.
Yet its zero-pressure momentum residual is
\[
\partial_tu_\gamma-\nu\Delta u_\gamma
=-e^{-\nu K^2t}\gamma'(t)\sin(Kx_1+\gamma(t))e_2.
\tag{9}
\]
This is divergence free with zero mean, so Leray projection leaves it
unchanged and periodic pressure cannot absorb it.
For \(\gamma(t)=\delta\sin(Mt)\), the initial velocity is unchanged
and the phase change is at most \(\delta\), while the initial force norm
is \(\delta M\). Exact timewise covariance does not control the force.

The source exposes the same issue:
[LinearWaveResidual.remainder](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/LinearWaveResidual.lean#L111)
contains \(iK(D\Phi)a\), alongside slow transport, the base derivative,
slow pressure and viscosity. For a labelwise constant \(K\ne0\),
\[
e^{iK\widetilde\Phi}=e^{iK\Phi+i\gamma},\qquad
\widetilde\Phi=\Phi+\gamma/K,\qquad
D\widetilde\Phi=D\Phi+(D\gamma)/K.
\tag{10}
\]
The added rapid-phase residual is \(i(D\gamma)a\), not
\(iK(D\gamma)a\).

The actual gate is
[ActualPrimaryBounds.chart_defect_local](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ActualPrimaryBounds.lean#L1284),
used in actual_local_inputs (1428). It uses the actual native phase
geometry through ActualPhaseDefect.active_copy_defect_germ and
native_reduced_polynomial. The related abstract
PrimaryMaterialDefect.defect_class (379) requires the supplied
PhaseConstruction, native coordinates, scale identities, carrier
containment and polynomial bounds on all slow-coordinate jets.
None of these follows from (3).

With the source's reciprocal-frequency class of order \(+1/2\), a
sufficient **proposed condition for this one changed defect** is
\[
\|\partial^\alpha(D\gamma_n)(z)\|
\le C_m\varepsilon_n^{1/2}G_n(z)^{p_m},
\qquad |\alpha|\le m.
\tag{11}
\]
For every fixed \(m\), \(C_m,p_m\) must work for all bands, active patches
and points. The derivatives and \(G_n\) are the source's chart quantities.
Together with the reciprocal-frequency bound, (11) puts
\((D\gamma_n)/K_n\) in class \(+1\).

The covariance theorem supplies none of (11). A fixed smooth compact
physical-time modulation still needs its actual chart pullback estimated.
Bandwise smoothness does not imply the quantifiers in
[WeightedClasses.MemClass](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/WeightedClasses.lean):
\(\forall m\,\exists C_m,p_m\,\forall n,z\).
For example, \(\gamma_n(t)=\sin(2^nt)\) is smooth on each band but has
derivative \(2^n\) at zero, exceeding every fixed polynomial in a slow
factor \(n^2\).

Even (11) closes only one gate. Spatial phase changes alter the normal,
inverse normal, polarization, principal pressure and solenoidal correction.
CorrectionAnalyticStep.WaveData separately requires particularLinear and
signedLinear estimates as well as support, regularity and weighted
amplitude bounds. They must be rederived for the replacement.

## 6. Two limits on the algebraic freedom

Arbitrary orthogonal mixing between signed slots is not licensed. For
\[
H=\begin{pmatrix}-1&-1\\-1&1\end{pmatrix},\qquad b=(\sqrt2,1),
\]
the target is \(H(b_0^2,b_1^2)^T=(-3,-1)^T\).
A quarter-turn preserves \(|b|\) but swaps the squared entries, giving
\((-3,1)^T\). Mixing slot profiles can additionally violate support
requirements. The valid corollary changes phase within each slot,
without changing its amplitude weight.

An independently held companion need not preserve mixed covariance:
\(\langle\cos\theta\cos(\theta+\gamma)\rangle=\tfrac12\cos\gamma\).
[HarmonicCovariance.mixedBlockCovariance_mem](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/HarmonicCovariance.lean)
requires matching frequency, phase and angular frequency. Its curl-error
lemma separately counts primary–curl terms and the curl square. One cannot
pass the phase corollary through that interface while leaving a required
matched companion unchanged.

## 7. Reusable result and next estimate

The exact periodized leading two-component stress realization has
independent slotwise phase freedom, under the unchanged strict cones,
sign pairs, tail partition, supports and nonzero integer modes above.
Equations (4)–(6) provide a distinct smooth interior family with explicit
ordinary finite-window jet costs. This is a corollary derived here from
the published theorem, not a claim that the external authors used this
replacement.

The smallest useful continuation is one explicit spatially nonconstant
modulation in the actual native charts, with a proof of (11) and the
changed normal and pressure estimates. Full residual and correction
interfaces would then remain to be checked. No new Navier–Stokes
singularity construction is asserted.

## 8. Inspection record

Read the selected declaration and proof and the complete single-pulse,
finite-slot, sign-pair and locally finite assembly arguments. Read the
relevant SmoothCovariance, HarmonicCovariance, LinearWaveResidual,
PrimaryMaterialDefect, WeightedClasses and WaveInteractionBounds
interfaces. The independent downstream reviewer checked the direct
actual-chart dependency. The phase, derivative, force and signed-matrix
calculations above are exact derivations; no fluid simulation was run.

SHA-256 values of the inspected files under NavierStokes/:

| File | SHA-256 |
|---|---|
| PartitionedCovariance.lean | 2fa4f3f7a6d4780556abc587ce8306952e69aaaabdbeedfd6858e3a2a2c74863 |
| SmoothCovariance.lean | 1124f4ae69a3a8237081b7596c8dbeb8557afac52ff894f8c4a5a8af4d0580ee |
| HarmonicCovariance.lean | 0a0b784165cda7e91dcc40a4cb59915d229c4cc859bec8ad5e2a8dbc4cabad35 |
| LinearWaveResidual.lean | 4a80e08fef738be7032db1e465e3219d56e10da2e368ac06d1a8023ccc1e85dc |
| PrimaryMaterialDefect.lean | e80e28e25fa37b2c97da2bbdea43ee2785d5de4d8c552dd1989437be05f72225 |
| WeightedClasses.lean | aa1724190228aadedc8ae1cd4bee9efe7c35c5bceac234a18448894f78d21bd7 |
| WaveInteractionBounds.lean | dc321405c8f02c5c1c268b90314700eb967fbdc8defe8c105467fc171cfa0bea |
