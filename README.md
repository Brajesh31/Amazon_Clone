# Amazon Clone

A static Amazon-inspired storefront interface built with plain HTML, CSS, and JavaScript. It demonstrates a marketplace-style navigation bar, hero carousel, category cards, product rails, promotional labels, and horizontal scrolling.

> This is an educational frontend prototype. It is not affiliated with Amazon. It does not implement authentication, live product search, cart persistence, checkout, payment processing, or order management.

## Features
- Marketplace-style primary and secondary navigation.
- Hero banner carousel with previous and next controls.
- Static category and product sections.
- Horizontal product rails with wheel-based scrolling.
- Responsive styling in `amazone.css`.

## Technology
- HTML5
- CSS3
- Vanilla JavaScript
- Font Awesome stylesheet loaded from a CDN
- Remote image assets and local image paths referenced by the page

## Project files
```text
.
├── index.html
├── amazone.css
├── amazone.js
├── docs/
└── .github/
```

## Run locally
No package installation or build step is required. Serve the repository root:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/>.

## Important asset note
The current tracked repository tree does not contain an `imgs/` directory, while `index.html` references multiple files under `imgs/`. Those product and category images will not load until the intended assets are added. The hero images and several icons are remote URLs and depend on third-party availability. Do not add copyrighted or unlicensed assets.

## Current limitations
- Product data and prices are hard-coded in `index.html`.
- Search, account, cart, and category links are visual only.
- No backend, API, database, authentication, checkout, or persistence exists.
- The carousel expects its hero image and control elements to be present.
- Remote image and icon providers can change or block assets.

## Documentation
- [Installation](docs/installation.md)
- [Architecture](docs/architecture.md)
- [Development](docs/development.md)
- [API status](docs/api.md)
- [Database status](docs/database.md)
- [Deployment](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Quality checks](docs/QA.md)

## Contributing and security
Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Report security concerns privately as described in [SECURITY.md](SECURITY.md).

## License
MIT. See [LICENSE](LICENSE).

Last updated: 2026-11-13 19:23 UTC
