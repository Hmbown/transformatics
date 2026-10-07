# Independent review of the asymmetric cycle's early speed loss

8 September 2026. **PASS at the stated finite written scope.** The
[asymmetric-cycle source](asymmetric-cycle-speed.md)
is reviewed at SHA-256
`7776c7406c1b68a952b267fe34af26e17ab3031a5f3779b63e3081866556cf65`.
Its [symbolic control](checks/check-asymmetric-cycle-speed.py)
was read at SHA-256
`192d25eed1a0ac68001114cf625490e3a138ffac6d8504ae34aa2e66e868857d`.
The coordinating agent separately reproduced that control. This review
also performed a different exact pressure-Poisson calculation, described
below, rather than relying only on another run of the same recurrence.

For each fixed a,b,c>0, the conclusion is a viscosity-uniform positive
short interval on which the actual solution has maximum speed strictly
below its initial value. It includes constant independent phase offsets.
It is not uniform as the amplitudes degenerate, a later-time exclusion,
or an infinite-stage result. These are AI-agent reviews, not external
expert acceptance or a formal PDE certificate. No DNS or source edits
were made in this review.

## 1. Full pressure signs and an independent arbitrary-amplitude check

Let A_j=grad U_(E,j). With the pressure convention in the source,

    -Delta Pi_E=tr((grad U_E)²).

The initial nonlinear term N is solenoidal, so Pi_E(0)=0 and U_1=-N.
Direct differentiation gives the source's complete U_2 and
Pi_1=-2abc cos x cos y cos z. In particular, the second pressure source
has the signs

    2tr(A_1²+A_0 A_2)=-8abc F_abc,
    Delta Pi_2=+8abc F_abc,
    Pi_2=-(4/3)abc F_abc.

The last identity follows because -Delta F_abc=6F_abc. The clarified
source states both the trace source and the Laplacian equation, avoiding
a sign ambiguity.

The supplied Fourier recurrence also has the correct sign. For the
convention Uhat=i v, the physical advective convolution equals -i R_n.
The Euler equation therefore gives v_(n+1)=R_n-m Pihat_n. Enforcing
m.v_(n+1)=0 gives exactly Pihat_n=(m.R_n)/|m|². Binomial factors are
the time product rule. The script's spatial line expansion contributes
i^(m.sigma+1+n), and its separate time factorial is correct. It retains
every generated mode before exact symbolic cancellation. The zero mode
of velocity is conserved by the solenoidal divergence form, with no
pressure divisor there.

For the independent check, form the third velocity jet directly from
the displayed physical lower jets:

    U_3=-A_0 U_2-2A_1 U_1-A_2 U_0-grad Pi_2.

Then compute and invert the full third pressure equation

    -Delta Pi_3=2tr(A_0 A_3)+6tr(A_1 A_2).              (1)

This was evaluated as an exact Laurent polynomial using
sin x=(X-X^(-1))/(2i), cos x=(X+X^(-1))/2 and
partial_x=iX partial_X, and likewise for y,z. Thus it does not use
the supplied fourth-velocity-jet recurrence. There are 68 nonzero
pressure-source modes, with squared frequencies 3,5,9,11; their zero
mode vanishes. Dividing every coefficient by its squared frequency
in (1), then differentiating and evaluating X=i sigma1, Y=i sigma2,
Z=i sigma3, gives identically for arbitrary real symbols a,b,c

    grad Pi_3(p_sigma)=(12/5)H_sigma,
    H_sigma=(ab²c² sigma2,bc²a² sigma3,ca²b² sigma1).     (2)

All eight choices of signs were checked exactly. No amplitude samples,
grid evolution, pressure cutoff or suppressed mode is involved.

The lower pressure contributions can also be read directly from their
trigonometric formulas. Along p+tau v, where
v=(a sigma2,b sigma3,c sigma1), the order-tau³ gradient coefficients are

    tau grad Pi_1:        2H_sigma,
    (tau²/2)grad Pi_2:   -(4/3)H_sigma,
    (tau³/6)grad Pi_3:    (2/5)H_sigma.

They sum to (16/15)H_sigma. This is a genuinely nonlocal pressure
calculation: the last coefficient comes from the complete inverse in
(1), rather than from local strain data alone.

## 2. The pressure calculation independently recovers the quartic value

At the initial corner the pressure is identically zero, grad Pi_1
vanishes to second spatial order, and grad Pi_2 vanishes to first
spatial order. For the actual Euler particle X(tau) beginning there,
smoothness first gives X=p+O(tau). The pressure expansion consequently
gives X''=-grad Pi_E(tau,X)=O(tau³), whence

    X(tau)=p+tau v+O(tau^5).

Substitution of (2) and the lower pressure contributions then yields

    X''=-(16/15)H_sigma tau³+O(tau^4),
    U_E(tau,X(tau))=v-(4/15)H_sigma tau^4+O(tau^5).

Replacing X(tau) by p+tau v changes the velocity by O(tau^5), since
the spatial gradient is locally bounded. Thus the full line expansion
in the source follows independently. Since v.H_sigma=3a²b²c², its
squared-speed quartic coefficient is -(8/5)a²b²c².

The material particle here must not be confused with a maximizing
point. The latter differs from the line already at order tau³; the
next section accounts for the value of that displacement separately.

## 3. All eight moving maxima and their exact isometries

Initially G_0=a² sin²y+b² sin²z+c² sin²x has exactly eight global
maxima. At each one, with D=diag(c²,a²,b²), the source's lower jets give

    Hess G_0=-2D, D³G_0=0,
    grad G_1=2D v, Hess G_1=0, grad G_2=0.

To solve grad G(tau,p(tau))=0, write
p(tau)=p+tau w+tau²z+O(tau³). The first equation is
-2D w+2D v=0, so w=v. The second is -2D z=0, because all three
remaining terms D³G_0[v,v]/2, Hess G_1 v and grad G_2/2 vanish.
Thus p(tau)=p+tau v+O(tau³). The inverse Hessian is legitimate for
fixed positive amplitudes; it is not asserted to be uniformly bounded
as any amplitude approaches zero.

This also checks the cancellation of the misleading quadratic term.
Writing B=a²b²+b²c²+c²a², the fixed-point coefficient is -B.
The displacement contributes -v.Dv+grad G_1.v=-B+2B=B.
The optimized quadratic coefficient is therefore zero. The truncated
field U_0-tau N lacks the true U_2 term and falsely predicts +B.

At the line p+tau v, grad G=O(tau³). Its distance from the true
maximizer is O(tau³), so the value difference is O(tau^6), including
the Hessian contribution. It cannot alter the quartic coefficient.

For each diagonal orthogonal E=diag(e1,e2,e3), choose half-period
shifts with cos delta_j=e_(j-1)e_j. Component i of the datum depends
only on x_(i+1), and
e_(i+1)cos delta_(i+1)=e_i. Therefore U_0(Ex+delta)=EU_0(x),
even when its amplitudes differ. The isometry maps the positive corner
to signs (e3,e1,e2), which exhaust all eight corners. Orthogonal and
translation invariance and smooth uniqueness preserve this identity
for Euler and for ordinary-viscosity NS; reflections cause no exception.

Choose disjoint small balls around the initial maxima with negative
definite Hessians. A compactness gap excludes their complement for a
smaller common time. C2 continuity preserves strict concavity in each
ball, and the implicit-function theorem gives its unique local maximum.
Every global maximum is therefore one of these branches. The isometries
make their values equal, so there is no unresolved branch splitting or
assumption about the maximum of unrelated analytic functions.

For constant phase offsets, translating by (gamma,alpha,beta) produces
(a sin(y+alpha),b sin(z+beta),c sin(x+gamma)). The full maximum-speed
history, including its time constants, is unchanged. The revised source
correctly includes these offsets rather than treating them as an open
repair of the early loss.

The optional polynomial consistency check is also sound. The line's
quartic coefficient is a homogeneous degree-six amplitude polynomial.
Half-period translations make its global value even in every amplitude.
When c=0 the displayed triangular Euler solution is exact, and on the
same corner line its velocity is constant, directly forcing that line
coefficient to vanish. This avoids taking a uniform remainder limit
through a degenerate Hessian. Cyclic relabeling covers the other two
planes. Divisibility by a²b²c² and the equal-amplitude value then recover
the same coefficient. The direct check in (1)--(2) is stronger than this
consistency argument alone.

## 4. Uniform actual remainders and strictly positive viscosity

For each fixed triple, the datum is a fixed trigonometric polynomial.
The H20 local energy inequality is uniform for mu in [0,1], because
mu Delta is dissipative. It gives a common positive lifespan and norm
bound, including auxiliary Euler. Differentiating the full projected
equation through five time orders loses at most two spatial derivatives
per order. The lowest resulting space is H10, well above the product
and spatial-embedding thresholds. This supplies the Taylor remainders
used for velocity, pressure, the lines and the maximum branches; it
does not treat the finite Fourier jets as a closed evolution system.

For W=U_mu-U_E the exact equation can be written

    W_tau+P[(U_mu.grad)W+(W.grad)U_E]-mu Delta W
                                               =mu Delta U_E.

The full H16 energy cancels top transport, retains dissipative
diffusion, and bounds the remaining coefficients by the common H20
norm. It yields ||W||H16<=C mu tau. In H14, the advective terms,
mu Delta(U_E-U_0), and mu Delta W are all bounded by C mu tau;
the last uses mu<=1. Hence

    W_tau-mu Delta U_0=O_H14(mu tau),
    U_mu=U_E-mu tau U_0+O_C2(mu tau²).

The extra time factor is essential; an O(mu) comparison would not
settle the small-mu, small-time sign. Since U_E-U_0=O_C2(tau),

    |U_mu|²=(1-2mu tau)|U_E|²+O_C0(mu tau²).

The multiplier is positive for tau<=1/4. Taking suprema therefore
preserves the uniform error, without needing to locate viscous maxima.
Combined with the Euler quartic expansion this gives

    ||U_mu||infinity²
       =R-2R mu tau-(8/5)P tau^4+O(tau^5+mu tau²),
    R=a²+b²+c², P=a²b²c².

The stated time choices bound the two remainders by (4/5)P tau^4
and R mu tau respectively. Thus the advertised strict upper bound
R-R mu tau-(4/5)P tau^4 follows uniformly for 0<=mu<=1.
All constants may depend on the fixed positive triple.

## 5. Verified scope

For (1,1,2), R=6 and P=4, so the Euler coefficient is -32/5 and
the conservative viscous quartic loss is -16/5, exactly as stated.
For u(t,x)=A U_mu(Aqt,qx), integer q, the physical viscosity relation
mu=nu q/A, speed factor A² and time factor (Aq)^(-1) are correct.
A>=nu q places the positive physical viscosity in the reviewed range.

No mathematical source correction is requested after the pressure-sign
and phase-offset clarifications. This rules out early maximum-speed
gain for the stated fixed-amplitude three-mode family. It does not
rule out later gain, changed frequency or phase geometry, additional
modes, another observable, or a sequence whose amplitudes degenerate
with h. ROOT and the two-track completion conditions remain open.
