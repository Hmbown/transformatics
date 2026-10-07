"""Physical-space controls independent of the sparse Fourier implementation."""
import json
from pathlib import Path
import sympy as s
import pytest
from experiments.nse_wave_handover import (energy_witness, mean_witness,
                                          divergence, norm2, checks)

x, z = s.symbols('x z', real=True)


def average_xz(f):
    return s.simplify(s.integrate(s.integrate(s.expand_trig(f),
                      (x,0,2*s.pi)), (z,0,2*s.pi))/(4*s.pi**2))


def test_direct_physical_energy_pairing_and_dissipation():
    m, n, a = 1, 5, s.Rational(3,7)
    e = s.Matrix([s.sin(m*x)*s.sin(n*z),0,
                  s.sin(m*x)+s.Rational(m,n)*s.cos(m*x)*s.cos(n*z)])
    W = s.Matrix([a*s.cos(n*z),0,0])
    assert s.simplify(s.diff(e[0],x)+s.diff(e[2],z)) == 0
    production = -e.dot(s.diff(W,z)*e[2])
    direct = average_xz(production)
    mass = average_xz(e.dot(e))
    diss = average_xz(s.diff(e,x).dot(s.diff(e,x))+
                      s.diff(e,z).dot(s.diff(e,z)))
    _, _, got, got_mass, got_diss = energy_witness(m,n,a)
    assert (direct,mass,diss) == (got,got_mass,got_diss)
    # Solenoidality does not remove longitudinal slow velocity.
    assert average_xz(e[2]**2) > 0


def test_generated_normal_mean_from_direct_pressure_poisson_equation():
    y = s.symbols('y', real=True)
    m = 2
    a = s.Rational(3,7)
    p0 = s.cos(m*z)**2*s.sin(m*x)*s.sin(m*y)
    raw = a*a/2*s.Matrix([s.diff(p0,x),s.diff(p0,y),0])
    p = -a*a*(s.Rational(1,4)+s.cos(2*m*z)/12)*s.sin(m*x)*s.sin(m*y)
    lap = sum(s.diff(p,v,2) for v in (x,y,z))
    div_raw = sum(s.diff(raw[i],v) for i,v in enumerate((x,y,z)))
    assert s.trigsimp(lap+div_raw) == 0
    force = -raw-s.Matrix([s.diff(p,v) for v in (x,y,z)])
    expected = -a*a*m/6*s.sin(m*x)*s.sin(m*y)*s.sin(2*m*z)
    assert s.trigsimp(force[2]-expected) == 0
    assert force[2] != 0 and raw[2] == 0  # Dropping pressure destroys this effect.
    for n in (10,13):
        w, _, low, expected_fourier = mean_witness(m,n,a)
        assert not divergence(w)
        assert low[2] == expected_fourier
        assert norm2(low) > 0


def test_exact_viscous_shear_is_an_unforced_background():
    t, a, nu = s.symbols('t a nu', positive=True)
    n=5
    W=a*s.exp(-nu*n*n*t)*s.cos(n*z)
    assert s.simplify(s.diff(W,t)-nu*s.diff(W,z,2)) == 0
    assert s.diff(W,x) == 0  # W dot grad W vanishes exactly.


def test_asymptotic_stability_obstruction_keeps_viscosity():
    q=s.symbols('q',positive=True)
    n,m,a,eps=q**4,q**2,q**-3,q**-16
    rate=(a*n-eps*(n*n+4*m*m+m**4/n**2))/(3+(m/n)**2)
    assert s.limit(rate/q,q,s.oo)==s.Rational(1,3)
    assert s.limit(a*m,q,s.oo)==0
    assert s.limit(eps*n*n,q,s.oo)==0
    assert s.limit(rate/(a*m),q,s.oo)==s.oo


def test_support_hypotheses_and_receipt_scope():
    with pytest.raises(ValueError):
        mean_witness(2,5)
    with pytest.raises(ValueError):
        energy_witness(5,2)
    rows=checks()
    assert all(r['passed'] for r in rows)
    saved=json.loads((Path(__file__).parents[1]/'artifacts/enstrophy_sup/nse_wave_handover.json').read_text())
    assert saved['checks']==rows
    assert saved['ROOT']=='OPEN'
    assert 'no cascade' in saved['scope']
