# 🗺️ Project Roadmap

This roadmap describes potential improvements to the existing Amazon-inspired static storefront. It is deliberately staged so that the prototype is made reliable before larger features or infrastructure are considered.

> [!NOTE]
> Roadmap items are proposals unless marked complete with evidence. A checklist item is not a delivery promise.

## 🎯 Guiding priorities

1. Correctness before feature count.
2. Repair broken resources before adding more visual sections.
3. Accessibility and semantic behaviour are part of frontend quality, not optional polish.
4. Keep the implementation dependency-light while that remains appropriate.
5. Do not add a backend simply to make the repository look more complex.
6. Do not describe mock UI as a real commerce workflow.

## Phase 1: Stabilize the current prototype

- [x] Add automated JavaScript behaviour tests.
- [x] Add HTML structure and local-reference validation.
- [x] Document the current architecture and non-functional UI elements.
- [x] Record the missing local image paths.
- [ ] Source original or permissively licensed replacement images.
- [ ] Add an asset manifest with source, creator, licence, and usage notes.
- [ ] Resolve all broken local asset references.
- [ ] Verify remote image/font/icon dependencies and document fallback behaviour.
- [ ] Run a complete browser-based responsive review.
- [ ] Review navigation semantics, accessible names, and focus order.

**Exit criteria:** no unexplained missing local files, all redistributed assets have a documented rights basis, and the current UI can be reviewed consistently on desktop and mobile.

## Phase 2: Improve frontend quality

- [ ] Replace placeholder anchors used as actions with semantic buttons where appropriate.
- [ ] Ensure all meaningful images have accurate alternative text.
- [ ] Add image loading/error fallbacks.
- [ ] Review heading hierarchy and landmark structure.
- [ ] Add reduced-motion handling if motion or animation is introduced.
- [ ] Review contrast and reflow at zoom.
- [ ] Improve product rail discoverability for keyboard and touch users.
- [ ] Add targeted tests for any new behaviour.

**Exit criteria:** interactions are keyboard operable, semantics are coherent, and test coverage matches implemented behaviour.

## Phase 3: Improve content maintainability

- [ ] Extract repeated product-card content into a small local data structure.
- [ ] Define the minimum product-card fields and validate missing values.
- [ ] Render repeated content with a focused, testable function.
- [ ] Keep content separate from layout and styling.
- [ ] Add empty-state and malformed-data tests.
- [ ] Keep a clear distinction between illustrative product content and real product offers.

**Exit criteria:** repeated content is easier to update without changing the page's visual structure, and rendering behaviour is tested.

## Phase 4: Optional frontend demonstration features

Only implement these if the project needs a richer browser-only demo:

- [ ] Local product filtering.
- [ ] Category filtering.
- [ ] Product detail presentation.
- [ ] Non-persistent demo cart with explicit educational labelling.
- [ ] Quantity and subtotal calculations with tests.
- [ ] Clear empty, no-results, and invalid-input states.

These features would still not constitute real commerce. Browser storage and client-side calculations must not be treated as secure order records or payment authority.

## Phase 5: Separate product decision for a real commerce system

A production-like store is a new system, not a small extension to the current page. Before building one, create a product requirements document, threat model, architecture, data model, operational plan, and cost estimate.

Potential system areas include:
- Catalog and inventory services.
- Account identity and authorization.
- Cart and order lifecycle.
- Server-authoritative prices, discounts, tax, and shipping.
- Payment-provider integration and webhook verification.
- Customer privacy, retention, and deletion.
- Abuse prevention, auditability, observability, backup, and recovery.
- Deployment, incident response, and ongoing security maintenance.

No such services are present in the current repository.

## Decision review

For each proposed item, document:
- User problem and expected outcome.
- Acceptance criteria.
- Implementation scope and dependencies.
- Accessibility and security impact.
- Test strategy.
- Maintenance cost.
- Whether documentation, diagrams, and asset records need updating.

## Progress reporting

Update this roadmap only after the relevant implementation is merged or committed and verified. Do not mark work complete because a document describes it.
