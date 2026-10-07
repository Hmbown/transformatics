"""Exact local algebra controls for the supplied-seed viscous packet note.

These checks do NOT certify the PDE analytic estimates, the existence of a
Gavrilov profile, its Floquet exponent, Sobolev constants, or a full NS proof.
The affine jet below is a local symbolic control, not the compact background.
No equation is time-stepped and no DNS or Lean expansion is performed.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/enstrophy_sup/nse_viscous_packet.json"
R = sp.Rational


def curl(v, coordinates):
    x, y, z = coordinates
    return sp.Matrix([sp.diff(v[2], y)-sp.diff(v[1], z),
                      sp.diff(v[0], z)-sp.diff(v[2], x),
                      sp.diff(v[1], x)-sp.diff(v[0], y)])


def gradient(f, coordinates):
    return sp.Matrix([sp.diff(f, x) for x in coordinates])


def divergence(v, coordinates):
    return sum(sp.diff(v[i], coordinates[i]) for i in range(3))


def advect(u, v, coordinates):
    return v.jacobian(coordinates)*u


def _zero(v):
    return all(sp.simplify(x) == 0 for x in v)


def affine_packet_jet(A, xi, b0, envelope, coordinates, h,
                      pressure_factor=2):
    """Differentiate the Cartesian curl at t=0, before cancelling terms.

The jets are S_t=-V.grad S, xi_t=-A.T xi and f_t=-V.grad f.
The polarization has the correct factor two; pressure_factor deliberately
varies only the pressure, allowing an independent missing-pressure control.
All returned amplitudes have the common exponential divided out.
"""
    A, xi, b0 = map(sp.Matrix, (A, xi, b0))
    coordinates = sp.Matrix(coordinates)
    if A.shape != (3, 3) or A.trace() != 0 or xi.dot(xi) == 0:
        raise ValueError("requires a trace-free 3D jet and nonzero covector")
    if xi.dot(b0) != 0:
        raise ValueError("initial polarization must be transverse")
    V, k2 = A*coordinates, xi.dot(xi)
    xi_t = -A.T*xi
    p0 = 2*xi.dot(A*b0)/k2
    b0_t = -A*b0+xi*p0
    f_t = -gradient(envelope, coordinates).dot(V)
    F = xi.cross(b0)*envelope/k2
    F_t = ((xi_t.cross(b0)+xi.cross(b0_t))*envelope
           +xi.cross(b0)*f_t)/k2 - F*2*xi.dot(xi_t)/k2
    phase = sp.exp(sp.I*xi.dot(coordinates)/h)
    S_t = -xi.dot(V)
    # Actual curls and Cartesian derivatives: no pre-cancelled residual used.
    w = h*curl(sp.I*F*phase, coordinates)
    w_t = h*curl(sp.I*(F_t+sp.I*F*S_t/h)*phase, coordinates)
    pressure = sp.I*h*pressure_factor*xi.dot(A*b0)*envelope*phase/k2
    residual = w_t+advect(V, w, coordinates)+A*w+gradient(pressure, coordinates)
    laplacian = w.applyfunc(lambda a: sum(sp.diff(a, x, 2) for x in coordinates))

    def demod(v):
        return v.applyfunc(lambda a: sp.simplify(sp.expand(a/phase)))

    correction = sp.I*curl(F, coordinates)
    # This comparison independently differentiates the factored correction.
    correction_t = sp.I*curl(F_t, coordinates)
    expected = h*(correction_t+advect(V, correction, coordinates)
                  +A*correction+sp.I*gradient(p0*envelope, coordinates))
    return {"wave": demod(w), "residual": demod(residual),
            "expected_residual": expected.applyfunc(sp.simplify),
            "laplacian": demod(laplacian),
            "divergence": sp.simplify(divergence(w, coordinates)/phase),
            "uncorrected_divergence": sp.simplify(
                divergence(b0*envelope*phase, coordinates)/phase),
            "correction": correction, "pressure_amplitude": p0*envelope,
            "transversality_time_derivative": sp.simplify(
                xi_t.dot(b0)+xi.dot(b0_t))}


def derivative_order(expression):
    return max((sum(n for _, n in a.variable_count)
                for a in expression.atoms(sp.Derivative)), default=0)


@lru_cache(maxsize=1)
def packet_checks():
    x, y, z = coordinates = sp.symbols("x y z", real=True)
    h, delta = sp.symbols("h delta", positive=True)
    A = sp.Matrix([[1, 2, 0], [0, -1, 1], [1, 0, 0]])
    xi, b0 = sp.Matrix([1, 2, 3]), sp.Matrix([2, -1, 0])
    f = sp.Function("f")(*coordinates)
    jet = affine_packet_jet(A, xi, b0, f, coordinates, h)
    wrong = affine_packet_jet(A, xi, b0, f, coordinates, h, pressure_factor=1)
    # A cubic envelope activates all three derivatives in the viscous term.
    # The delta^-3/2 mass normalization is priced separately below.
    polynomial = (1+x/delta+2*y/delta-z/delta
                  +(x*y+2*y*z+3*z*x+x*x)/delta**2
                  +(x**3+y**3+z**3+x*y*z)/delta**3)
    cubic = affine_packet_jet(A, xi, b0, polynomial, coordinates, h)
    origin = dict.fromkeys(coordinates, 0)
    cubic_residual = cubic["residual"].subs(origin)
    residual_coefficient = sp.Matrix([92, 94, -56])/49
    powers = set()
    for component in jet["laplacian"]:
        for term in sp.expand(component).as_ordered_terms():
            powers.add((int(term.as_powers_dict().get(h, 0)),
                        derivative_order(term)))
    # All Hessian and third-derivative atoms cancel in the Euler residual.
    # This is checked for arbitrary f, as well as the explicit cubic above.
    checks = {
        "nontrivial_incompressible_jet": A.trace() == 0 and A != -A.T,
        "nonzero_pressure_correction": xi.dot(A*b0) == 8,
        "transversality_preserved": jet["transversality_time_derivative"] == 0,
        "actual_curl_is_solenoidal": jet["divergence"] == 0,
        "curl_has_positive_leading_amplitude": _zero(jet["wave"]-b0*f-h*jet["correction"]),
        "direct_cartesian_pressure_residual_identity": _zero(jet["residual"]-jet["expected_residual"]),
        "arbitrary_envelope_euler_order_exactly_one": max(map(derivative_order, jet["residual"])) == 1,
        "cubic_envelope_residual_nonzero_h_over_delta": _zero(cubic_residual-sp.I*h/delta*residual_coefficient),
        "cubic_residual_has_no_inverse_h_term": all(sp.simplify(a/h).has(h) is False for a in cubic["residual"]),
        "viscous_derivative_pairs_complete": powers == {(-2, 0), (-1, 1), (0, 2), (1, 3)},
        "negative_omitting_curl_correction_detected": jet["uncorrected_divergence"] != 0,
        "negative_pressure_factor_one_detected": not _zero(wrong["residual"]-jet["residual"]),
        "missing_pressure_leaves_leading_parallel_error": _zero(
            (wrong["residual"]-jet["residual"]).subs(h, 0)-xi*R(4, 7)*f),
    }
    return {"checks": checks, "jet": str(A.tolist()), "covector": list(map(int, xi)),
            "polarization": list(map(int, b0)), "polynomial_envelope": str(polynomial),
            "cubic_origin_residual": [str(a) for a in cubic_residual],
            "euler_residual": [str(a) for a in jet["residual"]],
            "laplacian_h_power_and_envelope_order": sorted(powers),
            "scope": "Local differential identities and derivative counts only; no global PDE estimates or compact profile certified."}


def torus_mean(expression, coordinates):
    """Exact integral of the finite trigonometric controls used here."""
    result = sp.expand_trig(sp.expand(expression))
    for x in coordinates:
        result = sp.integrate(result, (x, -sp.pi, sp.pi))/(2*sp.pi)
    return sp.simplify(result)


@lru_cache(maxsize=1)
def energy_checks():
    x, y, z = coordinates = sp.symbols("x y z", real=True)
    eta = sp.symbols("eta", real=True)
    e = sp.Matrix([sp.sin(y), sp.sin(2*x), 0])
    w = sp.Matrix([sp.sin(2*x)*sp.cos(y), -2*sp.cos(2*x)*sp.sin(y), 0])
    v = sp.Matrix([sp.cos(z), sp.sin(x), sp.cos(y)])
    r = eta*w+e
    B = lambda u, a: advect(u, a, coordinates)
    exact_remainder = B(v+r, v+r)-B(v, v)-eta*(B(v, w)+B(w, v))
    required = B(v, e)+B(e, v)+eta*B(w, e)+eta*B(e, w)+B(e, e)+eta**2*B(w, w)
    transports = {name: torus_mean(e.dot(B(a, e)), coordinates)
                  for name, a in (("v", v), ("w", w), ("e", e))}
    stretching = torus_mean(e.dot(B(e, w)), coordinates)
    jac = w.jacobian(coordinates)
    symmetric = (jac+jac.T)/2
    bad_velocity = sp.Matrix([sp.sin(x), 0, 0])
    bad_error = sp.Matrix([0, 1+sp.cos(x), 0])
    bad_transport = torus_mean(bad_error.dot(B(bad_velocity, bad_error)), coordinates)
    C, K, norm = sp.symbols("C K norm", positive=True)
    checks = {
        "three_control_velocities_solenoidal": all(divergence(a, coordinates) == 0 for a in (v, w, e)),
        "full_quadratic_subtraction_identity": _zero(exact_remainder-required),
        "three_transport_energy_pairings_vanish": all(a == 0 for a in transports.values()),
        "strain_pairing_does_not_cancel": stretching == R(3, 4),
        "only_symmetric_gradient_enters_energy": sp.simplify(e.dot(jac*e)-e.dot(symmetric*e)) == 0,
        "negative_compressible_transport_detected": bad_transport == -R(1, 2),
        "H3_bootstrap_scalar_margin": sp.expand((K+C)*norm-(K*norm+C*norm**2)-C*norm*(1-norm)) == 0,
        "forcing_sign_after_moving_to_RHS": _zero(exact_remainder-(required-eta**2*B(w, w))-eta**2*B(w, w)),
        "negative_reversed_quadratic_forcing_detected": not _zero(2*eta**2*B(w, w)),
    }
    return {"checks": checks, "exact_transport_means": {k: str(a) for k, a in transports.items()},
            "stretching_mean": str(stretching), "compressible_control_mean": str(bad_transport),
            "scope": "Exact periodic algebra/energy cancellations and scalar bootstrap identity; no Sobolev or existence theorem certified."}


def time_power(base_h_power, rate, c):
    """At epsilon=nu*h^4 and T=c*log(1/epsilon), h^a*exp(rate*T)."""
    return sp.sympify(base_h_power)-4*sp.sympify(rate)*sp.sympify(c)


def conservative_c(gamma, kappa, Kn, K3, Ke):
    rates = tuple(map(sp.sympify, (gamma, kappa, Kn, K3, Ke)))
    if any(a.is_positive is not True or not a.is_number for a in rates):
        raise ValueError("requires positive numerical rates, fixed before choosing c")
    gamma, kappa, Kn, K3, Ke = rates
    # Half the minimum makes all four restrictions strict.
    return min(1/(16*(gamma+kappa)), 3/(8*Kn), 3/(8*K3), 1/(4*Ke))/2


@lru_cache(maxsize=1)
def scaling_checks():
    h, nu, gamma, kappa = sp.symbols("h nu Gamma kappa", positive=True)
    L, A = h**-10, h**-14
    epsilon, delta, eta = nu*h**4, sp.sqrt(h), h**6
    c_linear = 1/(16*(gamma+kappa))
    # Exact symbolic positive margins above the quoted epsilon exponents.
    epsilon_exponents = [R(1, 8)-gamma*c_linear,
                         R(1, 8)-gamma*c_linear,
                         R(1, 2)-gamma*c_linear,
                         R(3, 4)-(gamma+kappa)*c_linear]
    floors = [R(1, 16), R(1, 16), R(7, 16), R(11, 16)]
    margins = [sp.factor(a-b) for a, b in zip(epsilon_exponents, floors)]
    # Values below are illustrative rational rates, NOT computed profile rates.
    rates = dict(gamma=sp.Integer(17), kappa=sp.Integer(23),
                 Kn=sp.Integer(5), K3=sp.Integer(7), Ke=sp.Integer(31))
    c = conservative_c(**rates)
    exponents = {
        "spatial_coherence": time_power(R(1, 2), rates["gamma"], c),
        "Euler_envelope": time_power(R(1, 2), rates["gamma"], c),
        "viscosity": time_power(2, rates["gamma"], c),
        "background": time_power(3, rates["gamma"]+rates["kappa"], c),
        "H3_perturbation": time_power(3, rates["Kn"], c),
        "eta_grad_linear": time_power(3, rates["K3"], c),
        "nonlinear_error_div_eta": time_power(2, rates["Ke"], c),
        "physical_perturbation_highpass_upper": time_power(7, rates["Kn"], c),
    }
    # Normalized L2 envelope: squared derivative contributes delta^-3-2m;
    # the three-dimensional Jacobian cancels the delta^-3 normalization.
    m = sp.symbols("m", integer=True, nonnegative=True)
    normalization = sp.simplify(delta**(-3-2*m)*delta**3-delta**(-2*m))
    correction_excesses = [sp.factor(h**(1-a)*delta**(-(order+1-a))*h**order)
                           for order in (0, 1, 2, 3) for a in range(order+1)]
    # Express the strict-bound consequences as boundary margins.  The actual
    # chosen c is smaller, so these lower bounds become strict.
    boundary = {"H3": 3-4*R(3, 8), "eta_grad": 3-4*R(3, 8),
                "error_div_eta": 2-4*R(1, 4),
                "physical_highpass": 7-4*R(3, 8)}
    checks = {
        "physical_equation_viscosity": sp.simplify(nu*L/A-epsilon) == 0,
        "physical_time_factor": A*L == h**-24,
        "physical_frequency_threshold": L/h == h**-11,
        "physical_averaged_L2_factor": sp.simplify(A*L**(-R(3, 2))-h) == 0,
        "physical_initial_seed_power_seven": h*eta == h**7,
        "old_target_power_eleven_tenths": (L/h)**(-R(1, 10)) == h**R(11, 10),
        "viscous_principal_power_two": epsilon/h**2 == nu*h**2,
        "background_principal_power_three": epsilon/h == nu*h**3,
        "balanced_coherence_and_envelope": delta == h/delta,
        "normalized_L2_has_no_extra_volume_loss": normalization == 0,
        "all_initial_H3_correction_powers_bounded": all(a.as_powers_dict().get(h, 0) >= 0 for a in correction_excesses),
        "all_viscous_raw_powers_bounded_by_h_minus_two": all(a >= -2 for a in (-2, -1-R(1, 2), -1, 1-R(3, 2))),
        "linear_epsilon_exponent_floors": all(a.is_nonnegative is True for a in margins),
        "logarithmic_exponential_sign": time_power(1, 2, R(1, 3)) == -R(5, 3),
        "negative_reversed_exponent_detected": time_power(1, 2, R(1, 3)) != 1+4*2*R(1, 3),
        "fixed_H3_initial_smallness": eta*h**-3 == h**3,
        "quadratic_forcing_H3_H1_power": h**-3*h**-1 == h**-4,
        "nonlinear_remainder_div_eta_power_two": eta**2*h**-4/eta == h**2,
        "H8_background_is_smaller_than_seed": h**8/eta == h**2,
        "H3_bootstrap_boundary_margin": boundary["H3"] == R(3, 2),
        "small_linear_gradient_boundary_margin": boundary["eta_grad"] == R(3, 2),
        "nonlinear_error_boundary_margin": boundary["error_div_eta"] == 1,
        "old_target_excluded_by_actual_upper_bound": boundary["physical_highpass"]-R(11, 10) == R(22, 5) and 9-R(11, 10) > 0,
        "illustrative_c_obeys_all_strict_bounds": all((c < 1/(16*(rates["gamma"]+rates["kappa"])), c < 3/(8*rates["Kn"]), c < 3/(8*rates["K3"]), c < 1/(4*rates["Ke"]))),
        "illustrative_exponents_all_positive": all(a > 0 for a in exponents.values()),
    }
    return {"checks": checks, "linear_epsilon_exponents": [str(a) for a in epsilon_exponents],
            "linear_floor_margins": [str(a) for a in margins],
            "illustrative_rates_not_profile_certificates": {k: str(v) for k, v in rates.items()},
            "illustrative_c": str(c), "illustrative_h_exponents": {k: str(v) for k, v in exponents.items()},
            "strict_constraint_boundary_exponents": {k: str(v) for k, v in boundary.items()},
            "physical_L2_factor": "h/(2*pi)^(3/2), for unnormalized rescaled L2",
            "actual_old_target_exclusion": "Physical highpass <= C_nu*(h^9+h^(7-4*c*Kn)); 7-4*c*Kn>11/2>11/10. Conditional on the analytic H3 bootstrap, this excludes the actual old target throughout the window.",
            "scope": "Exact exponent implications of stated analytic estimates; illustrative rates are not bounds for the frozen profile."}


@lru_cache(maxsize=1)
def real_normalization_checks():
    a, d, h, phase = sp.symbols("a d h phase", real=True)
    real = a*sp.cos(phase)-h*d*sp.sin(phase)
    imag = a*sp.sin(phase)+h*d*sp.cos(phase)
    x, delta = sp.symbols("x delta", positive=True)
    # A finite exact envelope witness for the IBP coefficient; this polynomial
    # vanishes at its two endpoints.  It is not a claimed C-infinity packet.
    f2 = (1-(x/delta)**2)**2
    xi = sp.Integer(3)
    carrier = sp.exp(2*sp.I*xi*x/h)
    primitive = h*carrier/(2*sp.I*xi)
    checks = {
        "real_imag_squared_norm_identity": sp.trigsimp(real**2+imag**2-a**2-h**2*d**2) == 0,
        "half_mass_plus_oscillation_identity": sp.trigsimp(real**2-(a**2/2+a**2*sp.cos(2*phase)/2- a*h*d*sp.sin(2*phase)+h**2*d**2*sp.sin(phase)**2)) == 0,
        "IBP_carrier_factor_h": sp.simplify(sp.diff(primitive, x)-carrier) == 0,
        "IBP_boundary_witness_vanishes": f2.subs(x, delta) == 0 and f2.subs(x, -delta) == 0,
        "IBP_envelope_derivative_cost": sp.simplify(sp.diff(f2, x).subs(x, delta*a)*delta+4*a*(1-a*a)) == 0,
        "quadrature_lower_norm_one_half": sp.sqrt(R(1, 4)) == R(1, 2),
    }
    return {"checks": checks,
            "scope": "Quadrature and one-IBP algebra only. Uniform real mass uses the note's L1/L2 envelope estimates. Real selection is for one prescribed final time, with two signed Fourier lobes."}


def build_receipt():
    sections = {"packet": packet_checks(), "energy": energy_checks(),
                "scaling": scaling_checks(), "real_normalization": real_normalization_checks()}
    sections = {name: {**data, "checks": {key: bool(value) for key, value in data["checks"].items()}}
                for name, data in sections.items()}
    checks = {f"{section}.{key}": bool(value) for section, data in sections.items()
              for key, value in data["checks"].items()}
    return {"stamp": "2026-09-08", "node": "nse-viscous-packet-controls",
            "root_status": "OPEN", "E_prime_status": "OPEN", "gso_route_status": "DEAD",
            "evidence_class": "EXACT_LOCAL_ALGEBRA_AND_SCALING_CONTROLS_ONLY",
            "pde_analytic_estimates_certified": False, "lean_kernel_checked": False,
            "dns_run": False, "specific_profile_rates_computed": False,
            "unconditional_NS_solution_proved": False,
            "candidate_note": "references/navier-stokes/viscous-packet.md",
            **sections, "checks": checks, "all_green": all(checks.values()),
            "claim_boundary": "These finite exact controls support review of a supplied-seed finite-time estimate. They do not certify its analytic hypotheses, global PDE estimates, full formalization, original activation target, infinite cascade, blow-up, or regularity."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args(argv)
    receipt = build_receipt()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt, indent=2, default=str)+"\n")
    print(json.dumps({"all_green": receipt["all_green"], "checks": len(receipt["checks"]),
                      "out": str(args.out), "pde_analytic_estimates_certified": False}))
    return 0 if receipt["all_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
