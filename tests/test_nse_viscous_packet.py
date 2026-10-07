"""Independent algebra/normalization controls, not certification of PDE bounds."""

import json

import pytest
import sympy as sp

from experiments.nse_viscous_packet import (
    affine_packet_jet, build_receipt, conservative_c, curl, derivative_order,
    main, time_power, torus_mean,
)

R = sp.Rational


def test_exact_receipt_scope_and_negative_controls():
    receipt = build_receipt()
    assert receipt["all_green"], {k: v for k, v in receipt["checks"].items() if not v}
    assert receipt["root_status"] == receipt["E_prime_status"] == "OPEN"
    assert receipt["gso_route_status"] == "DEAD"
    for key in ("pde_analytic_estimates_certified", "lean_kernel_checked", "dns_run",
                "specific_profile_rates_computed", "unconditional_NS_solution_proved"):
        assert receipt[key] is False
    assert all(type(value) is bool for data in (receipt["packet"], receipt["energy"],
                                               receipt["scaling"], receipt["real_normalization"])
               for value in data["checks"].values())
    assert sum("negative_" in key for key in receipt["checks"]) >= 4


def test_independent_exact_shear_solution_at_finite_time():
    # Exact affine shear V=(y,0,0).  Its transported phase S=x-t*y has
    # xi=(1,-t,0), and the transverse polarization b=(t,1,0)/(1+t^2).
    # The envelope is transported too; verify the actual time-dependent
    # Cartesian curl against the factored residual for every symbolic t.
    x, y, z, t = sp.symbols("x y z t", real=True)
    h = sp.symbols("h", positive=True)
    coordinates = (x, y, z)
    xi = sp.Matrix([1, -t, 0])
    b0 = sp.Matrix([t, 1, 0])/(1+t*t)
    f = 1+(x-t*y)**2+y*z+z**3
    b = f*b0
    F = xi.cross(b)/xi.dot(xi)
    phase = sp.exp(sp.I*(x-t*y)/h)
    wave = h*curl(sp.I*F*phase, coordinates)
    A = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    pressure_amplitude = 2*xi.dot(A*b)/xi.dot(xi)
    pressure = sp.I*h*pressure_amplitude*phase
    correction = sp.I*curl(F, coordinates)
    residual = sp.diff(wave, t)+y*sp.diff(wave, x)+A*wave
    residual += sp.Matrix([sp.diff(pressure, a) for a in coordinates])
    expected = h*(sp.diff(correction, t)+y*sp.diff(correction, x)+A*correction
                  +sp.I*sp.Matrix([sp.diff(pressure_amplitude, a) for a in coordinates]))
    assert all(sp.simplify(sp.expand(residual[i]/phase)-expected[i]) == 0 for i in range(3))
    assert sp.simplify(sum(sp.diff(wave[i], coordinates[i]) for i in range(3))) == 0


def test_arbitrary_envelope_hessian_cancellation_against_closed_coefficients():
    x, y, z = coordinates = sp.symbols("x y z", real=True)
    h = sp.symbols("h", positive=True)
    f = sp.Function("independent_envelope")(*coordinates)
    jet = affine_packet_jet(sp.Matrix([[1, 2, 0], [0, -1, 1], [1, 0, 0]]),
                            [1, 2, 3], [2, -1, 0], f, coordinates, h)
    # Closed coefficient matrix recorded independently from the unsimplified
    # Cartesian derivative calculation; arbitrary f retains all Hessian jets.
    expected = sp.I*h*sp.Matrix([[252, -57, -46], [1, 70, -47],
                                 [46, -65, 28]])/98
    expected *= sp.Matrix([sp.diff(f, a) for a in coordinates])
    assert all(sp.simplify(a) == 0 for a in jet["residual"]-expected)
    assert max(map(derivative_order, jet["residual"])) == 1
    assert max(map(derivative_order, jet["laplacian"])) == 3


def test_second_jet_detects_missing_pressure_and_curl_correction():
    x, y, z = coordinates = sp.symbols("x y z", real=True)
    h = sp.symbols("h", positive=True)
    A = sp.Matrix([[2, 0, 1], [3, -1, 2], [-1, 1, -1]])
    xi, b0 = sp.Matrix([1, 0, 1]), sp.Matrix([1, 1, -1])
    f = 1+2*x+3*y+5*z+x*y*z
    good = affine_packet_jet(A, xi, b0, f, coordinates, h)
    bad = affine_packet_jet(A, xi, b0, f, coordinates, h, pressure_factor=1)
    assert good["divergence"] == 0
    assert sp.expand(good["uncorrected_divergence"]) == -x*y+x*z+y*z
    leading_defect = (bad["residual"]-good["residual"]).subs(h, 0)
    assert leading_defect == xi*f  # xi.A.b0/|xi|^2=1 for this second jet.
    assert any(a != 0 for a in leading_defect)
    with pytest.raises(ValueError):
        affine_packet_jet(A, xi, xi, f, coordinates, h)
    with pytest.raises(ValueError):
        affine_packet_jet(sp.eye(3), xi, b0, f, coordinates, h)


def test_actual_integral_checks_normalized_envelope_volume_factor():
    x, delta = sp.symbols("x delta", positive=True)
    factor = 1-(x/delta)**2
    mass1 = sp.integrate(factor**2, (x, -delta, delta))
    derivative1 = sp.integrate(sp.diff(factor, x)**2, (x, -delta, delta))
    # Tensor product of the endpoint-vanishing factors on [-delta,delta]^3.
    # This exact polynomial fixture verifies scaling, not C-infinity support.
    squared_mass = sp.simplify(delta**-3*mass1**3)
    squared_partial_norm = sp.simplify(delta**-3*derivative1*mass1**2)
    assert squared_mass == R(4096, 3375)
    assert squared_partial_norm == R(2048, 675)/delta**2
    assert sp.simplify(squared_partial_norm/squared_mass) == R(5, 2)/delta**2


def test_physical_average_normalization_on_exact_periodic_fixture():
    y, L, A = sp.symbols("y L A", positive=True)
    # F(y)=cos(y1/L) on T_L maps to u(x)=A*cos(x1) on the physical torus.
    rescaled_squared = sp.integrate(sp.cos(y/L)**2, (y, -sp.pi*L, sp.pi*L))*(2*sp.pi*L)**2
    physical_squared_average = A**2*sp.integrate(sp.cos(y)**2, (y, -sp.pi, sp.pi))/(2*sp.pi)
    factor_squared = A**2/(L**3*(2*sp.pi)**3)
    assert sp.simplify(factor_squared*rescaled_squared-physical_squared_average) == 0
    assert physical_squared_average == A**2/2
    assert sp.simplify((A**2*rescaled_squared/(2*sp.pi)**3)/physical_squared_average) == L**3


def test_transport_cancellation_requires_divergence_free_and_keeps_strain():
    x, y, z = coordinates = sp.symbols("x y z", real=True)
    e = sp.Matrix([sp.sin(y), sp.sin(2*x), 0])
    w = sp.Matrix([sp.sin(2*x)*sp.cos(y), -2*sp.cos(2*x)*sp.sin(y), 0])
    assert torus_mean(e.dot(e.jacobian(coordinates)*w), coordinates) == 0
    assert torus_mean(e.dot(w.jacobian(coordinates)*e), coordinates) == R(3, 4)
    # Direct one-dimensional integration, independent of torus_mean.
    e2 = 1+sp.cos(x)
    compressible_pair = sp.integrate(e2*sp.sin(x)*sp.diff(e2, x), (x, -sp.pi, sp.pi))/(2*sp.pi)
    assert compressible_pair == -R(1, 2)


def test_log_window_exponents_against_direct_substitution_and_bad_sign():
    epsilon, c, rate = R(1, 16), R(1, 3), sp.Integer(2)
    h = R(1, 2)
    actual = h*sp.exp(rate*c*sp.log(1/epsilon))
    assert sp.simplify(actual-h**time_power(1, rate, c)) == 0
    assert sp.simplify(actual-h**(1+4*rate*c)) != 0
    # Too-long windows are rejected by the real power, despite the tempting
    # reversed-sign formula always returning a positive power.
    assert time_power(R(1, 2), 3, 1) < 0


def test_strict_small_time_choice_for_disparate_fixed_rates():
    for rates in ((1, 1, 1, 1, 1), (10**6, 2, 3, 4, 5), (2, 3, 10**6, 4, 5),
                  (2, 3, 4, 10**6, 5), (2, 3, 4, 5, 10**6)):
        gamma, kappa, Kn, K3, Ke = map(sp.Integer, rates)
        c = conservative_c(*rates)
        assert c > 0 and c*kappa < 1
        assert time_power(R(1, 2), gamma, c) > 0
        assert time_power(3, Kn, c) > R(3, 2)
        assert time_power(3, K3, c) > R(3, 2)
        assert time_power(2, Ke, c) > 1
        # Actual physical high-pass UPPER bounds, not the signal lower bound.
        assert time_power(7, Kn, c)-R(11, 10) > R(22, 5)
    with pytest.raises(ValueError):
        conservative_c(1, 1, 0, 1, 1)


def test_real_quadrature_selection_is_a_weighted_ratio_at_one_time():
    # If both component gain ratios were smaller than their weighted average,
    # their sum would contradict the total ratio. Nonzero initial mass matters.
    initial = (R(2, 5), R(3, 5))
    final = (R(7, 10), R(9, 5))
    total = sum(final)/sum(initial)
    assert min(final[i]/initial[i] for i in range(2)) <= total
    assert max(final[i]/initial[i] for i in range(2)) >= total
    # The better quadrature can change at a different observation time.
    later = (R(9, 5), R(7, 10))
    assert final[1]/initial[1] > final[0]/initial[0]
    assert later[0]/initial[0] > later[1]/initial[1]


def test_receipt_writer_isolated(tmp_path):
    target = tmp_path / "viscous_packet.json"
    assert main(["--out", str(target)]) == 0
    receipt = json.loads(target.read_text())
    assert receipt["all_green"] is True
    assert receipt["pde_analytic_estimates_certified"] is False
    assert all(type(value) is bool for value in receipt["checks"].values())
