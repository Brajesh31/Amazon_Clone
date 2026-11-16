# ♿ Accessibility Engineering Notes

## 1. Purpose and conformance status

This document records accessibility-relevant implementation details and review requirements for the current static storefront. It is not an accessibility certification, audit report, or claim of WCAG conformance.

Accessibility must be considered across the actual page structure, keyboard interactions, visual presentation, images, and responsive behaviour. A control that looks interactive but does nothing can also create an accessibility problem because it communicates an unavailable action.

## 2. Current implementation observations

The page currently includes:
- An English document language declaration.
- A viewport meta element.
- A document title.
- A labelled primary navigation region.
- Native buttons for the hero previous and next controls.
- A search input with an accessible label that explicitly describes its demonstration-only status.
- A visible keyboard focus style for carousel buttons.
- A JavaScript update to `aria-hidden` on inactive hero slides.
- Responsive CSS breakpoints.

These are useful foundations, but they do not establish full accessibility.

## 3. Known concerns requiring review

### 3.1 Images and alternative text

Many local product and category images currently have empty `alt` values. Empty alternative text is correct only when an image is decorative or its information is already fully conveyed by adjacent text. It is not a universal placeholder for unknown content.

Because the local `imgs/` directory is absent, the intended visual content cannot reliably be inferred from the filename alone. When assets are restored:
1. Inspect the actual image.
2. Determine whether it conveys information or is decorative.
3. Write concise alternative text for informative images.
4. Use `alt=""` only for decorative or redundant images.
5. Avoid repeating the adjacent heading word-for-word unless that is needed to convey the image's content.

### 3.2 Carousel

The carousel has native buttons with accessible names, and JavaScript updates `aria-hidden` for inactive slides. Remaining considerations include:
- Whether the images have meaningful alternatives.
- Whether the active slide is clear to screen-reader users.
- Whether keyboard focus remains predictable after activation.
- Whether the controls remain usable at narrow widths.
- Whether future autoplay or animation would need pause and reduced-motion controls.

The current carousel does not autoplay. Do not add autoplay without a separate interaction and accessibility design.

### 3.3 Placeholder controls

Search, account, orders, cart, category links, and product links include presentation that may look interactive. Where an element is not a real action or destination, avoid misleading keyboard focus and accessible names. When implementing a control, give it a genuine action, state, and expected result.

### 3.4 Layout and visual access

Contrast, text scaling, zoom, reflow, reading order, and overflow need manual verification in browsers. CSS breakpoints alone do not prove that content remains accessible.

## 4. Semantic markup expectations

- Use landmarks such as `header`, `nav`, `main`, and `footer` where they clarify page structure.
- Use headings in a meaningful hierarchy rather than selecting heading levels only for visual size.
- Use `button` for actions and `a` for navigation.
- Associate labels with form inputs.
- Avoid using colour as the only signal for a state.
- Ensure controls have descriptive accessible names.
- Keep focus visible and in a logical order.
- Ensure hidden content is not exposed as active content to assistive technology.

## 5. Keyboard interaction expectations

- Every actionable control must be reachable using a keyboard.
- Native buttons should activate using Enter and Space.
- Anchors should navigate to meaningful destinations.
- Focus should not be obscured by overlays or clipped containers.
- Horizontal product rails must not require a mouse wheel as the only means of navigation.
- No interaction should trap keyboard focus.

## 6. Responsive and zoom review

Test at:
- Narrow mobile viewport.
- Common mobile portrait and landscape widths.
- Tablet width.
- Desktop width.
- 200% browser zoom.
- Increased text size where browser settings allow.

Confirm content reflows without unintended horizontal page scrolling, clipped controls, or overlapping text. Horizontal product rails are an intentional local overflow region and should remain discoverable.

## 7. Test procedure

Use the [Accessibility Test Plan](accessibility-test-plan.md) for a detailed checklist. At minimum:
1. Navigate the page using only a keyboard.
2. Inspect the browser accessibility tree.
3. Test with at least one screen reader when possible.
4. Inspect contrast and focus indicators.
5. Test zoom and narrow viewport reflow.
6. Verify image alternatives after restoring assets.
7. Record browser, assistive technology, steps, expected result, and actual result.

## 8. Definition of an accessibility improvement

A change is not complete merely because an ARIA attribute was added. It should improve the actual interaction or information exposed to users, use native semantics where possible, and be tested with the relevant keyboard, screen-reader, or visual scenario.

## 9. Related references

- [Accessibility test plan](accessibility-test-plan.md)
- [Feature reference](features.md)
- [Quality assurance](QA.md)
- [Workflow](workflow.md)
- [Contribution standards](../CONTRIBUTING.md)
