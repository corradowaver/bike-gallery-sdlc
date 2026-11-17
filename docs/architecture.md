# Bike Gallery architecture

## Initial design for SETUP-001

One repository, one Spring Boot backend and a Vue frontend. The product is local and single-user. Architectural changes belong to a task and its decision log.

The frontend calls an HTTP API. Backend feature packages have these boundaries:

- domain: domain types and invariants without framework dependencies;
- application: use cases and storage ports;
- infrastructure: JPA and filesystem adapters;
- web: controllers and HTTP DTOs;
- configuration: the composition root that wires implementations.

Dependency directions: application -> domain; infrastructure -> application/domain; web -> application and required domain types; configuration wires adapters. Domain does not depend on other layers. Application does not import infrastructure or web. Verify these boundaries with architecture tests.

Introduce interfaces at meaningful boundaries, such as image and metadata storage. Separate HTTP DTOs, domain types and JPA entities where responsibilities differ. Never expose JPA entities directly to clients.

## Storage

Use H2 in file mode. Store photos outside the container image. Configure paths through environment variables. Both the database and photos use persistent named volumes.

A single JPA transaction cannot guarantee consistency between files and metadata. Upload and deletion specifications must define partial-failure behavior and include corresponding tests.

## Build and Compose

The only orchestration file is compose.yaml at the repository root. A multi-stage Dockerfile first builds the frontend and then the backend with the generated Vue assets. The app service runs the resulting Java application.

The final image does not need the Vite development server. Direct Maven/Vite commands remain useful for development; acceptance uses Compose.

Use one app image and one compose.yaml. Supply configuration differences through environment variables without additional Compose files or overrides. Document example variables in .env.example.

If local SonarQube is selected, define it and its supporting infrastructure in the same compose.yaml under the quality profile. This profile enables auxiliary tools, not a separate application environment. Check resource and database requirements for the selected SonarQube version in SETUP-001.

Normal shutdown preserves volumes. Verify recovery after container recreation with isolated test data, not the user's gallery.
