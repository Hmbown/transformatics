"""Algebra pins for a classical logarithmic NS background comparison.

The PDE proof and imported compact Euler existence theorem are documented
in references/navier-stokes/steady-background.md. These symbolic checks do not
construct a Gavrilov profile, compute a Floquet map, or solve NS numerically.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_steady_background.json"


def polarization_rhs(A, xi, b):
    """Pressure-corrected inviscid short-wave amplitude equation."""
    if xi.dot(xi) == 0:
        raise ValueError("a nonzero real covector is required")
    return -A*b + 2*xi*(xi.dot(A*b))/xi.dot(xi)


def comparison_envelope(epsilon, F, kappa, tau):
    """The bootstrap envelope; its PDE use also requires z<=r."""
    epsilon, F, kappa, tau = map(sp.sympify, (epsilon, F, kappa, tau))
    if not (epsilon > 0 and F > 0 and kappa > 0 and tau >= 0):
        raise ValueError("requires epsilon,F,kappa>0 and tau>=0")
    return epsilon*F*(sp.exp(kappa*tau)-1)/kappa


@lru_cache(maxsize=1)
def scaling_checks():
    L, a, nu = sp.symbols("L a nu", positive=True)
    amplitude = a*L**sp.Rational(3, 2)
    eps = nu*L/amplitude
    scale_a = L**sp.Rational(-1, 10)
    H = L**sp.Rational(11, 10)
    checks = {
        "physical_mean_L2_normalization": sp.simplify(amplitude**2/L**3-a**2) == 0,
        "rescaled_viscosity": sp.simplify(eps-nu/(a*sp.sqrt(L))) == 0,
        "nonlinear_rescaling_factor": sp.simplify(amplitude**2*L/(amplitude*(amplitude*L))) == 1,
        "turnover_power": sp.simplify((amplitude*L).subs(a, scale_a)-L**sp.Rational(12, 5)) == 0,
        "small_viscosity_power": sp.simplify(eps.subs(a, scale_a)-nu*L**sp.Rational(-2, 5)) == 0,
        "inviscid_covector_damping_power": sp.simplify(eps.subs(a, scale_a)*(H/L)**2-nu*L**sp.Rational(-1, 5)) == 0,
    }
    return {"checks": checks, "scope": "Exact rescaling and feasibility exponents; no amplitude or iteration theorem."}


@lru_cache(maxsize=1)
def bootstrap_checks():
    eps, F, kappa, r, t = sp.symbols("eps F kappa r t", positive=True)
    bound = eps*F*(sp.exp(kappa*t)-1)/kappa
    T = sp.log(1+kappa*r/(2*eps*F))/kappa
    return {
        "checks": {
            "comparison_initial_zero": bound.subs(t, 0) == 0,
            "comparison_differential_equation": sp.simplify(sp.diff(bound, t)-kappa*bound-eps*F) == 0,
            "strict_bootstrap_endpoint": sp.simplify(bound.subs(t, T)-r/2) == 0,
            "comparison_increasing": sp.simplify(sp.diff(bound, t)).is_positive is True,
        },
        "bound": str(bound), "bootstrap_time": str(T),
        "scope": "The uniform Hs energy inequality and strong continuation are proved in the note, not certified by this scalar check.",
    }


@lru_cache(maxsize=1)
def ode_checks():
    q, v = sp.symbols("q v", positive=True)
    a, c, d, e, f = sp.symbols("a c d e f", real=True)
    # A b=-xi, xi.b=0: general remaining entries in this adapted frame.
    A = sp.Matrix([[a, -q/v, c], [d, 0, e], [f, 0, -a]])
    xi, b = sp.Matrix([q, 0, 0]), sp.Matrix([0, v, 0])
    normal_rhs = polarization_rhs(A, xi, b)

    entries = sp.symbols("a0:8", real=True)
    G = sp.Matrix([[entries[0], entries[1], entries[2]],
                   [entries[3], entries[4], entries[5]],
                   [entries[6], entries[7], -entries[0]-entries[4]]])
    x = sp.Matrix(sp.symbols("x0:3", real=True))
    y = sp.Matrix(sp.symbols("b0:3", real=True))
    xp = -G.T*x
    yp = polarization_rhs(G, x, y)
    constraint_rate = sp.simplify(xp.dot(y)+x.dot(yp))
    P = sp.eye(3)-x*x.T/x.dot(x)
    C = -G+2*x*x.T*G/x.dot(x)
    trace = sp.factor(sp.trace(P*C*P))

    T, w1, w2 = sp.symbols("T w1 w2", real=True)
    flow_derivative = sp.Matrix([[1, 0, T*w1], [0, 1, T*w2], [0, 0, 1]])
    covector = sp.Matrix(sp.symbols("z1 z2 zI", real=True))
    expected = sp.Matrix([covector[0], covector[1],
                          covector[2]-T*(w1*covector[0]+w2*covector[1])])
    return {
        "checks": {
            "pressure_normal_admissible": xi.dot(b) == 0 and A.trace() == 0,
            "steady_acceleration_is_pressure": A*b == -xi,
            "velocity_is_polarization_solution": normal_rhs == A*b,
            "polarization_constraint_preserved": constraint_rate == 0,
            "plane_trace_is_log_covector_loss": sp.simplify(trace+xp.dot(x)/x.dot(x)) == 0,
            "cotangent_return_formula": sp.simplify(flow_derivative.inv().T*covector-expected) == sp.zeros(3, 1),
        },
        "pressure_normal_rhs": str(normal_rhs),
        "plane_trace": str(trace),
        "return_condition": "Omega'(I).zeta_theta=0 for a closed orbit of positive period",
        "scope": "ODE identities only. Unit multipliers for the pressure-normal periodic carrier follow from the written determinant argument. No oblique Floquet spectrum computed.",
    }


def build_receipt():
    sections = {"scaling": scaling_checks(), "bootstrap": bootstrap_checks(), "ode": ode_checks()}
    checks = {f"{name}.{k}": v for name, part in sections.items() for k, v in part["checks"].items()}
    return {
        "stamp": "2026-09-08", "node": "nse-steady-background-local",
        "root_status": "OPEN", "E_prime_status": "OPEN", "gso_route_status": "DEAD",
        "evidence_class": "WRITTEN_CLASSICAL_PDE_COMPARISON_AND_RESTRICTED_ODE_PROOF_WITH_SYMBOLIC_PINS",
        "dns_run": False, "compact_profile_computed": False, "oblique_Floquet_map_computed": False,
        **sections, "checks": checks, "all_green": all(checks.values()),
        "sources": ["https://arxiv.org/html/1810.08020v1", "https://arxiv.org/html/1903.11699v1", "https://arxiv.org/html/2302.02982v1"],
        "claim_boundary": "Fixed-profile NS backgrounds persist for logarithmically many rescaled turnovers; the pressure-normal periodic inviscid carrier has unit multipliers. No high-seed amplification, finite-wavelength validation, novel theorem, infinite cascade, or ROOT closure.",
        "remaining_estimate": "Analyze returning oblique covectors on one specified compact steady Euler orbit before a viscous localized-wave amplification attempt.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args(argv)
    result = build_receipt()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(f"{args.out}: {sum(result['checks'].values())}/{len(result['checks'])} exact checks; ROOT OPEN")
    return 0 if result["all_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
