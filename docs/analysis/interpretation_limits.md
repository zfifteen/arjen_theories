# Interpretation Limits

This document states the strongest conclusion supported by the current repository and the exact limits that conclusion carries.

## 1. Strongest Supported Result

Within the four-constraint special case defined in `dijksman_rvm_revised.md`, the threshold

```text
omega_0 = pi c / L
```

separates three regimes:

- below threshold: no interior re-encounter
- at threshold: extremity recollision
- above threshold: interior re-encounter consistent with the onset of non-instantaneous gliding contact

This is the repository's main result. It is supported analytically in `special_case_derivation.md`, computationally in `scripts/special_case_experiment.py`, and empirically in the fixed Milestone 4 result files and figures.

## 2. What Is Not Established

The repository does not establish any of the following:

- a closed-form law for `tau_contact`
- a numeric scaling law for gliding-contact duration versus `omega`
- persistence of the mechanism under nonzero `omega_CD`
- persistence of the mechanism under nonzero plane tilt
- persistence of the mechanism under nonzero contact offset
- persistence of the mechanism under nonzero approach angle
- a bulk ensemble resistance law
- a quantitative identification of `omega` with mass
- a derivation of mass-energy equivalence

These are not minor caveats. They define the boundary of the result.

## 3. Why Generalization Stops Here

The Workstream E artifacts do not show disappearance of the mechanism under perturbation. They show something more limited: every tested nonzero perturbation row is currently `ambiguous`.

That ambiguity is not being used as rhetoric. It has one explicit cause recorded throughout the repository:

- the current source set does not provide the family-specific post-recollision contact law needed to determine whether gliding contact persists and, if so, what `tau_contact` would be

The correct interpretation is therefore not "generalization succeeded" and not "generalization failed." The correct interpretation is "generalization remains unresolved outside the special case."

## 4. Consequence for Ensemble Claims

The research plan allowed Workstream F only if Milestone 5 showed that the special-case effect was not geometrically fragile.

The current repository does not clear that gate. It does not yet provide even one nonzero perturbation family with a deterministic persistence result. For that reason:

- no ensemble artifact in this repository should be treated as evidence-bearing
- no bulk resistance or mass-like conclusion should be stated as if it had been derived
- the project should stop at the constrained special-case result unless new source support is added

## 5. Language Boundary for the Final Note

The final technical note may safely say:

- "constrained two-particle collision"
- "special-case geometry"
- "threshold `omega_0 = pi c / L`"
- "non-instantaneous gliding onset condition in the constrained geometry"
- "structurally analogous to inertial resistance within the constrained geometry"
- "generalization remains unresolved"

The final technical note should not say:

- "general mechanism of inertia"
- "mass derived from rotation"
- "`omega` shown to equal mass"
- "ensemble resistance established"
- "proof of mass-energy equivalence"

## 6. Reopening Condition

If this project is reopened, the next evidence-bearing step is not another interpretation pass. It is a new derivation.

At minimum, future work would need to add an explicit family-specific post-recollision contact law for at least one nonzero perturbation family. Without that, any stronger generalization or ensemble claim would exceed the present source support.
