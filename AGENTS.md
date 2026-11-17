# Bike Gallery

## Product

A local, single-user photo diary of bicycle trips. MVP: upload one photo, browse the gallery, view a photo and delete it. Additional features require a separate task.

Stack: Java 21, Spring Boot and Maven Wrapper; Vue 3, TypeScript and Vite; file-based H2; local persistent image storage. Pin compatible versions during project setup.

## Specification-driven workflow

- Write repository documentation, OpenSpec artifacts, decision logs, code comments and commit messages in English. Respond to the user in their preferred language.

- Before implementation, read the relevant OpenSpec specifications and change. Agree on a new feature's plan before changing behavior.
- Every task has an ID, such as PHOTO-001. Requirements have stable IDs, such as PHOTO-001-R1. Do not renumber accepted IDs when reordering documents.
- Represent one user-visible outcome as one OpenSpec change, including backend, frontend and verification tasks as needed.
- Reference requirement IDs in comments near the implementing logic and in the corresponding tests. Place references at meaningful block, method or test boundaries, not on every line or unrelated infrastructure code.
- Update the specification when agreed behavior changes. Do not weaken requirements to justify a faulty implementation.
- Keep tasks.md current. Mark a checklist item complete only after its corresponding verification is complete.

## Decision log

- Keep exactly one file per task: docs/decisions/<TASK_ID>.md. Use TEMPLATE.md.
- Append decisions during the task. A new chat, commit, subtask or agent does not require another decision log.
- Record meaningful alternatives, the selected option, reasons, consequences and related requirement IDs.
- design.md describes the current design; the decision log explains why choices were made or revised. Do not duplicate entire documents.

## Code quality

- Use descriptive names, cohesive functions and classes with a clear responsibility.
- Apply SOLID through clear responsibilities and dependency boundaries.
- Apply DRY to duplicated business rules and knowledge. Do not merge unrelated concepts merely because their code looks similar.
- Prefer the simplest design that satisfies current requirements. Do not add interfaces, factories or generalized mechanisms without a concrete need.
- Handle errors explicitly. Do not swallow exceptions or report false success.
- Read docs/architecture.md before changing module boundaries. Follow applicable nested AGENTS.md files.
- Keep unrelated refactoring out of feature tasks.

## Quality gates and review

- Follow docs/quality.md. After SETUP-001, use the verified commands documented there.
- Run relevant tests, analyzers and builds. Before closing a task, execute the complete required gate against the final version.
- Do not disable analyzers, lower thresholds, add exclusions or suppress findings merely to pass checks. Justified exceptions require a decision-log entry and review.
- Use verification-before-completion before claiming completion. If the skill is unavailable, disclose that and still provide the results of checks actually performed.
- Distinguish PASS, FAIL, NOT RUN and NOT APPLICABLE. Apply the scope rules in docs/quality.md. An unavailable required analysis service is NOT RUN, never NOT APPLICABLE or PASS.
- Require a separate review. Self-review by the implementation agent does not replace it.
- Archive a change only after blocking findings are resolved and acceptance is complete. OpenSpec document validation does not prove application correctness.

## Running and deploying

- The only Compose file is compose.yaml at the repository root.
- Do not create separate dev/prod/test Compose files, compose.override.yaml or additional files to combine with -f.
- Name the main service app. The intended startup command is docker compose up --build -d.
- Use one reproducible application build. Build Vue during image creation and serve its static assets through Spring Boot.
- Express configuration differences through environment variables. Document them in .env.example; never commit .env or secrets.
- Store the database and photos in persistent named volumes. Data must survive container recreation and ordinary docker compose down/up.
- Do not use docker compose down -v for normal shutdown or verification of a user's environment.
- If local SonarQube and its database are needed, define them in the same compose.yaml. A quality profile may enable auxiliary tooling. Do not define different dev/prod implementations of app through profiles.
- Pin selected image and dependency versions. Do not use latest in the final configuration.
- Bind the local, single-user MVP to loopback by default. Public deployment is a separate task.
- Direct Maven/Vite commands are allowed for fast development and diagnostics. Acceptance must use the single Compose deployment.

## Autonomy and communication

- Independently implement the agreed scope, run local checks and fix issues within the task.
- Ask about blocking product decisions. Do not repeatedly request permission for already-authorized routine work.
- Never delete user data to run tests. Use temporary files and isolated test storage.
- Report requirements covered, changes made, verification commands and results, outstanding findings and limitations.

## Project commands

Not configured yet. During SETUP-001, replace this section with verified commands and a reference to docs/quality.md. Do not claim scripts exist before creating and running them.
