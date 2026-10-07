"""Exact source, correction and frequency-scale controls; no fluid simulation.

The analytic estimates and their quantifiers live in the companion notes.
These checks include omitted-pressure and omitted-mean-advection controls.
"""

import sympy as s


def source_pressure_and_parity():
    p, q, mass = s.symbols("p q mass", positive=True)
    r = s.symbols("r", real=True)
    K = s.Matrix([p, q, r])
    eb, en = s.eye(3)[:, 0], s.eye(3)[:, 1]
    projection = s.eye(3) - K * K.T / K.dot(K)
    stress = mass * eb * eb.T
    normal = (en.T * projection * stress * K)[0]
    signed_source = s.simplify(s.im(-s.I * normal))
    assert s.simplify(signed_source - mass * p**2 * q / K.dot(K)) == 0
    assert signed_source.is_positive is True
    # Without pressure, this normal component disappears entirely.
    assert (en.T * stress * K)[0] == 0
    # A positive imaginary coefficient has a negative real normal derivative.
    coefficient = s.I * mass
    assert s.re(s.I * q * coefficient) == -q * mass
    y = s.symbols("y", real=True)
    f, g = -s.sin(q*y), s.cos(q*y)/q
    assert s.simplify(s.diff(g, y)-f) == 0
    print("PASS: full pressure sign, omission control and probe parity")


def complete_quadratic_remainder():
    # Noncommuting products stand for the ordered bilinear map (u.grad)v.
    m, z, dm, w = s.symbols("m z dm w", commutative=False)
    expansion = s.expand((m+z+dm+w)**2-(m+z)**2)
    prescribed = (m*dm+dm*m+z*dm+dm*z+z*w+w*z
                  +m*w+w*m+(dm+w)**2)
    assert s.expand(expansion-prescribed) == 0
    slow, fast, curl = s.symbols("slow fast curl", commutative=False)
    # dm.grad Z contains a principal fast term which must be in H_j.
    expanded = expansion.subs(dm*z, slow+fast+curl)
    corrected = s.expand(expanded-fast)
    expected = s.expand(prescribed).subs(dm*z, slow+curl)
    assert s.expand(corrected-expected) == 0
    assert s.expand(expanded-expected) == fast
    # Tangent/tangent principal products vanish, but a normal mean need not.
    a1, a2, c1, c2, n1, n2, n3 = s.symbols("a1 a2 c1 c2 n1 n2 n3")
    xi = s.Matrix([0, 0, 1])
    a, c = s.Matrix([a1,a2,0]), s.Matrix([c1,c2,0])
    mean = s.Matrix([n1,n2,n3])
    assert xi.dot(a) == xi.dot(c) == 0
    assert xi.dot(mean) == n3
    print("PASS: all ordered quadratic terms and normal-mean omission control")


def scale_and_tail_powers():
    F = s.Rational
    k, d, epsilon = F(3,2), F(5,4), F(4)
    rho = k-d
    J, order, beta = s.symbols("J order beta")
    residual = k+(J+1)*rho+F(3,2)*d
    assert s.simplify(residual-(29+2*J)/8) == 0
    h12 = k+F(3,2)*d-12*k
    assert h12 == -F(117,8)
    gradient = s.expand(F(19,24)*residual+F(5,24)*h12)
    h3 = s.expand(F(3,4)*residual+F(1,4)*h12)
    assert s.simplify(gradient-(19*J-17)/96) == 0
    assert s.simplify(h3-(3*J-15)/16) == 0
    assert gradient.subs(J,1) == F(1,48)
    assert gradient.subs(J,3) == F(5,12)
    for cost in [rho, epsilon-2*k, epsilon-k-d, epsilon-2*d]:
        assert cost >= rho
    stress = 2*k+3*d
    assert stress == F(27,4)
    assert k+3*d+12*rho == F(33,4)
    assert F(5,2)-24+24*d == F(17,2)
    assert 7-stress == F(1,4)
    assert 7+stress-d == F(25,2)
    assert 7+stress-4*d == F(35,4)
    assert 7+stress-5*d == F(15,2)
    assert stress-4*d == F(7,4)  # fixed-time proposed source scale
    assert stress-5*d == F(1,2)
    assert epsilon-2*d+7 == F(17,2)
    assert residual.subs(J,12) < stress < residual.subs(J,13)
    tail = s.expand((order-F(5,2))*beta+k+F(3,2)*d-order*k)
    assert s.simplify(tail-(order*(beta-F(3,2))+F(27,8)-F(5,2)*beta)) == 0
    assert tail.subs(beta,F(3,2)) == -F(3,8)
    assert s.diff(tail,order).subs(beta,F(151,100)) > 0
    for fixed_beta in [F(1501,1000),F(7,4),F(9,4)]:
        target = F(2)
        fixed_order = max(12, int(s.ceiling(
            (target+2-F(27,8)+F(5,2)*fixed_beta)/(fixed_beta-F(3,2))))+1)
        assert tail.subs({order:fixed_order,beta:fixed_beta}) > target+2
    print("PASS: source, finite-depth, physical diffusion and finer-tail powers")


def forced_inheritance_residual():
    t, lam, nu, K, L, a0, b0 = s.symbols(
        "t lam nu K L a0 b0", positive=True)
    d1 = nu*K**2*(1-s.exp(-2*lam*t))/(2*lam)
    dr = nu*L**2*(1-s.exp(-4*lam*t))/(4*lam)
    kap, freq = K*s.exp(-lam*t), L*s.exp(-2*lam*t)
    aa = a0*s.exp(3*lam*t-d1)
    bb = b0*s.exp(-lam*t-dr)
    cc = -b0*a0*K/(2*lam)*(1-s.exp(-2*lam*t))*s.exp(3*lam*t-d1-dr)
    assert s.simplify(s.diff(cc,t)-(3*lam-nu*(kap**2+freq**2))*cc+bb*aa*kap) == 0
    assert s.simplify(cc/bb+aa*kap*(s.exp(2*lam*t)-1)/(2*lam)) == 0

    x,y,z = s.symbols("x y z", real=True)
    a,b,c,k,l = s.symbols("a b c k l", real=True)
    u = s.Matrix([lam*x+b*s.sin(l*y), 2*lam*y,
        -3*lam*z+a*s.sin(k*x)+c*s.cos(k*x)*s.sin(l*y)])
    rates = {a:(3*lam-nu*k**2)*a, b:(-lam-nu*l**2)*b,
        c:(3*lam-nu*(k**2+l**2))*c-b*a*k,
        k:-lam*k, l:-2*lam*l}
    dt = sum((u.diff(v)*rate for v,rate in rates.items()), s.zeros(3,1))
    lap = sum((u.diff(v,2) for v in [x,y,z]), s.zeros(3,1))
    pressure_gradient = s.Matrix([-lam**2*x,-4*lam**2*y,-9*lam**2*z])
    residual = dt+u.jacobian([x,y,z])*u+pressure_gradient-nu*lap
    expected = s.Matrix([0,0,-b*c*k*s.sin(k*x)*s.sin(l*y)**2])
    assert all(s.simplify(v)==0 for v in residual-expected)
    assert s.simplify(sum(s.diff(u[i],v) for i,v in enumerate([x,y,z]))) == 0
    # Keeping only the linearized equations would miss this actual force.
    assert expected.subs({b:1,c:1,k:1,l:1,x:s.pi/2,y:s.pi/2}) == s.Matrix([0,0,-1])
    amp = s.symbols("amp", positive=True)
    assert s.expand((amp-a)*(amp+a)-(amp**2-a**2)) == 0
    print("PASS: exact finite-wave descendant, nonlinear force and omitted-feedback control")


if __name__ == "__main__":
    source_pressure_and_parity()
    complete_quadratic_remainder()
    scale_and_tail_powers()
    forced_inheritance_residual()
    print("Finite exact algebra only; not a PDE or Navier–Stokes certificate.")
