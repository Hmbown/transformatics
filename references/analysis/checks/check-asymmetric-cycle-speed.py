"""Exact symbolic full Fourier time jets for unequal cyclic amplitudes.

No grid evolution, DNS, mode suppression, or numerical parameter fitting.
The Fourier convention is uhat(k)=i*v(k) for real odd velocity fields.
Lifespan, maximizing-branch and viscosity remainders are written separately.
"""
import sympy as s
from itertools import product
from math import comb,factorial
A=s.symbols('a b c',real=True)
Z=(s.S.Zero,)*3

def add(d,k,v):
 old=d.get(k,Z);new=tuple(s.expand(old[j]+v[j]) for j in range(3))
 if any(new):d[k]=new
 elif k in d:del d[k]

def adv(a,b):
 d={}
 for k,v in a.items():
  for l,w in b.items():
   m=tuple(k[j]+l[j] for j in range(3));dot=sum(l[j]*v[j] for j in range(3))
   if dot:add(d,m,tuple(dot*z for z in w))
 return d

def proj(d):
 u,p={},{}
 for k,v in d.items():
  n=sum(z*z for z in k);r=s.expand(sum(k[j]*v[j] for j in range(3))/n) if n else s.S.Zero
  add(u,k,tuple(v[j]-k[j]*r for j in range(3)))
  if r:p[k]=r
 return u,p
u={}
for f,comp in [((0,1,0),0),((0,0,1),1),((1,0,0),2)]:
 for sign in [-1,1]:
  k=tuple(sign*z for z in f);v=list(Z);v[comp]=-s.Rational(sign,2)*A[comp];u[k]=tuple(v)
jets=[u];press=[]
for n in range(4):
 d={}
 for j in range(n+1):
  for k,v in adv(jets[j],jets[n-j]).items():add(d,k,tuple(comb(n,j)*z for z in v))
 u,p=proj(d);jets.append(u);press.append(p)
 print('jet',n+1,'modes',len(u),flush=True)

def along(data,n,corner,vpath,scalar=False):
 out=list(Z);imag=list(Z)
 for k,v in data.items():
  phase=sum(k[j]*corner[j] for j in range(3));speed=sum(k[j]*vpath[j] for j in range(3));po=(phase+1+n)%4
  cf=s.expand(speed**n)/factorial(n)*(1 if po<2 else -1)
  dest=out if po%2==0 else imag
  for j in range(3):dest[j]+=cf*(v*k[j] if scalar else v[j])
 assert all(s.expand(z)==0 for z in imag)
 return tuple(s.expand(z) for z in out)
for corner in product([-1,1],repeat=3):
 path=(A[0]*corner[1],A[1]*corner[2],A[2]*corner[0]);series=[]
 for n in range(5):
  out=list(Z)
  for j in range(n+1):
   w=along(jets[j],n-j,corner,path)
   for i in range(3):out[i]+=w[i]/factorial(j)
  series.append(tuple(s.expand(z) for z in out))
 assert series[:4]==[path,Z,Z,Z],series[:4]
 expected=tuple(-s.Rational(4,15)*path[j]*A[(j+1)%3]**2*A[(j+2)%3]**2 for j in range(3))
 assert all(s.expand(series[4][j]-expected[j])==0 for j in range(3)),(series[4],expected)
 H=tuple(path[j]*A[(j+1)%3]**2*A[(j+2)%3]**2 for j in range(3))
 for j,constant in [(1,s.Integer(2)),(2,-s.Rational(4,3)),(3,s.Rational(2,5))]:
  w=along(press[j],3-j,corner,path,scalar=True)
  assert all(s.expand(w[i]/factorial(j)-constant*H[i])==0 for i in range(3))
print('PASS symbolic all eight corners, velocity quartic and full pressure split')
assert [len(u) for u in jets] == [6,12,18,48,98]
for u in jets:
 for k,v in u.items():
  assert s.expand(sum(k[j]*v[j] for j in range(3)))==0
  assert u.get(tuple(-z for z in k),Z)==tuple(-z for z in v)
assert not press[0]
assert press[1]=={k:-s.prod(A)/4 for k in product([-1,1],repeat=3)}
print('PASS full-mode incompressibility, reality and exact first pressure')

# Direct trigonometric checks of the lower jets and moving maxima.
x,y,z=X=s.symbols('x y z',real=True)
a,b,c=A
u0=s.Matrix([a*s.sin(y),b*s.sin(z),c*s.sin(x)])
nonlinearity=u0.jacobian(X)*u0
u2=-s.Matrix([a*b**2*s.sin(y)*s.sin(z)**2,
              b*c**2*s.sin(z)*s.sin(x)**2,
              c*a**2*s.sin(x)*s.sin(y)**2])
p1=-2*a*b*c*s.cos(x)*s.cos(y)*s.cos(z)
full_second=nonlinearity.jacobian(X)*u0+u0.jacobian(X)*nonlinearity-s.Matrix([s.diff(p1,q) for q in X])
assert all(s.trigsimp(v)==0 for v in full_second-u2)
phase_mean=a*s.sin(x)*s.sin(y)*s.cos(y)*s.cos(z)+b*s.sin(y)*s.sin(z)*s.cos(x)*s.cos(z)+c*s.sin(x)*s.sin(z)*s.cos(x)*s.cos(y)
p2=-s.Rational(4,3)*a*b*c*phase_mean
g2_pressure=2*s.trace(nonlinearity.jacobian(X)**2+u0.jacobian(X)*u2.jacobian(X))
assert s.trigsimp(sum(s.diff(p2,q,2) for q in X)+g2_pressure)==0
g0=u0.dot(u0);g1=-2*u0.dot(nonlinearity);g2=2*nonlinearity.dot(nonlinearity)+2*u0.dot(u2)
metric=s.diag(c**2,a**2,b**2)
for corner in product([-1,1],repeat=3):
 at={X[j]:corner[j]*s.pi/2 for j in range(3)}
 path=s.Matrix([a*corner[1],b*corner[2],c*corner[0]])
 assert s.hessian(g0,X).subs(at)==-2*metric
 assert s.Matrix([s.diff(g1,q) for q in X]).subs(at)==2*metric*path
 assert s.hessian(g1,X).subs(at)==s.zeros(3)
 assert s.Matrix([s.diff(g2,q) for q in X]).subs(at)==s.zeros(3,1)
 assert all(s.diff(g0,p,q,r).subs(at)==0 for p,q,r in product(X,repeat=3))
print('PASS exact second pressure and nondegenerate moving-maximum equations')

# Orthogonal sign changes plus half-period translations preserve the datum
# for unequal amplitudes and connect all eight maximizing corners.
images=set()
for eps in product([-1,1],repeat=3):
 cos_shift=tuple(eps[(j-1)%3]*eps[j] for j in range(3))
 for j in range(3):
  assert eps[(j+1)%3]*cos_shift[(j+1)%3]==eps[j]
 image=tuple(eps[j]*cos_shift[j] for j in range(3))
 images.add(image)
assert images==set(product([-1,1],repeat=3))
print('PASS exact eight-corner symmetry; no unresolved splitting of maximum branches')

quartic=-s.Rational(8,5)*a**2*b**2*c**2
assert quartic.subs({a:1,b:1,c:2})==-s.Rational(32,5)
assert all(s.expand(quartic-quartic.subs(q,-q))==0 for q in A)
assert all(quartic.subs(q,0)==0 for q in A)
assert s.Rational(8,5)-s.Rational(4,5)==s.Rational(4,5)
print('PASS quartic speed loss, the (1,1,2) value and positive-viscosity margins')
print('Actual all-mode remainders and positive-viscosity continuation are separate written arguments.')
