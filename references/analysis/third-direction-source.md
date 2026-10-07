# A third-direction source and the cost of turning its polarization

8 September 2026. Exact Fourier identities and restricted local consequences
for the full, unforced Navier–Stokes equation. This note investigates the
first departure from the invariant two-wave geometry. It does not add a
wave to the already constructed actual solution \(Q_h\), prove a new
handover, or close ROOT or FORCED-D. No DNS is used.

The useful distinction is between **generating a new Fourier coefficient**
and **generating the independent donor needed to do so**. A supplied
third-direction donor generates the missing normal polarization, with an
explicit signed coefficient. All intermediate paths and pressure matter:
one proposed cubic channel cancels at equal frequencies. At the current
unequal frequencies, a separate geometric restriction makes a generated
high-frequency normal component small. These calculations identify what
must be extracted from the actual three-dimensional background; they do
not assert that its coefficient or sign has been established.

## 1. The new input is explicit

Use the frame \((p,r,n)=(e_x,e_y,e_z)\) of
[the existing receiver calculation](generated-receiver.md).
On a fixed \(2\pi\)-periodic torus, take positive integer frequencies

\[
P=\alpha e_z,\qquad Q=\beta e_y,\qquad R=\gamma e_x
\]

and the smooth real datum

\[
u_0=A e_x\cos(\alpha z)
 +(B e_x+C e_z)\cos(\beta y)
 +D e_y\cos(\gamma x).                                      \tag{1}
\]

The first two waves are the frozen outgoing model. The last wave is an
**additional supplied donor**, not a generated field. Here \(A,D\ne0\)
and \((B,C)\ne(0,0)\). All three independent axial wavevectors have
nonzero coefficients, so (1) has no continuous direction of translation
invariance. It is genuinely three-dimensional in this precise sense.
The field is solenoidal, mean-zero, and finite-energy. The viscosity

\[
u_t+\mathbb P\operatorname{div}(u\otimes u)=\nu\Delta u,
\qquad\nu>0,                                                \tag{2}
\]

is fixed. Pressure is periodic. The formulas also apply on an expanding
torus to allowed lattice frequencies, and to the repository's rescaled
equation after replacing \(\nu\) by \(\epsilon=\nu h^4\).

When \(D=0\), the exact invariant reduction in the existing receiver note
prevents production of any \(x\)-dependent mode. A third independent
wavevector cannot arise from sums of \(P,Q\) alone. The actual \(Q_h\)
has a compact background, envelopes and a moving frame, so this invariant
statement does not apply to its complete datum. It does prevent treating
(1)'s last term as a consequence of the frozen two-wave calculation.

## 2. Signed quadratic source with complete pressure

For complex Fourier amplitudes \(a,b\) at \(k,l\), define the complete
unordered cross contribution

\[
\mathcal C(k,a;l,b)
=-i\Pi_{k+l}\big[(a\cdot l)b+(b\cdot k)a\big],
\qquad \Pi_K=I-\frac{K\otimes K}{|K|^2}.                    \tag{3}
\]

This combines both ordered products. If the vector inside the square
brackets is \(V\), its cross pressure coefficient is

\[
\widehat p(K)=-\frac{K\cdot V}{|K|^2}.                    \tag{4}
\]

Each positive initial Fourier coefficient in (1) is half its displayed
cosine amplitude. In particular,

\[
\mathcal C(P,Ae_x/2;R,De_y/2)
       =-\frac{iAD\gamma}{4}e_y.                           \tag{5}
\]

The pressure in this pair is zero because \(P+R\perp e_y\).
The full real cross source is

\[
-AD\gamma\,e_y\cos(\alpha z)\sin(\gamma x).                \tag{6}
\]

The output \(e_y=r\) is precisely the normal component missing from the
old generated \(p\)-polarized sidebands. For the frozen outgoing shear

\[
\mathcal A_Q=-\beta(B e_x+C e_z)\otimes e_y,
\qquad
\mathcal A_Qe_y=-\beta(B e_x+C e_z),                       \tag{7}
\]

it is an algebraically active input. Equation (7) alone does not establish
amplification by the full non-affine outgoing wave; the frequency and
time hypotheses of such an approximation would still need proof.

Let \(U_j\) denote the degree-\(j\) terms in the convergent local expansion
of (2), as defined in
[the existing activation theorem](../navier-stokes/frequency-activation.md#2-the-all-mode-interval-estimate).
Orthogonality gives \(|P+R|^2=|P|^2+|R|^2\), so its exact quadratic term is

\[
\widehat U_2(P+R,t)
=-\frac{iAD\gamma t}{4}
          e^{-\nu(\alpha^2+\gamma^2)t}e_y.                 \tag{8}
\]

Both input heat factors and the output propagator are included. This
coefficient was initially zero. Its leading creation is real PDE
generation, conditional on the explicitly supplied donor \(D\).

## 3. All three cubic paths, including their cancellation

Set \(K=P+Q+R\), and abbreviate the initial coefficients by

\[
a=Ae_x/2,\qquad b=(Be_x+Ce_z)/2,\qquad c=De_y/2.
\]

The complete cubic coefficient at \(K\) is

\[
\widehat U_3(K,t)
=\frac{t^2}{2}e^{-\nu|K|^2t}
\left\{
\mathcal C(P+Q,\mathcal C(P,a;Q,b);R,c)
 +\mathcal C(P+R,\mathcal C(P,a;R,c);Q,b)
 +\mathcal C(Q+R,\mathcal C(Q,b;R,c);P,a)
\right\}.                                                \tag{9}
\]

There are no other degree-three paths to this wavevector. Independence
of the three axes forces one positive copy of each input wavevector;
negative inputs cannot reach \(K\) in three leaves. The three terms in
(9) each contain both ordered outer products. Orthogonality of the axes
makes the heat weight the same in every path even when the three
frequencies differ. Their time integral is exactly \(t^2/2\).

For a transparent pressure audit, first set

\[
\alpha=\beta=\gamma=N.
\]

Before multiplication by \(t^2e^{-3\nu N^2t}/2\), the projected path
coefficients are as follows:

| Intermediate pair | Contribution at \(N(1,1,1)\) |
|---|---|
| \(P+Q\), then \(R\) | \(ACDN^2(-1,-1,2)/24\) |
| \(P+R\), then \(Q\) | \(ADN^2(-B+2C,-B-C,2B-C)/24\) |
| \(Q+R\), then \(P\) | \(ACDN^2(-1,2,-1)/24\) |

Their sum is

\[
\boxed{
\widehat U_3(N(1,1,1),t)
=\frac{ABDN^2t^2}{48}e^{-3\nu N^2t}(-1,-1,2).
}                                                         \tag{10}
\]

In particular **all \(ACD\) contributions cancel at this frequency**.
Retaining the \(P+R\to Q\) pathway alone would incorrectly predict
an \(ACD\) output. For \(B=0\), this cubic coefficient vanishes despite
the datum being genuinely three-dimensional and the quadratic normal
source being nonzero. For \(B\ne0\), a signed normal component survives.

Pressure causes part of this cancellation. At degree two,

\[
\widehat p_2(Q+R,t)=-\frac{BD}{4}e^{-2\nu N^2t};
\]

the \(BD\) part of the raw pair interaction is entirely a gradient.
At degree three, the raw velocity source at \(K\), with its common
factor \(t e^{-3\nu N^2t}\) removed, is

\[
-\frac{ADN^2}{8}(B+2C,B+2C,2C).
\]

The corresponding pressure is

\[
\widehat p_3(K,t)
=\frac{iADN(B+3C)}{12}t e^{-3\nu N^2t}.                   \tag{11}
\]

Thus \(-iK\widehat p_3\) adds

\[
\frac{ADN^2(B+3C)}{12}(1,1,1)t e^{-3\nu N^2t},
\]

leaving the projected sum in the table. Neither pressure nor any
intermediate pair is omitted.

## 4. The unequal frequencies relevant to the outgoing packets

Take \(\gamma=\alpha\), while allowing \(\beta\) to differ. Put

\[
X=\alpha^2,\qquad Y=\beta^2,\qquad
E(t)=e^{-\nu(2\alpha^2+\beta^2)t}.
\]

Direct evaluation of all of (9) gives

\[
\widehat U_3(K,t)=\frac{ADt^2E(t)}8
\begin{pmatrix}
\displaystyle
\alpha\beta\frac{(B+C)X^2-BXY-(B+C)Y^2}{(X+Y)(2X+Y)}\\[6pt]
\displaystyle
\alpha^2\frac{(B+2C)Y^2-2(B+C)X^2}{(X+Y)(2X+Y)}\\[6pt]
\displaystyle
\alpha\beta\frac{(B+C)X-CY}{2X+Y}
\end{pmatrix}.                                           \tag{12}
\]

It obeys \(K\cdot\widehat U_3(K,t)=0\) identically and reduces to
(10) when \(X=Y\). For \(A,B,C,D>0\), its normal component changes sign
at

\[
\left(\frac\beta\alpha\right)^4
=\frac{2(B+C)}{B+2C}.                                     \tag{13}
\]

One cannot transfer the equal-frequency sign to a highly anisotropic
stage. When \(\alpha/\beta\to0\), the leading sizes are

\[
\begin{aligned}
\widehat U_{3,x}&\sim-\frac{AD\alpha\beta t^2E}8(B+C),\\
\widehat U_{3,y}&\sim \frac{AD\alpha^2t^2E}8(B+2C),\\
\widehat U_{3,z}&\sim-\frac{ACD\alpha\beta t^2E}8.
\end{aligned}                                            \tag{14}
\]

For positive \(B,C\), with constants uniform in their ratio, the normal
component is smaller than the full vector by \(O(\alpha/\beta)\).
This is a polarization cost, separate from its amplitude, heat, and
time costs. If \(\alpha\asymp h^{-1}\) and

\[
\beta\asymp h^{-3/2},
\]

the cost is \(O(h^{1/2})\). The quadratic normal mode \(P+R\) in (8)
has no such cost, but is at the coarser frequency \(O(\alpha)\).
It is not a short wave relative to the outgoing \(Q\)-carrier.

## 5. Local actual-NS realization and a signed margin

This section reuses the already proved all-mode local expansion; it
does not repeat its sparse prototype or propose a new regularity route.
Let

\[
M=\max(\alpha,\beta,\gamma),\qquad
W=|A|+\sqrt{B^2+C^2}+|D|,\qquad x=MWt.
\]

The initial Wiener norm \(\sum_k|\widehat u_0(k)|\) is exactly \(W\).
For \(3x<1\), the actual smooth solution is the sum of the homogeneous
terms, with the previously proved estimate

\[
\|U_j(t)\|_{A^0}\le Wc_jx^{j-1},\qquad
c_j=\frac{j^{j-1}}{j!},\qquad \frac{c_{j+1}}{c_j}<3.        \tag{15}
\]

The estimate includes the full Leray projection, every Fourier mode
and viscous dissipation. It is uniform in positive \(\nu\).
Independence of the three generators gives an extra parity fact at the
selected coefficients. To reach \(P+R\) requires even degree; after its
quadratic term the next possible degree is four. To reach \(P+Q+R\)
requires odd degree; after its cubic term the next possible degree is
five. Therefore

\[
\begin{aligned}
\big|\widehat u(P+R,t)-\widehat U_2(P+R,t)\big|
&\le \frac{(8/3)W x^3}{1-9x^2},\\
\big|\widehat u(K,t)-\widehat U_3(K,t)\big|
&\le \frac{(125/24)W x^4}{1-9x^2}.                         \tag{16}
\end{aligned}
\]

Indeed \(c_4=8/3,c_5=125/24\), and successive allowed degrees increase
by two, with coefficient ratio less than nine. These are errors for
the **actual full solution**, not errors inside a three-mode model.

For example, suppose \(A,B,D>0\) and the frequencies equal \(N\).
Whenever \(3NWt<1\) and

\[
\frac{(125/24)W(NWt)^4}{1-9(NWt)^2}
\le \frac{ABDN^2t^2}{96}e^{-3\nu N^2t},                  \tag{17}
\]

the selected actual coefficient has the signed bound

\[
-\operatorname{Re}\widehat u_y(N(1,1,1),t)
\ge\frac{ABDN^2t^2}{96}e^{-3\nu N^2t}>0.                \tag{18}
\]

For every fixed nonzero positive \(A,B,D,N,\nu\), (17) holds on a
nonempty sufficiently short interval: its left side is \(O(t^4)\)
and its right side is a positive multiple of \(t^2\). Thus a
quantitative local actual-NS realization exists. There is no assertion
of a useful cascade-scale time margin. For strongly unequal amplitudes
or frequencies, the explicit inequality must be evaluated anew; it is
not replaced by an amplitude-independent success claim.

The analogous bound for (8) follows from the first line of (16) when
that error is at most half \( |AD\gamma|t
e^{-\nu(\alpha^2+\gamma^2)t}/4\). The same argument applies to a
nonzero component of (12). Higher spatial derivative convergence is
already part of the source theorem. No pressure estimate has been
deduced from a pressure-free truncation.

## 6. A frequency-and-polarization obstruction to a cheap third direction

There is a simple geometric restriction beyond the individual cubic
calculation. Assume \(\gamma=\alpha\le\beta\). Every frequency in
the degree-\(j\) term can be written

\[
K=aP+bQ+cR,\qquad a,b,c\in\mathbb Z,
\qquad |a|+|b|+|c|\le j.
\]

With \(K_\perp=K-(K\cdot r)r\), this gives

\[
|K_\perp|\le j\alpha.                                   \tag{19}
\]

For any solenoidal coefficient \(v\) at a nonzero \(K\),

\[
|r\cdot v|\le \frac{|K_\perp|}{|K|}|v|.                  \tag{20}
\]

This follows by projecting \(r\) onto the plane \(K^\perp\).
The same inequality holds for complex coefficients by Cauchy–Schwarz
in that complexified plane. In particular, a degree-\(j\) contribution
at \(|K|\ge\beta/2\) with desired normal amplitude \(a_*>0\)
requires total amplitude at least

\[
|v|\ge\frac{\beta}{2j\alpha}a_* .                          \tag{20a}
\]

This is a relative component cost, not an absolute upper bound when
the total amplitude is uncontrolled. A large tangential amplitude can
pay it. The same ratio holds for the Fourier gradient amplitudes after
multiplication by \(|K|\). Thus a mode with \(|K|\ge\beta/2\)
and a normal component at least \(\theta |v|\), for fixed

\[
0<\theta\le1,
\]

must have \(|K_\perp|\ge\theta\beta/2\). Such a frequency cannot
occur in any homogeneous degree smaller than

\[
j_0=\left\lceil\frac{\theta\beta}{2\alpha}\right\rceil.
                                                                    \tag{21}
\]

Cancellation among low-degree vectors cannot evade this frequency
restriction: all vectors at any one near-\(r\) frequency obey (20).
Define the fixed Fourier region

\[
\mathcal E_\theta
=\{K:|K|\ge\beta/2,\ |K_\perp|\ge\theta |K|\}.
\]

For \(j_0\ge1\) and \(3MWt\le1/2\), (15) gives the full-solution bound

\[
\sum_{K\in\mathcal E_\theta}|\widehat u(K,t)|
\le\frac{W(3MWt)^{j_0-1}}{1-3MWt}
\le 2W\,2^{-(j_0-1)}.                                   \tag{22}
\]

Here \(c_j\le3^{j-1}\) follows directly from (15). If the ratio

\[
\beta/\alpha\asymp h^{-1/2},
\]

then \(j_0\gtrsim h^{-1/2}\) for each fixed \(\theta>0\).
A finite number of slow transverse interactions therefore cannot
produce a substantial high-frequency coefficient with an order-one
normal polarization. On the specific local interval in (22), the
aggregate amplitude in the required angular region is exponentially
small in that ratio.

This is **not** a global-in-time spectral obstruction. A long nonlinear
evolution may accumulate many interactions. A supplied independent
donor with transverse frequency comparable to \(\beta\) also removes
the large degree threshold, but its original derivative cost must then
be paid. Furthermore, the actual localized \(Q_h\) does not have the
finite Fourier support assumed here. Its smooth cutoff and background
tails require their own signed estimates; they cannot be declared zero
using (19).

## 7. Consequence for the current actual flow

The missing input is now precise: one needs a specified \(p\)-dependent
component of the **existing** velocity, an outgoing frequency region,
and a signed transported Duhamel lower bound that survives full pressure
and all competing paths. A generic assertion that the background is
three-dimensional supplies none of those quantities.

The endpoint \(C^1\) approximation and
[its proved later-time persistence](later-flow-attempt.md)
do not identify \(D\), its phase, or its spectrum. A small perturbation
of either sign can fit a given \(C^1\) error allowance, while (5) changes
sign with that perturbation. Therefore an almost-affine error upper
bound alone cannot be used as a signed lower bound for this source.
This is an insufficiency of those particular bounds, not a claim that
the already fixed \(Q_h\) may be changed freely.

The concrete alternatives are to derive a nonzero suitable coefficient
from the full prescribed background and corrections, or to propose a
new initial-data construction with the third donor explicitly included
and redo the entire original-time seed, localization, and continuation
budgets. The latter is a different construction. No new donor has been
inserted into \(Q_h\) by this note.

The new calculation therefore establishes a source mechanism and a
specific low-order obstruction. It does not establish the long host,
frequency rotation, net gain, inherited donor, or infinite common-data
trajectory needed by the research goal.

## 8. Verification scope

Exact SymPy matrix calculations evaluated all three terms of (9),
including both ordered products and the full Leray projector. They
checked the table, (10)–(14), \(K\cdot\widehat U_3=0\), and the
raw/pressure cancellation in (11). Separate exact Fourier convolution
over all signed original modes checked that the selected positive
triple has exactly the same coefficient, rather than relying on a
single interaction tree. The local remainder uses the existing proved
all-mode majorant, with the parity argument and constants in (16)
shown above. These are algebraic and written analytic checks; they
are not a formal PDE certificate or external expert acceptance.
