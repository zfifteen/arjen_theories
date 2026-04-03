# Summary of the Fixed Special-Case Threshold Sweep

This note summarizes the canonical threshold sweep in [`results/special_case_threshold.csv`](/Users/velocityworks/IdeaProjects/research/arjen_theories/results/special_case_threshold.csv), produced by [`scripts/special_case_experiment.py`](/Users/velocityworks/IdeaProjects/research/arjen_theories/scripts/special_case_experiment.py) for the constrained geometry defined in [`dijksman_rvm_revised.md`](/Users/velocityworks/IdeaProjects/research/arjen_theories/dijksman_rvm_revised.md).

The strongest supported result is narrow and explicit: the fixed seven-point sweep reproduces the three-regime threshold structure claimed in the source note for the special case. With `L = 2` and `c = 1`, the threshold is

```text
omega_0 = pi c / L = pi / 2
```

and the sampled ratios

```text
omega / omega_0 in {0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5}
```

separate cleanly into below-threshold, threshold, and above-threshold behavior.

## Regime Evidence

| Sweep region | `omega / omega_0` values | `delta_t` | `ell_rem` | First re-encounter location | Reported regime |
| --- | --- | --- | --- | --- | --- |
| Below threshold | `0.5`, `0.75`, `0.95` | negative | negative | `off_segment` | `instantaneous_contact` |
| Threshold | `1.0` | zero | zero | `tip` | `critical_recollision` |
| Above threshold | `1.05`, `1.25`, `1.5` | positive | positive | `interior` | `non_instantaneous_gliding_contact` |

The numerical transition is exact in the CSV:

- For `omega / omega_0 < 1`, the first possible re-encounter lies beyond the available half-length of `AB`, so no interior re-encounter is recorded and no gliding contact is reported.
- At `omega / omega_0 = 1`, the first re-encounter lands exactly at the extremity, matching the critical tip case.
- For `omega / omega_0 > 1`, the first re-encounter moves into the interior of `AB`, and the run reports non-instantaneous gliding contact.

The near-threshold row at `omega / omega_0 = 1.05` is the cleanest boundary check. It already gives

```text
delta_t = 0.0476190476190477
ell_rem = 0.0476190476190477
first_reencounter_location = interior
gliding_contact_occurs = yes
```

so the sign change occurs immediately above `omega_0`, not only far into the above-threshold regime.

## What This Sweep Establishes

Within the four-constraint special case, the sweep supports the following statements:

- the threshold `omega_0 = pi c / L` cleanly separates the three named regimes in the source note
- negative `delta_t` and `ell_rem` correspond to off-segment re-encounter and no gliding contact
- zero `delta_t` and `ell_rem` correspond to the tip-touching critical case
- positive `delta_t` and `ell_rem` correspond to interior re-encounter and the onset of non-instantaneous gliding contact

This is evidence for the existence result claimed in the source note. It is not yet a duration law.

## What This Sweep Does Not Establish

This artifact does not determine `tau_contact`. Every row in the CSV records

```text
tau_contact_supported = no
tau_contact = ""
tau_contact_status = undetermined_from_source_note
```

because the current source set does not specify the post-recollision contact condition needed to derive a unique gliding-contact duration. The present result therefore supports the threshold crossing and regime classification only. It does not yet support a numeric claim about how long above-threshold gliding contact lasts or how that duration scales with `omega`.
