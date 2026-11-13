# Development Guide

## Prerequisites

- A modern browser with JavaScript enabled.
- Python 3 for a simple static HTTP server.
- Node.js 20 or newer for the built-in test runner.
- Git for source control.

There is no `package.json`, bundler, transpiler, runtime dependency installation, or build output in the current project.

## Start a local server

Run from the repository root:

```bash
python -m http.server 8000
```

Visit <http://localhost:8000/>. Do not open `index.html` with a `file://` URL when testing relative assets.

## Source files

- `index.html`: static content and image paths.
- `amazone.css`: visual styles and breakpoints.
- `amazone.js`: browser interactions.
- `tests/amazone.test.js`: JavaScript unit tests.
- `scripts/check_html.py`: structural and local-reference checker.

## Run checks

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

The HTML checker reports unresolved local image paths as warnings because the current repository does not include the referenced `imgs/` directory. Do not mistake those warnings for repaired assets.

## Editing guidance

- Keep JavaScript selectors aligned with the classes in the HTML.
- Use semantic controls and keyboard-operable interactions for new functionality.
- Keep external asset URLs intentional and document their providers and licensing status.
- Do not add a frontend framework or build system unless there is a concrete requirement.
- Do not add pretend checkout, authentication, search, or cart behaviour.
- Avoid copying Amazon production content, imagery, or logos unless usage rights permit it.
- Check browser console errors and test both narrow and wide viewports after visual changes.

## Content and product data

The catalog is currently authored directly in HTML. If the project grows, consider extracting product card content into a small local JavaScript data structure before introducing a backend.
