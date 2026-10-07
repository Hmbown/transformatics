"""Independent column and cone controls; no unvalidated Gavrilov integration."""

import json

import pytest
import sympy as sp

from experiments.nse_gavrilov_oblique import (
    EIGENBASIS, LIMIT, build_receipt, cone_faces, limiting_geometry,
    main, plane_coordinates, plane_lift, reduced_matrix,
)


def test_exact_pins_and_scope():
    data = build_receipt()
    assert data["all_green"], data["checks"]
    assert data["root_status"] == "OPEN"
    assert not data["dns_run"]
    assert not data["specific_j_computed"]
    assert not data["full_NS_amplification_proved"]
    assert not data["lean_kernel_checked"]


def test_independent_cartesian_column_gradient_and_pressure():
    # Locally f(r)=r^-2 near r=1; U=(-y/r^2,x/r^2,c/r).
    x, y, z = sp.symbols("x y z", real=True)
    r2 = x*x+y*y
    c = sp.sqrt(2)/2
    U = sp.Matrix([-y/r2, x/r2, c/sp.sqrt(r2)])
    pressure = -1/(2*r2)
    A = U.jacobian([x, y, z])
    assert sp.simplify(A.trace()) == 0
    assert sp.simplify(A*U+sp.Matrix([sp.diff(pressure, v) for v in (x, y, z)])) == sp.zeros(3, 1)
    assert A.subs({x: 1, y: 0}) == limiting_geometry()[0]
    # This column is a local control, not the compact Gavrilov solution.


def test_moving_frame_reduction_matches_explicit_growing_solution():
    A, O, k = limiting_geometry()
    t = sp.symbols("t", real=True)
    eigenvector = sp.Matrix([-sp.Rational(4, 3), 1])
    b = plane_lift(k)*eigenvector*sp.exp(2*t/3)
    # Direct three-component equation, independent of reduced_matrix.
    full_rhs = -A*b-O*b+2*k*(k.dot(A*b))/k.dot(k)
    assert sp.simplify(sp.diff(b, t)-full_rhs) == sp.zeros(3, 1)
    assert sp.simplify(k.dot(b)) == 0


def test_general_plane_chart_and_degenerate_case():
    k = sp.Matrix([3, -2, 5])
    lift, chart = plane_lift(k), plane_coordinates(k)
    assert k.T*lift == sp.zeros(1, 2)
    assert chart*lift == sp.eye(2)
    with pytest.raises(ValueError):
        plane_lift([1, 0, 0])


def test_exact_period_map_and_similarity():
    # B^2=(4/9)I gives this closed-form fundamental matrix.
    t = sp.symbols("t", real=True)
    F = sp.cosh(2*t/3)*sp.eye(2)+sp.Rational(3, 2)*sp.sinh(2*t/3)*LIMIT
    assert sp.simplify(sp.diff(F, t)-LIMIT*F) == sp.zeros(2)
    assert sp.simplify(F.det()) == 1
    diagonal = EIGENBASIS.inv()*LIMIT*EIGENBASIS
    assert diagonal == sp.diag(sp.Rational(2, 3), -sp.Rational(2, 3))


def test_cone_checks_reject_large_uncontrolled_errors():
    # This perturbation ejects the upper cone face; generic continuity needs a bound.
    low, high, growth = cone_faces(sp.Matrix([[0, 0], [1, 0]]))
    assert high > 0
    assert growth > 0  # Growth alone is insufficient for cone invariance.


def test_cutoff_slope_is_material():
    c = sp.sqrt(2)/2
    f, h = sp.symbols("f h", real=True)
    O = sp.Matrix([[0, -f, 0], [f, 0, 0], [0, 0, 0]])
    A = sp.Matrix([[0, -f, 0], [f*(1+h), 0, 0], [c*f*(1+h), 0, 0]])
    # h=-1 permits an axial returning covector; its polarization is stable.
    stable = reduced_matrix(A.subs({h: -1, f: 1}), O.subs(f, 1), sp.Matrix([0, 0, 1]))
    assert stable*stable == -2*sp.eye(2)
    assert reduced_matrix(*limiting_geometry()) == LIMIT


def test_receipt_writer_isolated(tmp_path):
    target = tmp_path / "oblique.json"
    assert main(["--out", str(target)]) == 0
    assert json.loads(target.read_text())["all_green"]
