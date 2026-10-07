"""Independent algebra/constant checks; no finite test proves the PDE theorem."""

import json
from functools import lru_cache

import numpy as np
import pytest
import sympy as sp

from experiments.nse_frequency_activation import (
    EPSILON, OUT, TAU_STAR, bilinear, build_receipt, coefficient, cyclic_seed,
    exact_interactions, far_tail_bound, highpass_energy_defect, main,
    rational_majorant_checks, remainder_bound, support, tree_coefficient,
    vector_add, vector_inner,
)
from experiments.nse_qgso_transfer_budget import add, derivative, scale


def test_supplied_seed_is_real_mean_zero_and_genuinely_three_dimensional():
    checks = exact_interactions()["checks"]
    assert all(checks[k] for k in (
        "seed_raw_divergence_zero", "seed_reality", "seed_frequency_rank_three",
        "seed_mean_zero",
    ))
    # Break cyclic symmetry without introducing a translation-invariant direction.
    u = cyclic_seed()
    u[1] = add(u[1], {(1, 0, 0): EPSILON/2, (-1, 0, 0): EPSILON/2})
    assert add(*(derivative(u[i], i) for i in range(3))) == {}
    assert sp.Matrix(sorted(support(u))).rank() == 3
    assert highpass_energy_defect(vector_add(u, bilinear(u, u)), 1) == 0


@pytest.mark.parametrize("frequency,amplitude", [(1, 1), (2, sp.Rational(3, 2)), (5, -2)])
def test_signed_interactions_and_backreaction_scale_exactly(frequency, amplitude):
    N, A = frequency, sp.sympify(amplitude)
    u = cyclic_seed(N, A)
    b = bilinear(u, u)
    c = vector_add(bilinear(u, b), bilinear(b, u))
    assert coefficient(b, (N, N, 0)) == (0, 0, -sp.I*A*A*N/4)
    assert coefficient(c, (N, 2*N, 0)) == (0, 0, -A**3*N*N/8)
    assert vector_inner(b, b) == 3*A**4*N*N/4
    assert vector_inner(u, c) == -vector_inner(b, b)


def _fft_bilinear(a, b):
    """Independent physical product, spectral differentiation and pressure."""
    n = a.shape[1]
    wave = np.fft.fftfreq(n, d=1/n)
    k = np.array(np.meshgrid(wave, wave, wave, indexing="ij"))
    bh = np.fft.fftn(b, axes=(1, 2, 3)) / n**3
    raw = np.zeros_like(b)
    for j in range(3):
        derivative_b = np.fft.ifftn(1j*k[j]*bh, axes=(1, 2, 3)).real * n**3
        raw -= a[j]*derivative_b
    rawh = np.fft.fftn(raw, axes=(1, 2, 3)) / n**3
    k2 = np.sum(k*k, axis=0)
    safe = np.where(k2 == 0, 1, k2)
    projected = rawh - k*np.sum(k*rawh, axis=0)/safe
    return rawh, projected


@pytest.mark.parametrize("grid", [16, 24])
def test_exact_convolution_against_independent_physical_product_and_pressure(grid):
    q = 2*np.pi*np.arange(grid)/grid
    x, y, z = np.meshgrid(q, q, q, indexing="ij")
    u = np.array([np.cos(y), np.cos(z), np.cos(x)])
    # This closed expression is independent of the rational convolution code.
    b = np.array([np.sin(y)*np.cos(z), np.sin(z)*np.cos(x), np.sin(x)*np.cos(y)])
    _, bh = _fft_bilinear(u, u)
    raw1, c1 = _fft_bilinear(u, b)
    raw2, c2 = _fft_bilinear(b, u)
    uh = np.fft.fftn(u, axes=(1, 2, 3)) / grid**3
    wave = np.fft.fftfreq(grid, d=1/grid)
    ks = np.array(np.meshgrid(wave, wave, wave, indexing="ij"))
    # Diagnose the supplied field before any projection.
    assert np.max(np.abs(np.sum(ks*uh, axis=0))) < 2e-14
    exact_u = cyclic_seed()
    exact_b = bilinear(exact_u, exact_u)
    exact_c = vector_add(bilinear(exact_u, exact_b), bilinear(exact_b, exact_u))
    for actual, expected in [(bh, exact_b), (c1+c2, exact_c)]:
        target = np.zeros_like(actual)
        for k in support(expected):
            at = tuple(ki % grid for ki in k)
            target[(slice(None),)+at] = [complex(a) for a in coefficient(expected, k)]
        assert np.max(np.abs(actual-target)) < 3e-14
    assert (raw1+raw2)[:, 1, 1, 1] == pytest.approx([-0.25]*3, abs=2e-14)
    assert (c1+c2)[:, 1, 1, 1] == pytest.approx([0]*3, abs=2e-14)


def test_noninvariance_and_feedback_are_retained():
    result = exact_interactions()
    assert len(result["first_support"]) == 12
    assert len(result["third_order_support"]) == 18
    assert all(result["checks"].values())


def test_homogeneous_support_grows_instead_of_assuming_a_closed_triad():
    @lru_cache(maxsize=None)
    def term(n):
        if n == 1:
            return cyclic_seed()
        fields = [bilinear(term(j), term(n-j)) for j in range(1, n)]
        return [scale(add(*(f[i] for f in fields)), sp.Rational(1, n-1))
                for i in range(3)]
    for n in range(1, 5):
        u = term(n)
        assert all(sum(ki*ki for ki in k) <= n*n for k in support(u))
        assert add(*(derivative(u[i], i) for i in range(3))) == {}
    assert not support(term(3)) <= support(term(1)) | support(term(2))


def test_tree_majorant_from_generating_function():
    z = sp.symbols("z")
    T = sum(tree_coefficient(n)*z**n for n in range(1, 11))
    # Independent differential form of T exp(-T)=z; written proof handles all n.
    defect = sp.Poly(sp.expand(z*(1-T)*sp.diff(T, z)-T), z)
    assert all(defect.coeff_monomial(z**n) == 0 for n in range(1, 11))
    assert rational_majorant_checks()["checks"]["strong_third_derivative_tail_series"]


def test_activation_margin_is_rational_and_uniform_over_the_interval():
    result = rational_majorant_checks()
    assert all(result["checks"].values())
    assert sp.Rational(result["margin_over_one_eighth"]) == sp.Rational(333110403, 16877486080)
    # Worst endpoint, worst permitted perturbation, and Re=1 are conservative.
    for tau in (TAU_STAR/16, TAU_STAR/4, TAU_STAR):
        for eps in (0, EPSILON/2, EPSILON):
            lower = (1-2*tau)/4 - (6*eps+eps**2) - remainder_bound(3+eps, 1, tau)/tau
            assert lower > sp.Rational(1, 8)


def test_heat_damping_in_the_leading_target_is_integrated_exactly():
    nu, N, t, s = sp.symbols("nu N t s", positive=True)
    integrand = sp.exp(-2*nu*N*N*(t-s))*sp.exp(-2*nu*N*N*s)
    assert sp.simplify(sp.integrate(integrand, (s, 0, t)) - t*sp.exp(-2*nu*N*N*t)) == 0


def test_far_tail_uses_all_higher_orders_and_the_strict_cutoff():
    M, N, t = sp.Integer(3), sp.Integer(2), sp.Rational(1, 36)
    assert 3*M*N*t == sp.Rational(1, 2)
    assert far_tail_bound(M, N, t, 8*N) == 2*M/sp.Integer(2)**8
    assert far_tail_bound(M, N, t, 9*N-1) == far_tail_bound(M, N, t, 8*N)
    assert far_tail_bound(M, N, t, 9*N) == far_tail_bound(M, N, t, 8*N)/2


@pytest.mark.parametrize("bad", [(1, 1, sp.Rational(1, 3)), (1, 1, -1), (0, 1, 0)])
def test_remainder_rejects_use_outside_its_proved_range(bad):
    with pytest.raises(ValueError):
        remainder_bound(*bad)


def test_sparse_packet_energy_exponent_arithmetic():
    b = sp.symbols("b")
    # To compete with viscosity at H=L^b, m must scale at least L^(4b-2).
    assert sp.solve(sp.Eq(4*b-2, 3), b) == [sp.Rational(5, 4)]
    assert 4*sp.Rational(11, 10)-2 > 2
    # This arithmetic does not prove persistent sparsity or rule out denser packets.


def test_receipt_reproduces_and_writer_does_not_touch_pinned_artifacts(tmp_path):
    result = build_receipt()
    assert result == json.loads(OUT.read_text())
    assert result["all_green"] and result["root_status"] == result["E_prime_status"] == "OPEN"
    assert result["retired_gso_route_status"] == "DEAD" and not result["dns_run"]
    target = tmp_path / "receipt.json"
    assert main(["--out", str(target)]) == 0
    assert json.loads(target.read_text()) == result
