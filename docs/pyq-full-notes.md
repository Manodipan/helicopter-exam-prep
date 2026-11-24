# Helicopter Engineering — PYQ-based full notes

These notes cover the topics appearing in the uploaded 2023–24 and 2026–27 papers. They are written for understanding and exam answers: **idea → variables → derivation/method → check → memory cue**.

> **Scope note:** The instructor's current guidance for the upcoming exam was one forward-flight numerical (no derivation) and the rest on flapping (derivations and numericals). Older PYQs include a repeated forward-flight blade-element derivation and several other topics. Learn the repeated derivation well enough to understand it, but prioritize the instructor's current scope if time is short.

## Conventions and symbols

The course notes use the azimuth convention in which

$$
u_T = x+\mu\sin\psi,\qquad u_R=\mu\cos\psi,$$

where \(x=r/R\). Thus \(\psi=90^\circ\) is the advancing side and \(\psi=270^\circ\) the retreating side. Other books may start azimuth at a different blade position or reverse its direction; their sine/cosine signs can differ while the physics is the same. In an exam, draw the direction arrows and use the instructor's convention consistently.

| Symbol | Meaning |
|---|---|
| \(R, A=\pi R^2\) | Rotor radius and disk area |
| \(B, c, \sigma=Bc/(\pi R)\) | Blade count, chord, rotor solidity |
| \(\Omega, \Omega R\) | Rotor angular speed and tip speed |
| \(V, \mu=V/(\Omega R)\) | Forward speed and advance ratio |
| \(v_i, \lambda_i=v_i/(\Omega R)\) | Induced velocity and induced inflow ratio |
| \(\lambda\) | Total inflow ratio used in a given class formula; often \(\lambda_i+\mu\alpha_T\) for small disk angle |
| \(C_T=T/[\rho A(\Omega R)^2]\) | Thrust coefficient |
| \(a=dC_l/d\alpha\) | Section lift-curve slope, per radian |
| \(\theta,\alpha,\beta\) | Blade pitch, section angle of attack, flap angle |
| \(\psi, x=r/R\) | Blade azimuth and nondimensional radius |
| \(\gamma=\rho a cR^4/I_\beta\) | Lock number; aerodynamic forcing relative to flap inertia |
| \(I_\beta=\int y^2dm\) | Flapping moment of inertia about the hinge |

Use SI units consistently. In aerodynamic formulae, angles are in radians unless explicitly converted.

---

# 1. Dissymmetry of lift in forward flight ★

## Idea

A blade moving forward sees a larger relative speed on the advancing side than on the retreating side. Since dynamic pressure varies with speed squared, equal blade pitch would produce unequal lift. The resulting left–right lift imbalance would roll the helicopter.

At a simple front/rear-free picture level:

$$U_{\rm adv}\simeq \Omega r+V,\qquad U_{\rm ret}\simeq \Omega r-V,\qquad dL\propto U^2.$$

Thus the advancing side initially produces more lift.

## How the rotor responds

- Advancing blade: excess lift makes it flap up.
- Retreating blade: reduced lift makes it flap down.
- Flapping changes the blade's vertical velocity and angle of attack, tending to reduce the original lift difference.
- Cyclic pitch can add the required once-per-revolution pitch change; the flap response is phase-shifted from the pitch input.

The rotor therefore relieves the dissymmetry by **flapping and cyclic control**, not by the two sides having equal airspeed. In steady flight the rotor finds an equilibrium with the required thrust and moments.

### Exam answer (4-mark shape)

1. State \(U_{\rm adv}>U_{\rm ret}\).
2. Use \(L\sim\tfrac12\rho U^2Sc_l\), so advancing-side lift is initially greater.
3. Explain advancing blade flaps up and retreating blade flaps down; flap velocity changes local angle of attack.
4. State that flapping plus cyclic pitch produces the required balance and avoids an uncorrected rolling moment.

**Analogy:** A fast-moving hand feels more air pressure than a slow-moving hand. A flexible rotor blade responds by moving out of plane, rather than remaining a perfectly rigid disk.

**Memory cue:** **Fast side lifts → flaps up; slow side lifts less → flaps down.** Then mention cyclic control and phase lag.

---

# 2. Gyroscopic effect and precession

A spinning rotor has angular momentum \(\mathbf H=I\boldsymbol\Omega\). A moment changes the direction of \(\mathbf H\), according to

$$\boldsymbol\tau=\frac{d\mathbf H}{dt}=\boldsymbol\Omega_{\rm p}\times\mathbf H.$$

For a simple gyroscope, a moment applied at one point gives a maximum response about 90° later in the direction of rotation. A helicopter rotor is not a perfectly rigid gyroscope—its blades flap and have aerodynamic damping—but the 90° phase idea is a useful first explanation for why a cyclic input does not create maximum disk tilt at the same azimuth.

### Do not overclaim the 90° rule

The exact response phase depends on hinge offset, aerodynamic damping, rotor speed, and the course's azimuth/sign convention. For an ideal centrally hinged rotor, the class model gives a 90° lag. State which model you are using.

**Analogy:** Push the rim of a spinning bicycle wheel; it moves sideways rather than simply in the direction of the push.

**Memory cue:** A rotor's response is **phase-shifted**; name the assumed ideal 90° case, not a universal front/back direction.

---

# 3. Collective and cyclic pitch ★

## Collective pitch

Collective changes every blade's pitch by the same amount. It primarily changes mean blade lift and therefore rotor thrust. Pull collective up → pitch increases → thrust increases → the helicopter tends to climb (subject to power and control balance).

## Cyclic pitch

Cyclic pitch changes blade pitch once per revolution as a function of azimuth. It creates a first-harmonic pitch variation and controls rotor-disk flapping/tilt. It is used to control horizontal acceleration and attitude.

The course form is

$$\theta(\psi)=\theta_0-A_1\cos\psi-B_1\sin\psi.$$

The notes label \(A_1\) as lateral cyclic and \(B_1\) as longitudinal cyclic. Confirm the azimuth arrows in the exam sketch: other conventions can swap the labels or signs.

An equivalent amplitude/phase form is

$$\theta(\psi)=\theta_0-\theta_{cs}\cos(\psi+\phi),$$

where \(\theta_{cs}\) is cyclic amplitude and \(\phi\) sets its azimuthal direction.

For the ideal centrally hinged, 1/rev response used in the class notes,

$$\beta=a_0-a_1\cos\psi-b_1\sin\psi,\qquad A_1=b_1,\qquad B_1=-a_1.$$

This coefficient mapping expresses the 90° response phase under that convention.

**Analogy:** Collective is a shared volume knob; cyclic is a rotating steering input that varies blade pitch around the circle.

**Memory cue:** **Collective = same pitch on all blades. Cyclic = pitch changes with azimuth.**

---

# 4. Forward-flight velocity profiles and reverse flow ★

Let \(x=r/R\) and \(\mu=V/(\Omega R)\). Using the class convention:

$$u_T=x+\mu\sin\psi,\qquad u_R=\mu\cos\psi.$$

Here \(u_T\) is the tangential component in units of \(\Omega R\); \(u_R\) is the radial in-plane component. The local angle of attack also depends on axial inflow and flap velocity.

| Azimuth | Tangential component \(u_T\) | Radial component \(u_R\) | Interpretation |
|---|---:|---:|---|
| \(0^\circ\) | \(x\) | \(+\mu\) | Forward-flow tangential speed is rotational at this azimuth; there is radial cross-flow |
| \(90^\circ\) | \(x+\mu\) | 0 | Advancing side: forward speed adds to rotation |
| \(180^\circ\) | \(x\) | \(-\mu\) | Rotational tangential speed; radial cross-flow reversed |
| \(270^\circ\) | \(x-\mu\) | 0 | Retreating side; inner region can have reversed tangential flow |

At \(270^\circ\), set \(u_T=0\):

$$x=\mu.$$

So along that azimuth the blade's inner portion \(r<\mu R\) has reversed local tangential flow. In the whole rotor disk the boundary is a circle.

## Circle derivation

Write disk-plane coordinates as \(X=r\cos\psi\), \(Y=r\sin\psi\). The zero-tangential-speed boundary is

$$r+\mu R\sin\psi=0.$$

Since \(r=\sqrt{X^2+Y^2}\) and \(r\sin\psi=Y\), squaring gives

$$X^2+Y^2=-\mu RY,$$

or

$$X^2+\left(Y+\frac{\mu R}{2}\right)^2=\left(\frac{\mu R}{2}\right)^2.$$

Thus, for this choice of axes, the reverse-flow region is a circle with:

- radius \(r_{rev}=\mu R/2\);
- diameter \(d_{rev}=\mu R\);
- centre \((X,Y)=(0,-\mu R/2)\).

If the diagram's positive \(Y\) axis is reversed, the centre's sign changes; the radius and diameter do not.

Its area fraction is

$$\frac{\pi(\mu R/2)^2}{\pi R^2}=\frac{\mu^2}{4}.$$

For \(\mu=0.2,0.3,0.4\), this is 1%, 2.25%, and 4% respectively.

**Analogy:** Imagine a spinning record in a breeze. Near the center, the blade's rotational sweep is slow enough that the wind can overwhelm it; farther out, rotation wins.

**Memory cue:** Reverse-flow circle: **diameter \(\mu R\)**, hence area fraction **\(\mu^2/4\)**.

---

# 5. Autorotation

Autorotation is a powered-down descent in which upward airflow through the descending rotor supplies the energy that keeps the rotor turning. The engine is not driving the main rotor; the rotor extracts energy from the airflow and balances aerodynamic drag.

A blade section has three commonly described radial regions:

1. **Driven region**: aerodynamic force has a component that drives rotor rotation.
2. **Driving/autorotative region**: the blade produces useful tangential driving force while contributing to lift.
3. **Stall region**: inner blade sections may be at high angle of attack and contribute drag/stall losses.

Exact region boundaries depend on collective, rotor speed, descent rate, and inflow. In an autorotative steady state, the net aerodynamic torque about the rotor axis is approximately zero and rotor RPM is maintained.

To enter autorotation, collective is lowered to reduce blade pitch and drag; the pilot manages rotor RPM and descent rate, then raises collective near landing to use stored rotor kinetic energy for the flare.

**Analogy:** A windmill can keep spinning without a motor because moving air transfers energy to it. Here the helicopter descends through the air, and the upward flow through the disk sustains rotor rotation.

**Memory cue:** **Engine off; descent airflow on; aerodynamic driving torque balances rotor drag.**

---

# 6. Ground resonance

Ground resonance is a potentially destructive coupling between:

- rotor-blade in-plane lead–lag motion, especially when the blade mass distribution becomes asymmetric; and
- the helicopter fuselage/landing-gear motion while the aircraft is on the ground.

If the coupled frequencies and phase reinforce each other, the oscillation can grow rapidly. Articulated rotors with independent lead–lag hinges are particularly relevant to the classic explanation.

Prevention/response:

- keep lead–lag dampers and landing gear serviceable;
- avoid prolonged ground operation in rotor-speed ranges that excite the mode;
- avoid abrupt ground manoeuvres and landings that initiate blade lag imbalance;
- if resonance develops, follow the aircraft procedure—normally lift off promptly if safe, or shut down; do not remain in the resonant condition.

**Analogy:** Push a playground swing at its natural frequency; each push adds energy. Ground resonance is a rotor–airframe version of that feedback.

**Memory cue:** **Lead–lag imbalance + airframe/gear bounce + frequency coupling = ground resonance.**

---

# 7. Blade-element derivation of forward-flight thrust coefficient ★

This appeared in both papers, so know the derivation and assumptions. Even if the upcoming exam asks only a numerical, the derivation explains where the formula comes from.

## Assumptions

1. Steady, quasi-steady blade-element aerodynamics.
2. Constant chord and no blade twist for this closed-form expression.
3. Linear lift curve: \(C_l=a\alpha\), small angles in radians.
4. Uniform induced inflow \(\lambda\) over the disk.
5. Neglect blade flapping velocity, cyclic pitch, tip/root losses, compressibility, and drag contribution to thrust.
6. Integrate over all blade azimuths and radial stations; use the course definition \(\sigma=Bc/(\pi R)\).

These are modeling assumptions, not statements that the real rotor exactly behaves this way.

## Local blade-element relations

Let \(x=r/R\), \(\mu=V/(\Omega R)\), and let the normalized tangential speed be

$$q=x+\mu\sin\psi.$$

The local tangential speed is \(U_T=\Omega Rq\). For uniform collective \(\theta_0\), the local angle of attack under this simplified model is

$$\alpha\simeq\theta_0-\frac{\lambda}{q}.$$

A small element on one blade has lift

$$dL=\frac12\rho(\Omega R)^2q^2c\,a\alpha\,dr.$$

The vertical component is approximated by lift itself. Sum the blade elements over radius and azimuth, then normalize thrust by \(\rho A(\Omega R)^2\). With \(\sigma=Bc/(\pi R)\), the result is

$$C_T=\frac{\sigma a}{2}\int_0^1\left\langle q^2\alpha\right\rangle_\psi dx,$$

where \(\langle\cdot\rangle_\psi\) denotes the average over one revolution.

Substitute \(\alpha=\theta_0-\lambda/q\):

$$C_T=\frac{\sigma a}{2}\left[\theta_0\int_0^1\langle q^2\rangle dx-\lambda\int_0^1\langle q\rangle dx\right].$$

Now use

$$\langle q\rangle=x,\qquad \langle q^2\rangle=x^2+\frac{\mu^2}{2},$$

and integrate radially:

$$\int_0^1\langle q^2\rangle dx=\frac13+\frac{\mu^2}{2},\qquad
\int_0^1\langle q\rangle dx=\frac12.$$

Therefore

$$\boxed{C_T=\frac12\sigma a\left[\theta_0\left(\frac13+\frac{\mu^2}{2}\right)-\frac{\lambda}{2}\right]}.$$

For hover, \(\mu=0\):

$$\boxed{C_T=\frac12\sigma a\left(\frac{\theta_0}{3}-\frac{\lambda}{2}\right)}.$$

### Mental derivation path

1. Element lift is proportional to speed squared times angle of attack: \(U_T^2\alpha\).
2. Speed is \(x+\mu\sin\psi\); angle is pitch minus inflow angle.
3. Average over azimuth: \(\langle q\rangle=x\), \(\langle q^2\rangle=x^2+\mu^2/2\).
4. Integrate powers of \(x\): \(\int x^2dx=1/3\), \(\int xdx=1/2\).
5. Multiply by \(\sigma a/2\).

**Memory cue:** **Speed squared gives \(1/3+\mu^2/2\); inflow speed gives \(1/2\).**

---

# 8. Forward-flight numerical toolkit

## Step 1: rotor geometry and speed

$$A=\pi R^2,\quad \Omega=\frac{2\pi N_{rpm}}{60},\quad U_{tip}=\Omega R,\quad \sigma=\frac{Bc}{\pi R},\quad \mu=\frac{V}{\Omega R}.$$

## Step 2: thrust coefficient

If thrust/weight is known:

$$C_T=\frac{T}{\rho A(\Omega R)^2}.$$

For a steady level helicopter, normally \(T\simeq W\), with any disk tilt/vertical force balance treated as specified.

## Step 3: induced velocity and inflow

For the forward-flight momentum relation used in the class notes,

$$T=2\rho A v_i\sqrt{V^2+v_i^2}.$$

With \(v_h=\sqrt{T/(2\rho A)}\), solve

$$\left(\frac{v_i}{v_h}\right)^4+\left(\frac{V}{v_h}\right)^2\left(\frac{v_i}{v_h}\right)^2-1=0,$$

or use the positive root

$$\left(\frac{v_i}{v_h}\right)^2=\frac{-k+\sqrt{k^2+4}}{2},\qquad k=(V/v_h)^2.$$

Then \(\lambda_i=v_i/(\Omega R)\). If the disk is tilted by a small angle \(\alpha_T\), the course approximation is \(\lambda\simeq\lambda_i+\mu\alpha_T\).

## Step 4: blade-element coefficients

Use the thrust relation above to find \(\theta_0\) if needed, then class flapping relations:

$$a_0=\frac{\gamma}{8}\left[\theta_0(1+\mu^2)-\frac43\lambda\right],$$

$$a_1=\frac{\mu(\frac83\theta_0-2\lambda)}{1-\mu^2/2},\qquad
b_1=\frac{\frac43\mu a_0}{1+\mu^2/2}.$$

Check the class's definitions of \(\lambda\), cyclic signs, and angle convention before substitution.

## PYQ example: Q5(a), 2023–24

Given \(R=2\,m\), \(B=3\), \(V=20\,m/s\), \(v_i=1.5\,m/s\), \(N=250\,rpm\), sea level, use the supplied momentum expression:

$$A=\pi(2)^2=12.566\,m^2,\qquad \Omega=26.18\,rad/s.$$

$$T=2(1.225)(12.566)(1.5)\sqrt{20^2+1.5^2}\simeq926\,N.$$

$$C_T=\frac{926}{1.225(12.566)(26.18\cdot2)^2}\simeq 0.02195.$$

This uses the PYQ's forward-flight momentum relation and provided inflow; a different convention for the oblique-disk velocity needs to be followed if explicitly stated.

---

# 9. Forward-flight cyclic and lift-slope numericals

## Cyclic coefficients workflow (2023–24 Q5b)

1. Convert rpm to \(\Omega\), find \(\Omega R\), and calculate \(\mu\).
2. Find \(C_T\) from momentum or supplied thrust/weight.
3. Find \(\lambda_i\) from induced velocity; include disk-angle contribution if the course formula specifies it.
4. Find collective \(\theta_0\) from the thrust coefficient equation.
5. Use the class flapping relations to obtain \(a_1,b_1\), and then map to cyclic coefficients using the stated convention.
6. Convert radians to degrees only at the end.

For the course convention in these notes: \(A_1=b_1\) (lateral) and \(B_1=-a_1\) (longitudinal). State the convention in your answer.

## Find lift-curve slope (2026–27 Q4)

Given \(C_T\), use the same blade-element integral but retain the actual radial pitch/twist distribution:

$$C_T=\frac{\sigma a}{2}\int_0^1\left\langle q^2\alpha(x,\psi)\right\rangle dx.$$

Write \(\alpha(x,\psi)=\theta(x)-\phi(x,\psi)\), calculate the integral factor \(J\), and solve

$$a=\frac{2C_T}{\sigma J}.$$

If the paper assumes linear pitch \(\theta(x)=\theta_0+\theta_{tw}x\) and uniform inflow, the integral becomes

$$J=\theta_0\left(\frac13+\frac{\mu^2}{2}\right)
+\theta_{tw}\left(\frac14+\frac{\mu^2}{4}\right)-\frac{\lambda}{2}.$$

If it explicitly permits uniform angle of attack \(\alpha_0\), then \(J=\alpha_0(1/3+\mu^2/2)\) in the simplest model. But a stated 5° twist means pitch varies with radius; do not silently treat it as uniform angle of attack.

For Q4 (2026–27), the unambiguous geometry gives \(\Omega=20.94\,rad/s\), \(\Omega R=41.89\,m/s\), \(\mu\approx0.430\), and \(\sigma\approx0.0796\). With the 5° disk angle and given \(v_i=1\,m/s\), the course approximation is \(\lambda\simeq v_i/(\Omega R)+\mu\sin5^\circ\approx0.0613\). Then apply the linear-twist expression and solve \(a=2C_T/(\sigma J)\). The scan does not specify clearly whether “uniform twist of 5°” is a root-to-tip change (and its sign) or whether the 5° angle of attack is held uniform despite twist. Those interpretations give different \(J\); ask the instructor which definition was used rather than inventing a unique lift-slope answer.

**Exam trap:** twist is a change in geometric pitch along the blade. It is not automatically the local angle of attack.

---

# 10. Rotor power and parasite drag factor \(f/A\) (2023–24 Q4)

For the class power model,

$$C_Q=\underbrace{\frac18\sigma C_{D0}(1+K_1\mu^2)}_{\text{profile}}
+\underbrace{\kappa\lambda_iC_T}_{\text{induced}}
+\underbrace{\mu\frac{D_p}{W}C_T}_{\text{parasite}},$$

$$P=C_Q\rho A(\Omega R)^3,\qquad D_p=\frac12\rho V^2f.$$

Here \(f\) is equivalent flat-plate area; \(f/A\) is the nondimensional parasite drag factor. For an estimate using the paper data:

1. Calculate \(\Omega,U_{tip},\sigma,\mu,C_T\).
2. Find \(v_i\) from momentum theory and \(\lambda_i\).
3. Convert given power to \(C_Q=P/[\rho A(\Omega R)^3]\).
4. Subtract the profile and induced terms to isolate \(C_{Qp}\).
5. Solve \(C_{Qp}=\mu(D_p/W)C_T\) for \(D_p\), then
   \[
   f/A=\frac{D_p}{\tfrac12\rho V^2 A}.
   \]

### Application to the 2023–24 data

Given \(W=4500g\), \(R=4.5\,m\), \(B=3\), \(c=0.35\,m\), \(N=450\,rpm\), \(V=50\,m/s\), \(C_{D0}=0.012\), and \(P=450\,kW\), the geometric results are approximately

$$\Omega=47.12\,rad/s,\quad U_{tip}=212.1\,m/s,\quad \mu=0.2358,\quad \sigma=0.07427,\quad C_T=0.01260.$$

Using the example model values \(K_1=3\) and \(\kappa=1.2\), and the exact momentum root, the residual parasite term gives approximately \(f/A\approx0.0113\). This is an **assumption-dependent estimate**: if the course prescribes different \(K_1\), induced-power factor \(\kappa\), or inflow approximation, substitute those values; they change the result. Always show the assumed power model.

**Memory cue:** **Given total power → subtract profile and induced → parasite leftover → invert drag equation.**

---

# 11. Vertical climb rate (2026–27 Q3)

The available power is just enough to hover at 1500 kg. In vertical climb at 1300 kg, use the excess power after accounting for the lower-weight rotor's profile and induced power.

A common simple model is

$$P_{hover}=P_0+T v_h,
\qquad v_h=\sqrt{\frac{T}{2\rho A}},$$

where \(P_0\) is profile power. For uniform hover loading,

$$C_T=\frac{T}{\rho A(\Omega R)^2},\quad C_{L,mean}\simeq\frac{6C_T}{\sigma},\quad C_D=0.08+0.012C_{L,mean}^2,$$

$$C_{P0}\simeq\frac{\sigma C_D}{8},\qquad P_0=C_{P0}\rho A(\Omega R)^3.$$

In climb, ideal momentum gives

$$T=2\rho A v_i(v_i+V_c),\qquad P_{ideal}=T(v_i+V_c)=Tv_i+TV_c.$$

Procedure:

1. Use the 1500 kg hover condition to calculate available power \(P_A=P_{hover,1500}\).
2. At 1300 kg calculate thrust, \(C_T,C_L,C_D\), and climb profile power \(P_{0,1300}\).
3. Let \(Q=(P_A-P_{0,1300})/T_{1300}=v_i+V_c\).
4. From momentum, \(v_i=T/(2\rho A Q)\); then \(V_c=Q-v_i\).

Using sea-level density, ideal induced power (\(\kappa=1\)), and this uniform-blade approximation gives approximately:

- \(\sigma\approx0.0521\), \(U_{tip}\approx172.8\,m/s\);
- available hover power at 1500 kg \(\approx441\,kW\);
- climb rate at 1300 kg \(V_c\approx3.6\,m/s\).

This numerical answer depends on the problem's intended meaning of “total drag coefficient” and whether an empirical induced-power factor is prescribed. In the exam, use the lecturer's taught drag/power formula, state the ideal/empirical assumption, and keep \(TV_c\) separate from induced power.

**Analogy:** The engine's power budget is fixed. A lighter helicopter spends less on supporting weight; the remaining power buys altitude.

---

# 12. Steady vertical descent induced power (2026–27 Q5)

Take upward climb speed as positive. Let the helicopter descend at speed \(V_d>0\). In the normal working branch of axial momentum theory,

$$T=2\rho A v_i(v_i-V_d).$$

The question says \(V_d=v_i/3\), so

$$T=2\rho A v_i\left(v_i-\frac{v_i}{3}\right)
=\frac43\rho A v_i^2,$$

$$\boxed{v_i=\sqrt{\frac{3T}{4\rho A}}}.$$

For \(m=1000\,kg\), \(R=4\,m\), sea level, \(T\simeq mg=9810\,N\), \(A=50.27\,m^2\):

$$v_i\approx10.93\,m/s,\qquad V_d\approx3.64\,m/s.$$

If “induced power” means the induced component \(P_i=T v_i\),

$$\boxed{P_i\approx107.2\,kW}.$$

The ideal net rotor power in the axial momentum balance is \(T(v_i-V_d)=\tfrac23Tv_i\approx71.5\,kW\). These are different quantities: **induced component** versus **net shaft power in descent**. Write the definition your course uses. If the intended question instead says descent speed is one-third of hover induced velocity, the equation and result differ.

**Memory cue:** In descent, don't use the climb sign: replace \(V_c\) by \(-V_d\), then apply the stated relation.

---

# 13. Coning in hover: physics and excessive coning

Lift bends each blade upward. Centrifugal force acting through the flapped blade supplies a restoring tendency. At equilibrium, lift moment and centrifugal restoring moment balance, producing a steady coning angle \(\beta_0\).

For a simplified centrally hinged blade, use the course approximation

$$\beta_0\simeq\frac{T_{blade}}{C_F},\qquad C_F=\int\Omega^2r\,dm.$$

For a uniform blade of mass per unit length \(m'\),

$$C_F=m'\Omega^2\int_0^Rr\,dr=\frac12m'\Omega^2R^2.$$

A tip mass \(m_t\) adds \(m_t\Omega^2R\). Thus

$$C_F=\frac12m'\Omega^2R^2+m_t\Omega^2R.$$

### 2023–24 coning numerical

Given 3 blades, mass \(3000\,kg\), \(R=5\,m\), distributed mass \(m'=4\,kg/m\), tip mass \(5\,kg\), and 350 rpm:

$$\Omega=36.65\,rad/s,\qquad T_{blade}=\frac{3000(9.81)}{3}=9810\,N.$$

$$C_F=\frac12(4)(36.65)^2(5)^2+(5)(36.65)^2(5)\approx100.75\,kN.$$

$$\beta_0\simeq9810/100752=0.0974\,rad\simeq5.58^\circ.$$

Use this as the simplified class estimate; if the problem defines a different lift moment arm or a different centrifugal-force quantity, show that specified balance instead.

### Why excessive coning is bad

Large coning reduces the effective rotor-disk angle/vertical thrust component, increases blade/hinge structural loads, can reduce clearance, and signals excessive loading or low rotor speed. The exact consequences depend on design; keep the answer tied to rotor geometry and loads.

**Analogy:** A rotating flexible ruler bends outward under load until lift and centrifugal restoring effects balance.

**Memory cue:** **More thrust per blade → more flap/cone; more centrifugal restoring capacity → less cone.**

---

# 14. Flapping equation and the \(\tau=I\alpha\) interpretation

For a blade element at distance \(y\) from the flap hinge, flap angular acceleration \(\ddot\beta\) produces tangential acceleration \(y\ddot\beta\). Its inertial force is \(dm\,y\ddot\beta\); multiply by the moment arm \(y\) to get an inertial torque \(y^2dm\ddot\beta\). Summing gives

$$I_\beta=\int y^2dm,\qquad \tau_{inertia}=I_\beta\ddot\beta.$$

Aerodynamic lift moment is \(\tau_{aero}=\int y\,dL\). For small flap angle, centrifugal force gives a restoring torque approximately \(I_\beta\Omega^2\beta\). Therefore

$$\tau_{aero}-\tau_{restore}=I_\beta\ddot\beta,$$

or, with restoring torque shown as a positive magnitude on the right,

$$\boxed{\int y\,dL=I_\beta\ddot\beta+I_\beta\Omega^2\beta.}$$

With \(\psi=\Omega t\), \(\ddot\beta=\Omega^2\beta''\). The central-hinge simplified equation is

$$\beta''+\beta=\frac{M_{aero}}{I_\beta\Omega^2}.$$

The full class forward-flight integration gives the coefficient relations in the formula card/Section 8. The short memory line is

$$\boxed{\text{net flap torque}=I_\beta\times\text{flap angular acceleration}.}$$

The \(I_\beta\Omega^2\beta\) term is a restoring torque, not a second \(I\alpha\) term.

---

# 15. Flap hinge offset and natural frequency

Let \(e\) be the dimensionless hinge offset (physical offset divided by rotor radius). The class equation for free flapping is

$$\ddot\beta+\Omega^2(1+\varepsilon)\beta=0,\qquad
\varepsilon=\frac{3e}{2(1-e)}.$$

Compare with a simple oscillator, \(\ddot\beta+\omega_\beta^2\beta=0\). Hence

$$\omega_\beta=\Omega\sqrt{1+\varepsilon}
=\Omega\sqrt{\frac{2+e}{2(1-e)}}.$$

At zero offset \(e=0\), \(\omega_\beta=\Omega\), the 1/rev condition. For positive offset, frequency rises. To show monotonically:

$$\frac{d}{de}\left(\frac{\omega_\beta^2}{\Omega^2}\right)
=\frac{d}{de}\left(\frac{2+e}{2(1-e)}\right)
=\frac{3}{2(1-e)^2}>0.$$

So larger positive offset gives larger flap natural frequency in this model.

A more complete damped/forced equation in the notes is

$$\beta''+\omega_\beta^2\beta=\frac{\gamma}{8}(C_1\theta-C_2\beta'),
\quad C_1=1-\frac43e,\quad C_2=1-\frac83e.$$

The offset correction to aerodynamic damping used in the notes is

$$\eta=\frac{(1-e)^3(3+e)}{3},\qquad
\xi=\frac{\gamma\eta}{16\sqrt{1+\varepsilon}},\qquad
\varepsilon=\frac{3e}{2(1-e)}.$$

Here \(\eta\) reduces the effective damping as offset increases; \(\xi\) is the corresponding nondimensional damping measure in the course formula. For example, \(e=0.06,\gamma=6\) gives \(\eta\approx0.8472\), \(\omega_\beta/\Omega\approx1.0468\), and \(\xi\approx0.3035\). Do not confuse this expression with the no-offset damping estimate \(\gamma/16\), or use radians/degrees inconsistently.

**Analogy:** Moving the hinge outward changes the centrifugal restoring leverage, like stiffening a spring; the flap oscillation speeds up.

**Memory cue:** **Offset adds restoring stiffness → natural frequency rises.** At \(e=0\), recover \(\omega_\beta=\Omega\).

---

# 16. Lead–lag hinge

Flapping is out-of-plane; lead–lag is in-plane motion along the rotor's direction of rotation. Blades need lead–lag freedom because their in-plane velocity changes as they flap and as the rotor accelerates/decelerates. Without accommodation, large Coriolis/in-plane forces would be carried by the blade root and hub.

A lead–lag hinge (and damper) allows controlled in-plane motion and dissipates oscillatory energy. It reduces structural loads but introduces the possibility of ground resonance if blade lag motion couples with the fuselage/landing gear.

When a blade flaps while rotating, its radial distance from the shaft changes. Conservation of angular momentum in the rotating system produces a Coriolis acceleration proportional to the product of flap and in-plane (lead–lag) rates; the associated Coriolis force is often written in magnitude as \(F_{cor}=2m\Omega v_r\), where \(v_r\) is the radial velocity of the blade element. In a real blade this load is distributed along the span and is reacted through the lead–lag system and blade root. The simple exam point: **flapping motion can generate in-plane Coriolis loads**, which is another reason the blade needs lead–lag freedom.

**Memory cue:** **Flap = up/down; lead–lag = forward/back in rotor plane; changing radial motion in a rotating frame creates Coriolis load.**

---

# 17. Backward and lateral rotor-disc tilt

A centrally hinged rotor disk in forward flight may tilt backward and sideways because blade flapping is a response to azimuth-varying aerodynamic loads, with a phase relation set by rotor dynamics.

- Forward speed makes advancing/retreating dynamic pressure unequal.
- The blade flaps up/down in response.
- The maximum flap response occurs at an azimuth displaced from the maximum aerodynamic forcing (90° in the ideal centrally hinged class model).
- The combined flap harmonics set the disk's longitudinal and lateral tilt.

For the class form \(\beta=a_0-a_1\cos\psi-b_1\sin\psi\), the constant term is coning; the first harmonics are the two orthogonal tilts. Draw a disk top view, label nose/tail and advancing/retreating sides, then show the flap-up/down extrema. Explain the phase; do not assert a direction without the course azimuth convention.

**Memory cue:** **Forward-flight asymmetry creates 1/rev forcing; phase-shifted flap creates disk tilt.**

---

# 18. Formula and sanity-check sheet

$$\mu=\frac{V}{\Omega R},\qquad \sigma=\frac{Bc}{\pi R},\qquad C_T=\frac{T}{\rho A(\Omega R)^2},\qquad \lambda_i=\frac{v_i}{\Omega R}.$$

$$C_T=\frac12\sigma a\left[\theta_0\left(\frac13+\frac{\mu^2}{2}\right)-\frac{\lambda}{2}\right].$$

$$a_0=\frac{\gamma}{8}\left[\theta_0(1+\mu^2)-\frac43\lambda\right],\quad
a_1=\frac{\mu(\frac83\theta_0-2\lambda)}{1-\mu^2/2},\quad
b_1=\frac{\frac43\mu a_0}{1+\mu^2/2}.$$

$$C_F=\frac12m'\Omega^2R^2+m_t\Omega^2R,\qquad \beta_0\simeq\frac{T_{blade}}{C_F}.$$

$$\omega_\beta=\Omega\sqrt{\frac{2+e}{2(1-e)}},\qquad
\text{reverse-flow area fraction}=\frac{\mu^2}{4}.$$

### Sanity checks

- \(\mu=0\) (hover) should make first-harmonic forward-flight terms vanish in the simple model.
- A positive lift increase should increase thrust/coning, all else equal.
- \(C_T\), \(\mu\), \(\sigma\), and \(\lambda\) are dimensionless.
- Use radians inside lift-slope and small-angle formulae.
- \(\tau\) has units N·m; \(I\ddot\beta\) also has units N·m.
- Forward-flight disk angle adds a vertical inflow contribution; do not mix degrees and radians.
- State the sign/azimuth convention whenever identifying longitudinal/lateral cyclic or flap phase.
