# Quality policy

## Gate 1: ready for implementation

- Scope and acceptance criteria are agreed.
- An OpenSpec change and stable requirement IDs exist.
- Requirements include observable scenarios and meaningful failure cases.
- An API contract is defined when the task changes the API.
- Exactly one decision log exists for the task.
- The specification passes openspec validate and has no blocking open questions.

## Gate 2: ready for review

- Implementation and tests reference requirement IDs.
- Checkstyle, SpotBugs, ESLint, formatting checks and vue-tsc pass.
- Unit, integration and architecture tests pass.
- Implemented end-to-end scenarios pass.
- Backend and frontend build successfully; the Compose configuration is valid.
- SonarQube analysis has completed and its Quality Gate has passed. Successfully submitting a report is insufficient.

## SonarQube

During SETUP-001, pin the SonarQube edition and version, select Java and TypeScript Quality Profiles, define New Code and establish how CI receives analysis results. Do not promise PR or branch analysis without checking the selected edition's capabilities.

Proposed target conditions for new code:

- no new issues under the agreed profile;
- all new Security Hotspots reviewed with justification;
- coverage of at least 80%;
- duplication of at most 3%.

These are project targets, not a claim that every SonarQube edition has identical defaults. Check condition availability, behavior on small changes and exemptions. Explain differences between the target and actual gate before accepting the setup.

Coverage is not proof of correctness. Mandatory specification scenarios must be tested regardless of the percentage. Generate JaCoCo XML and frontend LCOV reports through tests and provide them to the analyzer. Do not hide missing reports by excluding code.

False positives and exceptions require justification and review. Do not bulk-mark findings as safe or exclude code simply to pass the gate.

## Gate 3: ready for completion

- A separate review is complete and blocking findings are resolved.
- Verification applies to the final version. After changes, rerun affected checks; before closing, execute the complete required gate.
- Verify the user scenario through the single Compose deployment.
- For storage changes, verify test-data persistence after container recreation.
- Acceptance is complete through the user or previously agreed objective acceptance criteria.
- Specifications, tasks.md and the decision log are current.

## Verification setup in SETUP-001

Configure the following and replace this section with actually verified commands:

- Maven Wrapper verify, including Checkstyle, SpotBugs, JUnit, integration tests and ArchUnit.
- npm scripts: lint, format:check, type-check, test:unit, build and test:e2e.
- scripts/verify.ps1 as a single verification entry point that returns a nonzero exit code on failure. It must not hide partial execution or succeed after skipping a mandatory gate.
- CI uses the same commands, waits for the final SonarQube Quality Gate status and identifies the analyzed commit.
- docker compose config --quiet, image build and application startup using the root compose.yaml.

Fast checks may run separately during development. The final report must identify what actually ran. Network failures, missing tokens and an unavailable SonarQube instance mean NOT RUN or FAIL, not PASS.

Do not create a separate test Compose file. Isolated acceptance may use a different Compose project name with the same file, separate volumes and an available port configured through an environment variable.
