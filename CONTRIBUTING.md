# 🤝 Contributing to Amazon Clone

Thank you for considering a contribution. This repository is an educational, static storefront prototype built with HTML, CSS, and browser-native JavaScript. Contributions should improve the quality, clarity, accessibility, reliability, and maintainability of that prototype.

> [!IMPORTANT]
> The visible search, account, order, cart, category, and product controls are not complete commerce features. A contribution must not describe them as functional unless the implementation and tests genuinely support that claim.

## 📚 Before you begin

Read these project documents before making a broad change:

- [Project overview](docs/project-overview.md) for the purpose and non-goals.
- [Architecture](docs/architecture.md) for the current browser-only structure.
- [Project structure](docs/project-structure.md) for file responsibilities.
- [Feature reference](docs/features.md) for implemented and presentation-only elements.
- [Testing strategy](docs/testing-strategy.md) for expected validation.
- [Accessibility notes](docs/ACCESSIBILITY.md) and [test plan](docs/accessibility-test-plan.md).
- [Security policy](SECURITY.md) for safe reporting and implementation boundaries.
- [Documentation maintenance standard](docs/documentation-maintenance.md) for keeping project information accurate.

## 🧰 Development environment

### Required tools

| Tool | Purpose | Requirement |
|---|---|---|
| Modern browser | Render and manually test the page | Required |
| Python 3 | Serve the site and run HTML validation | Required for documented Python commands |
| Node.js 20+ | Run the built-in test runner | Required for JavaScript tests |
| Git | Version control | Required for contributions |

The current application has no package manager manifest, framework, bundler, or application backend. Do not run an invented `npm install` step.

### Start the site

Run from the repository root:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`. Serving from the root is important because the document uses relative references such as `./amazone.css`, `./amazone.js`, and `imgs/...`.

## 🔍 Choose the right change

### Bug fix

A bug fix should identify the actual broken behaviour, explain its user impact, and include a reproducible test where practical. Avoid changing unrelated layout or renaming files as part of a focused correction.

### Frontend enhancement

A frontend enhancement should state whether it changes markup, styling, browser interaction, keyboard behaviour, or responsive layout. New interactive controls should use semantic elements and expose a useful accessible name and state.

### Documentation

Documentation must be project-specific and verifiable against the current source. Explain what exists, how it works, its constraints, and how to validate it. Clearly label future proposals as proposals.

### Asset contribution

For each added image, icon, font, or other media file, provide:
- The exact repository path and where it is used.
- The original source or creator.
- The licence or explicit permission basis.
- Any required attribution or redistribution conditions.
- The intended alternative text or decorative status.

A public URL does not automatically grant redistribution rights. Do not copy retailer imagery simply because the filename resembles an existing missing path.

## 🧪 Required validation

Run the checks from the repository root:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Then manually:
1. Serve the page over HTTP.
2. Check the browser console and network panel.
3. Activate the previous and next carousel controls.
4. Test carousel wrap-around at both ends.
5. Scroll each product rail with native horizontal input and vertical wheel input.
6. Confirm page scrolling is not trapped at rail boundaries.
7. Review the page at narrow, medium, and wide widths.
8. Navigate with a keyboard and inspect focus visibility.
9. Check image loading and ensure missing-asset warnings are understood rather than ignored.

The Python checker currently reports missing local image paths as warnings. Do not claim that a check is clean if unresolved references remain.

## 🧱 Implementation standards

- Keep selectors and behaviour synchronized across `index.html`, `amazone.css`, and `amazone.js`.
- Prefer semantic HTML over clickable generic containers.
- Use native buttons for actions and anchors for navigation.
- Preserve keyboard operability and visible focus.
- Avoid unnecessary dependencies for a small static project.
- Keep JavaScript defensive around optional DOM elements.
- Do not add fake authentication, checkout, payment, inventory, or order behaviour.
- Never put API keys, tokens, or private values in browser files.
- Keep test data synthetic and avoid real personal information.
- Avoid unrelated formatting churn that obscures the functional change.

## 📝 Documentation expectations

When behaviour changes, update the relevant feature, architecture, workflow, testing, accessibility, security, and limitation documents. When a path changes, update the project tree and links. When an asset changes, update the asset inventory and licence record. See [Documentation Maintenance](docs/documentation-maintenance.md).

## 🔀 Pull request expectations

A useful pull request includes:
- A concise title describing the outcome.
- The problem and context.
- The implementation approach and important trade-offs.
- Before/after screenshots for visual changes, when available.
- Automated and manual checks actually performed.
- Any new external dependency or asset and its licence.
- Known limitations and follow-up work.

Complete the repository pull request template. Keep changes reviewable and avoid combining unrelated work.

## 🛡️ Security reports

Do not publish exploitable details, secrets, or private user data in public issues. Follow [SECURITY.md](SECURITY.md) for responsible reporting.

## ✅ Definition of done

A contribution is ready when its behaviour is clear, its implementation is scoped, the relevant checks pass, documentation is accurate, accessibility has been considered, and no existing useful file or asset has been removed unintentionally.
