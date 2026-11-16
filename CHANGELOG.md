# 📜 Changelog

All notable project changes should be recorded here. Entries describe repository changes, not aspirational features. Dates use ISO 8601 calendar format.

The project does not currently use an automated release tool. Version labels below are repository history labels and should only be changed when a release is intentionally prepared.

## [Unreleased]

### Documentation and repository quality

- Expanded the project overview, architecture, workflow, data-flow, system-design, testing, maintenance, and accessibility documentation.
- Added a documentation navigation hub and documentation maintenance guidance.
- Added a static prototype architecture decision record.
- Added explicit distinctions between implemented interactions, presentation-only UI, and future proposals.
- Added diagrams describing the browser load sequence, carousel state changes, and product rail wheel handling.
- Expanded contributor, support, security, and community guidance.
- Added a documentation issue form and a documentation validation workflow.
- Improved the README with repository badges, project structure, setup, validation commands, known limitations, and links to technical references.

### Known issues retained intentionally

- The HTML still references local images under `imgs/`, but the directory is not tracked in the repository.
- External visual resources remain dependent on third-party hosts.
- Search, account, cart, product links, checkout, payments, and order management remain unimplemented.

## [0.1.0] - 2025-01-01

### Added

- Initial static marketplace-inspired storefront markup.
- Main navigation and secondary navigation presentation.
- Promotional hero image area with previous and next controls.
- Category cards and horizontally arranged product collections.
- Static deal cards and footer.
- Responsive CSS rules for narrower layouts.
- Browser-side carousel and horizontal product rail interactions.
- Initial dependency-free JavaScript behaviour tests and HTML/reference validation.

### Scope

The initial release is an educational frontend prototype. It does not implement a commerce backend or transaction lifecycle.

## Changelog maintenance rules

For each future entry:
1. Use a date only when the change is actually committed or released.
2. Group changes under Added, Changed, Fixed, Removed, Security, or Documentation where useful.
3. Identify user-visible behaviour and important compatibility changes.
4. Record material limitations and migration notes.
5. Do not claim a test, deployment, or security review occurred unless it was performed.
