"""Verify every number used in the helicopter exam prep pack."""
import math

def box(t): print("\n" + "=" * 66 + "\n" + t + "\n" + "=" * 66)

g = 9.81

# ---------------------------------------------------------------- A. coning (class numerical)
box("A. CONING - class numerical")
W_kg, N, R, A, RPM, m_blade = 7400, 4, 7.5, 176.7, 265, 64
W = W_kg * g
Om = 2 * math.pi * RPM / 60
T_blade = W / N
print(f"W = {W:.0f} N   T/blade = {T_blade:.0f} N")
print(f"Omega = {Om:.2f} rad/s  (class wrote 27.75)")
for label, mp in [("m'=9.2 kg/m (=> class CF)", 9.2), ("m'=64/7.5=8.533 kg/m", m_blade / R)]:
    CF = mp * Om**2 * R**2 / 2
    b0 = T_blade / CF
    print(f"{label:34s} CF = {CF:9.0f} N   beta = {b0:.4f} rad = {math.degrees(b0):.2f} deg")
print("class CF = 199353 N -> beta =", round(T_blade/199353, 4), "rad =", round(math.degrees(T_blade/199353), 2), "deg")
print("CF from 1st principles with m'=64/7.5 :", round((m_blade/R)*Om**2*R**2/2))

# ---------------------------------------------------------------- B. forward flight numerical
box("B. FORWARD FLIGHT FULL NUMERICAL")
rho = 1.225
Wh, Rw, Nw, c, a, Cd0, Omw, f = 58900.0, 7.5, 4, 0.5, 5.7, 0.012, 28.0, 2.5
mu, kappa, gam = 0.3, 1.2, 8.0
Aw = math.pi * Rw**2
OmR = Omw * Rw
sig = Nw * c / (math.pi * Rw)
V = mu * OmR
CT = Wh / (rho * Aw * OmR**2)
vh = math.sqrt(Wh / (2 * rho * Aw))
lam_h = vh / OmR
Cm = 0.5 * sig * a
print(f"A={Aw:.2f} m2  OmegaR={OmR:.0f} m/s  sigma={sig:.4f}  V={V:.1f} m/s")
print(f"C_T={CT:.6f}  vh={vh:.3f} m/s  lam_h={lam_h:.5f}  1/2*sigma*a={Cm:.4f}")

# induced velocity: exact quartic  x^4 + (V/vh)^2 x^2 - 1 = 0
def vi_exact(V, vh):
    kb = (V / vh)**2
    x2 = (-kb + math.sqrt(kb**2 + 4)) / 2
    return math.sqrt(x2) * vh
vi = vi_exact(V, vh)
print(f"V/vh={V/vh:.3f}  vi={vi:.4f} m/s  Glauert vi=CT/(2mu)*OmR={CT/(2*mu)*OmR:.4f}  lam_i={vi/OmR:.5f}")

# trim iteration for alpha_T and lambda
Dp = 0.5 * rho * V**2 * f
alphaT = Dp / Wh
for it in range(6):
    lam = vi / OmR + mu * alphaT
    # H force (profile part only, induced part small)
    CH0 = 0.25 * sig * Cd0 * mu
    alphaT = (CH0 / CT) + Dp / Wh
    # theta0 from thrust equation
    theta0 = (CT / Cm + lam / 2) / (1/3 + mu**2 / 2)
    # re-solve induced with updated... (vi fixed by thrust)
print(f"Dp={Dp:.0f} N  Dp/W={Dp/Wh:.4f}  CH0={CH0:.2e}  alphaT={alphaT:.4f} rad={math.degrees(alphaT):.2f} deg")
print(f"lam={lam:.5f}  lambda_i={vi/OmR:.5f}   theta0={theta0:.5f} rad = {math.degrees(theta0):.2f} deg")

# flapping coefficients
a0 = (gam / 8) * (theta0 * (1 + mu**2) - 4 * lam / 3)
a1 = mu * (8 * theta0 / 3 - 2 * lam) / (1 - 0.5 * mu**2)
b1 = (4 / 3) * mu * a0 / (1 + 0.5 * mu**2)
print(f"a0={a0:.5f} rad = {math.degrees(a0):.2f} deg")
print(f"a1={a1:.5f} rad = {math.degrees(a1):.2f} deg")
print(f"b1={b1:.5f} rad = {math.degrees(b1):.2f} deg")

# power
CQ0 = sig * Cd0 * (1 + 3 * mu**2) / 8
CQi = kappa * (vi / OmR) * CT
CQp = mu * (Dp / Wh) * CT
CQ = CQ0 + CQi + CQp
Pscale = rho * Aw * OmR**3
print(f"CQ0={CQ0:.3e}  CQi={CQi:.3e}  CQp={CQp:.3e}  CQ={CQ:.3e}")
print(f"P_prof={CQ0*Pscale/1e3:.1f} kW  P_ind={CQi*Pscale/1e3:.1f} kW  P_par={CQp*Pscale/1e3:.1f} kW")
print(f"P_total={CQ*Pscale/1e3:.1f} kW   (check Dp*V={Dp*V/1e3:.1f} kW, T*vi*kappa={kappa*Wh*vi/1e3:.1f} kW)")

# hover for comparison
lam_h2 = lam_h
theta0h = (CT / Cm + lam_h2 / 2) / (1/3)
CQ0h = sig * Cd0 / 8
CQih = kappa * lam_h2 * CT
Ph = (CQ0h + CQih) * Pscale
print(f"HOVER: theta0={math.degrees(theta0h):.2f} deg  P0={CQ0h*Pscale/1e3:.1f} kW  Pi={CQih*Pscale/1e3:.1f} kW  P={Ph/1e3:.1f} kW")
print(f"a0 hover = {math.degrees((gam/8)*(theta0h - 4*lam_h2/3)):.2f} deg")

# ---------------------------------------------------------------- C. momentum theory mini numerical
box("C. MOMENTUM THEORY NUMERICAL")
Wc, Rc = 15000.0, 5.5
Ac = math.pi * Rc**2
vhc = math.sqrt(Wc / (2 * rho * Ac))
print(f"A={Ac:.2f}  vh={vhc:.3f} m/s  Pih={Wc*vhc/1e3:.2f} kW")
for Vc in [20, 40, 50, 60]:
    vic = vi_exact(Vc, vhc)
    print(f" V={Vc:3d} m/s  V/vh={Vc/vhc:5.2f}  vi={vic:.3f}  vi/vh={vic/vhc:.4f}  "
          f"Pi={Wc*vic/1e3:6.2f} kW  Pi/Pih={vic/vhc:.3f}  Glauert={vhc**2/Vc:.3f}")

# ---------------------------------------------------------------- D. hinge offset / damping
box("D. HINGE OFFSET, FREQUENCY, DAMPING")
for e in [0.04, 0.06, 0.1]:
    eps = 3 * e / (2 * (1 - e))
    wb = math.sqrt(1 + eps)
    eta = (1 - e)**3 * (1 + e) / 3
    for gamx in [6, 8]:
        zeta = gamx / (16 * wb)
        zeta_eta = gamx * eta / (16 * wb)
        print(f"e={e:.2f} eps={eps:.4f} wb/Om={wb:.4f} eta={eta:.4f} gamma={gamx}: "
              f"zeta={zeta:.3f}  zeta(with eta)={zeta_eta:.3f}")
e = 0.06
print("class example e=0.0625: sqrt(1+e) =", round(math.sqrt(1 + 0.0625), 4),
      " sqrt(1+eps) =", round(math.sqrt(1 + 3*0.0625/(2*(1-0.0625))), 4))

# ---------------------------------------------------------------- E. reverse flow / tip Mach
box("E. LIMITS: REVERSE FLOW, TIP MACH, STALL")
for mu_l in [0.2, 0.3, 0.4]:
    print(f"mu={mu_l}: reversed-flow diameter d = mu*R = {mu_l*R:.2f} m  (R={R} m), "
          f"area fraction approx = {math.pi*mu_l**2/4*100:.2f} %")
a_sound = 340.0
for Vk in [200, 250, 300]:
    Vm = Vk / 3.6
    Mtip = (OmR + Vm) / a_sound
    mux = Vm / OmR
    print(f" V={Vk} km/h = {Vm:.1f} m/s: mu={mux:.3f}  advancing tip M={Mtip:.3f}  "
          f"retreating tip M={(OmR-Vm)/a_sound:.3f}")

# CT/sigma and stall margin
print(f"CT/sigma = {CT/sig:.4f}  (hover value {CT/sig:.4f})")

# ---------------------------------------------------------------- F. flapping-vs-cyclic check
box("F. A1=b1, B1=-a1 CHECK (90 deg lag)")
print("Hover, cyclic pitch theta = th0 - A1 cos psi - B1 sin psi")
print("beta'' + beta + (gamma/8) beta' = (gamma/8) theta")
print("-> cos psi : -b1 (beta) + a1 (beta'')  cancel ;  damping -(gamma/8)b1 ; RHS -(gamma/8)A1  -> b1 = A1")
print("-> sin psi : -a1 + b1 cancel ; damping +(gamma/8)a1 ; RHS -(gamma/8)B1 -> a1 = -B1")
