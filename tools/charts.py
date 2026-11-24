"""Generate SVG polyline data for the three quantitative charts."""
import math

rho = 1.225
g = 9.81

# ---------------- example helicopter ----------------
W, R, N, c, a, Cd0, Om, f = 58900.0, 7.5, 4, 0.5, 5.7, 0.012, 28.0, 2.5
A = math.pi * R**2
OmR = Om * R
sig = N * c / (math.pi * R)
CT = W / (rho * A * OmR**2)
vh = math.sqrt(W / (2 * rho * A))
Cm = 0.5 * sig * a
CQ0h = sig * Cd0 / 8
Pscale = rho * A * OmR**3

def vi_exact(Vb, vhb):
    kb = (Vb / vhb)**2
    return math.sqrt((-kb + math.sqrt(kb**2 + 4)) / 2) * vhb

print("### POWER CURVE DATA (V, Pprof, Pind, Ppar, Ptot) in kW")
print("V,prof,ind,par,tot")
rows = []
for V in range(0, 96, 5):
    mu = V / OmR
    if V == 0:
        vi, lam = vh, vh / OmR
        alphaT = 0.0
    else:
        vi = vi_exact(V, vh)
        Dp = 0.5 * rho * V**2 * f
        alphaT = Dp / W
        lam = vi / OmR + mu * alphaT
    CQ0 = sig * Cd0 * (1 + 3 * mu**2) / 8
    CQi = 1.2 * (vi / OmR) * CT
    CQp = mu * alphaT * CT
    rows.append((V, CQ0 * Pscale / 1e3, CQi * Pscale / 1e3, CQp * Pscale / 1e3,
                 (CQ0 + CQi + CQp) * Pscale / 1e3))
    print(f"{V},{rows[-1][1]:.1f},{rows[-1][2]:.1f},{rows[-1][3]:.1f},{rows[-1][4]:.1f}")

# find min power speed
best = min(rows, key=lambda r: r[4])
print("min power at V =", best[0], "kW =", round(best[4], 1))

# ---------------- induced velocity curve ----------------
print("\n### vi/vh vs V/vh  (exact quartic) and Glauert approx")
for i in range(0, 21):
    x = i * 0.25            # V/vh
    k = x * x
    y = math.sqrt((-k + math.sqrt(k * k + 4)) / 2)
    print(f"{x:.2f},{y:.4f}")

# ---------------- flap frequency vs hinge offset ----------------
print("\n### omega_beta/Omega vs e")
for i in range(0, 21):
    e = i * 0.02
    eps = 3 * e / (2 * (1 - e))
    print(f"{e:.2f},{math.sqrt(1 + eps):.4f}")

# ---------------- mu vs reversed flow / tip mach ----------------
print("\n### mu sweep for limit example (R=7.5, Om=28 => OmR=210)")
for Vk in range(0, 320, 20):
    V = Vk / 3.6
    mu = V / OmR
    print(f"{Vk:3d} km/h mu={mu:.3f}  d_rev={mu*R:.2f} m  M_tip={(OmR+V)/340:.3f}  "
          f"U_T_retr={(OmR-V)/340:.3f}")

# ---------------- verify quartic root vs iteration for the worked example
print("\n### check: arctan trim consistency")
V = 0.3 * OmR
Dp = 0.5 * rho * V**2 * f
CH0 = 0.25 * sig * Cd0 * 0.3
alphaT = Dp / W + CH0 / CT
print("alphaT deg =", round(math.degrees(alphaT), 3))
