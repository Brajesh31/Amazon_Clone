# 🧑‍💻 Development Guide

## 1. Development philosophy

Keep the current project understandable and lightweight. It is a static HTML/CSS/vanilla-JavaScript storefront prototype. Add complexity only when a real requirement justifies it, and update tests and documentation alongside implementation.

## 2. Prerequisites

| Tool | Version / expectation | Reason |
|---|---|---|
| Browser | Modern evergreen browser | Render and manually test |
| Python | Python 3 | Static server and HTML checker |
| Node.js | 20 or newer | Built-in test runner and syntax validation |
| Git | Current supported release | Version control |

There is no `package.json`, bundler, transpiler, frontend framework, or runtime dependency installation in the current repository.

## 3. Clone and serve

```bash
git clone https://github.com/Brajesh31/Amazon_Clone.git
cd Amazon_Clone
python -m http.server 8000
```

Open `http://localhost:8000/`.

Run the server from the repository root. Relative references such as `./amazone.css`, `./amazone.js`, and `imgs/...` are resolved against the page URL. Opening the file directly with `file://` is not an equivalent deployment test.

## 4. Source map

| File | Responsibility | Change considerations |
|---|---|---|
| `index.html` | Static page content and controls | Preserve semantic structure and align classes with JS/CSS |
| `amazone.css` | Layout, typography, colours, responsive rules | Test multiple widths and zoom |
| `amazone.js` | Carousel and product rail interactions | Guard optional DOM elements and cover behaviour with tests |
| `tests/amazone.test.js` | Mock-DOM behaviour tests | Extend assertions when interaction changes |
| `scripts/check_html.py` | HTML structure and local path checks | Keep warnings and failures meaningful |
| `docs/` | Project technical and operational knowledge | Update when implementation changes |

## 5. Standard validation

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
python scripts/check_docs.py
```

The checker reports unresolved local image paths as warnings because the repository currently lacks the referenced `imgs/` directory. Do not suppress these warnings without resolving or documenting the underlying issue.

## 6. JavaScript development practices

- Keep the script compatible with browser-native JavaScript.
- Avoid adding dependencies for simple DOM interactions.
- Query only the elements needed by the behaviour.
- Guard optional controls and empty collections.
- Use event options deliberately, especially when calling `preventDefault`.
- Keep state local when it has no need to survive a page reload.
- Avoid unsafe HTML injection when handling future user input.
- Keep selectors stable and update tests when markup changes.

## 7. HTML and CSS practices

- Prefer semantic landmarks and controls.
- Use buttons for actions and anchors for real destinations.
- Keep accessible names and visible focus styles.
- Keep responsive rules grouped by meaningful breakpoints.
- Avoid inline styles when a reusable stylesheet rule is clearer.
- Preserve image aspect ratio and prevent unexpected layout shifts.
- Use alternative text based on the actual image content, not guessed filenames.

## 8. Test development

The existing test suite uses Node.js built-in modules and a small mock DOM. It tests logic but does not provide browser layout fidelity. Add tests for new edge cases, including missing elements, empty data, boundaries, and independent instances.

Manual browser testing remains necessary for layout, real wheel input, keyboard focus, network failures, and accessibility.

## 9. Asset development

The local image directory is currently absent. Before adding assets, confirm redistribution rights, source, file path, alternative text, and visual fit. Update [Asset Inventory](ASSET-INVENTORY.md) and run the local-reference checker.

## 10. Documentation expectations

Update the relevant feature, workflow, architecture, QA, accessibility, security, and limitation documents when behaviour changes. See [Documentation Maintenance](documentation-maintenance.md).

## 11. Avoid unnecessary scope expansion

Do not add:
- A backend or database without a product requirement.
- Fake login or checkout flows.
- Unused packages or build tools.
- Credentials or secret values.
- Third-party images without permission.
- Long generic documentation that is not grounded in this implementation.
