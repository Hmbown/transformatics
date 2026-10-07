"""Exact profile/source controls. Run with .venv/bin/python. Not a PDE certificate."""

def check_profile_calculus():
    """Curved-phase heat/curl fixture, pressure mutation and phase moments."""
    import sympy as s
    from fractions import Fraction as R
    x, y, z, t, phase = s.symbols('x y z t phase', real=True)
    coords = (x, y, z)
    xi = s.Matrix([1, y, 0])  # grad(x + y**2/2), not a constant ray.
    b = s.Matrix([-y, 1, x])
    tau = t*(1+y*y)
    clock = 1+y*y  # q=0, epsilon=k=1: D tau=|xi|^2.
    C = -xi.cross(b)/xi.dot(xi)
    f = phase**3 + 6*tau*phase
    primitive = phase**4/4 + 3*tau*phase**2 + 3*tau**2
    # Polynomial heat solutions test local identities, not periodic mean claims.
    assert s.diff(primitive, phase) == f
    assert s.expand(s.diff(f, t)-clock*s.diff(f, phase, 2)) == 0
    def slow_curl(v):
        return s.Matrix([s.diff(v[2], y)-s.diff(v[1], z),
                         s.diff(v[0], z)-s.diff(v[2], x),
                         s.diff(v[1], x)-s.diff(v[0], y)])
    def fast_derivative(v, j):
        return s.diff(v, coords[j])+xi[j]*s.diff(v, phase)
    def physical_curl(v):
        return s.Matrix([fast_derivative(v[2], 1)-fast_derivative(v[1], 2),
                         fast_derivative(v[0], 2)-fast_derivative(v[2], 0),
                         fast_derivative(v[1], 0)-fast_derivative(v[0], 1)])
    c = slow_curl(C)
    extra = s.Matrix([s.diff(tau, v) for v in coords]).cross(C)
    wave = b*f + c*primitive + extra*s.diff(f, phase)
    exact = physical_curl(C*primitive)
    assert all(s.simplify(v)==0 for v in wave-exact)
    assert s.simplify(sum(fast_derivative(wave[j], j) for j in range(3)))==0
    incomplete = b*f+c*primitive
    bad_div = sum(fast_derivative(incomplete[j], j) for j in range(3))
    assert s.simplify(bad_div.subs({x:1,y:1,z:0,t:1,phase:1})) != 0
    # Tangent forced amplitude plus full longitudinal pressure cancels all H.
    ray=s.Matrix([1,2,3]); amp=s.Matrix([2,-1,0]); H=s.Matrix([1,0,1])
    A=s.Matrix([[1,2,3],[-1,0,1],[2,-2,-1]])
    Pi=s.eye(3)-ray*ray.T/ray.dot(ray)
    Gamp=-A*amp+2*ray*(ray.dot(A*amp))/ray.dot(ray)
    J=(2*ray.dot(A*amp)+ray.dot(H))/ray.dot(ray)
    assert Gamp-Pi*H+A*amp-ray*J == -H
    omitted=(2*ray.dot(A*amp))/ray.dot(ray)
    assert Gamp-Pi*H+A*amp-ray*omitted != -H
    # Two independent Fourier harmonics test every phase-mean stress product.
    aa, bb=s.symbols('aa bb', real=True)
    fp=aa*s.sin(phase)+bb*s.sin(2*phase)
    qp=-aa*s.cos(phase)-bb*s.cos(2*phase)/2
    fps=s.diff(fp,phase)
    avg=lambda v:s.simplify(s.integrate(s.expand_trig(v),(phase,-s.pi,s.pi))/(2*s.pi))
    M0=(aa*aa+bb*bb)/2
    assert avg(fp*qp)==0 and avg(fp*fps)==0
    assert avg(fp*fp)==M0
    assert avg(qp*qp)==(aa*aa+bb*bb/4)/2
    assert avg(fps*fps)==(aa*aa+4*bb*bb)/2
    assert avg(qp*fps)==-M0
    # Exact trace-free strain identity for real orthogonal ray/polarization.
    entries=s.symbols('a0:8')
    mat=s.Matrix([[entries[0],entries[1],entries[2]],
                  [entries[3],entries[4],entries[5]],
                  [entries[6],entries[7],-entries[0]-entries[4]]])
    normal=ray.cross(amp)
    rate=-amp.dot(mat*amp)/amp.dot(amp)-ray.dot(mat*ray)/ray.dot(ray)
    assert s.simplify(rate-normal.dot(mat*normal)/normal.dot(normal))==0
    K=R(3,2); D=R(5,4); eps=R(4)
    assert 3*K-D/2==R(31,8)
    assert eps-K+5*D/2-1==R(37,8)
    assert eps+3*D/2-1==R(39,8)
    assert eps+K-D/2==R(39,8)
    assert eps+2*K-3*D/2==R(41,8)
    assert R(31,8)*R(19,24)-R(117,8)*R(5,24)==R(1,48)
    assert R(9,4)*R(19,2)-R(117,8)==R(27,4)
    assert R(117,8)/R(19,2)==R(117,76)
    print('PASS: curved-phase heat curl, omitted-clock divergence mutation, full-pressure mutation, all phase-mean products, Kelvin strain identity, and exact scale/continuation powers.')

def check_generated_source():
    """Independent exact algebra for frozen outgoing waves; not a PDE certificate."""
    import sympy as s
    from fractions import Fraction as F
    x,y,z,t=s.symbols('x y z t', real=True)
    A,B,C,alpha,beta,eps=s.symbols('A B C alpha beta eps', positive=True)
    p=s.Matrix([1,0,0]); r=s.Matrix([0,1,0]); n=s.Matrix([0,0,1])
    xyz=s.Matrix([x,y,z])
    u1=A*s.cos(alpha*z)*p
    u2=s.cos(beta*y)*(B*p+C*n)
    u=u1+u2
    adv=u.jacobian(xyz)*u
    assert s.simplify(adv+A*C*alpha*s.sin(alpha*z)*s.cos(beta*y)*p)==s.zeros(3,1)
    assert s.simplify(sum(s.diff(adv[i],xyz[i]) for i in range(3)))==0
    # Exact Fourier Leray projection for both phases K1 +/- K2.
    K1=alpha*n; K2=beta*r
    for sigma in [1,-1]:
        K=K1+sigma*K2
        P=s.eye(3)-K*K.T/(K.dot(K))
        cross=(A*p).dot(sigma*K2)*(B*p+C*n)+(B*p+C*n).dot(K1)*(A*p)
        assert s.simplify(P*cross-A*C*alpha*p)==s.zeros(3,1)
    # Negative control: blindly retaining donor's large B in the transfer is false.
    assert s.diff(adv[0],B)==0
    # Nonlinear exact inviscid solution, with no inserted sideband.
    exact=s.Matrix([B*s.cos(beta*y)+A*s.cos(alpha*(z-C*t*s.cos(beta*y))),0,C*s.cos(beta*y)])
    assert s.simplify(exact.diff(t)+exact.jacobian(xyz)*exact)==s.zeros(3,1)
    assert s.simplify(sum(s.diff(exact[i],xyz[i]) for i in range(3)))==0
    # Full pressure-corrected geometric optics sees no amplification of p output.
    H,Pamp,Lam=s.symbols('H Pamp Lam', real=True)
    Nmat=-Lam*p*n.T-H*(n+Pamp*p)*r.T
    assert Nmat**3==s.zeros(3)
    assert s.simplify(Nmat**2-Lam*H*p*r.T)==s.zeros(3)
    for sigma in [1,-1]:
        K=K1+sigma*K2
        # p lies in kernel of the entire frozen two-shear gradient, not only B2.
        corrected=-Nmat*p+2*K*(K.dot(Nmat*p))/K.dot(K)
        assert corrected==s.zeros(3,1)
    # First donor-heat Duhamel coefficient: both parent modes use their actual heat rates.
    c1=-s.I*alpha*C*t*s.exp(-eps*(alpha**2+beta**2)*t)/2
    c0=s.exp(-eps*alpha**2*t)
    assert s.simplify(s.diff(c1,t)+eps*(alpha**2+beta**2)*c1+s.I*alpha*C*s.exp(-eps*beta**2*t)*c0/2)==0
    # Exact exponent bookkeeping in h and ell for Delta=ell^(-3/4).
    # (h exponent, ell exponent), fixed numeric |N|, |xi_2| suppressed.
    def add(*pairs): return tuple(sum(v[i] for v in pairs) for i in [0,1])
    a1=(F(1),F(1)); a2n=(F(3,2),F(7,8)); inv_h=(F(-1),F(0)); dt=(F(0),F(-3,4)); inv_k=(F(-3,2),F(0))
    zeta=add(a2n,inv_h,dt)
    first=add(a1,zeta)
    first_strain=add(first,inv_k)
    second_strain=add(a1,zeta,zeta,inv_k)
    assert zeta==(F(1,2),F(1,8))
    assert first==(F(3,2),F(9,8))
    assert first_strain==(F(0),F(9,8))
    assert second_strain==(F(1,2),F(5,4))
    assert add((F(4),F(0)),inv_k,inv_k,dt)==(F(1),F(-3,4))
    print('PASS: exact cross source, both Leray projections, B cancellation, pressure divergence, inviscid solution, nilpotent chain, p-polarization neutrality, donor-heat Duhamel coefficient, and five rational scale identities.')

def check_seed_derivatives():
    """Exact derivative/product checks; no PDE formalization."""
    import sympy as s
    from fractions import Fraction as R
    t,k=s.symbols('t k')
    b=s.Function('b')(t); dc=s.Function('dc')(t); th=s.Function('theta')(t)
    F=s.Function('F'); Q=s.Function('Q')
    q=s.diff(th,t); th2=s.diff(th,t,2); th3=s.diff(th,t,3)
    f=lambda j:s.diff(F(s.Symbol('u')),s.Symbol('u'),j).subs(s.Symbol('u'),th)
    leading=b*f(3)*q**3
    rhs=leading+3*s.diff(b,t)*f(2)*q**2+3*b*f(2)*q*th2+3*s.diff(b,t,2)*f(1)*q+3*s.diff(b,t)*f(1)*th2+b*f(1)*th3+s.diff(b,t,3)*f(0)
    assert s.simplify(s.diff(b*F(th),t,3)-rhs)==0
    rhsq=k*(s.diff(dc,t,3)*Q(th)+3*s.diff(dc,t,2)*F(th)*q+3*s.diff(dc,t)*(f(1)*q**2+F(th)*th2)+dc*(f(2)*q**3+3*f(1)*q*th2+F(th)*th3))
    # Substitute derivatives of Q with respect to its argument, retaining theta derivatives.
    lhs=s.diff(k*dc*Q(th),t,3)
    lhs=lhs.xreplace({s.Derivative(Q(th),(th,j)): f(j-1) for j in [1,2,3]})
    assert s.simplify(lhs-rhsq)==0, s.simplify(lhs-rhsq)
    # Curl lift's triple-product sign.
    xi=s.Matrix([1,2,3]); bb=s.Matrix([2,-1,0])
    assert xi.dot(bb)==0
    assert xi.cross(-xi.cross(bb)/xi.dot(xi))==bb
    # Leading relative h powers; use k=h^1.5,d=h^1.25.
    K=R(3,2); D=R(5,4)
    wave=[K-D,K-1,2*K-2*D,2*K-D-1,2*K-2,3*K-3*D]
    curl=[4*K-4*D,3*K-3*D,2*K-2*D,3*K-2*D-1,K-D,2*K-D-1,3*K-D-2]
    assert wave==[R(1,4),R(1,2),R(1,2),R(3,4),R(1),R(3,4)]
    assert curl==[R(1),R(3,4),R(1,2),R(1),R(1,4),R(3,4),R(5,4)]
    assert -14-30-2*K==-47
    print('PASS: both full third-derivative identities, curl sign, six plus seven relative h powers, physical D3 exponent.')


def check_forced_scaling_and_cutoff():
    """Physical force norms and the complete cutoff defect, with omission controls."""
    import sympy as s
    from fractions import Fraction as R
    # u=A U(As t,s x). Derive powers from the dimension/time Jacobians,
    # rather than treating the pointwise force factor as a norm factor.
    velocity_power, spatial_power = R(-14), R(-10)
    point = 2*velocity_power+spatial_power
    volume_l2 = -3*spatial_power/2
    time_l1 = -(velocity_power+spatial_power)
    assert point == -38
    assert spatial_power-velocity_power == 4  # epsilon=nu s/A.
    for r in range(4):
        for m in range(4):
            derivatives = r*spatial_power+m*(velocity_power+spatial_power)
            assert point+derivatives == -38-10*r-24*m
            assert point+derivatives+volume_l2 == -23-10*r-24*m
            assert point+derivatives+volume_l2+time_l1 == 1-10*r-24*m
    residual_l1_l2 = R(31,8)
    assert residual_l1_l2+point+volume_l2+time_l1 == R(39,8)
    assert residual_l1_l2+point+time_l1 != R(39,8)  # Missing volume.
    assert residual_l1_l2+point+volume_l2 != R(39,8)  # Missing time.
    assert R(1)-R(3,2)-4 == R(-9,2)  # Summable norm, growing pulse peaks.

    x,y,z,t,nu=s.symbols('x y z t nu', real=True)
    xyz=s.Matrix([x,y,z])
    V=s.Matrix([t*y,z,x])
    w=s.Matrix([(1+t)*x*x,-2*(1+t)*x*y,s.sin(x)])
    chi=s.Function('chi')(t)
    p0=x*y
    pi=x*z+t*y*y
    grad=lambda p:s.Matrix([s.diff(p,v) for v in xyz])
    lap=lambda u:u.applyfunc(lambda v:sum(s.diff(v,c,2) for c in xyz))
    defect=lambda u,p:u.diff(t)+u.jacobian(xyz)*u+grad(p)-nu*lap(u)
    assert s.simplify(sum(s.diff(w[j],xyz[j]) for j in range(3))) == 0
    assert s.simplify(sum(s.diff(V[j],xyz[j]) for j in range(3))) == 0
    increment=defect(V+w,p0+pi)-defect(V,p0)
    cut_increment=defect(V+chi*w,p0+chi*pi)-defect(V,p0)
    quadratic=(chi**2-chi)*w.jacobian(xyz)*w
    activation=s.diff(chi,t)*w
    expected=chi*increment+quadratic+activation
    assert all(s.simplify(v)==0 for v in cut_increment-expected)
    # This fixture has nonzero self-advection and time-dependent wave/base,
    # so either omission fails separately; an isolated linear wave would miss it.
    sample={chi:R(1,2),s.diff(chi,t):1,x:1,y:1,z:1,t:1,nu:1}
    for omitted in (quadratic,activation):
        wrong=cut_increment-(expected-omitted)
        assert any(s.simplify(v.subs(sample))!=0 for v in wrong)
    print('PASS: physical mixed force scaling, both norm-Jacobian omission controls, summable-force pulse powers, complete nonlinear cutoff identity and both cutoff omission controls.')


def check_forced_principal_heat_and_affine_core():
    """Axisymmetric/principal identities only; no complete viscous stage certificate."""
    import sympy as s
    z,r,Y,t=s.symbols('z r Y t', positive=True)
    g=s.Function('g')(z,Y)
    physical=g.subs(Y,r*r/2)
    gamma=s.diff(physical,z,2)+s.diff(physical,r,2)-s.diff(physical,r)/r
    xi=s.diff(physical,z,2)+s.diff(physical,r,2)+3*s.diff(physical,r)/r
    Lg=lambda f:s.diff(f,z,2)+2*Y*s.diff(f,Y,2)
    Lx=lambda f:Lg(f)+4*s.diff(f,Y)
    assert s.simplify(gamma-Lg(g).subs(Y,r*r/2))==0
    assert s.simplify(xi-Lx(g).subs(Y,r*r/2))==0
    assert s.simplify(xi-gamma-4*s.diff(g,Y).subs(Y,r*r/2))==0

    N=s.symbols('N', real=True)
    n=s.symbols('n', integer=True, nonzero=True)
    phase=s.Function('phase')(z,Y)
    amplitude=s.Function('amplitude')(z,Y)
    oscillation=s.exp(s.I*n*N*phase)
    wave=amplitude*oscillation
    principal=-n*n*amplitude*(s.diff(phase,z)**2+2*Y*s.diff(phase,Y)**2)
    for operator in (Lg,Lx):
        conjugated=s.expand(operator(wave)/oscillation)
        assert s.simplify(conjugated.coeff(N,2)-principal)==0
    assert s.simplify((Lx(wave)-Lg(wave))/oscillation
                     -4*(s.diff(amplitude,Y)+s.I*n*N*amplitude*s.diff(phase,Y)))==0

    # A varying matrix with noncommuting values exercises the scalar integrating
    # factor without assuming a constant or simultaneously diagonalizable host.
    M=s.Matrix([[1,t],[t,1+t*t]])
    B=s.simplify(M.diff(t)*M.inv())
    assert B.subs(t,0)*B.subs(t,1)-B.subs(t,1)*B.subs(t,0)!=s.zeros(2)
    inviscid=M*s.Matrix([2,-1])
    clock=t+t*t
    rate=s.diff(clock,t)
    viscous=s.exp(-n*n*clock)*inviscid
    assert all(s.simplify(v)==0 for v in inviscid.diff(t)-B*inviscid)
    assert all(s.simplify(v)==0 for v in viscous.diff(t)-(B-n*n*rate*s.eye(2))*viscous)
    assert inviscid[0].subs(t,1)==1 and inviscid[1].subs(t,1)==0
    assert s.simplify(viscous[1].subs(t,1))==0
    # Regression for the reviewed error: fundamental-mode damping is incorrect
    # at n=2, even though it would still leave the terminal zero component zero.
    wrong=s.exp(-clock)*inviscid
    wrong_residual=wrong.diff(t)-(B-4*rate*s.eye(2))*wrong
    assert any(s.simplify(v.subs(t,1))!=0 for v in wrong_residual)

    x,y,zz=s.symbols('x y zz', real=True)
    xyz=s.Matrix([x,y,zz])
    a=s.symbols('m0:9')
    matrix=s.Matrix(3,3,a)
    affine=matrix*xyz
    curl=lambda v:s.Matrix([s.diff(v[2],y)-s.diff(v[1],zz),
                             s.diff(v[0],zz)-s.diff(v[2],x),
                             s.diff(v[1],x)-s.diff(v[0],y)])
    assert s.simplify(curl(xyz.cross(affine))-(s.trace(matrix)*xyz-3*affine))==s.zeros(3,1)
    potential=-xyz.cross(affine)/3
    trace_free={a[8]:-a[0]-a[4]}
    assert s.simplify((curl(potential)-affine).subs(trace_free))==s.zeros(3,1)
    assert s.simplify((curl(-potential)-affine).subs(trace_free))!=s.zeros(3,1)
    print('PASS: both exact cylindrical-to-volume operators, shared all-mode principal diffusion, surviving drift, noncommuting-host heat return, missing-n2 regression, and trace-free affine curl sign/factor.')


if __name__ == '__main__':
    check_profile_calculus()
    check_generated_source()
    check_seed_derivatives()
    check_forced_scaling_and_cutoff()
    check_forced_principal_heat_and_affine_core()
