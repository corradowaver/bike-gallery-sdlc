# Proposal

Task: PRE-SETUP-001

## Why

The repository needs Git ignore rules before application setup. Exclude local settings, dependencies and generated output while retaining source files and reproducible build configuration.

## What Changes

- Add root, frontend and backend .gitignore files with shared and module-specific rules.
- Preserve .env.example, lockfiles, Maven Wrapper, source files, test resources and documentation.
- Verify positive and negative examples in an isolated temporary Git repository.
- Maintain one decision log: docs/decisions/PRE-SETUP-001.md.
- Make verification work at both active and archived change locations.
- Require English repository artifacts and clarify scope-based quality gates following review.

This is the narrow preparatory task PRE-SETUP-001. Full Java/Vue, storage, Compose, CI and analyzer setup remains SETUP-001. The change is now named add-gitignore, leaving setup-project available for SETUP-001.

## Capabilities

### New Capabilities

None. Only development tooling and workflow documentation change; application behavior does not. Use skip_specs: true. Requirements and acceptance scenarios PRE-SETUP-001-R1 through R5 are defined in design.md.

### Modified Capabilities

None. Main application specifications do not exist yet.

## Impact

Three .gitignore files, this change's planning and verification artifacts, one decision log, and the language/applicability rules in AGENTS.md and docs/quality.md. No API changes or application dependencies. Verification requires Python 3.10+ and Git. Ignore rules do not remove tracked files or user data.
