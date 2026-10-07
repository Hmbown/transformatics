"""Exact coupled-stage residuals and omission controls, not fluid simulation."""

import sympy as s

x, y, z = s.symbols("x y z", real=True)
lam, nu, k, l, m = s.symbols("lam nu k l m", positive=True)
a, b, c = s.symbols("a b c", real=True)
xyz = [x, y, z]
host = s.Matrix([lam*x, 2*lam*y, -3*lam*z])
host_pressure = -lam**2*(x*x+4*y*y+9*z*z)/2


def residual(u, pressure, rates):
    time = sum((u.diff(v)*rate for v, rate in rates.items()), s.zeros(3, 1))
    lap = sum((u.diff(v, 2) for v in xyz), s.zeros(3, 1))
    gradp = s.Matrix([s.diff(pressure, v) for v in xyz])
    return (time+u.jacobian(xyz)*u+gradp-nu*lap).applyfunc(s.simplify)


def curl(v):
    return s.Matrix([s.diff(v[2], y)-s.diff(v[1], z),
                     s.diff(v[0], z)-s.diff(v[2], x),
                     s.diff(v[1], x)-s.diff(v[0], y)])


def reverse_pair():
    u = host+s.Matrix([b*s.sin(l*z), 0, a*s.sin(k*x)])
    rates = {a:(3*lam-nu*k*k)*a, b:(-lam-nu*l*l)*b,
             k:-lam*k, l:3*lam*l}
    interaction_pressure = 2*a*b*k*l*s.cos(k*x)*s.cos(l*z)/(k*k+l*l)
    f = residual(u, host_pressure+interaction_pressure, rates)
    delta = (l*l-k*k)/(k*k+l*l)
    expected = a*b*delta*s.Matrix([l*s.sin(k*x)*s.cos(l*z), 0,
                                   -k*s.cos(k*x)*s.sin(l*z)])
    assert all(s.simplify(t)==0 for t in f-expected)
    omega_force = curl(f).applyfunc(s.simplify)
    assert s.simplify(omega_force[1]-a*b*(k*k-l*l)*s.sin(k*x)*s.sin(l*z))==0
    assert f.subs(l,k)==s.zeros(3,1)
    derivative = sum(s.diff(omega_force[1],v)*rate for v,rate in rates.items())
    assert s.simplify(derivative.subs(l,k)
        +8*lam*a*b*k*k*s.sin(k*x)*s.sin(k*z))==0
    # Equal frequency cancels the force only instantaneously, not its time jet.
    assert s.simplify(derivative.subs({a:1,b:1,lam:1,k:1,l:1,x:s.pi/2,z:s.pi/2}))==-8
    print("PASS: reverse-pair full pressure, residual and resonance time-derivative obstruction")


def three_cycle():
    v = s.Matrix([c*s.sin(m*y), b*s.sin(l*z), a*s.sin(k*x)])
    rates = {a:(3*lam-nu*k*k)*a, b:(-2*lam-nu*l*l)*b,
             c:(-lam-nu*m*m)*c, k:-lam*k,l:3*lam*l,m:-2*lam*m}
    f = residual(host+v, host_pressure, rates)
    expected = s.Matrix([b*c*m*s.sin(l*z)*s.cos(m*y),
                         a*b*l*s.sin(k*x)*s.cos(l*z),
                         a*c*k*s.sin(m*y)*s.cos(k*x)])
    assert all(s.simplify(t)==0 for t in f-expected)
    assert s.simplify(sum(s.diff(f[i],coord) for i,coord in enumerate(xyz)))==0
    matrix = v.jacobian(xyz).subs({x:0,y:0,z:0})
    assert f.jacobian(xyz).subs({x:0,y:0,z:0})==matrix**2
    spectral = s.symbols("spectral")
    B = s.diag(lam,2*lam,-3*lam)+matrix
    product = a*b*c*k*l*m
    assert s.expand(B.charpoly(spectral).as_expr()
        -((spectral-lam)*(spectral-2*lam)*(spectral+3*lam)-product))==0
    derivative = sum(s.diff(product,vv)*rate for vv,rate in rates.items())
    assert s.simplify(derivative+nu*(k*k+l*l+m*m)*product)==0
    potential = s.Matrix([-b/l*s.cos(l*z),-a/k*s.cos(k*x),-c/m*s.cos(m*y)])
    assert curl(potential)==v
    # Unlike the reverse pair, matching all three frequencies does not remove feedback.
    assert f.subs({a:1,b:1,c:1,k:1,l:1,m:1,x:0,y:s.pi/2,z:0})==s.Matrix([0,0,1])
    # Exact products used in the three circulation bounds and their geometric mean.
    assert s.expand((a*c*k)*(a*b*l)*(b*c*m)-(a*b*c)*product)==0
    print("PASS: genuine three-cycle residual, reverse edges, spectral product and missing-feedback control")


if __name__ == "__main__":
    reverse_pair()
    three_cycle()
    print("Exact finite algebra only; no analytic PDE certification or Navier–Stokes solution claim.")
