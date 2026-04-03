# Automation Folder

This folder contains the control documents for recurring Codex research runs.

## Files

- `AUTOMATION_MEMORY.md`: the session-to-session control file
- `WORK_LOG.md`: append-only diary of completed work
- `SCHEDULED_TASK_PROMPT.md`: ready-to-paste prompt text for the Codex Automations task

## How It Should Be Used

- The scheduled task should read `AUTOMATION_MEMORY.md` first.
- It should read `RESEARCH_PLAN.md` second.
- It should complete one bounded milestone slice per run, not just one file.
- When several tightly coupled files are needed to make that slice usable, it should finish them together in the same run.
- It must update both `AUTOMATION_MEMORY.md` and `WORK_LOG.md` before ending.
