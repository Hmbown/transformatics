"""Exact controls for the post-focus calculation; no fluid simulation.

Checks finite algebra and scale powers, including omissions that destroy the
outgoing connection. The analytic PDE estimates require their written proofs.
"""

import sympy as s


def zero(expr):
    assert s.simplify(expr) == 0, expr


def geometry_and_connection():
    t = s.symbols("t", nonnegative=True)
    c = s.sqrt(2) / 2
    mu = s.Rational(2, 3)
    N = s.Matrix([0, -c, 2])
    plus = s.Matrix([1, s.Rational(1, 3), c / 6])
    minus = s.Matrix([1, -s.Rational(1, 3), -c / 6])
    receiver = s.Matrix([-s.Rational(1, 3), s.Rational(8, 9), 4*c/9])
    A = s.Matrix([[0, -1, 0], [-1, 0, 0], [-c, 0, 0]])
    frame = s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    deformation = A - frame
    assert deformation**2 == s.zeros(3)
    pressure_generator = -A-frame + 2*N*(N.T*A)/(N.dot(N))
    assert s.simplify(pressure_generator*plus-mu*plus) == s.zeros(3, 1)
    assert s.simplify(pressure_generator*minus+mu*minus) == s.zeros(3, 1)
    future = (s.eye(3)-t*deformation).T*receiver
    zero(future.dot(plus)-2*t)
    zero(future.dot(minus)-(2*t-s.Rational(2, 3)))
    integral = s.Rational(7, 2)-(3*t+s.Rational(7, 2))*s.exp(-mu*t)
    zero(s.diff(integral, t)-future.dot(minus)*s.exp(-mu*t))
    zero(integral.subs(t, 0))
    assert s.limit(integral, t, s.oo) == s.Rational(7, 2)
    # Omitting the stable forcing removes this entire connection.
    assert s.integrate(0, (t, 0, s.oo)) != s.Rational(7, 2)
    # Omitting its constant term also changes the leading coefficient.
    assert s.integrate(2*t*s.exp(-mu*t), (t, 0, s.oo)) == s.Rational(9, 2)
    assert s.simplify((-A-frame)*plus-mu*plus) != s.zeros(3, 1)
    print("PASS: exact geometry, pressure, stable connection and omission controls")


def inner_conjugation():
    z = s.symbols("z", real=True)
    a, c = s.symbols("a c", negative=True)
    P = 1+a*a*z**4
    K21 = (2*a*a*z*z+2*c)/P
    K22 = -4*a*a*z**3/P
    weight = P**s.Rational(-1, 2)
    # V'' - K22 V' + K21 V = 0, with V = weight*Y.
    zero(2*s.diff(weight, z)/weight-K22)
    potential = (4*a*a*z*z-2*c*P)/P**2
    zero(s.diff(weight, z, 2)/weight-K22*s.diff(weight, z)/weight+K21+potential)
    zero(potential.subs(z, -z)-potential)
    assert potential.is_positive is True
    print("PASS: signed inner scalar conjugation and positive even potential")


def powers_and_margin():
    R = s.Rational
    gradient_high_weight = 12-1-R(3, 2)
    assert gradient_high_weight == R(19, 2)
    theta = (1+R(3, 2))/12
    assert theta == R(5, 24)
    margin = R(31, 8)*(1-theta)-R(117, 8)*theta
    assert margin == R(1, 48)
    assert margin-R(1, 192) == R(1, 64)
    assert margin-R(1, 192)-R(1, 384) > R(1, 96)
    assert gradient_high_weight*R(9, 4)-R(117, 8) == R(27, 4)
    assert R(15, 8)+R(1, 8) == 2
    assert 1+R(1, 8) == R(9, 8) < 2
    assert 2+2*R(1, 8) == R(9, 4)
    # Residual and the explicitly retained central diffusivity mismatch.
    k, d, epsilon = R(3, 2), R(5, 4), 4
    assert 3*k-d/2 == R(31, 8)
    assert epsilon-k+R(5, 2)*d-1 == R(37, 8)
    assert k+R(3, 2)*d-12*k == -R(117, 8)
    print("PASS: Fourier interpolation, adjustable clock margin and physical scale powers")


if __name__ == "__main__":
    geometry_and_connection()
    inner_conjugation()
    powers_and_margin()
    print("Finite algebra only; no nonlinear PDE certification or solution claim.")
