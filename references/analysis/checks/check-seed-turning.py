"""Exact controls for the thin limiting central Kelvin model.

These check matrix identities and the limiting turning equation, not
matched asymptotics, an actual-profile NS transfer, or global regularity.
Run with the repository Python environment. No numerical fluid evolution.
"""
import sympy as s


def main():
    c = s.sqrt(2) / 2
    mu = s.Rational(2, 3)
    A = s.Matrix([[0, -1, 0], [-1, 0, 0], [-c, 0, 0]])
    O = s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    D = A - O
    N = s.Matrix([0, -c, 2])
    beta = s.Matrix([1, s.Rational(1, 3), c / 6])
    alpha = N.cross(beta)
    omega = s.Matrix([0, c, 0])
    Gamma = omega.dot(N)
    zero = lambda x: all(s.simplify(v) == 0 for v in x)
    assert D * D == s.zeros(3)
    assert zero(D.T * N)
    assert Gamma == -s.Rational(1, 2)
    assert zero(mu * alpha - D * alpha - Gamma * beta)

    # Exact backward receiver covector in the rotating frame. The symbol
    # st stands for sT exp(-mu u); differentiate it by the chain rule.
    u, st, sT = s.symbols('u st sT', real=True)
    receiver = alpha / s.sqrt(alpha.dot(alpha))
    eta = receiver - 2 * u * s.Matrix([1, 0, 0])
    eta += s.Rational(9, 2) * (sT - st * (1 + mu * u)) * N
    eta_u = eta.diff(u) - mu * st * eta.diff(st)
    assert zero(eta_u - ((A - st * beta * N.T).T + O) * eta)

    # Independent direct limit of the pressure-corrected polarization.
    Q = s.Matrix.hstack(beta / s.sqrt(beta.dot(beta)), receiver,
                        N / s.sqrt(N.dot(N)))
    AQ, OQ = s.simplify(Q.T * A * Q), s.simplify(Q.T * O * Q)
    assert zero(Q.T * Q - s.eye(3))
    z, e = s.symbols('z e', positive=True)
    V, W = s.symbols('V W')
    b = 2 * s.sqrt(2) / 3
    ray = s.Matrix([-2 * b * z * e, 1, b * z**2])
    amplitude = s.Matrix([V / e, 2 * b * z * V - b * z**2 * W, W])
    assert s.simplify(ray.dot(amplitude)) == 0
    Ab = AQ - s.Matrix([1, 0, 0]) * s.Matrix([[0, 0, 1]]) / e**2
    rhs = (-Ab - OQ + 2 * ray * ray.T * Ab / ray.dot(ray)) * amplitude
    v_z = s.simplify(s.limit(-e**2 * rhs[0], e, 0))
    w_z = s.simplify(s.limit(-e * rhs[2], e, 0))
    P = 1 + b**2 * z**4
    assert s.simplify(v_z + W) == 0
    assert s.simplify(w_z - ((2 * b**2 * z**2 - 2 * b / 3) * V
                            - 4 * b**2 * z**3 * W) / P) == 0

    # Positive Volterra transform for the limiting scalar ODE.
    g = P**(-s.Rational(1, 2))
    Lg = s.diff(P * s.diff(g, z), z) + (2 * b**2 * z**2 - 2 * b / 3) * g
    assert s.simplify(Lg + (4 * b**2 * z**2 + 2 * b * P / 3)
                      / P**s.Rational(3, 2)) == 0
    y = s.Function('y')(z)
    Ly = s.diff(P * s.diff(g * y, z), z) + (2 * b**2 * z**2 - 2 * b / 3) * g * y
    assert s.simplify(g * Ly - s.diff(y, z, 2) - g * Lg * y) == 0
    # Under v=b z^2, integral z q(z) dz becomes this elementary integral.
    v = s.symbols('v', positive=True)
    mass = s.integrate(2 * v / (1 + v**2)**2 + 1 / (3 * (1 + v**2)),
                       (v, 0, s.oo))
    assert s.simplify(mass - 1 - s.pi / 6) == 0
    print('12 exact limiting-model controls passed; actual-profile matching remains open.')


if __name__ == '__main__':
    main()
