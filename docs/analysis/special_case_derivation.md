# Special-Case Derivation for the Constrained Two-Particle Collision

This document reconstructs the special-case geometry in `dijksman_rvm_revised.md` in explicit coordinates.

It does one narrow job:

- define a coordinate model consistent with the four stated constraints
- derive the threshold `omega_0 = pi c / L`
- recover the three regimes from one timing comparison
- identify the exact missing step that blocks a unique closed-form law for `tau_contact`

It does not add a stronger claim than the ground-truth note. In particular, it does not derive a mass law, an ensemble law, or a closed-form gliding-contact duration.

## 1. Coordinate Model

Choose coordinates so that the initial center contact occurs at the origin at time `t = 0`.

Use the following conventions.

- Segment `AB` has fixed length `L`, midpoint at the origin, and rotates in the `xy` plane with angular speed `omega`.
- Segment `CD` has zero angular speed in the special case: `omega_CD = 0`.
- Segment `CD` is aligned with the `z` axis, so the rotation plane of `AB` is exactly perpendicular to `CD`.
- The relative translational motion of `CD` is along the positive `y` direction with fixed speed `c`.
- The initial contact point is the midpoint of each segment.

These choices are coordinate conventions, not extra physics. They simply realize the four constraints from `dijksman_rvm_revised.md` in one explicit frame.

## 2. Kinematic Ingredients

At time `t`, write the orientation angle of `AB` as

```text
theta(t) = omega t
```

with `AB` chosen to lie along the `x` axis at `t = 0`.

A material point on `AB` at signed distance `s` from the midpoint has position

```text
r_AB(s, t) = (s cos(theta(t)), s sin(theta(t)), 0)
           = (s cos(omega t), s sin(omega t), 0)
```

with `-L/2 <= s <= L/2`.

The midpoint of `CD` translates as

```text
r_CD(t) = (0, c t, 0)
```

when projected into the rotation plane of `AB`.

The B-extremity of `AB` corresponds to `s = L/2`, so its projected trajectory is

```text
r_B(t) = (L/2 cos(omega t), L/2 sin(omega t), 0)
```

The tip speed is therefore

```text
v_tip = omega L / 2
```

which matches the ground-truth note.

## 3. First Re-Encounter Condition

After the initial center contact at `t = 0`, the next kinematic question is whether some point of `AB` can meet the translated trajectory of `CD`.

That requires

```text
r_AB(s, t) = r_CD(t)
```

which gives the two scalar conditions

```text
s cos(omega t) = 0
s sin(omega t) = c t
```

For `t > 0`, a nontrivial re-encounter must have `s != 0`. The first equation then forces

```text
cos(omega t) = 0
```

The first positive solution is

```text
t_rot = pi / (2 omega)
```

At that instant, `AB` is vertical in the `xy` projection, and the second condition gives the corresponding contact coordinate along `AB`:

```text
s_re = c t_rot = pi c / (2 omega)
```

This is the first point on `AB` that can re-enter the translated path of `CD`.

## 4. Threshold Derivation

The segment ends at `s = L/2`. A re-encounter is possible only if the first available contact coordinate lies on the segment:

```text
s_re <= L / 2
```

Substitute the expression for `s_re`:

```text
pi c / (2 omega) <= L / 2
```

Multiply by `2` and rearrange:

```text
omega >= pi c / L
```

Define the threshold

```text
omega_0 = pi c / L
```

This is exactly the threshold stated in `dijksman_rvm_revised.md`.

The same result can be written as a comparison of two times:

- rotation-to-trajectory time

```text
t_rot = pi / (2 omega)
```

- tip-clearance time

```text
t_clear = (L/2) / c = L / (2 c)
```

The threshold is the equality

```text
t_rot = t_clear
```

which again yields

```text
omega_0 = pi c / L
```

For later use, define the timing margin

```text
Delta t = t_clear - t_rot = L / (2 c) - pi / (2 omega)
```

and the remaining half-length after first re-encounter

```text
ell_rem = L/2 - s_re = L/2 - pi c / (2 omega)
```

Both quantities are positive only above threshold. They are useful kinematic diagnostics, but neither should be identified with `tau_contact` without an additional contact law.

## 5. Recovery of the Three Regimes

The three regimes in the ground-truth note follow directly from the sign of `Delta t`.

### 5.1 Regime 1: Instantaneous Contact

If

```text
omega < omega_0
```

then

```text
t_rot > t_clear
```

or equivalently

```text
s_re > L / 2
```

The first possible re-encounter would occur beyond the available segment length. In this reduced kinematic reconstruction, no interior re-encounter occurs after the initial center contact. This is the regime labeled "instantaneous contact" in the note.

### 5.2 Regime 2: Critical Recollision

If

```text
omega = omega_0
```

then

```text
t_rot = t_clear
s_re = L / 2
```

The first re-encounter occurs exactly at the B-extremity. This reproduces the note's critical case: the extremity reaches the translated trajectory of `CD`, producing a second brief collision but no interior gliding interval.

### 5.3 Regime 3: Interior Re-Encounter and Gliding Onset Condition

If

```text
omega > omega_0
```

then

```text
t_rot < t_clear
s_re < L / 2
```

The first re-encounter occurs at an interior point of `AB`, leaving positive remaining half-length `ell_rem`.

This is the kinematic condition required for the note's "non-instantaneous gliding contact" regime. It shows that the rotating segment catches the translated trajectory of `CD` before the extremity is reached.

## 6. What This Derivation Establishes

Within the coordinate realization above, the note's threshold and regime ordering are supported by one explicit timing comparison:

```text
t_rot = pi / (2 omega)
versus
t_clear = L / (2 c)
```

That comparison is sufficient to establish the following bounded result:

- below threshold, no interior re-encounter occurs
- at threshold, the first re-encounter occurs at the extremity
- above threshold, the first re-encounter occurs at an interior point

That is enough to support the note's existence claim for a regime transition in the constrained geometry.

## 7. Exact Unresolved Step for `tau_contact`

The ground-truth note goes further than first re-encounter: it states that above threshold the contact point glides along `AB` toward an extremity and that the resulting contact duration grows with `omega`.

The present derivation does not dispute that claim. It isolates the exact missing equation needed to derive it in closed form.

After the first interior re-encounter at

```text
t = t_rot
```

the note does not specify the post-recollision contact constraint that governs the subsequent joint motion of `AB` and `CD`.

To derive a unique formula for `tau_contact`, one would need an explicit rule answering this question:

```text
Once interior contact is re-established, what kinematic condition keeps the same moving contact point on both segments until separation?
```

Equivalent formulations are:

- What equation determines the trajectory of the contact point during the pushing phase?
- Is `CD` constrained to keep translating at speed `c` while being redirected, or is `c` only the separation speed once contact ends?
- Which relative velocity component is required to vanish while gliding contact is maintained?

Without that closure, `tau_contact(omega, L, c)` is not uniquely determined by the source note alone.

## 8. Safe Output of This Document

This document supports the following narrow statements and no stronger ones.

- The threshold `omega_0 = pi c / L` is derivable from the constrained geometry.
- The three regimes can be recovered from the sign of `Delta t = L/(2c) - pi/(2omega)`.
- The above-threshold regime is characterized kinematically by first interior re-encounter before tip clearance.
- A closed-form law for `tau_contact` still requires one explicit post-recollision contact law that the source note does not provide.

That is the correct stopping point for the analytic reconstruction based on the present ground-truth document.
