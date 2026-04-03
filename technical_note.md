# Technical Note on a Constrained Collision Mechanism for Inertia-Like Resistance in the Rotating Vector Model

## Abstract

This note records the strongest conclusion supported by the current repository derived from `dijksman_rvm_revised.md`. In the four-constraint special case, the threshold

```text
omega_0 = pi c / L
```

cleanly separates three regimes: below-threshold instantaneous contact, threshold extremity recollision, and above-threshold interior re-encounter consistent with the onset of non-instantaneous gliding contact. That result is supported by an explicit coordinate derivation, a deterministic special-case instrument, and fixed result files and figures. One-at-a-time perturbation artifacts were then constructed for nonzero `omega_CD`, plane tilt, contact offset, and approach angle. In every family, the zero-perturbation control reproduces the special-case transition, while every tested nonzero perturbation value remains `ambiguous` because the current source set does not provide a family-specific post-recollision contact law. The project therefore closes with a constrained special-case existence result, not a demonstrated general mechanism of inertia and not an ensemble theory of mass.

## 1. Problem and Scope

The source note proposes that inertia-like resistance may arise mechanically from collisions between massless rotating segments. The claim surface fixed in this repository is narrower than a general mass theory.

The question addressed here is:

1. can the constrained special-case geometry be stated explicitly
2. can its threshold structure be reproduced deterministically
3. do the current source-bound perturbation tests support generalization beyond that special case

The note does not attempt to derive mass-energy equivalence, a quantitative mass law, or an ensemble response law. Those remain outside the supported result.

## 2. Constrained Geometry

The special case uses four simultaneous constraints:

1. `omega_CD = 0`
2. segment `AB` rotates in a plane perpendicular to `CD`
3. initial contact occurs at the geometric centers
4. the translational approach of `CD` is perpendicular to `AB` at contact

With segment length `L` and separation speed `c`, the tip speed of `AB` is

```text
v_tip = omega L / 2
```

The coordinate derivation in `special_case_derivation.md` compares:

```text
t_rot = pi / (2 omega)
t_clear = L / (2 c)
```

and recovers the threshold

```text
omega_0 = pi c / L
```

This threshold is the analytic backbone of the project.

## 3. Special-Case Result

The deterministic instrument `scripts/special_case_experiment.py`, documented in `methods/special_case_experiment.md`, computes the threshold and the kinematic diagnostics needed to classify the special-case regimes. The fixed threshold sweep in `results/special_case_threshold.csv` and summarized in `results/special_case_summary.md` uses

```text
omega / omega_0 in {0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5}
```

For `L = 2` and `c = 1`, the result is:

| Sweep region | `omega / omega_0` values | First re-encounter location | Reported regime |
| --- | --- | --- | --- |
| Below threshold | `0.5`, `0.75`, `0.95` | `off_segment` | `instantaneous_contact` |
| Threshold | `1.0` | `tip` | `critical_recollision` |
| Above threshold | `1.05`, `1.25`, `1.5` | `interior` | `non_instantaneous_gliding_contact` |

The near-threshold row at `omega / omega_0 = 1.05` already shows the sign change into positive `delta_t` and positive `ell_rem`, so the transition occurs immediately above the analytic threshold rather than only far into the above-threshold regime.

The above-threshold scaling file `results/special_case_scaling.csv` and its figure show that the available kinematic diagnostics vary smoothly with `omega` once the system is above threshold. Those diagnostics are evidence for the onset structure only. They are not a numeric law for `tau_contact`.

## 4. Boundary on Contact Duration

The source note states that above threshold the contact duration grows with `omega`. The present repository does not derive that duration in closed form.

The missing step is explicit in `special_case_derivation.md` and `methods/special_case_experiment.md`: once interior contact is re-established, the source set does not specify the post-recollision condition that keeps the same moving contact point on both segments until separation.

For that reason:

- `tau_contact_supported = no` in the special-case result files
- `tau_contact` is left blank in the current CSV schema
- no artifact in this repository treats `delta_t` or `ell_rem` as a substitute duration law

This is a deliberate limit, not an omission.

## 5. One-At-A-Time Perturbation Tests

The repository then tests the four perturbation axes named in Section 6 of `dijksman_rvm_revised.md` using the contract fixed in `methods/perturbation_tests.md`:

- nonzero `omega_CD`
- nonzero plane tilt
- nonzero contact offset
- nonzero approach angle

Each family artifact includes the same seven-point zero-perturbation control plus one fixed nonzero ladder for that family. The resulting Milestone 5 assessment is:

| Family | Nonzero ladder | Zero-perturbation control | Family label |
| --- | --- | --- | --- |
| `CD` rotation | `omega_CD / omega in {0.25, 0.5, 0.75, 1.0}` | reproduces `N/N/N/N/Y/Y/Y` | `ambiguous` |
| Plane tilt | `15, 30, 45, 60` degrees | reproduces `N/N/N/N/Y/Y/Y` | `ambiguous` |
| Contact offset | `0.2, 0.4, 0.6, 0.8` | reproduces `N/N/N/N/Y/Y/Y` | `ambiguous` |
| Approach angle | `15, 30, 45, 60` degrees | reproduces `N/N/N/N/Y/Y/Y` | `ambiguous` |

The zero-perturbation control rows show that every family artifact remains anchored to the same special-case transition. The nonzero rows show the current research boundary just as clearly: the repository does not yet contain the family-specific contact laws required to determine whether gliding persists away from the special case.

## 6. Interpretation

The project therefore supports one bounded interpretation.

Within the constrained geometry, there is an existence result for a collision mechanism whose above-threshold behavior is structurally analogous to inertial resistance. That statement is supported.

The following stronger interpretations are not supported:

- that the mechanism generalizes across arbitrary collision geometries
- that `tau_contact` has been derived as a monotone function of `omega`
- that repeated collisions already justify a bulk inertia law
- that `omega` has been quantitatively identified with mass

The perturbation suite does not show persistence and does not show disappearance. It shows that the current source set is not yet strong enough to decide.

## 7. Project Outcome

The research plan required the project to stop if the evidence failed to justify continuation. That stopping rule now matters.

The current repository clears the special-case derivation and special-case evidence gates. It does not clear the gate required for an ensemble interpretation. No evidence-bearing Workstream F artifact should therefore be treated as part of the finished result.

The completed project outcome is:

- a clean claim boundary
- an explicit special-case threshold derivation
- a deterministic special-case instrument
- fixed special-case evidence files and figures
- fixed perturbation family artifacts
- an explicit generalization decision that remains limited to `ambiguous` outside the special case

That is a smaller claim than the original broader intuition suggested, but it is a research-grade result because every surviving statement is tied to an explicit derivation or recorded artifact.

## 8. Conclusion

The repository now supports a disciplined final conclusion.

In one geometrically constrained two-particle collision, massless rotating segments exhibit a threshold

```text
omega_0 = pi c / L
```

that separates instantaneous contact from interior re-encounter consistent with non-instantaneous gliding onset. That is the main result.

Beyond that special case, the current source set does not yet support deterministic statements about persistence under nonzero one-at-a-time perturbations. The project therefore ends with a constrained existence result and an explicit statement of what would have to be derived before any stronger generalization, ensemble, or mass-like conclusion could be defended.

## References

### Primary Source

- `dijksman_rvm_revised.md`

### Claim and Definition Control

- `claims.md`
- `definitions.md`

### Analytic and Methods Artifacts

- `special_case_derivation.md`
- `methods/special_case_experiment.md`
- `methods/perturbation_tests.md`

### Fixed Result Artifacts

- `results/special_case_threshold.csv`
- `results/special_case_scaling.csv`
- `results/special_case_summary.md`
- `results/perturbation_cd_rotation.csv`
- `results/perturbation_plane_tilt.csv`
- `results/perturbation_contact_offset.csv`
- `results/perturbation_approach_angle.csv`

### Fixed Figure Artifacts

- `figures/special_case_threshold.png`
- `figures/special_case_scaling.png`
- `figures/perturbation_cd_rotation.png`
- `figures/perturbation_plane_tilt.png`
- `figures/perturbation_contact_offset.png`
- `figures/perturbation_approach_angle.png`
