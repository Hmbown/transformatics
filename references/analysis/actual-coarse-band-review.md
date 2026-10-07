# Independent review of the actual intermediate-band calculation

8 September 2026. **PASS at the bounded written scope below.** No
load-bearing gap was found in the new implication. This review uses the
previously reviewed logarithmic host, full-profile identities and signed
postfocus theorem as inputs. It independently checks the new exact-linear
approximation, the complete annular estimates and the remainder's small
current-window clock. It is not a fresh certification of the entire
upstream NS construction, external expert acceptance or a formal PDE
certificate. ROOT, E-prime and FORCED-D remain open. No DNS, source edits,
canonical edits or git mutations were made.

Reviewed source:
[actual-coarse-band.md](actual-coarse-band.md),
SHA-256

    4ce7d677e3677995f74010515f8e0f817bc0b82695cddfb3a8bcd91967a13cb4

The bounded check script was also read and rerun:
[nse_coarse_band_linear_checks.py](../../experiments/nse_coarse_band_linear_checks.py),
SHA-256

    8351e29d339d6f42268086670eea680028fb6edbc031e9021abf8dc2e32a2859

## 1. What the implication actually proves

The fields remain Q, actual first-stage q, exact homogeneous viscous
linearization Z about q, and Ncal=Q-q-Z. Z starts from the full original
receiver curl datum. The fixed profile, physical viscosity, eta, original
focus and observation time are unchanged. The annular multiplier B_h is
an observation filter; no Fourier tail is deleted from the datum.

The signed postfocus pairing already established a lower bound for Ncal.
The new argument proves that q and Z are smaller in the entire relevant
annulus, so that pairing survives in B_h Q itself. It also bounds the
initial full-Q annulus more sharply than the endpoint lower bound.

All exponents and derivative orders are fixed before h tends to zero.
The family still changes its original datum with h. The conclusion is
neither generation above the finest supplied scale nor an infinite
trajectory. Full-flow dominance is asserted only in the stated annular
test, not for the unfiltered velocity or gradient at a point.

## 2. Exact linear correction, pressure and phase mean

Using the notation of the full-profile identity, let H_lin=R[a;0] and
solve the forced profile equation from zero for g_lin. Every term of
R[a;0] is linear in a, with coefficients independent of the auxiliary
phase. A phase derivative has zero mean, and the inverse phase derivative
is the prescribed zero-mean primitive. Spatial and material derivatives
commute with taking this auxiliary phase mean. Thus H_lin has exactly
zero phase mean, including the heat mismatch, curl commutator and slow
pressure derivative. Tangency and zero phase mean persist for g_lin.

The pressure in source (6) contains both 2 xi dot A_q g_lin and
xi dot H_lin. Its leading cancellation is

    2xi(xi dot A_q g)/|xi|^2-Pi_xi H
       -xi[2xi dot A_q g+xi dot H]/|xi|^2 = -H.

Consequently the primary residual is canceled exactly and the remaining
linear residual is R[g_lin;H_lin], as in source (7)-(8). No quadratic
stress or generated mean equation belongs in this auxiliary linear
construction. There is also no omission of a possible coarse component
of the exact Z: the whole global error Z-Z_app is estimated separately.

The evaluated profiles are genuine curls. They remain real, solenoidal
and spatially mean zero after extension of their compact potentials.
g_lin(0)=0 gives Z_app(0)=z_0 exactly, including its original curl term.
Zero auxiliary phase mean and zero spatial mean are different facts;
neither implies that the evaluated packet has zero coarse Fourier tail.
The source uses oscillatory integration, not that incorrect inference.

## 3. Complete residual and finite derivative budget

With rho=k/d, the primary profile has size k H_h^C. Direct substitution
in the full residual gives H_lin of size k rho H_h^C. The forced profile
equation has scalar dissipative Fourier factor and matrix growth governed
by actual q, so g_lin has the same size after another fixed H_h power.

In R[g_lin;H_lin], the material curl and slow pressure terms cost a
further k/d. Material differentiation is eliminated using the g equation,
D xi=-A_q^T xi and the exact material-curl commutator. This substitution
uses H_lin itself, not an unproved time derivative of H_lin or A_q.
The slow Laplacian, mixed viscosity and curl viscosity terms are smaller:
epsilon/k^2, epsilon/(kd), epsilon/d^2 have powers 1, 5/4 and 3/2.
The central heat mismatch also has a strictly positive extra power using
the existing whole-envelope covector comparison. Hence

    integral ||E[R[g_lin;H_lin]]||_2 dt
       <= k rho^2 d^(3/2) H_h^C = h^(31/8) H_h^C.

The derivative count closes with the stated finite inputs. To obtain
Z_app through physical order 12, the curl lift needs g_lin through slow
order 13, plus finite phase derivatives. Its forcing through slow order
13 uses at most 16 primary slow derivatives in the first residual.
The supplied primary order 18 and q C24 are sufficient. The second
residual needs only its L2 size here. The two later integrations by parts
need only two further amplitude derivatives, already within these bounds.
The fixed phase A80 budget covers the phase derivatives and mode sums.
No order depends on h and no all-order estimate is used.

Subtracting the approximate and exact linear equations yields a global
solenoidal energy estimate for E_Z=Z-Z_app. The entire pressure difference
drops out of that pairing; the transport term cancels and the stretching
coefficient is bounded by ||grad q||_infinity. The actual q clock is
O(ell^(9/8)), so

    sup ||E_Z||_2 <= h^(31/8) H_h^C.

No compact support is assigned to E_Z or to the pressure of exact Z.

## 4. Exact-linear H12 and interpolation

For the finite norm sum of k^j||D^j Z||_2, 0<=j<=12, the actual q
jets give transport commutator coefficients

    k^(j-1)||D^j q||_infinity
       <= C m_h(k/h)^(j-1),                 j>=1.

Differentiating the stretching term gives

    k^j||D^(j+1)q||_infinity
       <= C m_h(k/h)^j,                     j>=0.

Since k/h=h^(1/2), both are bounded by C m_h. The top undifferentiated
transport cancels against a solenoidal derivative of Z; pressure is
orthogonal to that derivative; diffusion is nonpositive. These facts
justify the closed weighted estimate using q through order 13 only.

The full initial curl has weighted norm h^(27/8) H_h^C. Thus

    ||Z||H12+||Z_app||H12 <= h^(-117/8) H_h^C.

The Z_app term follows from the profile jets just counted. The uniform
expanding-torus Fourier split then gives

    ||grad E_Z||_infinity <= h^(1/48) H_h^C,
    ||E_Z||_infinity      <= h^(25/16) H_h^C.

The exact arithmetic is
(31/8)(19/24)-(117/8)(5/24)=1/48 and
(31/8)(7/8)-(117/8)(1/8)=25/16. The energy clock here is q alone;
the larger full-Q clock cannot be silently substituted into this step.

## 5. Uniform annular estimates and the full initial band

The radial filter is a fixed smooth symbol of K/kappa_h. Its Euclidean
kernel is Schwartz with a uniform L1 norm after scaling, and periodization
does not increase that norm. It can be chosen equal to one on both signs
of the postfocus cone, uniformly in the terminal frame.

On a torus of side 2pi L, unnormalized Fourier inversion contributes
L^(-3), while an annulus contains O((L kappa_h)^3) modes. Fourier
Cauchy-Schwarz and Parseval therefore give the uniform estimate

    ||B_h E_Z||_infinity
       <= C kappa_h^(3/2)||E_Z||_2 <= h^2 H_h^C.

There is no cone cost in this estimate: B_h covers the whole annulus.

For the evaluated approximation, every profile mode n is nonzero.
For K in this annulus, the full phase nS/k-K dot x has gradient bounded
below by |n|/(2k H_h^C), because k kappa_h H_h^C tends to zero. Thus two
integrations by parts with this full phase are legitimate on the compact
chart. The smooth amplitude vanishes before its boundary. The inverse
covector and phase derivatives have the supplied finite bounds; each
integration costs at most d^(-1) H_h^C and gains k/|n|. The curl terms
and g_lin obey the same estimate. Summing the modes yields

    |Z_app_tilde(K)| <= C k d^3(k/d)^2 H_h^C.

Absolute Fourier inversion on the annulus multiplies this by kappa_h^3.
The result is again h^2 H_h^C. This is a bound for the actual evaluated
profile, not just for its formal phase average.

The independent q H12 bound is h^(-41/4) H_h^C. Its annular estimate is

    ||B_h q||_infinity
       <= C kappa_h^(3/2-12)||q||H12
       <= h^(23/8) H_h^C.

This uses the sharp actual q clock and global norms, including its
pressure-generated tails. At time zero Z_app=z_0 exactly, so the same
two-integration estimate bounds the full initial receiver without an
E_Z term. Adding q proves the initial velocity band bound h^2 H_h^C.
One extra annular derivative costs kappa_h, yielding h^(3/4) H_h^C.
The initial datum's Fourier tails are retained throughout.

## 6. Signed pairing and the full-Q strain bound

Let f be the already scaled, periodized postfocus cone kernel. Since
B_h is real and even and equals one on its Fourier support,

    <r dot Q,f> = <B_h(r dot Q),f>.

The q+Z pairing has absolute value at most
delta_h^(-4)(h^2+h^(23/8)) H_h^C. The reviewed positive Ncal pairing
has size at least c eta^(-1)h^(7/4)ell^(9/8)H_h^(-4A).
The gap 2-7/4=1/4 dominates every fixed cone and majorant cost. Therefore
the full-Q pairing stays positive for sufficiently small h.

Scalar duality proves source (2) for the annularly filtered full Q.
Using Delta v=2 div S(v) for solenoidal v=B_h Q, and moving the inverse
Laplacian to the same band-supported test, gives source (3). Its tensor
kernel has L1 norm C kappa_h^(-1)delta_h^(-4). This is a band calculation,
not an L-infinity Korn estimate. The initial-to-endpoint exponent gap
for the strain bound is also 3/4-1/2=1/4. Consequently the endpoint
lower bound divided by the established initial upper bound diverges.
This does not specify a monotone growth history inside the interval.

## 7. The exact remainder has a vanishing present clock

The source uses the exact decomposition

    Ncal=(Q-U1)+m1+E[W_gnl]-E[W_glin]-E_Z.

The actual nonlinear tracking error has gradient at most h^(1/96).
The mean has C1 size h^(1/2)H_h^C, the two evaluated profile corrections
have C1 size h^(1/4)H_h^C, and the exact-linear error has gradient
h^(1/48)H_h^C. Since H_h is subpower, their sum is bounded by
C h^(1/96) on the entire existing interval.

The velocity part also closes. For Q-U1, its known small global L2 norm
and gradient bound imply the displayed local interpolation inequality
with exponents 2/5 and 3/5. Optimizing a radius no larger than one gives
uniform constants on all these tori, with the additive L2 term covering
the boundary case. This velocity bound is much smaller than h^(1/96).
All remaining velocities are controlled by the correction bounds and
the h^(25/16) exact-linear error. Thus the stated full C1 bound follows.

Finally t_eta=O_eta(log ell), so the integral of ||grad Ncal||_infinity
is at most C h^(1/96)log ell, which tends to zero. This is compatible
with the nonzero annular lower bound, whose h exponent is much larger.
It bounds the remainder's own present contribution to a gradient clock;
it does not imply stability of the full flow map under the much larger
q and Z clock, or exclude a future interaction.

## 8. Negative controls and remaining boundary

The following controls distinguish the valid argument from shortcuts:

* Deleting xi dot H_lin from the pressure leaves the nonzero longitudinal
  residual xi(xi dot H_lin)/|xi|^2. An independent exact rational example
  checked this with a nontransverse H_lin.
* A zero phase mean does not itself remove coarse Fourier leakage after
  evaluation. The two integrations by parts and the global E_Z bound
  are necessary for the stated inference.
* Without any phase integration, the annular bound has only power h^(3/2).
  One integration gives h^(7/4), merely matching the signed signal before
  its subpower losses. The second produces the required h^2 margin.
* An unweighted high-order estimate using the raw q derivative suprema
  would lose the small scale factors. The factors (k/h)^(j-1) and
  (k/h)^j are explicitly present in the weighted energy calculation.
* A lower bound for Ncal alone cannot exclude cancellation by q+Z.
  Their independent full-annulus upper bounds are used before passing
  the signed pairing to Q.
* Small Ncal does not make the full Q clock small: q and Z remain in
  the exact decomposition.

All 16 author algebra checks passed when rerun. Additional exact
symbolic calculations checked the complete longitudinal-pressure
cancellation and its deletion control. Independent rational arithmetic
checked residual, interpolation, annulus and initial-band exponents,
including the failure of the one-integration shortcut. These finite
checks support the written audit; they do not certify the upstream PDE
existence theorem or an infinite trajectory.

No source correction is required by this review. The next unresolved
issue is a usable later coupling of the generated band, with its full
shape and surrounding flow retained. A detectable band with a vanishing
current strain clock does not itself establish another amplification
stage or close either Navier–Stokes track.
