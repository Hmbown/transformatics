"""Exact Fourier controls for single-phase forcing and a stability obstruction.

These periodic, finite-mode identities are not a cascade or a PDE error theorem.
The affine-energy witness is an embedded globally regular two-dimensional flow.
The generated-mean witness is a full-NS initial derivative, not a completed stage.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
Q = sp.Rational
I = sp.I


def clean(f):
    return {k: sp.simplify(v) for k, v in f.items() if sp.simplify(v) != 0}


def add(*fs):
    out = {}
    for f in fs:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def scale(f, a):
    return clean({k: a * v for k, v in f.items()})


def mul(f, g):
    out = {}
    for k, v in f.items():
        for l, w in g.items():
            n = tuple(k[j] + l[j] for j in range(3))
            out[n] = out.get(n, 0) + v * w
    return clean(out)


def trig(axis, n, sine=False):
    k = tuple(n if j == axis else 0 for j in range(3))
    neg = tuple(-v for v in k)
    return {k: 1 / (2 * I) if sine else Q(1, 2),
            neg: -1 / (2 * I) if sine else Q(1, 2)}


def deriv(f, axis):
    return clean({k: I * k[axis] * v for k, v in f.items()})


def divergence(u):
    return add(*(deriv(u[j], j) for j in range(3)))


def advect(u, v):
    return tuple(add(*(mul(u[j], deriv(v[i], j)) for j in range(3)))
                 for i in range(3))


def leray(u):
    keys = set().union(*(f.keys() for f in u))
    out = ({}, {}, {})
    for k in keys:
        v = [u[j].get(k, 0) for j in range(3)]
        kk = sum(x*x for x in k)
        kv = sum(k[j]*v[j] for j in range(3))
        for j in range(3):
            out[j][k] = v[j] if not kk else v[j] - Q(k[j], kk)*kv
    return tuple(clean(f) for f in out)


def inner(u, v):
    return sp.simplify(sum(sp.conjugate(c)*v[j].get(k, 0)
                           for j in range(3) for k, c in u[j].items()))


def norm2(u):
    return inner(u, u)


def grad_norm2(u):
    return sp.simplify(sum(sum(x*x for x in k)*sp.conjugate(v)*v
                           for f in u for k, v in f.items()))


def lowpass(u, radius):
    return tuple({k: v for k, v in f.items()
                  if sum(x*x for x in k) <= radius*radius} for f in u)


def is_real(u):
    return all(sp.simplify(f.get(tuple(-v for v in k), 0)-sp.conjugate(c)) == 0
               for f in u for k, c in f.items())


def energy_witness(m, n, a=sp.Integer(1)):
    if not (0 < m < n):
        raise ValueError('need integer 0 < m < n')
    a = sp.sympify(a)
    W = (scale(trig(2, n), a), {}, {})
    e = (mul(trig(0, m, True), trig(2, n, True)), {},
         add(trig(0, m, True), scale(mul(trig(0, m), trig(2, n)), Q(m, n))))
    prod = -inner(e, advect(e, W))
    return W, e, sp.simplify(prod), norm2(e), grad_norm2(e)


def mean_witness(m, n, a=sp.Integer(1)):
    if not (m > 0 and n >= 5*m):
        raise ValueError('need integers m > 0 and n >= 5m')
    a = sp.sympify(a)
    f = trig(2, m)
    b = (mul(f, trig(1, m)), scale(mul(f, trig(0, m)), -1), {})
    w = tuple(scale(mul(v, trig(2, n)), a) for v in b)
    raw = advect(w, w)
    force = tuple(scale(v, -1) for v in leray(raw))
    low = lowpass(force, 3*m)
    expected_z = scale(mul(mul(trig(0, m, True), trig(1, m, True)),
                           trig(2, 2*m, True)), -a*a*m/6)
    return w, raw, low, expected_z


def checks():
    rows = []
    def pin(name, truth):
        rows.append({'name': name, 'passed': bool(truth)})
    for m, n, a in [(1, 5, sp.Integer(1)), (2, 13, Q(3, 7))]:
        W, e, prod, mass, diss = energy_witness(m, n, a)
        tag = f'{m}-{n}'
        pin('real-solenoidal-'+tag, is_real(W) and is_real(e)
            and not divergence(W) and not divergence(e))
        pin('zero-mean-'+tag, all(f.get((0,0,0), 0) == 0 for f in W+e))
        pin('zero-self-interaction-'+tag, all(not f for f in advect(W, W)))
        pin('energy-production-'+tag, prod == a*n/4)
        pin('error-mass-'+tag, mass == (3+Q(m*m,n*n))/4)
        pin('error-dissipation-'+tag, diss == m*m+Q(n*n,4)+Q(m**4,4*n*n))
        pin('pressure-energy-invariance-'+tag, inner(e, leray(advect(e,W))) == -prod)
        w, raw, low, expected = mean_witness(m, n, a)
        pin('mean-datum-solenoidal-'+tag, is_real(w) and not divergence(w))
        pin('no-initial-low-modes-'+tag, all(not f for f in lowpass(w,3*m)))
        pin('generated-normal-mean-'+tag, clean(add(low[2],scale(expected,-1))) == {} and bool(low[2]))
        pin('unprojected-normal-zero-'+tag, not raw[2])
        pin('projected-mean-solenoidal-'+tag, not divergence(low))
    # Exact scale family: N=q^4, M=q^2, a=q^-3, epsilon=q^-16.
    # h << a << delta, but instantaneous log-norm growth is ~q/3.
    for q in (2, 3, 5):
        n, m, a, eps = q**4, q**2, Q(1,q**3), Q(1,q**16)
        rate = (a*n-eps*(n*n+4*m*m+Q(m**4,n*n)))/(3+Q(m*m,n*n))
        pin(f'viscous-growth-positive-{q}', rate > 0)
        pin(f'growth-exceeds-envelope-{q}', rate > a*m)
    return rows


def main():
    rows = checks()
    if not all(r['passed'] for r in rows):
        raise AssertionError([r for r in rows if not r['passed']])
    receipt = {
        'date':'2026-09-08',
        'scope':'Exact periodic Fourier identities and restricted failure of a generic envelope-only L2 stability bound; no cascade, completed handover or global NS result.',
        'method':'Symbolic sparse Fourier convolution, exact Leray multiplier and Parseval pairings; no sampled grid or DNS.',
        'checks':rows,
        'energy_formula': '(a*N-epsilon*(N^2+4*M^2+M^4/N^2))/(3+(M/N)^2)',
        'normal_mean_formula':'-(a^2*M/6)*sin(M*x)*sin(M*y)*sin(2*M*z)',
        'ROOT':'OPEN',
    }
    path=ROOT/'artifacts/enstrophy_sup/nse_wave_handover.json'
    path.write_text(json.dumps(receipt,indent=2)+'\n')
    print(f'{len(rows)} exact checks passed; {path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
