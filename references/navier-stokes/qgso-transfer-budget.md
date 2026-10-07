# Strain transfer and the rung-integrated dissipation budget

**Standing:** ROOT, `(E′)`, and Q-GSO averaged noncollapse remain OPEN.
The unconditional closure attempted here does not follow. What is proved
below is a periodic spatial identity, an exact square-completion, a
conditional continuation criterion, and the failure of the resulting
scalar estimates to exclude either escape ledger. Exact Fourier checks
verify the identities; they are not an evolution or singularity proof.

Pins: `experiments/nse_qgso_transfer_budget.py`,
`tests/test_nse_qgso_transfer_budget.py`,
`artifacts/enstrophy_sup/nse_qgso_transfer_budget.json`;
node `nse-qgso-transfer-budget`.

## 1. The spatial input and its provenance

Evan Miller proves the orthogonality
`<-Delta S, omega tensor omega> = 0` in Theorem 3.1 of
[On the interaction of strain and vorticity for solutions of the
Navier–Stokes equation, arXiv:2407.02691v2](https://arxiv.org/html/2407.02691v2).
It gives a globally regular strain-vorticity model and conditional
criteria for the full equation. The model theorem is **not** a theorem
of unconditional Navier–Stokes regularity. The identity is credited to
Miller; this note derives its periodic use and the estimates below.

Work with a smooth, unforced, divergence-free solution on `(2pi T)^3`,
viscosity `nu > 0`. All inner products in the proofs are **physical
integrals**, including the volume. Let

```text
S = sym grad u,     omega = curl u,     L = -Delta S,
Q = <S,S>,          D = <S,L>,          Z = <L,L>,
E = (1/2) integral |u|^2,               E' = -2 nu Q.
```

The scalar escape parameter `L` used later is unrelated to this tensor.
Use a positive starting time if only H1 initial data are assumed, so
these quantities are finite by smoothing. The zero-strain solution is
trivial; otherwise `Q,D > 0` on the interval under consideration.

For completeness the periodic orthogonality follows directly:

```text
<L, omega tensor omega>
  = <Delta u, (omega . grad) omega>
  = <Delta u, (curl omega) cross omega + grad(|omega|^2/2)>
  = 0.
```

Here `Delta u = -curl omega`; the cross term vanishes pointwise and the
gradient term vanishes by integration and incompressibility. Periodic
boundary terms vanish. Also `<L, Hess p> = 0` by two integrations by
parts. These are spatial facts, not scalar growth assumptions.

## 2. Two different orthogonalities in the full equation

Let `P_st` be the L2 orthogonal projection onto strains of mean-zero
periodic solenoidal vector fields. Define the **actual tensor**

```text
C = P_st[(u . grad)S + S^2 + (3/4) omega tensor omega].
```

The full NS strain equation has the exact form

```text
S_t = -nu L + (1/2) P_st(omega tensor omega) - C.       (1)
```

Transport integration and Betchov give

```text
<S,(u . grad)S> = 0,
<S,omega tensor omega> = -(4/3) integral tr(S^3),
<S,C> = 0.                                           (2)
```

Consequently (1) yields both budgets

```text
Q' = <S,omega tensor omega> - 2nu D,
D' = -2nu Z - 2<L,C>.                                (3)
```

The vorticity forcing is orthogonal to `L`, whereas `C` is orthogonal
to `S`. Confusing those two statements would incorrectly make `D`
monotone for the full equation.

An independent local-contraction expression checks (3). Write

```text
A = integral sum_(k,l) S_kl <partial_k S,partial_l S>_F,
B = integral sum_k tr[S (partial_k S)^2].
```

One integration by parts in the transport term gives `A`: its gradient
Gram matrix is symmetric, so the antisymmetric velocity gradient drops
out. Differentiating `S^2` gives `2B`. Thus

```text
D' = -2nu Z - 2A - 4B.                               (4)
```

Pressure and the explicit vorticity-square contraction have disappeared;
the signed transport and strain-gradient alignment remain.

## 3. Exact square-completion and the pumping cost

Set `X = L - (D/Q)S`. Then

```text
<X,S> = 0,       ||X||_2^2 = Z - D^2/Q >= 0,
<L,C> = <X,C>.
```

Substitute into (3) and complete the square, without an estimate:

```text
D' + 2nu D^2/Q + 2nu ||X + C/(2nu)||_2^2
    = ||C||_2^2/(2nu).                               (5)
```

Dropping only the nonnegative square proves

```text
D' + 2nu D^2/Q <= ||C||_2^2/(2nu).                    (6)
```

In particular every time interval `[a,b]` satisfies the integrated
**pumping cost**

```text
integral_a^b ||C||_2^2 dt
    >= 2nu [D(b)-D(a)] + 4nu^2 integral_a^b D^2/Q dt. (7)
```

This keeps a dissipative term that ordinary Young's inequality without
using `<S,C>=0` drops. It is a cost in the actual redistribution tensor
`C`. There is no established finite energy budget for `integral ||C||^2`.
Replacing that quantity by a bounded multiple of `integral Q` would be
an additional, presently unproved, estimate.

The other immediate sharpening is

```text
|<L,C>| <= sqrt(Z-D^2/Q) ||C||_2.                     (8)
```

With `delta^2 = 1-D^2/(QZ)`, `D'>0` requires
`delta ||C||_2 > nu sqrt(Z)`. If `delta=0`, the spatial identities
force zero enstrophy production and `D'=-2nu Z`: a single Laplacian
shell cannot be a growing NS strain state. This does not bound `delta`
away from one, or force it to vanish on a hypothetical singular ladder.

## 4. What bound would close the argument

Define the signed upper clock, with its negative part retained,

```text
R(t) = ||C(t)||_2^2/(2nu D(t)) - 2nu D(t)/Q(t),
K(t) = integral_(t0)^t R(s) ds.
```

Equation (6) implies `log(D(t)/D(t0)) <= K(t)`. Therefore

> If `sup_(t<T) K(t) < infinity`, the smooth solution continues past
> `T`. The hypothesis is OPEN for general NS solutions.

Indeed `D` is bounded; periodic Poincare bounds `Q`, and the standard
H1 continuation criterion applies. A more permissive necessary
condition is available specifically at Q-rung endpoints. Integration
by parts and Cauchy give the physical energy interpolation inequality
`Q^2 <= E D`, while `E(t) <= E(t0)`. Hence if
`Q(b_j)=q_* rho^j`, every such endpoint obeys

```text
K(b_j) >= 2j log(rho) + log(q_*^2/(E(t0)D(t0))).      (9)
```

An upper bound `K(b_j) <= 2j log(rho) - h_j + O(1)` with
`h_j -> infinity` would therefore rule out an infinite Q ladder.
No such bound was proved. The integrations in this section cover
**all intervening times**, not only positive-Q subsets or rung windows.

The exact, generally smaller clock is

```text
integral_a^b [-2<L,C>/D - 2nu Z/D] dt
    = log(D(b)/D(a)).                                (10)
```

This identity alone is not a closure. In particular a fixed excess
exponent over two is not a necessary escape condition; the slow ledger
below has `log(D_next/D)/log(rho) -> 2` from above.

## 5. Blob-first falsification of the attempted closure

Before new DNS, both escape ledgers were extended to include `D,Z,E`
and the norm constraints in (5)–(8). The following are **scalar data**,
not actual spatial tensors or Navier–Stokes solutions.

For the geometric ledger put `nu=1`, `s=T-t`, and

```text
Q=s^-1/2, M=8/s, E=4sqrt(s), D=s^-3/2, Z=2s^-5/2,
P=Q'+2D=(5/2)s^-3/2,
||C||_assigned^2=(121/16)s^-5/2.
```

Then `E'=-2Q`, `Q^2 <= ED`, `D^2 < QZ`,
`P/(MQ)=5/16 < c_B`, `M'/M^2=1/8`, and (6) holds with a
positive margin `(9/16)s^-5/2` after multiplication by `2nu`.
The two orthogonal pairings admit the explicit abstract Gram witness
at `s=1`

```text
S=(1,0), L=(1,1), W=(5/2,-5/2), C=(0,-11/4),
L.W=0, S.C=0,
2 S.(-L+W/2-C)=1/2, 2 L.(-L+W/2-C)=3/2.
```

This is a two-dimensional algebraic witness, **not a fixed-Laplacian
evolution or a realization of `W=omega tensor omega`**.
The actual scalar Q-rung prices are

```text
Hbar_j = sqrt(s_j)(1-rho^-1)/(8 log(rho)),
```

which have a finite geometric sum. The upper clock from section 4
costs `(57/16)log(rho)` per rung; the exact log-D clock is
`3log(rho)`. Both exceed the threshold in (9), so neither gives a
contradiction. Adding a nonnegative constant to `E` changes no energy
derivative. On `0<s<=1/4` the listed moments also satisfy the mean-zero
torus Poincare inequalities. No spatial existence is inferred.

For slow escape use `r>=0`, `L>=32`, `x=r+L`, and

```text
Q=e^r, M=e^r x^2, dt/dr=2/M,
E=4/x, D=e^(2r)x/2, Z=2D^2/Q,
||C||_assigned^2=(D^2/Q)(x+5/2)^2.
```

Again `E'=-2Q`, now `ED/Q^2=2`, and
`(Q'+2D)/(MQ)=1/2+1/x < c_B`. Equation (6) holds.
The prices remain `1/[(L+j log rho)(L+(j+1)log rho)]`, with finite
telescoping sum. The exact log-D increment is
`2log rho + log(1+log rho/x)`, while the upper-clock density is
`R dt/dr = x/2+5/2+9/(8x)`. These permit escape as well.

**Conclusion of this attack:** the new spatial cancellation is useful,
but its norm-and-moment consequences (6)–(9) do not rule out either
scalar escape. Any successful use must establish additional control of
the actual signed tensor `C` along NS evolution. Neither a universal
sign nor an automatic small-transfer cap follows from orthogonality.

## 6. Exact field check and frozen rung measurements

The pinned real solenoidal polynomial is

```text
u_a = a[(0,1,1)cos x + (1,1,-1)cos(y+z)
          + (1,-2,1)sin(x+y+z)].
```

Exact rational Fourier convolution, with no grid or maximizer search,
checks both budgets against the independently differentiated
velocity-form projected NS RHS. For `a=-1`, `nu=1/100`, its moments
**divided by `(2pi)^3`** are

```text
Q=13/2, D=17, Z=47, Q'=29/25, D'=303/50,
||C||^2=2425/72, delta^2=33/611.
```

Thus an actual smooth periodic NS **initial tangent** has positive
Q and D production while satisfying both orthogonalities. Changing
`a` to `+1` reverses the inviscid productions. There is no universal
pointwise sign that discards the transfer term. No completed rung,
long-time behavior, or continuum-max claim is made from this field.
The separate existing spectral velocity RHS at N=16 and N=24 also
reproduces these integrated moments after a raw divergence check.

The saved floor-slack source contains Q and D at every recorded sample.
Reusing its frozen rung endpoints and linear interpolation gives:

| Frozen family | Q rungs | `alpha_D=log(D_b/D_a)/log(Q_b/Q_a)` |
|---|---:|---|
| kida, nu=0.009, N=64 | 3 | 3.744, 3.614, 3.757 |
| two_scale_beltrami, nu=0.005, N=96 | 7 | 5.927, 4.629, 3.326, 2.411, 2.073, 2.537, 2.323 |

These are finite post-hoc measurements, with no new acceptance or
asymptotic verdict. The source did **not** save Z or the transfer tensor;
the separate integrals in (7)–(10) and the spectral variance cannot be
recovered. They are stored as missing, not zero or estimated by an
unjustified surrogate. The source SHA is recorded and no DNS is rerun.

## 7. Next analytic obligation

The remaining candidate is signed, cumulative transport control,
accounting for the actual relation of `C` to strain and vorticity.
Pressure-only growth rates, an unsigned per-instant dissipation floor,
or the scalar moments here do not supply it. Before another campaign,
derive a proposed inequality which the explicit ledgers cannot satisfy
and identify the spatial step that proves it for NS. The missing
step has not been established in this session.

## 8. Local verification receipt

- New instrument: **44 exact algebra/arithmetic checks**, all green.
- Focused tests: **34 passed**, covering `test_nse_qgso_transfer_budget.py`,
  `test_nse_qgso_prefix_audit.py`, and `test_nse_growth_set_osgood.py`.
- Ruff on the new instrument and tests: green.
- Coverage audit: **OK, 350 nodes**, with the same three pre-existing
  single-attack-path warnings (`h2clock`, `ksplit`, `phoctave-deep`).
- The campaign JSON/NPZ, floor-slack and floor-sharp receipts, and both
  frozen pressure-Hessian receipts are byte-identical to `e59f78b9`.

These are local checks. No hosted CI, new DNS, unconditional regularity,
or singular trajectory is claimed.
