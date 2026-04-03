# Methods for `scripts/special_case_experiment.py`

This document states the contract of the deterministic special-case instrument for the constrained collision in `dijksman_rvm_revised.md`.

It does one narrow job:

- define the exact geometry and inputs used by the script
- state the computed observables and CSV schema
- document the fixed no-argument threshold-spanning validation case
- state exactly why `tau_contact` is not derived by the current instrument

It does not widen the claim surface beyond `dijksman_rvm_revised.md`, `claims.md`, `definitions.md`, and `special_case_derivation.md`.

## 1. Scope

The script implements only the four-constraint special case:

- `omega_CD = 0`
- the rotation plane of `AB` is perpendicular to `CD`
- initial contact is at the geometric centers
- the translational approach of `CD` is perpendicular to `AB` at contact

The script is a deterministic kinematic instrument for the regime threshold. It is not a general collision solver, an ensemble model, or a derivation of mass.

## 2. Inputs and Defaults

The script accepts:

- one or more angular-speed values `omega`
- segment length `L` through `--length`
- separation speed `c` through `--separation-speed`
- an optional CSV path through `--output`

No-argument execution is the canonical representative run. Its defaults are:

```text
omega values = (1, pi/2, 2)
L = 2
c = 1
```

These defaults are deterministic and threshold-spanning because

```text
omega_0 = pi c / L = pi / 2
```

so the three default `omega` values land below threshold, at threshold, and above threshold.

## 3. Computed Quantities

For each `omega`, the script computes the threshold and the kinematic quantities derived in `special_case_derivation.md`:

```text
omega_0 = pi c / L
omega_ratio = omega / omega_0
v_tip = omega L / 2
t_rot = pi / (2 omega)
t_clear = L / (2 c)
Delta t = t_clear - t_rot
s_re = pi c / (2 omega)
ell_rem = L / 2 - s_re
```

The regime classification is determined only by the threshold comparison:

- `omega < omega_0` -> `instantaneous_contact`
- `omega = omega_0` -> `critical_recollision`
- `omega > omega_0` -> `non_instantaneous_gliding_contact`

The location of first re-encounter is recorded as:

- `off_segment` below threshold
- `tip` at threshold
- `interior` above threshold

## 4. Fixed CSV Schema

The script writes one CSV row per input `omega` with LF line endings and the following fixed columns.

| Column | Meaning |
| --- | --- |
| `omega` | Angular speed under test |
| `length` | Segment length `L` |
| `separation_speed` | Separation speed `c` |
| `omega_0` | Threshold `pi c / L` |
| `omega_ratio` | `omega / omega_0` |
| `v_tip` | Tip speed `omega L / 2` |
| `t_rot` | First quarter-turn time `pi / (2 omega)` |
| `t_clear` | Tip-clearance time `L / (2 c)` |
| `delta_t` | Kinematic timing margin `t_clear - t_rot` |
| `s_re` | First re-encounter coordinate `pi c / (2 omega)` |
| `ell_rem` | Remaining half-length `L / 2 - s_re` |
| `first_reencounter_location` | `off_segment`, `tip`, or `interior` |
| `interior_reencounter_occurs` | `yes` only when `s_re < L/2` |
| `gliding_contact_occurs` | `yes` only in the above-threshold regime supported by the source note |
| `regime` | Regime label from the threshold comparison |
| `tau_contact_supported` | Whether the current source set supports a derived `tau_contact` value |
| `tau_contact` | Contact duration field, left blank by the current instrument |
| `tau_contact_status` | Reason the duration field is blank |

## 5. Interpretation of `Delta t` and `ell_rem`

`Delta t` and `ell_rem` are kinematic diagnostics for threshold crossing.

They show whether the first possible re-encounter occurs before tip clearance and whether that first re-encounter lies in the interior of `AB`. They do not supply a closed-form gliding-contact duration.

The correct interpretation is:

- `Delta t < 0`: no interior re-encounter
- `Delta t = 0`: first re-encounter at the extremity
- `Delta t > 0`: first re-encounter in the interior

Neither `Delta t` nor `ell_rem` should be relabeled as `tau_contact`.

## 6. `tau_contact` Boundary

The source note states that above threshold the segments remain in non-instantaneous gliding contact and that the contact duration grows with `omega`. The present source set does not specify the post-recollision contact law needed to derive that duration uniquely.

The unresolved step is the same one identified in `special_case_derivation.md`:

```text
Once interior contact is re-established, what kinematic condition keeps the same moving contact point on both segments until separation?
```

Because that closure law is absent, the script emits:

- `tau_contact_supported = no`
- `tau_contact = ""`
- `tau_contact_status = undetermined_from_source_note`

This is an explicit limit of the current artifact, not a silent omission.

## 7. Canonical Validation Case

Running

```text
python3 scripts/special_case_experiment.py
```

with the defaults `L = 2` and `c = 1` yields `omega_0 = pi/2` and the following regime coverage:

| `omega` | Expected regime | Expected diagnostic sign |
| --- | --- | --- |
| `1` | `instantaneous_contact` | `delta_t < 0`, `ell_rem < 0` |
| `pi/2` | `critical_recollision` | `delta_t = 0`, `ell_rem = 0` |
| `2` | `non_instantaneous_gliding_contact` | `delta_t > 0`, `ell_rem > 0` |

This no-argument run is the fixed threshold-spanning validation case for Milestone 3.

## 8. What the Instrument Establishes

Within the constrained geometry, the instrument provides a deterministic mapping from `omega`, `L`, and `c` to:

- the threshold `omega_0`
- the sign of the timing margin `Delta t`
- the first re-encounter location
- the regime label implied by that threshold comparison

That is the correct support level for the current source material. Any future artifact that reports a numeric `tau_contact` must first add the missing post-recollision contact law explicitly.
