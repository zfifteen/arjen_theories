# Generalization Assessment for the One-At-A-Time Perturbation Tests

This document closes Milestone 5 of the research plan.

The strongest supported finding is plain: every perturbation artifact reproduces the special-case control transition at zero perturbation, but every tested nonzero perturbation value remains `ambiguous` under the current source set. The repository therefore does not support the claim that the mechanism has been shown to generalize beyond the four-constraint special case. It also does not support the stronger opposite claim that the mechanism has been shown to fail under perturbation. The correct family-level conclusion is narrower: generalization is unresolved because the required family-specific contact laws are absent.

## 1. Evidence Base

This assessment uses only the fixed Workstream E artifact set:

- `methods/perturbation_tests.md`
- `results/perturbation_cd_rotation.csv`
- `results/perturbation_plane_tilt.csv`
- `results/perturbation_contact_offset.csv`
- `results/perturbation_approach_angle.csv`
- the four matching perturbation figures

Each result file uses the same ordered reference sweep

```text
omega / omega_0 in {0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5}
```

and includes a zero-perturbation control row set plus one declared deterministic nonzero ladder for that family.

Under `methods/perturbation_tests.md`, the allowed family-level labels are:

- `persists`
- `weakens`
- `disappears`
- `ambiguous`

For this milestone, `ambiguous` means the current source set does not provide the family-specific gliding or `tau_contact` law required to classify the nonzero rows deterministically.

## 2. Cross-Family Result

| Family | Nonzero ladder used | Zero-perturbation control | Nonzero row status | Family outcome |
| --- | --- | --- | --- | --- |
| `CD` rotation | `omega_CD / omega in {0.25, 0.5, 0.75, 1.0}` | reproduces `N/N/N/N/Y/Y/Y` across the fixed sweep | all 28 nonzero rows are `ambiguous` | `ambiguous` |
| Plane tilt | `plane_tilt_degrees in {15, 30, 45, 60}` | reproduces `N/N/N/N/Y/Y/Y` across the fixed sweep | all 28 nonzero rows are `ambiguous` | `ambiguous` |
| Contact offset | `contact_offset in {0.2, 0.4, 0.6, 0.8}` | reproduces `N/N/N/N/Y/Y/Y` across the fixed sweep | all 28 nonzero rows are `ambiguous` | `ambiguous` |
| Approach angle | `approach_angle_degrees in {15, 30, 45, 60}` | reproduces `N/N/N/N/Y/Y/Y` across the fixed sweep | all 28 nonzero rows are `ambiguous` | `ambiguous` |

The control rows matter because they show that each family artifact remains anchored to the same special-case threshold transition already established in the derivation, special-case script, and Milestone 4 evidence files.

The nonzero rows matter because they show the present boundary of the project just as clearly: no tested perturbation family currently supports a deterministic `yes` or `no` answer for gliding persistence away from the special case.

## 3. Family Notes

### 3.1 `CD` Rotation

The `omega_CD = 0` control reproduces the special-case threshold transition exactly. Every nonzero `omega_CD / omega` value is marked `ambiguous` because the current source set does not provide a re-encounter/contact law for nonzero rotation of `CD`.

### 3.2 Plane Tilt

The zero-tilt control again reproduces the special-case threshold transition. Every nonzero `plane_tilt` row is `ambiguous` because the current source set does not specify how the post-recollision contact law changes once the collision plane is no longer perpendicular.

### 3.3 Contact Offset

The center-contact control reproduces the special-case transition. Every nonzero `contact_offset` row is `ambiguous` because the current source set does not provide a family-specific law for re-established contact away from center-on-center impact.

### 3.4 Approach Angle

The perpendicular-approach control reproduces the special-case transition. Every nonzero `approach_angle` row is `ambiguous` because the current source set does not provide a family-specific law for oblique translational approach after first re-encounter.

## 4. Milestone 5 Decision

Milestone 5 required the project to decide whether generalization is supported, limited, or false before any ensemble narrative was discussed.

The correct decision from the current artifact set is:

```text
generalization status = limited
family labels = ambiguous for all four tested perturbation families
```

This means:

- the special-case mechanism is reproducible and inspectable in its reference geometry
- the current repository does not support the claim that the mechanism persists under nonzero one-at-a-time perturbations
- the current repository also does not support the stronger claim that the mechanism disappears under those perturbations
- the present research boundary is therefore a constrained special-case existence result plus an explicit record of what is still missing for generalization

## 5. Consequence for the Project

Because every nonzero perturbation family remains `ambiguous`, the project does not have the evidence required to open the ensemble layer as a research-grade continuation. The safe stopping point is the special-case existence result together with an explicit statement that generalization remains unresolved.

That is the correct bounded answer to the question posed in Section 6 of `dijksman_rvm_revised.md`. The repository now contains a clean statement of what survives:

- the constrained threshold mechanism is supported
- the generalization hypothesis is not established
- the ensemble interpretation is not yet justified
