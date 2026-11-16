# ADR 0001: Keep the Project as a Static Frontend Prototype

- **Status:** Accepted
- **Date:** 2026-11-16
- **Decision owners:** Repository maintainers

## Context

The current repository is composed of a single HTML document, a CSS file, and a small vanilla JavaScript file. There is no package manifest, build system, framework, application API, or database. The core purpose is to demonstrate a marketplace-style interface and a small number of browser interactions.

Introducing a framework or backend would add operational and maintenance complexity without a demonstrated requirement in the current scope.

## Decision

Retain the project as a dependency-light static frontend prototype. Use browser-native HTML, CSS, and JavaScript for current capabilities. Keep the Node.js built-in test runner and Python standard-library validation script for development checks.

## Consequences

### Positive

- No runtime dependency installation is required.
- The project can be served by any ordinary static HTTP server.
- The implementation is easy to inspect and suitable for frontend learning.
- Tests can run without a third-party JavaScript test framework.

### Trade-offs

- Repeated product markup is manually maintained.
- There is no product data service or persistence.
- The current architecture cannot support real commerce operations.
- Browser-side behaviour cannot enforce transaction or account security.
- A future backend would require a separate design and implementation.

## Revisit when

Reconsider this decision when a concrete requirement needs dynamic product data, account state, persistent carts, orders, or other server-owned behaviour. A change in architecture must include requirements, threat modelling, data design, and a migration plan.
