"""Independent exact differential controls; these do not certify a PDE proof."""

import json
from functools import lru_cache

import pytest
import sympy as sp

from experiments.nse_loglog_handover import (
    build_receipt, curl_lift_amplitude, forced_remainder,
    gradient_error_exponent, main, pressure_amplitude, quadratic_coefficients,
)

R = sp.Rational


def _curl(v, X):
    # Independently differentiate a vector potential in Cartesian coordinates.
    x, y, z = X
    return sp.Matrix([sp.diff(v[2], y)-sp.diff(v[1], z),
                      sp.diff(v[0], z)-sp.diff(v[2], x),
                      sp.diff(v[1], x)-sp.diff(v[0], y)])


def _zero(v):
    entries = list(v) if isinstance(v, sp.MatrixBase) else [v]
    return all(sp.factor(sp.cancel(sp.expand(a))) == 0 for a in entries)


def test_receipt_has_exact_controls_and_preserves_machine_scope():
    receipt = build_receipt()
    assert receipt["all_green"], {k: v for k, v in receipt["checks"].items() if not v}
    assert receipt["evidence_class"] == "EXACT_ALGEBRA_ONLY"
    assert receipt["research_note"] == "references/navier-stokes/loglog-handover.md"
    assert receipt["written_proof_status"] == "INDEPENDENTLY_REVIEWED_RESTRICTED_ANALYTIC_RESULT"
    assert receipt["root_status"] == receipt["E_prime_status"] == "OPEN"
    for name in ("PDE_theorem_certified", "mean_PDE_estimates_certified",
                 "all_mode_remainder_bound_certified", "strong_continuation_certified",
                 "actual_perturbed_particle_tracked", "dns_run", "lean_kernel_checked"):
        assert receipt[name] is False
    for name in ("quadratic", "forced_harmonic_1", "forced_harmonic_2",
                 "mean_feedback", "scaling", "outgoing_wave"):
        assert all(type(value) is bool for value in receipt[name]["checks"].values())


@lru_cache(maxsize=1)
def _independent_real_packet():
    x, y, z = X = sp.symbols("x y z", real=True)
    h = sp.symbols("h", positive=True)
    # Curvature and amplitude vary in all three directions. The potential
    # is polynomial but is unrelated to the instrument's test fixture.
    S = y+x*z
    xi = sp.Matrix([sp.diff(S, a) for a in X])
    b = xi.dot(xi)*xi.cross(sp.Matrix([1, x, -y]))
    potential = (xi.cross(b)/xi.dot(xi)).applyfunc(sp.cancel)
    d = _curl(potential, X)
    W = b*sp.cos(S/h)-h*d*sp.sin(S/h)
    raw = W.jacobian(X)*W
    coefficients = quadratic_coefficients(b, d, b.jacobian(X), d.jacobian(X), h)
    # Expand exact trigonometric products before cancelling the polynomial
    # coefficients. This is actual differentiation, not supplied first jets.
    expected = coefficients[0]+coefficients[1]*sp.cos(2*S/h)+coefficients[2]*sp.sin(2*S/h)
    defect = (raw-expected).applyfunc(lambda a: sp.expand_trig(a).expand())
    defect = defect.applyfunc(lambda a: sp.trigsimp(a, method="fu"))
    return X, h, S, xi, b, d, W, coefficients, defect


def test_curved_real_quadratic_formula_by_actual_differentiation():
    *_, defect = _independent_real_packet()
    assert _zero(defect)


def test_curved_curl_packet_is_exactly_solenoidal_and_needs_the_mean():
    X, _, _, xi, b, d, W, coefficients, _ = _independent_real_packet()
    assert _zero(sum(sp.diff(W[i], X[i]) for i in range(3)))
    assert _zero(xi.dot(d)-sum(sp.diff(b[i], X[i]) for i in range(3)))
    assert not _zero(coefficients[0])
    assert not _zero(coefficients[1])


@lru_cache(maxsize=1)
def _independent_forced_packet():
    x, y, z, t = sp.symbols("x y z t", real=True)
    X = (x, y, z)
    h = sp.symbols("h", positive=True)
    n = sp.symbols("n", integer=True, nonzero=True)
    V = sp.Matrix([0, x, 0])
    A = V.jacobian(X)
    S = y-t*x+x*z
    xi = sp.Matrix([sp.diff(S, a) for a in X])
    # A complex transverse amplitude tests both quadratures. The normal
    # forcing is deliberately nonzero, so omitting its pressure is caught.
    g = xi.dot(xi)*xi.cross(sp.Matrix([1, sp.I, 0]))
    Gg = -A*g+2*xi*xi.dot(A*g)/xi.dot(xi)
    H = (Gg-g.diff(t)-g.jacobian(X)*V+(1+z-2*x)*xi).applyfunc(sp.cancel)
    potential = (xi.cross(g)/xi.dot(xi)).applyfunc(sp.cancel)
    E = sp.exp(sp.I*n*S/h)
    packet = h*_curl(sp.I*potential*E, X)/n
    pressure = pressure_amplitude(g, H, A, xi, h, n)*E
    # No factored-operator helper: differentiate the actual exponential
    # field, with its exact pressure, before removing E.
    actual = packet.diff(t)+packet.jacobian(X)*V+A*packet
    actual += sp.Matrix([sp.diff(pressure, a) for a in X])+H*E
    actual = (actual/E).applyfunc(lambda a: sp.cancel(sp.expand(a)))
    expected = forced_remainder(g, H, V, xi, X, t, h, n)
    return X, t, h, n, V, A, S, xi, g, H, packet, E, actual, expected


@pytest.mark.parametrize("harmonic", [1, 2, -1])
def test_forced_lift_against_full_exponential_differentiation(harmonic):
    *_, actual, expected = _independent_forced_packet()
    n = _independent_forced_packet()[3]
    assert _zero((actual-expected).subs(n, harmonic))


def test_forced_packet_lift_has_exact_curl_divergence_for_complex_amplitude():
    X, _, h, n, _, _, _, xi, g, _, packet, E, _, _ = _independent_forced_packet()
    assert _zero(sum(sp.diff(packet[i], X[i]) for i in range(3))/E)
    assert _zero(packet/E-curl_lift_amplitude(g, xi, X, h, n))


def test_missing_normal_pressure_leaves_a_nonzero_order_one_residual():
    X, _, h, n, _, A, _, xi, g, H, _, _, _, _ = _independent_forced_packet()
    normal_pressure = (pressure_amplitude(g, H, A, xi, h, n)
                       -pressure_amplitude(g, H, A, xi, h, n, normal_forcing=False))
    # Removing this pressure leaves +Pi_normal H at order h^0.
    defect = -sp.Matrix([sp.diff(normal_pressure, a) for a in X])
    defect -= sp.I*n*xi*normal_pressure/h
    leading = defect.applyfunc(sp.cancel).subs(h, 0)
    assert _zero(leading-xi*xi.dot(H)/xi.dot(xi))
    assert not _zero(leading)


@pytest.mark.parametrize("function", [curl_lift_amplitude, pressure_amplitude])
def test_zero_harmonic_cannot_use_oscillatory_inverse(function):
    x, y, z = X = sp.symbols("x y z", real=True)
    xi, g = sp.Matrix([0, 0, 1]), sp.Matrix([1, 0, 0])
    with pytest.raises(ValueError):
        if function is curl_lift_amplitude:
            function(g, xi, X, sp.Symbol("h"), 0)
        else:
            function(g, sp.zeros(3, 1), sp.zeros(3), xi, sp.Symbol("h"), 0)


def test_mean_feedback_fast_term_by_differentiating_an_actual_cross_advection():
    x, y, z = X = sp.symbols("x y z", real=True)
    h = sp.symbols("h", positive=True)
    S = z+x*y
    xi = sp.Matrix([y, x, 1])
    b = xi.dot(xi)*xi.cross(sp.Matrix([x, 1, 0]))
    potential = (xi.cross(b)/xi.dot(xi)).applyfunc(sp.cancel)
    d = _curl(potential, X)
    E = sp.exp(sp.I*S/h)
    Z = h*_curl(sp.I*potential*E, X)
    m = sp.Matrix([z, x, y])
    raw = (Z.jacobian(X)*m+m.jacobian(X)*Z)/E
    leading_coefficient = (h*raw).applyfunc(lambda a: sp.cancel(sp.expand(a))).subs(h, 0)
    assert _zero(leading_coefficient-sp.I*m.dot(xi)*b)
    assert not _zero(leading_coefficient)
    slow = b.jacobian(X)*m+m.jacobian(X)*b-m.dot(xi)*d
    slow += sp.I*h*(d.jacobian(X)*m+m.jacobian(X)*d)
    assert _zero(raw-sp.I*m.dot(xi)*b/h-slow)


def test_point_amplitude_and_volume_normalization_by_actual_integration():
    x, delta, a = sp.symbols("x delta a", positive=True)
    f = 1-(x/delta)**2
    one_mass = sp.integrate(f*f, (x, -delta, delta))
    fourth_mass = sp.integrate(f**4, (x, -delta, delta))
    quadratic_derivative = sp.integrate(f*f*sp.diff(f, x)**2, (x, -delta, delta))
    # The tensor-product envelope on its cube checks the volume powers;
    # this polynomial fixture is not asserted to be smooth at the boundary.
    mass_squared = sp.factor(a*a*one_mass**3)
    nonlinear_scale_squared = sp.factor(a**4*quadratic_derivative*fourth_mass**2)
    assert mass_squared == R(4096, 3375)*a*a*delta**3
    assert nonlinear_scale_squared == R(4194304, 10418625)*a**4*delta


@pytest.mark.parametrize("order,expected", [(9, -R(1, 36)), (10, 0),
                                           (11, R(1, 44)), (12, R(1, 24))])
def test_second_order_gradient_margin_from_independent_GN_weights(order, expected):
    # In three dimensions the derivative L-infinity interpolation weight
    # is (1+3/2)/s. Apply it directly to L2 h^(11/4) and Hs h^(7/4-s).
    weight = R(5, 2*order)
    direct = (1-weight)*R(11, 4)+weight*(R(7, 4)-order)
    assert direct == expected
    assert gradient_error_exponent(R(11, 4), R(7, 4)-order, order) == direct


def test_first_order_only_fails_the_gradient_bootstrap_at_every_sobolev_order():
    s = sp.symbols("s", positive=True)
    weight = R(5, 2)/s
    first_only = sp.factor((1-weight)*R(9, 4)+weight*(R(7, 4)-s))
    assert sp.simplify(first_only+R(1, 4)+R(5, 4)/s) == 0
    assert first_only.is_negative is True
    velocity = (1-R(3, 24))*R(11, 4)+R(3, 24)*(R(7, 4)-12)
    assert velocity == R(9, 8)


def test_residual_powers_from_independent_pointwise_and_volume_products():
    h = sp.symbols("h", positive=True)
    delta = sp.sqrt(h)
    volume_norm = delta**R(3, 2)
    primary, correction, mean = h, h*h/delta, h*h/delta
    products = {
        "forced_harmonic_remainder": h*(correction/delta)*volume_norm,
        "primary_correction_or_mean_primary_slow": (primary*correction/delta)*volume_norm,
        "mean_correction_fast": (mean*correction/h)*volume_norm,
        "mean_self_or_correction_pair": mean*(h*h*delta**(-R(1, 2))),
        "primary_viscosity": h**4*(primary/h**2)*volume_norm,
        "harmonic_correction_viscosity": h**4*(correction/h**2)*volume_norm,
        "mean_viscosity": h**4*h*h*delta**(-R(3, 2)),
        "primary_background_mismatch": h**4*(primary/h)*volume_norm,
    }
    saved = build_receipt()["scaling"]["residual_L2_h_powers_theta_half"]
    for key, product in products.items():
        exponent = sp.sympify(saved[key])
        assert sp.simplify(product/h**exponent) == 1
        assert exponent >= R(11, 4)


def test_outgoing_gradient_can_have_large_strain_and_only_zero_eigenvalues():
    # Non-axis-aligned independent vectors avoid reproducing the receipt's
    # diagonal-frame fixture. Matrix powers give the exact finite-time map.
    p, N = sp.Matrix([1, 2, 3]), sp.Matrix([2, -1, 0])
    kappa, t = sp.symbols("kappa t", real=True)
    A = kappa*p*N.T
    S = (A+A.T)/2
    assert p.dot(N) == 0
    assert A*A == sp.zeros(3)
    assert A.eigenvals() == {0: 3}
    assert sp.factor((S*S).trace()) == 35*kappa*kappa
    assert S.det() == 0
    assert sp.simplify((sp.eye(3)+t*A).det()) == 1
    assert _zero((sp.eye(3)+t*A).diff(t)-A*(sp.eye(3)+t*A))


def test_receipt_writer_isolated_and_json_boolean_types(tmp_path):
    target = tmp_path / "loglog.json"
    assert main(["--out", str(target)]) == 0
    receipt = json.loads(target.read_text())
    assert receipt["all_green"] is True
    assert receipt["PDE_theorem_certified"] is False
    assert all(type(v) is bool for v in receipt["checks"].values())
