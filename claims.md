# Claims Ledger for `dijksman_rvm_revised.md`

This document extracts the claim surface of `dijksman_rvm_revised.md` and classifies each statement by status.

It is a control document. Its purpose is to prevent scope drift in later derivations, experiments, figures, and summaries.

## 1. Established Claims in the Ground-Truth Note

These are claims the ground-truth note positively makes within its stated scope.

### 1.1 Particle Definition

- Within the Rotating Vector Model, a fundamental particle is modeled as a straight line segment of constant length `L` rotating about its center.
- At the level of particle definition in the note, the segment is treated as massless.

### 1.2 Existence of a Constrained Collision Analysis

- The note analyzes a two-particle collision under four simultaneous geometric constraints.
- Those four constraints define a measure-zero subset of all possible collision geometries.
- The analysis is claimed to be valid only within that constrained scenario.

### 1.3 Regime Structure in the Constrained Geometry

- The constrained collision admits three regimes distinguished by the angular speed `omega` of segment `AB`.
- For `omega < pi c / L`, the contact is instantaneous.
- For `omega = pi c / L`, a critical recollision occurs.
- For `omega > pi c / L`, non-instantaneous gliding contact occurs in which `AB` pushes `CD` while the contact point moves along `AB` toward an extremity.

### 1.4 Existence of Inertia-Like Behavior in the Constrained Geometry

- In the above-threshold constrained regime, longer gliding contact is associated with greater resistance to the translational motion of `CD`.
- Within the constrained geometry only, that sustained resistance is structurally analogous to inertia.
- The primary contribution of the note is an existence claim for that constrained mechanism.

### 1.5 Open Need for Generalization Testing

- The note explicitly states that whether the mechanism persists beyond the constrained geometry is an open question.
- The note identifies four one-at-a-time perturbation families that must be tested to evaluate generalization:
  - nonzero rotation of `CD`
  - non-perpendicular collision plane
  - off-center contact
  - oblique approach velocity

### 1.6 Open Need for an Ensemble Model

- A single two-particle collision is not sufficient to establish a bulk inertial property.
- A many-collision or statistical ensemble treatment is required before any quantitative connection to mass can be proposed.

## 2. Conjectures or Research Hypotheses in the Ground-Truth Note

These are not established by the note. They are presented as hypotheses, interpretations, or open research directions.

### 2.1 Generalization Hypothesis

- Non-instantaneous gliding contact may persist across a broad range of collision geometries beyond the constrained special case.
- If gliding-contact duration remains a monotonic function of `omega` across the specified perturbations, the special case may be representative rather than exceptional.

### 2.2 Bulk Resistance Interpretation

- A rapidly rotating segment moving through a population of slowly rotating segments may experience cumulative resistance due to repeated non-instantaneous collisions.
- That cumulative resistance may support an inertia-like interpretation at the ensemble level.

### 2.3 Possible Mass-Energy Connection

- If the mechanism generalizes and if a quantitative scaling law can be derived, the model may eventually be tested for consistency with a mass-energy relation.

## 3. Explicit Non-Claims

These are statements the ground-truth note explicitly does not claim.

- It does not claim a complete theory of mass.
- It does not claim a derivation of mass-energy equivalence.
- It does not claim that the constrained special-case result automatically generalizes to arbitrary collision geometries.
- It does not claim a quantitative scaling law equating angular speed with mass.
- It does not claim that `omega` is already shown to be proportional to mass.
- It does not claim that the present analysis alone establishes a bulk inertial property.

## 4. Allowed Language for Supporting Documents

The following language is aligned with the ground-truth note:

- "constrained two-particle collision"
- "special-case geometry"
- "non-instantaneous gliding contact"
- "structurally analogous to inertial resistance"
- "existence result within the constrained geometry"
- "generalization hypothesis"
- "ensemble model required"

## 5. Disallowed or Premature Language

The following formulations should not appear in supporting documents unless later work actually establishes them.

- "mass is derived"
- "the model explains inertia in general"
- "`omega` equals mass"
- "effective inertia index" as if already derived from first principles
- "proof of `E = mc^2`"
- "complete mechanical theory of inertia"
- "general result" when referring only to the constrained geometry

## 6. Practical Use

Every future artifact in this repository should answer these questions before it is treated as valid support material:

1. Which claim in this document does it support, test, or bound?
2. Does it introduce a stronger claim than the ground-truth note allows?
3. Does it clearly distinguish established results from conjectures and open problems?

If the answer to question 2 is yes, that artifact should be revised before it is treated as part of the technical-note pipeline.
