Perform final verification for task <TASK_ID>, change <CHANGE>.

Use verification-before-completion. Read the specification and tasks.md, inspect repository state and confirm a separate review exists. Ensure blocking findings are resolved and review/check results apply to the final state.

Run required quality gates from docs/quality.md. Check lint, static analysis, tests, build and the final SonarQube Quality Gate status. Do not replace missing evidence with an assumption of success.

Verify startup through the only compose.yaml. For storage tasks, verify that a test photo and its metadata survive app-container recreation. Use isolated test data. Do not delete user volumes.

Provide a table: requirement -> implementation -> verification -> result. Include a short manual acceptance scenario. Identify unrun checks and limitations. A failed or unrun mandatory gate leaves the task incomplete.

If acceptance is already explicitly complete and archiving is authorized, use openspec-archive-change and synchronize the main specifications. Otherwise, prepare the result for acceptance and leave the change active. Do not request consent that was already given.

After archiving, check that specifications, tasks and the decision log are current, and validate OpenSpec documents. Prepare a concise change description. Commit, push and merge only within the scope explicitly authorized by the user.
