# Contributing

Thanks for taking the time to improve this educational storefront prototype.

## Scope

Keep changes aligned with the current static HTML/CSS/JavaScript implementation unless a concrete requirement justifies a new architecture. Do not describe the project as a working store: it has no user accounts, search service, cart persistence, checkout, payment processing, API, or database.

## Development setup

Serve the repository root:

```bash
python -m http.server 8000
```

Use Node.js 20 or newer for tests. No npm installation is needed.

## Before opening a pull request

Run:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Also test the page in a browser at narrow and wide widths, use carousel controls, scroll product rails, inspect keyboard focus, and check the console.

## Contribution guidelines

- Keep selectors synchronized between HTML, CSS, and JavaScript.
- Prefer semantic elements and keyboard-operable controls.
- Provide descriptive alternative text for meaningful images.
- Do not add credentials, secrets, or private user data.
- Supply a clear licence or permission record for every new asset.
- Document new external services and their privacy implications.
- Do not claim functionality that is only represented by a visual placeholder.
- Keep test fixtures synthetic and dependency-free where practical.

## Pull requests

Explain the user-visible change, validation performed, known limitations, and any new assets or external dependencies. Include screenshots for visual changes. Complete the pull request template.
