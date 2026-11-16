# ADR 0001: Retain a Static Frontend Prototype

- **Status:** Accepted
- **Decision date:** 2026-11-16
- **Decision owner:** Repository maintainer
- **Scope:** Current Amazon Clone repository

## 1. Context

The repository is a small browser-side storefront demonstration. Its runtime consists of:
- `index.html` for static page content and controls.
- `amazone.css` for presentation and responsive layout.
- `amazone.js` for the carousel and product rail interactions.

The repository also contains Node.js built-in tests and a Python standard-library HTML checker. There is no package manifest, frontend framework, build pipeline, API, backend, or database.

The current product goal is to demonstrate frontend layout and browser interaction patterns. There is no requirement in the current implementation that needs server-side state or a framework runtime.

## 2. Decision drivers

The decision considers:
- The small size and clear boundaries of the existing code.
- The educational value of browser-native technologies.
- The absence of dynamic data and persistence requirements.
- The cost of adding dependencies and build configuration.
- The need to keep local setup simple.
- The risk of suggesting that a visual clone is a functioning commerce system.

## 3. Decision

Retain the project as a dependency-light static frontend prototype. Continue using HTML, CSS, and vanilla JavaScript for the current scope. Keep the Node.js built-in test runner and Python standard-library checker for development validation.

Do not introduce a framework, API, database, authentication system, or payment service unless a concrete product requirement justifies that architectural change.

## 4. Alternatives considered

### Alternative A: Introduce a frontend framework immediately

**Advantages:** component abstraction, state management patterns, and a larger ecosystem.

**Disadvantages:** adds dependencies and build tooling to a small page; does not solve the missing image assets or create real commerce capabilities; increases setup and maintenance requirements.

**Decision:** not selected for the current scope.

### Alternative B: Add a backend and database immediately

**Advantages:** could support dynamic data and persistent user operations if those features were required.

**Disadvantages:** no current user or data requirement justifies it; introduces security, deployment, maintenance, privacy, and operational responsibilities; would be misleading if only superficial endpoints were added.

**Decision:** not selected for the current scope.

### Alternative C: Keep the current static implementation

**Advantages:** minimal setup, easy source inspection, no runtime package installation, and suitable for frontend learning.

**Disadvantages:** content is manually maintained; no persistence or real commerce features; repeated markup may become difficult to scale.

**Decision:** selected.

## 5. Consequences

### Positive consequences

- The application can be served by an ordinary static HTTP server.
- The browser runtime has no framework dependency.
- Contributors can inspect the implementation directly.
- Tests can run without third-party JavaScript test packages.
- The project scope remains easy to explain accurately.

### Trade-offs

- Product/category content remains hard-coded.
- Browser state is not persistent.
- There is no authoritative product or pricing source.
- Real user accounts, cart, checkout, payments, and orders are out of scope.
- External resources and missing local image references affect visual reliability.
- A future backend would require a separate architecture decision.

## 6. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Project grows beyond static-page complexity | Revisit this decision when a concrete requirement appears |
| Repeated markup becomes hard to maintain | Consider a tested local data structure before a framework |
| Visual UI is mistaken for real commerce | Keep README and UI scope statements accurate |
| External assets fail or lack rights | Maintain the asset inventory and use approved resources |
| Mock-DOM tests are mistaken for browser verification | Keep manual browser and accessibility checks explicit |

## 7. Revisit criteria

Reopen this ADR if a committed product requirement needs dynamic product data, user identity, persistent cart or order records, server-side pricing and inventory, payment processing, or operational monitoring.

Any change should include requirements, threat modelling, data ownership, test strategy, migration planning, and maintenance cost.

## 8. Review history

This decision records the architecture appropriate to the current repository state. It should be superseded by a new ADR rather than silently rewritten if a future architectural change is approved.
