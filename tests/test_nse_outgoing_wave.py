"""Independent exact controls for the finite outgoing-wave calculation."""
from functools import lru_cache
from pathlib import Path
import json
import pytest
import sympy as s
from experiments.nse_outgoing_wave import shear_polarization, cell_error_exponent, checks

R=s.Rational


def zero(v):
    return all(s.simplify(x)==0 for x in v) if isinstance(v,s.MatrixBase) else s.simplify(v)==0


@lru_cache(maxsize=1)
def viscous_affine_fixture():
    x,y,z,t=s.symbols('x y z t',real=True)
    eps,k=s.symbols('eps k',positive=True)
    X=(x,y,z);position=s.Matrix(X)
    xi,b=shear_polarization(1,1,1,2,-1,1,t)
    A=s.zeros(3);A[0,2]=2;U=A*position
    # Directly integrate the time-dependent squared covector, retaining
    # viscosity instead of treating this as an undamped NS solution.
    action=3*t-2*t*t+R(4,3)*t**3
    damping=s.exp(-eps*action/k**2)
    plane=s.exp(s.I*xi.dot(position)/k)
    v=damping*b*plane
    pressure=2*s.I*k*xi.dot(A*(damping*b))/xi.dot(xi)*plane
    lap=v.applyfunc(lambda f:sum(s.diff(f,a,2) for a in X))
    actual=v.diff(t)+v.jacobian(X)*U+A*v
    actual+=s.Matrix([s.diff(pressure,a) for a in X])-eps*lap
    return X,t,eps,k,xi,b,A,v,pressure,action,actual/(damping*plane)


def test_complete_viscous_plane_wave_by_direct_PDE_differentiation():
    *_,actual=viscous_affine_fixture()
    assert zero(actual)


def test_actual_linear_pressure_poisson_and_divergence():
    X,_,_,_,_,_,A,v,pressure,_,_=viscous_affine_fixture()
    assert zero(sum(s.diff(v[i],a) for i,a in enumerate(X)))
    lap=sum(s.diff(pressure,a,2) for a in X)
    assert zero(lap+2*s.trace(A*v.jacobian(X)))
    # A constant background gradient is local and unbounded on R3; this
    # operator check does not claim an admissible periodic base flow.


def test_viscous_attenuation_uses_the_whole_covector_history():
    _,t,_,_,xi,_,_,_,_,action,_=viscous_affine_fixture()
    assert s.expand(s.diff(action,t)-xi.dot(xi))==0
    assert s.expand(action-xi.subs(t,0).dot(xi.subs(t,0))*t)!=0


def test_returning_plane_jordan_map_from_an_independent_basis():
    t=s.symbols('t',real=True)
    A=s.zeros(3);A[0,2]=3
    basis=s.Matrix.hstack(s.Matrix([1,0,0]),s.Matrix([0,-R(4,5),R(3,5)]))
    xi=s.Matrix([0,3,4])
    transport=s.eye(3)-t*A
    assert zero(basis.T*basis-s.eye(2))
    assert zero(xi.T*basis)
    restriction=s.simplify(basis.T*transport*basis)
    assert restriction==s.Matrix([[1,-R(9,5)*t],[0,1]])
    assert restriction.eigenvals()=={s.Integer(1):2}
    assert s.simplify((transport*basis[:,1]).dot(transport*basis[:,1])-1)==R(81,25)*t*t
    assert zero((s.eye(3)-t*A)*(s.eye(3)-2*t*A)-(s.eye(3)-3*t*A))


def test_higher_sobolev_bookkeeping_is_needed_for_cell_coefficients():
    for r in range(1,6):
        theta=R(2*r+3,64)
        direct=R(11,4)*(1-theta)+(R(7,4)-32)*theta+r-1
        assert direct==cell_error_exponent(r,32)>0
    assert cell_error_exponent(5,12)<0
    assert cell_error_exponent(7,32)<0  # Not an arbitrary-derivative certificate.


def test_two_signed_real_lobes_need_separate_normalization():
    # Fourier dictionaries on one periodic axis: complex carrier plus a
    # small low-frequency component, and its independently formed real part.
    eta=R(1,10);k=R(1,2);center=s.Integer(5);cut=s.Integer(2)
    packet={10:s.Integer(1),1:eta}
    real={10:R(1,2),-10:R(1,2),1:eta/2,-1:eta/2}
    def mass(f,low=False):
        return sum(abs(c)**2 for mode,c in f.items() if not low or abs(mode)<=cut)
    moment=sum((k*mode-center)**2*abs(c)**2 for mode,c in packet.items())
    assert mass(real,True)<=mass(packet,True)<=moment/(center-k*cut)**2
    assert mass(real)==mass(packet)/2
    real_moment=sum((k*mode-center)**2*abs(c)**2 for mode,c in real.items())
    assert real_moment>25  # The one-center moment is useless on the negative lobe.


def test_covector_hypotheses_and_saved_receipt_scope():
    t=s.symbols('t')
    with pytest.raises(ValueError):shear_polarization(0,0,0,1,0,0,t)
    with pytest.raises(ValueError):shear_polarization(0,1,1,1,1,1,t)
    rows=checks();assert all(row['passed'] for row in rows)
    record=json.loads((Path(__file__).parents[1]/'artifacts/enstrophy_sup/nse_outgoing_wave.json').read_text())
    assert record['checks']==rows
    assert record['ROOT']=='OPEN' and record['evidence_class']=='EXACT_ALGEBRA_ONLY'
    for key in ['PDE_theorem_certified','nonlinear_second_stage','time_zero_seed_compatibility','lean_kernel_checked','DNS']:
        assert record[key] is False
