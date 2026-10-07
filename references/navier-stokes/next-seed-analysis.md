# The current full NS trajectory cannot activate the proposed next finer scale within its proved window

8 September 2026. A written corollary of the original-time handover's
established H12 bound. This uses the actual nonlinear solution, including
all its generated modes. It is not a new global regularity criterion,
an infinite-cascade obstruction, or a formal certificate. ROOT remains open.

The [localized-profile extension](localized-profile.md) creates a finite-energy endpoint region with nearly uniform gradient. Its H12 budget is identical, so the frequency and clock conclusions below apply to both the original sinusoidal family and that fixed-profile extension. Two companion calculations locate the source and preparation gaps: [the signed outgoing interaction](../analysis/generated-receiver.md) and [the full-support flat-profile C3 cost](../analysis/flat-profile-seed-cost.md).

## 1. Input and statement

Use the actual solution Q_h in the original-time nonlinear handover,
on the expanding torus T_L^3=(R/(2pi L)Z)^3, with unnormalized norms:

    h=L^(-1/10), ell=sqrt(log(1/h)),
    k=h^(3/2), d=h^(5/4), epsilon=nu h^4,
    0<=t<=t_f=(2/mu)log ell-ell^(-3/4).

The completed continuation proof, equation (28), gives

    sup_[0,t_f] ||Q_h||H12 <= h^(-117/8) G_h,
    G_h=ell^K exp(C ell^(11/8)), log G_h=o(log(1/h)).   (1)

Here K,C are fixed constants for the chosen profile and viscosity.
The original initial-data estimate is sharper in its subpower factor:

    ||Q_h(0)||H12 <= C h^(-117/8) exp(C ell).           (2)

Write P_{>R} for the sharp Fourier projection onto physical rescaled
frequencies |n|/L>R, n in Z^3. For each fixed beta>0 put R=h^(-beta).
Then

    sup_[0,t_f] ||grad P_{>h^(-beta)} Q_h||infinity
       <= C h^a_beta G_h,
    a_beta=(19/2)beta-117/8.                           (3)

Thus every fixed beta>117/76 gives a vanishing high-pass gradient on
the entire proved interval. In particular the proposed next scale

    k_next=k^(3/2)=h^(9/4)

satisfies

    sup_[0,t_f] ||grad P_{>1/k_next} Q_h||infinity
                              <=h^(27/4-o(1)).        (4)

The high-pass strain has the same upper bound. Replacing the cutoff by
any fixed positive constant times 1/k_next changes only the constant.
A shell wholly above that cutoff also obeys this estimate by the same
Fourier proof. No assumption that the solution stays on finitely many
Fourier modes is used.

## 2. Uniform Fourier-tail proof

For a vector field v, write

    v(y)=sum_n vhat_n exp(i n.y/L),
    ||v||Hs^2=(2pi L)^3 sum_n (1+|n/L|^2)^s |vhat_n|^2.

For s>5/2 and R>=1, Cauchy--Schwarz gives

    ||grad P_{>R}v||infinity
      <= (2pi L)^(-3/2) ||v||Hs
          [sum_|n|/L>R |n/L|^2/(1+|n/L|^2)^s]^(1/2).

Dyadic shells 2^j R<|n|/L<=2^(j+1)R contain at most
C L^3(2^j R)^3 lattice points, uniformly for L,R>=1. On each shell
the summand is at most C_s(2^j R)^(2-2s). Summing the convergent
geometric series gives

    sum_|n|/L>R |n/L|^2/(1+|n/L|^2)^s
                                     <=C_s L^3 R^(5-2s).

The factor L^(3/2) cancels the Fourier normalization. Consequently

    ||grad P_{>R}v||infinity <= C_s R^(5/2-s)||v||Hs.   (5)

This is uniform in the growing period; no Poincare inequality or
normalized-volume convention is inserted. The velocity tail has the
stronger power R^(3/2-s), so a full C1 upper bound follows as well.
Set s=12 and use (1). For beta=9/4 the exponent is exactly

    (9/4)(19/2)-117/8=27/4.

The positive exponent threshold is (117/8)/(19/2)=117/76, rather
than exactly 3/2. Claiming exclusion at every beta>3/2 from H12 alone
would be unjustified. Higher fixed regularity could sharpen it, but is
not needed for (4) and is not asserted here.

## 3. A necessary clock for later activation from this same original datum

Continue the same Q_h on any interval where it remains smooth; do not
reset its initial datum or the physical viscosity. The integer H12
energy inequality used in the original continuation proof gives

    ||Q_h(t)||H12 <= ||Q_h(0)||H12 exp(C12 I_h(t)),
    I_h(t)=integral_0^t ||grad Q_h(s)||infinity ds.

Here C12 is independent of h and L; viscosity is dissipative. Combining
this with (2) and (5), for fixed beta>117/76,

    ||grad P_{>h^(-beta)}Q_h(t)||infinity
                  <=C h^a_beta exp(C0 ell+C12 I_h(t)). (6)

If this high-pass gradient reaches g_h>0, necessarily

    C12 I_h(t) >= a_beta log(1/h)+log g_h-C0 ell-log C. (7)

In particular, for any fixed g_h=g>0 the required accumulated strain
is at least (a_beta/C12)log(1/h)-O(ell). The present theorem supplies
only I_h(t_f)<=C ell^(11/8)=o(log(1/h)), so it cannot contain that
activation. This is an elementary necessary condition derived from a
known high-regularity estimate, not a newly controlled NS clock. No
bound on I_h after t_f is supplied by (7).

## 4. Consequences and limits for the next attempt

The existing two-wave interaction cannot be renamed a third seed and
counted twice. More strongly, all actual high-frequency components at
the specified next scale have the small bound (4) during this window,
whatever their nonlinear origin. This rules out an additional dominant
handover at that scale before t_f. It does not rule out tiny generated
seeds, transfer to nearby frequencies, later amplification after t_f,
or a different construction with different initial derivative costs.

The argument cannot be restarted at t_f with an uncharged new seed or
a new favorable Sobolev budget. A continuation must track the same
I_h, original H12 cost and diffusion history. The lower bound (7)
identifies a quantitative burden for the next proof: a sufficiently
long or sufficiently strong subsequent evolution, with an appropriate
error estimate when the old sublogarithmic history advantage is lost.

In physical coordinates u_L(t,x)=A_L Q_h(A_L L t,Lx),
A_L=L^(7/5), the gradient multiplier is A_L L=h^(-24).
The corresponding physical cutoff is L h^(-beta), and the right side
of (3) acquires h^(-24). Thus (4) is not a claim that the physical
absolute high-pass gradient tends to zero: at beta=9/4 its bound is
h^(-69/4-o(1)). At the proved endpoint it is negligible relative to
the total physical handover strain, whose lower bound is
c h^(-24) ell^(11/8). The gradient-time integral I_h is invariant
under this common coordinate conversion.

The result is a restriction on this finite varying-data family and
its present proved time window. It does not settle unforced 3D NS.


## Review provenance

[Independent review record](../analysis/profile-extension-review.md). Original reviewed source `nse-finer-frequency-window-20260908.md`, SHA-256 `a3e94f6809729eb7f7de9f8c3b34af3c2935fb3dc11a862d2e00d37bc2b826b9`. Archival changes resolve links and current-scope wording; they do not replace a formal PDE certificate.
