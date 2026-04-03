# Work Log

## How To Read This Log

- For overall project progress, start with [`/Users/velocityworks/IdeaProjects/research/arjen_theories/PROJECT_STATUS.md`](/Users/velocityworks/IdeaProjects/research/arjen_theories/PROJECT_STATUS.md).
- In each entry below, `Results` is the delivered value of that run.
- `Next step` tells you which remaining gap that run left open.

## Run Value Index

| Entry | Delivered artifact or change | Delivered value |
| --- | --- | --- |
| 2026-04-01 / Entry 1 | `RESEARCH_PLAN.md` | Fixed the roadmap, milestones, and gates for the technical note |
| 2026-04-01 / Entry 2 | `special_case_derivation.md` | Made the special-case threshold explicit and isolated the exact blocker on `tau_contact` |
| 2026-04-02 / Entry 1 | Automation guardrail update | Prevented future runs from drifting into summary-only work while milestone artifacts were still missing |
| 2026-04-02 / Entry 2 | Automation target clarification | Fixed the canonical Milestone 3 targets so runs would produce the right artifacts |
| 2026-04-02 / Entry 3 | Canonical-destination fix | Made automation outputs land in the visible repo instead of staying trapped in scratch worktrees |
| 2026-04-02 / Entry 4 | `scripts/special_case_experiment.py` | Produced the deterministic instrument that reproduces the special-case regime transition |
| 2026-04-02 / Entry 5 | `methods/special_case_experiment.md` | Fixed the instrument contract, schema, and current analytic limit in prose |
| 2026-04-02 / Entry 6 | `results/special_case_threshold.csv` | Created the first fixed evidence file for the threshold transition |
| 2026-04-02 / Entry 7 | `results/special_case_summary.md` | Stated the strongest supported special-case result plainly and bounded it |
| 2026-04-02 / Entry 8 | `figures/special_case_threshold.png` | Added the first threshold figure so the regime transition is inspectable visually |
| 2026-04-02 / Entry 9 | `results/special_case_scaling.csv` | Added the fixed above-threshold scaling dataset for supported kinematic diagnostics |
| 2026-04-02 / Entry 10 | `figures/special_case_scaling.png` | Completed the Milestone 4 evidence package so the project can move to perturbation tests |
| 2026-04-02 / Entry 11 | `methods/perturbation_tests.md` | Fixed the one-at-a-time perturbation contract before the first Milestone 5 result run |
| 2026-04-02 / Entry 12 | `results/perturbation_cd_rotation.csv` | Added the first family-specific perturbation matrix while keeping nonzero `omega_CD` rows explicitly ambiguous |
| 2026-04-02 / Entry 13 | `figures/perturbation_cd_rotation.png` | Added the first family-specific perturbation figure without converting ambiguity into a persistence claim |
| 2026-04-02 / Entry 14 | `results/perturbation_plane_tilt.csv` | Added the second family-specific perturbation matrix with inspectable zero-tilt control rows |
| 2026-04-02 / Entry 15 | `figures/perturbation_plane_tilt.png`, `results/perturbation_contact_offset.csv`, `figures/perturbation_contact_offset.png` | Closed the plane-tilt family and completed the contact-offset family at the current source boundary |

## 2026-04-01

### Entry 1

- Objective: Establish the project roadmap for producing a research-grade technical note.
- Work performed: Created `RESEARCH_PLAN.md` as the canonical roadmap anchored to `dijksman_rvm_revised.md`.
- Files changed: `RESEARCH_PLAN.md`
- Results: The project now has explicit workstreams, milestones, gates, standards, failure conditions, and next actions.
- Decisions: `dijksman_rvm_revised.md` is the ground-truth theory document. `RESEARCH_PLAN.md` is the canonical roadmap.
- Next step: Create `claims.md`.

### Entry 2

- Objective: Complete the analytic reconstruction task for the constrained special-case collision.
- Work performed: Created `special_case_derivation.md` using only `dijksman_rvm_revised.md`, `claims.md`, and `definitions.md`; derived the threshold `omega_0 = pi c / L` from the explicit timing comparison `t_rot = pi / (2 omega)` versus `t_clear = L / (2 c)`; and identified the exact missing post-recollision contact law that still blocks a unique closed-form expression for `tau_contact`.
- Files changed: `special_case_derivation.md`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now contains a bounded analytic artifact that fixes one coordinate realization of the four-constraint geometry, recovers the three regimes from first re-encounter timing, and states precisely what must be added before any `tau_contact` formula can be claimed.
- Decisions: `Delta t = t_clear - t_rot` and `ell_rem = L/2 - s_re` are safe kinematic diagnostics for later experiments, but neither is to be labeled as `tau_contact` without an explicit gliding-contact constraint.
- Next step: Replace or supersede the current off-scope `demo.py` with a deterministic special-case instrument that computes `omega_0`, `t_rot`, `t_clear`, `Delta t`, `s_re`, and regime labels.

## 2026-04-02

### Entry 1

- Objective: Realign the automation so scheduled runs consistently produce the next milestone-gating artifact instead of drifting into summary or maintenance work.
- Work performed: Tightened the scheduler prompt in `/Users/velocityworks/.codex/automations/arjen-dijksman/automation.toml`; added explicit anti-drift guardrails to `automation/AUTOMATION_MEMORY.md`; and updated `automation/SCHEDULED_TASK_PROMPT.md` so each run must identify the highest-priority missing artifact and advance it when unblocked.
- Files changed: `automation/AUTOMATION_MEMORY.md`, `automation/SCHEDULED_TASK_PROMPT.md`, `/Users/velocityworks/.codex/automations/arjen-dijksman/automation.toml`, `automation/WORK_LOG.md`
- Results: The automation now explicitly treats memory updates and summaries as closeout work only, forbids communication-only tasks while a milestone-gating artifact is missing and unblocked, and requires each successful run to materially advance an artifact file.
- Decisions: Milestone 3 remains the active target. The next acceptable scheduled run should produce the deterministic special-case instrument or a directly supporting methods artifact, not another status summary.
- Next step: On the next automated run, create or replace the special-case script and methods note for the constrained geometry.

### Entry 2

- Objective: Remove the remaining control-layer ambiguity around unfinished work and canonical Milestone 3 targets.
- Work performed: Tightened `/Users/velocityworks/.codex/automations/arjen-dijksman/automation.toml` again so runs must inspect `git status --short`, resume unfinished milestone work, and target canonical Milestone 3 files; updated `automation/AUTOMATION_MEMORY.md` and `automation/SCHEDULED_TASK_PROMPT.md` to name `scripts/special_case_experiment.py` and `methods/special_case_experiment.md` as the canonical artifacts; and rewrote `/Users/velocityworks/.codex/automations/arjen-dijksman/memory.md` into a compact current-state snapshot instead of a running stream of commentary.
- Files changed: `automation/AUTOMATION_MEMORY.md`, `automation/SCHEDULED_TASK_PROMPT.md`, `automation/WORK_LOG.md`, `/Users/velocityworks/.codex/automations/arjen-dijksman/automation.toml`, `/Users/velocityworks/.codex/automations/arjen-dijksman/memory.md`
- Results: The control layer now tells the automation exactly which Milestone 3 files count, makes unfinished artifact continuation the default, and reduces memory clutter that could distract future runs.
- Decisions: `demo.py` is now explicitly treated as non-canonical. The next acceptable run outcome is to create or materially advance `scripts/special_case_experiment.py`; the methods note is secondary unless the script is genuinely blocked.
- Next step: On the next automated run, create `scripts/special_case_experiment.py` or continue it if partially present.

### Entry 3

- Objective: Repair destination drift so automation work becomes visible in the canonical repository path instead of remaining isolated in a detached worktree.
- Work performed: Updated the scheduler prompt and control files to treat `/Users/velocityworks/IdeaProjects/research/arjen_theories` as the canonical destination; added explicit promotion-and-verification rules; and synced the previously isolated derivation and control-layer progress into the canonical repo.
- Files changed: `automation/AUTOMATION_MEMORY.md`, `automation/SCHEDULED_TASK_PROMPT.md`, `automation/WORK_LOG.md`, `/Users/velocityworks/.codex/automations/arjen-dijksman/automation.toml`, `/Users/velocityworks/.codex/automations/arjen-dijksman/memory.md`
- Results: Future automated runs are now instructed to verify visible repo changes in the canonical repo path before ending, and the missing derivation/control-layer work has been promoted into the canonical repo.
- Decisions: The worktree is now explicitly scratch only. Canonical repo visibility is a required closeout condition for future runs.
- Next step: On the next automated run, create `scripts/special_case_experiment.py` and verify that it appears in `/Users/velocityworks/IdeaProjects/research/arjen_theories`.

### Entry 4

- Objective: Create the canonical deterministic special-case instrument for the constrained geometry.
- Work performed: Created `scripts/special_case_experiment.py` as a minimal CLI that evaluates one or more `omega` values using only the supported special-case kinematics from `dijksman_rvm_revised.md` and `special_case_derivation.md`; computed `omega_0`, `omega_ratio`, `v_tip`, `t_rot`, `t_clear`, `Delta t`, `s_re`, `ell_rem`, the first re-encounter location, and regime classification; emitted a fixed CSV schema with LF endings; and left `tau_contact` blank with status `undetermined_from_source_note` instead of inventing a post-recollision law. Promoted the script into `/Users/velocityworks/IdeaProjects/research/arjen_theories/scripts/special_case_experiment.py` and verified it with `python3 -m py_compile` plus a threshold-spanning run at `L = 2`, `c = 1`, and `omega = {1, pi/2, 2}`.
- Files changed: `scripts/special_case_experiment.py`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now has its first canonical Milestone 3 artifact. The script reproduces the below-threshold off-segment case, the threshold tip case, and the above-threshold interior re-encounter case without widening the claim surface beyond the source note.
- Decisions: The script is a kinematic regime instrument, not a `tau_contact` solver. `gliding_contact_occurs` is reported as the source-note regime classification for the above-threshold case, while `tau_contact` remains explicitly unresolved until a post-recollision contact law exists.
- Next step: Write `methods/special_case_experiment.md` so the script contract, output columns, and current analytic limit are fixed in prose before generating result artifacts.

### Entry 5

- Objective: Complete the Milestone 3 methods artifact for the deterministic special-case instrument.
- Work performed: Created `methods/special_case_experiment.md` using only `dijksman_rvm_revised.md`, `claims.md`, `definitions.md`, `special_case_derivation.md`, and `scripts/special_case_experiment.py`; documented the four-constraint scope, exact input contract, computed kinematic quantities, fixed CSV schema, no-argument threshold-spanning validation case, and the explicit reason `tau_contact` remains blank. Promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/methods/special_case_experiment.md` and re-verified the default run of `python3 scripts/special_case_experiment.py`.
- Files changed: `methods/special_case_experiment.md`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 3 now has both required canonical artifacts: the deterministic script and its methods note. The repository now has a written contract for the current instrument, including the statement that `Delta t` and `ell_rem` are threshold diagnostics and not derived values of `tau_contact`.
- Decisions: Milestone 4 is now the active milestone. The next artifact should be `results/special_case_threshold.csv` from a fixed threshold-spanning sweep rather than more Milestone 3 documentation.
- Next step: Generate `results/special_case_threshold.csv` with fixed `omega` values spanning below, at, and above `omega_0`, then summarize the threshold result.

### Entry 6

- Objective: Create the first canonical Milestone 4 result artifact for the special-case threshold transition.
- Work performed: Ran `scripts/special_case_experiment.py` with the fixed seven-point sweep `omega / omega_0 = {0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5}` using the canonical normalization `L = 2` and `c = 1`; wrote the resulting CSV to `results/special_case_threshold.csv`; and promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/results/special_case_threshold.csv`.
- Files changed: `results/special_case_threshold.csv`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now has its first Milestone 4 evidence file. The sweep reproduces the expected regime transition exactly: `delta_t` and `ell_rem` are negative below threshold, zero at `omega = omega_0`, and positive above threshold; `first_reencounter_location` moves from `off_segment` to `tip` to `interior`; and the regime labels match `instantaneous_contact`, `critical_recollision`, and `non_instantaneous_gliding_contact`.
- Decisions: This CSV is the canonical threshold dataset for the constrained special case. `tau_contact` remains blank with status `undetermined_from_source_note`; the current source set still does not support a numeric gliding-duration law.
- Next step: Create `results/special_case_summary.md` to state the threshold finding plainly and bound it by the unresolved `tau_contact` limit.

### Entry 7

- Objective: Convert the fixed threshold CSV into the first evidence-bearing prose artifact for Milestone 4.
- Work performed: Created `results/special_case_summary.md` using only `dijksman_rvm_revised.md`, `claims.md`, `definitions.md`, `methods/special_case_experiment.md`, and `results/special_case_threshold.csv`; stated the exact threshold normalization `omega_0 = pi c / L = pi / 2` for `L = 2` and `c = 1`; summarized the seven-point sweep by below-threshold, threshold, and above-threshold regimes; highlighted the near-threshold `omega / omega_0 = 1.05` row as the immediate post-threshold interior re-encounter case; and promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/results/special_case_summary.md`.
- Files changed: `results/special_case_summary.md`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now has a canonical prose summary that states the strongest supported Milestone 4 finding plainly: the fixed sweep reproduces the source note's three-regime threshold structure in the constrained geometry. The artifact also records the exact current limit that `tau_contact` remains unsupported because the post-recollision contact law is absent from the source set.
- Decisions: `results/special_case_summary.md` is now the canonical interpretation note for `results/special_case_threshold.csv`. The next artifact should be the first threshold figure, not a duration claim or scaling analysis.
- Next step: Create `figures/special_case_threshold.png` directly from the fixed threshold CSV and keep the plotted claims limited to regime transition evidence.

### Entry 8

- Objective: Create the first canonical threshold figure for the fixed special-case sweep.
- Work performed: Generated `figures/special_case_threshold.png` directly from `results/special_case_threshold.csv` for the fixed seven-point sweep at `L = 2` and `c = 1`; plotted `ell_rem` against `omega / omega_0`; marked the threshold line at `omega / omega_0 = 1`; used separate markers for the instantaneous, critical, and above-threshold gliding regimes; and promoted the same PNG into `/Users/velocityworks/IdeaProjects/research/arjen_theories/figures/special_case_threshold.png`.
- Files changed: `figures/special_case_threshold.png`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now has a fixed visual artifact showing the threshold transition directly. Negative `ell_rem` values remain below threshold, the critical case lands exactly at zero, and positive `ell_rem` values begin immediately above threshold where the CSV reports interior re-encounter and non-instantaneous gliding contact.
- Decisions: The figure is limited to the threshold transition already supported by the current CSV and summary note. It does not introduce a numeric `tau_contact` claim.
- Next step: Create `results/special_case_scaling.csv` from a fixed above-threshold sweep before drawing the scaling figure.

### Entry 9

- Objective: Create the fixed above-threshold scaling dataset for the constrained special case.
- Work performed: Ran `scripts/special_case_experiment.py` with the fixed above-threshold sweep `omega / omega_0 = {1.05, 1.1, 1.25, 1.5, 2, 3, 4}` using the canonical normalization `L = 2` and `c = 1`; wrote the resulting rows to `results/special_case_scaling.csv`; verified that `delta_t` and `ell_rem` increase monotonically across the sweep while `s_re` decreases monotonically; and promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/results/special_case_scaling.csv`.
- Files changed: `results/special_case_scaling.csv`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now has the fixed Milestone 4 above-threshold dataset needed for the scaling figure. Every row remains in the `non_instantaneous_gliding_contact` regime, `first_reencounter_location` stays `interior`, and the available kinematic diagnostics vary smoothly with `omega / omega_0` without inventing a numeric `tau_contact` law.
- Decisions: `results/special_case_scaling.csv` is a kinematic scaling artifact, not a duration law. It records only the above-threshold observables supported by the current source set, and `tau_contact` remains blank with status `undetermined_from_source_note`.
- Next step: Create `figures/special_case_scaling.png` directly from `results/special_case_scaling.csv` and keep the plotted claim limited to above-threshold kinematic scaling.

## 2026-04-02

### Entry 10

- Objective: Create the missing special-case scaling figure for the fixed above-threshold sweep.
- Work performed: Generated `figures/special_case_scaling.png` directly from `results/special_case_scaling.csv`; plotted the supported above-threshold diagnostics `delta_t`, `s_re`, and `ell_rem` against `omega / omega_0`; added no `tau_contact` curve or duration claim; visually checked the rendered PNG in the worktree; and promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/figures/special_case_scaling.png`.
- Files changed: `figures/special_case_scaling.png`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 4 now has its full fixed artifact set in the canonical repository: threshold and scaling CSVs, threshold and scaling figures, and the special-case summary note. The new figure shows the fixed above-threshold sweep with monotone growth in `delta_t` and `ell_rem` and monotone decrease in `s_re`, matching the current kinematic support level of the source set.
- Decisions: The figure is limited to threshold-crossing diagnostics already supported by `dijksman_rvm_revised.md`, the derivation, and the current instrument. The unresolved post-recollision contact law still blocks any numeric `tau_contact` plot or duration scaling claim.
- Next step: Start Milestone 5 by creating `methods/perturbation_tests.md` so the one-at-a-time generalization tests have a fixed, source-bounded contract before any perturbation run.

### Entry 11

- Objective: Create the missing Milestone 5 methods artifact that fixes the perturbation-test contract before any family-specific generalization run.
- Work performed: Created `methods/perturbation_tests.md` using only `dijksman_rvm_revised.md`, `claims.md`, `definitions.md`, `special_case_derivation.md`, `methods/special_case_experiment.md`, `scripts/special_case_experiment.py`, and `results/special_case_summary.md`; fixed the special-case control configuration; defined the four allowed one-at-a-time perturbation families and their minimal parameters; anchored future family sweeps to the existing seven-point `omega / omega_0` reference sweep; specified the common cross-family observables; and stated explicitly that `delta_t`, `s_re`, `ell_rem`, and the special-case regime labels do not automatically transfer to nonzero perturbations. Promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/methods/perturbation_tests.md`.
- Files changed: `methods/perturbation_tests.md`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 5 now has its methods contract in the canonical repository. Future perturbation runs now have a fixed control, a bounded shared schema, explicit persistence labels, and a clear rule that `tau_contact` remains blank until a perturbed-geometry contact law is actually derived.
- Decisions: The special-case seven-point sweep is now the reference `omega` ladder for Workstream E comparisons. Nonzero perturbation value lists must be deterministic and declared explicitly in each family-specific artifact because the source note names the perturbation axes but does not prescribe canonical magnitudes.
- Next step: Create `results/perturbation_cd_rotation.csv` as the first family-specific perturbation result artifact using the `omega_CD` family and the fixed reference sweep.

### Entry 12

- Objective: Create the first family-specific perturbation result artifact for the nonzero-`omega_CD` rotation family.
- Work performed: Created `results/perturbation_cd_rotation.csv` using the fixed seven-point `omega / omega_0` reference sweep from `results/special_case_threshold.csv` as the zero-perturbation control; declared the deterministic nonzero ladder `omega_CD / omega in {0.25, 0.5, 0.75, 1.0}`; wrote one row for every sweep value at each ladder value; preserved the control-row `gliding_contact_occurs` results from the special case; marked every nonzero `omega_CD` row as `ambiguous`; left `tau_contact` blank for every row; and promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/results/perturbation_cd_rotation.csv`.
- Files changed: `results/perturbation_cd_rotation.csv`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 5 now has its first family-specific result file in the canonical repository. The artifact fixes a single comparison matrix for the `omega_CD` family, keeps the special-case control rows inspectable, and records the current source-boundary explicitly instead of inventing a nonzero-rotation gliding law.
- Decisions: Nonzero `omega_CD` rows are recorded as `ambiguous`, not `yes` or `no`, because the current source set does not provide a family-specific re-encounter/contact law that would justify a deterministic persistence or disappearance claim. The result file therefore advances Workstream E as a bounded status artifact, not as evidence that the CD-rotation family already generalizes or fails.
- Next step: Create `figures/perturbation_cd_rotation.png` from the fixed result matrix and keep the plotted claim limited to the control-versus-ambiguous status structure.

### Entry 13

- Objective: Create the first family-specific perturbation figure for the `omega_CD` rotation family.
- Work performed: Added `scripts/plot_perturbation_cd_rotation.py` as a narrow deterministic renderer for `results/perturbation_cd_rotation.csv`; generated `figures/perturbation_cd_rotation.png` as a categorical status matrix over the fixed `omega / omega_0` sweep and the declared `omega_CD / omega` ladder; marked the special-case threshold at `omega / omega_0 = 1`; encoded the zero-rotation control row as `N/N/N/N/Y/Y/Y`; encoded every nonzero `omega_CD` row as `A`; visually checked the rendered PNG in the worktree; and promoted the same script and figure into `/Users/velocityworks/IdeaProjects/research/arjen_theories`.
- Files changed: `scripts/plot_perturbation_cd_rotation.py`, `figures/perturbation_cd_rotation.png`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 5 now has its first family-specific result-and-figure pair in the canonical repository. The new figure makes the control-row threshold transition inspectable while preserving the exact current source boundary that nonzero `omega_CD` rows remain ambiguous rather than establishing persistence or disappearance.
- Decisions: The figure is a bounded status artifact, not a duration or generalization claim. The renderer fails explicitly if a future `omega_CD` matrix stops matching the current contract that nonzero rows remain `ambiguous`.
- Next step: Create `results/perturbation_plane_tilt.csv` with the same seven-point reference sweep and one explicitly declared deterministic nonzero `plane_tilt` ladder.

### Entry 14

- Objective: Create the next family-specific perturbation result artifact for the plane-tilt family.
- Work performed: Created `results/perturbation_plane_tilt.csv` using the fixed seven-point `omega / omega_0` reference sweep from `results/special_case_threshold.csv` as the zero-tilt control; declared the deterministic nonzero ladder `plane_tilt_degrees in {15, 30, 45, 60}`; wrote one row for every sweep value at each ladder value; preserved the control-row `gliding_contact_occurs` results from the special case; marked every nonzero `plane_tilt` row as `ambiguous`; left `tau_contact` blank for every row; validated the resulting 35-row matrix against the expected sweep and status contract; and promoted the same file into `/Users/velocityworks/IdeaProjects/research/arjen_theories/results/perturbation_plane_tilt.csv`.
- Files changed: `results/perturbation_plane_tilt.csv`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 5 now has its second family-specific result artifact in the canonical repository. The plane-tilt matrix fixes a single comparison dataset with inspectable zero-tilt control rows and a declared nonzero tilt ladder while keeping the current source boundary explicit for every perturbed row.
- Decisions: Nonzero `plane_tilt` rows are recorded as `ambiguous`, not `yes` or `no`, because the current source set does not provide a family-specific re-encounter/contact law that would justify a deterministic persistence or disappearance claim. The artifact therefore advances Workstream E as a bounded status matrix, not as evidence that the plane-tilt family already generalizes or fails.
- Next step: Create `figures/perturbation_plane_tilt.png` from the fixed result matrix and keep the plotted claim limited to the control-versus-ambiguous status structure.

### Entry 15

- Objective: Close the plane-tilt family and complete the contact-offset family without widening the Milestone 5 claim surface.
- Work performed: Added `scripts/plot_perturbation_plane_tilt.py` as a narrow deterministic renderer for `results/perturbation_plane_tilt.csv`; generated `figures/perturbation_plane_tilt.png` as a categorical status matrix over the fixed `omega / omega_0` sweep and the declared `plane_tilt_degrees` ladder; created `results/perturbation_contact_offset.csv` using the same seven-point control sweep with the deterministic nonzero ladder `contact_offset in {0.2, 0.4, 0.6, 0.8}`; added `scripts/plot_perturbation_contact_offset.py` as the matching renderer; generated `figures/perturbation_contact_offset.png`; visually checked both rendered PNGs in the worktree; and promoted the same files into `/Users/velocityworks/IdeaProjects/research/arjen_theories`.
- Files changed: `scripts/plot_perturbation_plane_tilt.py`, `figures/perturbation_plane_tilt.png`, `results/perturbation_contact_offset.csv`, `scripts/plot_perturbation_contact_offset.py`, `figures/perturbation_contact_offset.png`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 5 now has closed result-and-figure pairs for the `omega_CD`, `plane_tilt`, and `contact_offset` families. The new artifacts keep the special-case control transition inspectable, mark the threshold at `omega / omega_0 = 1`, and preserve the exact current source boundary that every nonzero `plane_tilt` and nonzero `contact_offset` row remains `ambiguous`.
- Decisions: The contact-offset artifact uses a deterministic interior ladder rather than the extremity limit so the family remains a bounded one-at-a-time perturbation matrix instead of folding in an endpoint singular case. Both new renderers fail explicitly if a future matrix violates the present contract that nonzero family rows stay `ambiguous`.
- Next step: Create `results/perturbation_approach_angle.csv` and `figures/perturbation_approach_angle.png` so the last pending perturbation family is fixed before writing `generalization_assessment.md`.

### Entry 16

- Objective: Close the final pending Milestone 5 perturbation family by completing the bounded `approach_angle` artifact set.
- Work performed: Created `results/perturbation_approach_angle.csv` using the fixed seven-point `omega / omega_0` reference sweep as the perpendicular-approach control; declared the deterministic nonzero ladder `approach_angle_degrees in {15, 30, 45, 60}`; preserved the special-case control-row `gliding_contact_occurs` pattern `N/N/N/N/Y/Y/Y`; marked every nonzero `approach_angle` row as `ambiguous`; added `scripts/plot_perturbation_approach_angle.py` as the matching deterministic renderer; generated `figures/perturbation_approach_angle.png`; visually checked the rendered PNG in the worktree; and promoted the same files into `/Users/velocityworks/IdeaProjects/research/arjen_theories`.
- Files changed: `results/perturbation_approach_angle.csv`, `scripts/plot_perturbation_approach_angle.py`, `figures/perturbation_approach_angle.png`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: Milestone 5 now has a closed result-and-figure pair for the final required perturbation family. The repository holds fixed, inspectable artifacts for all four one-at-a-time perturbation families while keeping the current source boundary explicit that every nonzero `approach_angle` row remains `ambiguous`.
- Decisions: The approach-angle family uses the same four-step angle ladder as the plane-tilt family so the nonzero obliquity scan remains deterministic and easy to compare across artifacts. The new renderer fails explicitly if a future matrix violates the present contract that nonzero `approach_angle` rows stay `ambiguous`.
- Next step: Write `generalization_assessment.md` from the four closed perturbation family artifacts and keep the conclusion bounded to persistence-versus-ambiguity labels supported by the current source set.

### Entry 17

- Objective: Wrap the repository around a final bounded conclusion instead of leaving the Milestone 5 stop decision implicit.
- Work performed: Created `generalization_assessment.md` from the four closed perturbation families using only the labels permitted by `methods/perturbation_tests.md`; created `interpretation_limits.md` to fix the exact boundary on supported language, ensemble claims, and reopening conditions; created `technical_note.md` as the final integrated note grounded in `dijksman_rvm_revised.md`, the derivation, the deterministic special-case instrument, the special-case evidence package, and the perturbation artifacts; and updated `PROJECT_STATUS.md` plus `automation/AUTOMATION_MEMORY.md` to mark the project as wrapped and closed at the present source-boundary support level.
- Files changed: `generalization_assessment.md`, `interpretation_limits.md`, `technical_note.md`, `PROJECT_STATUS.md`, `automation/AUTOMATION_MEMORY.md`, `automation/WORK_LOG.md`
- Results: The repository now reads as finished. It states the strongest surviving claim plainly: the constrained special-case threshold mechanism is supported, while every tested nonzero perturbation family remains `ambiguous`, so no ensemble or mass-like continuation is justified from the present source set.
- Decisions: Milestone 6 is treated as a stop decision rather than an unfinished experiment block because Milestone 5 did not justify continuation to the ensemble layer. Future work, if any, must begin with a new post-recollision derivation rather than another interpretive or presentation pass.
- Next step: None for the current source set.
