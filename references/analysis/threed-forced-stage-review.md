# Independent review of the compact three-dimensional forced stage

8 September 2026. **PASS at the finite written scope stated below.** This is
an independent AI-agent mathematical review, including exact algebra controls.
It is not external expert acceptance, a formal PDE certificate, or a proof of
ROOT, `(E′)` or FORCED-D. No DNS was used.

Reviewed source: [three-dimensional forced stage](threed-forced-stage.md).
The exact source SHA-256 reviewed is

```text
2ba3b8ba2168fadfe1d7225ff59b7e538a6fca1301684a983f5118541b336b59
```

The source was reread after its host cutoffs were explicitly fixed as unit
profiles evaluated at x/R. This makes the claimed cutoff constants uniform
under the displayed R scaling. No velocity, pressure or residual formula was
changed for that clarification. This reviewer did not modify the source.

## 1. Actual host, periodic pressure and unavoidable baseline cost

For A=diag(lambda,2lambda,-3lambda), the vector identity

```text
curl[x cross (Ax)]
 = x div(Ax) - (Ax) div x + ((Ax).grad)x - (x.grad)(Ax)
 = -3 Ax
```

checks the factor -1/3 in the host potential. Curling its compactly supported
cutoff gives an exactly divergence-free, mean-zero periodic H. In the radius
2R core, H=Ax and the specified pressure gradient is -A²x. The complete
stationary force therefore vanishes there. Outside the radius 3R support,
it also vanishes. The cutoff pressure is periodic; its shell derivatives
belong to the force and have not been hidden in a nonperiodic pressure.

The scaled fixed cutoffs give |D^p H| <= C_p lambda R^(1-p).
One derivative in the quadratic momentum term and two in the viscous term
give exactly the two powers in source (2).

For any smooth periodic pressure, stationary energy gives

```text
integral f_H.H = nu integral |grad H|².
```

The core contributes at least c lambda² R³ on the right, and
||H||_1 <= C lambda R⁴. Thus ||f_H||_infinity >= c nu lambda/R.
This is a lower bound on the complete host force, independent of pressure,
and is not inferred from a divergent upper bound.

The three distinct eigenvalues of the symmetric affine gradient exclude
rotational invariance: a nonzero infinitesimal rotation would have to
commute with A. Its off-diagonal entries would then vanish because the
eigenvalues differ, and a skew-symmetric diagonal matrix is zero. The host
therefore leaves the earlier full fixed-axis annular class. This fact alone
has no singularity implication.

## 2. Kelvin wave and its exact finite velocity gain

Write D=partial_t+Ax.grad. The source phase obeys D phi=0 because
kappa'=-lambda kappa. Also

```text
a'/a = 3lambda - nu kappa²,       A e3 = -3lambda e3.
```

These identities give (D+A-nu Delta)(a sin(phi)e3)=0.
The wave is independent of x3, so its self-advection vanishes. No interior
wave pressure is needed for this selected polarization. Integrating the
amplitude rate gives source (5), including its factor 1/(2lambda).
At lambda=nu K² and Theta=1 the exponent is
3-(1-exp(-2))/2 and the gain exceeds 12.

The frequency decreases by exp(-Theta), so the gradient amplification
has the extra factor exp(-Theta). The stated velocity gain is realized on
the bump plateau, where there are phase maxima once the supplied
localization conditions hold. It is a ratio of the actual perturbation
values at the selected interior phase points. It need not equal the exact
ratio of the full compact wave's global sup norms, which also include its
curl correction. The source correctly claims the plateau gain.

## 3. Complete curl residual and the pressure factor 8

Let c=a/kappa and write chi_i for a physical derivative. Transport gives

```text
D chi=0,       D chi_i=-A_ii chi_i,
c'/c=4lambda-nu kappa².
```

For W1=c chi_3 cos(phi), the material derivative has coefficient
7lambda-nu kappa²: 4lambda comes from c and 3lambda from the compressed
third-coordinate cutoff derivative. Adding A_11 supplies another lambda.
The carrier part of -nu Delta cancels -nu kappa². The remaining first
component before pressure is therefore

```text
8lambda(a/kappa)chi_3 cos(phi)
 -nu(a/kappa)Delta chi_3 cos(phi)
 +2nu a chi_13 sin(phi).
```

The fast x1 derivative of
pi_W=-8lambda(a/kappa²)chi_3 sin(phi) cancels exactly the first term.
Its other derivatives give the three -8lambda(a/kappa²)chi_i3 sin(phi)
terms retained in source (9). In the third component, both pieces of W3
have (D+A) coefficient -nu kappa². Expanding their Laplacians leaves

```text
-nu a[(Delta chi+2chi_11)sin(phi)
       +2kappa chi_1 cos(phi)
       -(Delta chi_1/kappa)cos(phi)].
```

This independently reproduces all three components of (9), including the
normal cutoff derivative, inverse-frequency derivative and full pressure.
The curl representation directly gives div W=0.

Exact symbolic control used a polynomial cutoff jet with all the relevant
mixed derivatives present:

```text
C=1+x+2y+3z+xy+2xz+3yz+x³+2y³+3z³
  +x²z+xz²+xyz+x²y²+y²z²+z²x².
```

At an arbitrary time slice, its transported time jet is
C_t=-(lambda x partial_x+2lambda y partial_y-3lambda z partial_z)C.
Together with the displayed a' and kappa', this reproduces the residual
identically in all parameters. This polynomial is a local algebra fixture,
not a proposed compact cutoff or numerical solution.

Two omitted-term negative controls passed:

* For chi=1+x3, the corrected linear residual is zero but omission of
  pi_W leaves exactly 8lambda(a/kappa)cos(phi)e1. The pressure term is
  load-bearing even though the wave was constructed as a curl.
* For the linear strip chi=1+x1, self-advection vanishes, while the exact
  residual is -2nu a kappa cos(phi)e3. At nu=a=1, kappa=2 and phase zero,
  it equals -4e3. Omitting viscous envelope differentiation would miss
  this nonzero force.

Adding W.grad W gives the full nonlinear equation. Its complete support
lies where H=Ax, so there is no host-shell cross term. Outside the packet,
the equation is the already paid-for stationary host equation. Both
pressures are compact smooth periodic functions. A global Leray projection
has not been substituted for these actual fields.

## 4. Spatial and Eulerian time bounds, activation and return

The support widths are exactly r exp(lambda t), r exp(2lambda t), and
r exp(-3lambda t). Their product is r³. The source's condition on the
whole finite window is necessary, including any portion before time zero;
the displayed positive-time radius bound alone is not used for that portion.

With the source's rho, kappa_*, K_* and e_loc, the residual terms respectively
cost

```text
lambda a_*/(kappa_*² rho²),
nu a_* K_*/rho,   nu a_*/rho²,   nu a_*/(kappa_* rho³).
```

This verifies (11). In W.grad W the principal wave is in e3 and has no
fast x3 phase derivative. A fast derivative in a cross term is paired with
the inverse-frequency curl correction. Each such term is bounded by
C a_*² rho^(-1)(1+e_loc)². Spatial differentiation preserves this
algebraic cancellation; each further derivative costs at most
M_x=K_*+rho^(-1). This verifies (12) and its differentiated form.

At fixed x, phi_t=-lambda kappa x1 and |kappa x1| <= C Kr throughout
the moving support. The phase time cost is consequently lambda Kr,
not merely the material rate lambda. The amplitude costs
lambda+nu K_*², envelope differentiation costs lambda, and activation
costs Delta^(-1). Repeated mixed differentiation is bounded by the
stated M_x^p M_t^m. Cutoff derivatives through p+m+3 suffice for the
linear residual; the nonlinear term requires no larger cutoff order.
This verifies the Eulerian mixed estimate (14).

For alpha W and pressure alpha pi_W, direct substitution gives exactly

```text
delta f=alpha R_lin+alpha² W.grad W+alpha' W.
```

No pressure time derivative belongs in the momentum equation. The
activation term alpha' W is mandatory. Flat endpoint cutoffs make the
return to H smooth, and the subsequent host cutoff with pressure beta² P_H
gives exactly (15). Counting its spatial derivatives and its time-ramp
derivatives gives (16). The wave and host ramps can be disjoint and smooth
at all joins. One completed finite example can therefore start and end at
rest with smooth compact-time forcing. It is an explicitly globally smooth
forced path, not a breakdown example.

For total mixed order p+m <= P, M_x^p M_t^m <= Q_P. The two restrictions
in (17) bound the linear and quadratic incremental-force contributions by
epsilon_f/2 each. Their minimum is positive for fixed finite parameters.
Reducing a0 realizes that positive choice of a_* while leaving the gain
ratio unchanged. The host and its ramps must still be added to the force.
One fixed example is smooth to all orders; this small-increment choice
controls a prescribed finite list of derivative norms, not one uniform
infinite-stage admissibility schedule.

## 5. Pressure-independent circulation and its restricted consequence

In the specified linear strip, chi_1=c_psi/r1 and all second derivatives
vanish. The other two cutoff factors are identically one there. Thus W has
only its third component, is independent of x3, has zero self-advection,
and pi_W=0. The exact force there is (18). The host force is zero because
this entire strip lies inside the affine core.

Choose consecutive phases 0 and pi inside the strip, and vertical edges
of height h3 lying entirely in its flat x3 portion. Their separation is
pi/kappa. Opposite signs on the vertical edges give circulation
4nu a kappa |c_psi| h3/r1; the horizontal edges contribute zero. Dividing
by the perimeter 2h3+2pi/kappa, and using kappa h3 >= pi, proves (19).
For any alternative periodic pressure, the added force is a gradient and
its circulation around this contractible loop vanishes. The lower bound
therefore applies to every pressure choice for this unchanged velocity.

The geometric hypotheses must remain in the conclusion: the fixed nonzero
linear slope, two required phase points in the strip, a height comparable
to r3 inside the flat portion, and kappa h3 >= pi. With these fixed
constants and a uniform upper bound on the support widths in the fixed
torus, kappa/r1 has a fixed positive lower bound. This gives (20).
The curl also has a sinusoidal component of amplitude
2nu a kappa² |c_psi|/r1, confirming the derivative obstruction independently
of pressure.

Consequently, an accumulating sequence whose complete velocity retains
this same strip on its alpha=1 gain intervals cannot have a_out tend to
infinity while the full force remains bounded through a finite terminal
time. This conclusion does not follow for a redesigned velocity merely
because part of it resembles the current wave. Additional older fields or
velocity corrections may alter or cancel (18); those changes require a new
complete residual calculation. The lower bound is invariant under changing
pressure, not under changing velocity.

## 6. Verdict and remaining obligation

The finite construction, mixed-force estimates, positive finite gain margin,
host cost and restricted unchanged-strip obstruction pass this review.
They give neither an unforced realization of the held host nor a completed
smooth-force singularity construction. Genuine three-dimensional geometry
has been achieved, but this particular localized stage still pays a
necessary viscous force cost. An infinite construction needs a different
complete velocity/force mechanism and a common all-order terminal budget.
ROOT, `(E′)` and FORCED-D remain OPEN.
