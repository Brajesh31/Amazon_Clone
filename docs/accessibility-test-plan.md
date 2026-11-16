# ♿ Accessibility Test Plan

This plan supplements [Accessibility Notes](ACCESSIBILITY.md). It is a test checklist, not a claim of conformance.

## Keyboard checks

- [ ] Tab through all interactive elements in a logical order.
- [ ] Confirm visible focus styles.
- [ ] Activate carousel controls using Enter and Space.
- [ ] Confirm no non-functional placeholder element is presented as an actionable control.
- [ ] Confirm focus is not hidden behind sticky or overlapping content.

## Screen-reader checks

- [ ] Confirm document title and primary navigation landmark.
- [ ] Confirm buttons expose meaningful accessible names.
- [ ] Confirm informative images have useful alternative text.
- [ ] Confirm decorative images are ignored by assistive technology.
- [ ] Confirm inactive carousel slides are not announced as visible content.
- [ ] Confirm heading levels describe the content hierarchy.

## Visual and responsive checks

- [ ] Check text contrast against the actual backgrounds.
- [ ] Zoom to 200% and verify content remains usable.
- [ ] Test narrow viewport widths and text reflow.
- [ ] Check that content is not conveyed through colour alone.
- [ ] Confirm product rails remain discoverable without a mouse wheel.
- [ ] Respect reduced-motion preferences if motion is introduced.

## Important implementation notes

The current carousel updates `aria-hidden` on slides, and its controls have accessible labels. This is a useful baseline but not a complete accessible carousel pattern. Consider focus order, announcements, pause controls if autoplay is ever added, and reduced-motion handling.

The current HTML contains many empty image alt attributes. Each must be reviewed in context: empty alt is appropriate only when the image is decorative or redundant with adjacent text.

## Reporting

Include browser, assistive technology, viewport, keyboard steps, expected outcome, and actual outcome in an accessibility issue. Avoid sharing personal or sensitive user information in screenshots.
