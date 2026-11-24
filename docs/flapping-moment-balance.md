# Flapping moment balance: read it as \(\tau=I\alpha\)

The key relation is Newton's second law for rotation:

$$
\tau_{\text{net}} = I\alpha.
$$

For a rotor blade flapping about its hinge:

- \(\beta\) is the blade's flapping angle;
- \(\ddot{\beta}\) is its angular acceleration about the hinge;
- \(y\) is distance along the blade, measured from the flapping hinge;
- \(dm\) is a small piece of blade mass;
- \(I_\beta\) is the blade's flapping moment of inertia about that hinge.

As in any rotation,

$$
I_\beta = \int y^2\,dm.
$$

A small mass element \(dm\) at distance \(y\) contributes \(y^2dm\) to the moment of inertia. Thus the torque needed to angularly accelerate the blade is

$$
\tau_{\text{inertia}} = I_\beta\ddot{\beta}
= \left(\int y^2\,dm\right)\ddot{\beta}.
$$

## The two torques in the blade balance

### Aerodynamic torque

A small lift force \(dL\) acts at distance \(y\) from the hinge. Its moment is lever arm times force, \(y\,dL\). Adding up all the blade elements gives

$$
\tau_{\text{aero}} = \int y\,dL.
$$

### Centrifugal restoring torque

The rotating blade has centrifugal force. When it flaps by a small angle \(\beta\), the geometry gives that force a component which tends to return the blade toward the rotor plane. For a small angle, its restoring moment is

$$
\tau_{\text{restore}} \approx I_\beta\Omega^2\beta,
$$

where \(\Omega\) is the rotor angular speed.

## Put it into \(\tau_{\text{net}}=I\alpha\)

The aerodynamic torque acts in the direction of positive flap; the restoring torque acts against it. Therefore the **signed** net-torque equation is

$$
\tau_{\text{aero}} - \tau_{\text{restore}}
= I_\beta\ddot{\beta}.
$$

Substitute the expressions for the two torques:

$$
\int y\,dL - I_\beta\Omega^2\beta
= I_\beta\ddot{\beta}.
$$

Rearrange to the common class-notes form, where the restoring torque is shown on the right as a positive magnitude:

$$
\boxed{
\int y\,dL
= I_\beta\ddot{\beta} + I_\beta\Omega^2\beta
= \left(\int y^2\,dm\right)\ddot{\beta}
+ \left(\int y^2\,dm\right)\Omega^2\beta
}
$$

Read this as:

> **Aerodynamic lift torque = torque to accelerate the flap + centrifugal restoring torque.**

The second term on the right is not another \(I\alpha\) term. It is a restoring torque, analogous to a spring torque. The first term is exactly the familiar rotational law \(I\alpha\).

## Dimensional check

Both sides must be moments (torques):

$$
\int y\,dL: \quad \mathrm{m}\cdot\mathrm{N} = \mathrm{N\,m},
$$

and

$$
I_\beta\ddot{\beta}: \quad
(\mathrm{kg\,m^2})(\mathrm{s^{-2}})
= \mathrm{kg\,m^2\,s^{-2}}
= \mathrm{N\,m}.
$$

Likewise, \(I_\beta\Omega^2\beta\) has units \(\mathrm{N\,m}\), since radians are dimensionless and \(\Omega\) has units \(\mathrm{s^{-1}}\).

## One-line memory aid

$$
\boxed{\text{net torque about the flap hinge}
= I_\beta\times\text{flap angular acceleration}}
$$

Here, net torque means **aerodynamic torque minus centrifugal restoring torque**. The integral \(\int y^2dm\) is simply the blade's rotational inertia about its flapping hinge.
