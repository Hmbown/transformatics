"""Periodic strain-transfer identities and the conditional pumping estimate.

See references/navier-stokes/qgso-transfer-budget.md for proofs and attribution.
The strain/Laplacian-vorticity orthogonality is Miller's identity, not a new
discovery here. Exact finite Fourier algebra checks the periodic adaptation
and the derived estimate against the velocity-form NS right-hand side.

No trajectory is run. Scalar ledgers are not NS solutions. Frozen endpoint
measurements cannot recover the separate transfer and diffusion integrals.
ROOT, (E'), and Q-GSO averaged noncollapse remain OPEN.
"""

from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_qgso_transfer_budget.json"
FROZEN = ROOT / "artifacts/enstrophy_sup/nse_qgso_floor_slack_probe.json"
ZERO = (0, 0, 0)
TEST_NU = sp.Rational(1, 100)


def add(*polys):
    out = {}
    for p in polys:
        for k, value in p.items():
            out[k] = out.get(k, 0) + value
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def scale(p, a):
    return {k: sp.expand(a*v) for k, v in p.items() if sp.expand(a*v) != 0}


def multiply(p, q):
    out = {}
    for k, a in p.items():
        for m, b in q.items():
            n = tuple(ki+mi for ki, mi in zip(k, m))
            out[n] = out.get(n, 0) + a*b
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def derivative(p, axis):
    return {k: sp.expand(sp.I*k[axis]*a) for k, a in p.items() if k[axis]}


def minus_laplacian(p):
    return {k: sum(ki*ki for ki in k)*a for k, a in p.items() if k != ZERO}


def inner(p, q):
    """Real bilinear mean, (2pi)^-3 integral p q, for real Fourier fields."""
    return sp.expand(sum(a*q.get(tuple(-ki for ki in k), 0)
                         for k, a in p.items()))


def tensor_inner(A, B):
    return sp.expand(sum(inner(A[i][j], B[i][j])
                         for i in range(3) for j in range(3)))


def strain(u):
    return [[scale(add(derivative(u[j], i), derivative(u[i], j)), sp.Rational(1, 2))
             for j in range(3)] for i in range(3)]


def vector_project(v):
    """Exact Fourier Leray projection; retains a vector's zero mode."""
    ks = set().union(*(p.keys() for p in v))
    out = [{} for _ in range(3)]
    for k in ks:
        k2 = sum(ki*ki for ki in k)
        dot = sum(k[i]*v[i].get(k, 0) for i in range(3))
        for i in range(3):
            out[i][k] = sp.expand(v[i].get(k, 0) - k[i]*dot/k2) if k2 else v[i].get(k, 0)
    return [add(p) for p in out]


def strain_project(A):
    """Orthogonal projection onto periodic compatible strains; zero mean."""
    ks = set().union(*(p.keys() for row in A for p in row))
    out = [[{} for _ in range(3)] for _ in range(3)]
    for k in ks:
        k2 = sum(ki*ki for ki in k)
        if not k2:
            continue
        Ak = sp.Matrix([[A[i][j].get(k, 0) for j in range(3)] for i in range(3)])
        kv = sp.Matrix(k)
        w = (sp.eye(3)-kv*kv.T/k2)*Ak*kv
        projected = (kv*w.T+w*kv.T)/k2
        for i in range(3):
            for j in range(3):
                out[i][j][k] = sp.expand(projected[i, j])
    return [[add(p) for p in row] for row in out]


def triad_velocity(amplitude=1):
    """Pinned real mean-zero solenoidal polynomial; all coefficients exact.

    u = a [(0,1,1) cos x + (1,1,-1) cos(y+z)
            + (1,-2,1) sin(x+y+z)].
    These three modes are an identity test, not a singularity candidate.
    """
    a = sp.sympify(amplitude)
    out = [{} for _ in range(3)]
    for k, v, phase in [((1, 0, 0), (0, 1, 1), "cos"),
                        ((0, 1, 1), (1, 1, -1), "cos"),
                        ((1, 1, 1), (1, -2, 1), "sin")]:
        assert sum(ki*vi for ki, vi in zip(k, v)) == 0
        for i in range(3):
            coefficient = a*v[i]/2 if phase == "cos" else a*v[i]/(2*sp.I)
            out[i][k] = coefficient
            out[i][tuple(-ki for ki in k)] = sp.conjugate(coefficient)
    return [add(p) for p in out]


@lru_cache(maxsize=8)
def fourier_identity_checks(amplitude=1, nu=TEST_NU) -> dict:
    """Compare exact continuum integrals through independent equations."""
    u = triad_velocity(amplitude)
    S = strain(u)
    L = [[minus_laplacian(p) for p in row] for row in S]
    grad = [[derivative(u[i], j) for j in range(3)] for i in range(3)]
    omega = [add(grad[2][1], scale(grad[1][2], -1)),
             add(grad[0][2], scale(grad[2][0], -1)),
             add(grad[1][0], scale(grad[0][1], -1))]
    ww = [[multiply(omega[i], omega[j]) for j in range(3)] for i in range(3)]
    S2 = [[add(*(multiply(S[i][k], S[k][j]) for k in range(3)))
           for j in range(3)] for i in range(3)]
    advS = [[add(*(multiply(u[k], derivative(S[i][j], k)) for k in range(3)))
             for j in range(3)] for i in range(3)]
    C = strain_project([[add(advS[i][j], S2[i][j], scale(ww[i][j], sp.Rational(3, 4)))
                         for j in range(3)] for i in range(3)])
    # Independently differentiate the velocity-form projected NS RHS.
    advu = [add(*(multiply(u[k], derivative(u[i], k)) for k in range(3)))
            for i in range(3)]
    projected_adv = vector_project(advu)
    up = [add(scale(projected_adv[i], -1), scale(minus_laplacian(u[i]), -nu))
          for i in range(3)]
    Sp = strain(up)
    Q, D, Z = tensor_inner(S, S), tensor_inner(S, L), tensor_inner(L, L)
    Qp, Dp = 2*tensor_inner(S, Sp), 2*tensor_inner(L, Sp)
    P = tensor_inner(S, ww)
    C2 = tensor_inner(C, C)
    # Physical gradient-contraction form of the same D production.
    dS = [[[derivative(S[i][j], k) for j in range(3)] for i in range(3)]
          for k in range(3)]
    A = sum(inner(S[k][m], add(*(multiply(dS[k][i][j], dS[m][i][j])
                                for i in range(3) for j in range(3))))
            for k in range(3) for m in range(3))
    B = sum(inner(S[i][j], multiply(dS[k][j][m], dS[k][m][i]))
            for i in range(3) for j in range(3) for k in range(3) for m in range(3))
    # The velocity pressure is reconstructed separately from tr((grad u)^2).
    f = add(*(multiply(grad[i][j], grad[j][i]) for i in range(3) for j in range(3)))
    p = {k: value/sum(ki*ki for ki in k) for k, value in f.items() if k != ZERO}
    H = [[derivative(derivative(p, i), j) for j in range(3)] for i in range(3)]
    delta2 = sp.cancel(1-D*D/(Q*Z))
    square_field = [[add(L[i][j], scale(S[i][j], -D/Q), scale(C[i][j], 1/(2*nu)))
                     for j in range(3)] for i in range(3)]
    checks = {
        "raw_divergence_zero": add(*(derivative(u[i], i) for i in range(3))) == {},
        "laplacian_vorticity_orthogonality": tensor_inner(L, ww) == 0,
        "strain_transfer_orthogonality": tensor_inner(S, C) == 0,
        "laplacian_pressure_orthogonality": tensor_inner(L, H) == 0,
        "betchov": sp.expand(P+sp.Rational(4, 3)*tensor_inner(S, S2)) == 0,
        "q_budget_vs_velocity_rhs": sp.expand(Qp-P+2*nu*D) == 0,
        "d_budget_vs_velocity_rhs": sp.expand(Dp+2*nu*Z+2*tensor_inner(L, C)) == 0,
        "d_budget_gradient_contractions": sp.expand(Dp+2*nu*Z+2*A+4*B) == 0,
        "compatible_strain_projection": strain_project(S) == S,
        "spectral_variance_positive": bool(0 < delta2 < 1),
        "signed_projection_bound": bool(tensor_inner(L, C)**2 <= (Z-D*D/Q)*C2),
        "pumping_bound": bool(2*nu*Dp+4*nu**2*D*D/Q <= C2),
        "completed_square_identity": sp.expand(Dp+2*nu*D*D/Q
                                                +2*nu*tensor_inner(square_field, square_field)
                                                -C2/(2*nu)) == 0,
    }
    moments = {"Q": Q, "D": D, "Z": Z, "P": P, "Qprime": Qp,
               "Dprime": Dp, "C_norm_squared": C2, "A": A, "B": B,
               "delta_squared": delta2, "transfer_ratio": sp.cancel(C2*Q/(4*nu**2*D*D))}
    return {"amplitude": str(amplitude), "nu": str(nu), "checks": checks,
            "moments_divided_by_volume": {k: str(v) for k, v in moments.items()},
            "scope": "Exact periodic polynomial and NS tangent; no completed rung or blow-up claim."}


def scalar_budget_checks() -> dict:
    """Test the derived scalar estimate before any new DNS is contemplated."""
    s, r, L = sp.symbols("s r L", positive=True)
    nu = sp.Integer(1)
    Q, D, Z, M, E = s**(-sp.Rational(1, 2)), s**(-sp.Rational(3, 2)), 2*s**(-sp.Rational(5, 2)), 8/s, 4*sp.sqrt(s)
    Qp, Dp = -sp.diff(Q, s), -sp.diff(D, s)
    prod = Qp+2*nu*D
    # Minimal norm of an abstract C orthogonal to S and with the prescribed
    # < -Delta S,C >.  This assigns scalar data, not the actual NS tensor C.
    C2 = sp.simplify((Dp+2*nu*Z)**2/(4*(Z-D*D/Q)))
    ratio = sp.simplify(C2*Q/(4*nu**2*D*D))
    # Slow escape retains the previous ledger, with L >= 32 for the
    # additional dissipation and kinetic-energy inequalities imposed here.
    x = r+L
    Qs, Ms, Es = sp.exp(r), sp.exp(r)*x*x, 4/x
    Ds = sp.exp(2*r)*x/2
    Zs = 2*Ds*Ds/Qs
    drdt = Ms/2
    Qsp, Dsp = sp.diff(Qs, r)*drdt, sp.diff(Ds, r)*drdt
    C2s = sp.simplify((Dsp+2*nu*Zs)**2/(4*(Zs-Ds*Ds/Qs)))
    rate = sp.simplify(C2/(2*nu*D)-2*nu*D/Q)
    slow_clock_density = sp.simplify((C2s/(2*nu*Ds)-2*nu*Ds/Qs)/drdt)
    # At s=1 these abstract vectors realize the assigned Gram matrix and
    # both scalar evolution pairings. They are not Fourier fields.
    Svec, Avec = sp.Matrix([1, 0]), sp.Matrix([1, 1])
    Wvec, Cvec = sp.Matrix([sp.Rational(5, 2), -sp.Rational(5, 2)]), sp.Matrix([0, -sp.Rational(11, 4)])
    tangent = -Avec+Wvec/2-Cvec
    checks = {
        "blob_energy_identity": sp.simplify(-sp.diff(E, s)+2*nu*Q) == 0,
        "blob_energy_interpolation": sp.simplify(E*D/Q**2) == 4,
        "blob_spectral_variance_half": sp.simplify(1-D*D/(Q*Z)) == sp.Rational(1, 2),
        "blob_betchov_cap": bool((sp.Rational(5, 16))**2 < sp.Rational(8, 27)),
        "blob_rate_below_riccati": sp.simplify(-sp.diff(M, s)/M**2) == sp.Rational(1, 8),
        "blob_pumping_inequality": sp.simplify((C2-2*nu*Dp-4*nu**2*D*D/Q)*s**sp.Rational(5, 2)) == sp.Rational(9, 16),
        "blob_transfer_ratio_exceeds_one": ratio == sp.Rational(121, 64),
        "blob_signed_upper_clock_density": rate == 57/(32*s),
        "abstract_orthogonal_pairings": Avec.dot(Wvec) == 0 and Svec.dot(Cvec) == 0,
        "abstract_q_evolution_pairing": 2*Svec.dot(tangent) == sp.Rational(1, 2),
        "abstract_d_evolution_pairing": 2*Avec.dot(tangent) == sp.Rational(3, 2),
        "slow_energy_identity": sp.simplify(sp.diff(Es, r)*drdt+2*nu*Qs) == 0,
        "slow_energy_interpolation": sp.simplify(Es*Ds/Qs**2) == 2,
        "slow_betchov_production_ratio": sp.simplify((Qsp+2*nu*Ds)/(Ms*Qs)-sp.Rational(1, 2)-1/x) == 0,
        "slow_betchov_cap_L32": bool((sp.Rational(1, 2)+sp.Rational(1, 32))**2 < sp.Rational(8, 27)),
        "slow_transfer_ratio": sp.simplify(C2s*Qs/(4*nu**2*Ds*Ds)-(x+sp.Rational(5, 2))**2/4) == 0,
        "slow_pumping_inequality": sp.simplify((C2s-2*nu*Dsp-4*nu**2*Ds*Ds/Qs)/(nu**2*Ds*Ds/Qs)-(x+sp.Rational(1, 2))**2) == 0,
        "slow_signed_upper_clock_density": sp.simplify(slow_clock_density-x/2-sp.Rational(5, 2)-sp.Rational(9, 8)/x) == 0,
    }
    return {"checks": checks, "blob": {"Q": str(Q), "M": str(M), "E": str(E),
            "D": str(D), "Z": str(Z), "production": str(prod),
            "C_norm_squared_assigned": str(C2), "transfer_ratio": str(ratio),
            "upper_clock_per_Q_rung": "(57/16) log(rho)",
            "price_on_Q_rung": "sqrt(s_start) (1-rho^-1)/(8 log(rho))"},
            "slow": {"L_min": 32, "D": str(Ds), "Z": str(Zs),
            "E": str(Es), "transfer_ratio": "(r+L+5/2)^2/4",
            "price": "1/((L+j log(rho))(L+(j+1) log(rho)))"},
            "verdict": "Both scalar escape ledgers survive the pumping estimate.",
            "energy_note": "A nonnegative constant may be added to E. The blob also obeys mean-zero torus Poincare moment inequalities for 0 < s <= 1/4.",
            "scope": "Scalar and Hilbert-space-compatible norm assignments only; no spatial tensor or NS solution is asserted."}


def frozen_endpoint_rows() -> dict:
    data = json.loads(FROZEN.read_text())
    results = []
    for result in data["results"]:
        samples = result["rows"]
        t = np.array([r["t"] for r in samples])
        q = np.array([r["Q"] for r in samples])
        d = np.array([r["D"] for r in samples])
        if not (np.all(np.diff(t) > 0) and np.all(q > 0) and np.all(d > 0)):
            raise ValueError("strict sample times and positive Q,D required")
        rows = []
        for r in result["rung_ledger"]:
            a, b = r["a"], r["b"]
            if not t[0] <= a < b <= t[-1]:
                raise ValueError("rung endpoints must lie inside the sampled interval")
            qa, qb = np.interp([a, b], t, q)
            da, db = np.interp([a, b], t, d)
            if qb <= qa:
                raise ValueError("completed Q growth rung required")
            rows.append({"rung_index": r["rung_index"], "a": a, "b": b,
                         "q_ratio": float(qb/qa), "d_ratio": float(db/da),
                         "net_log_D_growth": float(np.log(db/da)),
                         "alpha_D": float(np.log(db/da)/np.log(qb/qa)),
                         "separate_transfer_and_diffusion_integrals": None,
                         "spectral_variance": None})
        results.append({"family": result["family"], "nu": result["nu"],
                        "N": result["N"], "rows": rows})
    return {"source": str(FROZEN.relative_to(ROOT)),
            "sha256": hashlib.sha256(FROZEN.read_bytes()).hexdigest(),
            "method": "Linear interpolation at the already frozen rung endpoints; no derivatives estimated.",
            "scope": "Finite post-hoc endpoint measurements only. Z and the transfer tensor were not saved; no new acceptance-grade claim or asymptotic verdict.",
            "results": results}


def build_receipt() -> dict:
    exact = [fourier_identity_checks(a) for a in (1, -1)]
    scalar = scalar_budget_checks()
    checks = [v for row in exact for v in row["checks"].values()]
    checks += list(scalar["checks"].values())
    return {"stamp": "2026-09-04", "node": "nse-qgso-transfer-budget",
            "evidence_class": "PROVED_IDENTITIES_AND_CONDITIONAL_ESTIMATE_WITH_SCALAR_OBSTRUCTION",
            "literature": "Evan Miller, arXiv:2407.02691v2, Theorem 3.1; https://arxiv.org/html/2407.02691v2",
            "exact_fourier_checks": exact, "scalar_obstructions": scalar,
            "frozen_endpoint_measurements": frozen_endpoint_rows(),
            "all_green": all(checks), "check_count": len(checks),
            "root_status": "OPEN", "E_prime_status": "OPEN",
            "averaged_noncollapse_status": "OPEN",
            "claim_boundary": "The signed transfer integral remains uncontrolled. Neither this estimate, a finite field check, nor a scalar ledger proves regularity or blow-up."}


if __name__ == "__main__":
    receipt = build_receipt()
    OUT.write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps({"all_green": receipt["all_green"], "checks": receipt["check_count"],
                      "out": str(OUT), "root_status": receipt["root_status"]}))
    if not receipt["all_green"]:
        raise SystemExit(1)
