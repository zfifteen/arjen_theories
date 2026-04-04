# Supplemental Derivation for the Approach-Angle Onset Threshold

This note records a bounded supplemental result for one perturbation family from [`methods/perturbation_tests.md`](../methods/perturbation_tests.md).

It asks a narrower question than the current perturbation CSV answers:

- under oblique translational approach
- while keeping the other three special-case constraints fixed
- when does the first post-contact re-encounter move from off-segment to the segment interior

This note does not derive `tau_contact`. It does not establish sustained gliding after re-encounter. It does not change the repository's current final stop condition. Its purpose is narrower: document a family-specific onset law for first re-encounter in the approach-angle family.

## 1. Scope

Keep the following three special-case constraints from [`special_case_derivation.md`](special_case_derivation.md):

- `omega_CD = 0`
- segment `AB` rotates in a plane perpendicular to `CD`
- initial contact occurs at the geometric centers

Relax only the fourth constraint.

Let the translational path of `CD` in the rotation plane make an angle `alpha` away from the special-case perpendicular direction, with:

```text
0 <= alpha < pi / 2
```

Here:

- `alpha = 0` is the special-case perpendicular approach
- larger `alpha` means a more oblique in-plane approach
- the limit `alpha -> pi / 2` is degenerate because the translational path approaches tangency with `AB` at the initial instant

## 2. Coordinate Model

Use the same coordinates as in [`special_case_derivation.md`](special_case_derivation.md).

Segment `AB` has midpoint at the origin and rotates in the `xy` plane:

```text
r_AB(s, t) = (s cos(omega t), s sin(omega t), 0)
```

with

```text
-L/2 <= s <= L/2
```

The projected translational path of `CD` is now:

```text
r_CD(t) = (c t sin(alpha), c t cos(alpha), 0)
```

This choice preserves the special-case convention that `alpha = 0` corresponds to motion along the positive `y` direction.

## 3. First Re-Encounter Condition

A post-contact re-encounter requires:

```text
r_AB(s, t) = r_CD(t)
```

which gives:

```text
s cos(omega t) = c t sin(alpha)
s sin(omega t) = c t cos(alpha)
```

For `t > 0`, a nontrivial re-encounter again has `s != 0`. Dividing the two equations gives:

```text
tan(omega t) = cot(alpha) = tan(pi / 2 - alpha)
```

For

```text
0 <= alpha < pi / 2
```

the first positive solution is:

```text
omega t_re = pi / 2 - alpha
```

so:

```text
t_re = (pi / 2 - alpha) / omega
```

At that instant the direction of the material point on `AB` matches the direction of the translated path of `CD`, and the contact coordinate is:

```text
s_re = c t_re = c (pi / 2 - alpha) / omega
```

This reduces exactly to the special-case result

```text
t_re = pi / (2 omega)
s_re = pi c / (2 omega)
```

when `alpha = 0`.

## 4. Approach-Angle Threshold Law

The first re-encounter lies on the segment if and only if:

```text
s_re <= L / 2
```

Substitute the expression above:

```text
c (pi / 2 - alpha) / omega <= L / 2
```

which rearranges to:

```text
omega >= c (pi - 2 alpha) / L
```

Define the family-specific onset threshold:

```text
omega_c(alpha) = c (pi - 2 alpha) / L
```

Using the special-case threshold

```text
omega_0 = pi c / L
```

this becomes:

```text
omega_c(alpha) = omega_0 (1 - 2 alpha / pi)
```

This is the supplemental result of the note.

It has three immediate consequences:

- `omega_c(0) = omega_0`, so the special case is recovered exactly
- `omega_c(alpha)` decreases linearly as the approach becomes more oblique
- `omega_c(alpha) -> 0` as `alpha -> pi / 2` from below, reflecting the tangential degeneracy of the setup

## 5. Regime Labels for First Re-Encounter

Within this narrower onset-only derivation, the first re-encounter location is classified by the sign of:

```text
ell_alpha = L / 2 - s_re = L / 2 - c (pi / 2 - alpha) / omega
```

The interpretation matches the special-case derivation:

- `ell_alpha < 0`: first re-encounter lies beyond the available half-length, so no interior re-encounter is supported
- `ell_alpha = 0`: the first re-encounter lands exactly at the extremity
- `ell_alpha > 0`: the first re-encounter lies in the interior

Equivalently:

- `omega < omega_c(alpha)` gives off-segment re-encounter
- `omega = omega_c(alpha)` gives the extremity case
- `omega > omega_c(alpha)` gives interior re-encounter

## 6. Canonical Sweep Predictions

On the repository's fixed reference sweep

```text
omega / omega_0 in {0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5}
```

the onset law predicts the following first-reencounter patterns for the declared nonzero angle ladder in [`results/perturbation_approach_angle.csv`](../../results/perturbation_approach_angle.csv):

| `approach_angle_degrees` | `omega_c / omega_0` | Canonical onset pattern |
| --- | --- | --- |
| `0` | `1` | `off / off / off / tip / interior / interior / interior` |
| `15` | `5/6` | `off / off / interior / interior / interior / interior / interior` |
| `30` | `2/3` | `off / interior / interior / interior / interior / interior / interior` |
| `45` | `1/2` | `tip / interior / interior / interior / interior / interior / interior` |
| `60` | `1/3` | `interior / interior / interior / interior / interior / interior / interior` |

These are onset predictions only. They classify where the first possible re-encounter occurs along `AB`. They do not yet classify the duration of any later gliding interval.

## 7. What This Note Changes

This supplemental derivation sharpens one part of the perturbation story.

It supports the statement that the approach-angle family is not intrinsically ambiguous at the level of first re-encounter onset. Under the retained three-constraint geometry, that onset threshold shifts deterministically with `alpha` according to:

```text
omega_c(alpha) = omega_0 (1 - 2 alpha / pi)
```

That is a narrower and more explicit claim than "all nonzero approach angles are unresolved."

## 8. What This Note Does Not Change

This note does not establish any of the following:

- that interior first re-encounter automatically implies sustained gliding contact
- that `gliding_contact_occurs` can now be filled deterministically for all nonzero approach-angle rows
- that `tau_contact` has been derived for oblique approach
- that the overall generalization assessment should be upgraded from its current bounded stop condition

The current repository boundary still matters.

[`generalization_assessment.md`](generalization_assessment.md) and [`technical_note.md`](technical_note.md) use `gliding_contact_occurs` and `tau_contact` as the evidence-bearing quantities for Workstream E. The present note derives a family-specific onset law for first re-encounter only. It does not yet supply the post-recollision contact law needed to convert that onset result into a full persistence or duration result.

## 9. Practical Consequence

If this repository is reopened for further work on the approach-angle family, the next bounded artifact should separate onset from duration.

A family-specific onset file could report quantities such as:

- `approach_angle_degrees`
- `omega_reference_ratio`
- `t_re`
- `s_re`
- `ell_alpha`
- `first_reencounter_location`
- `interior_reencounter_occurs`

That would let the repository record the deterministic onset law documented here without overstating what is still missing for gliding persistence and `tau_contact`.
