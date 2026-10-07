# Independent review of the fixed finite-depth profile recurrence

8 September 2026. Reviewer: the separate AI agent
`audit_continuation_and_3d`. **PASS at the stated fixed-finite-depth written
analytic scope**, after the scaled Sobolev embedding correction recorded
below. This is not external expert acceptance, a formal PDE certificate,
or a complete Navier–Stokes proof.

## Exact source reviewed

[finite-depth-profile.md](finite-depth-profile.md)
with SHA-256
`0db98f52c48860df594ce932838071be980349c604c6135f50be03700c6c76d1`.
The reviewer reread this exact version after its embedding correction.
No change to that source was made by the reviewer.

The proof uses the actual first-stage q, phase and full forced-profile
identity from [the localized-profile construction](../navier-stokes/localized-profile.md),
and the sharp history and continuation framework of
[the logarithmic host](../navier-stokes/logarithmic-host.md). This review
checks the new recurrence and its stated use of those inputs. It is not
a fresh independent proof of every upstream analytic result.

## What was checked

**Exact remainder.** Expand the residual of
q+m+Z+delta m+W about q+m+Z. The linear mean equation cancels the phase
mean r_j^0, and the tangent profile equation cancels R_j-r_j^0. The
additional forcing (delta m dot xi/k) partial_s a_j cancels precisely the
fast principal part of delta m dot grad^k Z. Its uncancelled part is
(delta m dot xi) partial_s r_(a_j), together with the slow derivative
already shown in equation (7). The old/new mean, old/new wave and
new/new quadratic terms are all present. No tangency of the global mean
was assumed. The full longitudinal pressure numerator xi dot H_j is
retained.

**Norms and global tails.** The source now states the correct embedding

    d^r ||D^r v||infinity <= C S_(r+2)(v).

The earlier sentence omitted d^r. The subsequent recurrence already
charged each slow derivative by d^(-1), so correcting that sentence does
not change its residual powers. The norms use global unnormalized L2 for
the phase-independent mean; neither that mean nor its pressure is assigned
the compact wave volume. Products of mean tails use a pointwise bound on
one factor and a global L2 bound on the other. Nonzero phase forcings stay
in the smoothly extended transported chart.

**One power gain per round.** A residual of point-amplitude order
k rho^(j+1) gives both increments of that order, up to the stated subpower
factor. The new mean's added fast forcing has factor |a_j|/k, with no
negative power of h. The remaining linear curl, pressure, tangent-wave
cross and normal-curl terms cost k/d=rho. The old mean's fast advection
costs |m_j|/k=O(rho); the new mean's fast advection of the new wave costs
rho^(j+1). Slow mean products are smaller. The ordinary viscous factors
epsilon/k^2, epsilon/(kd), epsilon/d^2 are h, h^(5/4), h^(3/2), up to nu,
and hence smaller than rho=h^(1/4). Derivatives of xi and its inverse
enter the finite subpower factor, not a further uncontrolled exponential.

**Finite derivative hierarchy.** The mean estimate uses differentiated
solenoidal energy about q; pressure disappears in these pairings. The
profile estimate retains each Fourier mode's nonnegative heat damping.
Because the central clock is spatially constant, slow differentiation
does not generate spatial derivatives of that clock. The proposed eight
additional derivatives per prior round leaves room for the three slow
derivatives in the residual, phase derivatives and pointwise recovery.
The first-stage high-order proof can use a larger fixed Sobolev index
without changing its original datum. The strict scaled C-r error power
1/4-(r+3/2)/M stays positive at the stated choice of M.

**Initial datum and leading history.** Every correction starts at zero,
including its curl lift, so U_J(0) is unchanged. For each fixed J, all
new correction-gradient integrals tend to zero as h tends to zero. Their
constants may depend on J, but they do not multiply the leading
B eta ell^2 history. Thus the fixed H12 energy constant and the leading
clock loss can be kept separate from the finite-order correction
constants. No bound polynomial in accumulated strain for arbitrary full
PDE errors has been used.

**Actual-solution comparison.** The approximation uses only the known
first-stage q. It can therefore be constructed before extending the full
Q_h; the relative-energy/H12 bootstrap is not circular. When the displayed
error exponent has a positive fixed margin, interpolation improves the
gradient bootstrap and strong continuation supplies the claimed actual
finite interval. A fixed larger eta changes subpower constants in q's
O_eta(ell^(9/8)) clock. It requires a correspondingly large fixed J for
the full comparison; neither parameter is allowed to grow with h.

## Independent arithmetic checks

Exact rational arithmetic verifies

    k rho^(J+1) d^(3/2) = h^((29+2J)/8),
    [(29+2J)/8](19/24)-(117/8)(5/24)=(19J-17)/96,
    [(29+2J)/8](3/4)-(117/8)(1/4)=(3J-15)/16.

These give J=1's gradient power 1/48 and J=3's power 5/12 before the
separately stated clock loss. The H3 estimate controls the Fourier-summed
gradient by Fourier Cauchy–Schwarz; its weights are integrable in three
dimensions with constants uniform on the stated expanding tori.
Arithmetic checks verify these formulas, not the full analytic argument.

## Limits of the verdict

The result improves approximation of the same finite actual evolution.
It supplies neither a signed nonzero new receiving component nor an
infinite compatible initial datum. It does not make a small rescaled
residual into an all-orders smooth physical force: physical derivative
conversion, baseline forcing, activation and reset remain separate.
No conclusion is certified for J tending to infinity, J depending on h,
eta depending on h, or one fixed datum approaching a singular time.
ROOT, E-prime and FORCED-D remain open.
