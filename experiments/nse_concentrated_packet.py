"""Exact pins for concentrated background persistence and relative NS energy.

See references/navier-stokes/concentrated-packet.md for the restricted PDE
theorems and their proofs. All-mode background bounds reuse classical local
theory. The relative estimate does not prove a perturbed solution smooth.
No DNS or finite-time singularity is computed by this instrument.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

import sympy as sp

from experiments.nse_frequency_activation import (
    bilinear, coefficient, raw_bilinear, support, vector_add, vector_inner,
)
from experiments.nse_qgso_transfer_budget import add, derivative, scale

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_concentrated_packet.json"
PERSISTENCE_X = sp.Rational(1, 512)
LOCAL_X = sp.Rational(1, 6)


def _positive_integer(n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")


def packet_moments(n):
    """Closed exact moments; evaluates arbitrary integer n without a field/grid."""
    _positive_integer(n)
    n = sp.Integer(n)
    d = 2*n + 1
    S2 = n*(2*n-1)*(7*n-1)/6

    def sum4(r):
        return r*(r+1)*(2*r+1)*(3*r*r+3*r-1)/30

    S4 = sp.expand(sum4(2*n-1)-sum4(n-1))
    E = 2*d*S2*S4
    D = 2*d*S2*S2
    m, L = 4*n*n*d, 3*n
    return {
        "n": int(n), "cutoff": int(L), "mode_count": int(m),
        "max_frequency_squared": int(9*n*n-8*n+2),
        "S2": S2, "S4": S4,
        "raw_mean_norm_squared": E, "raw_compressive_gradient": D,
        "sigma_squared_over_a_squared": sp.cancel(D*D/E),
        "sigma_squared_over_LWbar_squared": sp.cancel(D*D/(E*L*L*m)),
    }


def packet_fourier(n):
    """Enumerate the unnormalized real solenoidal witness, never project its input.

    F_n = sum k1*k2*(-k2,k1,0)*sin(k.x), where k1 in [n,2n),
    |k2| in [n,2n), and |k3|<=n. Use closed moments for larger n.
    """
    _positive_integer(n)
    if n > 16:
        raise ValueError("enumerated witnesses stop at n=16; use packet_moments")
    second = list(range(n, 2*n)) + list(range(1-2*n, 1-n))
    u = [{} for _ in range(3)]
    for p, q, r in product(range(n, 2*n), second, range(-n, n+1)):
        k = (p, q, r)
        v = (-p*q*q, p*p*q, 0)
        for i in range(3):
            if v[i]:
                u[i][k] = v[i]/(2*sp.I)
                u[i][(-p, -q, -r)] = -v[i]/(2*sp.I)
    return u


def gradient_at_zero(u):
    return sp.Matrix(3, 3, lambda i, j:
                     sp.expand(sum(sp.I*k[j]*v for k, v in u[i].items())))


def reflection_covariant(u):
    for axis in range(3):
        for k in support(u):
            reflected = tuple(-q if j == axis else q for j, q in enumerate(k))
            for i in range(3):
                sign = -1 if i == axis else 1
                if u[i].get(reflected, 0) != sign*u[i].get(k, 0):
                    return False
    return True


@lru_cache(maxsize=1)
def packet_exact_checks():
    checks, rows = {}, []
    for n in (1, 2, 4):
        u = packet_fourier(n)
        p = packet_moments(n)
        D = p["raw_compressive_gradient"]
        checks.update({
            f"n{n}.raw_divergence": add(*(derivative(u[i], i) for i in range(3))) == {},
            f"n{n}.real": all(u[i].get(tuple(-q for q in k), 0) == sp.conjugate(v)
                             for i in range(3) for k, v in u[i].items()),
            f"n{n}.mean_zero": all((0, 0, 0) not in c for c in u),
            f"n{n}.mode_count": len(support(u)) == p["mode_count"],
            f"n{n}.spectral_rank_three": sp.Matrix(sorted(support(u))).rank() == 3,
            f"n{n}.actual_support_radius": max(sum(q*q for q in k) for k in support(u)) == p["max_frequency_squared"],
            f"n{n}.mean_norm": vector_inner(u, u) == p["raw_mean_norm_squared"],
            f"n{n}.central_hyperbolic_gradient": gradient_at_zero(u) == sp.diag(-D, D, 0),
            f"n{n}.coordinate_reflections": reflection_covariant(u),
        })
        rows.append({k: str(v) if isinstance(v, sp.Basic) else v for k, v in p.items()})
    b = bilinear(packet_fourier(1), packet_fourier(1))
    checks["pressure_generates_third_component"] = coefficient(b, (2, 0, 2))[2] == -sp.I/2
    return {"checks": checks, "rows": rows,
            "third_component_NS_tangent": "B(F1,F1)_hat_3(2,0,2)=-i/2; F1_3=0 initially"}


def high_seed(j, shifted=False):
    """Four high modes; the self-interaction generates a low frequency."""
    _positive_integer(j)
    qx = 1-2*j if shifted else -2*j
    u = [{} for _ in range(3)]
    for k, v in [((2*j, 0, 0), (0, 1, 0)), ((qx, 1, 0), (1, -qx, 0))]:
        for i in range(3):
            if v[i]:
                u[i][k] = sp.Integer(v[i])
                u[i][tuple(-q for q in k)] = sp.Integer(v[i])
    return u


@lru_cache(maxsize=1)
def relative_energy_checks():
    U = packet_fourier(1)
    w = high_seed(2, shifted=True)
    full = vector_add(U, w)
    w_rhs = vector_add(bilinear(full, full), [scale(p, -1) for p in bilinear(U, U)])
    actual = vector_inner(w, w_rhs)
    compression = vector_inner(w, raw_bilinear(w, U))
    leak = high_seed(3)
    leak_rhs = bilinear(leak, leak)
    return {
        "checks": {
            "relative_full_rhs_identity": actual == compression,
            "relative_compression_not_vacuously_zero": compression != 0,
            "background_transport_cancels": vector_inner(w, raw_bilinear(U, w)) == 0,
            "perturbation_self_transport_cancels": vector_inner(w, raw_bilinear(w, w)) == 0,
            "high_seed_raw_divergence": add(*(derivative(leak[i], i) for i in range(3))) == {},
            "seed_initially_all_above_cutoff": all(sum(q*q for q in k) > 9 for k in support(leak)),
            "high_self_interaction_generates_low_mode": coefficient(leak_rhs, (0, 1, 0)) == (-sp.I, 0, 0),
        },
        "nonlinear_relative_pairing": str(actual),
        "low_generated_coefficient": "(-i,0,0) at (0,1,0)",
        "scope": "Exact instantaneous identities supporting a written integrated PDE estimate; no support invariance is asserted.",
    }


def relative_envelope(Wbar, L, t, H, epsilon):
    """Rational upper envelope on high-pass mean L2 for x=L*Wbar*t<=1/6."""
    W, L, t, H, eps = map(sp.sympify, (Wbar, L, t, H, epsilon))
    x = L*W*t
    if not (W > 0 and L > 0 and H >= L and t >= 0 and eps >= 0 and x <= LOCAL_X):
        raise ValueError("requires Wbar,L>0, H>=L, t,epsilon>=0, and L*Wbar*t<=1/6")
    r = 3*x
    J = sp.floor(H/L)
    tail = sp.cancel(W*r**J/(1-r))
    clock = sp.cancel(x/(1-3*x))
    gain = sp.cancel(1/(1-clock))  # exp(clock) <= 1/(1-clock), 0<=clock<=1/3.
    return {"x": x, "J": J, "background_tail": tail,
            "strain_integral_bound": clock, "relative_gain_bound": gain,
            "total_bound": sp.cancel(tail + gain*eps)}


def persistence_checks():
    x = PERSISTENCE_X
    temporal = x + (1-3*x)**-2 - 1
    spatial = (1+3*x)/(64*(1-3*x)**3)
    clock = x/(1-3*x)
    # Universal polynomial checks use n=z+1, z>=0; all coefficients nonnegative.
    n, z = sp.symbols("n z")
    S2 = n*(2*n-1)*(7*n-1)/6
    def sum4(r):
        return r*(r+1)*(2*r+1)*(3*r*r+3*r-1)/30
    S4 = sp.expand(sum4(2*n-1)-sum4(n-1))
    polynomials = {
        "S2_lower": S2-n**3,
        "S4_upper": 4*n*n*S2-S4,
        "sigma_ratio_lower_one_over_72": 4*S2**3-n**4*S4,
    }
    universal = {name: all(c >= 0 for c in sp.Poly(sp.expand(p.subs(n, z+1)), z).all_coeffs())
                 for name, p in polynomials.items()}
    return {
        "checks": {
            **universal,
            "temporal_gradient_margin": bool(temporal < sp.Rational(1, 36)),
            "spatial_gradient_margin": bool(spatial < sp.Rational(1, 36)),
            "material_ball_trapping": bool(1/(1-clock) < 2),
            "clock_exact": clock == sp.Rational(1, 509),
            "minimum_compression_integral": x/18 == sp.Rational(1, 9216),
        },
        "time_fraction": str(x),
        "temporal_margin": str(sp.Rational(1, 36)-temporal),
        "spatial_margin": str(sp.Rational(1, 36)-spatial),
        "flow_radius_amplification_upper": str(1/(1-clock)),
        "minimum_compression_integral": "1/9216",
        "universal_polynomials_at_n_equal_z_plus_one": {
            name: str(sp.expand(p.subs(n, z+1))) for name, p in polynomials.items()},
    }


def seed_exclusion_checks():
    eta = sp.Rational(1, 8)
    result = relative_envelope(1, 1, LOCAL_X, 6, eta/3)
    return {
        "checks": {
            "strain_clock_at_most_one_third": result["strain_integral_bound"] == sp.Rational(1, 3),
            "relative_gain_at_most_three_halves": result["relative_gain_bound"] == sp.Rational(3, 2),
            "background_tail_at_most_target_quarter": result["background_tail"] == eta/4,
            "strict_total_below_target": bool(result["total_bound"] == 3*eta/4 < eta),
        },
        "example": {k: str(v) for k, v in result.items()},
        "target": str(eta), "seed_norm": str(eta/3),
        "condition": "epsilon<=eta/3 and floor(H/L)>=max(1,ceil(log2(8 Wbar/eta)))",
    }


def build_receipt():
    sections = {"packet": packet_exact_checks(), "relative": relative_energy_checks(),
                "persistence": persistence_checks(), "exclusion": seed_exclusion_checks()}
    checks = {f"{name}.{k}": v for name, result in sections.items() for k, v in result["checks"].items()}
    return {
        "stamp": "2026-09-08", "node": "nse-concentrated-packet-local",
        "root_status": "OPEN", "E_prime_status": "OPEN", "gso_route_status": "DEAD",
        "evidence_class": "WRITTEN_RESTRICTED_PDE_ESTIMATES_WITH_EXACT_ALGEBRA_AND_INDEPENDENT_AGENT_AUDIT",
        "dns_run": False,
        **sections, "checks": checks, "all_green": all(checks.values()),
        "claim_boundary": "The exact low-data background has concentrated persistent local strain. Relative/high-pass L2 bounds allow every generated mode and arbitrary high seeds, but neither prove perturbed smoothness nor exclude a later cascade. Classical local/relative-energy tools; no novelty claim.",
        "remaining_estimate": "Control accumulated background strain and the seed phase/shape over intervals longer than the proved local window, or quantify adequate intermediate-mode seed generation. No such estimate is proved here.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args(argv)
    result = build_receipt()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{args.out}: {sum(result['checks'].values())}/{len(result['checks'])} exact checks; ROOT OPEN")
    return 0 if result["all_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
