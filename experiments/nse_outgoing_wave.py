"""Exact controls for outgoing-shear polarization and secondary-wave scales.

These finite algebra checks do not certify a linearized PDE estimate, a
nonlinear second stage, compatible initial seeds, or global Navier--Stokes.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
R = s.Rational


def simplify(v):
    return v.applyfunc(s.simplify) if isinstance(v, s.MatrixBase) else s.simplify(v)


def shear_polarization(p, q, r, sigma, b20, b30, t):
    """Exact undamped solution; p=0 is handled without division by p."""
    p, q, r, sigma, b20, b30 = map(s.sympify, (p, q, r, sigma, b20, b30))
    xi = s.Matrix([p, q, r-sigma*p*t])
    if p == 0:
        if q*q+r*r == 0:
            raise ValueError('covector must be nonzero')
        if s.simplify(q*b20+r*b30) != 0:
            raise ValueError('returning-plane polarization must be tangent')
        # Select initial streamwise component zero for this branch.
        return xi, s.Matrix([-sigma*t*b30, b20, b30])
    k2 = p*p+q*q
    kappa = s.sqrt(k2)
    zeta = xi[2]
    def J(z):
        return z/(2*k2*(k2+z*z))+s.atan(z/kappa)/(2*kappa**3)
    C = b30*(k2+r*r)
    b3 = C/(k2+zeta*zeta)
    b2 = b20-2*q*C*(J(zeta)-J(r))
    b1 = -(q*b2+zeta*b3)/p
    return xi, s.Matrix([b1, b2, b3])


def principal_rhs(A, xi, b, pressure_factor=2):
    return -A*b+pressure_factor*xi*xi.dot(A*b)/xi.dot(xi)


def cell_error_exponent(r, sobolev_order):
    # h^r D^r e/(h ell), using L2 h^(11/4) and Hs h^(7/4-s).
    weight = R(2*r+3, 2*sobolev_order)
    return s.simplify(R(11,4)*(1-weight)+(R(7,4)-sobolev_order)*weight+r-1)


def checks():
    rows=[]
    def pin(name, ok):
        rows.append({'name':name,'passed':bool(ok)})
    t=s.symbols('t', real=True)
    for p,q,r,sigma,b20,b30 in [(1,2,3,2,-1,1),(-2,1,1,-3,2,1),(2,0,3,1,0,2)]:
        xi,b=shear_polarization(p,q,r,sigma,b20,b30,t)
        A=s.zeros(3);A[0,2]=sigma
        tag=f'{p}-{q}-{r}-{sigma}'
        pin('covector-'+tag,simplify(xi.diff(t)+A.T*xi)==s.zeros(3,1))
        pin('pressure-polarization-'+tag,simplify(b.diff(t)-principal_rhs(A,xi,b))==s.zeros(3,1))
        pin('transversality-'+tag,simplify(xi.dot(b))==0)
        pin('b3-K-invariant-'+tag,simplify(b[2]*xi.dot(xi)-b30*(p*p+q*q+r*r))==0)
        pin('pressure-factor-negative-'+tag,simplify((b.diff(t)-principal_rhs(A,xi,b,1)).subs(t,0))!=s.zeros(3,1))
    xi,b=shear_polarization(0,3,4,2,-4,3,t)
    A=s.zeros(3);A[0,2]=2
    pin('returning-Jordan-lift-up',simplify(b.diff(t)-principal_rhs(A,xi,b))==s.zeros(3,1))
    xi,b=shear_polarization(0,0,1,2,1,0,t)
    pin('normal-covector-no-gain',b==s.Matrix([0,1,0]))
    sigma,gamma,z=s.symbols('sigma gamma z', positive=True)
    E=s.zeros(3);E[0,2]=sigma
    pin('nilpotent-gradient',E*E==s.zeros(3))
    pin('unipotent-propagator',(s.eye(3)-t*E).det()==1)
    tilt=E.copy();tilt[2,0]=gamma
    receiver=s.Matrix([0,1,0])
    pin('cross-shear-covector-returns',tilt.T*receiver==s.zeros(3,1))
    block=(-tilt).extract([0,2],[0,2])
    pin('bounded-cross-shear-can-change-exponents',s.factor((z*s.eye(2)-block).det())==z*z-sigma*gamma)
    for order in range(1,6):
        pin(f'cell-derivative-{order}-margin-H32',cell_error_exponent(order,32)>0)
    pin('H12-not-enough-for-cell-C5',cell_error_exponent(5,12)<0)
    h=s.symbols('h', positive=True)
    wavelength,width,epsilon=h**R(3,2),h**R(5,4),h**4
    powers={
        'coherence':width/h,
        'curl-envelope':wavelength/width,
        'viscous-principal':epsilon/wavelength**2,
        'viscous-cross':epsilon/(wavelength*width),
        'viscous-envelope':epsilon/width**2,
        'viscous-curl':epsilon*wavelength/width**3,
    }
    expected={'coherence':R(1,4),'curl-envelope':R(1,4),'viscous-principal':1,
              'viscous-cross':R(5,4),'viscous-envelope':R(3,2),'viscous-curl':R(7,4)}
    for name,v in powers.items():pin(name+'-power',s.simplify(v/h**expected[name])==1)
    lam=s.symbols('lam',positive=True);d=lam**(-R(3,4))
    pin('transient-gain-scale',s.simplify(lam*d-lam**R(1,4))==0)
    pin('transient-bootstrap-smallness',s.limit(d+lam*d*d,lam,s.oo)==0)
    pin('transient-not-an-exponential-return',s.limit((lam*d*d)/(lam*d),lam,s.oo)==0)
    return rows


def main():
    rows=checks()
    record={'date':'2026-09-08','node':'nse-outgoing-wave-linearized',
        'ROOT':'OPEN','E_prime':'OPEN','evidence_class':'EXACT_ALGEBRA_ONLY',
        'research_note':'references/navier-stokes/outgoing-wave.md',
        'PDE_theorem_certified':False,'nonlinear_second_stage':False,
        'time_zero_seed_compatibility':False,'lean_kernel_checked':False,'DNS':False,
        'checks':rows,'all_green':all(r['passed'] for r in rows),
        'scope':'Exact shear and scale controls only. The separate written proof must justify actual-background coefficients, localized viscous comparison, real normalization and high-pass gain. No global theorem or next-seed supply is certified.'}
    out=ROOT/'artifacts/enstrophy_sup/nse_outgoing_wave.json'
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'checks':len(rows),'all_green':record['all_green']}))
    return 0 if record['all_green'] else 1

if __name__=='__main__':raise SystemExit(main())
