# Independent review of the growing-window nonlinear remainder

8 September 2026. **PASS as a bounded consequence of the reviewed
Gevrey background, uniform profile operators and growing-window
continuation.** This is a written AI-agent review, not a formal PDE
certificate or external expert acceptance. No new global Navier--Stokes
result, research DNS or canonical source edit is involved.

Reviewed source:
[growing-window-remainder.md](growing-window-remainder.md),
SHA-256

```text
a54882be5ab52cdf987285bdbd579b6cc8f9a518eb6c8aa255e78dd35d00bc42
```

This review checks the new linear correction, exact-remainder subtraction
and Fourier-tail argument. It uses the separate background and operator
reviews for their uniform estimates; it does not replace those audits.
The fixed Gevrey-2 profile choice is essential to the explicit schedule.

## 1. Exact linear construction and initial datum

The source uses the actual q and the exact viscous linear receiver Z,
both with their existing data. Subtracting their equations from full Q
gives the stated equation for N_gen=(Q-q)-Z with forcing
-div((Q-q) tensor (Q-q)). No normal, phase mean or global pressure
component is removed from that exact remainder.

The forced-profile identity can be checked directly. In its principal
terms, the amplitude equation contributes

    2xi(xi.A v)/|xi|² - H + xi(xi.H)/|xi|².

The fast derivative of p_v cancels both longitudinal terms, leaving
-H. Expanding the full viscous operator on v+k r_v then gives exactly
the local/central diffusion mismatch, the material-curl remainder,
the slow pressure derivative, and the four slow/mixed viscous terms
listed in source (6). The longitudinal pressure xi.H is indispensable.

This residual is linear in v and H, with coefficients independent of
the auxiliary phase. It therefore preserves zero formal phase mean.
This fact does not identify phase mean with the spatial integral of an
evaluated profile. The primary residual H_0, the three forced corrections
and their complete residuals telescope to H_3. There are no quadratic
wave products or omitted mean equation in this linear construction.

Each correction vanishes initially as a spatial function; its curl lift
therefore vanishes too. Z_3 starts at exactly z_0. The compact chart is
used for approximate wave factors only. The exact Z and its pressure
may have global tails, which the subsequent global energy estimates retain.

Material differentiation of the curl potential uses D_t xi=-A^Txi and
the actual forced amplitude equation. It needs spatial derivatives of
H and q, not an unestimated time derivative of q. The spatially constant
central heat rate creates no spatial coefficient derivatives.

## 2. Three fixed corrections and global exact-Z error

The 54,46,38,30 reservation leaves sufficient slow and phase derivatives
after three rounds. The larger common N=N0+8J and the fixed larger
background reservation cover the primary residual and coefficient jets
needed to start this hierarchy. Evaluated H12 needs at most one further
amplitude derivative for its curl lift; order 30 leaves ample room.
The full phase-Wiener norms keep every phase index.

Each fixed residual round gains rho=k/d, with epsilon/k²,
epsilon/(kd) and epsilon/d² smaller. Thus H_3 has normalized amplitude
k rho^4 times a fixed power of M_N. There are only three linear rounds,
so that exponent is independent of J. Multiplying by the genuine wave
volume factor d^(3/2) and the time factor proves

    integral ||E[H_3]||2 dt <= h^(35/8) M_N^C.

The exact linear error equation has energy growth controlled by
integral ||grad q||infinity <= C I_q, already a fixed power of M_N.
It does not pay the much larger full-Q clock. Pressure drops in the
global solenoidal pairing, and diffusion is nonpositive. This gives
the complete L2 error, including all global pressure-generated tails.

For high regularity, the fixed twelve-derivative norm weighted by k^r
has transport coefficients bounded by

    C_12 m_h [(k/h)K_N]^(i-1),

and stretching coefficients by the corresponding ith power. Since
(k/h)K_N=h^(1/2-o(1)), the sum over the fixed thirteen q orders is
bounded by C_12 m_h, with C_12 independent of N and J. Fixed-order
linear Galerkin/energy arguments therefore supply actual Z on the
already established q interval. Its initial weighted norm is at most
k d^(3/2) M_N^C, so conversion back to H12 gives

    k^(-12) k d^(3/2) = h^(-117/8).

The approximate Z_3 has the same H12 scale by its reserved profile
bounds. Uniform expanding-torus Fourier interpolation then gives

    gradient exponent = (19·35-5·117)/192 = 5/12,
    velocity exponent = (7·35-117)/64 = 2.

The low-frequency interpolation terms are smaller. At only two
corrections, the gradient exponent would be 7/32<1/4, so that proof
would not establish the claimed h^(1/4-o(1)) remainder scale.

## 3. Subtracting both approximations

The uniform nonlinear recurrence sums its corrections geometrically,
with scaled amplitude at most k rho M_N^C and evaluated C1 size at
most rho M_N^C. These constants do not grow with the number of rounds
after the common M_N is fixed. The three linear corrections obey the
same bounds. Global nonlinear means use their scaled global Sobolev
norms; no compact support is assigned to their tails.

The exact four-term identity (13) in the source now gives

    sup ||N_gen||C1 <= h^(1/4)M_N^C+h^eta,
    sup ||N_gen||infinity <= h^(7/4)M_N^C+h^eta.

The linear errors h^(5/12) and h² are smaller than the respective
correction bounds. The full nonlinear error has the needed velocity
bound as well: with C12>=1, its velocity interpolation has a no-larger
clock coefficient and a larger favorable J coefficient than its
gradient interpolation. The strict continuation margin absorbs fixed
constants when forming the C1 norm.

Multiplication by T=O(log ell) preserves h^(1/4-o(1)), since
H_N=o(ell²). Hence the full generated remainder has vanishing
rescaled C1 norm and vanishing integrated gradient on this window.
This is an upper bound on N_gen, not on the large q or Z separately.
It neither eliminates the earlier signed generated component nor
propagates its lower bound to the new endpoint.

The physical conversion is consistent: velocity and gradient acquire
h^(-14) and h^(-24), so their small rescaled norms need not remain
small physically. Physical time acquires h^24, which cancels the
gradient factor in the accumulated clock. That clock is invariant.

## 4. Full-Q finer-frequency tails

The larger fixed K condition is necessary for this proof step. The
nonlinear L2/H12 interpolation to H3 has exponent and clock coefficient

    (3J-15)/16,        Gamma_3=(3+C12)/4.

Consequently 3K/16>Gamma_3 B+2, together with the existing C1 condition,
makes the actual H3 error at most h^eta after the vanishing loss is
absorbed. The term ell^(15/8) in that loss is retained; divided by
eta ell² it contributes ell^(-3/16). Increasing K changes proof depth,
not the data or observation time. Strong uniqueness identifies the
same actual solution.

For any fixed beta>3/2 and P, choose fixed r so that

    r(beta-3/2)+27/8-5beta/2 > P+2.

The final order N0>=max(54,r+4) preserves the needed derivatives.
The q-only H^r energy uses the smaller actual-q clock. The receiving
wave costs k^(1-r)d^(3/2), and the global means cost
k rho d^(3/2-r). Relative to the receiver exponent 27/8-3r/2,
the first-stage exponent is larger by r/2-13/8, and the mean exponent
is larger by (r+1)/4; both are positive for r>=12.

Crucially, the explicit uniform inputs give the stronger estimate

    (J+1)H_N=O_K(ell^(11/8)+ell^(5/16)log ell)=o(ell²).

Thus the fixed-r norm of U_J really has only a subpower coefficient.
This does not follow from an arbitrary a posteriori package with
L_h=o(eta ell²); the stated uniform H_N estimate is used here.
No raw high-order full-Q energy estimate is substituted for this
approximation estimate.

The Fourier tail bound has constants uniform in the expanding torus:
the normalized-volume factor cancels the lattice density in
Cauchy--Schwarz. Apply it to U_J in H^r and to the actual error in H3.
The two contributions are h^(P+2-o(1)) and C h^eta, both smaller than
h^P for sufficiently small h. A sharp projection is not applied to
a C1 bound using a false L-infinity operator estimate.

## 5. Verdict and limits

No defect was found in the complete linear residual, datum preservation,
fixed-order weighted exact-Z estimate, correction subtraction, or enlarged-K
H3 tail argument. The conclusions concern eta=ell^(1/16), one fixed
quantitative Gevrey choice, and a family whose initial data still vary
with h. They do not give a uniform beta-down-to-3/2 limit, a zero tail,
a new phase, a signed lower bound at the new endpoint, or useful later
amplification of the small remainder.

The linear construction would fail its claimed recurrence if xi.H were
dropped from pressure. Two linear corrections do not provide the requested
C1 scale. A C1-only nonlinear error does not justify the sharp tail, and
the weaker loss condition o(eta ell²) alone does not justify a fixed-r
subpower approximation. The audited proof retains the inputs that avoid
each of these failures. The remainder and tail conclusions can therefore
be integrated as corollaries of the restricted growing-profile window,
without changing any global problem's OPEN status.
