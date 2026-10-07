#!/usr/bin/env python3
"""Bounded exact checks for the postfocus coarse-source calculation.

These checks cover finite algebra only. They do not certify the analytic
matching, actual-q comparison, PDE continuation, or any infinite cascade.
No flow simulation or parameter search is performed.
"""

from fractions import Fraction as F
import json

import sympy as s


def run_checks():
    checks = []

    def record(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    z, a, c = s.symbols("z a c", real=True)
    p = 1 + a**2 * z**4
    q = 2 * a**2 * z**2 + 2 * c
    reduced = z**2 * q / p - s.diff(z**2 * s.diff(p, z) / p, z) / 2
    target = 2 * c * z**2 / p - 8 * a**2 * z**4 / p**2
    record("stable_integral_identity", s.simplify(reduced - target) == 0)

    ap, cp = s.symbols("ap cp", positive=True)
    positive_form = 2 * ap * (
        cp * z**2 / (1 + ap**2 * z**4)
        + 4 * ap**2 * z**4 / (1 + ap**2 * z**4) ** 2
    )
    signed_integrand = 2 * a * (
        c * z**2 / p - 4 * a**2 * z**4 / p**2
    )
    record(
        "strict_positive_integrand_for_negative_a_c",
        s.simplify(signed_integrand.subs({a: -ap, c: -cp}) - positive_form) == 0,
    )

    entries = s.symbols("a00 a01 a02 a10 a11 a12 a20 a21")
    a00, a01, a02, a10, a11, a12, a20, a21 = entries
    a0 = s.Matrix(
        [[a00, a01, a02], [a10, a11, a12], [a20, a21, -a00 - a11]]
    )
    beta1, beta2, v1, v2, ell = s.symbols("beta1 beta2 v1 v2 ell", nonzero=True)
    normal = s.Matrix([0, 0, 1])
    beta = s.Matrix([beta1, beta2, 0])
    tangent = s.Matrix([v1, v2, 0])
    abar = a0 - beta * normal.T / ell

    def kelvin(matrix, covector):
        return -matrix + 2 * covector * (covector.T * matrix) / covector.dot(covector)

    record(
        "primary_cotangent_unchanged_by_rank_one_shear",
        s.simplify((-abar.T + a0.T) * normal) == s.zeros(3, 1),
    )
    record(
        "full_pressure_kelvin_restriction",
        s.simplify((kelvin(abar, normal) - kelvin(a0, normal)) * tangent)
        == s.zeros(3, 1),
    )

    k1, k2, k3, f1, f2, f3 = s.symbols("k1 k2 k3 f1 f2 f3", real=True)
    wave = s.Matrix([k1, k2, k3])
    auxiliary = s.Matrix([f1, f2, f3])
    velocity = wave.cross(auxiliary)
    projector = s.eye(3) - wave * wave.T / wave.dot(wave)
    constraint_derivative = (-a0.T * wave).dot(velocity) + wave.dot(
        kelvin(a0, wave) * velocity + projector * auxiliary
    )
    record("forced_kelvin_preserves_transversality", s.simplify(constraint_derivative) == 0)
    strain_symbol = s.I * (velocity * wave.T + wave * velocity.T) / 2
    record(
        "band_strain_duality",
        s.simplify(2 * s.I * strain_symbol * wave + wave.dot(wave) * velocity)
        == s.zeros(3, 1),
    )

    scale_equalities = {
        "inner_stable_mass": (F(-1, 2) + 2 * F(5, 2), F(9, 2)),
        "incoming_outer_tail": (2 + 5 * F(3, 10), F(7, 2)),
        "outgoing_outer_tail": (2 * F(5, 2) - 1, F(4)),
        "growing_overlap": (F(1, 2) - F(3, 10), F(1, 5)),
        "normalized_endpoint_ell_power": (2 * F(7, 8) - F(1, 2) - F(1, 8), F(9, 8)),
        "velocity_h_power": (2 * F(3, 2) + 3 * F(5, 4) - 4 * F(5, 4), F(7, 4)),
        "strain_h_power": (2 * F(3, 2) + 3 * F(5, 4) - 5 * F(5, 4), F(1, 2)),
        "coarse_heat_h_power": (4 - 2 * F(5, 4), F(3, 2)),
        "relative_stress_h_power": (F(29, 8) + F(27, 8), F(7)),
        "focus_translation": (F(-3, 4) + F(1, 2), F(-1, 4)),
        "physical_radial_scale": (10 + F(5, 4), F(45, 4)),
    }
    for name, (left, right) in scale_equalities.items():
        record(name, left == right)

    return {
        "scope": "finite_exact_algebra_only",
        "checks_passed": len(checks),
        "checks": checks,
        "dns_run": False,
        "ns_solution_claim": False,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2))
