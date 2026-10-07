#!/usr/bin/env python3
"""Finite algebra checks for exact-linear coarse-band exclusion.

No PDE simulation is performed. Analytic remainder, support, and energy
estimates are written in actual-coarse-band.md.
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

    k1, k2, k3, h1, h2, h3 = s.symbols("k1 k2 k3 h1 h2 h3", real=True)
    xi = s.Matrix([k1, k2, k3])
    forcing = s.Matrix([h1, h2, h3])
    proj = s.eye(3) - xi * xi.T / xi.dot(xi)
    record(
        "full_longitudinal_pressure_recovers_entire_forcing",
        s.simplify(-proj * forcing - xi * xi.dot(forcing) / xi.dot(xi) + forcing)
        == s.zeros(3, 1),
    )

    k, d = F(3, 2), F(5, 4)
    rho = k - d
    checks_of_powers = {
        "linear_corrected_residual": (k + 2 * rho + F(3, 2) * d, F(31, 8)),
        "weighted_linear_initial_L2": (k + F(3, 2) * d, F(27, 8)),
        "linear_H12": (k + F(3, 2) * d - 12 * k, F(-117, 8)),
        "linear_error_gradient": (
            F(31, 8) * F(19, 24) - F(117, 8) * F(5, 24),
            F(1, 48),
        ),
        "linear_error_velocity": (
            F(31, 8) * F(7, 8) - F(117, 8) * F(1, 8),
            F(25, 16),
        ),
        "linear_error_band": (F(31, 8) - F(3, 2) * d, F(2)),
        "two_IBP_profile_band": (-3 * d + k + 3 * d + 2 * rho, F(2)),
        "background_H12": (F(7, 4) - 12, F(-41, 4)),
        "background_band": (F(7, 4) - 12 + d * F(21, 2), F(23, 8)),
        "initial_band_gradient": (2 - d, F(3, 4)),
        "endpoint_velocity_margin": (2 - F(7, 4), F(1, 4)),
        "endpoint_strain_margin": (F(3, 4) - F(1, 2), F(1, 4)),
        "weighted_q_derivative_ratio": (k - 1, F(1, 2)),
        "mean_gradient": (k + rho - d, F(1, 2)),
        "profile_gradient": (k + rho - k, F(1, 4)),
    }
    for name, (left, right) in checks_of_powers.items():
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
