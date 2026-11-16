# 🧪 Testing Strategy

## 1. Goals

Testing should protect the behaviour that actually exists, catch regressions early, and clearly identify what automated checks cannot prove. The current project is a static frontend, so the strategy focuses on JavaScript interactions, basic document validation, and manual browser review.

## 2. Test layers

| Layer | Tool | Coverage |
|---|---|---|
| Syntax | Node.js `--check` | JavaScript parse errors |
| Unit/behaviour | Node.js built-in test runner | Carousel and wheel-handler logic |
| Markup validation | Python standard library checker | Required tags, title, duplicate IDs |
| Local resource validation | Python checker | Relative file references |
| Browser smoke test | Manual browser | Actual rendering and interaction |
| Accessibility review | Keyboard/screen-reader/manual inspection | Focus, names, semantics, alternatives |
| CI | GitHub Actions | Repeatable automated checks on repository changes |

## 3. Current automated cases

### Carousel

- Startup selects the first slide.
- Only the active slide is displayed.
- Inactive slides receive `aria-hidden="true"`.
- Next and previous controls move the active index.
- Index wraps at both boundaries.
- Click default action is prevented when a supported event is passed.
- Missing slides and missing controls do not crash the script.

### Product rails

- Vertical-dominant wheel movement changes horizontal scroll position.
- The candidate scroll position is clamped to the valid range.
- Native horizontal wheel movement is not intercepted.
- Page scrolling is not trapped when a rail reaches a boundary.
- Multiple rails receive independent handlers.

## 4. Run checks locally

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

No package installation is required. Use Node.js 20 or newer and Python 3.

## 5. Manual browser matrix

| Scenario | Input method | Expected observation |
|---|---|---|
| Initial load | Browser navigation | Page structure and styles load |
| Carousel forward | Mouse/keyboard | Next slide is displayed |
| Carousel backward | Mouse/keyboard | Previous slide is displayed |
| Carousel wrap | Repeated activation | Index wraps across endpoints |
| Rail movement | Horizontal trackpad | Native horizontal scrolling remains available |
| Rail movement | Vertical wheel over rail | Rail scrolls if it has room |
| Rail boundary | Vertical wheel at end | Page scrolling remains available |
| Narrow layout | Responsive viewport | Controls and text remain usable |
| Keyboard traversal | Tab/Enter/Space | Focus order and activation are understandable |
| Resource failure | Network tools | Broken remote/local resources are identified |

## 6. Mock-DOM limitations

The Node.js suite creates lightweight element objects with the properties and event methods needed by the script. This allows deterministic testing of logic without a browser. It does not implement CSS layout, image loading, focus navigation, accessibility trees, real wheel-device behaviour, or browser-specific rendering.

A passing unit test must not be described as proof of cross-browser visual correctness.

## 7. HTML checker limitations

The Python checker uses the standard-library HTML parser. It verifies selected structural conditions, duplicate IDs, and local file references. It is not a full HTML conformance validator and does not fetch remote resources.

Missing local image paths are reported as warnings because the current repository has no tracked `imgs/` directory.

## 8. Test design guidelines

- Test observable behaviour, not internal implementation details where avoidable.
- Cover normal, boundary, and missing-element cases.
- Keep fixtures deterministic and synthetic.
- Avoid network calls in unit tests.
- Do not weaken assertions to hide a genuine regression.
- Add a regression test when a reproducible defect is fixed.
- Keep manual-only checks clearly labelled.

## 9. Future browser automation

A real browser automation framework may be considered if visual and interaction complexity increases. Before adding it, define the browser matrix, expected coverage, runtime cost, maintenance burden, and CI execution requirements.

## 10. Failure handling

Preserve failure output, reproduce on the same commit, identify whether the problem is code or environment, fix the underlying cause, and rerun the full suite. Update documentation when the test scope changes.
