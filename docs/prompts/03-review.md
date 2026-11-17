Act as the separate reviewer for task <TASK_ID>, OpenSpec change <CHANGE>.

Comparison base: <BASE_SHA>. Reviewed version: <HEAD_SHA>. Include additional uncommitted changes only when explicitly requested, and identify the exact state reviewed.

Read applicable AGENTS.md files, the specification, the task's sole decision log, docs/architecture.md, docs/quality.md and the diff. Independently verify implementation rather than relying on the implementation agent's conclusions.

Check:
- requirements and negative scenarios;
- storage correctness, error handling and the HTTP contract;
- one top-level Java type per file, clear responsibilities, appropriate abstractions and no duplicated business rules;
- Clean Architecture boundaries and architecture tests;
- whether requirement-ID comments match actual logic and tests;
- whether quality gates were weakened or unjustified exclusions/suppressions were introduced;
- the single compose.yaml, persistent data and reproducible startup;
- verification and SonarQube results for the exact version under review.

Do not edit source code or configuration. You may run checks with isolated test data. Do not fix findings during review.

For each finding, give severity, file and line, consequences, a reproduction scenario and the requirement ID if applicable. Separate defects from optional suggestions. Do not require refactoring solely because of personal preference.

If there are no findings, say so and explain the review limits. List checks run and not run. Conclude whether the task is ready for acceptance or needs fixes.
