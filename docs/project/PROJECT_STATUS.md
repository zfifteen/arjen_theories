# Project Status

## Project Goal

The project goal is a professional, research-grade technical note that determines, in order, whether the mechanism in `dijksman_rvm_revised.md` can be stated cleanly, reproduced deterministically in the constrained special case, tested beyond that special case, and only then interpreted at ensemble scale.

The note is not trying to prove a full theory of mass. Its bounded target is narrower: establish exactly what the constrained special case supports, test whether that effect survives one-at-a-time perturbations, and stop if the evidence fails.

## Current Position

- Project state: wrapped and bounded
- Completed milestones: 1 through 5 and 7
- Milestone 6 disposition: not opened as an evidence-bearing workstream because Milestone 5 did not justify continuation to the ensemble layer
- Final technical-note artifacts: `generalization_assessment.md`, `interpretation_limits.md`, and `technical_note.md`

The project has moved from an informal theory note to a bounded special-case evidence package plus a formal stop decision on what does and does not generalize.

## Strongest Supported Result So Far

Within the four-constraint special-case geometry, the threshold

```text
omega_0 = pi c / L
```

cleanly separates three regimes:

- below threshold: no interior re-encounter
- at threshold: extremity recollision
- above threshold: interior re-encounter consistent with non-instantaneous gliding onset

This result is now supported three ways in the repository:

- analytically in [`special_case_derivation.md`](../analysis/special_case_derivation.md)
- computationally in [`scripts/special_case_experiment.py`](../../scripts/special_case_experiment.py) and [`special_case_experiment.md`](../methods/special_case_experiment.md)
- empirically in the fixed Milestone 4 outputs under [`results/`](../../results/) and [`figures/`](../../figures/)

That is an existence result within the constrained geometry only. It is not a duration law, not a demonstrated generalization result, and not an ensemble result.

## Final Project Decision

The project now has a clear stopping point.

- `generalization_assessment.md` closes Milestone 5 by showing that every perturbation artifact reproduces the zero-perturbation control transition while every tested nonzero perturbation value remains `ambiguous`
- `interpretation_limits.md` records the exact boundary this creates for interpretation
- `technical_note.md` integrates the derivation, experiment artifacts, generalization decision, and stop condition into the final note

The repository therefore supports a constrained special-case existence result and an explicit statement that generalization remains unresolved outside that special case.

## What Has Been Delivered

| Milestone | Key artifacts | Delivered value |
| --- | --- | --- |
| 1. Claim Lock | [`claims.md`](../foundations/claims.md), [`definitions.md`](../foundations/definitions.md) | Fixed the claim surface so later artifacts do not overstate what the source note supports |
| 2. Special-Case Formalization | [`special_case_derivation.md`](../analysis/special_case_derivation.md) | Made the threshold derivation explicit and isolated the exact missing step that blocks a closed-form `tau_contact` law |
| 3. Research Instrument | [`scripts/special_case_experiment.py`](../../scripts/special_case_experiment.py), [`special_case_experiment.md`](../methods/special_case_experiment.md) | Produced a deterministic instrument with a fixed CSV schema that reproduces the special-case threshold transition |
| 4. Special-Case Evidence | [`results/special_case_threshold.csv`](../../results/special_case_threshold.csv), [`results/special_case_scaling.csv`](../../results/special_case_scaling.csv), [`special_case_summary.md`](../results/special_case_summary.md), [`figures/special_case_threshold.png`](../../figures/special_case_threshold.png), [`figures/special_case_scaling.png`](../../figures/special_case_scaling.png) | Completed a fixed evidence package showing the special-case threshold transition and above-threshold kinematic trends without inventing a numeric `tau_contact` law |
| 5. Generalization Decision | [`perturbation_tests.md`](../methods/perturbation_tests.md), perturbation result files and figures, [`generalization_assessment.md`](../analysis/generalization_assessment.md) | Closed the four one-at-a-time perturbation families and recorded the correct bounded outcome: every nonzero family remains `ambiguous` under the current source set |
| 6. Ensemble Decision | [`interpretation_limits.md`](../analysis/interpretation_limits.md) | Stopped the project before any unsupported ensemble narrative and fixed the language boundary for future use |
| 7. Final Technical Note | [`technical_note.md`](../analysis/technical_note.md) | Integrated the surviving derivation, evidence, and limits into the final research-grade note |

## What Remains Open

These are open research problems, not missing deliverables for this repository state:

- derive a post-recollision contact law that yields a supported `tau_contact`
- derive at least one family-specific perturbation law that converts `ambiguous` nonzero rows into deterministic persistence or disappearance results
- justify an ensemble layer only after that perturbation support exists
- test any later ensemble scaling law against the note's explicitly excluded mass claims

## Final Wrap-Up Value

The value of the finished repository is not that it proved a broad theory. The value is that it turns an initially loose intuition into a small set of auditable statements:

- what the constrained special case supports
- what the fixed computations reproduce
- what the perturbation tests do and do not decide
- where the project must stop to avoid overclaiming

## Reading Order

If you want the shortest path through the repo, read these in order:

1. [`PROJECT_STATUS.md`](PROJECT_STATUS.md)
2. [`technical_note.md`](../analysis/technical_note.md)
3. [`claims.md`](../foundations/claims.md)
4. [`definitions.md`](../foundations/definitions.md)
5. [`special_case_derivation.md`](../analysis/special_case_derivation.md)
6. [`special_case_summary.md`](../results/special_case_summary.md)
7. [`generalization_assessment.md`](../analysis/generalization_assessment.md)
8. [`interpretation_limits.md`](../analysis/interpretation_limits.md)

## Current Research Limit

The main open technical limit has not changed:

- the repository still does not contain a derived post-recollision contact law
- because of that, no artifact should claim a numeric `tau_contact` law yet
- because of that, the nonzero perturbation families remain `ambiguous`
- because of that, no ensemble interpretation should be treated as established in this repository state
