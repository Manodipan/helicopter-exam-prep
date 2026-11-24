"""Emit ready-to-paste SVG snippets (dark theme) with exact, computed geometry."""
import math

OUT = {}
A = '#4cc2ff'; B = '#ffb02e'; C = '#39d98a'; D = '#ff6b6b'; V = '#b98cff'
GRID = '#1e2b3d'; INK = '#8ea3bb'; LBL = '#c9d8e8'

# ------------------------------------------------------------------ 1. power curve
W, R, N, c, a, Cd0, Om, f = 58900.0, 7.5, 4, 0.5, 5.7, 0.012, 28.0, 2.5
rho = 1.225
A_d = math.pi * R**2; OmR = Om * R
sig = N * c / (math.pi * R); CT = W / (rho * A_d * OmR**2)
vh = math.sqrt(W / (2 * rho * A_d)); Pscale = rho * A_d * OmR**3
def vi_exact(Vb, vhb):
    kb = (Vb / vhb) ** 2
    return math.sqrt((-kb + math.sqrt(kb ** 2 + 4)) / 2) * vhb
pts = []
for i in range(0, 101):
    Vf = i * 0.95
    mu = Vf / OmR
    if Vf < 1e-9:
        vi, alT = vh, 0.0
    else:
        vi = vi_exact(Vf, vh); alT = 0.5 * rho * Vf ** 2 * f / W
    lam = vi / OmR + mu * alT
    CQ0 = sig * Cd0 * (1 + 3 * mu ** 2) / 8
    CQi = 1.2 * lam * CT
    CQp = mu * alT * CT
    pts.append((Vf, CQ0 * Pscale / 1e3, CQi * Pscale / 1e3, CQp * Pscale / 1e3,
                (CQ0 + CQi + CQp) * Pscale / 1e3))

W0, H0 = 760, 380
ML, MR, MT, MB = 58, 16, 16, 46
def X(v): return ML + (v / 100.0) * (W0 - ML - MR)
def Y(p): return H0 - MB - (p / 1900.0) * (H0 - MT - MB)
def path(idx):
    return " ".join(f"{'M' if k == 0 else 'L'}{X(r[0]):.1f},{Y(r[idx]):.1f}" for k, r in enumerate(pts))

g = [f'<svg viewBox="0 0 {W0} {H0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{H0}" fill="#0f1620"/>')
for v in range(0, 101, 20):
    g.append(f'<line x1="{X(v):.1f}" y1="{MT}" x2="{X(v):.1f}" y2="{H0-MB}" stroke="{GRID}"/>')
    g.append(f'<text x="{X(v):.1f}" y="{H0-MB+18}" fill="{INK}" font-size="12" text-anchor="middle">{v}</text>')
for p in range(0, 1900, 500):
    g.append(f'<line x1="{ML}" y1="{Y(p):.1f}" x2="{W0-MR}" y2="{Y(p):.1f}" stroke="{GRID}"/>')
    g.append(f'<text x="{ML-8}" y="{Y(p)+4:.1f}" fill="{INK}" font-size="12" text-anchor="end">{p}</text>')
g.append(f'<line x1="{ML}" y1="{H0-MB}" x2="{W0-MR}" y2="{H0-MB}" stroke="#44556b"/>')
g.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{H0-MB}" stroke="#44556b"/>')
g.append(f'<text x="{(ML+W0-MR)/2}" y="{H0-8}" fill="{LBL}" font-size="13" text-anchor="middle">forward speed V  (m/s)</text>')
g.append(f'<text x="18" y="28" fill="{LBL}" font-size="13">power (kW)</text>')
for idx, col, name in [(4, '#ffffff', 'Total'), (1, A, 'Profile'), (2, C, 'Induced'), (3, B, 'Parasite')]:
    g.append(f'<path d="{path(idx)}" fill="none" stroke="{col}" stroke-width="{2.6 if idx==4 else 1.9}" '
             f'stroke-linecap="round" opacity="{1 if idx==4 else .92}"/>')
# markers
for idx, col, tx, ty in [(2, C, 42, 300), (3, B, 70, 430), (1, A, 66, 210), (4, '#fff', 55, 900)]:
    v, p = (40 if idx != 3 else 70), (pts[int(40/0.95)][idx] if idx != 3 else pts[int(70/0.95)][idx])
    if idx == 4:
        v, p = 35, pts[int(35/0.95)][4]
    g.append(f'<circle cx="{X(v):.1f}" cy="{Y(p):.1f}" r="4" fill="#0f1620" stroke="{col}" stroke-width="2"/>')
    g.append(f'<text x="{X(v)+9:.1f}" y="{Y(p)-7:.1f}" fill="{col}" font-size="12.5">{name}</text>')
# min power annotation
g.append(f'<line x1="{X(35):.1f}" y1="{Y(615):.1f}" x2="{X(35):.1f}" y2="{H0-MB}" stroke="{D}" stroke-width="1" stroke-dasharray="3 4" opacity=".8"/>')
g.append(f'<text x="{X(35)+7:.1f}" y="{Y(615)-22:.1f}" fill="{D}" font-size="11.5">min power ≈ 35 m/s</text>')
g.append(f'<text x="{X(6):.1f}" y="{Y(1079)-8:.1f}" fill="#8ea3bb" font-size="11.5">hover: 1080 kW</text>')
g.append('</svg>')
OUT['power'] = "\n".join(g)

# ------------------------------------------------------------------ 2. vi/vh curve
W0, H0 = 620, 360
ML, MR, MT, MB = 58, 20, 18, 46
def X2(v): return ML + (v / 5.2) * (W0 - ML - MR)
def Y2(p): return H0 - MB - (p / 1.05) * (H0 - MT - MB)
g = [f'<svg viewBox="0 0 {W0} {H0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{H0}" fill="#0f1620"/>')
for v in [0, 1, 2, 3, 4, 5]:
    g.append(f'<line x1="{X2(v):.1f}" y1="{MT}" x2="{X2(v):.1f}" y2="{H0-MB}" stroke="{GRID}"/>')
    g.append(f'<text x="{X2(v):.1f}" y="{H0-MB+18}" fill="{INK}" font-size="12" text-anchor="middle">{v}</text>')
for p in [0, .25, .5, .75, 1.0]:
    g.append(f'<line x1="{ML}" y1="{Y2(p):.1f}" x2="{W0-MR}" y2="{Y2(p):.1f}" stroke="{GRID}"/>')
    g.append(f'<text x="{ML-8}" y="{Y2(p)+4:.1f}" fill="{INK}" font-size="12" text-anchor="end">{p:g}</text>')
g.append(f'<line x1="{ML}" y1="{H0-MB}" x2="{W0-MR}" y2="{H0-MB}" stroke="#44556b"/>')
g.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{H0-MB}" stroke="#44556b"/>')
g.append(f'<text x="{(ML+W0-MR)/2}" y="{H0-8}" fill="{LBL}" font-size="13" text-anchor="middle">V / v\u2095</text>')
g.append(f'<text x="14" y="30" fill="{LBL}" font-size="13">v\u1d62 / v\u2095</text>')
ex = " ".join(f"{'M' if k==0 else 'L'}{X2(k*0.13):.1f},{Y2(math.sqrt((-(k*0.13)**2+math.sqrt((k*0.13)**4+4))/2)):.1f}" for k in range(0, 41))
gl = " ".join(f"{'M' if k==0 else 'L'}{X2(k*0.13):.1f},{Y2(1/math.sqrt(1+(k*0.13)**2)):.1f}" for k in range(0, 41))
g.append(f'<path d="{gl}" fill="none" stroke="{B}" stroke-width="2" stroke-dasharray="6 4"/>')
g.append(f'<path d="{ex}" fill="none" stroke="{A}" stroke-width="2.8" stroke-linecap="round"/>')
g.append(f'<circle cx="{X2(5.0):.1f}" cy="{Y2(0.1998):.1f}" r="4" fill="#0f1620" stroke="{A}" stroke-width="2"/>')
g.append(f'<text x="{X2(3.4):.1f}" y="{Y2(0.28):.1f}" fill="{A}" font-size="12.5">exact (quartic) — what sir derived</text>')
g.append(f'<text x="{X2(0.75):.1f}" y="{Y2(0.90):.1f}" fill="{B}" font-size="12.5">Glauert  v\u1d62 = v\u2095² / V</text>')
g.append(f'<text x="{X2(0.05):.1f}" y="{Y2(1.02):.1f}" fill="{C}" font-size="11.5">hover = 1</text>')
g.append('</svg>')
OUT['vi'] = "\n".join(g)

# ------------------------------------------------------------------ 3. flap frequency
W0, H0 = 560, 340
ML, MR, MT, MB = 62, 20, 18, 46
def X3(e): return ML + (e / 0.4) * (W0 - ML - MR)
def Y3(w): return H0 - MB - ((w - 0.98) / (1.44 - 0.98)) * (H0 - MT - MB)
g = [f'<svg viewBox="0 0 {W0} {H0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{H0}" fill="#0f1620"/>')
for e in [0, .1, .2, .3, .4]:
    g.append(f'<line x1="{X3(e):.1f}" y1="{MT}" x2="{X3(e):.1f}" y2="{H0-MB}" stroke="{GRID}"/>')
    g.append(f'<text x="{X3(e):.1f}" y="{H0-MB+18}" fill="{INK}" font-size="12" text-anchor="middle">{e:.1f}</text>')
for w in [1.0, 1.1, 1.2, 1.3, 1.4]:
    g.append(f'<line x1="{ML}" y1="{Y3(w):.1f}" x2="{W0-MR}" y2="{Y3(w):.1f}" stroke="{GRID}"/>')
    g.append(f'<text x="{ML-8}" y="{Y3(w)+4:.1f}" fill="{INK}" font-size="12" text-anchor="end">{w:.1f}</text>')
g.append(f'<line x1="{ML}" y1="{H0-MB}" x2="{W0-MR}" y2="{H0-MB}" stroke="#44556b"/>')
g.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{H0-MB}" stroke="#44556b"/>')
g.append(f'<text x="{(ML+W0-MR)/2}" y="{H0-8}" fill="{LBL}" font-size="13" text-anchor="middle">hinge offset  e = e\u1d63/R</text>')
g.append(f'<text x="12" y="30" fill="{LBL}" font-size="13">\u03c9\u03b2 / \u03a9</text>')
fp = " ".join(f"{'M' if k==0 else 'L'}{X3(k*0.01):.1f},{Y3(math.sqrt(1+3*(k*0.01)/(2*(1-k*0.01)))):.1f}" for k in range(0, 41))
g.append(f'<path d="{fp}" fill="none" stroke="{V}" stroke-width="2.7" stroke-linecap="round"/>')
g.append(f'<line x1="{ML}" y1="{Y3(1.0):.1f}" x2="{W0-MR}" y2="{Y3(1.0):.1f}" stroke="{C}" stroke-dasharray="5 4" stroke-width="1.4"/>')
g.append(f'<text x="{X3(0.26):.1f}" y="{Y3(1.005):.1f}" fill="{C}" font-size="11.5">e = 0 → ω = Ω (exactly resonant)</text>')
for e in [0.04, 0.1]:
    w = math.sqrt(1+3*e/(2*(1-e)))
    g.append(f'<circle cx="{X3(e):.1f}" cy="{Y3(w):.1f}" r="4" fill="#0f1620" stroke="{V}" stroke-width="2"/>')
    g.append(f'<text x="{X3(e)+7:.1f}" y="{Y3(w)-7:.1f}" fill="{V}" font-size="11.5">{w:.3f} at e={e}</text>')
g.append('</svg>')
OUT['freq'] = "\n".join(g)

# ------------------------------------------------------------------ 4. rotor disc planform
W0 = 520
cx, cy, r = 250, 250, 170
g = [f'<svg viewBox="0 0 {W0} {W0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{W0}" fill="#0f1620"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#141d29" stroke="#3c5064" stroke-width="2"/>')
# advancing half shading
g.append(f'<path d="M {cx} {cy-r} A {r} {r} 0 0 1 {cx} {cy+r} Z" fill="{A}" opacity="0.10"/>')
# reversed flow region
rr = 0.3 * r
g.append(f'<circle cx="{cx-rr}" cy="{cy}" r="{rr}" fill="{D}" opacity="0.22" stroke="{D}" stroke-width="1.4" stroke-dasharray="4 3"/>')
# arrows
g.append(f'<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
         f'<path d="M0,0 L9,4.5 L0,9 z" fill="{B}"/></marker>'
         f'<marker id="arb" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
         f'<path d="M0,0 L9,4.5 L0,9 z" fill="{A}"/></marker></defs>')
g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-160}" stroke="{B}" stroke-width="2.4" marker-end="url(#ar)"/>')
g.append(f'<text x="{cx+8}" y="{cy-150}" fill="{B}" font-size="13">V (flight)</text>')
# rotation arc
g.append(f'<path d="M {cx-95} {cy-140} A {r+28} {r+28} 0 0 1 {cx+95} {cy-140}" fill="none" stroke="{A}" stroke-width="2" marker-end="url(#arb)"/>')
g.append(f'<text x="{cx}" y="{cy-r-34}" fill="{A}" font-size="13" text-anchor="middle">Ω</text>')
g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+118}" y2="{cy}" stroke="{C}" stroke-width="2" marker-end="url(#ar)"/>')
g.append(f'<text x="{cx+124}" y="{cy+5}" fill="{C}" font-size="13">ψ = 90° advancing</text>')
g.append(f'<text x="{cx-206}" y="{cy+5}" fill="{D}" font-size="12.5">ψ = 270°</text>')
g.append(f'<text x="{cx-200}" y="{cy+22}" fill="{D}" font-size="12.5">retreating</text>')
g.append(f'<text x="{cx}" y="{cy+r+34}" fill="{LBL}" font-size="12.5" text-anchor="middle">ψ measured from the rear (trailing) blade position</text>')
g.append(f'<text x="{cx}" y="{cy+r+54}" fill="{D}" font-size="12.5" text-anchor="middle">reversed flow: r &lt; μR (diameter = μ·2R... see note)</text>')
g.append(f'<text x="{cx-rr}" y="{cy+rr+18}" fill="{D}" font-size="12" text-anchor="middle">U\u209c = 0</text>')
g.append('</svg>')
OUT['disc'] = "\n".join(g)

# ------------------------------------------------------------------ 5. flapping geometry side view (T_e formula)
W0, H0 = 640, 320
g = [f'<svg viewBox="0 0 {W0} {H0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{H0}" fill="#0f1620"/>')
O = (120, 230)
be = math.radians(12)
L = 470
tip = (O[0] + L * math.cos(be), O[1] - L * math.sin(be))
g.append(f'<line x1="{O[0]}" y1="{H0-30}" x2="{O[0]}" y2="40" stroke="#44556b" stroke-width="2" stroke-dasharray="6 4"/>')
g.append(f'<text x="{O[0]-4}" y="34" fill="{INK}" font-size="12" text-anchor="end">shaft</text>')
g.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{tip[0]:.0f}" y2="{tip[1]:.0f}" stroke="#cbd9e8" stroke-width="7" stroke-linecap="round"/>')
# hinge offset e
g.append(f'<circle cx="{O[0]+28}" cy="{O[1]-6}" r="5" fill="{B}"/>')
g.append(f'<text x="{O[0]+34}" y="{O[1]+24}" fill="{B}" font-size="12">hinge, offset eR</text>')
# beta arc
g.append(f'<path d="M {O[0]+120} {O[1]} A 120 120 0 0 0 {O[0]+120*math.cos(be):.1f} {O[1]-120*math.sin(be):.1f}" fill="none" stroke="{A}" stroke-width="1.6"/>')
g.append(f'<text x="{O[0]+126}" y="{O[1]-30}" fill="{A}" font-size="14">β</text>')
g.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{O[0]+L}" y2="{O[1]}" stroke="#44556b" stroke-dasharray="5 4"/>')
# lift arrow + CF
mx = O[0] + L * 0.62 * math.cos(be); my = O[1] - L * 0.62 * math.sin(be)
g.append(f'<line x1="{mx:.0f}" y1="{my:.0f}" x2="{mx:.0f}" y2="{my-74:.0f}" stroke="{C}" stroke-width="2.6" marker-end="url(#ar)"/>')
g.append(f'<text x="{mx+8:.0f}" y="{my-78:.0f}" fill="{C}" font-size="13">dL = ½ρU_T²c·a·α·dr</text>')
g.append(f'<line x1="{mx:.0f}" y1="{my:.0f}" x2="{mx+86:.0f}" y2="{my:.0f}" stroke="{B}" stroke-width="2.4" marker-end="url(#ar)"/>')
g.append(f'<text x="{mx+90:.0f}" y="{my-8:.0f}" fill="{B}" font-size="13">CF = m′Ω²r·dr</text>')
g.append(f'<text x="{mx-10:.0f}" y="{my+22:.0f}" fill="{INK}" font-size="13">r</text>')
g.append(f'<line x1="{O[0]+28}" y1="{O[1]+46}" x2="{mx:.0f}" y2="{my+16:.0f}" stroke="#5c7188" stroke-width="1" stroke-dasharray="3 3"/>')
g.append(f'<text x="{W0-14}" y="{H0-14}" fill="{INK}" font-size="11.5" text-anchor="end">take moments about the hinge (not the shaft!)</text>')
g.append('</svg>')
OUT['flapgeo'] = "\n".join(g)

# ------------------------------------------------------------------ 6. azimuth phasing diagram
W0 = 480
cx, cy, r = 240, 240, 150
g = [f'<svg viewBox="0 0 {W0} {W0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{W0}" fill="#0f1620"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#141d29" stroke="#3c5064" stroke-width="1.6"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#67788e"/>')
g.append(f'<text x="{cx}" y="{cy-r-16}" fill="{LBL}" font-size="12.5" text-anchor="middle">ψ = 180° (nose)</text>')
g.append(f'<text x="{cx}" y="{cy+r+22}" fill="{LBL}" font-size="12.5" text-anchor="middle">ψ = 0° (tail)</text>')
g.append(f'<text x="{cx+r+8}" y="{cy+4}" fill="{LBL}" font-size="12.5">ψ = 90°</text>')
g.append(f'<text x="{cx-r-8}" y="{cy+4}" fill="{LBL}" font-size="12.5" text-anchor="end">ψ = 270°</text>')
g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-r}" stroke="#44556b" stroke-dasharray="4 4"/>')
g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+r}" stroke="#44556b" stroke-dasharray="4 4"/>')
g.append(f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="#44556b" stroke-dasharray="4 4"/>')
# max pitch at 90 deg (A1), max flap at 180
g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="{B}" stroke-width="3"/>')
g.append(f'<text x="{cx+r+6}" y="{cy-10}" fill="{B}" font-size="11.5">max cyclic pitch (A₁)</text>')
g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-r}" stroke="{C}" stroke-width="3"/>')
g.append(f'<text x="{cx-6}" y="{cy-r-30}" fill="{C}" font-size="11.5" text-anchor="middle">max flap-up (a₁·cos ψ)</text>')
g.append(f'<path d="M {cx+r*0.86} {cy-r*0.5} A {r*0.99} {r*0.99} 0 0 0 {cx+r*0.5} {cy-r*0.86}" fill="none" stroke="{A}" stroke-width="2" marker-end="url(#arb)"/>')
g.append(f'<text x="{cx+r*0.66}" y="{cy-r*0.78}" fill="{A}" font-size="12">90° lag</text>')
g.append(f'<text x="{cx}" y="{W0-12}" fill="{INK}" font-size="11.5" text-anchor="middle">response lags excitation by 90° (resonance, e = 0)</text>')
g.append('</svg>')
OUT['phase'] = "\n".join(g)

# ------------------------------------------------------------------ 7. coning force diagram
W0, H0 = 520, 360
g = [f'<svg viewBox="0 0 {W0} {H0}" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif,system-ui,sans-serif">']
g.append(f'<rect width="{W0}" height="{H0}" fill="#0f1620"/>')
O = (110, 250)
be = math.radians(14)
L = 330
tip = (O[0] + L * math.cos(be), O[1] - L * math.sin(be))
g.append(f'<line x1="{O[0]}" y1="{H0-40}" x2="{O[0]}" y2="36" stroke="#44556b" stroke-width="2" stroke-dasharray="6 4"/>')
g.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{tip[0]:.0f}" y2="{tip[1]:.0f}" stroke="#cbd9e8" stroke-width="7" stroke-linecap="round"/>')
g.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{O[0]+L}" y2="{O[1]}" stroke="#44556b" stroke-dasharray="5 4"/>')
g.append(f'<path d="M {O[0]+130} {O[1]} A 130 130 0 0 0 {O[0]+130*math.cos(be):.1f} {O[1]-130*math.sin(be):.1f}" fill="none" stroke="{A}" stroke-width="1.6"/>')
g.append(f'<text x="{O[0]+136}" y="{O[1]-34}" fill="{A}" font-size="14">β₀</text>')
mx = O[0] + L * 0.58 * math.cos(be); my = O[1] - L * 0.58 * math.sin(be)
g.append(f'<line x1="{mx:.0f}" y1="{my:.0f}" x2="{mx:.0f}" y2="{my-92:.0f}" stroke="{C}" stroke-width="2.6" marker-end="url(#ar)"/>')
g.append(f'<text x="{mx+7:.0f}" y="{my-96:.0f}" fill="{C}" font-size="13">L (lift)</text>')
g.append(f'<line x1="{mx:.0f}" y1="{my:.0f}" x2="{mx+104:.0f}" y2="{my:.0f}" stroke="{B}" stroke-width="2.6" marker-end="url(#ar)"/>')
g.append(f'<text x="{mx+108:.0f}" y="{my+4:.0f}" fill="{B}" font-size="13">CF = m′Ω²r·dr</text>')
# components of CF
g.append(f'<line x1="{mx:.0f}" y1="{my:.0f}" x2="{mx+104:.0f}" y2="{my+26:.0f}" stroke="{B}" stroke-width="1.5" stroke-dasharray="4 3"/>')
g.append(f'<text x="{mx+50:.0f}" y="{my+46:.0f}" fill="{INK}" font-size="11.5">CF·sinβ ≈ CF·β  (in-plane)</text>')
g.append(f'<text x="{mx-14:.0f}" y="{my+30:.0f}" fill="{INK}" font-size="11.5">CF·cosβ</text>')
g.append(f'<text x="{W0-14}" y="{H0-14}" fill="{INK}" font-size="11.5" text-anchor="end">equilibrium: L·r ≈ CF·β·r  →  β₀ ≈ L/CF</text>')
g.append('</svg>')
OUT['coning'] = "\n".join(g)

if __name__ == '__main__':
    import json
    json.dump(OUT, open('tools/svg_out.json', 'w'), indent=1)
    print({k: len(v) for k, v in OUT.items()})
