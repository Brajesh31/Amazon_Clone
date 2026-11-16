# 🚀 Future Scope and Engineering Opportunities

The items below are proposals, not implemented features. They are ordered to improve the existing prototype before introducing a much larger commerce architecture.

## Phase 1: Repair and stabilize the current prototype

- [ ] Decide whether to restore the missing `imgs/` files or replace them with properly licensed assets.
- [ ] Add a rights/source record for every supplied visual asset.
- [ ] Review image alternative text and decorative-image handling.
- [ ] Check layout reflow and keyboard usability across screen sizes.
- [ ] Add a local visual regression or browser smoke-test strategy if project complexity warrants it.

**Completion evidence:** no broken local image references, documented asset rights, and repeatable accessibility/browser checks.

## Phase 2: Improve frontend maintainability

- [ ] Extract repeated product content into a small local JavaScript data structure.
- [ ] Render repeated cards through a focused function.
- [ ] Keep content separate from presentation.
- [ ] Add tests for the rendering logic and empty/error states.
- [ ] Add stronger semantic landmarks and consistent control behaviour.

**Completion evidence:** less duplicated markup, stable UI output, and automated tests covering new behaviour.

## Phase 3: Add optional storefront interactions

Possible additions, only after clear requirements:

- [ ] Functional client-side product filtering.
- [ ] Product detail presentation.
- [ ] Local demo cart with explicit non-persistent behaviour.
- [ ] Quantity and subtotal calculations.
- [ ] Empty state and invalid-input handling.

These features would still be a frontend demonstration unless backed by a trusted service. Do not treat local browser state as a secure order or payment record.

## Phase 4: Consider a real application backend

A separate product specification would be required before implementing:

- Product catalogue and inventory APIs.
- Authentication and authorization.
- Persistent cart and order records.
- Server-side price calculation.
- Payment provider integration.
- Order status and customer support workflows.
- Privacy, retention, audit logging, backup, recovery, and monitoring.

A backend should not be added merely to make the repository appear larger or more advanced.

## Decision gate

Before starting a phase, define the user problem, acceptance criteria, data requirements, security impact, test approach, and maintenance cost. Update the roadmap and architecture only after the decision is made.
