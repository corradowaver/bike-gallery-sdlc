Plan task <TASK_ID>, OpenSpec change <CHANGE>.

User-visible outcome: <describe one feature or setup outcome>.

Read applicable AGENTS.md files, docs/product.md if present, relevant specifications, docs/architecture.md and docs/quality.md. Inspect the current project state first so you do not plan work that already exists. If product.md is absent, capture the agreed product scope there before finalizing the plan.

Use grill-me or grill-me-with-docs for critical questioning only if the skills are available and appropriate. If they are missing, disclose that and clarify requirements through an ordinary discussion. Do not present another skill as either of these.

Use openspec-propose. Define scope, stable requirement IDs <TASK_ID>-R*, positive and negative scenarios, the API contract where relevant and acceptance criteria. The technical plan must follow the architecture and single-compose.yaml policy. Do not add separate Compose files for tests or environments.

Create or update the sole docs/decisions/<TASK_ID>.md file. Include required backend/frontend implementation, verification, separate review and completion in tasks.md. Propose behavior checks rather than tests that merely mirror implementation details.

For SETUP-001 / setup-project, cover the runnable Java/Spring and Vue foundation, persistent storage, multi-stage app image, the single Compose deployment, static analyzers, tests, SonarQube, verification scripts, CI and verified run instructions. Preserve existing OpenSpec configuration. Verify tool compatibility and skill availability; report missing prerequisites honestly.

Validate the change using OpenSpec. Do not change application code yet. Present the proposal and any blocking questions for agreement.
