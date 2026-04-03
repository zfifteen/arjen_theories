# Automation Memory

## Mission

Advance this project toward a professional, research-grade technical note grounded in `dijksman_rvm_revised.md`.

## Canonical Sources

- Ground-truth theory note: `dijksman_rvm_revised.md`
- Canonical roadmap: `RESEARCH_PLAN.md`

## Operating Rules

- Read this file first on every automated run.
- Read `RESEARCH_PLAN.md` second on every automated run.
- Do not widen the claim surface beyond `dijksman_rvm_revised.md`.
- Choose one bounded milestone slice from `RESEARCH_PLAN.md` that meaningfully advances the project.
- Prefer a small finished unit of work over broad partial work.
- Treat code as a research instrument: deterministic, narrow, auditable.
- Update this file and `automation/WORK_LOG.md` before ending every run.
- If blocked on the best next task, document the blocker here and complete the best unblocked supporting task instead.

## Operational Guardrails

- At the start of each run, identify the highest-priority missing artifact for the current milestone before doing any other work.
- Inspect `git status --short` at the start of each run and continue unfinished work on the current milestone before selecting a new task.
- Treat the start-of-run `git status --short` output as the baseline for commit scope.
- Treat one concrete task as one bounded milestone slice, not one file.
- When multiple tightly coupled files are required to make that slice usable and inspectable, complete them in the same run.
- Do not split a producer artifact and its directly dependent figure or companion file across separate runs if both can be completed from the same source-bounded context without new theory.
- If the remaining milestone work is mostly mechanical artifact completion, batch the next 2-4 tightly coupled missing files into one run when that closes a clearer gate.
- Only stop after a single file if the dependent files are blocked by missing source support, would require new derivation, or would create a commit-scope conflict.
- If that artifact can be advanced, advance it in the run. Do not spend the run on summaries, comparisons, progress estimates, or memory-only maintenance.
- Updating memory, work logs, or explanatory notes does not count as the completed task for the run.
- Do not choose a communication task or cleanup task while a milestone-gating artifact is still missing and unblocked.
- Only mark a task as blocked if the missing information is absent from `dijksman_rvm_revised.md`, `claims.md`, `definitions.md`, and the current repository artifact set.
- A successful run should leave at least one milestone-relevant artifact newly created or materially advanced.
- If the run changes repository files, create a commit before ending.
- Stage only files changed during the current run. Do not sweep unrelated pre-existing changes into the automation commit.
- If a required touched file already had unrelated uncommitted changes before the run and commit scope cannot be kept clean, stop and report a commit-scope conflict instead of mixing authorship.
- Use a detailed commit message that names the completed task, the main files changed, the substantive result, and any explicit remaining blocker or limit.

## Canonical Milestone Targets

### Milestone 3

- Primary code artifact: `scripts/special_case_experiment.py`
- Primary methods artifact: `methods/special_case_experiment.md`
- `demo.py` is not a milestone artifact and should not be extended as if it were the research instrument. It may be read for salvage only.

## Canonical Destination

- The canonical destination for repository files is `/Users/velocityworks/IdeaProjects/arjen_theories`.
- The worktree is scratch only. Any repository file created or modified during an automated run must also be created or modified at the same relative path under the canonical destination before closeout.
- Before closeout, verify the visible repo result with `git -C /Users/velocityworks/IdeaProjects/arjen_theories status --short`.

## Current Status

- Progress toward project goal: The repository is wrapped at a professional, research-grade stopping point. It now contains the bounded claim contract, the explicit special-case derivation, the deterministic special-case instrument, the fixed special-case evidence package, the full one-at-a-time perturbation artifact set, the generalization decision, the interpretation-limit note, and the final technical note.
- Current milestone: Project closed
- Active workstream: none
- Last run delivered value: Added `generalization_assessment.md`, `interpretation_limits.md`, and `technical_note.md`, then updated `PROJECT_STATUS.md` so the repo states its final conclusion and stopping rule explicitly.
- Active task: none
- Last completed: Wrapped the project around the constrained special-case result and the explicit Milestone 5 stop decision
- Known blockers: A closed-form law for `tau_contact` remains blocked because `dijksman_rvm_revised.md` does not specify the post-recollision contact constraint needed for the gliding phase. For nonzero `omega_CD`, nonzero `plane_tilt`, nonzero `contact_offset`, and nonzero `approach_angle`, the current source set also lacks a family-specific re-encounter/contact law, so those rows remain `ambiguous`.

## Priority Queue

1. None. Reopen only if new source support adds a family-specific post-recollision contact law.

## Next Recommended Action

No further repository work is required for the present source set. If the project is reopened, start with a new derivation rather than another interpretation pass.

## Session Close Checklist

- Update `automation/WORK_LOG.md`
- Update the `Current Status` section in this file
- Record any new blocker
- Record the next recommended action
- Ensure any new artifact is aligned with `dijksman_rvm_revised.md`
- If repository files changed, create the detailed run commit before ending and report the commit in the final response
