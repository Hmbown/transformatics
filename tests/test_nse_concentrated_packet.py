"""Independent packet, relative-energy, pressure, and interval-domain checks."""

import json

import numpy as np
import pytest
import sympy as sp

from experiments.nse_concentrated_packet import (
    LOCAL_X, OUT, PERSISTENCE_X, build_receipt, gradient_at_zero, high_seed,
    main, packet_fourier, packet_moments, persistence_checks,
    relative_energy_checks, relative_envelope,
)
from experiments.nse_frequency_activation import bilinear, coefficient, support
from experiments.nse_qgso_transfer_budget import add, derivative


@pytest.mark.parametrize("n", [1, 2, 4, 8])
def test_closed_packet_moments_against_independent_finite_sums(n):
    p = packet_moments(n)
    raw_energy, raw_compression, representatives = 0, 0, 0
    for k1 in range(n, 2*n):
        for k2 in range(1-2*n, 2*n):
            if abs(k2) < n:
                continue
            for _ in range(-n, n+1):
                v1, v2 = -k1*k2*k2, k1*k1*k2
                raw_energy += sp.Rational(v1*v1+v2*v2, 2)
                raw_compression -= k1*v1
                representatives += 1
    assert raw_energy == p["raw_mean_norm_squared"]
    assert raw_compression == p["raw_compressive_gradient"]
    assert 2*representatives == p["mode_count"]
    assert p["sigma_squared_over_LWbar_squared"] >= sp.Rational(1, 72)


def _physical_packet(n, grid):
    q = 2*np.pi*np.arange(grid)/grid
    x, y, z = np.meshgrid(q, q, q, indexing="ij")
    xs = sum(k*np.sin(k*x) for k in range(n, 2*n))
    xc = sum(k*k*np.cos(k*x) for k in range(n, 2*n))
    ys = sum(k*np.sin(k*y) for k in range(n, 2*n))
    yc = sum(k*k*np.cos(k*y) for k in range(n, 2*n))
    zz = 1 + 2*sum(np.cos(k*z) for k in range(1, n+1))
    return np.array([-2*xs*yc*zz, 2*xc*ys*zz, np.zeros_like(x)])


def _spectral(v):
    grid = v.shape[1]
    wave = np.fft.fftfreq(grid, d=1/grid)
    k = np.array(np.meshgrid(wave, wave, wave, indexing="ij"))
    vh = np.fft.fftn(v, axes=(1, 2, 3))/grid**3
    return k, vh


def _gradient(v):
    grid = v.shape[1]
    k, vh = _spectral(v)
    return np.array([np.fft.ifftn(1j*k[j]*vh, axes=(1, 2, 3)).real*grid**3
                     for j in range(3)]).swapaxes(0, 1)


def _rhs_hat(v, nu):
    k, vh = _spectral(v)
    grid = v.shape[1]
    gradient = _gradient(v)
    adv = np.einsum("jabc,ijabc->iabc", v, gradient)
    rawh = -np.fft.fftn(adv, axes=(1, 2, 3))/grid**3
    k2 = np.sum(k*k, axis=0)
    projected = rawh - k*np.sum(k*rawh, axis=0)/np.where(k2 == 0, 1, k2)
    return projected - nu*k2*vh


@pytest.mark.parametrize("n,grid", [(1, 16), (2, 24), (4, 32)])
def test_packet_against_independent_factorized_trigonometric_field(n, grid):
    stats = packet_moments(n)
    normalization = np.sqrt(float(stats["raw_mean_norm_squared"]))
    v = _physical_packet(n, grid)/normalization
    k, vh = _spectral(v)
    # The input is checked before any Leray projection.
    assert np.max(np.abs(np.sum(k*vh, axis=0))) < 2e-12
    assert np.mean(np.sum(v*v, axis=0)) == pytest.approx(1, abs=2e-13)
    expected = np.zeros_like(vh)
    exact = packet_fourier(n)
    for mode in support(exact):
        ix = tuple(q % grid for q in mode)
        expected[(slice(None),)+ix] = [complex(c)/normalization for c in coefficient(exact, mode)]
    assert np.max(np.abs(vh-expected)) < 2e-14
    sigma = float(stats["raw_compressive_gradient"])/normalization
    assert _gradient(v)[:, :, 0, 0, 0] == pytest.approx(np.diag([-sigma, sigma, 0]), abs=3e-11)
    if n == 1:
        assert _rhs_hat(v, 0)[:, 2, 0, 2] == pytest.approx([1j/12, 0, -1j/12], abs=3e-13)


def test_pressure_generates_vertical_velocity_from_horizontal_initial_packet():
    u = packet_fourier(1)
    assert u[2] == {}
    assert coefficient(bilinear(u, u), (2, 0, 2))[2] == -sp.I/2


def test_relative_energy_with_full_pressure_against_independent_physical_products():
    grid = 24
    q = 2*np.pi*np.arange(grid)/grid
    x, y, z = np.meshgrid(q, q, q, indexing="ij")
    U = _physical_packet(1, grid)
    c = np.cos(-3*x+y)
    w = np.array([2*c, 2*np.cos(4*x)+6*c, np.zeros_like(z)])
    nu = 0.03
    rhs = np.fft.ifftn(_rhs_hat(U+w, nu)-_rhs_hat(U, nu), axes=(1, 2, 3)).real*grid**3
    actual = np.mean(np.sum(w*rhs, axis=0))
    gradU, gradw = _gradient(U), _gradient(w)
    contraction = np.mean(np.einsum("iabc,ijabc,jabc->abc", w, gradU, w))
    expected = -nu*np.mean(np.sum(gradw*gradw, axis=(0, 1))) - contraction
    assert actual == pytest.approx(expected, abs=3e-11)
    assert -contraction == pytest.approx(float(sp.sympify(relative_energy_checks()["nonlinear_relative_pairing"])), abs=3e-12)
    assert abs(contraction) > 1


@pytest.mark.parametrize("j", [1, 3, 7])
def test_high_support_is_not_invariant_even_without_a_background(j):
    w = high_seed(j)
    assert add(*(derivative(w[i], i) for i in range(3))) == {}
    assert all(sum(q*q for q in k) > j*j for k in support(w))
    assert coefficient(bilinear(w, w), (0, 1, 0)) == (-sp.I, 0, 0)


def test_persistence_margins_and_material_ball_trapping_are_exact():
    p = persistence_checks()
    assert all(p["checks"].values())
    assert sp.Rational(p["temporal_margin"]) == sp.Rational(16716335, 1193845248)
    assert sp.Rational(p["spatial_margin"]) == sp.Rational(55932389, 4747400244)
    assert sp.Rational(p["flow_radius_amplification_upper"]) == sp.Rational(509, 508)


def test_relative_gain_bound_does_not_differentiate_the_high_seed():
    epsilon = sp.Rational(1, 24)
    near = relative_envelope(1, 1, LOCAL_X, 6, epsilon)
    far = relative_envelope(1, 1, LOCAL_X, 60, epsilon)
    assert near["relative_gain_bound"] == far["relative_gain_bound"] == sp.Rational(3, 2)
    assert far["background_tail"] < near["background_tail"]
    assert near["total_bound"] == sp.Rational(3, 32) < sp.Rational(1, 8)
    at_start = relative_envelope(1, 1, 0, 6, epsilon)
    assert at_start["total_bound"] == epsilon


def test_bound_cannot_be_extended_by_silently_restarting_the_clock():
    with pytest.raises(ValueError):
        relative_envelope(1, 1, sp.Rational(1, 3), 100, sp.Rational(1, 1000))


@pytest.mark.parametrize("bad", [0, -1, 1.5, True])
def test_invalid_packet_scale_is_rejected(bad):
    with pytest.raises(ValueError):
        packet_moments(bad)


def test_large_symbolic_scale_does_not_request_a_grid_or_enumerate_modes():
    p = packet_moments(2**100)
    assert p["mode_count"] == 4*(2**100)**2*(2**101+1)
    assert p["sigma_squared_over_LWbar_squared"] >= sp.Rational(1, 72)
    with pytest.raises(ValueError):
        packet_fourier(2**100)


def test_receipt_reproduces_and_writer_respects_artifact_immutability(tmp_path):
    result = build_receipt()
    assert result == json.loads(OUT.read_text())
    assert result["all_green"] and not result["dns_run"]
    assert result["root_status"] == result["E_prime_status"] == "OPEN"
    assert result["gso_route_status"] == "DEAD"
    target = tmp_path/"receipt.json"
    assert main(["--out", str(target)]) == 0
    assert json.loads(target.read_text()) == result
