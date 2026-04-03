# Methods for One-At-A-Time Perturbation Tests

This document fixes the contract for Workstream E in the research plan.

It does one narrow job:

- define the reference configuration from which each perturbation departs
- define the four allowed one-at-a-time perturbation families from `dijksman_rvm_revised.md`
- define the common observables that future perturbation result files may report without widening the claim surface
- state exactly which special-case diagnostics do not carry over automatically to nonzero perturbations

It does not introduce a general collision law, a new threshold derivation, an ensemble model, or a bulk inertia claim.

## 1. Reference Configuration

Every perturbation test is anchored to the same special-case geometry used in the existing derivation and instrument:

- `omega_CD = 0`
- the rotation plane of `AB` is perpendicular to `CD`
- the initial contact point is the geometric center of each segment
- the translational approach of `CD` is perpendicular to `AB` at contact

The special-case threshold remains the reference angular-speed scale:

```text
omega_0 = pi c / L
```

For Workstream E, `omega_0` is a reference anchor, not a claim that the perturbed geometry obeys the same threshold law.

The canonical angular-speed sweep is the same fixed seven-point sweep already used for the special-case evidence:

```text
omega / omega_0 in {0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5}
```

Each perturbation family should use this ordered sweep so that the special-case control and the perturbed rows are directly comparable.

## 2. One-At-A-Time Rule

Each Workstream E artifact may vary exactly one departure from the special case.

The four allowed perturbation families are:

1. nonzero rotation of `CD`
2. tilt of the collision plane away from perpendicular
3. off-center initial contact
4. oblique translational approach

For a valid one-at-a-time test:

- one family parameter is set to a nonzero value
- the other three family parameters remain fixed at their special-case values
- `L`, `c`, and the ordered `omega` sweep are declared explicitly

No Workstream E artifact may combine two or more departures in the same run.

## 3. Perturbation Parameters

The perturbation families are represented by the following minimal parameters.

### 3.1 `CD` Rotation Family

- Parameter: `omega_CD`
- Special-case value: `0`
- Allowed direction of variation: from `0` toward `omega`

This family answers the question: does gliding contact persist when the second segment is no longer stationary in rotation?

### 3.2 Plane-Tilt Family

- Parameter: `plane_tilt`
- Meaning: angular deviation from the special-case perpendicular orientation
- Special-case value: `0`
- Allowed direction of variation: from `0` toward parallel alignment

This family answers the question: does gliding contact persist when the rotation plane is no longer exactly perpendicular to `CD`?

### 3.3 Contact-Point Family

- Parameter: `contact_offset`
- Meaning: signed initial displacement of the shared contact point away from the geometric center
- Special-case value: `0`
- Allowed direction of variation: from `0` toward an extremity

This family answers the question: does gliding contact persist when the collision is no longer center-on-center?

### 3.4 Approach-Angle Family

- Parameter: `approach_angle`
- Meaning: angular deviation of the translational approach direction away from perpendicularity with respect to `AB` at contact
- Special-case value: `0`
- Allowed direction of variation: from `0` toward oblique approach

This family answers the question: does gliding contact persist when the relative translational motion is no longer perpendicular to `AB`?

## 4. Required Control and Sweep Structure

Each perturbation family result file must include:

- a zero-perturbation control row set that reproduces the special-case configuration for the same `omega` sweep
- one or more nonzero values of the family parameter
- the same ordered `omega / omega_0` reference ratios for the control and perturbed rows

The zero-perturbation control is required because Workstream E is a comparison against the established special-case behavior, not a fresh unrestricted search.

The source note names the perturbation axes but does not fix a canonical nonzero magnitude ladder for them. For that reason, each family-specific result artifact must declare its deterministic nonzero value list explicitly before execution. The value list may be different across families, but it must remain fixed within a given artifact.

## 5. Supported Common Observables

Until a perturbed-geometry contact law is derived, the common cross-family observables are limited to quantities that can be stated without reusing unsupported special-case formulas.

Each perturbation result row should therefore report:

- `omega`
- `omega_reference_ratio`, defined as `omega / (pi c / L)`
- `length`
- `separation_speed`
- the active family parameter column
- `gliding_contact_occurs`
- `tau_contact_supported`
- `tau_contact`
- `tau_contact_status`

The field meanings remain:

- `gliding_contact_occurs = yes` only when the instrument supports a deterministic claim of non-instantaneous contact for that row
- `tau_contact_supported = yes` only when the instrument derives a numeric contact duration from an explicit perturbed-geometry contact law
- `tau_contact` is left blank when that law is absent
- `tau_contact_status` explains the blank deterministically

## 6. Special-Case Quantities That Do Not Transfer Automatically

The following special-case diagnostics are derived in `special_case_derivation.md` under the four simultaneous special constraints:

- `delta_t`
- `s_re`
- `ell_rem`
- the threshold law `omega_0 = pi c / L` as a perturbation-specific regime separator
- the three-label regime classification `instantaneous_contact`, `critical_recollision`, and `non_instantaneous_gliding_contact`

These quantities must not be copied into nonzero perturbation rows as if they still held unchanged.

They may appear only if a family-specific derivation shows that the same formula remains valid for that family. Absent that derivation, the perturbation result artifacts should use only the common observables listed in Section 5.

## 7. Family-Level Outcome Labels

`generalization_assessment.md` should classify each tested perturbation value using the following bounded labels.

- `persists`: at least one nonzero perturbation value still yields `gliding_contact_occurs = yes` on the fixed reference sweep
- `weakens`: gliding contact still occurs, but only on a stricter subset of the above-threshold reference sweep than in the zero-perturbation control
- `disappears`: no tested row at that perturbation value yields `gliding_contact_occurs = yes`
- `ambiguous`: the instrument cannot make a deterministic yes-or-no gliding decision for one or more required rows

These labels are about persistence of the phenomenon, not yet about a validated duration law.

## 8. `tau_contact` Boundary

The ground-truth note states a stronger target for generalization:

- gliding contact should persist
- `tau_contact` should remain a monotonically increasing function of `omega`

The current artifact set does not yet supply the perturbed-geometry contact law needed to derive numeric `tau_contact` for any nonzero perturbation family.

Until that law is written for a given family, Workstream E can support only:

- presence or absence of gliding contact
- explicit reporting of whether `tau_contact` is supported
- bounded persistence labels as defined in Section 7

It cannot yet support a full monotonic-duration claim across perturbations.

## 9. Planned Canonical Artifact Set

This methods contract supports the following planned Milestone 5 artifacts:

- `results/perturbation_cd_rotation.csv`
- `results/perturbation_plane_tilt.csv`
- `results/perturbation_contact_offset.csv`
- `results/perturbation_approach_angle.csv`
- `figures/perturbation_cd_rotation.png`
- `figures/perturbation_plane_tilt.png`
- `figures/perturbation_contact_offset.png`
- `figures/perturbation_approach_angle.png`
- `generalization_assessment.md`

Those artifacts must remain inside the scope fixed here and in `dijksman_rvm_revised.md`.
