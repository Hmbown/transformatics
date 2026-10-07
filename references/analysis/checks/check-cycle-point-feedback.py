"""Exact pressure feedback on the existing periodic cycle; no flow simulation."""
import sympy as S

x, y, z, mu = S.symbols("x y z mu", real=True)
X = S.Matrix([x, y, z])
zero = {x: 0, y: 0, z: 0}
C = S.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
s, r, beta, ls, lr = S.symbols("s r beta ls lr", real=True)
B = s * C + r * C ** 2
H = -2 * s * r * S.eye(3) + beta * (C + C ** 2)
rhs = -B ** 2 - H + mu * (ls * C + lr * C ** 2)
assert S.simplify(rhs - (-r ** 2 - beta + mu * ls) * C
                  - (-s ** 2 - beta + mu * lr) * C ** 2) == S.zeros(3)
cc, dd = S.symbols("cc dd", real=True)
assert S.simplify((s ** 2 + r ** 2).subs(
    {s: (cc + dd) / 2, r: (cc - dd) / 2}) - (cc ** 2 + dd ** 2) / 2) == 0
print("PASS: exact symmetry-reduced central gradient equations")

# Previously proved time jets are inputs to the new pressure calculation.
U = S.Matrix([S.sin(y), S.sin(z), S.sin(x)])
N = U.jacobian(X) * U
T = -S.Matrix([S.sin(y) * S.sin(z) ** 2,
                S.sin(z) * S.sin(x) ** 2,
                S.sin(x) * S.sin(y) ** 2])
U1 = -N - mu * U
U2 = T + 4 * mu * N + mu ** 2 * U
B0, B1, B2 = [v.jacobian(X) for v in [U, U1, U2]]
F = (S.sin(x) * S.sin(y) * S.cos(y) * S.cos(z)
     + S.sin(x) * S.sin(z) * S.cos(x) * S.cos(y)
     + S.sin(y) * S.sin(z) * S.cos(x) * S.cos(z))
p2 = 12 * mu * S.cos(x) * S.cos(y) * S.cos(z) - S.Rational(4, 3) * F
g2 = 2 * S.trace(B1 * B1 + B0 * B2)
assert S.simplify(S.expand(sum(S.diff(p2, q, 2) for q in X) + g2)) == 0
assert S.diff(p2, x, y).subs(zero) == -S.Rational(4, 3)
assert S.hessian(p2, X).subs(zero) == (
    -12 * mu * S.eye(3) - S.Rational(4, 3) * (C + C ** 2))


def adv(v, w):
    return w.jacobian(X) * v


def lap(v):
    return S.Matrix([sum(S.diff(vv, q, 2) for q in X) for vv in v])


assert lap(U2).jacobian(X).subs(zero) == (
    (-2 - mu ** 2) * C - 8 * mu * C ** 2)
U3 = (-adv(U2, U) - 2 * adv(U1, U1) - adv(U, U2)
      - S.Matrix([S.diff(p2, q) for q in X]) + mu * lap(U2))
B3 = S.simplify(U3.jacobian(X).subs(zero))
s3 = -S.Rational(2, 3) - 2 * mu - mu ** 3
r3 = S.Rational(4, 3) - 12 * mu ** 2
assert S.simplify(B3 - s3 * C - r3 * C ** 2) == S.zeros(3)
assert S.expand(s3 + r3) == S.Rational(2, 3) - 2 * mu - 12 * mu ** 2 - mu ** 3
assert S.expand(s3 - r3) == -2 - 2 * mu + 12 * mu ** 2 - mu ** 3
omitted_offdiag = B3 - S.Rational(4, 3) * (C + C ** 2)
assert S.simplify(omitted_offdiag - B3) != S.zeros(3)
print("PASS: full second pressure jet, Laplacian jets, third gradient and pressure-omission control")
print("Finite algebra only; no closed scalar amplifier or Navier–Stokes solution claim.")
