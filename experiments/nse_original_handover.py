"""Exact algebra and scale controls for the original-time handover notes.

These checks do not certify the written ODE matching estimates, PDE residual
bounds, strong continuation, or infinite iteration. No numerical flow is run.
Execute this file to emit a JSON receipt; a failed check gives exit status 1.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as s


def zero(expression):
    """Test a rational/symbolic identity exactly, component by component."""
    if isinstance(expression, s.MatrixBase):
        return all(s.factor(entry) == 0 for entry in expression)
    return s.simplify(expression) == 0


def projected_generator(pressure_factor=2, frame_sign=1):
    """Derive backward polarization from the 3D equation, then eliminate b_r.

    x,y,w are the moving-frame covector coordinates. A is an arbitrary
    trace-free Euler gradient, not a particular thin-limit numerical matrix.
    Omega follows from the primary polarization and cotangent equations.
    """
    x, y, w, shear = s.symbols('x y w shear', real=True)
    entries = s.symbols('a11 a12 a13 a21 a22 a23 a31 a32', real=True)
    a11, a12, a13, a21, a22, a23, a31, a32 = entries
    A = s.Matrix([[a11, a12, a13], [a21, a22, a23],
                  [a31, a32, -a11-a22]])
    omega = s.Matrix([[0, a21, -a31], [-a21, 0, -a32],
                      [a31, a32, 0]])
    eta = s.Matrix([x, y, w])
    rank_one = s.zeros(3)
    rank_one[0, 2] = shear
    background = A-rank_one
    backward = (background + frame_sign*omega
                - pressure_factor*eta*eta.T*background/eta.dot(eta))
    lift = s.Matrix([[1, 0], [-x/y, -w/y], [0, 1]])
    projected = (backward*lift).extract([0, 2], [0, 1])
    return {
        'coordinates': (x, y, w, shear), 'entries': entries,
        'A': A, 'omega': omega, 'eta': eta, 'lift': lift,
        'projected': projected,
    }


def checks():
    rows = []

    def pin(name, passed, details=None):
        row = {'name': name, 'passed': bool(passed)}
        if details is not None:
            row['details'] = details
        rows.append(row)

    model = projected_generator()
    x, y, w, shear = model['coordinates']
    a11, a12, a13, a21, a22, a23, a31, a32 = model['entries']
    A, omega, eta = model['A'], model['omega'], model['eta']
    K = model['projected']
    norm2 = x*x+y*y+w*w
    pin('arbitrary-gradient-trace-free', zero(s.trace(A)))
    pin('primary-frame-skew', zero(omega+omega.T))
    pin('receiving-lift-transverse', zero(eta.T*model['lift']))
    expected_D = s.Matrix([[a11, a12-a21, a13+a31],
                          [2*a21, a22, a23+a32],
                          [0, 0, -a11-a22]])
    pin('exact-cotangent-triangular-frame', zero(A-omega-expected_D))

    # The full pressure response to shear is derived before any inner limit.
    shear_column = K.diff(shear)
    expected_shear = s.Matrix([[0, -1+2*x*x/norm2],
                               [0, 2*x*w/norm2]])
    for row in range(2):
        for col in range(2):
            pin(f'full-shear-entry-{row+1}{col+1}',
                zero(shear_column[row, col]-expected_shear[row, col]))

    expected_numerator = -2*(
        a11*x*y*w-a12*x*x*w+a21*y*y*w-a22*x*y*w
        -a31*x*x*y-a31*y**3+a32*x**3+a32*x*y*y)
    pin('K21-complete-pressure-numerator',
        zero(K[1, 0]*y*norm2-expected_numerator))
    pin('K21-independent-of-shear', zero(K[1, 0].diff(shear)))
    pin('K21-a32-cancellation',
        zero(K[1, 0].diff(a32)*y*norm2+2*x*(x*x+y*y)))
    pin('K22-a32-cancellation',
        zero(K[1, 1].diff(a32)*y*norm2+2*w*(x*x+y*y)))
    pin('K22-no-a32-w-cubed',
        s.Poly(s.cancel(K[1, 1].diff(a32)*y*norm2), w).degree() == 1)

    wrong_pressure = projected_generator(pressure_factor=1)['projected']
    wrong_frame = projected_generator(frame_sign=-1)['projected']
    pin('negative-control-pressure-one-breaks-shear',
        not zero(wrong_pressure.diff(shear)-expected_shear))
    pin('negative-control-pressure-one-breaks-a32-cancellation',
        not zero(wrong_pressure[1, 1].diff(a32)*y*norm2
                 +2*w*(x*x+y*y)))
    pin('negative-control-frame-sign-breaks-K21',
        not zero(wrong_frame[1, 0]*y*norm2-expected_numerator))

    # This formal frozen-coefficient limit is NOT the growing-interval estimate.
    e = s.symbols('e', positive=True)
    z = s.symbols('z', real=True)
    scaled = s.diag(e, 1)*K*s.diag(1, e)
    substitutions = {x: 2*a21*e*z, y: 1, w: -a21*z*z, shear: e**-2}
    frozen = scaled.subs(substitutions).applyfunc(
        lambda value: s.limit(s.cancel(value), e, 0))
    P = 1+a21*a21*z**4
    expected_frozen = s.Matrix([
        [0, -1], [(2*a21*a21*z*z+2*a31)/P, -4*a21*a21*z**3/P]])
    for row in range(2):
        for col in range(2):
            pin(f'frozen-inner-entry-{row+1}{col+1}',
                zero(frozen[row, col]-expected_frozen[row, col]))

    # Conjugate the second-order operator independently using a free function.
    Y = s.Function('Y')(z)
    g = P**s.Rational(-1, 2)
    potential = 2*a21*a21*z*z+2*a31
    operator = s.diff(P*s.diff(g*Y, z), z)+potential*g*Y
    q = (4*a21*a21*z*z-2*a31*P)/P**2
    pin('positive-connection-full-conjugation',
        zero(operator/(P*g)-(s.diff(Y, z, 2)-q*Y)))
    positive_a, positive_c = s.symbols('positive_a positive_c', positive=True)
    P_positive = 1+positive_a**2*z**4
    pin('positive-kernel-decomposition',
        zero(q.subs({a21: -positive_a, a31: -positive_c})
             -4*positive_a**2*z*z/P_positive**2-2*positive_c/P_positive))
    t = s.symbols('t', nonnegative=True)
    moment_first = s.integrate(2*positive_a**2*t/(1+positive_a**2*t*t)**2,
                               (t, 0, s.oo))
    moment_second = s.integrate(positive_c/(1+positive_a**2*t*t), (t, 0, s.oo))
    pin('general-Volterra-kernel-moment',
        zero(moment_first+moment_second-1-s.pi*positive_c/(2*positive_a)))
    pin('thin-Volterra-kernel-moment',
        zero((moment_first+moment_second).subs(positive_c, positive_a/3)
             -1-s.pi/6))

    # Exact real curl identity at theta=pi/2, applied componentwise.
    coordinate = s.symbols('coordinate', real=True)
    amplitude = s.Function('amplitude')(coordinate)
    curl_amplitude = s.Function('curl_amplitude')(coordinate)
    theta = s.Function('theta')(coordinate)
    wavelength = s.symbols('wavelength', positive=True)
    velocity = amplitude*s.cos(theta)-wavelength*curl_amplitude*s.sin(theta)
    actual_third = s.diff(velocity, coordinate, 3).subs(
        {s.sin(theta): 1, s.cos(theta): 0})
    phase_slope = s.diff(theta, coordinate)
    expected_third = (
        amplitude*(phase_slope**3-s.diff(theta, coordinate, 3))
        -3*s.diff(amplitude, coordinate)*s.diff(theta, coordinate, 2)
        -3*s.diff(amplitude, coordinate, 2)*phase_slope
        -wavelength*s.diff(curl_amplitude, coordinate, 3)
        +3*wavelength*s.diff(curl_amplitude, coordinate)*phase_slope**2
        +3*wavelength*curl_amplitude*phase_slope*s.diff(theta, coordinate, 2))
    pin('exact-centered-third-curl-derivative', zero(actual_third-expected_third))
    pin('negative-control-third-leading-sign',
        not zero(actual_third-(expected_third-2*amplitude*phase_slope**3)))

    # All powers are pairs (h exponent, ell exponent); no floating point fits.
    def add(*powers):
        return tuple(sum(power[index] for power in powers) for index in (0, 1))

    def scale(power, factor):
        return tuple(factor*entry for entry in power)

    kh, dh = (F(3, 2), F(0)), (F(5, 4), F(0))
    ah, ray = (F(3, 2), -F(13, 8)), (F(0), F(1))
    inverse_h = (-F(1), F(0))
    leading = add(ah, scale(ray, 3), scale(kh, -3))
    pin('third-derivative-leading-powers', leading == (-F(3), F(11, 8)),
        {'h': str(leading[0]), 'ell': str(leading[1])})
    remainders = [
        add(ah, scale(inverse_h, 2), scale(kh, -1)),
        add(ah, scale(dh, -1), inverse_h, scale(kh, -1)),
        add(ah, scale(dh, -2), ray, scale(kh, -1)),
        add(kh, ah, scale(dh, -4)),
        add(ah, scale(dh, -2), scale(ray, 2), scale(kh, -1)),
        add(ah, scale(dh, -1), ray, inverse_h, scale(kh, -1)),
    ]
    expected_margins = [(F(1), -F(3)), (F(3, 4), -F(3)),
                        (F(1, 2), -F(2)), (F(1), -F(3)),
                        (F(1, 2), -F(1)), (F(3, 4), -F(2))]
    for index, (remainder, expected) in enumerate(zip(remainders, expected_margins), 1):
        margin = add(remainder, scale(leading, -1))
        pin(f'third-curl-error-margin-{index}', margin == expected and margin[0] > 0,
            {'h': str(margin[0]), 'ell': str(margin[1])})

    residual = 3*kh[0]-dh[0]/2
    packet_l2 = kh[0]+F(3, 2)*dh[0]
    high_norm = packet_l2-12*kh[0]
    pin('full-corrected-residual-exponent', residual == F(31, 8))
    pin('packet-L2-exponent', packet_l2 == F(27, 8))
    pin('packet-H12-exponent', high_norm == -F(117, 8))
    gradient_error = residual*F(19, 24)+high_norm*F(5, 24)
    velocity_error = residual*F(7, 8)+high_norm*F(1, 8)
    pin('H12-GN-gradient-positive-margin', gradient_error == F(1, 48))
    pin('H12-GN-velocity-margin', velocity_error == F(25, 16))
    pin('velocity-error-smaller-than-wavelength', velocity_error-kh[0] == F(1, 16))
    uncorrected = 2*kh[0]+dh[0]/2
    pin('negative-control-omitted-correction-fails-C1',
        uncorrected*F(19, 24)+high_norm*F(5, 24) == -F(17, 96))
    pin('principal-viscous-residual-exponent',
        F(4)-kh[0]+F(3, 2)*dh[0] == F(35, 8))
    pin('mean-viscous-residual-exponent',
        F(4)+2*kh[0]-F(3, 2)*dh[0] == F(41, 8))
    pin('harmonic-viscous-residual-exponent',
        F(4)+dh[0]/2 == F(37, 8))

    overlap_a = F(3, 10)
    R_power = F(1, 2)-overlap_a
    pin('growing-inner-overlap-exponent', R_power == F(1, 5))
    pin('weighted-inner-perturbation-smallness', F(1, 2)-R_power == overlap_a)
    pin('frozen-connection-tail-smallness', 2*R_power == F(2, 5))
    pin('outer-remainder-smallness', 1-2*overlap_a == F(2, 5))
    pin('nonlinear-history-subpower-room', F(11, 8) < 2)
    pin('initial-strain-exponent', 1-F(13, 8) == -F(5, 8))
    pin('terminal-normal-strain-exponent', F(5, 2)-F(13, 8) == F(7, 8))
    pin('terminal-tangent-strain-exponent', 3-F(13, 8) == F(11, 8))

    physical_velocity, physical_space = -F(14), -F(10)
    pin('fixed-physical-viscosity-scaling', physical_space-physical_velocity == 4)
    pin('physical-third-derivative-h-exponent',
        physical_velocity+3*physical_space+leading[0] == -47)
    pin('physical-first-derivative-h-exponent', physical_velocity+physical_space == -24)
    attenuation = (2*kh[0], -F(11, 8))
    terminal_fine = (F(0), F(11, 8))
    pin('C3-attenuation-kills-this-handover',
        add(attenuation, terminal_fine) == (F(3), F(0)))
    return rows


def main():
    rows = checks()
    source = Path(__file__)
    record = {
        'date': '2026-09-08',
        'node': 'nse-original-time-nonlinear-handover',
        'research_note': 'references/navier-stokes/original-nonlinear-handover.md',
        'evidence_class': 'EXACT_ALGEBRA_AND_EXPONENT_CONTROLS_ONLY',
        'scope': 'Original-time handover supporting identities and rational powers',
        'written_PDE_proof_separate': True,
        'PDE_theorem_certified': False,
        'growing_interval_matching_certified': False,
        'strong_existence_certified': False,
        'infinite_iteration_certified': False,
        'Lean_kernel_checked': False,
        'DNS': False,
        'ROOT': 'OPEN',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'checks_passed': sum(row['passed'] for row in rows),
        'checks_total': len(rows),
        'all_passed': all(row['passed'] for row in rows),
        'checks': rows,
    }
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0 if record['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
