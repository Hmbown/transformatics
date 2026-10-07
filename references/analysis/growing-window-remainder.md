# The generated remainder on the quantitative growing window

8 September 2026. **Draft bounded consequence for independent review.**
Assuming the quantitative growing-window approximation package and its
actual continuation conclusion, the exact nonlinear remainder has
vanishing rescaled C1 norm and accumulated strain on that window. Three
complete linear profile corrections suffice. The finer-frequency
exclusion also extends to this window after a larger fixed proof-depth
coefficient is chosen. These statements concern the same chosen data;
they do not supply another receiving phase or an infinite trajectory.
ROOT, E-prime and FORCED-D remain OPEN. No DNS is used.

Inputs, at the versions read here:

- [Quantitative background](growing-window-background.md),
  SHA-256 `cb6189ebfb82a7038c12c2de051a052b02cead06686c7cea1b2f2a4d62afdc48`.
- [Uniform profile operators](uniform-profile-window.md),
  SHA-256 `08e137749fe30db52751ac4553e82d7ba1e0842b80367d3ebfc0dafe6b2bcb90`.
- [Growing-depth continuation](growing-depth-budget.md),
  SHA-256 `2a7b8ff6258eb003652d3a3334b41aa135330d21ee1776b9c021b2d9a8977505`.
- [One-correction linear comparison](actual-coarse-band.md),
  SHA-256 `2b2f6aeeef78374ff91b72322163f637d90e7b416e84a427d264c46c8f6740ea`.

## 1. Quantifiers and the exact remainder

Fix one admissible Gevrey-2 choice of the existing Gavrilov profile,
cutoffs and periodic phase profile before taking h to zero. Keep the
same original two-wave datum, including its exact curl corrections.
Use the expanding rescaled torus of side 2pi L, with

    L=h^(-10), epsilon=nu h^4, k=h^(3/2), d=h^(5/4),
    rho=k/d=h^(1/4), ell²=log(1/h), eta=ell^(1/16),
    T=t_f+3log(ell)/(16mu), J=ceil(K eta), N=N0+8J.

The constant K is chosen once for the nonlinear continuation estimate.
The proof order J varies with h; the datum at a given h does not vary
with J. All norms below use unnormalized spatial L2.

To distinguish the material derivative from the coefficient majorant,
write D_t=partial_t+q.grad and

    I_q=integral_0^T m_h dt=O(ell^(19/16)),
    W_N=1+T+log(N+2),
    H_N=C[N²(I_q+1)+N^4 W_N], M_N=exp(H_N).

Constants in a fixed power of M_N are independent of h,N,J. With K
fixed, H_N=O_K(ell^(21/16)+ell^(1/4)log ell)=o(ell²).
The sharper relation JH_N=o(ell²) will be used only for the tail estimate.

Let Z solve the exact viscous linearization about the actual first-stage
solution q, with the original receiving datum z_0:

    D_t Z+(Z.grad)q-epsilon Delta Z+grad p_Z=0,
    div Z=0, Z(0)=z_0.

Set W=Q-q and N_gen=W-Z. Then, exactly,

    D_t N_gen+(N_gen.grad)q-epsilon Delta N_gen+grad p_N
        =-div(W tensor W), div N_gen=0, N_gen(0)=0.       (1)

Equivalently one may apply the full Leray projector to (1). No normal
or mean component of the right side has been discarded. In particular
N_gen is the complete nonlinear remainder, not a selected phase mean.

The conclusions are

    sup_[0,T] ||N_gen||C1 <= h^(1/4) M_N^C+h^eta,
    integral_0^T ||grad N_gen||infinity dt
                         <= T[h^(1/4)M_N^C+h^eta]
                         =h^(1/4-o(1)) ->0.              (2)

The velocity estimate can be sharpened to

    sup_[0,T] ||N_gen||infinity <= h^(7/4)M_N^C+h^eta.    (3)

These are upper bounds, compatible with the separately proved signed
coarse output on the earlier fixed-eta window. They neither propagate
that signed lower bound to T nor prove that the remainder is zero.

## 2. Exact linear corrections, with their full pressure

Write xi=grad S, A=grad q and let kappa_c(t)>=0 be the spatially
constant central heat rate. For a tangent zero-phase-mean profile v put

    V_v=-xi cross partial_s^(-1)v/|xi|²,
    r_v=curl_x V_v, W_v=v+k r_v,
    E[v](x)=v(x,S(x)/k).

Thus E[W_v] is exactly solenoidal. The primary receiving amplitude a
obeys (D_t-kappa_c partial_s²)a=G_xi a, where
G_xi=-A+2xi tensor(xi^T A)/|xi|². Its original datum is exactly
z_0=E[W_a](0).

Denote the complete forced-profile residual by R[v;H]. The identity is

    (D_t+A-epsilon Delta)E[W_v]+grad E[p_v]
                  =-E[H]+E[R[v;H]],
    p_v=-k partial_s^(-1)[(2xi.A v+xi.H)/|xi|²],           (4)

when (D_t-kappa_c partial_s²)v=G_xi v-Pi_xi H. In particular the
longitudinal term xi.H is part of the pressure.

Start with H_0=R[a;0]. For j=1,2,3 solve successively

    (D_t-kappa_c partial_s²)g_j=G_xi g_j-Pi_xi H_(j-1),
    g_j(0)=0, H_j=R[g_j;H_(j-1)].                         (5)

All coefficients are independent of the auxiliary phase. The residual
is linear in its arguments, so every H_j has zero formal phase mean.
No phase-independent mean equation or quadratic wave product is present
in this linear construction. Formal phase mean is not identified with
spatial averaging of an evaluated profile.

Define

    Z_3=E[W_a+W_(g_1)+W_(g_2)+W_(g_3)].

Summing (4) telescopes exactly to a residual E[H_3]. Each g_j and its
spatial derivatives vanish at zero; hence Z_3(0)=z_0 without modifying
the original datum. Tangency, reality and zero phase mean persist.
The profiles and their curl potentials remain in the material chart.
Neither the exact Z nor its pressure is asserted to have compact support.

For clarity, the full residual used at every round is

    R[v;H]=(kappa_c-epsilon|xi|²/k²)partial_s² W_v
       +k[(D_t+A-kappa_c partial_s²)r_v
          -grad_x partial_s^(-1)((2xi.A v+xi.H)/|xi|²)]
       -epsilon Delta_x v-(epsilon/k)L_1 v
       -epsilon k Delta_x r_v-epsilon L_1 r_v,
    L_1 v=2(xi.grad_x)partial_s v+(div xi)partial_s v.     (6)

Eliminate material derivatives in (6) by (5), D_t xi=-A^T xi,
and the exact material-curl commutator before counting derivatives.
This retains the full pressure and requires no unestimated time
derivative of q. The central heat rate has no spatial derivatives;
every phase Fourier mode retains its nonnegative damping.

## 3. Finite derivative reservation and the linear error

Use the global scaled spatial and phase-Wiener norms of the uniform
operator note. A sufficient reservation for this linear construction
starts at spatial/phase order 54 and retains order 30 after three rounds,
losing at most eight orders per round. Thus take N0>=54; a fixed extra
phase reserve of 80 and a fixed larger background order are harmless.
The same choices cover the evaluated H12 norm and pointwise recovery.
The background already supplies order-dependent constants through a
fixed larger multiple of N. All phase indices are retained.

The primary amplitude has normalized size k M_N^C. Equations (5),(6)
and the audited linear operator bound give, at the successively reserved
orders,

    H_j has size <= k rho^(j+1) M_N^C, 0<=j<=3,
    g_j has size <= k rho^j M_N^C, 1<=j<=3.               (7)

The constant exponent C may be enlarged finitely for these three
rounds. The small factors in (6) are k/d, epsilon/k²,
epsilon/(kd), and epsilon/d², whose powers are respectively
1/4, 1, 5/4, 3/2. The full local/central heat discrepancy is bounded
by (epsilon/k²)M_N^C. The slow pressure term with H gains k/d after
the reserved derivative. This proves the gain in (7), including that
term; it is not obtained from tangency alone.

Consequently,

    integral_0^T ||E[H_3]||2 dt
             <=k rho^4 d^(3/2)M_N^C=h^(35/8)M_N^C.      (8)

Subtract the approximate linear equation from the exact one. The
global solenoidal L2 pairing cancels transport and full pressure;
diffusion has nonpositive sign. Growth costs only integral||grad q||,
which is at most C I_q. Thus

    sup_[0,T] ||Z-Z_3||2 <=h^(35/8)M_N^C.                (9)

This estimates every component, including pressure-generated global
tails. It does not use an L-infinity bound for the Leray projector.

For exact high regularity use the fixed weighted norm
sum_(r=0)^12 k^r||D^r Z||2. Actual-q jets satisfy

    ||D^i q||infinity <= C m_h h^(1-i)K_N^(i-1)(i!)²,
    log K_N <= C N² W_N.

In transport commutators the weight gives
m_h[(k/h)K_N]^(i-1), times fixed combinatorial constants. Stretching
gives m_h[(k/h)K_N]^i. Since (k/h)K_N=h^(1/2-o(1)), the fixed
thirteen required q orders yield a coefficient C_12 m_h independent
of N. Full pressure drops only in each solenoidal derivative pairing.
This gives linear wellposedness through the already established q
window by finite-order Galerkin energy estimates, and

    sup_[0,T] (||Z||H12+||Z_3||H12)
                          <=h^(-117/8)M_N^C.            (10)

Indeed the original receiver's weighted norm is at most
k d^(3/2)M_N^C, and k^(-12)k d^(3/2)=h^(-117/8).
The approximate norm follows directly from the reserved profile jets.
There is no full-Q clock loss in (9) or (10).

Uniform expanding-torus Fourier splitting, including its low-frequency
term, now gives

    ||grad(Z-Z_3)||infinity
       <=C||Z-Z_3||2^(19/24)||Z-Z_3||H12^(5/24)
            +C||Z-Z_3||2 <=h^(5/12)M_N^C,
    ||Z-Z_3||infinity <=h² M_N^C.                       (11)

The gradient exponent is (19*35-5*117)/192=5/12; the velocity exponent
is (7*35-117)/64=2. At two corrections the gradient exponent would
only be 7/32<1/4. This explains the use of three corrections.

## 4. Subtraction from the actual nonlinear approximation

The nonlinear approximation has the exact form
U_J=q+m_J+E[W_(a_J)], with a_J starting from the same primary a.
The uniform recurrence gives

    ||m_J+E[W_(a_J-a)]||C1 <=rho M_N^C,
    ||m_J+E[W_(a_J-a)]||infinity <=k rho M_N^C.           (12)

Global mean tails use scaled global norms and Sobolev recovery, not a
compact support assumption. The three linear corrections satisfy the
same bounds by (7). The full nonlinear continuation estimate gives
||Q-U_J||C1<=h^eta. Its velocity assertion follows from interpolation
with H12 weight 1/8: the clock coefficient (7+C12)/8 is at most
(19+5C12)/24, while its favorable J coefficient 7/32 exceeds 19/96.
Thus the same fixed K chosen for C1 suffices also for velocity.

Use the exact identity

    N_gen=(Q-U_J)+(U_J-q-E[W_a])
                    -(Z_3-E[W_a])-(Z-Z_3).             (13)

Equations (11)--(13) prove (2),(3). Constants such as T=O(log ell)
are fixed powers of M_N. Since h^eta is smaller than every fixed
positive h power, the conclusion is h^(1/4-o(1)) in C1 and in clock.

Only the rescaled velocity and gradient are small. In the physical
variables u=h^(-14)Q, y=h^(-10)x, s=h^(-24)t, the velocity and gradient
acquire factors h^(-14) and h^(-24). Their sup norms need not be small.
The accumulated gradient clock is invariant under this scaling.

## 5. Full actual finer-power tails on the same window

Fix beta>3/2 and P>0 before h tends to zero. The same data satisfy

    sup_[0,T] ||grad P_(>h^(-beta))Q||infinity <=h^P      (14)

for all sufficiently small h, provided the fixed proof constants are
chosen as follows. This projection is the full sharp Fourier tail.

First enlarge the fixed K, if necessary, to satisfy both the C1
continuation condition and

    3K/16 > B(3+C12)/4+2.                               (15)

This changes only the depth of an approximation to the same unique
solution. It changes neither the original datum nor T. Interpolate the
complete nonlinear error between L2 and H12 to H3. With
Gamma_3=(3+C12)/4, the growing-depth package gives

    log||Q-U_J||H3 <=-[(3J-15)/16]ell²
             +(1+Gamma_3)L_h+Gamma_3 B eta ell²+O(T),
    L_h=C[(J+1)^3(I_q+1)+(J+1)^5W_N+ell^(15/8)+1].

Here L_h=o(eta ell²), so (15) implies

    sup_[0,T]||Q-U_J||H3 <=h^eta.                       (16)

This extra estimate is needed: a sharp Fourier projection cannot be
applied to a C1 error using an asserted uniform L-infinity operator norm.
Expanding-torus Fourier Cauchy--Schwarz instead gives
||grad P_(>R)e||infinity<=C||e||H3 uniformly in R>=1,L>=1.

Next choose one fixed integer r>=12 so that

    A_r(beta):=r(beta-3/2)+27/8-5beta/2 > P+2.           (17)

Enlarge N0 to at least max(54,r+4) and retain the same eight orders
per nonlinear round. No high-order energy estimate for full Q is
needed. The q-only fixed H^r energy uses the clock I_q and gives
||q||H^r<=[1+h^(7/4-r)]exp(C_r I_q). Direct evaluation of the known
profiles and global means gives

    sup_[0,T]||U_J||H^r
       <=[1+h^(7/4-r)+k^(1-r)d^(3/2)
                         +k rho d^(3/2-r)]exp(C_r(J+1)H_N)
       <=h^(27/8-3r/2)exp(C_r(J+1)H_N).                 (18)

For fixed r,K, (J+1)H_N=O_K(ell^(11/8)+ell^(5/16)log ell)=o(ell²).
Thus the last factor in (18) is h^(-o(1)), despite J growing.
The first-stage global contribution and every mean tail are included.
Only the compact oscillatory terms use the volume d³.

Uniform Fourier Cauchy--Schwarz yields, for r>5/2,

    ||grad P_(>R)v||infinity <=C_r R^(5/2-r)||v||H^r.

The reciprocal torus volume cancels the density of lattice frequencies;
there is no expanding-volume loss. Equations (17),(18) bound the
approximation's tail by h^(P+2-o(1)). Add (16), and reduce h to absorb
constants and the strict exponent margin. This proves (14).

The order of choices is the fixed Gevrey data, beta and P; then fixed
r,K,N0; then h. The growing indices J,N are the prescribed functions
of h. Thresholds need not be uniform as beta decreases to 3/2 or P
increases. At beta=3/2 the r-dependent gain vanishes, and this argument
does not assert (14). It does not exclude the coarser generated band,
an exceptionally small finer seed, or a later transfer.

## 6. Verification boundary

This proof uses the actual q, full pressure, complete original curl
datum and the uniform growing-depth package. It does not substitute
a fixed-index constant into a growing-index estimate. Three fixed
linear corrections use only the q clock; growing nonlinear depth pays
the full Q clock. The former supplies (2), while the stronger H3 error
choice in (15) supplies the full sharp-tail conclusion (14).

The resulting vanishing remainder clock is a limitation on treating
N_gen alone as a new strain host during this interval. It is not a
bound on the much larger q or Z, a no-interaction theorem, or a
later-time impossibility result. A signed lower estimate at the new
endpoint is a separate calculation and is not claimed here.
