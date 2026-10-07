"""Exact algebra controls for the written log-log NS packet handover result.

This instrument certifies symbolic identities and power arithmetic only.
The separate written proof has passed independent analytic review. This
instrument does not certify the mean PDE estimates, all-mode residual
estimate, strong continuation, the handover theorem, or ROOT.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_loglog_handover.json"


def gradient(f, coordinates):
    return sp.Matrix([sp.diff(f, x) for x in coordinates])


def curl(v, coordinates):
    x, y, z = coordinates
    return sp.Matrix([
        sp.diff(v[2], y)-sp.diff(v[1], z),
        sp.diff(v[0], z)-sp.diff(v[2], x),
        sp.diff(v[1], x)-sp.diff(v[0], y),
    ])


def divergence(v, coordinates):
    return sum(sp.diff(v[i], x) for i, x in enumerate(coordinates))


def clean(expr):
    if isinstance(expr, sp.MatrixBase):
        return expr.applyfunc(lambda v: sp.factor(sp.cancel(sp.expand(v))))
    return sp.factor(sp.cancel(sp.expand(expr)))


def quadratic_coefficients(b, d, jac_b, jac_d, h):
    """Q0,Qcos,Qsin for Re[(b+i h d)exp(i phi)], with xi.d=div b."""
    g = jac_b.trace()
    bb, dd = jac_b*b, jac_d*d
    return (
        (bb+g*b+h*h*dd)/2,
        (bb-g*b-h*h*dd)/2,
        -h*(jac_b*d+jac_d*b-g*d)/2,
    )


def curl_lift_amplitude(g, xi, coordinates, h, n):
    """Amplitude of the exact curl lift for exp(i n phi), n nonzero."""
    if n == 0:
        raise ValueError("the zero harmonic requires its own solenoidal PDE")
    potential = clean(xi.cross(g)/xi.dot(xi))
    return clean(g+sp.I*h*curl(potential, coordinates)/n)


def pressure_amplitude(g, forcing, A, xi, h, n, *, normal_forcing=True):
    if n == 0:
        raise ValueError("nonzero harmonic required")
    p = 2*xi.dot(A*g)/xi.dot(xi)
    if normal_forcing:
        p += xi.dot(forcing)/xi.dot(xi)
    return clean(sp.I*h*p/n)


def direct_operator_amplitude(U, pressure, V, phase, coordinates, time, h, n):
    """Direct differentiation after removing the common exponential."""
    xi = gradient(phase, coordinates)
    A = V.jacobian(coordinates)
    transport_phase = sp.diff(phase, time)+xi.dot(V)
    return clean(
        U.diff(time)+U.jacobian(coordinates)*V+A*U
        +sp.I*n*transport_phase*U/h
        +gradient(pressure, coordinates)+sp.I*n*xi*pressure/h
    )


def forced_remainder(g, forcing, V, xi, coordinates, time, h, n):
    A = V.jacobian(coordinates)
    c = sp.I*curl(clean(xi.cross(g)/xi.dot(xi)), coordinates)
    scalar = clean((2*xi.dot(A*g)+xi.dot(forcing))/xi.dot(xi))
    return clean(h*(c.diff(time)+c.jacobian(coordinates)*V+A*c
                    +sp.I*gradient(scalar, coordinates))/n)


@lru_cache(maxsize=1)
def quadratic_checks():
    # At a point rotate a nonzero xi to the third axis. All first jets
    # remain arbitrary subject to the exact divergence constraints.
    q, h, phase = sp.symbols("q h E", nonzero=True)
    b1, b2, d1, d2 = sp.symbols("b1 b2 d1 d2")
    J = sp.Matrix(3, 3, sp.symbols("J0:9"))
    K = sp.Matrix(3, 3, sp.symbols("K0:9"))
    K[2, 2] = -K[0, 0]-K[1, 1]
    xi = sp.Matrix([0, 0, q])
    b = sp.Matrix([b1, b2, 0])
    d = sp.Matrix([d1, d2, J.trace()/q])
    cosine, sine = (phase+1/phase)/2, (phase-1/phase)/(2*sp.I)
    W = b*cosine-h*d*sine
    direct_jacobian = (J*cosine-h*K*sine
                       -b*xi.T*sine/h-d*xi.T*cosine)
    zero, second_cos, second_sin = quadratic_coefficients(b, d, J, K, h)
    residual = clean(direct_jacobian*W-zero
                     -second_cos*(cosine*cosine-sine*sine)
                     -second_sin*2*sine*cosine)

    # A genuine curved phase/curl field additionally checks that the jet
    # constraints arise from differentiation, not just asserted symbols.
    x, y, z = sp.symbols("x y z", real=True)
    X = (x, y, z)
    S = z+x*y
    k = gradient(S, X)
    curved_b = k.dot(k)*k.cross(sp.Matrix([0, 1, 1]))
    curved_d = curl(clean(k.cross(curved_b)/k.dot(k)), X)
    Jb, Jd = curved_b.jacobian(X), curved_d.jacobian(X)
    C, D = (phase+1/phase)/2, (phase-1/phase)/(2*sp.I)
    packet = curved_b*C-h*curved_d*D
    # Chain rule dE/dx=(i/h)xi E; this differentiates the actual field.
    raw_jac = sp.Matrix.hstack(*[
        packet.diff(var)+sp.I*k[i]*phase*packet.diff(phase)/h
        for i, var in enumerate(X)
    ])
    q0, qc, qs = quadratic_coefficients(curved_b, curved_d, Jb, Jd, h)
    curved_residual = clean(raw_jac*packet-q0-qc*(C*C-D*D)-qs*2*C*D)
    stress_div = Jb*curved_b+divergence(curved_b, X)*curved_b
    stress_div += h*h*(Jd*curved_d+divergence(curved_d, X)*curved_d)
    return {
        "checks": {
            "arbitrary_rotated_first_jets": residual == sp.zeros(3, 1),
            "curved_gradient_nonconstant": k.jacobian(X) != sp.zeros(3),
            "curved_tangency": clean(k.dot(curved_b)) == 0,
            "curl_normal_identity": clean(k.dot(curved_d)-divergence(curved_b, X)) == 0,
            "curl_divergence_zero": divergence(curved_d, X) == 0,
            "curved_packet_divergence": clean(raw_jac.trace()) == 0,
            "curved_direct_quadratic_identity": curved_residual == sp.zeros(3, 1),
            "mean_is_half_stress_divergence": clean(2*q0-stress_div) == sp.zeros(3, 1),
            "omitted_mean_leaves_nonzero_force": clean(q0) != sp.zeros(3, 1),
            "second_harmonic_nontrivial": clean(qc) != sp.zeros(3, 1) or clean(qs) != sp.zeros(3, 1),
        },
        "scope": "Pointwise first-jet identity is rotation-covariant. The explicit curved-gradient curl fixture is an independent differential realization; neither is a PDE trajectory.",
    }


@lru_cache(maxsize=1)
def moving_curved_fixture():
    x, y, z, t = sp.symbols("x y z t", real=True)
    X = (x, y, z)
    V = sp.Matrix([y, 0, 0])
    S = z+(x-t*y)*y
    xi = gradient(S, X)
    g = clean(xi.dot(xi)*xi.cross(sp.Matrix([1, 0, 1+t])))
    A = V.jacobian(X)
    Gg = clean(-A*g+2*xi*xi.dot(A*g)/xi.dot(xi))
    Dg = g.diff(t)+g.jacobian(X)*V
    forcing = clean(Gg-Dg+(1+x+z)*xi)
    return X, t, V, S, xi, g, forcing


@lru_cache(maxsize=2)
def forced_harmonic_checks(n):
    X, t, V, S, xi, g, forcing = moving_curved_fixture()
    h = sp.symbols("h", positive=True)
    A = V.jacobian(X)
    U = curl_lift_amplitude(g, xi, X, h, n)
    p = pressure_amplitude(g, forcing, A, xi, h, n)
    raw = direct_operator_amplitude(U, p, V, S, X, t, h, n)
    remainder = forced_remainder(g, forcing, V, xi, X, t, h, n)
    bad_p = pressure_amplitude(g, forcing, A, xi, h, n, normal_forcing=False)
    missing_normal = clean(direct_operator_amplitude(U, bad_p, V, S, X, t, h, n)
                           +forcing-remainder)
    missing_all = clean(direct_operator_amplitude(U, 0, V, S, X, t, h, n)
                        +forcing-remainder)
    transverse = clean(forcing-xi*xi.dot(forcing)/xi.dot(xi))
    div_lift = divergence(U, X)+sp.I*n*xi.dot(U)/h
    at = {t: 0, X[0]: 1, X[1]: 2, X[2]: 0}
    normal_leading = clean(missing_normal.subs(h, 0).subs(at))
    all_leading = clean(missing_all.subs(h, 0).subs(at))
    return {
        "checks": {
            "nontrivial_incompressible_velocity": divergence(V, X) == 0 and A != sp.zeros(3),
            "transported_curved_phase": clean(sp.diff(S, t)+xi.dot(V)) == 0 and xi.jacobian(X) != sp.zeros(3),
            "exact_cotangent_transport": clean(xi.diff(t)+xi.jacobian(X)*V+A.T*xi) == sp.zeros(3, 1),
            "tangent_amplitude": clean(xi.dot(g)) == 0,
            "nonzero_transverse_forcing": transverse != sp.zeros(3, 1),
            "nonzero_normal_forcing": clean(xi.dot(forcing)) != 0,
            "exact_solenoidal_lift": clean(div_lift) == 0,
            "direct_forced_pressure_lift_identity": clean(raw+forcing-remainder) == sp.zeros(3, 1),
            "dropping_normal_pressure_fails_at_leading_order": normal_leading != sp.zeros(3, 1),
            "dropping_all_pressure_fails_at_leading_order": all_leading != sp.zeros(3, 1),
            "remainder_has_one_h_factor": clean(remainder.subs(h, 0)) == sp.zeros(3, 1),
        },
        "harmonic": n,
        "missing_normal_pressure_leading_at_rational_point": str(normal_leading),
        "missing_all_pressure_leading_at_rational_point": str(all_leading),
    }


@lru_cache(maxsize=1)
def mean_feedback_checks():
    X, t, _, _, xi, b, _ = moving_curved_fixture()
    x, y, z = X
    h = sp.symbols("h", positive=True)
    m = sp.Matrix([y, z, x])
    d = curl(clean(xi.cross(b)/xi.dot(xi)), X)
    U = b+sp.I*h*d
    raw = U.jacobian(X)*m+sp.I*xi.dot(m)*U/h+m.jacobian(X)*U
    leading = sp.I*xi.dot(m)*b/h
    slow = b.jacobian(X)*m+m.jacobian(X)*b-xi.dot(m)*d
    slow += sp.I*h*(d.jacobian(X)*m+m.jacobian(X)*d)
    missing = clean(h*(raw-slow))
    return {
        "checks": {
            "mean_field_solenoidal": divergence(m, X) == 0,
            "normal_mean_nonzero": clean(xi.dot(m)) != 0,
            "exact_mean_primary_split": clean(raw-leading-slow) == sp.zeros(3, 1),
            "leading_mean_force_tangent": clean(xi.dot(leading)) == 0,
            "omitting_mean_phase_feedback_fails": missing != sp.zeros(3, 1),
            "omission_contains_inverse_h": clean(missing.subs(h, 0)) != sp.zeros(3, 1),
        },
        "scope": "This is the cross-advection identity, not a bound for the nonlocal mean PDE.",
    }


def gradient_error_exponent(residual_power, sobolev_power, s):
    return sp.factor(residual_power*(1-sp.Rational(5, 2)/s)
                     +sobolev_power*sp.Rational(5, 2)/s)


@lru_cache(maxsize=1)
def scaling_checks():
    theta = sp.symbols("theta", positive=True)
    s = sp.symbols("s", positive=True)
    first = 2+theta/2
    second = 3-theta/2
    hs = 1+3*theta/2-s
    grad_first = gradient_error_exponent(first, hs, s)
    grad_second = gradient_error_exponent(second, hs, s)
    vel_second = sp.factor(second*(1-sp.Rational(3, 2)/s)+hs*sp.Rational(3, 2)/s)
    values = {"theta": sp.Rational(1, 2), "s": 12}
    pins = {theta: values["theta"], s: values["s"]}
    # x=sqrt(log(1/h)): this proves exp(C sqrt(log(1/h))) times
    # any fixed logarithmic power is subpolynomial, via its log ratio.
    x, alpha, C, J = sp.symbols("x alpha C J", positive=True)
    log_ratio = sp.limit((-alpha*x*x+C*x+J*sp.log(x))/x**2, x, sp.oo)
    ell, mu, tau = sp.symbols("ell mu tau", positive=True)
    integrated = sp.integrate(sp.exp(mu*tau)/ell, (tau, 0, 2*sp.log(ell)/mu))
    # These are conditional exponents of the stated norm/product bounds,
    # not a symbolic substitute for proving those bounds on the torus.
    residual_powers = {
        "forced_harmonic_remainder": 3-theta/2,
        "primary_correction_or_mean_primary_slow": 3-theta/2,
        "mean_correction_fast": 3-theta/2,
        "mean_self_or_correction_pair": 4-3*theta/2,
        "primary_viscosity": 3+3*theta/2,
        "harmonic_correction_viscosity": 4+theta/2,
        "mean_viscosity": 6-3*theta/2,
        "primary_background_mismatch": 4+3*theta/2,
    }
    specialized = {key: value.subs(theta, sp.Rational(1, 2))
                   for key, value in residual_powers.items()}
    return {
        "checks": {
            "first_residual_power": first.subs(theta, values["theta"]) == sp.Rational(9, 4),
            "second_residual_power": second.subs(theta, values["theta"]) == sp.Rational(11, 4),
            "first_order_gradient_exponent_negative": clean(grad_first+(1-theta)*(s+5)/(2*s)) == 0,
            "second_order_gradient_formula": clean(grad_second-(1-theta)*(s-10)/(2*s)) == 0,
            "H10_only_borderline": grad_second.subs({theta: sp.Rational(1, 2), s: 10}) == 0,
            "H9_does_not_close": grad_second.subs({theta: sp.Rational(1, 2), s: 9}) < 0,
            "H12_gradient_margin": grad_second.subs(pins) == sp.Rational(1, 24),
            "H12_velocity_margin": vel_second.subs(pins) == sp.Rational(9, 8),
            "subpolynomial_log_factor": log_ratio == -alpha,
            "integrated_central_strain": clean(integrated-(ell-1/ell)/mu) == 0,
            "positive_correction_gradient_powers": (2-2*theta).subs(theta, sp.Rational(1, 2)) == 1 and (1-theta).subs(theta, sp.Rational(1, 2)) == sp.Rational(1, 2),
            "physical_packet_power": (2+3*theta/2).subs(theta, sp.Rational(1, 2)) == sp.Rational(11, 4),
            "packet_power_below_old_threshold": sp.Rational(11, 4) > sp.Rational(11, 10),
            **{f"residual_power_{key}_at_least_11_over_4": power >= sp.Rational(11, 4)
               for key, power in specialized.items()},
        },
        "first_order_gradient_exponent": str(grad_first),
        "second_order_gradient_exponent": str(grad_second),
        "H12_gradient_error_power": "1/24",
        "H12_velocity_error_power": "9/8",
        "residual_L2_h_powers_theta_half": {key: str(power) for key, power in specialized.items()},
        "assumptions": "Envelope exponent 0<theta<1; s>5/2; the main application fixes theta=1/2 and s=12. The L2/Hs estimates and nearby-covector bound are analytic inputs, not machine-certified here.",
        "scope": "Conditional power arithmetic. The norms, remainder bounds, nearby-covector control, and strong bootstrap must be established analytically.",
    }


@lru_cache(maxsize=1)
def outgoing_wave_checks():
    kappa, p, q = sp.symbols("kappa p q", real=True)
    # Orthonormal coordinates put any nonzero orthogonal p-vector and N
    # in the first and third directions. Their lengths are p,q here.
    pv, N = sp.Matrix([p, 0, 0]), sp.Matrix([0, 0, q])
    A = kappa*pv*N.T
    S = (A+A.T)/2
    polynomial_A, polynomial_S = A.charpoly(), S.charpoly()
    lam_A, lam_S = polynomial_A.gen, polynomial_S.gen
    return {
        "checks": {
            "transverse_rank_one_gradient_nilpotent": A*A == sp.zeros(3),
            "all_gradient_eigenvalues_zero": polynomial_A.as_expr() == lam_A**3,
            "strain_has_two_opposite_eigenvalues": clean(polynomial_S.as_expr()-lam_S*(lam_S**2-kappa**2*p**2*q**2/4)) == 0,
            "nonzero_strain_does_not_imply_gradient_hyperbolicity": S.subs({kappa: 1, p: 1, q: 2}).eigenvals() == {-1: 1, 0: 1, 1: 1},
        },
        "scope": "Instantaneous leading-gradient control only. No next-carrier Floquet multiplier is established by large strain.",
    }


def build_receipt():
    sections = {
        "quadratic": quadratic_checks(),
        "forced_harmonic_1": forced_harmonic_checks(1),
        "forced_harmonic_2": forced_harmonic_checks(2),
        "mean_feedback": mean_feedback_checks(),
        "scaling": scaling_checks(),
        "outgoing_wave": outgoing_wave_checks(),
    }
    # SymPy relational results must become actual JSON booleans at both
    # levels, not strings that would remain truthy when a check failed.
    sections = {name: {**section, "checks": {
        key: bool(value) for key, value in section["checks"].items()
    }} for name, section in sections.items()}
    checks = {f"{name}.{key}": bool(value) for name, section in sections.items()
              for key, value in section["checks"].items()}
    return {
        "stamp": "2026-09-08",
        "node": "nse-loglog-strain-handover",
        "evidence_class": "EXACT_ALGEBRA_ONLY",
        "research_note": "references/navier-stokes/loglog-handover.md",
        "written_proof_status": "INDEPENDENTLY_REVIEWED_RESTRICTED_ANALYTIC_RESULT",
        "written_proof_scope": "Finite supplied-seed smooth NS strain handover with changing initial data; justified by the separate written proof, not by this receipt.",
        "root_status": "OPEN", "E_prime_status": "OPEN",
        "dns_run": False, "lean_kernel_checked": False,
        "PDE_theorem_certified": False,
        "mean_PDE_estimates_certified": False,
        "all_mode_remainder_bound_certified": False,
        "strong_continuation_certified": False,
        "actual_perturbed_particle_tracked": False,
        "candidate_evaluation_point": "Reference Euler particle; not the perturbed NS particle.",
        "claim_boundary": "Exact differential identities, failed-omission controls, and conditional exponent arithmetic only. The written note separately establishes its restricted analytic statement. This receipt does not certify the handover PDE theorem, next Floquet amplifier, activation target, infinite cascade, novelty, or ROOT.",
        **sections, "checks": checks, "all_green": all(checks.values()),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args(argv)
    receipt = build_receipt()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(f"{args.out}: {sum(receipt['checks'].values())}/{len(receipt['checks'])} exact checks; algebra only; ROOT OPEN")
    return 0 if receipt["all_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
