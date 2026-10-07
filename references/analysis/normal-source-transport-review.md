# Independent review of transport of the generated normal component

8 September 2026. **PASS at the fixed-short-time written analytic scope
stated below.** This separate AI-agent review checks the new transport and
duality argument against its stated upstream packet estimates. It is not
external expert acceptance, a formal PDE certificate, or a solution of
ROOT, `(E′)` or FORCED-D. No DNS was used. The reviewer did not edit the
source.

Reviewed source:
[normal-source-transport.md](normal-source-transport.md),
with exact SHA-256

```text
4f32a640a675659b13838d80245271ad85524fdd3630124f0f6be9c51375022d
```

The [initial-source calculation](actual-third-source.md),
[original nonlinear handover](../navier-stokes/original-nonlinear-handover.md),
[full-profile construction](../navier-stokes/localized-profile.md) and
[logarithmic host](../navier-stokes/logarithmic-host.md) were read for the
specific preparation, actual-q jets and relative-error inputs used here.
This is not a new independent proof of all those upstream results.

## 1. What is actually being measured

The fields are W=Q-q and N=W-Z, where Z solves the exact homogeneous
viscous linearization about the actual q, with the already supplied receiver
z0 as its initial datum. Thus N(0)=0. Z is an auxiliary comparison, not
another datum added to Q and not an applied force.

Subtracting the two NS equations and then the Z equation gives exactly

```text
partial_t N + B_q N - epsilon Delta N
 = -P div(W tensor W),
B_q v=P(q.grad v + A v),       A=grad q.
```

Every interaction linear in the full W, including q times its generated
mean, remains in B_q. The source is the complete actual relative stress
W tensor W. This avoids needing to make the possibly much larger total
stress involving q into a small error.

The lower bounds concern the normal component of N relative to this
specified linear comparison. They are not lower bounds for the normal
component of the full Q, nor a claim that the generated remainder dominates
the background or linear receiver.

## 2. Small relative stress, globally and uniformly in the initial interval

The relative L2 energy inequality uses only the actual-q gradient:
advection by q and self-advection by W cancel, pressure pairs to zero,
and the remaining production is the A term. The initial packet estimates
give ||z0||2 <= C a_h d^(3/2), including its curl lift. Since q's gradient
is uniformly bounded on a fixed initial time interval, source (8) follows
with a constant independent of h.

The one-round comparison gives

```text
||W-Z_a||2/(a_h d^(3/2))
 <= C[h^(1/4) ell^(13/8) E_h
       +h^(1/2-B eta) ell^(13/8) E_h]=o(1).
```

Here the global mean and full profile correction use their global L2
norms. They are not assigned compact support. Choosing a permitted small
fixed eta with B eta<1/4 leaves positive powers, and does not change the
initial datum. Since log E_h=o(ell²), both terms vanish. Consequently

```text
||W tensor W-Z_a tensor Z_a||1
 <= (||W||2+||Z_a||2)||W-Z_a||2=o(M_h).
```

This is small relative to the receiver's stress mass M_h, which is the
necessary scale for the signed argument. It is not merely an absolute
o(1) bound on a much larger total-flow stress.

On this same fixed initial interval, |A| is uniformly bounded and the
pressure-bearing polarization generator has norm at most 3|A|. Hence
beta_h(s)=e_b+O(s) and |xi_c(s)| is comparable to ell. The central heat
time is O(nu h ell² s)=o(1). The original preparation bounds propagate
with only a fixed-time factor. The transported bump still has squared
integral d³ integral chi² and diameter at most C d mathcal E_h.

The phase-mean stress therefore has mass M_h beta_h tensor beta_h+o(M_h).
Curl contributions are relatively o(1). For the nonzero phase modes,
|xi|>=c ell permits integration by parts. Differentiating the envelope
costs d^(-1) times its fixed preparation majorant, and the prescribed
probe costs only R_h^(-1)<=d^(-1). A relative factor
(k/d)mathcal E_h tends to zero. The fixed smooth profile norms sum these
mode estimates. This justifies comparing the actual evaluated stress to
its auxiliary phase mean; no spatial averaging identity is assumed.

## 3. Projected real probe and expanding-torus normalization

For one Fourier direction v, the gradient of the negative sine probe at
the origin is -[P(v)e_n] tensor v. Its contraction with e_b tensor e_b
is

```text
-(e_b.v)[e_b.P(v)e_n]
 = (e_b.v)²(e_n.v)/|v|² > 0
```

on the selected cone. This independently checks the sign in source (15).
Rotation from one fixed cone profile gives uniform constants as the
orthogonal directions e_b,e_n vary with h.

The Fourier support avoids zero, so the Euclidean Leray multiplier keeps
the probe Schwartz. Periodization on the side-2pi H_h torus samples the
same multiplier and commutes with Leray. The fixed test has zero mode
zero. Its L1 norm, H6 norm and the weighted derivative L2 norms in (16)
are uniform. On the central cube, distance to the origin is no larger
than the Euclidean distance of any of its translates. Summing the fixed
Schwartz tails proves the weighted bounds and the vanishing image error
at the origin, uniformly over the chosen rotations.

The physical-in-rescaled-coordinates terminal test has factor kappa_h³.
Its scalar L1 norm is unchanged by x=Y+R_h y because the Jacobian is
R_h³=kappa_h^(-3). There is no omitted growing-torus volume factor.

## 4. Backward adjoint and its moving-frame energy estimate

On solenoidal vectors, integration by parts gives

```text
B_q^* phi=P(-q.grad phi+A^T phi).
```

Therefore the backward terminal equation must be
partial_s phi=B_q^* phi-epsilon Delta phi, exactly source (18).
With this choice, the B_q and diffusion terms cancel in the derivative
of <N,phi>. Reversing time makes the diffusion coefficient positive.

For sigma=t-s and y=(x-Y(s))/R_h, differentiating the moving center
subtracts q(s,Y(s))/R_h from the drift. A constant transport field commutes
with Leray on solenoidal tests. The resulting equation is precisely

```text
partial_sigma Phi=P(b_s.grad_y Phi-A_s^T Phi)
                   +delta_h Delta_y Phi,
b_s=[q(s,Y+R_h y)-q(s,Y)]/R_h,
delta_h=epsilon/R_h².
```

The q jets give D_y^r b_s=R_h^(r-1)D_x^r q, bounded for 1<=r<=5
because R_h/h tends to zero. Also b_s(0)=0, so the global Lipschitz
bound on q gives |b_s(y)|<=C dist(y,0) along a shortest torus path.
The drift's unweighted supremum can be large; it is not bounded uniformly
or inserted into an energy coefficient.

Subtracting the fixed terminal profile is the essential step. The forcing
for Xi=Phi-Phi_h^H uses b_s only against a fixed Schwartz derivative.
Its H4 norm is uniformly bounded by (16), the bounded derivatives of b_s,
and delta_h ||Phi_h^H||H6. For the unknown Xi, ordinary unweighted H4
energy suffices. Leray commutes with derivatives and disappears in the
solenoidal energy pairing; divergence-free transport cancels. All remaining
commutators use derivatives of b_s or A_s through the displayed orders.
Diffusion is nonpositive in the energy inequality. This proves
||Xi||H4 <= C sigma exp(C sigma).

Uniform H4-to-C1 embedding follows by Fourier Cauchy–Schwarz. The sum of
|n/H_h|²(1+|n/H_h|²)^(-4) has order H_h³; the unnormalized Parseval
factor cancels H_h^(3/2) after taking its square root. Thus (22) is uniform
on the expanding torus. No weighted estimate is imposed on an unknown
pressure tail, and no long-time stability claim is used.

## 5. Signed endpoint output and normal diagonal strain

The packet diameter divided by R_h is O(mathcal E_h^(-1)). The fixed
probe gradient is therefore nearly constant across its support. Its
contraction with the phase-mean stress is c_psi+O(s)+o(1).
Replacing Z_a tensor Z_a by the full W tensor W costs o(M_h) times
C kappa_h^4. Replacing the fixed probe by the exact adjoint costs
C t kappa_h^4 ||W||2². These errors give source (24), uniformly for
0<=s<=t<=t0.

Choose t0 first to control the O(t) error, then choose h to control every
uniform o(1) error. Integrating the exact adjoint identity gives a positive
lower bound c t M_h kappa_h^4. The errors are bounds on the integrand,
so they also carry the factor t after integration. The statement remains
valid for every 0<t<=t0 with one sufficiently small-h threshold.

At the endpoint, N is solenoidal. Self-adjointness of Leray converts the
vector pairing into the scalar pairing with e_n.N and kappa_h³ f_h^H.
The bounded scalar L1 norm proves the normal-velocity lower bound, without
requiring the interior adjoint to remain parallel to e_n.

The cosine primitive g_h obeys partial_(e_n)g_h=f_h and is Schwartz,
since e_n.v is bounded away from zero on the Fourier support. Spatial
integration by parts replaces the scalar kernel by kappa_h² g_h^H,
whose L1 norm is C/kappa_h. This proves the gradient bound with one
additional factor kappa_h. Because e_n is a fixed unit direction for
each h, partial_(e_n)(e_n.N)=e_n^T S(N)e_n is a diagonal component of
the symmetric strain.

## 6. Independent controls and scope

Exact algebra checks supplied three negative controls:

* At e_b=e1, e_n=e3 and v=(1,0,1), the projected contraction is 1/2;
  the unprojected contraction is zero. Omitting pressure loses the
  leading signed normal contribution.
* On the 2pi torus, take q=(sin y,0,0), N=(0,sin x,0), and
  phi=(sin x cos y,-cos x sin y,0), all divergence-free. The exact
  B_q/B_q^* pairing agrees. Omitting A^T phi leaves a pairing error of
  magnitude 2pi³. The transpose term is load-bearing.
* Differentiating the odd sine vector probe gives an even probe whose
  gradient at the center is zero. It does not preserve the preceding
  signed rank-one contraction. The cosine-antiderivative endpoint
  argument is the valid route to the normal diagonal-strain estimate.

Rational arithmetic checks give

```text
M_h ~ h^(27/4) ell^(-13/4),
M_h kappa_h^4 ~ h^(7/4) ell^(-13/4) mathcal E_h^(-8),
M_h kappa_h^5 ~ h^(1/2) ell^(-13/4) mathcal E_h^(-10),
epsilon/R_h² = nu h^(3/2) mathcal E_h^(-4),
physical wavelength scale = h^(45/4) mathcal E_h².
```

The source, adjoint and real scalar duality pass review with these
quantifiers. They establish a nonzero generated normal remainder on a
fixed small initial rescaled interval, in the same varying-data family.
They do not transport its sign through focus, create a new short-wave
phase, locate a receiving core or prove that it dominates the total flow.
The remaining full signed postfocus pairing in source (28) is not decided
by a smaller approximation error alone. ROOT, `(E′)` and FORCED-D remain
OPEN.
