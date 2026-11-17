# Backend: Java and Spring

- Use one top-level class, interface, enum or record per source file. Nested types are allowed for tightly related local structures; do not use them to combine unrelated responsibilities.
- Prefer constructor injection. Avoid field injection.
- Organize code by feature with explicit domain, application, infrastructure and web boundaries. Do not create empty layers for the sake of folder structure.
- domain must not depend on Spring, JPA, HTTP or filesystem APIs.
- application implements use cases and depends on domain and required ports. It must not depend on web or infrastructure implementations.
- infrastructure implements persistence and external interactions. web maps HTTP requests and responses and invokes application use cases.
- A separate composition root wires ports and implementations using Spring.
- Do not expose JPA entities directly through the API. Use DTOs for the HTTP contract.
- Separate input validation from business invariants. Enforce important invariants in the use case or domain model.
- Use server-generated identifiers for stored filenames. Treat the original filename as metadata, not as a storage path.
- Validate uploaded image content, not just its extension or client-supplied Content-Type.
- Treat database and filesystem operations as separate resources. Do not assume @Transactional rolls back filesystem changes. Specify partial-failure behavior and test it.
- Test observable behavior, including failures. Use temporary directories and an isolated database for storage tests.
- Check architecture dependencies with ArchUnit and one top-level type per file with Checkstyle.
- Obtain concrete limits and behavior from the specification instead of inventing them during implementation.
