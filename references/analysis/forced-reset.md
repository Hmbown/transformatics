# Forced finite resets and the smooth-terminal-force budget

Independent agent review: [scope and corrections](forced-stage-review.md). These reviews do not certify a complete Navier–Stokes proof.

Independent analytic strategy check, 8 September 2026. All formulas below use physical coordinates x,t and one fixed viscosity nu>0. No canonical edits, site changes, or DNS. These are controlled examples and sufficient convergence criteria, not forced or unforced blow-up proofs.

## 1. Exact finite steering is available

Let V solve forced NS with pressure p_V and force f_V on a fixed periodic cube (or on R3). Let z be a smooth compactly supported divergence-free field embedded in that domain, and eta(t) a smooth ramp from zero to one over an interval of length Delta, flat at its endpoints. Set

    u=V+eta z, p=p_V.

Then u solves exactly the same fixed-viscosity NS equation with force

    f=f_V+eta' z-nu eta Delta_x z
       +eta[(V.grad)z+(z.grad)V]+eta^2(z.grad)z.             (1)

No approximation or missing pressure equation occurs: the external force need not be divergence-free. Taking divergence of (1) gives precisely the pressure compatibility for this choice of p. One may instead Leray-project the added force and shift its gradient part into p. On the torus that preserves smoothness, but on R3 it generally produces noncompact algebraic tails. Keeping (1) and the inherited pressure avoids that unnecessary tail when the added field is compactly supported. This matters if rapidly decaying forcing is eventually required.

More generally any prescribed smooth solenoidal path u has the exact realization

    p=0, f=partial_t u+(u.grad)u-nu Delta_x u.               (2)

For compactly supported u, this f is compactly supported; for periodic u it is periodic. This observation proves finite controllability with unrestricted distributed forcing. It proves no uniform bound on the force as stages shrink or gradients grow.

## 2. An explicit compact affine-core reset

For any trace-free matrix M and radius r, define

    B_{M,r}(x)=curl[-chi(x/r) x cross (Mx)/3],

where chi is a fixed smooth cutoff equal to one on an inner ball and supported in a larger ball. Since curl[x cross (Mx)]=-3Mx when trace M=0, this field is exactly Mx in its inner ball and is globally divergence-free. It is compactly supported and can be embedded periodically. For every fixed j,

    ||D^j B_{M,r}||infinity <= C_j |M| r^(1-j).             (3)

Choose a smooth matrix path M(t) interpolating between any two trace-free matrices, and apply (2) to B_{M(t),r}. This exactly resets the inner velocity gradient. It requires no symmetry assumption on M'+M^2: in the inner ball the force is simply (M'+M^2)x, with the prescribed zero pressure. Outside, cutoff derivatives are retained in (2).

If |M|<=M_* and the interpolation scale is Delta, then

    ||D^m f||infinity <= C_m [M_* r^(1-m)/Delta
                    +nu M_* r^(-1-m)+M_*^2 r^(1-m)].       (4)

Time derivatives add the appropriate powers of Delta^-1. Resetting around a nonzero base V adds the cross terms in (1). This is a concrete exact finite construction; it is not inexpensive uniformly in r, Delta or M_*.

## 3. General seed-insertion costs, including time derivatives

For a fixed-shape compact curl seed with velocity amplitude a and scale r,

    ||D^m z||infinity <= C_m a r^-m.

Equation (1) gives

    ||D^m(f-f_V)||infinity <= C_m [a Delta^-1 r^-m
       +nu a r^(-m-2)+a^2 r^(-m-1)
       +a sum_{j=0}^m (B_j r^(-(m-j+1))
                            +B_{j+1} r^(-(m-j)))],         (5)

where B_j bounds D^j V during the interval. For mixed derivatives define

    B_j^[p]=max_{0<=l<=p} Delta^l ||partial_t^l D^j V||infinity.

Then a sufficient bound for ||partial_t^p D^m(f-f_V)||infinity is the right side of (5) with B_j replaced by B_j^[p], multiplied by C_{p,m} Delta^-p. This includes the extra Delta^-1 in eta' and all base time derivatives by the product rule. It is an upper bound, not a necessary cost theorem: special transported seeds or nonlinear cancellations can reduce the residual.

For anisotropic/multiscale packets, r is the smallest derivative scale, not automatically the envelope radius. The exact derivative norms may be used instead of a single-r estimate. Ignoring the oscillatory wavelength in the viscosity or force-derivative budget is invalid.

## 4. A nonvacuous criterion for infinitely many force pulses

Let disjoint intervals I_j accumulate only at a finite T, with lengths Delta_j. Suppose force corrections f_j are smooth, flat at each interval endpoint, and supported in I_j in time. If for every fixed p,m,

    sup_{I_j} ||partial_t^p D^m f_j||infinity ->0,           (6)

then their sum extends by zero at and after T to a C-infinity force, flat in time at T, on a common compact spatial domain. To see this, for each derivative order its piecewise values extend continuously to zero; the next time derivative also extends continuously, giving the derivative identity at T by the fundamental theorem of calculus. Induct on derivative order. For overlapping intervals, summability of these mixed-derivative sup norms is a stronger sufficient criterion, together with the corresponding terminal limits.

Thus requiring the bounds in (5), with their mixed-derivative versions, to tend to zero for all p,m is an explicit, nonvacuous force-budget criterion. For example take

    r_j=2^-j, Delta_j=2^-j, a_j=exp(-2^(4j)), V=0.

Use smooth on-and-off ramps flat at their ends, with the exact force (2). Every quantity in (5) tends to zero at every fixed derivative order. This gives an actual C-infinity forced solution and force through T. Its strains a_j/r_j tend to zero, so it is not a singularity or a growing reset. The example shows both that the criterion is achievable and why a cascade would need more than arbitrary insertion of attenuated seeds.

If one wishes to retain every inserted seed rather than turn it off, the cumulative velocity, nonlinear cross terms and any force after each ramp must also be controlled. Disjoint forcing intervals alone do not prove (6) for that different construction. Spatially disjoint persistent components on a compact domain have their own smooth-velocity compatibility requirement. On R3, compact common spatial support makes spatial decay automatic; moving supports escaping to infinity require weighted bounds as well.

A smooth nonzero terminal background force can be allowed by applying (6) to the difference from a specified smooth extension. Smoothness at T is not synonymous with vanishing force at T; zero extension is a convenient sufficient construction, not a necessary form of a Clay-admissible force.

## 5. A genuine lower bound for one tempting holding strategy

The preceding upper budgets must not be mistaken for impossibility arguments. There is, however, an exact obstruction to holding a fixed-shape compact reset stationary with bounded force at shrinking radii.

Let z_r=a Z(x/r) for a fixed nonzero smooth compact divergence-free Z. Hold u=z_r on a time plateau and use p=0, f=(z_r.grad)z_r-nu Delta z_r. Pairing with z_r and integrating gives

    integral f.z_r = nu ||grad z_r||2^2,

because the advective pairing vanishes. Thus

    ||f||infinity >= nu ||grad z_r||2^2/||z_r||1
                    =c_Z nu a/r^2.                        (7)

The same pairing bound applies with any pressure for which integration by parts is legitimate. With p=0 the force is compactly supported at radius O(r). Taylor's formula from a support exit then implies, for each fixed m, ||D^m f||infinity >= c_{m,Z} nu a r^(-m-2). For an affine-core shape a=M_* r, already its force supremum is at least c nu M_*/r. Hence an infinite sequence of stationary held compact cores with increasing M_* and shrinking r cannot have a continuous terminal force by this strategy.

This lower bound does not apply unchanged to a freely evolving stage: its time derivative can offset diffusion. It is not a theorem that all forced cascades are impossible.

## 6. Comparison with the present stage family in physical units

The current finite theorem converts by

    L=h^-10, A=h^-14,
    u(t,x)=A Q(A L t,Lx), epsilon=nu L/A=nu h^4.

For the original finer receiver, its rescaled amplitude is k ell^(-13/8), central phase gradient is comparable to ell, and k=h^(3/2). Thus its physical amplitude and initial wavelength scale are

    a_phys ~ h^(-25/2) ell^(-13/8),
    r_phys ~ k/(ell L)=h^(23/2)/ell,
    initial strain ~ h^-24 ell^(-5/8).

These amplitudes and derivatives are not small in physical coordinates. A naive insertion budget includes

    nu a_phys/r_phys^2 ~ nu h^(-71/2) ell^(3/8).

Using the original physical window Delta~h^24 log ell also gives

    a_phys/Delta ~ h^(-73/2) ell^(-13/8)/(log ell).

These are bookkeeping costs for this artificial ramp, not lower bounds on the force of the actual unforced solution. That solution of course has force zero because its full dynamics cancel the residual. The existing stage estimates do not establish analogous cancellations for a matrix-reset or next-seed insertion operator. They also do not provide one common evolving base for an infinite schedule.

For the outgoing physical affine-like ball, the radius is about h^(23/2) and gradient about h^-24 ell^(11/8). Replacing it by the stationary compact fixed-shape holding construction of section 5 would force at least order nu h^(-71/2) ell^(11/8), so that particular reset has no bounded-force limit. Dynamic resets remain a separate possibility.

**Conclusion:** forced research admits exact finite matrix steering and seed insertion, but the current estimates do not establish the all-derivative terminal-force criterion for a naive repeated manufactured reset. A viable forced cascade must exhibit a coherent time-dependent trajectory whose residual has smooth terminal jets, not merely a succession of independently steerable states. The unforced route adds the stronger requirement that this residual vanish identically. Neither target is closed here.
