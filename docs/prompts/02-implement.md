Implement agreed task <TASK_ID>, OpenSpec change <CHANGE>, using openspec-apply-change.

Read applicable AGENTS.md files, the change, relevant main specifications, docs/architecture.md and docs/quality.md. Confirm that the plan is agreed and blocking questions are resolved.

Independently implement the scope, run local checks and fix issues. Do not stop to request repeated permission for routine, already-authorized actions. Discuss product behavior outside the agreed specification before implementing it.

Follow one top-level Java type per file, Clean Code, SOLID, DRY and the concrete architecture boundaries in AGENTS.md. Do not add speculative abstractions.

Reference requirement IDs in comments near the implementing logic and in tests. Maintain tasks.md and the sole docs/decisions/<TASK_ID>.md file. Preserve IDs and do not weaken requirements to make tests pass.

Keep exactly one root compose.yaml. Use one application build and environment-variable configuration. Do not create prod/dev/test/override files. Do not delete user volumes.

Run checks from docs/quality.md, including SonarQube analysis and waiting for its Quality Gate when configured and reachable. Verify the user flow through Compose with test data. If a required check cannot run, mark it NOT RUN and explain why; the required gate remains incomplete.

Use verification-before-completion. Finish with a requirement-to-implementation-to-verification mapping, commands and actual results, limitations and the verified code state. Do not claim final task closure before separate review and acceptance. Do not archive the change at this stage.
