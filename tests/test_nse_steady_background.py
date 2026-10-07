"""Check algebra and independent exact ODE controls, not a numerical PDE claim."""

import json

import pytest
import sympy as sp

from experiments.nse_steady_background import (
    bootstrap_checks, build_receipt, comparison_envelope, main,
    ode_checks, polarization_rhs, scaling_checks,
)


def test_exact_sections_and_claim_boundary():
    for section in (scaling_checks(), bootstrap_checks(), ode_checks()):
        assert all(section["checks"].values()), section
    receipt = build_receipt()
    assert receipt["all_green"]
    assert receipt["root_status"] == receipt["E_prime_status"] == "OPEN"
    assert not receipt["dns_run"]
    assert not receipt["compact_profile_computed"]
    assert not receipt["oblique_Floquet_map_computed"]


def test_independent_affine_control_distinguishes_frequency_and_velocity_gain():
    t = sp.symbols("t", real=True)
    A = sp.diag(-2, 2, 0)
    # A neutral covector permits a growing velocity polarization.
    xi = sp.Matrix([0, 0, 1])
    b = sp.Matrix([sp.exp(2*t), 0, 0])
    assert sp.diff(xi, t) == -A.T*xi
    assert sp.diff(b, t) == polarization_rhs(A, xi, b)
    assert xi.dot(b) == 0
    # A growing covector instead has a decaying transverse polarization here.
    xi = sp.Matrix([sp.exp(2*t), 0, 0])
    b = sp.Matrix([0, sp.exp(-2*t), 0])
    assert sp.diff(xi, t) == -A.T*xi
    assert sp.diff(b, t) == polarization_rhs(A, xi, b)


def test_solid_rotation_pressure_normal_independent_periodic_control():
    t = sp.symbols("t", real=True)
    A = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    X = sp.Matrix([sp.cos(t), sp.sin(t), 0])
    # P=(x^2+y^2)/2; xi=grad P; V=A X.
    xi, b = X, A*X
    assert sp.simplify(sp.diff(xi, t)+A.T*xi) == sp.zeros(3, 1)
    assert sp.simplify(sp.diff(b, t)-polarization_rhs(A, xi, b)) == sp.zeros(3, 1)
    assert b.subs(t, 2*sp.pi) == b.subs(t, 0)
    # This affine control is not asserted to be the compact Gavrilov field.


def test_return_condition_is_not_automatic_for_closed_particle_orbit():
    # At I0 the orbit winds (1,2) in period 2pi; local Omega'=(3,5).
    D = sp.Matrix([[1, 0, 6*sp.pi], [0, 1, 10*sp.pi], [0, 0, 1]])
    returning = sp.Matrix([5, -3, 7])
    other = sp.Matrix([1, 0, 7])
    assert D.inv().T*returning == returning
    assert D.inv().T*other != other


def test_bootstrap_radius_and_domain():
    eps, F, kappa, r = sp.Rational(1, 100), 3, 5, sp.Rational(1, 2)
    T = sp.log(1+kappa*r/(2*eps*F))/kappa
    assert comparison_envelope(eps, F, kappa, 0) == 0
    assert sp.simplify(comparison_envelope(eps, F, kappa, T)-r/2) == 0
    assert sp.simplify(comparison_envelope(eps, F, kappa, 2*T)-r) > 0
    with pytest.raises(ValueError):
        comparison_envelope(eps, F, kappa, -1)
    with pytest.raises(ValueError):
        polarization_rhs(sp.eye(3), sp.zeros(3, 1), sp.ones(3, 1))


def test_writer_uses_test_destination(tmp_path):
    target = tmp_path / "steady.json"
    assert main(["--out", str(target)]) == 0
    assert json.loads(target.read_text())["all_green"]
