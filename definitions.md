# Definitions and Operational Terms

This document fixes the core objects, symbols, and operational terms for work derived from `dijksman_rvm_revised.md`.

Its purpose is to keep later derivations, experiments, and figures consistent.

## 1. Core Objects

### 1.1 Segment Particle

A particle is modeled as a straight line segment of constant length `L` rotating about its midpoint.

### 1.2 Segment Labels

- `AB`: the rotating segment whose angular speed is varied in the special-case analysis
- `CD`: the second segment involved in the collision

These labels are role labels for the special-case setup. They are not a claim about distinct particle species.

## 2. Primary Quantities

### 2.1 Segment Length

- Symbol: `L`
- Meaning: the constant length of a segment particle

### 2.2 Angular Speed

- Symbol: `omega`
- Meaning: the angular speed of segment `AB` in the special-case setup

### 2.3 Angular Speed of the Second Segment

- Symbol: `omega_CD`
- Meaning: the angular speed of segment `CD`
- In the special-case setup, `omega_CD = 0`

### 2.4 Separation Speed

- Symbol: `c`
- Meaning: the fixed speed at which the massless particles separate after contact in the note's model

### 2.5 Tip Speed

- Symbol: `v_tip`
- Definition:

```text
v_tip = omega L / 2
```

- Meaning: the linear speed of an extremity of segment `AB`

## 3. Special-Case Geometric Constraints

The ground-truth note defines the analyzed collision using four simultaneous constraints.

### 3.1 Constraint 1: No Rotation of `CD`

```text
omega_CD = 0
```

### 3.2 Constraint 2: Perpendicular Rotation Plane

Segment `AB` rotates in a plane exactly perpendicular to segment `CD`.

### 3.3 Constraint 3: Center Contact

The initial contact point is the geometric center of each segment.

### 3.4 Constraint 4: Perpendicular Translational Approach

The translational velocity `V` of `CD` relative to `AB` is perpendicular to `AB` at the moment of contact.

## 4. Regime Threshold

The ground-truth note defines the regime threshold as:

```text
omega_0 = pi c / L
```

This threshold separates the three named collision regimes in the special-case geometry.

## 5. Collision Regimes

### 5.1 Regime 1: Instantaneous Contact

Condition:

```text
omega < omega_0
```

Operational meaning:

- the segments touch momentarily
- they separate without sustained sliding contact

### 5.2 Regime 2: Critical Recollision

Condition:

```text
omega = omega_0
```

Operational meaning:

- after the initial separation, an extremity of `AB` reaches the trajectory of `CD`
- a second brief collision occurs
- the note does not treat this as sustained gliding contact

### 5.3 Regime 3: Non-Instantaneous Gliding Contact

Condition:

```text
omega > omega_0
```

Operational meaning:

- contact persists for a nonzero duration
- segment `AB` pushes `CD`
- the contact point moves along `AB` toward one extremity
- separation occurs when the extremity is reached

## 6. Operational Terms for Experiments

These definitions should be used in computational and analytic supporting work unless later derivation requires refinement.

### 6.1 Contact Event

A contact event is an interval during which the two segments are in mechanical contact under the model assumptions.

### 6.2 Instantaneous Contact

An interaction with zero sustained contact duration at the resolution of the model.

### 6.3 Gliding Contact

A nonzero-duration contact event in which the contact point advances along the length of `AB` rather than remaining fixed at the initial center point.

### 6.4 Contact Duration

- Symbol: `tau_contact`
- Meaning: the duration of sustained gliding contact in a single collision event

This quantity is central to the research program because the ground-truth note treats it as the immediate geometric source of resistance-like behavior.

### 6.5 Inertia-Like Behavior

Within this project, "inertia-like behavior" means sustained resistance to the translational motion of `CD` produced by non-instantaneous gliding contact in the constrained geometry.

This phrase does not mean:

- proven inertial mass
- a Lorentz-invariant mass term
- a demonstrated bulk property of matter

## 7. Generalization-Test Parameters

The ground-truth note identifies four perturbation axes to test whether the special-case effect generalizes.

### 7.1 Rotation Perturbation

Vary `omega_CD` away from zero.

### 7.2 Plane-Tilt Perturbation

Tilt the rotation plane of `AB` away from exact perpendicularity with respect to `CD`.

### 7.3 Contact-Point Perturbation

Shift the initial contact point away from the geometric centers.

### 7.4 Approach-Angle Perturbation

Vary the relative translational approach direction away from perpendicularity.

## 8. Ensemble-Level Terms

These terms belong to later work only. They should not be treated as already established.

### 8.1 Background Population

A statistical distribution of slowly rotating segments encountered by a rapidly rotating segment.

### 8.2 Cumulative Resistance

A possible aggregate effect produced by repeated collisions in an ensemble model.

This is a research target, not a completed result.

## 9. Interpretation Boundaries

The following distinctions must be preserved in all future documents:

- special-case result versus generalized result
- single-collision behavior versus ensemble behavior
- geometric resistance proxy versus mass
- qualitative analogy versus quantitative derivation

## 10. Default Notational Policy

Until a stricter derivation document is written:

- use `L`, `omega`, `omega_CD`, `c`, `V`, `v_tip`, `omega_0`, and `tau_contact`
- avoid introducing extra notation unless it is necessary for a derivation or experiment
- define every new symbol in the document where it first appears
