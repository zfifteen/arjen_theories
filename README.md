![arjen_theories hero banner](assets/banner-hero.jpg)

# arjen_theories

This repository takes one geometric idea seriously and then narrows it until only auditable claims remain.

The starting idea comes from Arjen Dijksman's Rotating Vector Model: maybe inertia-like resistance does not need to be assumed as a primitive property, but can instead emerge mechanically from collisions between massless rotating line segments. This repository does not claim that the idea has been proved as a theory of mass. It asks a smaller question and answers it carefully: in the exact collision geometry described by the source note, is there a clean threshold where contact changes from instantaneous to sustained gliding, and does the current source set justify saying that the effect survives outside that special case?

The strongest supported answer is narrow and clear. Inside one four-constraint special case, the threshold

```text
omega_0 = pi c / L
```

is supported analytically and reproduced deterministically in code and fixed result files. Outside that special case, the current source set does not yet support a deterministic yes-or-no generalization claim. That is the point of this repository: not to make the idea sound larger, but to show exactly what survives careful reconstruction.

## What Arjen's Original Conjecture Was

The repository's primary source is [`dijksman_rvm_revised.md`](docs/source/dijksman_rvm_revised.md), which preserves the physical content of the original note while correcting its claim boundaries. That revised note cites Arjen's original `materion.free.fr` page at `http://materion.free.fr/OldVersion/physique/reconsider.htm`, and [`thread.md`](docs/history/thread.md) preserves part of the public citation trail around the broader materion / RVM idea.

In plain language, the original conjecture is:

1. A fundamental particle can be modeled as a massless line segment of fixed length `L` rotating about its center.
2. In one specially arranged two-particle collision, a fast enough rotating segment can keep contact with another segment for a nonzero time instead of just touching and separating instantly.
3. That sustained gliding contact produces resistance to translational motion that is structurally analogous to inertia.
4. If that mechanism survived beyond the exact special geometry, and if many such collisions were accumulated statistically, it might point toward a mechanical origin of inertia and eventually toward a mass-like interpretation.

That last step is the conjectural leap. The original idea is interesting because it tries to move from geometry to inertia. It becomes difficult because each step after the special case requires new derivations that the source note does not yet supply.

## What This Repository Refines

The repository keeps the intuition but tightens the logic.

What was broadened in the original intuition:

- a special-case collision result was allowed to suggest a more general mechanical mechanism
- gliding contact was treated as if it were already close to an inertia law
- the path from collision geometry to mass-like behavior was left open-ended

What is refined here:

- the source note is rewritten as a scoped, corrected technical statement in [`dijksman_rvm_revised.md`](docs/source/dijksman_rvm_revised.md)
- the exact claim surface is locked in [`claims.md`](docs/foundations/claims.md)
- the basic objects, symbols, and operational terms are fixed in [`definitions.md`](docs/foundations/definitions.md)
- the special-case threshold is derived explicitly in [`special_case_derivation.md`](docs/analysis/special_case_derivation.md)
- a deterministic special-case instrument is implemented in [`scripts/special_case_experiment.py`](scripts/special_case_experiment.py)
- one-at-a-time perturbation tests are defined and executed without pretending that unsupported formulas transfer automatically
- the project stops at the point where the source support runs out

The practical difference is simple: the original idea was "this may be a mechanical route to inertia." The refined result in this repository is "one constrained collision mechanism survives careful reconstruction; broader claims remain open."

## Main Result

Within the following four simultaneous constraints,

1. `omega_CD = 0`
2. segment `AB` rotates in a plane perpendicular to `CD`
3. initial contact occurs at the geometric centers
4. the translational approach of `CD` is perpendicular to `AB` at contact

the repository supports a clean threshold law:

```text
omega_0 = pi c / L
```

That threshold separates three regimes:

| Condition | Supported regime |
| --- | --- |
| `omega < omega_0` | instantaneous contact |
| `omega = omega_0` | critical recollision at the tip |
| `omega > omega_0` | interior re-encounter consistent with non-instantaneous gliding onset |

This is an existence result inside the constrained geometry only.

The repository does **not** claim:

- a closed-form law for `tau_contact`
- a demonstrated generalization beyond the special case
- an ensemble inertia law
- a derivation of mass or `E = mc^2`

## Technical Explanation of What Was Developed Here

The repository is organized as a small research pipeline.

### 1. Claim control

[`claims.md`](docs/foundations/claims.md) extracts what the source note actually claims, what it merely hypothesizes, and what it explicitly does not claim. This prevents later code and figures from sounding stronger than the source support allows.

[`definitions.md`](docs/foundations/definitions.md) then fixes the objects and terms used everywhere else: segment length `L`, separation speed `c`, angular speed `omega`, the threshold `omega_0`, the three regime labels, and the meaning of `tau_contact`.

### 2. Analytic derivation

[`special_case_derivation.md`](docs/analysis/special_case_derivation.md) turns the special-case picture into explicit timing comparisons. The key comparison is between

```text
t_rot = pi / (2 omega)
t_clear = L / (2 c)
```

and that is what yields the threshold `omega_0 = pi c / L`.

The derivation also defines the kinematic diagnostics used later:

```text
Delta t = t_clear - t_rot
s_re = pi c / (2 omega)
ell_rem = L / 2 - s_re
```

These are threshold-crossing diagnostics. They are not silently rebranded as a duration law.

### 3. Deterministic instrument

[`scripts/special_case_experiment.py`](scripts/special_case_experiment.py) is a narrow deterministic instrument for the constrained geometry. It runs with no command-line arguments and evaluates the canonical threshold-spanning default case:

```text
omega values = (1, pi/2, 2)
L = 2
c = 1
```

It writes a fixed CSV schema with columns such as:

- `omega`
- `omega_0`
- `omega_ratio`
- `v_tip`
- `t_rot`
- `t_clear`
- `delta_t`
- `s_re`
- `ell_rem`
- `first_reencounter_location`
- `gliding_contact_occurs`
- `tau_contact_supported`

The methods contract for that script is documented in [`methods/special_case_experiment.md`](docs/methods/special_case_experiment.md).

### 4. Fixed evidence package

The core evidence files are:

- [`results/special_case_threshold.csv`](results/special_case_threshold.csv)
- [`results/special_case_scaling.csv`](results/special_case_scaling.csv)
- [`results/special_case_summary.md`](docs/results/special_case_summary.md)
- [`figures/special_case_threshold.png`](figures/special_case_threshold.png)
- [`figures/special_case_scaling.png`](figures/special_case_scaling.png)

These show that the threshold transition is reproducible and that the supported kinematic diagnostics vary smoothly above threshold.

### 5. One-at-a-time perturbation program

The original note named four ways the special case could fail to generalize. This repository turns those into a bounded perturbation program in [`methods/perturbation_tests.md`](docs/methods/perturbation_tests.md):

- nonzero `omega_CD`
- non-perpendicular collision plane
- off-center contact
- oblique approach angle

Each family keeps a zero-perturbation control row set and varies only one parameter at a time. The repository then records the family-level result in:

- [`results/perturbation_cd_rotation.csv`](results/perturbation_cd_rotation.csv)
- [`results/perturbation_plane_tilt.csv`](results/perturbation_plane_tilt.csv)
- [`results/perturbation_contact_offset.csv`](results/perturbation_contact_offset.csv)
- [`results/perturbation_approach_angle.csv`](results/perturbation_approach_angle.csv)
- [`generalization_assessment.md`](docs/analysis/generalization_assessment.md)

The result is not "generalization succeeded" and not "generalization failed." The correct result is "nonzero perturbation families remain ambiguous under the current source set because the necessary family-specific post-recollision contact laws are missing."

## Evidence Plots

### Special-case threshold sweep

![Fixed special-case threshold sweep](https://raw.githubusercontent.com/zfifteen/arjen_theories/fe4861a1826a85e948a2bfe08f76c93df80d3bb2/figures/special_case_threshold.png)

This figure visualizes the central special-case transition. Negative `ell_rem` values mean the first possible re-encounter lies beyond the available half-length of `AB`, so no interior re-encounter is supported. Zero is the tip case. Positive values move the first re-encounter into the interior, which is the supported onset of non-instantaneous gliding contact.

### Above-threshold scaling diagnostics

![Special-case above-threshold scaling diagnostics](https://raw.githubusercontent.com/zfifteen/arjen_theories/fe4861a1826a85e948a2bfe08f76c93df80d3bb2/figures/special_case_scaling.png)

This figure is intentionally modest in what it claims. It shows that once the system is above threshold, the available kinematic diagnostics change smoothly with `omega / omega_0`. It does **not** plot `tau_contact`, because the repository does not derive that quantity from the current source set.

### CD-rotation perturbation matrix

![CD rotation perturbation status matrix](https://raw.githubusercontent.com/zfifteen/arjen_theories/fe4861a1826a85e948a2bfe08f76c93df80d3bb2/figures/perturbation_cd_rotation.png)

The bottom control row reproduces the special-case transition: no supported gliding below threshold, the threshold anchor at `omega / omega_0 = 1`, and supported gliding above threshold. Every nonzero `omega_CD / omega` row remains ambiguous because the source set does not provide a family-specific gliding/contact law for rotating `CD`.

### Plane-tilt perturbation matrix

![Plane tilt perturbation status matrix](https://raw.githubusercontent.com/zfifteen/arjen_theories/fe4861a1826a85e948a2bfe08f76c93df80d3bb2/figures/perturbation_plane_tilt.png)

This plot asks whether the effect survives once the collision plane is no longer exactly perpendicular. The control row still behaves like the special case. Every nonzero tilt row stays ambiguous for the same reason: no perturbed-geometry closure law is available.

### Contact-offset perturbation matrix

![Contact offset perturbation status matrix](https://raw.githubusercontent.com/zfifteen/arjen_theories/fe4861a1826a85e948a2bfe08f76c93df80d3bb2/figures/perturbation_contact_offset.png)

This plot tests whether the phenomenon survives once the collision is no longer center-on-center. Again, the control row is intact and every nonzero row remains ambiguous under the current source set.

### Approach-angle perturbation matrix

![Approach angle perturbation status matrix](https://raw.githubusercontent.com/zfifteen/arjen_theories/fe4861a1826a85e948a2bfe08f76c93df80d3bb2/figures/perturbation_approach_angle.png)

This plot tests oblique approach rather than perpendicular approach. It closes the same way as the other perturbation families: special-case control retained, nonzero rows unresolved.

## Reading Order

If you want the fastest route through the repository, read these in order:

1. [`README.md`](README.md)
2. [`PROJECT_STATUS.md`](docs/project/PROJECT_STATUS.md)
3. [`technical_note.md`](docs/analysis/technical_note.md)
4. [`dijksman_rvm_revised.md`](docs/source/dijksman_rvm_revised.md)
5. [`special_case_derivation.md`](docs/analysis/special_case_derivation.md)
6. [`results/special_case_summary.md`](docs/results/special_case_summary.md)
7. [`generalization_assessment.md`](docs/analysis/generalization_assessment.md)
8. [`interpretation_limits.md`](docs/analysis/interpretation_limits.md)

## What Counts as the Finished Research Result

The evidence-bearing core of the repo is:

- [`dijksman_rvm_revised.md`](docs/source/dijksman_rvm_revised.md)
- [`claims.md`](docs/foundations/claims.md)
- [`definitions.md`](docs/foundations/definitions.md)
- [`special_case_derivation.md`](docs/analysis/special_case_derivation.md)
- [`methods/special_case_experiment.md`](docs/methods/special_case_experiment.md)
- [`methods/perturbation_tests.md`](docs/methods/perturbation_tests.md)
- [`results/`](results/)
- [`figures/`](figures/)
- [`generalization_assessment.md`](docs/analysis/generalization_assessment.md)
- [`interpretation_limits.md`](docs/analysis/interpretation_limits.md)
- [`technical_note.md`](docs/analysis/technical_note.md)

Historical or exploratory materials are kept for provenance, but they should not be read as the bounded final conclusion without checking them against the claim controls above. That includes items such as:

- [`thread.md`](docs/history/thread.md)
- [`The Concept of Inertia.pdf`](<The Concept of Inertia.pdf>)
- [`experiment.md`](docs/history/experiment.md)
- [`demo.py`](demo.py)

## Reproducing the Core Instrument

The core special-case instrument runs with no arguments:

```bash
python3 scripts/special_case_experiment.py
```

That command prints the canonical threshold-spanning CSV rows to stdout.

The perturbation plotting scripts also support no-argument execution with their canonical defaults:

```bash
python3 scripts/plot_perturbation_cd_rotation.py
python3 scripts/plot_perturbation_plane_tilt.py
python3 scripts/plot_perturbation_contact_offset.py
python3 scripts/plot_perturbation_approach_angle.py
```

## Next Steps and Research Roadmap

The next steps are not "make the theory bigger." They are the smallest steps required to justify any stronger statement.

1. Derive a post-recollision contact law for the special case.
   Without that, `tau_contact` is still not a supported numeric quantity.

2. Resolve at least one nonzero perturbation family with a family-specific law.
   A single deterministic persistence or disappearance result would move the project past the current `ambiguous` boundary.

3. Re-evaluate the perturbation families one by one.
   The point is to learn whether the special-case mechanism is representative or geometrically fragile.

4. Open the ensemble layer only if perturbation support exists.
   A many-collision inertia interpretation is downstream of, not prior to, the geometry question.

5. Test any later scaling proposal against the note's explicit non-claims.
   No later work should smuggle in "mass," "`omega` equals mass," or "`E = mc^2`" language without a separate derivation.

## Why This Repository Matters

The value here is not that it proves a sweeping theory. The value is that it converts a broad and interesting intuition into a small set of statements that can be defended line by line:

- what the constrained geometry supports
- what the deterministic computations reproduce
- what the perturbation suite does and does not decide
- where the project must stop to avoid overclaiming

That makes the repository useful even if the larger theory never closes. It is a worked example of taking a speculative physical idea, extracting its strongest testable core, and keeping only what survives.
