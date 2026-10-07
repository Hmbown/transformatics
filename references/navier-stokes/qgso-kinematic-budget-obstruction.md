# A solenoidal path with exact E/Q/D balances and a nonzero NS residual

**ROOT, `(E′)`, and Q-GSO averaged noncollapse remain OPEN.** The path
constructed here is **not a Navier–Stokes solution**. Its full PDE residual
has nonzero curl. Its purpose is to determine whether the failure of the
previous scalar closure disappears when the budgets are realized by an
actual divergence-free spatial field. It does not.

The conclusion is restricted: energy, enstrophy and strain-gradient
dissipation balances, together with instantaneous solenoidal identities,
do not imply averaged noncollapse for all time-dependent fields satisfying
those inputs. A proof using further NS dynamics or other regularity
criteria is outside this obstruction. No priority claim is made.

The local-energy extension in section 8 supplies one such additional
NS constraint: it excludes this path with an exact, strictly positive
weighted residual. That exclusion has not been extended to general
escape scenarios.

Pins: `experiments/nse_qgso_kinematic_budgets.py`,
`tests/test_nse_qgso_kinematic_budgets.py`,
`artifacts/enstrophy_sup/nse_qgso_kinematic_budgets.json`;
node `nse-qgso-kinematic-budget-obstruction`.

## 1. Statement and definitions

For every `nu>0` there is a positive `T` and a periodic, divergence-free,
mean-zero kinematic path `u(t)` on `(R/(2pi Z))^3`, smooth in space and time
for `0<=t<T`, with all of the following properties:

1. With physical integrals
   `E=||u||_2^2/2`, `Q=||S||_2^2`, `D=||grad S||_2^2`,
   `Z=||Delta S||_2^2`, the three exact balances hold:

   ```text
   E'=-2nu Q,       Q'=P-2nu D,       D'=T_D-2nu Z.     (1)
   P=-(4/3) integral tr(S^3),
   T_D=-integral Delta^2 u . (u.grad)u.
   ```

   `T_D` is the actual inviscid D production functional of this spatial
   field, not an independently assigned scalar. Its equivalent form
   `-2A-4B` is in the preceding transfer-budget note.
2. `Q(t)=A_Q/sqrt(T-t)` and `M(t)=A_M/(T-t)` for positive constants.
   Its completed **kinematic** Q-rung prices have a finite geometric sum.
3. The full NS residual is nonzero for every `t<T`; no choice of pressure
   eliminates it. If pressure is chosen by the usual periodic Poisson
   equation, that residual is orthogonal to `u`, `-Delta u`, and
   `Delta^2 u` at every time. Thus none of (1) detects it.
4. A nonnegative compact streamfunction weight detects a strict failure
   of the local energy inequality, for every pressure choice. The
   normalized residual costs more than `(1/2) log rho` per kinematic
   Q-rung, including for the smooth version.

Instantaneous Betchov, Miller, pressure-orthogonality and the other
applicable spatial identities hold because the fields are solenoidal.
In particular the D balance and square-completion from the preceding
note also hold with the **actual** tensor
`C=P_st[(u.grad)S+S^2+(3/4)omega tensor omega]`.

The proof first constructs an exactly integrable C4 compact prototype,
then produces a C-infinity version by mollification and persistence of
the matching root. The smooth path in the statement is this latter
version. No step identifies either path with an NS evolution.

## 2. Compact divergence-free profiles

On the unit ball in R3, set `v=|y|^2` and

```text
phi_b(v)=(1-v)^6(1+b v),
V_b=curl[phi_b(|y|^2)(-y2*y3,y1*y3,0)],                (2)
```

and extend by zero outside the ball. The potential vanishes to order
six at the boundary, so `V_b` vanishes to order five. Its zero extension
is C4 and belongs to H3, which is sufficient for all moments below and
their integrations by parts. Its mean vanishes by oddness, and its
divergence vanishes distributionally because it is a curl.

Write `R=y1^2+y2^2`, `z=y3`. Then `V_b=(y1 f,y2 f,g)` with

```text
f=-phi_b(R+z^2)-2z^2 phi_b'(R+z^2),
g=2z phi_b(R+z^2)+2zR phi_b'(R+z^2).
```

In the rest of this section `E,Q,D,Z,P,T_D` denote the fixed profile
moments, not their time-dependent rescalings. They are polynomial
functions of `b`, quadratic for the first four and cubic for the last
two. The instrument derives them exactly. Every monomial integral uses

```text
(1/pi) integral_B1 R^a z^(2j)
  = 4^(a+2) a! (2j)! (a+j+2)! / [j! (2a+2j+4)!],     (3)
```

and odd z powers integrate to zero. This follows by first integrating
`R` from zero to `1-z^2` in cylindrical coordinates and then evaluating
a beta integral. The rational moment polynomials are retained in both
the instrument and receipt. An independent Cartesian vector-potential
calculation verifies them by quadrature.

## 3. Simultaneous matching of all three balances

Let `s=T-t`, and for constants `a>0`, `lambda>0`, define

```text
u(t,x) = a lambda s^-1/2 V_b(x/(lambda sqrt(s))).       (4)
```

Choose `T` small enough that the support stays strictly inside the
fundamental cell. Extension by zero is then an exact periodic field;
there is no periodic-image approximation in its local moment integrals.
For any compact profile in this construction, scaling gives

```text
E(t)=a^2 lambda^5 E sqrt(s),
Q(t)=a^2 lambda^3 Q s^-1/2,
D(t)=a^2 lambda   D s^-3/2,
Z(t)=a^2/lambda   Z s^-5/2,
P(t)=a^3 lambda^3 P s^-3/2,
T_D(t)=a^3 lambda T_D s^-5/2.                         (5)
```

The first two balances in (1) hold identically if

```text
lambda^2=4nu Q/E,
a=(Q^2+ED)/(2QP).                                    (6)
```

The third then holds precisely when

```text
F(b)=(Q^2+ED)T_D-(3QD+EZ)P = 0.                      (7)
```

Direct use of (3) gives `F(b)=c pi^3 f_7(b)` for a positive rational
constant `c`, where

```text
f_7(b) = 20758518849965 b^7
       + 516170124633279 b^6
       + 6138596124777861 b^5
       + 40657377434216463 b^4
       + 163688546826655119 b^3
       + 386285610551598405 b^2
       + 458840954166907455 b
       + 286123964156441325.
```

Exact rational endpoint signs and Sturm root counting prove that
`f_7` has one simple root in

```text
[-220007/50000, -110003/25000] = [-4.40014,-4.40012].  (8)
```

It is also the polynomial's only real root. Zero exclusion and exact
positive samples show that all six profile moments are positive
throughout (8); therefore (6) is well-defined and positive. These are
exact checks, not decisions from floating-point signs. The approximate
labels are

```text
b_* = -4.400130634380...,
a   = 92.32555138...,
lambda^2/nu = 564.66493178....
```

Equations (5)–(8) prove the three balances for **every** `s>0` on the
interval of support containment. They are not a match at finitely many
times. Periodic pressure terms vanish in the integrated budgets, even
though the periodic pressure itself need not obey a simple dilation law.

## 4. A pressure-independent certificate that the PDE is not satisfied

The profile part of the full residual, up to a positive scalar factor
and a pressure gradient, is

```text
R_b = (V_b+(y.grad)V_b)/2 + a(V_b.grad)V_b - beta Delta V_b,
beta=nu/lambda^2=E/(4Q)>0.                            (9)
```

Near the origin write `phi_b(v)=1+c_1 v+c_2 v^2+...`, where
`c_1=b-6` and `c_2=15-6b`. Direct differentiation shows that the
`y1*y3` coefficient of `(curl R_b)_2` is

```text
-28 c_1(1+a) + 504 beta c_2.                          (10)
```

For every b in (8), `c_1<0`, `c_2>0`, and (6) gives `a,beta>0`.
Thus (10) is strictly positive. At the matching root it is approximately
`27213.69`. The exact positivity argument, not this decimal, certifies
that the full residual is nonzero and cannot be removed by pressure.
An independent Cartesian Taylor-jet differentiation checks (10).

Let `p` solve the usual zero-mean periodic pressure Poisson equation and
let `R_NS=u_t+(u.grad)u+grad p-nu Delta u`. By (1) and integration by
parts,

```text
<u,R_NS>=0,
<-Delta u,R_NS>=0,
<Delta^2 u,R_NS>=0,                                  (11)
```

while `curl R_NS` is nonzero. This is the precise missing information:
three vanishing global pairings do not make the vector residual vanish.

## 5. Why an exactly smooth version exists

Convolve the compact velocity profiles with a fixed smooth compact
radial mollifier of radius epsilon, producing `V_(b,epsilon)`. This
preserves divergence, zero mean and compact support. The profiles
converge to `V_b` in H3 uniformly for b in the compact interval (8).
All six moment functionals converge uniformly there; their first
derivatives in b do as well, since the family is linear in b.

For `T_D`, use the equivalent expression
`-<Delta V,Delta[(V.grad)V]>`: it is continuous in H3 in three
dimensions by the H3 product estimates. There is no need to assume
global convergence of fourth derivatives of the zero extension.

The opposite signs of `F` at the two rational endpoints persist for
all sufficiently small epsilon. The intermediate value theorem gives
a root `b_epsilon` between them; simplicity also gives a unique nearby
root and convergence to `b_*`. All positive moments persist. Choose
`a_epsilon,lambda_epsilon` by (6), so (1) remains **exact** for the
mollified path, with no approximation error left in the balances.

On a fixed neighborhood of the origin the original profiles are
polynomials. Their mollifications therefore converge in every local
derivative used in (10). The strictly positive curl coefficient
persists. The smooth path still has a nonzero full NS residual.
Finally decrease T if necessary to contain the enlarged compact
support in the periodic cell. This proves the smooth statement in
section 1. The exact rational receipt pins the prototype; the written
continuity argument supplies the smooth version.

## 6. Completed kinematic prices and the scope of the obstruction

Let `M_b=||sym grad V_b||_infinity`, which is finite and nonzero. No
numerical maximum is needed: at the origin the prototype strain is
`diag(-1,-1,2)`, and this remains nonzero after small mollification.
Define `A_Q=a^2 lambda^3 Q`, `A_M=a M_b`. From (4),

```text
Q=A_Q/sqrt(s),       M=A_M/s.
```

For `rho>1`, consecutive Q-rungs have `s_j=s_0 rho^(-2j)`. Every
time on a rung has `Q'>0`; direct integration gives

```text
Hbar_j = (A_Q/A_M) sqrt(s_j)(1-rho^-1)/log(rho),
sum_(j>=0) Hbar_j = (A_Q/A_M) sqrt(s_0)/log(rho) < infinity. (12)
```

The total Q time-integral is finite and the BKM clock diverges. The
actual Betchov pointwise-in-time global production cap is satisfied
because these are genuine solenoidal fields and their Q balance holds.
Thus adding spatial realizability and all three balances does not
remove the geometric escape within this class of kinematic paths.

This is a restricted insufficiency statement. In particular,

```text
||u(t)||_3^3 = a^3 lambda^6 ||V_b||_3^3
```

is constant. The path does not meet the necessary singular-NS behavior
supplied by the critical-L3 regularity theorem of
[Escauriaza, Seregin and Sverak](https://www.pdmi.ras.ru/~seregin/Recent%20Publications/engESS3.pdf).
It is not claimed to satisfy the complete standard battery, and it is
not an ESS-compatible replacement for the earlier multiscale scalar
ledger. One geometric countermodel is sufficient for the narrower
claim about (1), but it does not defeat an argument using additional
NS information. The need to use more than energy-level control also
appears in [Tao's averaged-equation result](https://arxiv.org/abs/1402.0290);
no properties of that different equation are used in this proof.

## 7. Consequence for the next attack

Do not spend another round merely replacing the abstract scalar D/Z/C
assignments by compatible spatial moments. That repair alone cannot
close Q-GSO: the missing residual can be nonzero while all three
evolution balances and the instantaneous identities hold exactly.
The next proposed estimate must either use actual local NS dynamics
that reject this path or an additional criterion such as critical-L3
control. It must still be tested against the ESS-compatible scalar
escape already in the repository. Neither requirement was discharged
here; the unconditional objective remains unsolved.

## 8. The local energy balance detects the hidden residual

This extension tests an additional necessary NS condition. For a smooth
divergence-free field and any smooth pressure, write `e=|u|^2/2`. The
local energy residual is

```text
L_E = partial_t e + div[(e+p)u] - nu Delta e + nu|grad u|^2
    = u . R_NS.                                      (13)
```

It vanishes for smooth unforced NS. The local energy inequality requires
`L_E<=0` in distributions. The kinematic path fails even that inequality.

To see this without evaluating pressure, use its streamfunction

```text
psi_b(y) = (y1^2+y2^2)y3 phi_b(|y|^2).
```

The cylindrical formula `V_r=-psi_z/r`, `V_z=psi_r/r` proves
`V_b.grad psi_b=0`; smoothness extends it across the axis. Thus the
nonnegative compact weight `psi_b^2` gives both cancellations

```text
integral psi_b^2 V_b . grad p = 0,
integral psi_b^2 V_b . (V_b.grad)V_b = 0.              (14)
```

The first uses integration by parts and the first-integral identity;
the second is the same argument applied to `|V_b|^2/2`. No pressure
symmetry or self-similar pressure formula is assumed.

Define the profile integrals

```text
J0 = integral psi_b^2 V_b . [V_b+(y.grad)V_b]/2,
Jd = integral psi_b^2 V_b . Delta V_b,
W  = integral psi_b^2 |V_b|^2/2,
J  = J0 - beta Jd,        beta=E/(4Q).
```

Exact integration by (3), followed by rational polynomial zero exclusion
on the entire bracket (8), proves

```text
W > 0,        J > W/4 > 0.                           (15)
```

The receipt retains the exact rational functions for `J0,Jd,W,J`.
At `b_*`, `J/W` is approximately `0.2812170773`; the bound in (15)
is certified by exact signs, not that decimal. Cartesian derivatives
and quadrature independently verify the same weighted functional.

For `Phi(t,x)=psi_b(x/(lambda sqrt(s)))^2`, (5), (9) and (14) give

```text
integral Phi u.R_NS = a^2 lambda^5 s^-1/2 J > 0,
integral Phi e     = a^2 lambda^5 sqrt(s) W.           (16)
```

After multiplying Phi by a nonnegative smooth time cutoff supported
inside any rung, (16) contradicts the local energy inequality. The time
dependence of Phi is legitimate: (13) is tested as a distribution, or
equivalently the time derivative of the test function must be retained
when integrating by parts. It is not silently discarded here.

There is also a uniform diagnostic cost on every completed kinematic
Q-rung:

```text
integral_(I_j) [integral Phi u.R_NS / integral Phi e] dt
    = 2(J/W) log(rho) > (1/2) log(rho).               (17)
```

This is a normalized **residual** cost. It is not a dissipation price
or a new regularity criterion for genuine NS solutions, whose residual
is zero.

The exclusion persists for the C-infinity construction. Mollify the
vector potential in (2); curl commutes with convolution, so this gives
the same mollified velocity as section 5. A radial mollifier preserves
its azimuthal form. Set `psi_epsilon=y1 A_(epsilon,2)-y2 A_(epsilon,1)`.
The first-integral identity remains exact, the compact weights are
smooth, and the profile integrals in (15) converge uniformly near the
matching root. The strictly positive gap persists for sufficiently
small epsilon. Hence the **smooth** countermodel also fails local
energy; this is not an artifact of the prototype's support edge.

This weight uses the special geometry of the constructed profile.
The cancellation in (14) has not been extended to arbitrary 3D flows.
It supplies a concrete local test that rejects this path, not the
missing general Q-GSO prefix estimate.

## 9. Local energy equality does not replace the momentum equation

A separate exact example keeps the scope precise. For `nu>0` set

```text
u(t,x,y,z)=exp(-nu t)(0,cos(x+t^2),sin(x+t^2)),  p=0.
```

The field is smooth, periodic, mean-zero and divergence-free. Its
advection and pressure source vanish, while

```text
R_NS=2t exp(-nu t)(0,-sin(x+t^2),cos(x+t^2)),
u.R_NS=0,       |R_NS|^2=4t^2 exp(-2nu t).
```

It satisfies the local energy equality pointwise and violates the full
momentum equation for `t>0`. This is a **decaying shear with no growing
Q-rungs**. It is not a counterexample to any growth-rung regularity
criterion. It establishes only that a local-energy check cannot serve
as a certificate that a proposed field solves the full NS equation.

The current attack therefore supplies an additional local exclusion
but no unconditional bound for genuine NS trajectories. Further work
must retain the full NS dynamics and address the ESS-compatible escape
as well; neither issue is resolved by adding another diagnostic alone.

## 10. Local verification

The regenerated receipt has **36 passing exact algebra/arithmetic
checks**. The four focused modules (kinematic budgets, transfer budget,
prefix audit and growth-set Osgood) have **45 passing tests**, including
independent Cartesian differentiation and quadrature of the weighted
energy residual. Ruff passes on the modified instrument and tests.
`scripts/coverage_audit.py` passes with 351 nodes and the same three
pre-existing attack-path-count warnings. Only the existing kinematic
node changed in the machine graph.

The eight preceding campaign, floor, pressure, transfer and prefix
receipts were checked byte-for-byte against the preceding commit and
are unchanged. These checks provide reproducibility and bookkeeping
evidence, not a substitute for the written analytic arguments.

The C-infinity existence step is the written mollification and
root-persistence proof, not a claim established by finite quadrature.
No new DNS, numerical maximum certificate, hosted CI or NS blow-up
claim is attached to these checks.
