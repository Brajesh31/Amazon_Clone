# 🧪 Quality Assurance Plan

## 1. Purpose and scope

This document defines repeatable checks for the static storefront. It covers JavaScript syntax, browser interaction tests, HTML structure, local file references, and manual browser review.

It does not claim end-to-end coverage of an e-commerce system. The repository has no checkout, authentication, payment, order, or database workflows to test.

## 2. Quality gates

| Gate | Command or method | Expected result |
|---|---|---|
| Required source files | CI file checks | HTML, CSS, and JS entry files exist |
| JavaScript syntax | `node --check amazone.js` | No syntax errors |
| JavaScript behaviour | `node --test tests/*.test.js` | All test cases pass |
| HTML/reference validation | `python scripts/check_html.py` | Required structure is valid; missing assets are reported |
| Browser smoke test | Manual HTTP preview | Page and interactions render without unexpected console errors |
| Responsive review | Browser viewport testing | Content remains readable and controls usable |
| Accessibility review | Keyboard and assistive technology | Meaningful names, order, focus, and alternatives |

## 3. Automated JavaScript coverage

The current test suite uses Node.js built-in modules and a lightweight mock DOM. It does not require a third-party test framework.

### Carousel cases

- Initial startup displays the first slide.
- Inactive slides are hidden.
- The script updates `aria-hidden` values.
- Next control moves forward one slide.
- Previous control moves backward one slide.
- Navigation wraps at the first and final slide.
- Default click behaviour is prevented when a suitable event is provided.
- Empty slide collections and absent controls do not crash the script.

### Product rail cases

- Vertical-dominant wheel input changes `scrollLeft`.
- The wheel event is prevented only when horizontal movement occurs.
- Native horizontal wheel input is not intercepted.
- A rail at its right boundary does not trap page scrolling.
- Each product rail receives an independent event handler.

The test suite does not currently exercise a real browser layout engine. Mock DOM tests are useful for logic but cannot prove visual rendering or cross-browser behaviour.

## 4. Run the complete local suite

From the repository root:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Use Node.js 20 or newer for the documented test environment and Python 3 for the HTML checker.

## 5. Manual browser test cases

### Page loading

- [ ] Open the page through an HTTP server started at the repository root.
- [ ] Confirm `amazone.css` and `amazone.js` load.
- [ ] Check the browser console for syntax or runtime errors.
- [ ] Inspect network requests for failed local and remote resources.

### Carousel

- [ ] Confirm the first image appears on load.
- [ ] Activate Next several times.
- [ ] Confirm the sequence wraps to the first image.
- [ ] Activate Previous from the first image.
- [ ] Confirm it wraps to the last image.
- [ ] Verify controls are keyboard operable.
- [ ] Inspect focus visibility and accessible names.

### Product rails

- [ ] Scroll horizontally using a trackpad or horizontal wheel input.
- [ ] Use vertical wheel input over a product rail.
- [ ] Confirm the rail moves while content remains available.
- [ ] Reach the beginning and end of a rail.
- [ ] Confirm page scrolling continues at both boundaries.
- [ ] Repeat with every rail on the page.

### Responsive and visual review

- [ ] Review at narrow mobile width.
- [ ] Review at common phone width.
- [ ] Review at tablet width.
- [ ] Review at desktop width.
- [ ] Zoom to 200%.
- [ ] Confirm no controls overlap or become unreachable.
- [ ] Confirm product cards remain legible.
- [ ] Review image cropping after assets are restored.

## 6. Known test limitations

- No browser automation suite is currently configured.
- No screenshot-based visual regression suite is configured.
- External image/font/icon requests are not tested for availability by the unit tests.
- The local `imgs/` directory is missing from the tracked repository.
- Accessibility checks require manual review and are not replaced by structural HTML validation.

## 7. Failure triage

When a check fails:
1. Preserve the complete error output.
2. Identify the failing source file and test case.
3. Reproduce the issue on the same commit.
4. Determine whether the failure is code, environment, or missing-resource related.
5. Fix the cause rather than weakening the assertion without justification.
6. Rerun the complete suite.
7. Update documentation when the behaviour or known limitations change.

## 8. Release quality rule

A release should not be described as fully verified unless the automated suite and the relevant manual browser checks were actually run. Record unresolved issues explicitly.
