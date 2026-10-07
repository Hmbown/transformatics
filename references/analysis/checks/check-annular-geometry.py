"""Exact algebra for annular geometry, viscous returns and later-flow powers.

These controls are not a PDE certificate or a flow simulation.
"""

import sympy as s

r, z = s.symbols('r z', positive=True)
xi = s.Function('xi')(r, z)
theta = s.Function('theta')(r, z)

# The weight is r dr dz. Retain the 3/r diffusion coefficient.
diffusion = r * xi * (s.diff(xi, r, 2) + 3 / r * s.diff(xi, r) + s.diff(xi, z, 2))
dissipation = r * (s.diff(xi, r) ** 2 + s.diff(xi, z) ** 2)
flux = s.diff(r * xi * s.diff(xi, r) + xi ** 2, r) + s.diff(r * xi * s.diff(xi, z), z)
assert s.simplify(diffusion + dissipation - flux) == 0

# The angular derivative of omega_theta e_theta contributes xi^2.
cartesian_gradient = r * (s.diff(r * xi, r) ** 2 + s.diff(r * xi, z) ** 2 + xi ** 2)
weighted_gradient = r ** 3 * (s.diff(xi, r) ** 2 + s.diff(xi, z) ** 2)
assert s.simplify(cartesian_gradient - weighted_gradient - s.diff(r ** 2 * xi ** 2, r)) == 0
# Omitting this basis derivative must fail the identity.
assert s.simplify(cartesian_gradient - r * xi ** 2 - weighted_gradient - s.diff(r ** 2 * xi ** 2, r)) != 0

# Multiplying the swirl variable by r^2 conjugates the complete operators.
def l_gamma(f):
    return s.diff(f, r, 2) - s.diff(f, r) / r + s.diff(f, z, 2)

def l_xi(f):
    return s.diff(f, r, 2) + 3 * s.diff(f, r) / r + s.diff(f, z, 2)

assert s.simplify(l_gamma(r ** 2 * theta) - r ** 2 * l_xi(theta)) == 0
assert s.simplify(l_gamma(r ** 2 * theta) - r ** 2 * l_gamma(theta)) != 0

print('PASS: weighted diffusion pairing, full Cartesian vorticity gradient, omitted-basis negative control, and full-operator conjugation with negative control.')

# The same scalar diffusion still creates spatial matrix commutators.
t, nu = s.symbols('t nu', positive=True)
phi = s.Function('phi')(t)
J = s.Matrix([[0, 0], [1, 0]])
M = s.eye(2) + phi * s.cos(z) * J
H = s.Matrix([s.Function('h1')(t, z), s.Function('h2')(t, z)])
B = s.diff(phi, t) * s.cos(z) * J
assert J ** 2 == s.zeros(2)
assert s.simplify(s.diff(M, t) - B * M) == s.zeros(2)
product_residual = s.diff(M * H, t) - nu * s.diff(M * H, z, 2) - B * M * H
heat_residual = M * (s.diff(H, t) - nu * s.diff(H, z, 2))
commutator = -nu * (s.diff(M, z, 2) * H + 2 * s.diff(M, z) * s.diff(H, z))
assert s.simplify(product_residual - heat_residual - commutator) == s.zeros(2, 1)
assert s.simplify(commutator) != s.zeros(2, 1)

# Integration by parts at a zero-endpoint phi fixes both sideband signs.
N, flight = s.symbols('N flight', positive=True)
for shift in (-1, 1):
    exponent = -nu * ((N + shift) ** 2 * (flight - t) + N ** 2 * t)
    factor = s.exp(exponent)
    assert s.simplify(s.diff(factor, t) / factor - nu * (2 * shift * N + 1)) == 0
print('PASS: spatial return commutator and both exact sideband integration-by-parts factors.')

# Track the displayed powers independently with exact rational arithmetic.
from fractions import Fraction as Q
P, pressure_log, initial_H = Q(11, 8), Q(2), Q(117, 8)
assert P + pressure_log == Q(27, 8)
assert 2 * P + pressure_log - 5 == -Q(1, 4)
assert Q(17, 2) * Q(9, 4) - initial_H == Q(9, 2)
assert Q(9, 2) + Q(1, 2) == 5
assert Q(19, 2) * Q(9, 4) - initial_H == Q(27, 4)
assert -Q(14) + Q(10) == -4
assert -4 + 2 * Q(3, 2) == -1
print('PASS: seven exact later-lifetime, persistence, source and local-Reynolds exponent controls.')
