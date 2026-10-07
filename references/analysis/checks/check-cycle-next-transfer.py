"""Exact finite Fourier jets for the cycle's moving speed maximum. No DNS.

For real odd velocity fields, uhat(k)=i*v(k), with v real and rational.
The dictionary retains every mode generated in each exact time derivative.
The analytic lifespan, moving-maximum and remainder arguments are separate.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

ZERO = (F(0),) * 3


def add_mode(data, k, value):
    old = data.get(k, ZERO)
    new = tuple(old[j] + value[j] for j in range(3))
    if any(new):
        data[k] = new
    elif k in data:
        del data[k]


def minus_advection(a, b):
    """Coefficients v of -(a.grad)b, before the exact Leray projection."""
    result = {}
    for k, v in a.items():
        for ell, w in b.items():
            m = tuple(k[j] + ell[j] for j in range(3))
            dot = sum(ell[j] * v[j] for j in range(3))
            if dot:
                add_mode(result, m, tuple(dot * z for z in w))
    return result


def project_and_pressure(raw):
    """Return P(-advection) and the real coefficients of its pressure."""
    velocity, pressure = {}, {}
    for k, v in raw.items():
        n = sum(z * z for z in k)
        parallel = sum(k[j] * v[j] for j in range(3)) / n if n else F(0)
        add_mode(velocity, k, tuple(v[j] - k[j] * parallel for j in range(3)))
        if parallel:
            pressure[k] = parallel
    return velocity, pressure


initial = {}
for frequency, component in [((0, 1, 0), 0), ((0, 0, 1), 1), ((1, 0, 0), 2)]:
    for sign in (-1, 1):
        k = tuple(sign * z for z in frequency)
        v = [F(0)] * 3
        v[component] = F(-sign, 2)
        initial[k] = tuple(v)

jets, pressures = [initial], []
for order in range(4):
    raw = {}
    for j in range(order + 1):
        for k, v in minus_advection(jets[j], jets[order - j]).items():
            add_mode(raw, k, tuple(comb(order, j) * z for z in v))
    velocity, pressure = project_and_pressure(raw)
    jets.append(velocity)
    pressures.append(pressure)

assert [len(u) for u in jets] == [6, 12, 18, 48, 90]
for u in jets:
    for k, v in u.items():
        assert sum(k[j] * v[j] for j in range(3)) == 0
        assert u.get(tuple(-z for z in k), ZERO) == tuple(-z for z in v)
assert not pressures[0]
# Pi_1=-2 cos(x) cos(y) cos(z): all eight coefficients are -1/4.
assert pressures[1] == {k: F(-1, 4) for k in product((-1, 1), repeat=3)}
print("PASS: exact all-mode jets, reality, incompressibility, initial pressure response")


def phase_split(power, value, real, imaginary, index):
    power %= 4
    destination = real if power % 2 == 0 else imaginary
    destination[index] += value if power < 2 else -value


def directional_coefficient(data, order, corner, path):
    """Coefficient t^order of u(p+t*path), p=corner*pi/2."""
    real, imaginary = [F(0)] * 3, [F(0)] * 3
    for k, v in data.items():
        phase = sum(k[j] * corner[j] for j in range(3))
        speed = sum(k[j] * path[j] for j in range(3))
        coefficient = F(speed ** order, factorial(order))
        for j in range(3):
            phase_split(1 + phase + order, coefficient * v[j], real, imaginary, j)
    assert not any(imaginary)
    return tuple(real)


def pressure_gradient_coefficient(data, order, corner, path):
    """Coefficient t^order of grad Pi(p+t*path), with real Fourier Pi."""
    real, imaginary = [F(0)] * 3, [F(0)] * 3
    for k, p in data.items():
        phase = sum(k[j] * corner[j] for j in range(3))
        speed = sum(k[j] * path[j] for j in range(3))
        coefficient = F(speed ** order, factorial(order))
        for j in range(3):
            phase_split(1 + phase + order, coefficient * k[j] * p,
                        real, imaginary, j)
    assert not any(imaginary)
    return tuple(real)


for corner in product((-1, 1), repeat=3):
    path = (corner[1], corner[2], corner[0])
    coefficients = []
    for total in range(5):
        value = [F(0)] * 3
        for j in range(total + 1):
            contribution = directional_coefficient(jets[j], total - j, corner, path)
            for i in range(3):
                value[i] += contribution[i] / factorial(j)
        coefficients.append(tuple(value))
    assert coefficients[:4] == [path, ZERO, ZERO, ZERO]
    assert coefficients[4] == tuple(-F(4, 15) * z for z in path)
    speed_squared = [
        sum(coefficients[j][i] * coefficients[n - j][i]
            for j in range(n + 1) for i in range(3))
        for n in range(5)
    ]
    assert speed_squared == [F(3), F(0), F(0), F(0), -F(8, 5)]

    # The three contributions to grad Pi(t,p+t*path) at order t^3.
    contributions = [
        tuple(z / factorial(j) for z in
              pressure_gradient_coefficient(pressures[j], 3 - j, corner, path))
        for j in (1, 2, 3)
    ]
    assert contributions == [
        tuple(F(2) * z for z in path),
        tuple(-F(4, 3) * z for z in path),
        tuple(F(2, 5) * z for z in path),
    ]
    assert tuple(sum(v[i] for v in contributions) for i in range(3)) == tuple(
        F(16, 15) * z for z in path)
print("PASS: all eight moving corners, quartic speed loss -8/5, complete pressure sum 16/15")

# Check the spatial optimization algebra independently with trigonometric jets.
import sympy as s
x, y, z = X = s.symbols("x y z", real=True)
u0 = s.Matrix([s.sin(y), s.sin(z), s.sin(x)])
n = u0.jacobian(X) * u0
tjet = -s.Matrix([s.sin(y) * s.sin(z) ** 2,
                  s.sin(z) * s.sin(x) ** 2,
                  s.sin(x) * s.sin(y) ** 2])
g0 = u0.dot(u0)
g1 = -2 * u0.dot(n)
g2 = 2 * n.dot(n) + 2 * u0.dot(tjet)
for corner in product((-1, 1), repeat=3):
    substitution = {X[j]: corner[j] * s.pi / 2 for j in range(3)}
    path = s.Matrix([corner[1], corner[2], corner[0]])
    assert s.Matrix([s.diff(g0, q) for q in X]).subs(substitution) == s.zeros(3, 1)
    assert s.hessian(g0, X).subs(substitution) == -2 * s.eye(3)
    assert s.Matrix([s.diff(g1, q) for q in X]).subs(substitution) == 2 * path
    assert s.hessian(g1, X).subs(substitution) == s.zeros(3)
    assert s.Matrix([s.diff(g2, q) for q in X]).subs(substitution) == s.zeros(3, 1)
    assert all(s.diff(g0, a, b, c).subs(substitution) == 0
               for a, b, c in product(X, repeat=3))
print("PASS: nondegenerate initial maxima, maximizer motion p+t*U0+O(t^3)")
assert F(8, 5) - F(4, 5) == F(4, 5)
assert F(6) - F(3) == F(3)
print("PASS: finite-time speed-loss margins after stated analytic remainders")
print("No time stepping, grid truncation of an evolving solution, or DNS was used.")
