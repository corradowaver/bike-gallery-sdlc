# Bike Gallery: Codex workflow

Bike Gallery is a local, single-user photo diary of bicycle trips. The MVP covers uploading a photo, browsing the gallery, viewing a photo and deleting it.

This repository currently contains workflow instructions and OpenSpec configuration. Application code, Dockerfile and compose.yaml are to be implemented in SETUP-001.

## Instruction locations

```text
AGENTS.md                          Shared, persistent development instructions
backend/AGENTS.md                  Java and backend architecture rules
frontend/AGENTS.md                 Vue and TypeScript rules
docs/architecture.md               Architecture and deployment boundaries
docs/quality.md                    Quality gates and verification policy
docs/decisions/TEMPLATE.md         Template for one decision log per task
docs/prompts/01-plan.md            Plan a task
docs/prompts/02-implement.md       Implement an agreed change
docs/prompts/03-review.md          Perform a separate review
docs/prompts/04-fix.md             Address review findings
docs/prompts/05-complete.md        Verify and close a task
```

Codex uses applicable AGENTS.md files as persistent instructions. Files in docs/prompts do not run automatically: paste their contents into a chat or explicitly ask Codex to execute the prompt in the file. Architecture and quality documents are referenced by AGENTS.md.

## Working sequence

1. Open this repository as a project in Codex.
2. Use docs/prompts/01-plan.md to plan SETUP-001, change setup-project. Its scope is a runnable backend and frontend, persistent storage, one Compose configuration and working quality gates.
3. Resolve requirements and review the OpenSpec proposal before implementation. Capture agreed MVP behavior in docs/product.md when available.
4. Start implementation with docs/prompts/02-implement.md.
5. In a separate chat, use docs/prompts/03-review.md with the base and reviewed commit SHAs. Explicitly include uncommitted changes if needed.
6. Address findings with docs/prompts/04-fix.md and obtain another review when warranted.
7. Run docs/prompts/05-complete.md. Authorize archiving and committing once acceptance is complete.
8. Repeat the plan, implementation, review and completion cycle for PHOTO-001 and subsequent tasks.

One task means one OpenSpec change and one docs/decisions/<TASK_ID>.md file. Checklist items, commits, agents and new chats do not create additional decision logs.

Replace <TASK_ID>, <CHANGE>, <BASE_SHA>, <HEAD_SHA> and <REVIEW> before using a prompt. The first feature is PHOTO-001 / upload-photo. Skill names in prompts are instructions to Codex, not PowerShell commands.

There is no bootstrap prompt in this set.

## Skills

- OpenSpec is already initialized in this repository. Inspect its existing configuration and project skills before changing the setup.
- Use verification-before-completion when available; report its absence and still provide actual verification evidence.
- Install grill-me and grill-me-with-docs only from supplied, verified sources. Do not create placeholder skills with these names.
- A skill named grilling is a separate skill, not automatically an equivalent replacement. If it is available, identify it accurately and agree on using it as an alternative.
- Requirements can be clarified through an ordinary discussion while the requested skills are unavailable.

## Single Compose deployment

The only orchestration file is compose.yaml at the repository root. After SETUP-001, the intended commands are:

```powershell
docker compose config --quiet
docker compose up --build -d
docker compose ps
docker compose logs --tail 100 app
docker compose down
```

Do not create separate dev, prod, test or override Compose files, or combine multiple files using -f. Configuration differences use environment variables documented in .env.example. Do not commit the actual .env file or secrets.

The app image contains the built Vue frontend served by Spring Boot. Store the database and photos in persistent named volumes. Ordinary shutdown must preserve them.

If SonarQube runs locally, define it and its supporting services in the same compose.yaml. A quality profile may enable auxiliary tooling; it must not represent a separate dev/prod application deployment.

## References

- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenSpec setup](https://openspec.dev/docs/setup)
- [OpenSpec workflow](https://openspec.dev/docs/quickstart)
- [SonarQube standards](https://docs.sonarsource.com/sonarqube-community-build/user-guide/about-new-code)

Prepared on November 17, 2026. Check tool compatibility during setup, then pin the selected versions.
