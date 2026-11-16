# 🚀 Future Scope and Engineering Opportunities

## 1. Status and decision principle

Everything in this document is proposed work unless it is independently implemented, tested, and reflected in the current source. This roadmap is not a promise or a claim that the application already supports the listed capabilities.

The best next change is not necessarily the largest feature. Repairing broken assets, semantics, and test gaps can provide more value than adding a large quantity of superficial UI.

## 2. Phase 1: Asset and rendering integrity

### Proposed work

- [ ] Decide which local image slots are necessary.
- [ ] Source original or permissively licensed replacements.
- [ ] Record source, creator, rights basis, and usage restrictions.
- [ ] Add consistent dimensions and file naming.
- [ ] Add meaningful alternative text or mark decorative assets correctly.
- [ ] Add a fallback for failed image loads where useful.
- [ ] Verify all local references with the HTML checker.

### Acceptance evidence

- No unresolved local asset path remains without an explicit reason.
- Every redistributed asset has a documented rights basis.
- Images render at expected aspect ratios and do not create avoidable layout shifts.
- Alternative text has been reviewed against actual image content.

## 3. Phase 2: Accessibility and semantic quality

### Proposed work

- [ ] Review landmarks and heading hierarchy.
- [ ] Ensure each action uses a native button.
- [ ] Ensure each navigation element has a meaningful destination.
- [ ] Review keyboard focus and order.
- [ ] Test carousel state with assistive technology.
- [ ] Review contrast and zoom/reflow.
- [ ] Ensure horizontal rails can be used without a mouse wheel.

### Acceptance evidence

Documented keyboard, screen-reader, and visual checks. Do not claim formal conformance without a defined audit.

## 4. Phase 3: Maintainable static content

### Proposed work

- [ ] Extract repeated product card values into a local data structure.
- [ ] Define required fields and safe defaults.
- [ ] Render repeated cards with a focused function.
- [ ] Add tests for empty, malformed, and valid records.
- [ ] Keep the product text explicitly illustrative.
- [ ] Preserve a no-framework approach unless the project needs more.

### Acceptance evidence

Less duplicated content, stable output, and tests for rendering and data edge cases.

## 5. Phase 4: Optional browser-only interactions

Potential features:
- [ ] Client-side product filtering.
- [ ] Category filtering.
- [ ] Product detail presentation.
- [ ] A clearly labelled, non-persistent demo cart.
- [ ] Quantity and subtotal calculation.
- [ ] Empty and no-results states.
- [ ] Clear feedback for invalid user input.

These features would still be demonstrations. Browser-side storage and calculations are not trusted transaction records.

## 6. Phase 5: Separate decision for a commerce backend

A real commerce system would be a substantial new product scope. Before implementation, write a product requirements document, data model, threat model, architecture, cost estimate, and operational plan.

Potential domains:
- Product catalogue and inventory.
- Authentication, account recovery, and authorization.
- Cart and order lifecycle.
- Server-authoritative price, tax, shipping, and discount calculations.
- Payment provider integration and webhook verification.
- Privacy, retention, export, and deletion.
- Abuse prevention and rate limiting.
- Auditability, monitoring, backups, and incident response.

None of these services exists in the current repository.

## 7. Change decision template

Before starting any phase, document:
1. User problem.
2. Intended outcome.
3. Scope and non-goals.
4. Acceptance criteria.
5. Data and trust boundaries.
6. Accessibility impact.
7. Security and privacy impact.
8. Test plan.
9. Documentation changes.
10. Maintenance cost.

## 8. Progress integrity

Only mark a roadmap item complete after the implementation is committed and the acceptance evidence exists. A diagram, issue, or documentation paragraph does not count as implementation.
