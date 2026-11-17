# Design

Task: PRE-SETUP-001

## Context

See proposal.md for scope. Backend and frontend currently contain instructions but no application or build configuration. Three ignore files implement the preparatory rules. The following stable requirements describe their behavior.

## Goals / Non-Goals

Goals: precise ignores for local/generated files, trackable source and build configuration, isolated verification, and reproducible checks after archiving.

Non-goals: installing application dependencies, implementing the application, setting up Compose/CI/analyzers, or removing tracked files. Git ignore is not a way to remove secrets from history.

## Decisions

Shared rules live at the root; tool-specific rules live in each module. Alternatives and rationale are in the sole decision log at docs/decisions/PRE-SETUP-001.md (repository-relative path).

### PRE-SETUP-001-R1: Shared exclusions

Ignore .env and .env.* at any depth, followed by !.env.example. Ignore .idea/, .vscode/, *.iml, .DS_Store, Thumbs.db and *.log at any depth. Do not blanket-ignore hidden files, images, JARs or arbitrary data/build directories.

### PRE-SETUP-001-R2: Frontend

Ignore /node_modules/, /dist/, /coverage/, /.vite/, /playwright-report/ and /test-results/ anchored at the frontend root, plus *.tsbuildinfo within frontend. Nested source directories with these names must remain trackable unless another explicit rule applies.

### PRE-SETUP-001-R3: Backend

Ignore /target/ anchored at the backend root. Preserve all Maven Wrapper files, including backend/.mvn/wrapper/maven-wrapper.jar. Add further module-specific exclusions only when a concrete need appears.

### PRE-SETUP-001-R4: Preserved files

Do not exclude source files, test resources, build configuration, lockfiles, Maven Wrapper, documentation, OpenSpec or the ignore files themselves. Example paths below need not exist in the working tree.

## Acceptance examples for R1-R4

Each listed path is a separate scenario: WHEN Git evaluates the path with the three project ignore files, THEN its ignored status must match the expected value.

### PRE-SETUP-001-R1

Expected: ignored.

- `.env`
- `frontend/.env.local`
- `backend/.env.test`
- `.idea/workspace.xml`
- `frontend/.vscode/settings.json`
- `backend/service.iml`
- `frontend/.DS_Store`
- `Thumbs.db`
- `backend/app.log`

Expected: trackable (not ignored).

- `.env.example`
- `frontend/.env.example`
- `backend/.env.example`

### PRE-SETUP-001-R2

Expected: ignored.

- `frontend/node_modules/vue/index.js`
- `frontend/dist/index.html`
- `frontend/coverage/lcov.info`
- `frontend/.vite/cache.json`
- `frontend/playwright-report/index.html`
- `frontend/test-results/result.txt`
- `frontend/tsconfig.app.tsbuildinfo`

Expected: trackable (not ignored).

- `frontend/src/dist/example.ts`
- `docs/dist/example.md`

### PRE-SETUP-001-R3

Expected: ignored.

- `backend/target/classes/example/App.class`
- `backend/target/app.jar`
- `backend/target/site/jacoco/jacoco.xml`

Expected: trackable (not ignored).

- `backend/src/test/resources/target/sample.txt`
- `docs/target/example.md`

### PRE-SETUP-001-R4

Expected: trackable (not ignored).

- `.gitignore`
- `frontend/.gitignore`
- `backend/.gitignore`
- `frontend/package.json`
- `frontend/package-lock.json`
- `frontend/vite.config.ts`
- `frontend/src/App.vue`
- `backend/pom.xml`
- `backend/mvnw`
- `backend/mvnw.cmd`
- `backend/.mvn/wrapper/maven-wrapper.properties`
- `backend/.mvn/wrapper/maven-wrapper.jar`
- `backend/src/main/java/example/App.java`
- `backend/src/test/resources/photo.jpg`
- `compose.yaml`
- `Dockerfile`
- `AGENTS.md`
- `docs/quality.md`
- `docs/decisions/PRE-SETUP-001.md`
- `openspec/config.yaml`

### PRE-SETUP-001-R5: Safe, reproducible verification

Copy only the three final ignore files into a temporary Git repository. Disable external Git configuration and excludes, use an empty template, and verify that repository-local excludes have no active rules. Compare every example independently with git check-ignore --no-index -v -z --non-matching --stdin. A matched negation rule means the path is not ignored; a bulk exit code alone is insufficient.

- Success: all positive and protective examples match their expectations, with the matching rule reported when present.
- Failure: missing ignore files, unexpected matches, missing exclusions or Git failures return FAIL. Missing Git reports NOT RUN.
- Root discovery: locate the nearest ancestor containing openspec/config.yaml or config.yml, independently of directory depth and current working directory. Active and archived locations must work; absence of such an ancestor must fail explicitly.
- Do not modify the user's index or create test fixtures in the working tree. Do not use git rm or git clean. Verify temporary cleanup paths.
- Preserve separate review and acceptance before closing the task.

## Risks / Trade-offs

- Overbroad rules hide useful files: test negative examples and anchor generated directories to module roots.
- Personal Git settings affect results: isolate configuration and repository state.
- Future tools generate additional files: update rules during SETUP-001 using actual configuration.
- Archiving changes directory depth: root discovery and regression tests must not assume a fixed parent count.
- Apply docs/quality.md by scope. Application builds, SonarQube and Compose are NOT APPLICABLE to this change, not PASS. An unavailable applicable check is NOT RUN and remains blocking.

## Migration Plan

Apply the three ignore files, verify all examples, perform separate review, and complete acceptance. No application startup or data migration is required. Reverting rules does not require deleting ignored files. Archive only after acceptance; verification must remain runnable from the archived location.
