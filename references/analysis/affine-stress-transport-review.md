# Independent review of the affine stress-transport calculation

8 September 2026. The coordinating agent independently read the complete
[affine source](affine-stress-transport.md), written by a
separate agent, at SHA-256
`c1f743a776c4b3815b75a5b825d2f591b57bcd2c962e9a4be922ac361436ed46`.
The restricted calculations pass this written review. This is AI-agent
review, not external expert acceptance or a formal PDE certificate.

## Checks of the transport and reconstruction

The deformation satisfies F'=AF with det F=1, so the compact prescribed
stress has exactly the stated Fourier coefficient on K=F^(-T)K0.
Differentiating K.n=0 gives both copies of the pressure correction in
G_K=-A+2K(K^T A)/|K|^2. The projected stress source preserves the same
constraint. The scalar heat factor commutes with this time-dependent
matrix evolution; the matrix propagator itself is not replaced by an
exponential of an integral.

With G=F^(-1)F^(-T), the lift J_G reconstructs the missing K0 coordinate
from K.n=0. Applying P0 F^T to the equation gives exactly
P0 F^T(A^T-A)F^(-T)J_G for the fixed-plane generator. The endpoint dual
row and its backward equation retain both the metric lift and deformation.

For symmetric A(t), the generator vanishes without assuming commutation
at different times. The primary polarization still has the longitudinal
metric correction in equation (7). In the selected two-plane sign case,
K.b=alpha S, the source coefficient is
alpha S(beta+alpha gamma)/m0, and the endpoint metric contraction is
-alpha V_T/m0. Their product gives equation (8), including both factors
of alpha/m0. Positivity uses the stated angle condition and positive
definiteness of the metric; no general rotating-host sign is inferred.

## Checks of the sign reversal

For rigid rotation, b rotates oppositely to K in the laboratory frame.
Thus K.b=s0 cos(2omega t), and the instantaneous normal source is
-c0 s0^2 cos^2(2omega t). Rotating the response back contributes the
additional frame term. On the specified transverse orthonormal basis,
the resulting homogeneous operator is the unit skew rotation in (10).
Direct differentiation of both expressions in (11) verifies the forcing,
the initial conditions, and the endpoint value 3/40 in (12).

The skew propagator has norm one. Bounding the scalar heat difference by
delta(theta-s) and the forcing by s0 gives the normal error
s0^2 delta theta_*^2/2=27pi^2 delta/32. At delta=1/1000 this is less
than 3/80, so the sign reversal persists for the stated positive viscosity.
Including the receiver heat factor costs delta+2delta_p in that bound.
The affine host is not a finite-energy periodic flow; the conclusion is
only a counterexample to the instantaneous-sign inference.

## Checks of the inner identity

Under the stated two-sided decays, every boundary term in the two
integrations by parts vanishes. The coefficient after using the scalar
equation is

    2a [c z^2/P - 4a^2 z^4/P^2],  P=1+a^2 z^4,

which is positive away from zero when a,c<0. The leading VW integral
is a vanishing boundary term, while the WR integral is strictly positive
for a nonzero matched solution. Forward physical time reverses the z
limits, giving the positive factor e. The source correctly retains the
existing datum's exact focus, rather than silently replacing it by the
nearby nominal time.

These identities support the separate actual-flow calculation; they do
not establish its stress comparison, localization, pressure tails or
finite-cone lower bound. They supply no infinite trajectory or new
original datum. ROOT, E-prime and FORCED-D remain OPEN.
