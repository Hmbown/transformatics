# Independent review of the cyclic datum's point feedback

8 September 2026. **PASS at the stated finite written scope.** This review
independently derives the pressure sign and additional time jets in
[the point-feedback source](cycle-point-feedback.md).
It pins source SHA-256
`a822b08c86d07a901ff8f39f4661309ca75f230f6b1f8d4cf82e18c95d5d9cd1`.
The calculation below was made from its displayed fields, without reading
or rerunning its supporting symbolic controls. This is separate AI-agent
review, not external expert acceptance or formal PDE certification.
There is no new datum, DNS, closed pointwise evolution, or global
regularity or breakdown claim.

## Exact symmetry and pressure sign

For C=E12+E23+E31, the given datum satisfies U0(Cx)=C U0(x).
Together with central oddness and uniqueness this fixes the center and
makes its velocity gradient commute with C. Its trace-free real commutant
is exactly the span of C and C squared. The symmetric Hessian commutant
is the span of I and C+C squared. These facts justify the displayed forms
without making a local closure assumption.

Writing B=sC+rC squared gives

    B squared=2sr I+r squared C+s squared C squared.

The Poisson equation is Delta Pi=-g, with g=tr[(grad U) squared].
Thus the nonzero Fourier coefficients satisfy Pi_hat=g_hat/|k| squared.
Two derivatives contribute -k1 k2, so the minus sign in the source's
formula (6) is correct. The zero Fourier coefficient of g vanishes by
periodic integration by parts and incompressibility. Smoothness gives
the stated summability; no pointwise ordinary-kernel interpretation is
needed. At the center, the pressure trace is -6sr, hence alpha=-2sr.
Subtracting B squared and this full Hessian recovers both equations (5),
including the off-diagonal pressure and positive-viscosity spatial jets.

## Independent second pressure jet

Use N=(sin z cos y,sin x cos z,sin y cos x) for the first nonlinear
field of the earlier transfer note; here N is a vector field, not a new
source. Set D0=grad U0, DN=grad N and DT=grad T. The already established
velocity jets give

    grad U_tau(0)=-DN-mu D0,
    grad U_tautau(0)=DT+4mu DN+mu squared D0.

Let F be the three-term scalar function in section 4 of the source.
Direct matrix contraction yields

    tr(D0 squared)=0,
    tr(D0 DN)=3cos x cos y cos z,
    tr(DN squared)=-2F,
    tr(D0 DT)=-2F.

For example tr(DN squared) is twice the sum of the three products of
opposite off-diagonal entries. Each is the negative of one summand of F.
Consequently differentiating tr[(grad U) squared] twice gives

    g_tautau(0)=2tr(DN squared+D0 DT)+12mu tr(D0 DN)
              =-8F+36mu cos x cos y cos z.

Each term of F is a product with frequencies 1,2,1 in some order;
therefore -Delta F=6F. Also -Delta(cos x cos y cos z)=3cos x cos y cos z.
Applying the exact periodic inverse Laplacian gives precisely

    Pi_tautau(0)=-(4/3)F+12mu cos x cos y cos z.

At the origin F=xy+xz+yz plus terms of total degree at least four.
Its off-diagonal Hessian entries are one and its diagonal entries zero.
The Hessian of the cosine product is -I. Hence

    beta''(0)=-4/3, alpha''(0)=-12mu.

This checks the nonlocal inversion, not merely the pressure trace.
The trace alone could not have determined beta''.

## Laplacian and third-gradient coefficients

Directly apply Delta partial_y to the first component
T1=-sin y sin squared z: its value at zero is -2.
The same operator on 4mu N1 is zero and on mu squared (U0)1 is
-mu squared. Applying Delta partial_z instead gives zero from T1,
-8mu from 4mu N1, and zero from the original wave. Thus

    l_s''(0)=-2-mu squared, l_r''(0)=-8mu.

Differentiate the exact point equations twice. With c(0)=d(0)=1,
the independent formulas are

    c'''(0)=-[c'(0) squared+c''(0)+d'(0) squared+d''(0)]
             -2beta''(0)+mu[l_s''(0)+l_r''(0)],
    d'''(0)=c''(0)+2c'(0)d'(0)+d''(0)
             +mu[l_s''(0)-l_r''(0)].

Substituting the previously reviewed first and second jets gives

    c'''(0)=2/3-2mu-12mu squared-mu cubed,
    d'''(0)=-2-2mu+12mu squared-mu cubed.

Both match (11). The pressure contribution to c''' is +8/3;
setting beta'' to zero while retaining the other actual jets therefore
lowers c''' by 8/3, as stated. The pressure-free calculation is a
negative control, not an alternative actual solution.

## Remainder and conclusion

The earlier uniform H12 bound and three time derivatives through H6
give g''' in H5 by the product rule. The pressure Hessian multiplier
has order zero on the mean-zero torus, so its value at the center and
the cubic Taylor remainder for beta are uniformly controlled. This
justifies beta(tau)=-(2/3)tau squared+O(tau cubed) on the stated common
short interval, uniformly for mu in [0,1]. Positive physical viscosity
is retained in the actual statement.

The exact reduction remains driven by the full nonlocal beta and two
third-spatial-derivative jets. The source correctly avoids inferring
their later signs from these early derivatives, or a global continuation
bound from a single center. No source correction is requested.
