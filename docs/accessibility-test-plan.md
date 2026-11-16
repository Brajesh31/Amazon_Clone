# ♿ Accessibility Test Plan

## 1. Purpose and status

This plan provides repeatable manual checks for the current storefront. It is a test plan, not a completed audit or a claim of WCAG conformance. Record actual results when tests are performed.

## 2. Keyboard navigation

- [ ] Load the page and navigate using Tab only.
- [ ] Confirm the focus order follows the visible content order.
- [ ] Confirm every real action is keyboard reachable.
- [ ] Confirm carousel buttons activate with Enter and Space.
- [ ] Confirm focus indicators are visible against each background.
- [ ] Confirm focus is not clipped by an overflow container.
- [ ] Confirm no keyboard trap exists.
- [ ] Confirm placeholder links do not falsely advertise unavailable actions.

## 3. Screen-reader and semantics review

- [ ] Confirm the document language is correctly declared.
- [ ] Confirm the page title describes the page.
- [ ] Confirm navigation and main content landmarks are discoverable.
- [ ] Confirm heading levels communicate the page hierarchy.
- [ ] Confirm controls expose useful accessible names.
- [ ] Confirm the search input label explains its demonstration-only status.
- [ ] Confirm informative images have accurate alternative text.
- [ ] Confirm decorative images use empty alternative text.
- [ ] Confirm inactive carousel slides are not exposed as active content.
- [ ] Confirm carousel state changes are understandable to screen-reader users.

## 4. Visual accessibility

- [ ] Check text contrast against the actual rendered backgrounds.
- [ ] Check focus indicator contrast.
- [ ] Zoom to 200% and inspect layout.
- [ ] Increase text size and confirm labels remain visible.
- [ ] Check narrow viewport reflow.
- [ ] Confirm meaning is not conveyed through colour alone.
- [ ] Confirm controls have sufficient size and spacing for practical activation.
- [ ] Review images and text at high display scaling.

## 5. Product rail interaction

- [ ] Confirm horizontal scrolling works with a trackpad.
- [ ] Confirm horizontal scrolling is not available only through a mouse wheel.
- [ ] Test keyboard access and focus order around product content.
- [ ] Confirm page scrolling continues at rail boundaries.
- [ ] Ensure hidden or clipped content remains discoverable where necessary.

## 6. Carousel-specific review

The current carousel does not autoplay. Its native buttons have accessible labels and JavaScript updates `aria-hidden` on slides.

- [ ] Confirm button labels distinguish previous and next.
- [ ] Confirm each slide's alternative text communicates meaningful content.
- [ ] Confirm inactive slides are hidden from visual and assistive technology presentation.
- [ ] Confirm focus remains on the activated button after a change.
- [ ] Confirm repeated activation does not produce unexpected focus movement.
- [ ] If autoplay is ever added, require pause/stop controls and reduced-motion consideration before release.

## 7. Browser and assistive technology record

For each completed test, record:
- Browser and version.
- Operating system.
- Screen reader and version, if used.
- Viewport and zoom level.
- Test steps.
- Expected result.
- Actual result.
- Defect link or follow-up action.

Do not claim a test passed when it was not performed.

## 8. Reporting

Create an accessibility issue with a concise summary, affected page section, reproducible steps, impact, and sanitized evidence. Avoid including personal or sensitive information in screenshots.

## 9. Related references

- [Accessibility Notes](ACCESSIBILITY.md)
- [Quality Assurance](QA.md)
- [Feature Reference](features.md)
- [Contribution Guide](../CONTRIBUTING.md)
