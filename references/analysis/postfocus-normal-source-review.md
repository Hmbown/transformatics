# Independent review of the signed postfocus source

8 September 2026. **PASS at the bounded written scope stated below.**
No load-bearing gap was found in the new implication. This review treats
the previously reviewed logarithmic-host theorem and its central matching
estimates as inputs; it is not a new independent certification of their
entire PDE construction. It checks the new transported source, its error
margin, the expanding-torus comparison and the endpoint norm extraction.
This is a separate AI-agent mathematical review, not external expert
acceptance or a formal PDE certificate. ROOT, E-prime and FORCED-D remain
open. No DNS, source edits, canonical edits or git mutations were made.

Reviewed source:
[postfocus-normal-source.md](postfocus-normal-source.md),
SHA-256

    684e14f4b82fca085427c07c6ab0b0af9f3367dfce0ba32e3dcfabdfe495b552

The earlier source with SHA beginning a78d3909 was read first. The pinned
version adds the resolved exact-focus convention and reproduction section;
both additions were read before this verdict.

## 1. Exact object and quantifiers

The object is the nonlinear remainder Ncal=(Q-q)-Z, where Q and q are
the already constructed actual unforced solutions and Z is the exact
viscous linearization about q with the original receiver datum. Hence

    Ncal_t+B_q Ncal-epsilon Delta Ncal
        =-P div[(Q-q) tensor (Q-q)],       Ncal(0)=0.

In particular all q-times-mean interactions are in the exact linear
operator. There is no restarted receiver, new force or third donor.

The seed's exact focus is t_c=t_f=(2/mu)log ell-ell^(-3/4). The upstream
original-preparation and outer-matching definitions both impose their
terminal covector there. The nominal time (2/mu)log ell is different.
The correction in the pinned source preserves the datum and the exact
endpoint exponential; the small displacement is not used as an equality.

The profile, viscosity and sufficiently small eta are fixed first. All
majorant powers, cone parameters and differentiation orders are fixed
before h tends to zero. The scale family still has changing initial data.
Neither the threshold in h nor this review is uniform as eta tends to zero.

The conclusion is a lower bound for r(t_eta) dot Ncal and for the full
symmetric gradient of Ncal. It is not a full-Q dominance statement, a
diagonal normal-strain statement, a coherent-core statement or a next-stage
amplification theorem. The source states these distinctions correctly.

## 2. The exact stable channel and signed inner integral

For Abar=A0-beta tensor N/ell, N dot beta=0 gives

    N'=-Abar^T N=-A0^T N.

For every v perpendicular to N, both extra shear terms in the full
Kelvin generator vanish:

    [-Abar+2N(N^T Abar)/|N|^2]v
      =[-A0+2N(N^T A0)/|N|^2]v.

The factor 2 is required by the moving transversality constraint; the
stress force also needs P_N. Thus the exact propagator on this particular
plane is the primary two-column Floquet propagator. Since r dot B_+=0,
its endpoint r row retains only the stable source coordinate
(r dot b)/d_-, with d_-=r dot B_-<0. This rederives source (10)-(11),
including its e^(-mu L_eta) factor. A general propagator norm would not
give the same signed conclusion.

The independent affine note
[affine-stress-transport.md](affine-stress-transport.md)
also derives the full forced Kelvin equation and all frame transforms.
Its inner identity was recomputed independently of the source author's
symbolic checks. For P=1+a^2 z^4, W=-V' and
R=-2azV+az^2W,

    integral V W dz = -[V^2]/2 = 0,

    integral W R dz
       =a integral [z^2(V')^2-V^2] dz
       =2a integral [c z^2/P-4a^2 z^4/P^2] V^2 dz > 0.

The last equality uses (PV')'+(2a^2 z^2+2c)V=0. All three boundary
terms zV^2, z^2VV' and z^2(P'/P)V^2 vanish under the different incoming
and outgoing decays. Because a,c stay in a compact negative set and
V=|a|Y_+/sqrt(P), the lower bound is uniform: restrict the integral to
any fixed positive interval away from zero and use Y_+>=1. The uniform
upper bound follows from the stated two tail asymptotics. Physical time
has ds=-e dz and traverses decreasing z, so its total orientation is
positive. No additional sign is lost at the focus.

The two negative Floquet factors d_-(t_eta) and d_-(t_f) then yield the
positive real response in the source. The |a| factor in V and the
original normalization N_h comparable to D_h are both retained.

## 3. Matching errors and both outer tails

The incoming full-system bounds give y_1=O(ell^2/u^2) and
y_2=O(ell/u^3). The exact transverse lift yields

    b_n=O(ell/u^3+u^(-5))=O(ell/u^3)

on u>=u_m=ell^(-3/10), because ell u_m^2 tends to infinity.
Also b_r=d_- y_2. The weighted stable-source integral on this incoming
outer portion is therefore O(ell^2 u_m^(-5))=O(ell^(7/2)). The remaining
u>=1 portion is O(ell^2), using its exponential weight and the bounded
Floquet frame. The main inner mass is eD_h^2 comparable to ell^(9/2),
so neither tail requires a favorable sign.

For tau>=1, the outgoing full-system estimates yield

    b_r=O(D_h e^(-mu tau)),
    b_n=O(D_h/[ell(1+tau)e^(mu tau)]).

After multiplication by e^(mu tau), their product is integrable with
total O(D_h^2/ell)=O(ell^4). The fixed interval [delta,1] has the same
bound with a delta-dependent constant. This remains smaller than the
inner mass through the endpoint L_eta.

The growing-interval inner comparisons are sufficient for the signed
product, not merely for an amplitude norm. Incoming weighted errors in
V and W reconstruct an error o(D_h)/(1+z) in b_r; the Taylor remainder
eD_h is absorbed because ez<=u_m. The incoming product is dominated by
C D_h^2/(1+z)^4. Outgoing weighted errors reconstruct b_r=O(D_h) and
b_n=O(D_h)/(1+|z|)^2, with error O(delta)+o(1) in those weights.
Their product is integrable on the outgoing side as well.

Consequently one can first choose delta, then h, and finally send the
analysis partition delta to zero. It changes no data. The slow factor
e^(mu(s-t_f))|N(s)|/d_-(s) has bounded relative variation on this inner
interval. These observations justify the uniform asymptotic in (16).

With theta_h=k ell^(7/8)/N_h and N_h comparable to D_h, its physical
receiving normalization gives

    theta_h^2 eD_h^2 e^(-mu L_eta)
       comparable to eta^(-1) k^2 ell^(9/8).

The source's exponent and sign are correct. Restoring the coarse heat
factor and the receiver's central profile heat changes this expression
by a positive h-power error times a subpower factor. The stable integral
is not assumed pointwise positive before making that comparison.

## 4. Actual stress errors fit below the signed signal

The source correctly uses the global relative field W=Q-q. Its stated
L2 bounds imply

    ||W tensor W-Z_a tensor Z_a||_1
        <= [h^7+h^(29/4-B eta)] H_h^C.

The signed stress mass before the coarse derivative is proportional to
h^(27/4) times a power of ell. Thus the relative h-power gaps are 1/4
and 1/2-B eta, respectively. For B eta<1/4 both are strictly positive.
Time integration and any fixed powers of H_h and delta_h^(-1) preserve
these gaps. This estimate includes global mean tails and all cross
products; it does not assign compact support to a generated mean.

The central-to-envelope comparison factors out the transported bump.
Its squared integral is preserved by incompressibility. The remaining
unweighted polarization comparison has error (d/h)H_h^C, as supplied by
the logarithmic-host proof. The curl remainder and nonzero profile modes
gain k/d=h^(1/4) times fixed subpower factors. One integration by parts
in a nonzero phase mode suffices for a positive power: the covector
inverse, the differentiated phase and the coarse probe derivatives have
the supplied finite-order bounds. The existing smooth profile summation
is more than sufficient. This justifies phase averaging against the test;
it is not an equality with a pointwise spatial mean.

## 5. Euclidean affine adjoint and expanding-torus comparison

The actual backward adjoint has the sign

    phi_s=P(-q dot grad phi+A^T phi)-epsilon Delta phi.

In backward elapsed time and y=(x-Y(s))/R_h, its generator becomes
P[b_s dot grad-A_s^T]+(epsilon/R_h^2)Delta. The moving center removes
the potentially large constant velocity. The lower-order transpose term
cannot be omitted. The exact dual pairing with W tensor W is source (21).

For the Euclidean affine adjoint, the compact Fourier support follows an
invertible linear deformation and stays away from zero. Differentiating
the finite-dimensional Fourier equations a fixed number of times costs
exp(C integral m_h), with inverse frequency and frame norms also bounded
by such factors. This is H_h^C, not an exponential of H_h. Derivatives
of the scalar heat factor preserve finite-order bounds; diffusion is
retained with the parabolic sign. Cone derivatives cost fixed powers of
delta_h^(-1). This establishes the finite weighted seminorms needed from
(22) without a claim about weighted norms of the unknown actual pressure.

The affine drift is not periodic. On a central fundamental cube, each
noncentral image has |y+2pi H_dom j| bounded below by c H_dom |j|, and
|2pi H_dom j| is bounded by a constant times that distance. Five spatial
moments and at most five derivatives of the known affine test give

    ||image defect||H4
       <= C m_h H_dom^(-4) H_h^C delta_h^(-C),

after summing |j|^(-4). These orders lie within the source's budget of
24. The image defect and the central Taylor defect are estimated on
that cube; their sum is the periodic forcing. Neither individual affine
drift term needs to be declared a smooth periodic coefficient.
Leray and diffusion commute with periodization on the band-supported
tests, including the zero-mode convention.

Taylor's theorem and the actual q jets bound the other forcing in H4 by
m_h(R_h/h) times those known weighted seminorms. In the unknown difference,
unweighted H4 energy cancels the divergence-free transport. Commutators
use scaled coefficient derivatives bounded by C m_h once R_h/h<=1.
The energy clock is therefore C integral m_h. Uniform expanding-torus
H4-to-C1 embedding yields the asserted positive h-power error.

The order of parameter choices can be made noncircular. With the finite
derivative orders fixed, bound all angular and weighted constants first.
Choose M large enough for the cone sign, then A large enough for
H_h^(-A+C+CM) to vanish in the packet-to-point comparison. The exponents
C in these bounds can be chosen independently of A: affine scaled heat
is bounded for epsilon/R_h^2<=1, and actual scaled coefficient bounds
are uniform once R_h/h<=1. The threshold in h may then depend on A.
No h-dependent choice of M, A or derivative order is required.

Relative to the signed pairing, the remaining error factors have the
following types, with fixed exponents and harmless powers of ell:

| Error | Sufficient factor tending to zero |
| --- | --- |
| Global relative stress | h^(1/4) H_h^C delta_h^(-C) |
| Other nonlinear tracking term | h^(1/2-B eta) H_h^C delta_h^(-C) |
| Actual central model or phase averaging | h^gamma H_h^C delta_h^(-C), gamma>0 |
| Actual-q curvature in the adjoint | h^(1/4) H_h^(A+C) delta_h^(-C) |
| Periodic images | h^45 H_h^(4A+C) delta_h^(-C) |
| Packet replaced by its central stress mass | H_h^(-A+C) delta_h^(-C) |
| Coarse diffusion | h^(3/2) H_h^C |

The first six errors acquire the common gradient scaling kappa_h^4
in the actual pairing. The final polynomial signed coefficient is larger
than each remaining error for sufficiently small h. In particular a
mere o(1) error of unspecified size was not compared to a vanishing
signal.

## 6. Finite cone, real scalar pairing and strain

A first angular derivative of the affine Kelvin response costs only
H_h^C. Choosing M larger than this fixed exponent makes the cone-wide
perturbation smaller than the polynomial signed central coefficient.
The same choice keeps the complete cotangent history near the bounded
N history. This is stronger than continuity on a single ray.

For the unit-integral smooth cone weight, four Fourier derivatives have
L1 norm at most C delta_h^(-4). Fourier integration by parts in three
dimensions gives ||f_h||_1<=C delta_h^(-4). The positive sine convention
agrees with a Fourier response -i v. The endpoint Leray projection is
removed from the scalar pairing using solenoidality, while the entire
interior adjoint remains projected and vector-valued.

Periodizing kappa_h^3 f_h(kappa_h(x-Y)) does not increase its L1 norm.
The lattice spacing in the scaled frequency variable is H_dom^(-1),
and H_dom delta_h tends to infinity. Thus no fixed-volume factor or
one-ray sampling assumption enters the lower bound.

Finally, for solenoidal Ncal,

    Delta Ncal=2 div S(Ncal).

Move the inverse Laplacian to the endpoint band-supported test. Its
gradient symbol has degree -1 and is smooth on this annulus, so the
tensor kernel has L1 norm at most C kappa_h^(-1) delta_h^(-4).
This proves the additional kappa_h in the symmetric-strain lower bound.
It uses neither an L-infinity bound for Leray nor an L-infinity Korn
inequality. The powers h^(7/4) and h^(1/2) in source (5)-(6) follow.

## 7. Negative controls and verification boundary

The review independently checked the following ways the argument could
otherwise give an invalid lower bound:

* Keeping only the largest inner growing-row coefficient gives exactly
  zero, because integral V W is a boundary term.
* For b=e1 and K=e1+e3, the projected stress source has e3 component
  -1/2; deleting its pressure projection gives zero in that component.
* Affine advection does not commute with periodization. For the solenoidal
  Schwartz field Phi=(-2y2,2y1,0)exp(-|y|^2), A=diag(1,-1,0), one image
  with shift e1 contributes (0,-2/exp(1),0) at y=0 to
  A e1 dot grad Phi(y+e1). Its defect cannot be set to zero termwise.
* Unit Fourier mass does not imply uniformly bounded L1 kernel norm as
  the cone narrows. A factorized transverse rescaling already has L1
  norm proportional to delta_h^(-2). The source's larger delta_h^(-4)
  allowance is valid and explicitly paid.
* The strain identity requires divergence-free Ncal. For the compressible
  field (sin x1,0,0), Delta v-2 div S(v)=(sin x1,0,0), not zero.
* A source-free norm estimate or the affine formula alone cannot certify
  the actual signed source. The independent affine note contains a
  positive-viscosity example with a reversed transported sign.

The author's 17 bounded algebra checks were read and rerun successfully.
Separate exact symbolic controls checked the pressure-source deletion,
the nonzero affine image term and the solenoidality condition; rational
arithmetic independently checked the tail, error and normalization powers.
These checks supplement the written estimates above. They do not test an
infinite-dimensional trajectory or replace the previously reviewed
existence theorem.

No mathematical source correction is required by this audit. The result
is a finite coarse source lower bound in an explicitly subtracted actual
remainder. Its spatial shape, usable subsequent coupling, full-Q dominance
and infinite iteration remain additional research questions.
