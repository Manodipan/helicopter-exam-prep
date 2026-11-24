# Helicopter Engineering PYQ topic checklist

Based on the uploaded **End-Autumn 2023–24** paper and **Mid-Autumn 2026–27** paper. A tick means the topic has been studied and can be answered without notes. ★ marks a repeat across these two papers.

## Checklist → notes map

Every checklist item below points to the corresponding numbered section in [`pyq-full-notes.md`](pyq-full-notes.md). Short-answer definitions are in [`two-mark-definition-bank.md`](two-mark-definition-bank.md). The definition number is shown where one exists.

| Checklist topic | Full notes section(s) | 2-mark definition |
|---|---:|---:|
| Dissymmetry of lift | §1 | #1 |
| Gyroscopic effect / precession | §2 | #9 |
| Collective and cyclic pitch | §3, §9 | #7–8 |
| Cyclic pitch / flap harmonics and coefficients | §3, §8–9 | #8, #10 |
| Coning; excessive coning; coning numerical | §13 | #11 |
| Rotor-disc tilt | §17 | #13 |
| Lead–lag hinge | §16 | #12 |
| Ground resonance | §6 | #6 |
| Autorotation | §5 | #5 |
| Blade-element derivation of forward-flight \(C_T\) | §7 | #17–18 |
| Velocity components by azimuth | §4 | #2–3 |
| Reverse-flow circle, radius, centre, area | §4 | #3 |
| Forward-flight \(C_T\) numerical | §8 | #18 |
| Find lift-curve slope from rotor data | §9 | #20–21 |
| Forward-flight cyclic coefficients | §9 | #8 |
| Parasite drag factor \(f/A\) | §10 | #23 |
| Flapping moment equation / \(\tau=I\alpha\) | §14 | #10 |
| Hinge-offset frequency and damping | §15 | #14–15 |
| Climb rate | §11 | #24 |
| Descent induced power | §12 | #22 |
| Hover induced velocity and power | §8, §11–12 | #22 |

**Coverage note:** the full notes contain worked values where the PYQ data and convention determine an answer (coning, forward-flight \(C_T\), climb estimate, descent estimate, and \(f/A\) estimate). For the 2026–27 lift-curve-slope question, the scan does not define the twist sign/distribution clearly, so the notes give the full setup and identify the missing interpretation rather than inventing a unique answer. The cyclic-coefficient question has a complete calculation workflow and class sign convention; use the course's intended inputs/convention for the final substitution.

## A. Flapping, rotor response, and controls

- [ ] ★ **Dissymmetry of lift in forward flight**: advancing vs retreating blade; why unequal lift creates a rolling moment; how flapping/ cyclic control removes or balances it. (2023–24 Q1a; 2026–27 Q1e)
- [ ] **Gyroscopic effect and precession**: why rotor response is displaced in azimuth; effect on rotor response. (2023–24 Q1b)
- [ ] ★ **Collective and cyclic pitch**: what each control changes; centrally hinged blade pitch law as a function of azimuth; identify longitudinal and lateral cyclic. (2023–24 Q1c; 2026–27 Q1c)
- [ ] **Cyclic pitch and flap harmonics**: relate pitch harmonics to flap response; know the class sign convention and 90° response phase. (2023–24 Q5b; connects to Q1c)
- [ ] **Coning in hover**: why it occurs; effects/risks of excessive coning. (2023–24 Q1d)
- [ ] **Centrally hinged rotor-disc tilt in forward flight**: explain backward and lateral tilt with sketches and blade response. (2023–24 Q1e)
- [ ] **Lead–lag hinge**: why it is required; in-plane blade motion and relief of loads. (2023–24 Q1f)
- [ ] **Ground resonance**: mechanism (coupling of rotor lead–lag motion and airframe motion) and ways to prevent/overcome it. (2026–27 Q1d)
- [ ] **Autorotation**: energy/momentum explanation and blade regions in autorotation. (2026–27 Q1b)

## B. Blade-element theory and forward flight

- [ ] ★ **Derive the rotor thrust coefficient in forward flight using blade-element theory**, with assumptions stated. This is a 10–15 mark question in both papers. (2023–24 Q2; 2026–27 Q2)
- [ ] **Forward-flight velocity components vs azimuth**: at \(\psi=0^\circ,90^\circ,180^\circ,270^\circ\), distinguish rotational and forward velocity; sketch advancing, retreating, and reverse-flow regions. (2026–27 Q1a)
- [ ] **Reverse-flow region geometry**: derive why its boundary is circular and find its radius and centre; state its area fraction. (2023–24 Q1g; 2026–27 Q1a)
- [ ] **Forward-flight thrust coefficient numerical**: use advance ratio, inflow, disk angle/angle of attack, solidity, blade chord and lift-curve slope correctly. (2023–24 Q5a)
- [ ] **Find blade lift-curve slope from a forward-flight rotor numerical**, using thrust coefficient and given twist/angle of attack/inflow. (2026–27 Q4)
- [ ] **Cyclic coefficients in forward flight**: determine lateral and longitudinal cyclic coefficients from the specified rotor/flapping data. (2023–24 Q5b)
- [ ] **Parasite drag factor \(f/A\) from power required in forward flight**: separate profile, induced, and parasite power; solve the power balance. (2023–24 Q4)

## C. Flapping derivations and numericals

- [ ] **Centrally hinged flapping equation**: start from moment balance; identify \(I_\beta=\int y^2dm\); explain the \(I_\beta\ddot\beta\) inertial torque and centrifugal restoring torque.
- [ ] **Hinge-offset effect on flap natural frequency**: derive the frequency relation and show mathematically that increasing offset raises the frequency. (2023–24 Q3a)
- [ ] **Coning / centrifugal force numerical in hover**: include distributed blade mass and a concentrated tip mass; calculate centrifugal force and flapping/coning angle. (2023–24 Q3b)
- [ ] **Flapping coefficients and cyclic response**: know what mean, cosine, and sine flap coefficients represent; derive/use the relations relevant to the taught model.

## D. Momentum theory, power, climb, and descent

- [ ] **Vertical climb performance**: use hover power capability, weight change, rotor/drag data and the climb power balance to calculate rate of climb. (2026–27 Q3)
- [ ] **Steady vertical descent induced power**: use momentum theory when descent speed is specified relative to induced velocity; identify the correct descent-flow relation. (2026–27 Q5)
- [ ] **Hover induced velocity and power**: \(v_h\), induced power, and their dependence on thrust and disk area. Needed for climb/descent questions.

## E. Fast priority order

1. [ ] Dissymmetry of lift, flap response, cyclic pitch, and rotor-disc tilt.
2. [ ] Forward-flight blade-element derivation of \(C_T\), including assumptions and the azimuth velocity sketch.
3. [ ] Flapping moment balance, coning, and hinge-offset natural-frequency derivation.
4. [ ] The numerical methods: forward-flight \(C_T\)/cyclic, power and \(f/A\), coning with tip mass, climb rate, descent induced power.
5. [ ] Short conceptual answers: autorotation, ground resonance, lead–lag hinge, gyroscopic precession, excessive coning.

## Scope note for the upcoming exam

The instructor's more recent guidance for **your upcoming exam** was: exactly one forward-flight question, numerical only; the remaining questions focus on flapping, including derivations and numericals. The older papers show that forward-flight \(C_T\) derivation has appeared repeatedly, but that historical pattern should **not** override the instructor's explicit current scope. Use it as background unless the instructor updates the guidance.
