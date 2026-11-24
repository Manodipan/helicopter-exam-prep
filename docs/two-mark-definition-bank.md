# Two-mark definition bank — Helicopter Engineering

For tomorrow's expected **50-mark pattern**, prepare the short-answer topics as crisp 2-mark responses. A reliable format is:

> **Define the term in one sentence. Add one mechanism, consequence, or distinguishing feature.**

Avoid a long derivation for 2 marks. A small labelled sketch can replace some words where the question asks for one.

## Rotor and forward-flight basics

### 1. Dissymmetry of lift
**Dissymmetry of lift** is the unequal lift produced on the advancing and retreating sides of a rotor in forward flight because their relative airspeeds differ. Since lift varies approximately with speed squared, the imbalance tends to create a rolling moment; blade flapping and cyclic pitch provide the balancing response.

### 2. Advancing and retreating blades
The **advancing blade** moves in the same direction as the helicopter's forward speed, so its local tangential speed is increased. The **retreating blade** moves against forward speed, so its local tangential speed is reduced and its inboard part may experience reverse flow.

### 3. Reverse-flow region
The **reverse-flow region** is the inner portion of the retreating side where forward-flight velocity exceeds the blade's local rotational tangential velocity, reversing the direction of local flow over the blade. In the ideal disk-plane sketch its boundary is a circle of radius \(\mu R/2\), diameter \(\mu R\), and area fraction \(\mu^2/4\).

### 4. Advance ratio
The **advance ratio** \(\mu=V/(\Omega R)\) is the helicopter forward speed divided by rotor tip speed. It measures how important forward motion is relative to blade rotation and controls the severity of advancing/retreating-side asymmetry.

### 5. Autorotation
**Autorotation** is a rotor state in which upward airflow through a descending helicopter supplies the aerodynamic torque that keeps the main rotor turning, without engine drive. In steady autorotation, aerodynamic driving torque balances rotor drag while the pilot manages rotor speed and descent rate.

### 6. Ground resonance
**Ground resonance** is a growing oscillation caused by coupling between rotor-blade lead–lag motion and fuselage/landing-gear motion while the helicopter is on the ground. If the coupled motion is reinforced near a natural frequency, vibration can become destructive; serviceable dampers and correct operational response help prevent it.

## Controls and rotor response

### 7. Collective pitch
**Collective pitch** changes the pitch angle of all rotor blades by approximately the same amount at the same time. It primarily changes mean rotor thrust; increasing collective generally increases blade angle of attack, lift, and power demand.

### 8. Cyclic pitch
**Cyclic pitch** varies blade pitch once per rotor revolution as a function of azimuth. This creates a periodic lift/flapping response that tilts the rotor thrust vector and controls helicopter attitude and horizontal motion.

### 9. Gyroscopic effect / precession
**Gyroscopic precession** is the change in direction of a spinning rotor's angular-momentum vector when a moment is applied. In the ideal gyroscope model the maximum response is displaced by 90° in the direction of rotation; actual rotor response depends on flapping dynamics and sign convention.

### 10. Flapping
**Flapping** is the out-of-plane angular motion of a rotor blade about its flapping hinge. It lets the rotor accommodate changing aerodynamic loads around the azimuth, including the lift asymmetry of forward flight.

### 11. Coning
**Coning** is the upward cone-shaped deflection of rotor blades in hover or flight, caused by lift acting against centrifugal restoring effects. Its equilibrium angle depends on blade thrust/lift and centrifugal force; excessive coning reduces clearance and raises structural concerns.

### 12. Lead–lag hinge
A **lead–lag hinge** permits a blade to move forward and backward in the rotor plane. It accommodates in-plane motion and reduces loads associated with changing blade speed and flapping; lead–lag damping is also important for ground-resonance control.

### 13. Rotor-disc tilt
**Rotor-disc tilt** is the inclination of the rotor's plane of rotation relative to the nominal plane, produced by cyclic pitch and blade flapping. Its direction and phase depend on the azimuth convention and rotor response; the tilt redirects the rotor thrust vector.

## Flapping dynamics and blade-element quantities

### 14. Flapping hinge offset
**Flapping hinge offset** is the radial distance between the flapping hinge and the rotor shaft, usually written nondimensionally as \(e\). A positive offset increases centrifugal restoring stiffness and therefore raises the blade's flapping natural frequency above the 1/rev value in the class model.

### 15. Flapping natural frequency
The **flapping natural frequency** is the frequency at which a blade oscillates freely in flap after a disturbance. For the course hinge-offset model, \(\omega_\beta=\Omega\sqrt{(2+e)/[2(1-e)]}\), so it equals \(\Omega\) at zero offset and increases with positive offset.

### 16. Lock number
The **Lock number** \(\gamma=\rho a cR^4/I_\beta\) is a nondimensional measure of aerodynamic forcing relative to blade flapping inertia. A larger \(\gamma\) means aerodynamic loads have greater influence on flap response.

### 17. Blade-element theory
**Blade-element theory** divides each rotor blade into small spanwise elements, calculates local aerodynamic force from local velocity and angle of attack, then integrates those forces over blade radius and azimuth to obtain rotor thrust and moments.

### 18. Thrust coefficient
The **thrust coefficient** \(C_T=T/[\rho A(\Omega R)^2]\) is a nondimensional measure of rotor thrust. It allows rotor thrust/loading to be compared independently of the particular size and rotational speed.

### 19. Solidity
**Rotor solidity** \(\sigma=Bc/(\pi R)\) is total blade planform area divided by rotor disk area for constant-chord blades. It measures how much blade area is available to generate aerodynamic force.

### 20. Lift-curve slope
The **lift-curve slope** \(a=dC_l/d\alpha\) is the rate at which a blade section's lift coefficient changes with angle of attack in the linear, attached-flow range. It is normally quoted per radian in rotor equations.

### 21. Blade twist
**Blade twist** is the spanwise variation of blade pitch from root to tip. It is used to tailor spanwise loading; twist changes geometric pitch and is not the same thing as angle of attack.

## Power and performance

### 22. Induced velocity and induced power
**Induced velocity** \(v_i\) is the flow velocity imparted through the rotor disk to produce thrust. The ideal induced-power component is \(P_i=T v_i\) (with empirical corrections such as an induced-power factor when specified); climb or descent power must be kept distinct from this component.

### 23. Parasite drag factor \(f/A\)
The **parasite drag factor** \(f/A\) is equivalent flat-plate fuselage area \(f\) divided by rotor disk area \(A\). It nondimensionally describes fuselage drag relative to rotor size; parasite power grows with forward speed because drag is multiplied by speed.

### 24. Rate of climb
The **rate of climb** \(V_c\) is the helicopter's vertical upward speed. In a steady power balance, excess power above the power needed to support the aircraft is used to gain altitude, approximately \(P_{excess}=W V_c\).

## 2-mark answer cues

- **Dissymmetry:** unequal advancing/retreating speed → unequal lift → flap/cyclic response.
- **Autorotation:** descending airflow drives rotor → aerodynamic torque sustains RPM.
- **Ground resonance:** lead–lag motion couples with landing gear/fuselage → growing oscillation.
- **Collective vs cyclic:** same pitch change on every blade vs pitch varied with azimuth.
- **Coning:** lift bends blades upward; centrifugal effect restores; excessive angle affects clearance/loads.
- **Hinge offset:** offset adds restoring stiffness → flap natural frequency rises.
- **Reverse flow:** inner retreating blade where forward flow overtakes rotation; diameter \(\mu R\).

## Last-minute method

For each definition, say it aloud in **two clauses**: (1) what it is, (2) why it matters. If asked “explain,” add the cause-and-effect arrow. If asked “draw,” sketch the rotor top view, mark nose, tail, advancing side, retreating side, and azimuth before adding arrows.
