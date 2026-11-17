# Tasks

Task: PRE-SETUP-001. Requirements and examples: design.md, R1-R5. Mark items complete only after implementation and corresponding verification.

## 1. Shared rules

- [x] 1.1 Create root .gitignore for R1; verify positive examples and all three .env.example exceptions using R5.

## 2. Module rules

- [x] 2.1 Create frontend/.gitignore for R2; verify positive and protective examples using R5.
- [x] 2.2 Create backend/.gitignore for R3; verify positive and protective examples and Maven Wrapper preservation using R5.

## 3. Verification and acceptance

- [x] 3.1 Verify all 46 R1-R4 cases together in an isolated Git repository and record actual results.
- [x] 3.2 Complete separate review of the final files and verification matrix; identify the reviewed version and resolve blocking findings. Review fixes require follow-up verification/review.
- [x] 3.3 Repeat the applicable final gate, run openspec validate add-gitignore --strict, check the diff and record acceptance before archiving.

## 4. Review follow-up

- [x] 4.1 Replace fixed-depth project-root discovery and verify active, archived and missing-root scenarios under R5.
- [x] 4.2 Translate task artifacts to English, establish the repository language rule, and rename the change to add-gitignore while preserving requirement IDs and decision history.
- [x] 4.3 Clarify scope-based quality gates without exempting affected build, deployment or analyzer changes; refresh verification evidence.
