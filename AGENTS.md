# Repository Instructions

- Scripts in this repository must run successfully with no command-line arguments.
- No-argument execution should use deterministic, sensible defaults that produce a meaningful representative output instead of a usage error.
- If a task cannot be represented with sensible no-argument defaults, do not add it as a standalone script in this repository.
- Keep explicit CLI overrides for all defaults so the script remains usable for the exact experiment.
- Each automation run must commit its repository changes before ending.
- Automation-run commits should stage only the files changed in that run and use a detailed commit message that names the artifact or task completed, the substantive files touched, the main result, and any explicit limitation or blocker that remains.
