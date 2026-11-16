# 📜 Changelog

All notable project changes should be recorded here. Entries describe repository changes, not aspirational features. Dates use ISO 8601 calendar format.

The project does not currently use an automated release tool. Version labels below are repository history labels and should only be changed when a release is intentionally prepared.

## [Unreleased]

### Frontend and accessibility

- Added a skip-to-main-content link and a main content landmark.
- Identified the promotional carousel as a labelled region with a descriptive carousel role.
- Replaced the invalid image list wrapper with a dedicated carousel image container and aligned the JavaScript selector.
- Removed non-functional category placeholder anchors and retained their presentation as non-interactive labels.
- Added consistent keyboard focus styling and a reduced-motion media query.
- Added descriptive CSS section organization and centralized storefront design tokens.
- Corrected the product image maximum-height unit and the product-card heading selector.
- Improved carousel and product-rail code comments to document state, event, and boundary behaviour.

### Tests and validation

- Expanded JavaScript coverage for one-slide carousels, lower and upper rail clamping, equal wheel deltas, non-passive listeners, and synthetic events without `preventDefault`.
- Strengthened HTML validation for document language, charset, viewport metadata, duplicate IDs, image alternative-text attributes, and local file references.
- Added a Markdown validation utility for non-empty documentation files and local relative links.
- Integrated the documentation checker into CI and the documentation workflow.
- Updated the pull request checklist and contributor commands to include documentation validation.

### Documentation and repository quality

- Expanded the project overview, architecture, workflow, data-flow, system-design, testing, maintenance, deployment, and accessibility documentation.
- Added a documentation navigation hub and documentation maintenance guidance.
- Added a static prototype architecture decision record.
- Added explicit distinctions between implemented interactions, presentation-only UI, and future proposals.
- Added diagrams describing browser startup, carousel state changes, and product rail wheel handling.
- Expanded contributor, support, security, and community guidance.
- Improved issue forms and pull request guidance.
- Updated the README with badges, architecture diagrams, complete documentation navigation, setup, validation, known limitations, and repository structure.
- Updated editor, environment, Git ignore, Dependabot, and GitHub Actions configuration comments and behaviour.

### Known issues retained intentionally

- The HTML still references local images under `imgs/`, but the directory is not tracked in the repository.
- External visual resources remain dependent on third-party hosts.
- Search, account, cart, product navigation, checkout, payments, and order management remain unimplemented.
- Automated JavaScript tests use a mock DOM and do not replace browser or assistive technology testing.

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
