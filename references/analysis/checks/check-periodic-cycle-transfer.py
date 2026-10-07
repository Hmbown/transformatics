"""Exact periodic NS time jets; no numerical time integration or PDE certificate."""
import sympy as s

x, y, z = s.symbols("x y z", real=True)
mu = s.symbols("mu", nonnegative=True)
X = s.Matrix([x, y, z])
U = s.Matrix([s.sin(y), s.sin(z), s.sin(x)])


def div(v):
    return s.simplify(sum(s.diff(v[i], X[i]) for i in range(3)))


def lap(v):
    return s.Matrix([sum(s.diff(vv, q, 2) for q in X) for vv in v])


def adv(v, w):
    return w.jacobian(X) * v


def average(f):
    f = s.expand(f)
    for q in X:
        f = s.integrate(f, (q, 0, 2 * s.pi)) / (2 * s.pi)
    return s.simplify(f)


def grad_pair(v, w):
    return sum(s.diff(v[i], q) * s.diff(w[i], q)
               for i in range(3) for q in X)


N = adv(U, U)
N_expected = s.Matrix([s.sin(z) * s.cos(y), s.sin(x) * s.cos(z),
                       s.sin(y) * s.cos(x)])
assert s.simplify(N - N_expected) == s.zeros(3, 1)
assert div(U) == div(N) == 0
U1 = -N - mu * U
p1 = -2 * s.cos(x) * s.cos(y) * s.cos(z)
T = -s.Matrix([s.sin(y) * s.sin(z) ** 2,
               s.sin(z) * s.sin(x) ** 2,
               s.sin(x) * s.sin(y) ** 2])
U2 = T + 4 * mu * N + mu ** 2 * U
full_second = -adv(U1, U) - adv(U, U1) - s.Matrix(
    [s.diff(p1, q) for q in X]) + mu * lap(U1)
assert s.simplify(s.expand(full_second - U2)) == s.zeros(3, 1)
assert div(U1) == div(U2) == 0

at0 = {x: 0, y: 0, z: 0}
C = U.jacobian(X).subs(at0)
assert C ** 3 == s.eye(3)
assert U1.jacobian(X).subs(at0) == -C ** 2 - mu * C
assert U2.jacobian(X).subs(at0) == 4 * mu * C ** 2 + mu ** 2 * C
assert s.hessian(p1, X).subs(at0) == 2 * s.eye(3)
omitted_pressure = U2 + s.Matrix([s.diff(p1, q) for q in X])
assert div(omitted_pressure).subs(at0) == 6
print("PASS: full pressure-corrected jets, stagnation gradient, omitted-pressure control")

Q0 = average(grad_pair(U, U)) / 2
Q1 = average(grad_pair(U, U1))
Q2 = average(grad_pair(U1, U1) + grad_pair(U, U2))
E1 = average(U.dot(U1))
assert Q0 == s.Rational(3, 4)
assert s.simplify(Q1 / Q0 + 2 * mu) == 0
assert s.simplify(Q2 / Q0 - 1 - 4 * mu ** 2) == 0
assert E1 == -s.Rational(3, 2) * mu
assert average(N.dot(N)) == s.Rational(3, 4)
assert average(grad_pair(N, N)) == s.Rational(3, 2)
assert average(U.dot(N)) == 0
assert s.simplify(lap(N) + 2 * N) == s.zeros(3, 1)

# The second inviscid jet has only squared-frequency 1 and 5.
fundamental = -U / 2
shell5 = T - fundamental
assert s.simplify(lap(shell5) + 5 * shell5) == s.zeros(3, 1)
assert average(shell5.dot(U)) == 0
assert average(shell5.dot(N)) == 0

theta = 8 * mu
quadratic_Q = 1 - 2 * mu * theta + (s.Rational(1, 2) + 2 * mu ** 2) * theta ** 2
assert s.expand(quadratic_Q - 1) == 16 * mu ** 2 + 128 * mu ** 4
fixed_clock_margin = s.Rational(1, 2) - s.Rational(1, 8) - s.Rational(1, 4)
assert fixed_clock_margin == s.Rational(1, 8)
print("PASS: exact energy/enstrophy jets, generated reverse shell, viscous regrowth margin")
print("PASS: fixed-clock gain margin under mu<=tau0/16 and C_Q*tau0<=1/4")
print("Analytic short-time remainder is a separate written Sobolev argument; no DNS.")
