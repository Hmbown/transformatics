"""Exact algebra behind the force-removal notes; not a PDE certificate.

Run from the repository with .venv/bin/python. No simulation, external source
verification, or assertion about the unforced Navier--Stokes lifespan occurs.
"""

import sympy as s


checked = 0


def zero(expression):
    global checked
    assert s.simplify(expression) == 0, expression
    checked += 1


def nonzero(expression):
    global checked
    assert s.simplify(expression) != 0, expression
    checked += 1


# Complete azimuthal cutoff residual at z=0, viscosity one.
r, z, h, kappa = s.symbols("r z h kappa", positive=True)
eta = s.Function("eta")(r)
K = kappa * r ** (-1 - 2 * h)
residual = -K * (s.diff(eta, r, 2) + s.diff(eta, r) / r)
residual -= 2 * s.diff(K, r) * s.diff(eta, r)
beta = 1 + 4 * h
D_eta = s.diff(eta, r, 2) - beta * s.diff(eta, r) / r
zero(residual + K * D_eta)
zero(s.diff(r ** (-beta) * s.diff(eta, r), r) - r ** (-beta) * D_eta)
# Dropping the product-Laplacian term changes the terminal coefficient.
nonzero((-K * (s.diff(eta, r, 2) + s.diff(eta, r) / r)) + K * D_eta)

# Source heat profile and full pressure-corrected centrifugal symbol.
tau = s.symbols("tau", positive=True)
H = s.Function("H")
q = 4 * tau / r**2
heat = kappa * r ** (-1 - 2 * h) * H(q)
Omega_heat = heat / r
discriminant = s.diff((r * heat) ** 2, r) / r**3
slope = s.diff(H(s.Symbol("q")), s.Symbol("q")).subs(s.Symbol("q"), q)
zero(discriminant + 4 * (h + q * slope / H(q)) * Omega_heat**2)
zero(discriminant - 2 * Omega_heat * (s.diff(heat, r) + heat / r))

Omega, d, chi, rho, nu, k, lam = s.symbols(
    "Omega d chi rho nu k lam", positive=True
)
matrix = s.Matrix([[0, 2 * Omega * chi], [2 * d * Omega * chi, 0]])
gamma = 2 * Omega * s.sqrt(d) * chi
growing = s.Matrix([1, s.sqrt(d)])
for entry in matrix * growing - gamma * growing:
    zero(entry)
zero((matrix - nu * k**2 * s.eye(2) - lam * s.eye(2)).det()
     - ((lam + nu * k**2) ** 2 - gamma**2))
# Radial forcing must first be projected onto the meridional solenoidal line.
meridional_projector = s.Matrix([[chi**2, -chi*rho], [-chi*rho, rho**2]])
projected = meridional_projector * s.Matrix([2 * Omega, 0])
zero(projected[0] - 2 * Omega * chi**2)
zero(projected[1] + 2 * Omega * chi * rho)
nonzero(2 * Omega * chi**2 - 2 * Omega)

# Exact compact axisymmetric solenoidal lift used by the quasimode.
R = s.symbols("R", real=True)
envelope = s.Function("C")(r, z)
phase = s.exp(s.I * k * z)
psi = -r * R * envelope * phase / (s.I * k)
vr = -s.diff(psi, z) / r
vz = s.diff(psi, r) / r
zero(vr - R * (envelope + s.diff(envelope, z) / (s.I * k)) * phase)
zero(vz + R * (s.diff(envelope, r) + envelope / r) * phase / (s.I * k))
zero(s.diff(r * vr, r) / r + s.diff(vz, z))
# Keeping only the radial leading term loses exact incompressibility.
nonzero(s.diff(r * R * envelope * phase, r) / r)

# Full cylindrical quasimode residual; includes basis rotation and curvature.
omega0 = s.symbols("omega0", positive=True)
omega_r = s.Function("omega")(r)
B_r = 2 * omega_r + r * s.diff(omega_r, r)
B0 = -2 * d * omega0
gamma0 = 2 * omega0 * s.sqrt(d)
T = R * s.sqrt(d)
Hk = envelope * phase
J = s.diff(Hk, z) / (s.I * k)
vtheta = T * Hk


def dc(expr):
    return s.diff(expr, r, 2) + s.diff(expr, r) / r + s.diff(expr, z, 2)


def lk(expr):
    return dc(expr) - expr / r**2 + k**2 * expr


raw_r = (gamma0 - nu * k**2) * vr - nu * (dc(vr) - vr / r**2)
raw_r -= 2 * omega_r * vtheta
formula_r = 2 * T * ((omega0 - omega_r) * Hk + omega0 * (J - Hk))
formula_r -= nu * R * lk(J)
zero(raw_r - formula_r)
raw_theta = (gamma0 - nu * k**2) * vtheta
raw_theta += B_r * vr - nu * (dc(vtheta) - vtheta / r**2)
formula_theta = R * ((B_r - B0) * Hk + B_r * (J - Hk)) - nu * T * lk(Hk)
zero(raw_theta - formula_theta)
zero((gamma0 - nu * k**2) * vz - nu * dc(vz)
     - (gamma0 * vz - nu * (dc(vz) + k**2 * vz)))
# Halving the transport coupling loses the cylindrical basis contribution.
nonzero(raw_r + omega_r * vtheta - formula_r)

# Plateaux in the anisotropic heat-Leray obstruction.
x, y = s.symbols("x y", real=True)
v = s.Matrix([x**2, -2 * x * y])
zero(s.diff(v[0], x) + s.diff(v[1], y))
advective = v.jacobian(s.Matrix([x, y])) * v
zero(advective[0] - 2 * x**3)
zero(advective[1] - 2 * x**2 * y)
zero(s.diff(advective[1], x) - s.diff(advective[0], y) - 4 * x * y)
nonzero(s.diff(advective[1], x) - s.diff(advective[0], y))

# Cylindrical pressure primitive: the remaining axial term must be retained.
radial, axial = s.symbols("radial axial", positive=True)
Psi = s.Function("Psi")(radial, axial)
Theta = s.Function("Theta")(radial, axial)
Aamp, small_r, long_L = s.symbols("Aamp small_r long_L", positive=True)
primitive_r = -Theta**2 / radial
centrifugal = -Aamp**2 * Theta**2 / (small_r * radial)
zero(centrifugal - Aamp**2 / small_r * primitive_r)
primitive_z = Aamp**2 / long_L * s.diff(Psi, axial)
nonzero(primitive_z)

# Finite-window Duhamel amplification, with residual budget epsilon*lambda.
eps, gain = s.symbols("eps gain", positive=True)
lower = gain / (1 + eps * (gain - 1))
zero(lower.subs(gain, 1 / eps) - 1 / (eps * (2 - eps)))
nonzero(lower.subs(gain, 1 / eps) - 1 / eps)

# Time and spatial exponents: no numerical approximations.
alpha = s.Rational(1, 2) + h
D = s.Rational(1, 2) - h
zero(alpha + 1 - 2 * alpha - s.Rational(1, 2) + h)
zero(alpha + 1 - 2 * alpha - D)
a, b = h / 8, h / 4
for exponent in (a, b-a, h-2*b, h-a-b, h-2*a, h):
    assert s.simplify(exponent / h) > 0
    checked += 1

# Exact Riccati modulation: a time shift may move the terminal time.
v0, epsilon = s.symbols("v0 epsilon", positive=True)
theta = s.atan(v0 / s.sqrt(epsilon)) / s.sqrt(epsilon)
theta_prime = s.diff(theta, v0) * v0**2
zero(theta_prime - v0**2 / (v0**2 + epsilon))
zero(epsilon + (theta_prime - 1) * (v0**2 + epsilon))
nonzero(epsilon + (theta_prime - 1) * v0**2)

# Force coupling: a curl-free input leaves vorticity cross input modulo gradient.
coords = s.Matrix([x, y, z])
U = s.Matrix([s.Function(name)(x, y, z) for name in ("U1", "U2", "U3")])
phi = s.Function("phi")(x, y, z)
grad_phi = s.Matrix([s.diff(phi, q) for q in coords])


def gradient(expr):
    return s.Matrix([s.diff(expr, q) for q in coords])


def curl(field):
    return s.Matrix([
        s.diff(field[2], y) - s.diff(field[1], z),
        s.diff(field[0], z) - s.diff(field[2], x),
        s.diff(field[1], x) - s.diff(field[0], y),
    ])


coupling = grad_phi.jacobian(coords) * U + U.jacobian(coords) * grad_phi
for entry in coupling - gradient(U.dot(grad_phi)) - curl(U).cross(grad_phi):
    zero(entry)
# The second adjoint pressure tail is not in general another gradient.
local_U = s.Matrix([y, 0, 0])
harmonic_q = (x**2 - y**2) / 2
tail = local_U.jacobian(coords).T * gradient(harmonic_q)
zero(sum(s.diff(harmonic_q, q, 2) for q in coords))
zero(curl(tail)[2] - 1)
nonzero(curl(tail)[2])
lap_grad = s.Matrix([sum(s.diff(entry, q, 2) for q in coords) for entry in grad_phi])
adjoint_gradient = nu * lap_grad + grad_phi.jacobian(coords) * U
adjoint_gradient -= U.jacobian(coords).T * grad_phi
adjoint_formula = gradient(nu * sum(s.diff(phi, q, 2) for q in coords) + U.dot(grad_phi))
adjoint_formula -= 2 * U.jacobian(coords).T * grad_phi
for entry in adjoint_gradient - adjoint_formula:
    zero(entry)

# Exact response derivatives for a time-dependent, noncommuting matrix.
t = s.symbols("t", real=True)
At = s.Matrix([[t, 1], [1 + t**2, -t]])
wt = s.Matrix([1 + t, t**2])
zt = s.Matrix([s.Function("z1")(t), s.Function("z2")(t)])
first = At * zt + wt
third = s.diff(first, t, 2)
replacement = {}
for i in range(2):
    replacement[s.diff(zt[i], t, 2)] = (At * wt + s.diff(wt, t))[i]
    replacement[s.diff(zt[i], t)] = wt[i]
    replacement[zt[i]] = 0
third_at_restart = third.xreplace(replacement)
correct_third = At**2 * wt + 2 * s.diff(At, t) * wt + At * s.diff(wt, t) + s.diff(wt, t, 2)
for entry in third_at_restart - correct_third:
    zero(entry)
naive_third = s.diff(At * wt + s.diff(wt, t), t) + At * (At * wt + s.diff(wt, t))
nonzero((naive_third - correct_third)[0])

# Terminal Green kernel signs and the mode-dependent backward diffusive cost.
terminal, start, c, mode = s.symbols("terminal start c mode", positive=True)
kernel = s.exp(c / h * ((terminal - t)**(-h) - (terminal - start)**(-h)))
zero(s.diff(kernel, t) - c * (terminal - t)**(-1-h) * kernel)
zero(s.diff(kernel, start) + c * (terminal - start)**(-1-h) * kernel)
mode_kernel = kernel * s.exp(-nu * (2 * s.pi * mode)**2 * (t - start))
zero(s.diff(mode_kernel, t) - (c * (terminal-t)**(-1-h) - nu*(2*s.pi*mode)**2) * mode_kernel)

# Positive quasimodes do not count unstable eigenvalues.
large = s.symbols("large", positive=True)
jordan = s.Matrix([[-1, large], [0, -1]])
jordan_v = s.Matrix([1, 2/large]) / s.sqrt(1 + 4/large**2)
jordan_residual = (jordan - s.eye(2)) * jordan_v
zero(jordan_residual.dot(jordan_residual) - (4/large)**2 / (1 + 4/large**2))
characteristic = jordan.charpoly()
zero(characteristic.as_expr() - (characteristic.gen + 1)**2)

# The angular cancellation adds r0 to the first response bound; packet packing.
order = s.symbols("order", integer=True, nonnegative=True)
zero(-1-h + s.Rational(3,4) + s.Rational(1,2)+h/8 + order*h/8
     - (s.Rational(1,4)-7*h/8+order*h/8))
zero((s.Rational(1,2)-h) - (s.Rational(1,2)+h/8) + 9*h/8)

# Low-axial affine response: radial heat and dilation do not commute.
profile = s.Function("profile")(r)


def radial_heat(expr):
    return s.diff(expr, r, 2) + s.diff(expr, r)/r - expr/r**2


def dilation(expr):
    return r*s.diff(expr, r) + expr


zero(radial_heat(dilation(profile)) - dilation(radial_heat(profile))
     - 2*radial_heat(profile))
nonzero(radial_heat(dilation(profile)) - dilation(radial_heat(profile)))

# Full nonlinear cylindrical momentum for an arbitrary prescribed strain.
strain = s.Function("strain")(t)
swirl = s.Function("swirl")(t, r)
radial_velocity = strain*r
axial_velocity = -2*strain*z
radial_pressure = -(s.diff(strain,t)+strain**2)*r + swirl**2/r
axial_pressure = (2*s.diff(strain,t)-4*strain**2)*z
zero(s.diff(r*radial_velocity,r)/r+s.diff(axial_velocity,z))
zero(s.diff(radial_velocity,t)+radial_velocity*s.diff(radial_velocity,r)
     - swirl**2/r - nu*radial_heat(radial_velocity)+radial_pressure)
zero(s.diff(axial_velocity,t)+axial_velocity*s.diff(axial_velocity,z)
     + axial_pressure)
azimuthal_momentum = s.diff(swirl,t)+radial_velocity*s.diff(swirl,r)
azimuthal_momentum += radial_velocity*swirl/r-nu*radial_heat(swirl)
zero(azimuthal_momentum - (s.diff(swirl,t)+strain*dilation(swirl)-nu*radial_heat(swirl)))

# Exact time-dependent strain transformation, including the heat clock.
accumulated = s.Function("accumulated")(t)
heat_clock = s.Function("heat_clock")(t)
heat_solution = s.Function("heat_solution")
new_radius = r*s.exp(-accumulated)
transformed = s.exp(-accumulated)*heat_solution(heat_clock,new_radius)
transformed_residual = s.diff(transformed,t)+strain*dilation(transformed)-nu*radial_heat(transformed)
transformed_residual = transformed_residual.subs({
    s.diff(accumulated,t):strain,
    s.diff(heat_clock,t):s.exp(-2*accumulated),
})
clock_var, radius_var = s.symbols("clock_var radius_var", positive=True)
heat_profile = heat_solution(clock_var,radius_var)
heat_residual = s.diff(heat_profile,clock_var)-nu*(
    s.diff(heat_profile,radius_var,2)+s.diff(heat_profile,radius_var)/radius_var
    -heat_profile/radius_var**2)
heat_residual = heat_residual.subs({clock_var:heat_clock,radius_var:new_radius}, simultaneous=True)
zero(transformed_residual-s.exp(-3*accumulated)*heat_residual)

# Exact powers in the completed reference's first-derivative estimate.
coefficient_loss = s.Rational(1,100000)
zero(-s.Rational(1,2)-h+h/2-s.Rational(1,2)-h/2 - (-1-h))
zero(1+s.Rational(3,2)*h-s.Rational(17,25)*h - (1+s.Rational(41,50)*h))
for margin in (s.Rational(1,2)-coefficient_loss, s.Rational(9,50),
               s.Rational(9,10)-coefficient_loss):
    assert margin > 0
    checked += 1
# Radial thinness cannot freeze the slow axial channel without a viscous cost.
zero((-1-h)+(s.Rational(1,2))-(s.Rational(1,2)-h)+1)
# Gevrey-2 leakage exponents at k*ell and k*R.
zero((-s.Rational(1,2)-h/4+s.Rational(1,2)+h/8)/2+h/16)
zero((-s.Rational(1,2)-h/4+s.Rational(1,2))/2+h/8)

# Natural radial scale: exact incompressibility, viscous curl and swirl equations.
radial, clock = s.symbols("radial clock", positive=True)
alpha = s.symbols("alpha", positive=True)
radial_f = s.Function("f_radial")(radial, clock)
radial_c = s.Function("c_radial")(radial, clock)
radial_omega = s.Function("omega_radial")(radial, clock)
radial_g = s.Function("g_radial")(radial, clock)
axial_k = alpha * tau**(-s.Rational(1, 2) + h)


def physical_dr(expr):
    return s.diff(expr, radial) / s.sqrt(tau)


def radial_a(expr):
    return (-s.diff(expr, radial, 2) - s.diff(expr, radial)/radial
            + expr/radial**2 + alpha**2*tau**(2*h)*expr)


def modal_vector_laplacian(expr):
    return (physical_dr(physical_dr(expr))
            + physical_dr(expr)/(s.sqrt(tau)*radial)
            - expr/(tau*radial**2) - axial_k**2*expr)


radial_vr = -s.I*alpha*tau**h*radial_f
radial_vz = s.diff(radial_f, radial) + radial_f/radial
radial_vtheta = -s.I*radial_c
radial_curl = s.I*axial_k*radial_vr - physical_dr(radial_vz)
zero(physical_dr(radial_vr) + radial_vr/(s.sqrt(tau)*radial)
     + s.I*axial_k*radial_vz)
zero(radial_curl - radial_a(radial_f)/s.sqrt(tau))
curl_equation = (s.diff(radial_curl, clock)/tau
                 - nu*modal_vector_laplacian(radial_curl)
                 - 2*tau**(-1-h)*radial_omega*s.I*axial_k*radial_vtheta)
zero(tau**s.Rational(3, 2)*curl_equation
     - (s.diff(radial_a(radial_f), clock) + nu*radial_a(radial_a(radial_f))
        - 2*alpha*radial_omega*radial_c))
swirl_equation = (s.diff(radial_vtheta, clock)/tau
                  - nu*modal_vector_laplacian(radial_vtheta)
                  - 2*tau**(-1-h)*radial_g*radial_omega*radial_vr)
zero(s.I*tau*swirl_equation - (s.diff(radial_c, clock)
     + nu*radial_a(radial_c) - 2*alpha*radial_g*radial_omega*radial_f))
# Recovering meridional kinetic energy leaves this endpoint term, not zero
# pointwise. It vanishes only after integration with homogeneous f traces.
zero(radial*radial_vz**2 - radial*s.diff(radial_f, radial)**2
     - radial_f**2/radial - s.diff(radial_f**2, radial))
nonzero(s.diff(radial_f**2, radial))

# A radial lift enters both the fourth-order meridional equation and swirl.
lift_f = s.Function("lift_f")(radial, clock)
lift_c = s.Function("lift_c")(radial, clock)
q_residual = lambda f, c: (s.diff(radial_a(f), clock)
    + nu*radial_a(radial_a(f)) - 2*alpha*radial_omega*c)
c_residual = lambda f, c: (s.diff(c, clock) + nu*radial_a(c)
    - 2*alpha*radial_g*radial_omega*f)
zero(q_residual(radial_f+lift_f, radial_c+lift_c)
     - q_residual(radial_f, radial_c) - q_residual(lift_f, lift_c))
zero(c_residual(radial_f+lift_f, radial_c+lift_c)
     - c_residual(radial_f, radial_c) - c_residual(lift_f, lift_c))

# Full nonlinear comparison: powers after paying the global strain clock.
theta_power = (1+h)/16
scale_power = -(1+h)/2
duration_power = 1+h
zero(s.Rational(5, 2)*scale_power + 2*duration_power - theta_power
     - 11*(1+h)/16)  # quadratic bootstrap and integrated gradient
zero(s.Rational(3, 2)*scale_power + duration_power - theta_power
     - 3*(1+h)/16)   # absolute velocity error
zero(s.Rational(5, 2)*scale_power + duration_power - theta_power
     + 5*(1+h)/16)   # instantaneous gradient may grow
zero(-(1+h) + duration_power)  # local clock gains sqrt(log)

# Remote axisymmetric swirl stress: full Newtonian pressure multipole sign.
xx, yy, zz = s.symbols("xx yy zz", real=True)
target_radius = s.symbols("target_radius", positive=True)
newton_green = -1/(4*s.pi*s.sqrt(xx**2+yy**2+zz**2))
zero(s.diff(newton_green, xx, 2) + s.diff(newton_green, yy, 2)
     + s.diff(newton_green, zz, 2))
# For integrated stress diag(m,m,0), pi=m*G_zz away from its support.
zero(s.diff(newton_green, zz, 4).subs({xx:target_radius, yy:0, zz:0})
     + 9/(4*s.pi*target_radius**5))
# R-normalized test: U~R^(-1-2h), e~R^(-3/2), volume~R^3.
zero((-1-2*h)-s.Rational(3, 2)+3 - (s.Rational(1, 2)-2*h))
zero((s.Rational(1, 2)-2*h-5)/2 + s.Rational(9, 4)+h)

# Endpoint correction: form the complete products before extracting tau powers.
endpoint_log = s.symbols("endpoint_log", positive=True)
endpoint_loss = h / 64
endpoint_K = tau ** (-(1 + h) / 2)
endpoint_k = tau ** (-s.Rational(1, 2) - h / 4)
endpoint_d = tau ** (1 + h) * s.sqrt(endpoint_log)
endpoint_clock = tau ** (-endpoint_loss)
zero(endpoint_k / endpoint_K - tau ** (h / 4))
endpoint_quadratic = endpoint_K ** s.Rational(5, 2) * endpoint_d**3
endpoint_quadratic *= endpoint_clock**2
zero(endpoint_quadratic / (
    tau ** (7 * (1 + h) / 4 - 2 * endpoint_loss)
    * endpoint_log ** s.Rational(3, 2)) - 1)
zero(endpoint_quadratic / endpoint_d / (
    tau ** (3 * (1 + h) / 4 - 2 * endpoint_loss) * endpoint_log) - 1)

# The variational residual contains both error transport and error gradient.
endpoint_speed = endpoint_K ** s.Rational(3, 2) * endpoint_d * endpoint_clock
endpoint_gradient = endpoint_K ** s.Rational(5, 2) * endpoint_d * endpoint_clock
endpoint_variational = endpoint_d * endpoint_clock * (
    endpoint_k * endpoint_speed + endpoint_gradient)
zero(endpoint_variational / (
    tau ** (3 * (1 + h) / 4 - 2 * endpoint_loss)
    * endpoint_log * (1 + tau ** (h / 4))) - 1)
zero(endpoint_K**2 * tau**(h/8) * endpoint_d * endpoint_clock / (
    tau ** (h / 8 - endpoint_loss) * s.sqrt(endpoint_log)) - 1)
zero(endpoint_speed / (
    tau ** ((1 + h) / 4 - endpoint_loss) * s.sqrt(endpoint_log)) - 1)
zero(endpoint_gradient * endpoint_d / (
    tau ** (3 * (1 + h) / 4 - endpoint_loss) * endpoint_log) - 1)
for margin in (h/8-endpoint_loss, (1+h)/4-endpoint_loss,
               3*(1+h)/4-2*endpoint_loss):
    assert s.simplify(margin) > 0
    checked += 1

# Exact convolution for a source bounded by t^2 exp(2 a t).  Its equation
# fixes the two-clock exponent used in the nonlinear endpoint remainder.
endpoint_a, endpoint_time = s.symbols("endpoint_a endpoint_time", positive=True)
endpoint_integral = s.exp(endpoint_a * endpoint_time) * (
    s.exp(endpoint_a * endpoint_time) * (
        endpoint_time**2 / endpoint_a
        - 2 * endpoint_time / endpoint_a**2 + 2 / endpoint_a**3)
    - 2 / endpoint_a**3)
zero(endpoint_integral.subs(endpoint_time, 0))
zero(s.diff(endpoint_integral, endpoint_time) - endpoint_a * endpoint_integral
     - endpoint_time**2 * s.exp(2 * endpoint_a * endpoint_time))
nonzero(s.diff(endpoint_integral, endpoint_time) - endpoint_a * endpoint_integral
        - endpoint_time**2 * s.exp(endpoint_a * endpoint_time))

# Full Kelvin pressure can defeat a constant phase-normal metric.
shear_sigma, metric_Lambda = s.symbols("shear_sigma metric_Lambda", positive=True)
shear_N = s.Matrix([[0, shear_sigma, 0], [0, 0, 0], [0, 0, 0]])
kelvin_xi = s.Matrix([1, 1, 0]) / s.sqrt(2)
kelvin_b = s.Matrix([-1, 1, 0]) / s.sqrt(2)
metric_H = s.diag(1, metric_Lambda**2, 1)
kelvin_xi_dot = -shear_N.T * kelvin_xi
kelvin_pressure = 2 * s.I * kelvin_xi.dot(shear_N * kelvin_b) / kelvin_xi.dot(kelvin_xi)
kelvin_b_dot = (-shear_N * kelvin_b - s.I * kelvin_xi * kelvin_pressure
                - nu * kelvin_xi.dot(kelvin_xi) * kelvin_b)
zero(kelvin_xi.dot(kelvin_b))
zero(kelvin_xi_dot.dot(kelvin_b) + kelvin_xi.dot(kelvin_b_dot))
zero(kelvin_b_dot[0] - nu / s.sqrt(2))
zero(kelvin_b_dot[1] - (shear_sigma - nu) / s.sqrt(2))
weighted_rate = kelvin_b.dot(metric_H * kelvin_b_dot) / kelvin_b.dot(metric_H * kelvin_b)
zero(weighted_rate - shear_sigma * metric_Lambda**2 / (1 + metric_Lambda**2) + nu)
bare_scaled = s.diag(1, metric_Lambda, 1) * (-shear_N) * s.diag(1, 1/metric_Lambda, 1)
bare_gram = bare_scaled.T * bare_scaled
bare_char = bare_gram.charpoly()
zero(bare_char.as_expr() - bare_char.gen**2
     * (bare_char.gen - shear_sigma**2 / metric_Lambda**2))
# Missing pressure violates the transported solenoidal constraint and rate.
bare_b_dot = -shear_N * kelvin_b - nu * kelvin_b
nonzero(kelvin_xi_dot.dot(kelvin_b) + kelvin_xi.dot(bare_b_dot))
bare_rate = kelvin_b.dot(metric_H * bare_b_dot) / kelvin_b.dot(metric_H * kelvin_b)
nonzero((weighted_rate - bare_rate).subs(metric_Lambda, 2))

# A nontrivial three-dimensional nilpotent shear map: exact inverse and cost.
map_a1, map_a2, map_n3, map_d = s.symbols(
    "map_a1 map_a2 map_n3 map_d", real=True)
map_a = s.Matrix([map_a1, map_a2, 0])
map_n = s.Matrix([-map_a2, map_a1, map_n3])
map_phase = k * map_n.dot(coords)
map_dyad = map_a * map_n.T
map_value = coords + map_d * map_a * s.cos(map_phase)
map_jacobian = map_value.jacobian(coords)
map_inverse_jacobian = s.eye(3) + map_d * k * map_dyad * s.sin(map_phase)
zero(map_n.dot(map_value) - map_n.dot(coords))
zero(map_jacobian.det() - 1)
zero(sum(entry**2 for entry in map_jacobian * map_inverse_jacobian - s.eye(3)))
map_inverse_value = map_value - map_d * map_a * s.cos(k * map_n.dot(map_value))
zero(sum(entry**2 for entry in map_inverse_value - coords))
zero(s.trace(map_jacobian.T * map_jacobian) - 3
     - (map_d * k * s.sin(map_phase))**2 * map_a.dot(map_a) * map_n.dot(map_n))
# Determinant one does not make this change orthogonal or remove its shear.
nonzero((map_jacobian.T * map_jacobian - s.eye(3))[1, 1].subs(
    {map_a1: 1, map_a2: 0, map_n3: 0}))

# Angularly averaged axial-Hessian weight, including cylindrical orientation.
# At a target on the x axis, the in-plane radial/tangential eigenvalues of
# Hess(G_zz) rotate as cos^2(theta), sin^2(theta) around the target circle.
target_angle = s.symbols("target_angle", real=True)
newton_gzz = s.diff(newton_green, zz, 2)
newton_radial = s.diff(newton_gzz, xx, 2).subs(
    {xx: target_radius, yy: 0, zz: 0})
newton_tangential = s.diff(newton_gzz, yy, 2).subs(
    {xx: target_radius, yy: 0, zz: 0})
newton_average = -s.integrate(
    newton_radial * s.cos(target_angle)**2
    + newton_tangential * s.sin(target_angle)**2,
    (target_angle, 0, 2*s.pi)) / (2*s.pi)
zero(newton_average + 9 / (8*s.pi*target_radius**5))
# Keeping just the tangential eigenvalue even changes the sign.
nonzero(newton_average + newton_tangential)
assert newton_average < 0 and -newton_tangential > 0
checked += 1

# Actual slow pressure curvature: eta=2 K W_theta_theta, B<0, W<0.
pressure_R, pressure_Bmag, pressure_Kmag, pressure_Wmag = s.symbols(
    "pressure_R pressure_Bmag pressure_Kmag pressure_Wmag", positive=True)
pressure_M = s.symbols("pressure_M", real=True)
pressure_Bscale = -pressure_Bmag * pressure_R ** (-2 - 2*h)
pressure_Kscale = pressure_Kmag * pressure_R ** (-1 - 2*h)
pressure_Wscale = -pressure_Wmag * pressure_R ** (-5)
pressure_eta = 2 * pressure_Kscale * pressure_Wscale
pressure_curvature = (pressure_Bscale * pressure_eta * (-pressure_R*pressure_M/2)
                      * pressure_R**3)
zero(pressure_curvature + pressure_Bmag*pressure_Kmag*pressure_Wmag*pressure_M
     * pressure_R**(-4-4*h))
zero(tau**(2+2*h) * pressure_curvature.subs(pressure_R, s.sqrt(tau))
     + pressure_Bmag*pressure_Kmag*pressure_Wmag*pressure_M)
# The radial Taylor remainder is O(R^2), producing O(sqrt(tau)) after scaling.
pressure_remainder = pressure_Bscale * pressure_eta * pressure_R**2 * pressure_R**3
zero(tau**(2+2*h) * pressure_remainder.subs(pressure_R, s.sqrt(tau))
     - 2*pressure_Bmag*pressure_Kmag*pressure_Wmag*s.sqrt(tau))

print(f"PASS: {checked} exact identities, exponent checks and negative controls.")
print("Scope: algebra only; source identification and analytic estimates are in the notes.")
