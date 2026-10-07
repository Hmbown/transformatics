"""Exact pins for a restricted full-NS frequency-activation estimate.

The continuum proof is in references/navier-stokes/frequency-activation.md.
This program checks finite Fourier algebra and rational constants. It does
not integrate a trajectory, certify a singularity, or prove ROOT by testing.
The convergent all-mode expansion is classical local theory, specialized
here to make the activation and remainder explicit; no novelty is claimed.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from math import factorial
from pathlib import Path

import sympy as sp

from experiments.nse_qgso_transfer_budget import (
    add, derivative, inner, multiply, scale, strain, vector_project,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_frequency_activation.json"
EPSILON = sp.Rational(1, 256)
TAU_STAR = sp.Rational(1, 512)


def cyclic_seed(frequency=1, amplitude=1):
    """u0 = A (cos(N y), cos(N z), cos(N x)); supplied field is solenoidal."""
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    a = sp.sympify(amplitude)
    if a.is_real is not True:
        raise ValueError("amplitude must be real")
    out = []
    for axis in (1, 2, 0):
        k = tuple(frequency if i == axis else 0 for i in range(3))
        out.append({k: a/2, tuple(-q for q in k): a/2})
    return [add(p) for p in out]


def raw_bilinear(a, b):
    """-(a . grad)b before pressure/Leray projection."""
    return [scale(add(*(multiply(a[j], derivative(b[i], j))
                        for j in range(3))), -1) for i in range(3)]


def bilinear(a, b):
    return vector_project(raw_bilinear(a, b))


def vector_add(a, b):
    return [add(p, q) for p, q in zip(a, b)]


def vector_inner(a, b):
    """Fourier mean inner product; physical integral is (2pi)^3 times this."""
    return sp.expand(sum(inner(p, q) for p, q in zip(a, b)))


def support(u):
    return set().union(*(p.keys() for p in u))


def coefficient(u, k):
    return tuple(p.get(k, sp.Integer(0)) for p in u)


def cutoff(u, cutoff_squared, high=False):
    return [{k: v for k, v in p.items()
             if (sum(q*q for q in k) > cutoff_squared) == high} for p in u]


def highpass_energy_defect(u, cutoff_squared):
    """Full nonlinearity vs low-low source plus low-strain amplification."""
    low = cutoff(u, cutoff_squared)
    high = cutoff(u, cutoff_squared, high=True)
    S = strain(low)
    stretching = sum(inner(high[i], multiply(S[i][j], high[j]))
                     for i in range(3) for j in range(3))
    # Both sides are the nonlinear part of one half d/dt ||high||_2^2.
    full = vector_inner(high, bilinear(u, u))
    split = vector_inner(high, bilinear(low, low)) - stretching
    return sp.expand(full - split)


@lru_cache(maxsize=1)
def exact_interactions():
    u = cyclic_seed()
    b = bilinear(u, u)
    raw_c = vector_add(raw_bilinear(u, b), raw_bilinear(b, u))
    c = vector_project(raw_c)
    s2 = {sum(q*q for q in k) for k in support(b)}
    s3 = {sum(q*q for q in k) for k in support(c)}
    combined = vector_add(u, [scale(p, sp.Rational(1, 5)) for p in b])
    checks = {
        "seed_raw_divergence_zero": add(*(derivative(u[i], i) for i in range(3))) == {},
        "seed_reality": all(p.get(tuple(-q for q in k), 0) == sp.conjugate(v)
                            for p in u for k, v in p.items()),
        "seed_frequency_rank_three": sp.Matrix(sorted(support(u))).rank() == 3,
        "seed_mean_zero": all((0, 0, 0) not in p for p in u),
        "first_twelve_modes_on_sqrt2_shell": len(support(b)) == 12 and s2 == {2},
        "target_signed_coefficient": coefficient(b, (1, 1, 0)) == (0, 0, -sp.I/4),
        "first_nonlinearity_mean_l2_squared": vector_inner(b, b) == sp.Rational(3, 4),
        "initial_energy_transfer_zero": vector_inner(u, b) == 0,
        "third_order_returns_to_seed_and_creates_sqrt5": len(support(c)) == 18 and s3 == {1, 5},
        "feedback_signed_coefficient": coefficient(c, (1, 0, 0)) == (0, 0, -sp.Rational(1, 4)),
        "next_generated_signed_coefficient": coefficient(c, (1, 2, 0)) == (0, 0, -sp.Rational(1, 8)),
        "pressure_is_nontrivial_at_next_order": coefficient(raw_c, (1, 1, 1)) == (-sp.Rational(1, 4),)*3,
        "pressure_removes_diagonal_at_this_order": coefficient(c, (1, 1, 1)) == (0, 0, 0),
        "energy_feedback_identity": vector_inner(u, c) + vector_inner(b, b) == 0,
        "highpass_split_identity": highpass_energy_defect(combined, 1) == 0,
    }
    return {
        "checks": checks,
        "first_support": [list(k) for k in sorted(support(b))],
        "third_order_support": [list(k) for k in sorted(support(c))],
        "first_mean_l2_squared": str(vector_inner(b, b)),
        "third_order_mean_l2_squared": str(vector_inner(c, c)),
        "third_order_note": "C=B(U,B(U,U))+B(B(U,U),U); time-integrated cubic term has its own heat factors.",
    }


def tree_coefficient(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return sp.Rational(n**(n-1), factorial(n))


def remainder_bound(mean_wiener, frequency, time):
    """A0 tail after homogeneous degrees 1 and 2, with x=M*N*t < 1/3."""
    M, N, t = map(sp.sympify, (mean_wiener, frequency, time))
    x = M*N*t
    if not (M > 0 and N > 0 and t >= 0 and 3*x < 1):
        raise ValueError("requires M,N>0, t>=0, and 3*M*N*t<1")
    return sp.cancel(sp.Rational(3, 2)*M*x*x/(1-3*x))


def far_tail_bound(mean_wiener, frequency, time, cutoff_frequency):
    """Bound sum_{|k|>H}|u_hat(k)| for initially supported |k|<=N."""
    M, N, t, H = map(sp.sympify, (mean_wiener, frequency, time, cutoff_frequency))
    r = 3*M*N*t
    if not (M > 0 and N > 0 and t >= 0 and H >= N and r < 1):
        raise ValueError("requires M,N>0, H>=N, t>=0, and 3*M*N*t<1")
    return sp.cancel(M*r**sp.floor(H/N)/(1-r))


def rational_majorant_checks():
    cs = [sp.Integer(0), sp.Integer(1)]
    for n in range(2, 25):
        cs.append(sp.Rational(n, 2*(n-1))*sum(cs[a]*cs[n-a] for a in range(1, n)))
    eps, tau = EPSILON, TAU_STAR
    m = 3 + eps
    perturbation = 6*eps + eps**2
    tail_per_A_tau = sp.cancel(remainder_bound(m, 1, tau)/tau)
    # Re=A/(nu*N)>=1 gives exp(-2*tau/Re)>=1-2*tau.
    lower = sp.cancel((1-2*tau)/4 - perturbation - tail_per_A_tau)
    r = sp.symbols("r")
    d3_series = sp.Integer(1)/(1-r)
    for _ in range(3):
        d3_series = r*sp.diff(d3_series, r) + 3*d3_series
    d3_closed = (27-44*r+31*r*r-8*r**3)/(1-r)**4
    checks = {
        "tree_recurrence_exact_through_24": all(cs[n] == tree_coefficient(n) for n in range(1, 25)),
        "ratio_below_three_through_24": all(cs[n+1] < 3*cs[n] for n in range(1, 24)),
        "convergence_margin_positive": bool(3*m*tau < 1),
        "robust_activation_lower_exceeds_one_eighth": bool(lower > sp.Rational(1, 8)),
        "activation_threshold_is_one_over_4096": tau/8 == sp.Rational(1, 4096),
        "strong_third_derivative_tail_series": sp.cancel(d3_series - d3_closed) == 0,
        "far_tail_at_local_endpoint": far_tail_bound(1, 1, sp.Rational(1, 6), 8) == sp.Rational(1, 128),
    }
    return {
        "checks": checks,
        "epsilon": str(eps), "tau_star": str(tau),
        "worst_normalized_wiener_size": str(m),
        "lower_coefficient_divided_by_A_tau": str(lower),
        "margin_over_one_eighth": str(lower-sp.Rational(1, 8)),
        "activation_amplitude_divided_by_A": "1/4096",
        "majorant_ratio_at_endpoint": str(3*m*tau),
        "tree_coefficients_1_to_8": [str(c) for c in cs[1:9]],
        "universal_proof_location": "references/navier-stokes/frequency-activation.md#2-the-all-mode-interval-estimate",
    }


def build_receipt():
    algebra, bounds = exact_interactions(), rational_majorant_checks()
    checks = {**{f"fourier.{k}": v for k, v in algebra["checks"].items()},
              **{f"majorant.{k}": v for k, v in bounds["checks"].items()}}
    return {
        "stamp": "2026-09-08", "node": "nse-frequency-activation-local",
        "evidence_class": "WRITTEN_RESTRICTED_LOCAL_PDE_PROOF_WITH_EXACT_FOURIER_AND_RATIONAL_PINS",
        "root_status": "OPEN", "E_prime_status": "OPEN",
        "retired_gso_route_status": "DEAD", "dns_run": False,
        "exact_interactions": algebra, "rational_majorant": bounds,
        "checks": checks, "all_green": all(checks.values()),
        "claim_boundary": "Classical convergent all-mode expansion gives a short-time activation theorem for a finite-band 3D seed and small finite-band perturbations; no infinite cascade, global regularity, blow-up, or novelty claim.",
        "next_obligation": "Analyze spatially concentrated packets with growing Fourier support; control phase, all interactions, and inter-step errors. Sparse mode generation does not implement an energy-supercritical shell amplifier.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args(argv)
    receipt = build_receipt()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"{args.out}: {sum(receipt['checks'].values())}/{len(receipt['checks'])} exact checks; ROOT OPEN")
    return 0 if receipt["all_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
