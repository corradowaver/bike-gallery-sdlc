# PRE-SETUP-001: Git ignore rules before project setup

OpenSpec change: add-gitignore (previously setup-project).

This is the task's only decision log. Superseded decisions are retained below.

## D1: Distribute ignore rules

- Date: 2026-11-17
- Related requirements: PRE-SETUP-001-R1 through R4
- Context: The user requested separate root, frontend and backend ignore files for PRE-SETUP-001.
- Alternatives considered: One root file; three files with duplicates; shared root rules plus module-specific rules.
- Decision: Use shared root rules and module-specific files with generated directories anchored to the module root.
- Rationale: Matches the requested layout without duplicating common rules or ignoring unrelated source paths.
- Consequences: Keep .env.example, lockfiles and Maven Wrapper trackable. Define future storage paths during SETUP-001.
- Status: accepted.

## D2: Isolated behavior verification

- Date: 2026-11-17
- Related requirements: PRE-SETUP-001-R1 through R5
- Context: The application and build commands do not exist yet.
- Alternatives considered: Create fixtures in the working tree; test only positive examples; use a temporary repository with positive and negative examples.
- Decision: Use a temporary Git repository with external ignore rules disabled and verify every example.
- Rationale: Detect both missing exclusions and accidentally hidden source without touching user data or the index.
- Consequences: This does not verify application runtime. The initial report marked application checks NOT RUN; D6 clarifies their applicability for this task.
- Status: accepted; applicability reporting clarified by D6.

## D3: Initial change naming and specification scope

- Date: 2026-11-17
- Related requirements: PRE-SETUP-001-R1 through R5
- Context: The user originally clarified the task ID to PRE-SETUP-001 while keeping setup-project as the change name, which README also used for full SETUP-001.
- Alternatives considered: Expand scope to full setup; rename the change; preserve the requested name and narrow scope.
- Decision: Initially retain setup-project and use skip_specs: true, with tooling requirements and scenarios in design.md.
- Rationale: Followed the original naming request and the schema's tooling-only path.
- Consequences: This name would conflict with the future setup task. Planning did not constitute acceptance.
- Status: naming superseded by D5; tooling-only specification scope retained.

## D4: Reproducible verification artifact

- Date: 2026-11-17
- Related requirements: PRE-SETUP-001-R1 through R5
- Alternatives considered: Keep only one-off command history; retain a standalone checker with the change.
- Decision: Keep verify_gitignore.py and verification.md in the change, referencing requirement IDs.
- Rationale: Enables independent reproduction of the positive and negative Git behavior checks without application infrastructure.
- Consequences: Requires Python 3.10+ and Git. The original fixed-parent root discovery was found unsuitable for archiving; D5 corrects it.
- Status: accepted with the correction in D5.

## D5: Review corrections and stable root discovery

- Date: 2026-11-17
- Related requirements: PRE-SETUP-001-R5
- Context: A separate review found the naming conflict, fixed-depth root discovery and Russian artifacts. The user authorized fixing these findings.
- Alternatives considered: Keep the ambiguous name; change the hard-coded parent count after archiving; discover the project using stable configuration markers.
- Decision: Rename the change to add-gitignore, preserve all requirement IDs, discover the nearest ancestor OpenSpec configuration, translate task artifacts and require English repository artifacts in AGENTS.md.
- Rationale: Leaves setup-project available for SETUP-001 and keeps checks runnable at active and archived depths without relying on the current directory.
- Consequences: Update command references and add regression checks. Respond to users in their preferred language. Final acceptance remains separate from these corrections.
- Status: accepted.

## D6: Scope-based quality gates

- Date: 2026-11-17
- Related requirements: PRE-SETUP-001-R5
- Context: Unconditional application gates would block a narrow ignore-rule task before the application exists.
- Alternatives considered: Require every future tool; silently skip checks; explicitly classify applicability by changed scope.
- Decision: Apply Git behavior, checker regressions, document/OpenSpec consistency, whitespace and separate review to this task. Mark unrelated application/SonarQube/Compose checks NOT APPLICABLE with reasons.
- Rationale: Preserve meaningful verification without pretending unrelated checks passed.
- Consequences: Required but unavailable checks remain NOT RUN and blocking. Configuration changes affecting builds, deployment or analyzers must run their affected checks. SETUP-001 remains responsible for establishing its promised tooling.
- Status: accepted.
