# Scheduled Task Prompt

Use the following prompt for the Codex Automations task:

```text
Advance the research in this project by completing one bounded milestone slice from the plan.

At the start of the run:
1. Read `automation/AUTOMATION_MEMORY.md`.
2. Read `RESEARCH_PLAN.md`.
3. Inspect `git status --short` and treat that output as the baseline for commit scope.
4. Inspect `git -C /Users/velocityworks/IdeaProjects/arjen_theories status --short`.
5. Treat `/Users/velocityworks/IdeaProjects/arjen_theories` as the canonical destination for repository files.
6. If the current milestone already has unfinished artifact work in the worktree, continue it before choosing a new task.
7. Identify the highest-priority missing canonical artifact family or decision package required by the current milestone.
8. Read only the additional files needed to close that slice.

During the run:
- Use `dijksman_rvm_revised.md` as the ground-truth theory document.
- Do not widen the project scope beyond that document.
- Treat one concrete task as one bounded milestone slice, not one file.
- When multiple tightly coupled files are required to make a slice usable and inspectable, complete them in the same run.
- Prefer closing a whole perturbation family in one run when the work is source-bounded, for example result CSV + rendering script + figure.
- Do not split a producer artifact and its immediately dependent figure or companion file across separate runs if both can be completed from the same source-bounded context without new theory.
- If the remaining milestone work is mostly mechanical artifact completion rather than new derivation, batch the next 2-4 tightly coupled missing files into one run when that closes a clearer gate.
- Only stop after a single file if the dependent files are blocked by missing source support, would require new derivation, or would create a commit-scope conflict.
- Keep all code and methods deterministic, narrow, and auditable.
- If blocked on the best next task, document the blocker and complete the best unblocked supporting task instead.
- If the highest-priority missing artifact family can be advanced, advance that family slice and do not spend the run on summaries, comparisons, progress estimates, or memory-only maintenance.
- Memory updates, work-log updates, and explanatory summaries do not count as the one concrete task.
- Do not choose a communication or cleanup task while a milestone-gating artifact is still missing and unblocked.
- For Milestone 3, the canonical targets are `scripts/special_case_experiment.py` and `methods/special_case_experiment.md`. `demo.py` is not a milestone artifact.
- If the current active task is code or methods, produce or modify every canonical file needed to make that slice inspectable in the run. Do not end with only notes about what should be built next.
- Any repository file created or modified in the worktree must also be created or modified at the same relative path under `/Users/velocityworks/IdeaProjects/arjen_theories` before the run ends.
- If the run changes repository files, create a commit before ending.
- Stage only files changed during the current run. Do not include unrelated pre-existing changes in the automation commit.
- If a required touched file already had unrelated uncommitted changes before the run and commit scope cannot be kept clean, stop and report a commit-scope conflict instead of mixing authorship.
- Use a detailed commit message that names the completed task, the main files changed, the substantive result, and any explicit remaining blocker or limit.

Before ending the run:
1. Update `automation/AUTOMATION_MEMORY.md` with current status, blockers, and next recommended action.
2. Append a dated entry to `automation/WORK_LOG.md` describing what was done, which files changed, what results were produced, and what should happen next.
3. If repository files changed, create the detailed commit before ending the run.
4. Verify the promoted changes with `git -C /Users/velocityworks/IdeaProjects/arjen_theories status --short`.
5. Briefly summarize the completed work and the commit in the final response.
```

## Notes

- Keep the automation prompt short. Durable project instructions should live in repository files, not only in the scheduler UI.
- The automation should treat `automation/AUTOMATION_MEMORY.md` as the control file and `automation/WORK_LOG.md` as the append-only session diary.
