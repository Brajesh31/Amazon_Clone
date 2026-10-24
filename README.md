# Amazon Clone

A static Amazon-inspired storefront interface built with plain HTML, CSS, and JavaScript. The project demonstrates a responsive marketplace layout with a navigation bar, search presentation, hero carousel, product category cards, horizontal product rails, and simple wheel-based scrolling.

> This is an educational frontend prototype. It is not affiliated with Amazon and does not implement authentication, checkout, product APIs, payments, or order management.

## Features

- Amazon-style primary and secondary navigation.
- Hero banner carousel controlled by previous and next buttons.
- Category cards and horizontal product sections.
- Static product cards with promotional labels and prices.
- Wheel-to-horizontal-scroll behavior for product rails.
- Responsive layout rules in [`amazone.css`](./amazone.css).

## Project structure

```text
.
├── index.html       # Page markup and product content
├── amazone.css      # Layout, colors, typography, and responsive styling
├── amazone.js       # Carousel and product-rail interactions
└── imgs/            # Expected local product images referenced by index.html
```

## Run locally

No build step or package installation is required. Serve the directory from its root so relative image paths resolve:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/> in a browser. A local web server is preferred over opening `index.html` directly because browser file-security rules can affect asset loading.

## Current limitations

- Product data and prices are hard-coded in `index.html`.
- The search field, account links, cart, and navigation links are visual only.
- The carousel depends on JavaScript and assumes the expected image elements exist.
- Some images and icons are loaded from third-party CDNs; local `imgs/` assets must be present for the product sections.
- There is no persistence, API, authentication, payment processing, or server-side validation.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the review and change process. For design or accessibility changes, include screenshots and test the page at narrow and wide viewport sizes.

## License

Released under the MIT License. See [`LICENSE`](./LICENSE).

Last updated: 2026-10-24 05:28 UTC
