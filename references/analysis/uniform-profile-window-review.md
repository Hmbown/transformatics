# Independent review of the uniform profile operators and recurrence

8 September 2026. **PASS for sections 2–4, conditional on the stated
quantitative actual-q and prepared-phase inputs.** This reviews
[the uniform profile window](uniform-profile-window.md)
at source SHA-256
`08e137749fe30db52751ac4553e82d7ba1e0842b80367d3ebfc0dafe6b2bcb90`.
The source includes the coordinating agent's per-order majorant
clarification after (7). Its background input, at this read, has SHA-256
`3004a6cd9b1de908d3cf75bcb079140f7cba7de943b5ac9c2586b249096e064f`
and is undergoing a separate independent review.

The pinned version also retains the velocity/gradient comparison in (1b)
and spells out the reference-particle and whole-label errors in section 5.
Those clarifications do not change sections 2–4 reviewed below; they make
explicit the additional inputs needed to use the operator estimates.

The focus here is the global mean, full pressure, polarization solver,
phase composition and growing-depth bookkeeping. The sharp outgoing
central history in section 5 requires its own stated input; this review
does not replace a verification of that history or of the background
lemma. No DNS, canonical source edit, formal PDE certificate or external
expert acceptance is supplied.

## 1. Norms and pressure-complete global mean propagation

The S_r norm is d^(-3/2) times an l1 sum of the d-weighted derivative
L2 norms. Its equivalence to the Hilbert derivative norm loses at most
sqrt(r+1). On tori of side at least 2pi, scaled Fourier Sobolev gives
the required pointwise bound from two additional spatial derivatives.
The inhomogeneous low-frequency terms are included; there is no
expanding-volume Poincare assumption.

Leibniz expansion then proves the stated product estimate. The product
uses a pointwise factor and a global L2 factor, including when both
fields are noncompact mean tails. Counting tensor contractions costs
at most exp(Crlog(r+2)). Phase Wiener convolution introduces at most
2^M, which fits a fixed power of D. The phase primitive divides by
nonzero integer frequencies, so no h-dependent spatial divisor occurs.
Evaluation is bounded by the complete phase l1 sum; it requires neither
orthogonality nor a Fourier truncation of the actual evaluated field.

In the mean equation each spatial derivative remains solenoidal.
Its full pressure gradient pairs to zero in L2, while the top transport
term cancels because q is divergence-free. For i>=2, the scaled q
coefficient contains (d/h)^(i-1)=rho^(i-1). With the Gevrey-2 input,

    binomial(r,i)(i!)² <= r N^(2i-2), r<=N.

Thus the sum of those coefficients is bounded by a geometric series
in rho K_N N². The leading i=1 term is only O(N m_h). The stretching
terms have one more derivative of q and one more d; their extra
polynomial factors are summable by the same smallness. The safe
aggregate coefficient C N² m_h is valid. Gronwall costs exp(CN²I_q),
which is a fixed power of D. High jets have not entered this exponent
as an undifferentiated largest-order norm.

## 2. The normalized phase bound does not cost D to the N

The terminal phase is affine on the prepared chart. Its subsequent
spatial dependence comes from actual-q flow maps, not from the bump.
The normalized cotangent satisfies the closed fiber equation

    Dn=-A^T n+(n.A^T n)n, |n|=1,
    D log|xi|=-n.A^T n.

The coefficient acting on the top fiber variation is bounded by C|A|.
There is no inverse-magnitude coefficient in that top equation. The
given per-order flow and q estimates consequently supply h^(-r)
times their finite Gevrey majorants for spatial derivatives of n and
log|xi|. Multiplying by d^r gives precisely rho^r.

The source's largest-order D may be used only after these compositions
are estimated. For a partition r_1+...+r_m=r with positive parts,

    sum r_i² <= r²,  sum r_i^4 <= r^4,
    sum r_i log K_N = r log K_N.

Replacing r_i by r_i+1 changes only fixed constants, because m<=r.
Factorial products and the number of partitions contribute at most
exp(Crlog(r+2)). Repeated zeroth inverse-magnitude factors contribute
O(r I_q) to the logarithm, with harmless original normalization powers.
These fit C[N²(I_q+1)+N^4 W]. This independently checks the added
majorant explanation. It would be incorrect to take an arbitrary
order-N bound D first and use it once per chain-rule factor; that
would artificially create D^N.

The inverse covector in the pressure and lift is also covered. One may
write it as n exp(-log|xi|), retaining the same partition accounting.
Products forming G=-A+2n tensor(n^T A) contain only a fixed number of
coefficient fields. Its zeroth bound is C m_h; each positive spatial
derivative brings rho^r times the already constructed D majorant.

## 3. Full polarization, heat and longitudinal pressure

For each nonzero phase mode, the scalar heat term has sign -kappa n²
and commutes with the matrix transport. The spatially constant central
clock creates no differentiated-clock terms with an additional n².
The derivative commutators of q and G are controlled as above. The
resulting mode energy estimate has coefficient C N² m_h, independently
of the phase index; summation with A_M weights is therefore legitimate.

Tangency persists because Dxi=-A^Txi and the projected profile equation
preserves xi.g=0. The mean-zero phase property also persists. Spatial
support follows material transport of the compact chart and its forcing;
extension by zero is smooth at the material boundary. This support
statement concerns oscillatory profiles, not the separately solved mean.

The complete pressure numerator 2xi.Ag+xi.H is present in (10).
Its longitudinal part combines with -Pi_xi H to produce the entire
-H, not merely its tangential projection. The exact material-curl
commutator eliminates time derivatives using spatial jets of q, g
and H. Consequently the linear remainder requires no unestimated
pressure tail or time derivative of q. No L-infinity boundedness of
Leray is assumed at any step.

## 4. Eight reserved orders suffice without growing the datum

Let r_out=M_out=N-8(j+1) denote the next residual's target orders.
A sufficient concrete accounting is:

* Linear lift/viscosity remainder needs delta a through spatial
  r_out+3 and phase M_out+2.
* Nonlinear products of lifted fields, with two extra spatial orders
  for pointwise recovery, need delta a through r_out+4. The largest
  slow derivative on one lifted field is two.
* Solving delta a to that order requires its forcing H at r_out+4.
  The product (delta m.xi/k)(a_j)_s is controlled with delta m and
  the old amplitude through r_out+6. Its extra phase derivative,
  combined with the required heat derivatives, needs at most M_out+3.
* The mean solve has no derivative loss in the differentiated global
  energy estimate. The pressure-input derivative in the linear
  remainder is lower than the orders already counted.

All these lie within r_out+8 and M_out+8. The prescribed extra known
background/phase orders cover coefficient derivatives. A sufficiently
large fixed N0 also leaves the final H12 and pointwise recovery orders.
Thus the reserve is ample; it is not silently increasing with the
phase mode or adding data at later rounds.

The exact recurrence contains every global mean-mean, mean-wave and
wave-wave term. It cancels the new mean's leading fast advection of
the old amplitude before estimating the remainder. Tangency removes
only the leading tangent/tangent fast products; normal curl products
remain and cost k/d. The ordinary viscosity ratios and the complete
central/local mismatch have the stated smaller h powers. Their phase
derivatives are charged to the reserved A_M orders, rather than bounded
by discarding high phase indices.

Every round therefore consists of a fixed number of bounded operators
and quadratic products, giving fixed exponents b in (11). Prior residuals
are estimated by F_j rather than expanded into an exponentially large
tree. Existing amplitudes are bounded in the currently reserved norms;
higher norms available from earlier rounds imply those lower norms.

## 5. Recurrence and remaining assembly

With A=C D^b, g_j=F_j/k and z=2A²rho, the proposed induction is exact.
If g_j<=A rho, then

    A rho g_j+A g_j² <=2A²rho g_j=z g_j.

Starting at g_0<=A rho and z<=1/2 gives g_j<=A rho z^j. The sum of
increment norms is at most A k sum g_j<=2kA²rho. The evaluated-gradient
bound follows from the same operator estimate divided by k. Its time
integral is still vanishing after the fixed power of D that pays T.
This is a finite induction bounded by a geometric series, not the
construction of an infinite profile sequence at fixed h.

Evaluation restores the genuine d^(3/2) L2 factor for the compact wave
part. Global means retain their global scaled norms. The leading H12
power is k k^(-12)d^(3/2)=h^(-117/8); the mean and first-stage terms
have smaller h costs. Equations (13)–(14) follow with log loss
C(J+1)H_N. Initial increments vanish exactly, and the phase-mean
residual has the zero spatial integral needed to retain the original
mean-zero velocity. No changed datum enters the induction.

Finally the arithmetic in (16)–(17) is consistent: the three leading
loss ratios have exponents -11/16, -7/4 and -3/16. The old through-focus
history ell^(15/8) is correctly retained. Provided the separate sharp
history statement and the independently audited background lemma hold,
the conditional continuation budget applies as stated. The operator
and recurrence audit finds no further correction required.
