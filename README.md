# Amazon Clone

An **Amazon-inspired static storefront prototype** built with HTML, CSS, and vanilla JavaScript. It demonstrates a marketplace-style navigation layout, promotional hero carousel, category cards, product rails, and deal cards.

This repository is a frontend learning project. It is not affiliated with or endorsed by Amazon. It is **not a functioning online store**: search, account, cart, product links, checkout, payment processing, and order management are not implemented.

## Features

- Two-level marketplace-style navigation layout.
- Hero image carousel with previous and next controls.
- Static category cards and product sections.
- Horizontal product rails with vertical-wheel support.
- Responsive CSS presentation.
- Dependency-free JavaScript tests for carousel and product-rail behaviour.

## Technology

| Area | Technology |
| --- | --- |
| Markup | HTML5 |
| Styling | CSS3 |
| Browser behaviour | Vanilla JavaScript |
| Tests | Node.js built-in test runner |
| HTML validation | Python standard library |
| External resources | Third-party image, font, and icon URLs |

No npm package installation, bundler, frontend framework, or backend is required.

## Project structure

```text
.
├── index.html
├── amazone.css
├── amazone.js
├── tests/
│   └── amazone.test.js
├── scripts/
│   └── check_html.py
├── docs/
│   ├── ACCESSIBILITY.md
│   ├── ASSET-INVENTORY.md
│   ├── SECURITY-REVIEW.md
│   └── ...
└── .github/
    └── workflows/
```

## Run locally

Use Python 3 from the repository root:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/>.

## Run automated checks

Node.js 20 or newer and Python 3 are required for the test commands:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

The HTML checker reports absent local image paths as warnings. The current Git repository does not contain the referenced `imgs/` directory, so category and product image slots remain broken in a clean checkout.

## Known limitations

- The HTML contains 47 references across 31 unique local image paths under `imgs/`, but those files are not tracked.
- The hero carousel uses remote images that can disappear or change.
- Search, account, cart, categories, and product actions are visual placeholders.
- Product content and promotional values are hard-coded in HTML.
- There is no API, database, authentication, server-side validation, or persistence.
- This is not an e-commerce, checkout, or payment implementation.
- Third-party logos, imagery, fonts, and icons require separate usage-rights review.

See the [asset inventory](docs/ASSET-INVENTORY.md), [architecture](docs/architecture.md), [API status](docs/api.md), [database status](docs/database.md), [accessibility notes](docs/ACCESSIBILITY.md), and [security review](docs/SECURITY-REVIEW.md).

## Documentation

- [Installation](docs/installation.md)
- [Development](docs/development.md)
- [Architecture](docs/architecture.md)
- [Asset inventory](docs/ASSET-INVENTORY.md)
- [Accessibility](docs/ACCESSIBILITY.md)
- [API and integrations](docs/api.md)
- [Database](docs/database.md)
- [Deployment](docs/deployment.md)
- [Testing and QA](docs/QA.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Report concerns privately according to [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).