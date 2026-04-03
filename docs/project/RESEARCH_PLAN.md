# Research Plan for a Technical Note on the Rotating Vector Model Inertia Mechanism

## 1. Purpose

This document defines the work required to produce a professional, research-grade technical note based on [`dijksman_rvm_revised.md`](../source/dijksman_rvm_revised.md).

That document is the ground-truth source for scope, claims, and terminology. All supporting documents, derivations, experiments, figures, and summary notes must remain consistent with it. Nothing in this plan widens the claim surface beyond what the ground-truth document supports.

The target outcome is a technical note that is:

- technically explicit
- scoped correctly
- experimentally supported where claims are empirical
- clear about what is established, what is conjectural, and what remains open

## 2. Ground-Truth Contract

The current ground-truth document makes a narrow claim:

- In one geometrically constrained two-particle collision, massless rotating segments can exhibit non-instantaneous gliding contact that is structurally analogous to inertial resistance.

It does not claim:

- a complete theory of mass
- a derivation of mass-energy equivalence
- general validity across arbitrary collision geometries
- a demonstrated quantitative law equating angular speed with mass

Every research task in this plan must preserve that contract.

## 3. Final Deliverable

The final deliverable is a professional technical note suitable for circulation as a serious research document. It should contain:

- a compact statement of the problem
- exact definitions and assumptions
- a clean derivation of the special-case geometry
- deterministic computational experiments
- fixed, reproducible result artifacts
- an explicit generalization assessment
- a disciplined interpretation section that does not overclaim

The note should be understandable to a technically literate reader without requiring them to reconstruct missing assumptions from informal prose.

## 4. Research Objectives

The work should answer, in order, the following questions:

1. What exactly is the constrained collision geometry being claimed?
2. Can the threshold between instantaneous and gliding contact be derived cleanly?
3. Can the special-case mechanism be reproduced with a deterministic computational instrument?
4. How does gliding-contact duration depend on angular speed within the constrained geometry?
5. Does the effect persist when the four special constraints are relaxed one at a time?
6. If the effect persists, can a many-collision ensemble model justify a bulk resistance interpretation?
7. What is the strongest conclusion supported by the combined derivation and experiments?

## 5. Research Principles

The project should follow these principles throughout:

- Keep the scope narrow and explicit.
- Prefer one deterministic computational path over multiple fallback paths.
- Treat the code as a research instrument, not as a general software product.
- Separate analytic results from numerical results.
- Separate observed behavior from interpretation.
- State the strongest supported finding plainly, then bound it with exact limits.
- If a key conjecture fails under test, record that failure directly and update the plan.

## 6. Workstreams

The project divides into six workstreams. They should be developed in the order listed here because each later workstream depends on the earlier ones.

### Workstream A: Claim Control and Definitions

Purpose:
Create a precise contract for what the project is and is not trying to establish.

Deliverables:

- `claims.md`
- `definitions.md`
- `notation.md` if needed

Tasks:

- Extract every positive claim from the ground-truth document.
- Classify each claim as established, conjectural, or explicitly excluded.
- Define all symbols and operational terms.
- Fix a single vocabulary for "instantaneous contact," "critical recollision," "gliding contact," and "inertia-like behavior."

Completion criterion:

- A reader can tell exactly what is being tested before looking at any code or figures.

### Workstream B: Analytic Reconstruction of the Special Case

Purpose:
Rebuild the constrained collision argument in explicit mathematical form.

Deliverables:

- `special_case_derivation.md`
- one or more derivation figures if needed

Tasks:

- Specify the geometry in coordinates.
- Define the rotational and translational motions.
- Derive the threshold condition separating the three regimes.
- Determine whether a closed-form expression for contact duration can be derived.
- If a closed form cannot be derived, identify the exact unresolved step without inventing a substitute claim.

Completion criterion:

- The special case can be followed line by line without relying on informal intuition.

### Workstream C: Deterministic Experiment Instrument

Purpose:
Produce the smallest computational tool that can test the special-case claim.

Deliverables:

- one executable script
- one fixed output schema
- one methods note for the script

Tasks:

- Implement the constrained geometry only.
- Accept only the parameters required for the exact experiment.
- Compute contact behavior deterministically.
- Emit reproducible result files in plain text formats with LF endings.
- Keep the code auditable and minimal.

Minimum observables:

- regime classification
- whether gliding contact occurs
- contact duration
- threshold crossing behavior as angular speed varies

Completion criterion:

- The script can reproduce the special-case regime transition from a clean run and save stable outputs.

### Workstream D: Special-Case Results

Purpose:
Turn the instrument into a first set of evidence-bearing results.

Deliverables:

- `results/special_case_threshold.csv`
- `results/special_case_scaling.csv`
- `results/special_case_summary.md`
- `figures/special_case_threshold.png`
- `figures/special_case_scaling.png`

Tasks:

- Sweep angular speed across the threshold.
- Confirm the below-threshold, critical, and above-threshold regimes.
- Measure contact duration above threshold.
- Characterize how the duration changes with angular speed.
- Record any discontinuities, singular behavior, or numerical edge cases.

Completion criterion:

- The measured special-case behavior matches or falsifies the ground-truth description in a way that is inspectable and reproducible.

### Workstream E: One-At-A-Time Perturbation Tests

Purpose:
Test whether the special-case mechanism survives beyond the measure-zero setup.

Deliverables:

- `methods/perturbation_tests.md`
- one result file per perturbation family
- one figure per perturbation family
- `generalization_assessment.md`

Perturbation families:

- nonzero rotation of the second segment
- tilt of the collision plane away from perpendicular
- off-center contact
- oblique approach velocity

Tasks:

- Vary one parameter at a time while holding the others fixed.
- Use the same observables as the special-case experiment wherever possible.
- Record whether gliding contact persists, weakens, becomes ambiguous, or disappears.
- Avoid folding multiple departures from the original geometry into one experiment.

Completion criterion:

- The project has a defensible answer to whether the mechanism generalizes beyond the exact special case.

### Workstream F: Ensemble and Interpretation Layer

Purpose:
Only if Workstream E supports continuation, test whether repeated collisions can justify a bulk resistance interpretation.

Deliverables:

- `ensemble_model.md`
- `results/ensemble_summary.csv`
- `figures/ensemble_response.png`
- `interpretation_limits.md`

Tasks:

- Define the minimum many-collision setup needed to measure cumulative resistance-like behavior.
- Choose observables that are directly computed, not rhetorically named.
- Measure response versus angular speed and background density.
- State clearly whether the results justify saying "inertia-like resistance" at the ensemble level.
- State equally clearly what they do not justify.

Completion criterion:

- The interpretation layer is tied to measured quantities and bounded by exact assumptions.

## 7. Ordered Milestones

### Milestone 1: Claim Lock

Required outputs:

- `claims.md`
- `definitions.md`

Gate:

- No derivation or code work proceeds until the project has a fixed claim surface.

### Milestone 2: Special-Case Formalization

Required outputs:

- `special_case_derivation.md`

Gate:

- The threshold condition and regime definitions must be explicit before any numerical experiment is treated as evidence.

### Milestone 3: Research Instrument

Required outputs:

- minimal deterministic experiment script
- methods note

Gate:

- The instrument must compute the special case without hidden heuristics or undocumented branches.

### Milestone 4: Special-Case Evidence

Required outputs:

- threshold and scaling result files
- threshold and scaling figures
- summary note

Gate:

- The special-case claim must be empirically reproduced or explicitly revised.

### Milestone 5: Generalization Decision

Required outputs:

- perturbation result set
- `generalization_assessment.md`

Gate:

- The project must decide whether generalization is supported, limited, or false before discussing bulk inertia-like behavior.

### Milestone 6: Ensemble Decision

Required outputs:

- ensemble experiment and summary, only if justified

Gate:

- No ensemble narrative proceeds unless the perturbation tests show the special-case effect is not geometrically fragile.

### Milestone 7: Final Technical Note

Required outputs:

- the technical note itself
- fixed figures
- references
- appendix or methods supplement if needed

Gate:

- Every sentence in the final note must map to either the ground-truth contract, an explicit derivation, or a recorded result.

## 8. Recommended File Structure

The project should evolve toward a small, explicit structure like this:

```text
arjen_theories/
  RESEARCH_PLAN.md
  dijksman_rvm_revised.md
  claims.md
  definitions.md
  special_case_derivation.md
  generalization_assessment.md
  interpretation_limits.md
  technical_note.md
  methods/
    special_case_experiment.md
    perturbation_tests.md
  results/
    special_case_threshold.csv
    special_case_scaling.csv
    ensemble_summary.csv
  figures/
    special_case_threshold.png
    special_case_scaling.png
    ensemble_response.png
  scripts/
    special_case_experiment.py
    perturbation_experiments.py
    ensemble_experiment.py
```

This structure should remain small. Additional files should only be added when they serve a direct evidentiary role in the technical note.

## 9. Standards for Experiments

All experiments should satisfy the following standards:

- deterministic execution
- fixed parameter declaration
- explicit units or normalized units
- stable output schema
- no randomization unless the experiment specifically requires it and the rationale is documented
- no fallback computation paths
- no interpretation mixed into raw result files

Each experiment should produce:

- a methods note
- one or more machine-readable outputs
- one concise prose summary of the result

## 10. Standards for Writing

All supporting documents and the final note should follow this order wherever possible:

- observable setup
- definitions
- named quantities
- law or equation
- derivation or method
- measured effect
- interpretation
- scope limits

The prose should avoid:

- overclaiming beyond the tested regime
- using "mass" when only a resistance proxy has been measured
- substituting illustrations for derivations
- hiding open problems behind suggestive language

## 11. Failure Conditions

The plan should explicitly allow the project to stop or narrow if one of these occurs:

- the threshold condition in the special case cannot be reconstructed cleanly
- the numerical instrument does not reproduce the claimed regime structure
- gliding contact disappears under minimal perturbation, showing geometric fragility
- the ensemble model cannot be defined without smuggling in the desired conclusion

If any of these occur, the technical note should be rewritten to match the strongest surviving result rather than forcing the original narrative.

## 12. Immediate Next Actions

The next work should be:

1. Create `claims.md`.
2. Create `definitions.md`.
3. Write `special_case_derivation.md`.
4. Design the minimal deterministic special-case experiment script.
5. Define the output schema for the first result files.

These tasks establish the contract, the formal geometry, and the first evidence path. They should be completed before any attempt to write the final technical note.

## 13. Success Condition

This project succeeds if it produces a technical note whose strongest claim is exactly supported by its derivations and experiments, whose limits are explicit, and whose evidence can be audited from the files in this repository without reconstruction from chat history or informal drafts.
