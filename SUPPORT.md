# 🆘 Support and Troubleshooting

This repository is an educational static storefront prototype. Support requests should focus on reproducible problems in the HTML, CSS, JavaScript, tests, documentation, or static hosting setup.

## 1. Start with the project guides

Before opening a support issue, review:

- [README](README.md) for project scope and quick start.
- [Installation](docs/installation.md) for local preview.
- [FAQ](docs/faq.md) for common questions.
- [Troubleshooting](docs/troubleshooting.md) for known failure modes.
- [Asset Inventory](docs/ASSET-INVENTORY.md) for unresolved image paths.
- [Testing Strategy](docs/testing-strategy.md) for local checks.

## 2. Reproduce locally

Run from the repository root:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/` and reproduce the issue. For automated validation, run:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

The project does not require npm installation, an API server, a database, or environment secrets.

## 3. Information to include

A high-quality support request contains:

| Detail | What to provide |
|---|---|
| Summary | One sentence describing the problem |
| Environment | Browser, browser version, OS, and device class |
| Revision | Branch and commit SHA if known |
| Setup | Exact local server command or hosting context |
| Steps | Numbered steps that reliably reproduce the issue |
| Expected result | What should happen |
| Actual result | What happens instead |
| Evidence | Sanitized console/network output or screenshot |
| Scope | Whether the issue is reproducible locally and after deployment |

Remove access tokens, private URLs, personal data, and any sensitive browser information before sharing logs or screenshots.

## 4. Known limitation: missing local images

The current source references a local `imgs/` directory that is not tracked in the repository. Broken product/category image slots are therefore a known repository issue, not necessarily a local installation problem. Consult [Asset Inventory](docs/ASSET-INVENTORY.md).

## 5. What this project does not support

This repository does not provide customer support for real purchases, account access, payments, delivery, refunds, or product availability. The storefront is not connected to Amazon and cannot access Amazon customer or order systems.

## 6. Security concerns

Do not post exploit details or secrets publicly. Follow [SECURITY.md](SECURITY.md) for private vulnerability reporting.

## 7. Requesting a feature

Use the GitHub feature request form. Explain the user problem, the expected behaviour, whether the change remains frontend-only, and how it can be tested. A proposed feature is not a commitment to implement it.
