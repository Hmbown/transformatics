"""Exact algebra pins for selected Gavrilov oblique polarization instability.

The written analytic existence proof, including its imported analytic
coordinate expansion and small-parameter limit, is in
references/navier-stokes/gavrilov-oblique.md. This instrument does not compute
a Gavrilov orbit, an explicit smallness threshold, or a NS trajectory.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

import sympy as sp

from experiments.nse_steady_background import polarization_rhs

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_gavrilov_oblique.json"
LIMIT = sp.Matrix([[0, -sp.Rational(8, 9)], [-sp.Rational(1, 2), 0]])
EIGENBASIS = sp.Matrix([[-sp.Rational(4, 3), sp.Rational(4, 3)], [1, 1]])
CONE_ERROR = sp.Rational(1, 12)
CONE_RADIUS = sp.Rational(1, 2)


def limiting_geometry():
    c = sp.sqrt(2)/2
    A = sp.Matrix([[0, -1, 0], [-1, 0, 0], [-c, 0, 0]])
    frame_rate = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    k = sp.Matrix([0, -c, 2])
    return A, frame_rate, k


def plane_lift(k):
    """(b_normal,s=k_t b_axial-k_axial b_t) -> b in the plane k.b=0."""
    k = sp.Matrix(k)
    d = k[1]**2+k[2]**2
    if d == 0:
        raise ValueError("nonzero tangential/axial covector component required")
    return sp.Matrix([[1, 0], [-k[1]*k[0]/d, -k[2]/d],
                      [-k[2]*k[0]/d, k[1]/d]])


def plane_coordinates(k):
    k = sp.Matrix(k)
    return sp.Matrix([[1, 0, 0], [0, -k[2], k[1]]])


def reduced_matrix(A, frame_rate, k):
    """Constant moving-frame reduction; a variable k also needs chart derivatives."""
    b1, b2 = sp.symbols("bn s", real=True)
    b = plane_lift(k)*sp.Matrix([b1, b2])
    rhs = plane_coordinates(k)*(polarization_rhs(A, k, b)-frame_rate*b)
    return sp.simplify(rhs.jacobian([b1, b2]))


@lru_cache(maxsize=1)
def limit_checks():
    A, O, k = limiting_geometry()
    lift, chart = plane_lift(k), plane_coordinates(k)
    G = -A-O+2*k*k.T*A/k.dot(k)
    B = reduced_matrix(A, O, k)
    vorticity = sp.Matrix([A[2, 1]-A[1, 2], A[0, 2]-A[2, 0], A[1, 0]-A[0, 1]])
    return {
        "checks": {
            "trace_free_full_gradient": A.trace() == 0,
            "orthonormal_frame_rate_skew": O+O.T == sp.zeros(3),
            "returning_covector_in_frame": sp.simplify((-A.T-O)*k) == sp.zeros(3, 1),
            "plane_constraint": sp.simplify(k.T*lift) == sp.zeros(1, 2),
            "plane_chart_inverse": sp.simplify(chart*lift) == sp.eye(2),
            "full_generator_preserves_plane": sp.simplify(k.T*G*lift) == sp.zeros(1, 2),
            "pressure_corrected_reduction": B == LIMIT,
            "diagonalization": sp.simplify(EIGENBASIS.inv()*B*EIGENBASIS) == sp.diag(sp.Rational(2, 3), -sp.Rational(2, 3)),
            "squared_generator": B*B == sp.Rational(4, 9)*sp.eye(2),
            "nonzero_vorticity_covector_invariant": sp.simplify(vorticity.dot(k)) == -sp.Rational(1, 2),
            "pressure_restores_plane_constraint": sp.simplify(k.T*(-A-O)*lift) != sp.zeros(1, 2),
        },
        "gradient": str(A), "frame_rate": str(O), "covector": str(k),
        "polarization_matrix": str(B), "eigenvalues": ["2/3", "-2/3"],
        "one_poloid_limit_multipliers": ["exp(4*pi/3)", "exp(-4*pi/3)"],
        "vorticity_covector_pairing": "-1/2",
    }


@lru_cache(maxsize=1)
def asymptotic_checks():
    I, r = sp.symbols("I r", positive=True)
    k3, q1 = sp.symbols("k3 q1", real=True)
    # Only coefficients whose powers can affect these leading limits enter.
    K = I+k3*I**3
    q = sp.sqrt(I)*(1+q1*I)
    omega1 = sp.diff(K, I)
    omega1prime = -sp.diff(K, I)**2/K+sp.diff(K, I, 2)
    omega2prime = sp.diff(q, I)*omega1+q*omega1prime
    zeta_sigma = -2*omega2prime/omega1prime
    values = {
        "Omega1_limit": sp.limit(omega1.subs(I, r*r/2), r, 0),
        "r_squared_Omega1prime_limit": sp.limit((r*r*omega1prime.subs(I, r*r/2)), r, 0),
        "r_Omega2prime_limit": sp.limit((r*omega2prime.subs(I, r*r/2)), r, 0),
        "zeta_sigma_over_r_limit": sp.limit(zeta_sigma.subs(I, r*r/2)/r, r, 0),
    }
    expected = [1, -2, -sp.sqrt(2)/2, -sp.sqrt(2)/2]
    return {
        "checks": {name: value == target for (name, value), target in zip(values.items(), expected)},
        "leading_limits": {name: str(value) for name, value in values.items()},
        "scope": "Formal leading-jet algebra only. Uniform differentiated remainder control uses the cited analytic coordinate theorem in the written proof.",
    }


def cone_faces(R, radius=CONE_RADIUS):
    """Exact slope derivative at both cone faces, plus uniform growth floor."""
    R = sp.Matrix(R)
    h = sp.sympify(radius)
    lam = sp.Rational(2, 3)
    def slope(y):
        return R[1, 0]+(-2*lam+R[1, 1]-R[0, 0])*y-R[0, 1]*y*y
    return slope(-h), slope(h), lam+R[0, 0]-abs(R[0, 1])*h


@lru_cache(maxsize=1)
def cone_checks():
    rows = []
    for values in product((-CONE_ERROR, CONE_ERROR), repeat=4):
        low, high, growth = cone_faces(sp.Matrix(2, 2, values))
        rows.append((low, high, growth))
    lower, upper, growth = min(v[0] for v in rows), max(v[1] for v in rows), min(v[2] for v in rows)
    return {
        "checks": {
            "all_box_vertices_inward": all(low > 0 and high < 0 for low, high, _ in rows),
            "lower_face_margin": lower == sp.Rational(23, 48),
            "upper_face_margin": upper == -sp.Rational(23, 48),
            "uniform_growth_floor": growth == sp.Rational(13, 24),
            "growth_strictly_above_half": bool(growth > sp.Rational(1, 2)),
        },
        "error_entry_bound": str(CONE_ERROR), "slope_radius": str(CONE_RADIUS),
        "lower_face_margin": str(lower), "upper_face_margin": str(upper),
        "growth_rate_lower": str(growth),
        "periodic_multiplier_lower": "exp(13*pi/12)",
        "scope": "The four uncertain entries enter each face affinely; checking all 16 rational vertices certifies the full box. The cone invariance and fixed-point eigenvector argument are written separately.",
    }


def build_receipt():
    sections = {"limit": limit_checks(), "asymptotics": asymptotic_checks(), "cone": cone_checks()}
    checks = {f"{name}.{key}": bool(value) for name, section in sections.items() for key, value in section["checks"].items()}
    return {
        "stamp": "2026-09-08", "node": "nse-gavrilov-oblique-instability",
        "root_status": "OPEN", "E_prime_status": "OPEN", "gso_route_status": "DEAD",
        "evidence_class": "WRITTEN_ANALYTIC_EXISTENCE_PROOF_FOR_INVISCID_POLARIZATION_ODE_WITH_EXACT_ALGEBRA_PINS",
        "dns_run": False, "specific_j_computed": False, "full_NS_amplification_proved": False,
        "lean_kernel_checked": False,
        **sections, "checks": checks, "all_green": all(checks.values()),
        "claim_boundary": "For all sufficiently large selected rational tori and specified compact pressure cutoffs, the actual Gavrilov inviscid polarization ODE has an expanding oblique Floquet multiplier. Smallness threshold is existential, not numerically computed. No finite-wavelength NS activation, infinite cascade, novel-priority, or regularity claim.",
        "remaining_estimate": "Freeze one unstable profile; prove a localized finite-wavelength comparison with the actual viscous NS background, tracking pressure, phase, damping, seed amplitude and nonlinear error on the logarithmic interval.",
        "sources": ["https://arxiv.org/html/1810.08020v1", "https://arxiv.org/html/2302.02982v1"],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args(argv)
    data = build_receipt()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print(f"{args.out}: {sum(data['checks'].values())}/{len(data['checks'])} exact checks; ROOT OPEN")
    return 0 if data["all_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
