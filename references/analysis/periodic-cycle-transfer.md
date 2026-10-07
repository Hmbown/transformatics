# Actual periodic cycle transfer, with pressure and a short-time remainder

8 September 2026. Bounded written calculation, independently reviewed by
the coordinating agent at its stated finite scope. This is AI-agent
review, not external expert acceptance or formal PDE certification.
The [review record](periodic-cycle-transfer-review.md)
pins the source before this link was added; equations are unchanged.
This evolves an actual ordinary-viscosity unforced periodic NS
solution. It does not retain the three independent Kelvin amplitudes by
applying their missing nonlinear force. The generated reverse modes are
part of the solution, with an explicit pressure-corrected second time jet.
No DNS, infinite cascade, global regularity or breakdown claim is made.
ROOT, E-prime and FORCED-D remain OPEN.

The cyclic sine datum below is a common spatial translation of the
cosine datum in [the original activation example](../navier-stokes/frequency-activation.md).
The new calculation is its full second-order pressure response and
positive-time total enstrophy gain, not a new initial geometry or a
repetition of the first-coefficient activation result.

## 1. One explicit datum and its normalization

On the fixed torus of side 2pi, take nu>0, an integer q>=1 and A>0, with

    u(0,x)=A(sin(qx2),sin(qx3),sin(qx1)), f=0.         (1)

This is smooth, mean zero, divergence free and genuinely depends on all
three coordinates. All three original waves are supplied in (1). No
additional reverse wave is supplied later. Let

    y=qx, tau=Aq t, mu=nu q/A,
    u(t,x)=A U(tau,y), p(t,x)=A^2 Pi(tau,y).

Then U solves ordinary periodic NS with viscosity mu and initial datum
U0=(sin y2,sin y3,sin y1). Integer q makes this an exact repeated pattern
on the same physical torus. Spatial averages retain their normalization;
physical velocity, gradient and time factors are A, Aq and Aq,
respectively. For the uniform local estimates below assume 0<=mu<=1.
The actual physical claim always has nu>0 and hence mu>0.

Set the spatial pressure mean to zero. In the following normalized
formulas write the coordinates as x,y,z and define

    U0=(sin y,sin z,sin x),
    N=(sin z cos y,sin x cos z,sin y cos x),
    T=-(sin y sin^2 z,sin z sin^2 x,sin x sin^2 y).    (2)

## 2. Full first and second time jets

The initial nonlinearity is N=(U0.grad)U0. It is divergence free, so
Pi(0)=0. The first time jet is exactly

    U1:=partial_tau U(0)=-N-mu U0.                   (3)

In particular the reverse edges enter with a negative sign. Their
frequencies have squared length 2. They are produced by the nonlinear
equation rather than prescribed as independent receivers.

Let M=(N.grad)U0+(U0.grad)N. A direct calculation gives

    M=(2sin x cos y cos z-sin y sin^2 z,
       2sin y cos x cos z-sin z sin^2 x,
       2sin z cos x cos y-sin x sin^2 y),
    div M=6cos x cos y cos z.

Differentiating the actual pressure Poisson equation therefore yields

    Pi1:=partial_tau Pi(0)=-2cos x cos y cos z,
    P M=M-grad Pi1=T.                                (4)

Here P is the exact periodic Leray projector. Because Delta N=-2N,
the complete second velocity jet is

    U2:=partial_tau^2 U(0)=T+4mu N+mu^2 U0.           (5)

All cross terms, the first pressure response, and full viscosity are
included. Pi1 has squared frequency 3. T has only squared frequencies
1 and 5, as follows from sin^2 z=(1-cos 2z)/2. The actual solution
has no finite-mode closure: equations (3)-(5) specify its first jets,
and the remainder below contains all subsequent modes.

## 3. Stagnation-point strain and vorticity are different observables

The datum is odd under central inversion. The equation and uniqueness
preserve this symmetry, with pressure even, so U(tau,0)=0 throughout
its classical lifetime. Put

    C=grad U0(0)=E12+E23+E31, C^3=I,
    S0=(C+C^2)/2.

Equations (3)-(5) imply

    grad U(tau,0)
      =C-tau(C^2+mu C)
          +(tau^2/2)(4mu C^2+mu^2 C)+O(tau^3).       (6)

The first generated gradient is the complete reverse cycle -C^2.
At second inviscid order, grad M(0)=2I is exactly cancelled by
Hess Pi1(0)=2I. Omitting pressure creates a false diagonal strain and
even a false nonzero divergence at this order.

The symmetric strain and vorticity satisfy

    S(tau,0)=[1-(1+mu)tau+(2mu+mu^2/2)tau^2]S0
                                                    +O(tau^3),
    omega(tau,0)=[1+(1-mu)tau+(mu^2/2-2mu)tau^2]
                         omega0+O(tau^3),
    omega0=(-1,-1,-1).                               (7)

Thus for mu<1 the stagnation-point vorticity initially grows, while
the symmetric strain initially decreases. This is consistent with
vortex stretching: C omega0=omega0. It is not evidence for an increasing
pointwise strain amplifier. The uniform remainder in section 5 turns
these derivative signs into corresponding sufficiently short finite-time
statements when mu stays a fixed distance below 1.

## 4. Global energy loss and genuinely generated enstrophy

Use unnormalized integrals and V=(2pi)^3. Define

    E(tau)=(1/2)integral |U|^2,
    Q(tau)=integral |S|_F^2
           =(1/2)integral |grad U|^2
           =(1/2)integral |omega|^2.

The equalities for Q use periodic incompressibility. Here
E0=Q0=3V/4 and

    ||N||_2^2=3V/4,
    ||grad N||_2^2=3V/2,
    <U0,N>=0,
    <U0,M>=-||N||_2^2.                              (8)

For the last identity, div N=div U0=0 and integration by parts give
<U0,(N.grad)U0>=0 and
<U0,(U0.grad)N>=-<N,(U0.grad)U0>.
It follows from the complete jets that

    Q'(0)=-2mu Q0,
    Q''(0)=(1+4mu^2)Q0,
    Q(tau)/Q0
        =1-2mu tau+(1/2+2mu^2)tau^2+O(tau^3).        (9)

For example,
Q''(0)=||grad U1||_2^2+<grad U0,grad U2>.
The nonlinear part is ||grad N||_2^2-||N||_2^2=Q0;
it is not obtained by deleting pressure from a pointwise calculation.

More specifically, let P2 project onto the complete squared-frequency-2
shell. Orthogonality and (3)-(5) give

    P2 U(tau)=-tau N+2mu tau^2 N+O_(H1)(tau^3),
    (1/2)||grad P2 U(tau)||_2^2/Q0=tau^2+O(tau^3).  (10)

That shell was absent at time zero. The squared-frequency-1 shell has
enstrophy ratio 1-2mu tau+(2mu^2-1/2)tau^2+O(tau^3).
Its loss and the reverse-shell gain give (9); squared-frequency-5
velocity first appears at order tau^2 and affects energy at order tau^4.

Kinetic energy, however, obeys the exact unforced identity

    E'=-2mu Q<=0.                                   (11)

Enstrophy gain is therefore not kinetic-energy gain, and neither
equation (9) nor (10) supplies an L-infinity velocity amplification
claim. Physical E and Q carry factors A^2 and A^2q^2, respectively.

## 5. A uniform actual-solution remainder

The Taylor signs can be given a positive-time scope without numerical
integration. On the fixed normalized torus choose the full H12 norm.
The standard differentiated energy estimate for divergence-free U is

    d||U||_(H12)/d tau <= C_12 ||U||_(H12)^2.         (12)

The positive viscosity contributes a nonpositive energy term and may
be discarded for this upper estimate. All constants are fixed-torus
Sobolev product constants; U0 is one fixed trigonometric polynomial.
Classical local existence and (12) give universal T0>0 and M<infinity,
independent of 0<=mu<=1, such that

    sup_[0,T0]||U||_(H12)<=M.                        (13)

For example one may choose T0 below
[2C_12||U0||_(H12)]^(-1) and M=2||U0||_(H12), after fixing the norm
convention and standard local-existence constants. No inviscid limiting
argument is needed for the positive-viscosity solutions.

Differentiate the exact projected momentum equation in time. Boundedness
of P in Sobolev spaces, mu<=1 and the product rule successively give

    sup ||partial_tau^j U||_(H^(12-2j))<=C_j(M),
                                      j=1,2,3.      (14)

For instance U_tau is bounded in H10; its differentiated equation
contains the two ordered products of U and U_tau and mu Delta U_tau,
which are bounded in H8. A further differentiation, including both
U_tau products, gives H6. Thus Taylor's integral remainder proves

    ||U-U0-tau U1-(tau^2/2)U2||_(H6)<=C_U tau^3.     (15)

H6 controls the full C1 norm in three dimensions, so (6)-(7) have
the stated genuine pointwise remainders. Likewise

    Q'''=3<grad U_tau,grad U_tautau>
                         +<grad U,grad U_tautautau>

is uniformly bounded by (13)-(14). There is one universal C_Q>=1 with

    |Q(tau)/Q0-1+2mu tau-(1/2+2mu^2)tau^2|
                          <=C_Q tau^3, 0<=tau<=T0.  (16)

The constants are not numerical DNS fits. They can be evaluated from
fixed Sobolev constants, but no optimized numerical threshold is claimed.
Equation (15) also justifies the all-mode remainder in (10).

## 6. A strictly viscous finite enstrophy gain

Take any fixed physical nu>0 and integer q>=1. Choose A so that

    0<mu=nu q/A<=min(1,T0/8,1/(64C_Q)).              (17)

At the actual positive time tau_*=8mu, the quadratic part of (9) is

    Q(tau_*)/Q0=1+16mu^2+128mu^4+remainder.

Equation (16) bounds that remainder in absolute value by
512C_Q mu^3<=8mu^2. Therefore

    Q(tau_*)>=Q0(1+8mu^2)>Q0,
    t_* =tau_*/(Aq)=8nu/A^2.                        (18)

This is an actual unforced positive-viscosity conclusion from the
specified datum. Q initially decreases because Q'(0)<0, then exceeds
its starting value on this proved short interval. The generated reverse
shell contributes the nonlinear gain; it was not independently supplied.

The vanishing relative gain in (18) reflects this particular choice of
a very early time; it is not a limitation of the nonlinear transfer.
A fixed normalized clock gives a uniform finite relative gain. Choose
once

    tau0=min(T0/2,1/(4C_Q),1)>0,
    0<mu<=tau0/16.

In (16), the initial viscous loss is at most tau0^2/8 and the remainder
is at most tau0^2/4. Keeping the positive nonlinear quadratic term gives

    Q(tau0)/Q0>=1+tau0^2/8,
    t0=tau0/(Aq).                                   (19)

The additional 2mu^2 tau0^2 term is positive and was not needed.
Both tau0 and the guaranteed relative gain tau0^2/8 are independent of
mu. This is a fixed finite clock, not an optimized numerical gain or a
claim of arbitrarily large amplification. It also retains positive
physical viscosity by choosing A>=16nu q/tau0.

Both versions pay their explicit high-Reynolds input condition, with all
initial waves present. Neither proves large velocity gain, an inherited
next host, persistent
activation at arbitrarily fine scales, or compatibility of an infinite
sequence. Each fixed A,q defines one actual smooth datum and finite
solution; varying them is not one evolving trajectory.

For a future forced stage the concrete new ingredient is the complete
nonlinear reverse-shell transfer (3)-(5), with its pressure response
and an actual all-mode remainder. Its subsequent coupling, localization
and smooth-force cost must be computed from the resulting full state.
They cannot be replaced by the earlier three independent Kelvin ODEs.

## Exact verification

[The supporting script](checks/check-periodic-cycle-transfer.py)
checks the full projected first/second jets, the pressure omission
countercheck, exact global averages, shell eigenvalues, the margin
at tau=8mu and the fixed-clock margin in (19). The coordinating agent's
independent read checked the jets, pressure, normalizations, uniform
H12-to-time-jet bounds and both finite gain margins. The local existence,
uniform Sobolev bounds and Taylor
remainder are separate written analytic arguments. These checks are
exact algebra, not research DNS or formal PDE certification.
