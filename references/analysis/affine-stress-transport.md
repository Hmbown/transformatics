# Exact affine transport of a rank-one stress: invariants and a sign reversal

8 September 2026. **Exact finite affine-model calculations.** These formulas
retain the full linearized pressure, the changing covector and ordinary
positive viscosity. They do not replace the actual-q propagator or prove
that a localized NS stress has the prescribed form for a whole flight.
No DNS, infinite trajectory, or closure of ROOT, `(E′)` or FORCED-D is
claimed.

The [independent coordinating-agent review](affine-stress-transport-review.md)
passed at this written model scope and pins the source before this review
link was added. Equations and estimates are unchanged. This is AI-agent
review, not external expert acceptance or formal PDE certification.

Section 5 independently checks an inner coefficient communicated by the
separate `outgoing_outer` agent. It is a signed inner-model identity, not
an actual postfocus source theorem.

## 1. Prescribed affine host and exact Kelvin forcing

Let A(t) be a smooth real trace-free matrix on [0,T], and take nonzero
initial covectors xi0 and K0. Let

```text
F'=AF,   F(0)=Id,   det F=1,
xi(t)=F(t)^(-T)xi0,
b'=-Ab+2xi(xi.A b)/|xi|²,   xi0.b0=0.
```

F is the actual matrix solution, not exp(integral A) unless the matrices
commute. The affine background is x'=A(t)x. For a general A, its own
momentum residual is not being asserted to vanish. The calculation below
is the exact linearized incompressible operator about this prescribed host.

To make a compact stress field rather than a point mass, take a fixed
smooth compact scalar envelope Gamma and prescribe

```text
S(t,x)=b(t) tensor b(t) Gamma(F(t)^(-1)x).
```

With the unnormalized Fourier transform on R³ and K(t)=F(t)^(-T)K0,

```text
S_hat(t,K(t))=Gamma_hat(K0) b(t) tensor b(t).
```

This is exact because det F=1. A transported center X(t)=F(t)X0 adds
only the fixed phase exp(-iK0.X0). No claim about the actual receiver's
envelope being an exact affine transport is used here.

Let v be the zero-initial-data solution of the forced linearized equation

```text
partial_t v+(Ax).grad v+A v+grad p-nu Delta v=-div S,
div v=0,                         nu>0.
```

Along K(t), set v_hat(t,K(t))=-i Gamma_hat(K0) n(t). The real amplitude
n satisfies

```text
n'=G_K n-nu|K|²n+Pi_K b(K.b),        n(0)=0,
G_K=-A+2K(K^T A)/|K|²,             K.n=0,
Pi_K=Id-K tensor K/|K|².                         (1)
```

For a general complex envelope coefficient the same factorization remains
valid; a sign of an imaginary Fourier component must include that known
factor. A nonnegative even Gamma supported sufficiently close to zero has
Gamma_hat(K0)>0, which will be convenient for the counterexample below.

There are two pressure corrections in (1). Differentiating K.n=0 gives
one contribution from K'=-A^T K and another from -An, producing the factor
2 in G_K. The forcing also needs Pi_K. Projecting just -An, or omitting
projection of the stress divergence, gives a different equation.

Let M_K(t,s) denote the full homogeneous polarization map between the
moving planes K(s)^perp and K(t)^perp. The exact solution is

```text
n(T)=integral_0^T exp[-nu integral_s^T |K(u)|² du]
       M_K(T,s) Pi_K(s)b(s) [K(s).b(s)] ds.          (2)
```

The scalar heat factor commutes with every polarization matrix, even when
A varies in time. A nonnegative scalar stress weight m(s), for example a
phase-mean heat factor, can simply multiply the integrand. The sign of an
instantaneous component does not determine its sign after M_K(T,s).

## 2. All frame changes in one fixed-plane equation

Put

```text
P0=Pi_K0,       G=F^(-1)F^(-T),       qK=K0^T G K0=|K|²,
J_G=Id-K0 (K0^T G)/qK,
C=P0 F^T n,                       C in K0^perp.
```

Here G is a positive-definite metric matrix; it is not the Kelvin
generator G_K. The exact reconstruction is

```text
n=F^(-T)J_G C.                                      (3)
```

Indeed F^T n differs from C by a multiple of K0, and K.n=0 fixes that
multiple to -K0^T G C/qK. J_G is this metric-dependent lift, not the
Euclidean orthogonal projection P0.

Differentiate F^T n in (1), then apply P0. Every multiple of K0 vanishes.
The exact fixed-plane equation is

```text
C'=H_K C-nu qK C+P0 F^T b(K.b),
H_K=P0 F^T(A^T-A)F^(-T)J_G.                         (4)
```

Thus the remaining homogeneous motion in these coordinates comes from
the antisymmetric part of A, with the full deformation metric retained.
Neither F^T nor J_G preserves the Euclidean norm in general. They cannot
be discarded when translating a coordinate gain or sign back to a
physical component.

For a physical endpoint measurement e.n(T), the terminal fixed-plane
covector is

```text
l_T=P0 J_G(T)^T F(T)^(-1)e.
```

If l solves l'=-H_K^T l backward from l_T, then

```text
e.n(T)=integral_0^T exp[-nu integral_s^T qK(u) du]
           l(s).P0 F(s)^T b(s) [K(s).b(s)] ds.       (5)
```

This displays the entire transported sign test. A positive instantaneous
physical contraction is not a replacement for l(s) in (5).

## 3. A pure-strain invariant and a useful restricted sign case

If A(t) is symmetric at every time, H_K=0. No commutation of matrices at
different times is needed. The homogeneous quantity

```text
exp(nu integral_0^t |K|²) P0 F(t)^T n(t)
```

is constant, and the forced solution becomes

```text
C(T)=integral_0^T exp[-nu integral_s^T |K(u)|² du]
                      P0 F(s)^T b(s) [K(s).b(s)] ds,
n(T)=F(T)^(-T)J_G(T)C(T).                            (6)
```

For the primary inviscid polarization itself, the same calculation gives

```text
F^T b=b0-xi0 [xi0^T G b0]/[xi0^T G xi0].            (7)
```

This is an explicit metric projection, not a claim that b=F^(-T)b0.
The omitted longitudinal term is generally nonzero.

For a concrete sign criterion, normalize xi0=n0 and b0=e0 to orthogonal
unit vectors; a different nonzero b0 magnitude multiplies the stress
response by its square. Choose K0=alpha e0+beta n0, with alpha,beta>0,
and write

```text
m0=|K0|,       w0=(beta e0-alpha n0)/m0,
gamma_s=(n0^T G_s e0)/(n0^T G_s n0),
d_s=e0-gamma_s n0,               S_s=d_s^T G_s d_s>0,
V_T=w0^T G_T w0-(K0^T G_T w0)²/(K0^T G_T K0)>0.
```

Equation (7) gives F_s^T b_s=d_s and K_s.b_s=alpha S_s. The source
in (6) is parallel to w0, with coefficient
alpha S_s(beta+alpha gamma_s)/m0. The endpoint metric lift gives

```text
xi(T).n(T)
 =-(alpha²/m0²) V_T integral_0^T
      exp[-nu integral_s^T |K(u)|² du]
                  S_s(beta+alpha gamma_s) ds.        (8)
```

Here beta+alpha gamma_s=(xi(s).K(s))/|xi(s)|². In particular, if this
angle pairing stays positive, the generated component along the current
primary normal is strictly negative for every T>0. Dividing by |xi(T)|
to use a unit normal does not change the sign. An aligned diagonal strain
has gamma_s=0 and satisfies this criterion. This is a restricted sign
statement; it does not apply to a general rotating host.

## 4. Exact reversal despite one-signed instantaneous normal forcing

The following counterexample keeps the normal direction fixed and retains
ordinary viscosity. Let

```text
J_z=[[0,-1,0],[1,0,0],[0,0,0]],       A=omega J_z,    omega>0,
F(t)=R_z(omega t),
xi0=e3,          b0=e1,
b(t)=(cos(omega t),-sin(omega t),0),
K0=(s0,0,c0),    s0=sqrt(3)/2,       c0=1/2.
```

The receiver equation is exact: xi=e3, xi.A b=0, and b'=-Ab.
Its phase covector may be multiplied by any constant without changing this
polarization. Meanwhile K(t)=R_z(omega t)K0 and |K(t)|=1. The real source
in (1) has normal component

```text
e3.Pi_K b(K.b)=-c0 s0² cos²(2omega t)
             =-(3/8)cos²(2omega t) <= 0.             (9)
```

The coarse covector's normal component never changes sign. Thus a reversal
below cannot be attributed to changing the normal or its orientation.

Rotate the response back by R_z(-omega t), and use the orthonormal basis
u0=(c0,0,-s0), v0=e2 of K0^perp. Put theta=omega t and write

```text
omega R_z(-omega t)n(t)=x(theta)u0+y(theta)v0,
delta=nu/omega.
```

The exact equations, including the frame rotation and pressure, are

```text
x'= y-delta x+(s0/4)(1+cos(4theta)),
y'=-x-delta y-(s0/2)sin(4theta),
x(0)=y(0)=0.                                         (10)
```

The factor 2 in the rotating-frame homogeneous operator is
-2Pi_K0 J_z; restricting it to this plane gives the unit rotation in
(10). Using only the laboratory -A term would give the wrong frequency.

At delta=0, the exact solution is

```text
x(theta)=(s0/10)[sin(theta)+sin(4theta)],
y(theta)=s0[(1/10)cos(theta)+(3/20)cos(4theta)-1/4].    (11)
```

Direct differentiation verifies (10) and its initial conditions. At
theta_*=3pi/2,

```text
omega e3.n(theta_*/omega)=-s0 x(theta_*)=3/40>0,      (12)
```

opposite to every nonzero instantaneous normal source in (9).

Positive viscosity does not remove this counterexample. The exact solution
of (10) is the rotation Duhamel integral multiplied by
exp[-delta(theta-s)] inside the integral. Its forcing vector has norm at
most s0. Since 1-exp(-z)<=z for z>=0, its normal difference from (11)
at theta_* is at most

```text
s0² delta theta_*²/2=27pi² delta/32.                  (13)
```

For delta=1/1000, this is less than 3/80. Hence the true viscous response
still obeys e3.n(theta_*/omega)>3/(80omega)>0. At any prescribed nu>0,
choose omega=1000nu to obtain this example. The envelope coefficient
Gamma_hat(K0)>0 simply multiplies the Fourier response. In terms of the
physical complex coefficient v_hat=-i Gamma_hat(K0)n, the corresponding
imaginary normal component reverses sign as well.

If the receiver's own scalar heat attenuation is included, its stress
has the additional factor exp(-2delta_p theta), with
delta_p=nu|xi0|²/omega. The same estimate replaces delta by
delta+2delta_p in (13). Choosing omega sufficiently large preserves the
reversal with both heat clocks present. This observation does not turn the
prescribed compact stress into a complete nonlinear solution.

The rigidly rotating affine host itself has an exact quadratic pressure,
but is not a finite-energy or periodic global velocity. This is a counterexample
to a proposed sign inference for the affine transport operator, not a
Navier–Stokes breakdown construction or an actual-q counterexample.

## 5. A distinct inner coefficient with a strict sign

In the inner receiver notation, let a<0, c<0 be fixed and put

```text
P(z)=1+a²z⁴,       W=-V',
W'=[(2a²z²+2c)V-4a²z³W]/P,
R=-2azV+az²W.                                       (14)
```

Here R is a component label, unrelated to a support radius. Assume the
selected solution has the incoming decay V=O(z^(-2)), V'=O(z^(-3)) as
z tends to positive infinity, and outgoing decay V=O(|z|^(-1)),
V'=O(|z|^(-2)) as z tends to negative infinity. These are the boundary
conditions supplied by the matched inner branch. All integrals below
converge.

The apparently leading source cancels exactly:

```text
integral_(-infinity)^infinity V W dz
 =-(1/2)[V²]_(-infinity)^infinity=0.                 (15)
```

The other component does not cancel. Since (14) is equivalent to
(P V')'+(2a²z²+2c)V=0, integration by parts gives

```text
integral W R dz
 =a integral [z²(V')²-V²] dz
 =2a integral [c z²/P-4a²z⁴/P²]V² dz > 0            (16)
```

for every nonzero such V. To check the coefficient explicitly,

```text
z²(2a²z²+2c)/P-(1/2)(z²P'/P)'
 =2c z²/P-8a²z⁴/P².
```

The boundary terms zV², z²VV' and z²(P'/P)V² vanish at both infinities
under the stated decays. Because a,c<0, the integrand coefficient after
multiplication by 2a is positive for z!=0. A nonzero solution cannot be
supported only at z=0, so the integral is strictly positive.

Write z=(t_c-t)/e with e>0, where t_c is the focus actually prescribed
by the seed data. In the original seed and outer-matching notes that
time is t_c=(2/mu)log ell-ell^(-3/4), also denoted t_f in the canonical
logarithmic host. The nominal time (2/mu)log ell differs by o(e) when e
is comparable to ell^(-1/2). That asymptotic shift must not be silently
inserted into an exact covector condition or used to change the datum.
Physical time has dt=-e dz and moves from large positive to negative z.
Consequently the complete time-oriented integral is +e times (16), not
its negative.

This identity was proposed by `outgoing_outer` and independently derived
here. It supplies a candidate stable-channel sign where the leading
growing-channel contribution is a boundary term. Finite matching errors,
outer tails, Floquet basis conversion, ordinary damping and the comparison
to an actual-q transported source remain separate estimates. Equation
(16) alone does not prove a nonzero actual postfocus output.

## 6. What these formulas permit

The useful invariant is (6) for symmetric hosts. The general replacement
is the exact transported pairing (5). The rotation example proves that
one-signed instantaneous normal forcing does not imply a one-signed
endpoint response, even with positive viscosity and a fixed normal.
The distinguished inner coefficient (16) gives a concrete alternative
sign to test after the full matching and transport estimates.

Exact symbolic checks verified the rotation equations and solution, the
viscous comparison coefficient, and the inner integration-by-parts
coefficient. Exact rational checks in a nonorthogonal deformation frame
also verified transversality, the metric lift, the fixed-plane generator,
endpoint duality and the factors in (8). The source is an affine-model
note: localization errors,
nonlocal actual pressure, the actual full-Q stress and the necessary
postfocus comparison are not replaced by these identities.
