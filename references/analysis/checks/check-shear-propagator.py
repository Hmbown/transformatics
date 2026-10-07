import numpy as np
from scipy.integrate import solve_ivp, quad
sigma=lambda t: 3*np.cos(4*t)-.6
th=lambda t: .75*np.sin(4*t)-.6*t
cases=[(1.,.4,2.),(0.,1.,.3),(1e-10,1.,2.),(1.,0.,-2.),(0.,0.,1.)]
worst=0.
for eta in cases:
 eta=np.array(eta);p,q,r=eta;kappa=np.hypot(p,q);eps=.07;T=1.3
 xi=lambda t: np.array([p,q,r-p*th(t)])
 if kappa:
  EH=np.array([p,q,0])/kappa; ET=np.array([-q,p,0])/kappa
  EP=lambda t: (-(r-p*th(t))*EH+kappa*np.array([0.,0.,1.]))/np.linalg.norm(xi(t))
  b0=.6*EP(0)+.8*ET
  R=np.linalg.norm(eta)/np.linalg.norm(xi(T))
  J=q*np.linalg.norm(eta)*quad(lambda u:1/(kappa*kappa+(r-p*u)**2),0,th(T),epsabs=1e-12)[0]
  expected=.6*R*EP(T)+(.8+.6*J)*ET
 else:b0=np.array([.6,.8,0]);expected=b0.copy()
 damp=np.exp(-eps*quad(lambda t:np.dot(xi(t),xi(t)),0,T)[0]);expected*=damp
 def rhs(t,b):
  x=xi(t);K=x@x;return -sigma(t)*b[2]*np.array([1.,0.,0.])+2*sigma(t)*p*b[2]*x/K-eps*K*b
 sol=solve_ivp(rhs,[0,T],b0,rtol=2e-12,atol=2e-14)
 err=np.linalg.norm(sol.y[:,-1]-expected);worst=max(worst,err)
 assert err<1e-9,(eta,err)
print('5 Fourier orientations, sign-changing sigma, full viscous ODE: max endpoint difference',worst)
