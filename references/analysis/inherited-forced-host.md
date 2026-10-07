# Can the finite three-dimensional stage supply its next host?

8 September 2026. Reviewed bounded calculation for FORCED-D. The
[independent review](inherited-forced-host-review.md) pins
mathematical source SHA-256
`33b99003fe91d9112b61b42350106ddf6145a1b2144ea2c86dfc9c191281e42a`.
Root also independently read the argument and checked the exact nonlinear
residual. Later review-label edits change no equations. This is AI-agent
review of written analysis, not external expert acceptance or a formal PDE
certificate. Physical viscosity nu>0 is fixed. This note studies the **same
fields** in the [finite affine-core construction](threed-forced-stage.md),
whose SHA-256 at this calculation was
`2ba3b8ba2168fadfe1d7225ff59b7e538a6fca1301684a983f5118541b336b59`.
No DNS or infinite construction is supplied. ROOT and FORCED-D remain open.

The outgoing shear really can amplify another receiver. An exact
finite-wavelength calculation below preserves that nonnormal gain, rather
than judging it by its eigenvalues. It also gives a new necessary
transition inequality: in the specified two-wave extension, making the
descendant velocity exceed the parent on a flight with bounded base clock
Theta=lambda tau
costs at least a constant times descendant velocity divided by flight time
in the actual force. This force cannot be removed by changing pressure.
That conclusion concerns the written fields; velocity corrections which
change their interior nonlinear interaction require a new calculation.

## 1. The older state, and what is actually present at its endpoint

Use the source's smooth compact periodic host H, pressure P_H and force
f_H, with

    A=diag(lambda,2lambda,-3lambda), H=Ax on |x|<2R.

The packet W is the exact transported-cutoff curl in source equation (6).
On its plateau, choose phase zero at the fixed central particle x=0. Then

    u=Ax+a(t)sin(kappa(t)x1)e3,
    kappa=K exp(-lambda t),
    D_1(t)=nu K^2(1-exp(-2lambda t))/(2lambda),
    a=a0 exp(3lambda t-D_1),
    s=a kappa=s0 exp(2lambda t-D_1), s0=a0 K.          (1)

We take a0>0 and K>0. The complete older periodic state is H+W, not the
nonperiodic affine expression by itself. Its force is exactly

    f_old=f_H+R_lin+W.grad W,                          (2)

with the full pressure and residual in source equations (8)-(10). The
older host cost and its mixed derivatives have not disappeared at handoff.
In the specified pressure convention, the packet force is supported
strictly inside the host's outer force shell. In particular its addition
does not lower the supremum of f_H on that shell. The source proves

    ||f_H||infinity >= c nu lambda/R,
    ||D^p f_H||infinity
      <= C_p[lambda^2 R^(1-p)+nu lambda R^(-1-p)].      (3)

The lower bound for H alone is pressure independent. The disjoint-support
argument for the *total* force here uses our specified pressure; we do not
infer a shell-local pressure-independent bound from the global H pairing.

At the central particle the full gradient is

    B(t)=A+s(t)E31.                                   (4)

Here Eij maps ej to ei. Its characteristic polynomial is that of A, so
the eigenvalues are lambda, 2lambda and -3lambda. Also

    tr B^2=14lambda^2, det B=-6lambda^3,
    ||(B-B^T)/2||_F=|s|/sqrt(2).                      (5)

Thus an orthogonal change of physical frame cannot turn B into a
symmetric diagonal host with error o(|s|). For every symmetric C,
||B-C||_F>=|s|/sqrt(2). Exact similarity to another member of the stated
diagonal family forces its rate to equal lambda. Neither statement
excludes nonnormal transient amplification; section 3 calculates it.

The local approximation also has a definite radius and higher jets. On
a central ball of radius r_next contained in the plateau,

    ||grad u-B||infinity <= |s| kappa^2 r_next^2/2,
    ||u-Bx||infinity <= a kappa^3 r_next^3/6.           (6)

For a relative gradient tolerance delta, kappa r_next<=sqrt(2delta)
is sufficient. Higher spatial derivatives retain their a kappa^m cost.
A large endpoint matrix does not supply an independently chosen next
flight, arbitrary radius, or an all-orders affine approximation.

## 2. Actual deformation, support loss and receiving covectors

The source cutoff follows exp(tA), but particles follow the **full** u.
As long as a particle stays on the plateau, define

    I(t)=integral_0^t exp(3lambda v)a(v)dv.

Its exact trajectory from X=(X1,X2,X3) is

    x1=exp(lambda t)X1, x2=exp(2lambda t)X2,
    x3=exp(-3lambda t)[X3+sin(KX1)I(t)].               (7)

The actual deformation matrix is therefore

    F_u(t,X)=diag(exp(lambda t),exp(2lambda t),exp(-3lambda t))
               +K exp(-3lambda t)I(t)cos(KX1)E31.    (8)

It has determinant one but is not exp(tA). If the flat part of the
initial cutoff contains |Xi|<=c_0 r, the exact plateau test is

    |X1|,|X2|<=c_0 r,
    sup_(0<=v<=t)|X3+sin(KX1)I(v)|<=c_0 r.            (9)

For example an entire initial ball of radius b stays there if
b[1+K sup I]<=c_0 r. The central particle stays there exactly, but a
neighborhood must pay this shear displacement. This sufficient ball
condition is not claimed to be the largest possible shaped core. The
Eulerian packet widths themselves remain
r exp(lambda t), r exp(2lambda t), r exp(-3lambda t); they obey the
source's separate containment condition sqrt(3)r exp(2Theta)<R.

A phase initially with covector xi_0 is transported by the full velocity
according to xi=F_u^(-T)xi_0. At a fixed initial point this is

    xi1=exp(-lambda t)[xi01-K I(t)cos(KX1)xi03],
    xi2=exp(-2lambda t)xi02,
    xi3=exp(3lambda t)xi03.                           (10)

Thus a generic receiver with xi03 nonzero has at least the heat clock

    nu integral_0^t |xi(v)|^2dv
       >= nu |xi03|^2[exp(6lambda t)-1]/(6lambda).    (11)

The contracting kappa history in (1) is not its history. The shear term
in xi1 also remains, with its possible signed cancellation, in the full
clock. A different receiving orientation must use (10), not the parent
wave's scalar diffusion factor.

One can diagonalize B with P=I+[s/(4lambda)]E31. This is not a rotation:

    B=P A P^(-1),
    M=P^(-1)P^(-T)
      =[[1,0,-c],[0,1,0],[-c,0,1+c^2]], c=s/(4lambda).

For x=P(t)y and u(t,x)=P(t)v(t,y), with C=P^(-1)P', the exact transformed
equation is

    v_t+(v-Cy).grad_y v+C v+M grad_y p
       =nu M:D_y^2 v+P^(-1)f.                       (12)

The pressure, diffusion and time-dependent-coordinate terms all change.
The two nontrivial eigenvalues of M have product one and sum 2+c^2;
their ratio grows like c^4. The physical frequency is P^(-T)eta and its
viscous rate is nu eta^T M eta. This conditioning cannot be erased by
renaming a nonorthogonal coordinate system as a physical affine host.

## 3. A surviving principal shear amplifier

Along the center, the pressure-correct principal polarization equation is

    xi'=-B^T xi,
    b'=-B b+2xi (xi.Bb)/|xi|^2-nu|xi|^2b,
    xi.b=0.                                         (13)

Choose xi(0)=L e2 and b(0)=b10 e1. Then
xi=L exp(-2lambda t)e2, b2=0 and the pressure term is zero. Set

    D_r(t)=nu L^2[1-exp(-4lambda t)]/(4lambda).

Direct integration gives

    b1=b10 exp(-lambda t-D_r),
    b3=-b10 exp(3lambda t-D_r)
              [s0/(nu K^2)] [1-exp(-D_1(t))].        (14)

Indeed integral_0^t s(v)exp(-4lambda v)dv
=s0[1-exp(-D_1)]/(nu K^2). For fixed positive Theta=lambda t and
nu K^2/lambda of order one, this transfer can have size s0/lambda.
Unchanged eigenvalues do not bound it by an absolute constant.

Equation (14) is a central principal calculation. In particular the
cos(kappa x1) variation of the host can carry an order-one diffusion
cost when nu K^2 is comparable to lambda. The next section retains
that variation exactly instead of asserting a uniform arbitrary-error
or finite-wavelength estimate from (14).

## 4. An exact finite-wavelength descendant, with its full interference

On the same plateau put ell(t)=L exp(-2lambda t) and add

    V_flat=b(t)sin(ell x2)e1
              +c(t)cos(kappa x1)sin(ell x2)e3,
    b=b0 exp(-lambda t-D_r),
    c=-[b0 a0 K/(2lambda)](1-exp(-2lambda t))
                             exp(3lambda t-D_1-D_r). (15)

Both terms are solenoidal. At t=0 only the b0 receiver is supplied; c=0.
The full viscous linearization about (1), not just its center, gives

    b'=(-lambda-nu ell^2)b,
    c'=[3lambda-nu(kappa^2+ell^2)]c-b a kappa.         (16)

These identities hold with zero additional interior pressure. They prove
(15) by direct integration. The descendant has two physical Fourier
covectors (kappa,ell,0) and (-kappa,ell,0), each with the exact heat clock
D_1+D_r. Its velocity gain relative to the input b0 is

    |c(t)|/|b0|=[s0/(2lambda)](1-exp(-2Theta))
                                      exp(3Theta-D_1-D_r). (17)

This is a real finite-wavelength nonnormal gain. It may be arbitrarily
large on a freely supplied sufficiently large s0. The nonlinear equation
nevertheless has the additional exact term

    V_flat.grad V_flat
       =-b c kappa sin(kappa x1)sin^2(ell x2)e3.       (18)

The parent self-interaction vanishes, parent-on-receiver transport in e3
vanishes, and receiver-on-parent transport is exactly the source already
included in (16). No other interior nonlinear term is omitted. Thus
u=Ax+a sin(kappa x1)e3+V_flat has **precisely (18)** as its interior
force, with the background quadratic pressure. It is generally nonzero
and not a gradient. A linearized amplifier cannot discard it.

The new central gradient is

    A+sE31+beta E12+gamma E32,
    beta=b ell, gamma=c ell.                         (19)

The nonnormal network is larger, but its characteristic polynomial is
still that of A (permute the coordinate order to 2,1,3). More usefully,
its exact amplitude ratios distinguish three objectives:

    |c|/a = [|b0|K/(2lambda)](1-exp(-2Theta))exp(-D_r),
    |gamma|/s = [|b0|L/(2lambda)]
                     (1-exp(-2Theta))exp(-Theta-D_r). (20)

Consequently a descendant gradient at least s requires the actual
incoming receiver gradient |b0|L>=3sqrt(3)lambda: the maximum of
exp(-Theta)(1-exp(-2Theta)) is 2/(3sqrt(3)), and D_r>=0.
That receiver can be small relative to a much larger s0, but it is not
a free infinitesimal perturbation relative to lambda. Making its
frequency large also increases D_r. Equation (20), rather than just
(17), is the relevant parent-to-descendant comparison.

## 5. Complete periodic realization and every mixed force derivative

Here is a compact realization of (15); localization is not deferred.
Use the same transported bump chi as the parent, and let

    eta_+=(kappa,ell,0), eta_-=(-kappa,ell,0),
    A_b=-(b/ell)cos(ell x2)e3,
    A_c=(c/2) sum_(sigma=+,-)
            [(eta_sigma cross e3)/|eta_sigma|^2]cos(eta_sigma.x),
    V=curl[chi(A_b+A_c)].                             (21)

On the common plateau this is exactly (15), since
cos(kappa x1)sin(ell x2) is the half-sum of the two displayed sine modes.
The compact curl is solenoidal, mean zero and periodic. Keep the parent's
pressure P_H+pi_W; take no new pressure. Then the exact full increment is

    delta f=(partial_t-nu Delta)V
          +(u_old.grad)V+(V.grad)u_old+(V.grad)V.     (22)

This is a specified physical force, with no projection tails or missing
pressure reconstruction. Its support remains inside |x|<R when the
source containment holds. On the plateau it equals (18).

For clarity, the following deliberately coarse upper bound charges the
entire cutoff defect, even terms which cancel in the interior. On a
fixed window with dimensionless length at most Theta_bar set

    rho=min_i,t r_i(t),
    mu_*=min_t min(kappa,ell)>0,
    K_*=max_t kappa, L_*=max_t ell,
    e=1/(mu_*rho), Z_*=sup_t(|b|+|c|), a_*=sup_t a,
    M_x=K_*+L_*+rho^(-1),
    M_t=lambda[1+(K+L)r]+nu(K_*^2+L_*^2)+a_*K_*+Delta^(-1).

Assume e<=c_0<1 and the complete support stays inside the host core.
The coefficients satisfy, at every fixed order,

    ||D_x^p partial_t^m V||infinity
       <= C_(p,m,Theta_bar) Z_*(1+e) M_x^p M_t^m.

The term a_*K_* bounds the coupling b a kappa in c'; it is essential
when c initially vanishes. Coefficient differentiation then proves the
stated bounds inductively from (16). Eulerian phase differentiation
pays lambda(K+L)r, the inverse covectors in (21) pay lambda, and cutoff
derivatives pay rho^(-1) spatially and lambda in time.

If V is activated or removed by alpha(t), with derivatives at order j
bounded by C_j Delta^(-j), the exact increment becomes

    alpha[(partial_t-nu Delta)V
               +(u_old.grad)V+(V.grad)u_old]
          +alpha^2 V.grad V+alpha' V.

For each fixed p,m its norm is at most

    C_(p,m,Theta_bar) M_x^p M_t^m
      { Z_*(1+e)[M_t+lambda R M_x+lambda+nu M_x^2]
             +(2a_*Z_*+Z_*^2)(1+e)^2 M_x }.          (23)

This follows by differentiating the displayed exact increment, using
||H||infinity<=C lambda R, ||grad H||infinity<=C lambda,
and the analogous explicit-curl derivative bound for W. Since
rho<=R, spatial derivatives of H obey the same upper factors. The
activation derivatives are covered by Delta^(-1) in M_t. This bound
includes ordinary viscosity, all primary/descendant/curl interactions,
and every Eulerian mixed derivative; it is not a material-derivative
substitute. Fixed constants depend only on the bumps, order and stated
finite window. Add the **old** complete force bounds (3) and source
equation (14) to (23) to obtain the full force budget. Host ramps, if
chosen, additionally pay source equation (16).

Small b0 makes this finite increment small through any fixed derivative
order, since b,c are both linear in b0. It simultaneously makes both
ratios in (20) small. There is no terminal-force conclusion from this
small increment on a fixed enormous older state.

## 6. A pressure-independent transition cost for these exact fields

Suppose the common plateau contains the following loop at the outgoing
time tau=Theta/lambda: fix x2=pi/(2ell), take x1 from -pi/(2kappa) to
pi/(2kappa), and use two vertical sides of length h3 with kappa h3>=pi.
All four sides must remain in the plateau. These are explicit finite
geometry requirements, achievable when its phase widths are large
enough; no circulation assertion is made if the loop does not fit.

For (18), the circulation magnitude is 2|bc|kappa h3, while the perimeter
is 2h3+2pi/kappa. Every smooth pressure change has zero circulation.
Therefore the **total actual force**, for any such pressure change,
satisfies

    ||f(tau)||infinity >= |b(tau)c(tau)|kappa(tau)/2
      = lambda |c(tau)|^2/[a(tau)(exp(2Theta)-1)].     (24)

The equality follows exactly from (15); no upper bound has been
interpreted as a lower bound. At this loop the host force and every
cutoff correction vanish. This isolates the nonlinear cost independently
of the parent's separate boundary-viscosity obstruction.

Let a_j be this parent's outgoing velocity amplitude, d_j=|c(tau)| the
descendant amplitude, and F_j=||f(tau)||infinity. For every transition
of this form with bounded base clock Theta=lambda tau<=Theta_bar,
(24) implies

    d_j^2 <= 2 exp(2Theta_bar) F_j tau_j a_j.          (25)

We used exp(2Theta)-1<=2Theta exp(2Theta_bar). If the desired transition
has d_j>=q a_j for a fixed q>0, it necessarily satisfies

    d_j <= [2 exp(2Theta_bar)/q] F_j tau_j.            (26)

Thus these very same localized fields cannot give an accumulating
sequence of bounded-base-clock, parent-comparable increasing-velocity
handoffs with bounded total force: tau_j tends to zero, and bounded
F_j in (26) instead makes d_j tend to zero. This remains true even if
lambda varies between proposed stages; it does not assume a positive
uniform lower bound on lambda. Allowing enormous older amplitudes while
keeping d_j/a_j tiny does not meet the parent-comparable transition test.

There is also a bound for a small relative descendant. On the plateau
rectangle used above, sin(ell x2)=1 is attained and kappa x1 covers an
interval of length pi. The exact supremum of the absolute combined
vertical wave is therefore

    A_new=sqrt(a^2+|c|^2).

This is the vertical-wave amplitude, excluding Ax and the supplied
horizontal receiver b. Since |c|^2/a=(A_new-a)(A_new+a)/a>=2(A_new-a),
equation (24) also gives

    A_new-a <= exp(2Theta_bar) F_j tau_j.              (26a)

Thus its added vertical amplitude costs force times flight duration
even when |c|/a is tiny. This is a stage inequality; summing it along
one solution first requires the actual mixed outgoing profile, all
older components and support to match the next stage's input. No such
unproved matching is hidden in (26a). The bounded base clock here is
lambda tau, not the integrated norm of the full shear gradient.

Equations (24)-(26) are restricted to the exact construction, a surviving
plateau loop, and activation equal to one at measurement. They do not
rule out a different full evolution whose velocity corrections cancel
(18), a changed geometry without that loop, or flights with unbounded
Theta. Such changes must supply their own gain, support, heat and mixed
force budget. Pressure alone and the already priced exterior cutoff
cannot cancel this particular circulation.

## 7. Same-field handoff and the surviving research question

Merely restarting (1) with the existing single wave requires

    lambda_(j+1)=lambda_j,
    K_(j+1)=kappa_j(tau_j), a_(j+1)(0)=a_j(tau_j),

up to compatible phase/sign conventions, and it must retain the actual
outgoing cutoff shape. The original isotropic bump does not reset
itself. Along that same unaltered evolution,

    a(t)=a0 exp[3lambda t-nu integral_0^t kappa(v)^2dv]
         <= a0 exp(3lambda t),
    kappa(t)=K exp(-lambda t).                       (27)

Relabelling finite subintervals cannot create a diverging velocity or
a finer phase at a finite total physical time. Turning the wave off
returns H, with the same lambda, and pays alpha'W. Replacing H by a
new scaled host changes the actual global state and reintroduces its
force/transition cost. Neither operation is inheritance.

The receiver in sections 4-6 improves this analysis: it really transfers
strain through the existing shear and includes a generated mixed mode.
But the full force cost (25), the actual receiver input, covectors and
cutoff are part of that very same transfer. The new gradient (19) is
not the diagonal host stipulated for the original stage.

There is also a useful exact check on cancelling the interior defect
dynamically. In the unlocalized affine calculation take

    u1=lambda x1+b(t)sin(ell x2), u2=2lambda x2,
    u3=-3lambda x3+v(t,x1,x2).

Keeping (16)'s b equation, the complete unforced interior equation is

    v_t+[lambda x1+b sin(ell x2)]v_1+2lambda x2 v_2
                    -3lambda v=nu( v_11+v_22 ).      (28)

For bounded smooth v on R2 the parabolic maximum principle gives
||v(t)||infinity<=exp(3lambda t)||v(0)||infinity.
Its drift is smooth and at most linear on every finite interval; the
bound follows equally by the corresponding transport-diffusion
representation. The full completion creates additional modes, rather
than permitting the first linearized descendant to grow without its
feedback. Equation (28) permits very large gradient distortion, but
only the original finite lambda velocity-growth clock. It is an
interior affine calculation, **not** a global assertion about the
compact three-dimensional periodic field: localization introduces
additional components and feedback outside the plateau.

The remaining useful target is a genuinely inherited full three-
dimensional coupling which changes this one-way interior structure,
with a quantitatively useful next velocity gain after its feedback is
included. It must track a real next seed or its smooth activation,
the actual core and covectors, and the same complete force through
all transitions. The finite-depth profile construction may alter a
specified wave defect after its hypotheses are proved for the new
host; it cannot be assumed to cancel (18), replace the older host, or
pay for a different receiving wave without those calculations.

## Verification scope

Exact symbolic differentiation checked all three amplitude equations
(1), (16), the matrices (5), (12), (19), the entire ordinary NS interior
residual (18), the two ratios (20), and the endpoint identity in (24).
The threshold 3sqrt(3) was checked at Theta=(log 3)/2. The trajectory
and covector equations were derived by direct integration and matrix
inversion, and their central ODEs passed symbolic substitution. The
curl realization, finite-order product bounds and loop
argument are written analytic calculations, not a formal certificate.
No arbitrary-error polynomial bound, global continuation from an
interior model, infinite smooth-force construction or NS solution
claim is used.

Independent agent review reproduced the full residual, compact-curl
signs, ratios, threshold, moving-coordinate metric and circulation
identity, and checked the mixed force bound at its stated scope. Eight
separate symbolic checks passed. That review and the coordinating
review both confirmed (26a), including its plateau-phase and vertical-
wave qualifications. The review requested the explicit distinction
between the base clock lambda tau and the full gradient clock, now
included above. This is a restricted written calculation, not a full
proof certification.
