# Independent review of actual periodic cycle transfer

8 September 2026. The coordinating agent independently read the complete
[periodic-cycle source](periodic-cycle-transfer.md) and
derived its enstrophy coefficients independently. The written finite
result passes, at source SHA-256
`da9ba95df48cc7df48cc1eb4dabf0dfe1665c3756905f4deb6e408438d9f26ef`.
The [exact controls](checks/check-periodic-cycle-transfer.py)
are pinned at
`641b0eeca018efc6df1464d43c6e431b826aa5315dc5ad0d352f281935eeff09`.
This is separate AI-agent review, not external expert acceptance or
formal PDE certification. No research DNS was used.

## Full equation and pressure

The integer-frequency change of variables preserves periodicity and
spatial averages on the fixed torus; it gives normalized viscosity
mu=nu q/A and time tau=Aq t. The initial interaction N is divergence
free and has squared frequency 2, so the first pressure is zero and
U1=-N-mu U0 is exact. Differentiating the full equation gives the two
ordered nonlinear products M, their pressure projection and the
viscous coefficient 4mu N. In particular div M=6cos x cos y cos z,
Pi1=-2cos x cos y cos z and P M=T are consistent with the periodic
Poisson sign and zero pressure mean.

At the odd stagnation point, grad N=C^2 and grad M=2I. The pressure
Hessian cancels that entire second inviscid gradient. The resulting
strain and vorticity coefficients in (7) have opposite initial signs
for mu<1. This does not contradict the pointwise vortex-stretching
identity. Omitting pressure would create a false trace at second order.

## Global moments and actual remainders

The normalization Q=integral |S|^2=(1/2)||grad U||_2^2 is correct for
periodic solenoidal fields. Independent integration by parts gives
<U0,M>=-||N||_2^2 and ||grad N||_2^2=2||N||_2^2, with
||N||_2^2=Q0=3(2pi)^3/4. Consequently

    Q'(0)=-2mu Q0,  Q''(0)=(1+4mu^2)Q0.

The initially absent squared-frequency-2 shell has velocity
-tau N+2mu tau^2 N+O_H1(tau^3). The squared-frequency-5 contribution
first affects energy at fourth order. Kinetic energy nevertheless
decreases by the exact unforced energy identity.

The fixed datum has a uniform H12 local existence bound for
0<=mu<=1. Dropping only the nonpositive diffusion term gives the
viscosity-independent energy bound. Three differentiated equations
then control U_tau in H10, U_tautau in H8 and U_tautautau in H6.
Sobolev products lose no more derivatives than specified. Taylor's
integral remainder therefore controls both the C1 jets and the global
Q remainder, with one finite constant independent of mu in this range.
No numerical trajectory or finite Fourier closure supplies this step.

## Positive-time margins

At tau=8mu, the normalized quadratic gain is 16mu^2+128mu^4. Under
the stated bounds, the cubic remainder is at most 8mu^2; this proves
the early strictly viscous gain.

The coordinating agent also proposed and checked the stronger fixed-clock
version. For

    tau0=min(T0/2,1/(4C_Q),1),  0<mu<=tau0/16,

the adverse linear term costs at most tau0^2/8, the positive quadratic
term contributes at least tau0^2/2, and the remainder costs at most
tau0^2/4. Thus Q(tau0)/Q0>=1+tau0^2/8. The physical time is
tau0/(Aq), and the gain is independent of mu in this specified range.
This removes an unnecessary vanishing-gain restriction, without claiming
large or indefinitely repeated gain.

The output is a full periodic NS state containing all subsequent modes.
It is not a rescaled copy of the initial cycle, a proved next host,
a localized stage, an L-infinity velocity amplification result, or an
infinite construction. ROOT, E-prime and FORCED-D remain OPEN.
