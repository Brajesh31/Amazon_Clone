# 🛍️ Project Overview

## 1. Purpose

Amazon Clone is an **Amazon-inspired static storefront prototype**. It recreates selected visual patterns of an online marketplace using a single HTML page, a stylesheet, and browser-native JavaScript.

The project is useful for studying:

- Structuring a multi-section storefront with semantic HTML.
- Building responsive layouts with CSS Flexbox and media queries.
- Implementing a lightweight image carousel without a framework.
- Creating horizontally scrollable product rails.
- Validating browser behaviour with Node.js's built-in test runner.

This is a learning and interface demonstration project, not a production commerce application.

## 2. Problem statement

A developer learning frontend fundamentals needs a concrete interface that combines navigation, promotional content, category groupings, product imagery, responsive layout, and small interactions. The prototype brings these patterns together without requiring a package manager, application framework, build system, API, or database.

## 3. Proposed solution

The page is assembled from three core browser resources:

| Resource | Role |
|---|---|
| `index.html` | Defines page content, navigation, carousel controls, category cards, product rails, and footer |
| `amazone.css` | Defines presentation, layout, typography, colours, and responsive breakpoints |
| `amazone.js` | Controls hero slide visibility and converts vertical wheel movement into horizontal product-rail scrolling |

The supporting test and validation scripts provide repeatable checks without adding runtime dependencies.

## 4. Current capabilities

- Two-level marketplace-style navigation presentation.
- Five-image hero carousel with previous and next controls.
- Static category and promotional cards.
- Horizontal product collections.
- Wheel-to-horizontal scrolling on product rails.
- Responsive layout adjustments for narrower viewports.
- Automated tests for carousel and rail interaction behaviour.
- HTML/local-reference validation.

## 5. Explicit non-goals

The current implementation does not provide:

- Product search or filtering.
- Account registration, sign-in, or sessions.
- A functional cart or wishlist.
- Product detail pages or working product links.
- Checkout, payment processing, tax, shipping, or refunds.
- Inventory, order management, or customer service workflows.
- Application APIs, database persistence, or server-side validation.

Do not describe the prototype as a complete e-commerce platform.

## 6. Technology profile

| Layer | Technology | Use |
|---|---|---|
| Content | HTML5 | Page structure and controls |
| Presentation | CSS3 | Responsive visual layout |
| Interaction | Vanilla JavaScript | Carousel and product rails |
| Tests | Node.js built-in test runner | Behaviour regression tests |
| HTML validation | Python standard library | Local markup and asset-reference checks |
| Static serving | Python HTTP server or equivalent | Local preview |

There is no package manifest or framework runtime.

## 7. Repository health observations

The repository includes automated tests, CI, contribution guidance, security guidance, accessibility notes, an asset inventory, and release documentation.

A material presentation issue remains: `index.html` references image paths under `imgs/`, but the tracked repository tree does not contain that directory. A clean checkout therefore cannot display those local image resources. See [Asset Inventory](ASSET-INVENTORY.md).

## 8. Intended audience

- Frontend learners.
- Contributors practising HTML, CSS, and vanilla JavaScript.
- Reviewers assessing browser-side UI patterns.
- Developers studying lightweight static prototypes.

## 9. Product identity and trademark note

The project is an independent educational interface inspired by a familiar marketplace layout. It is not affiliated with, sponsored by, or endorsed by Amazon. Third-party brand assets and retailer imagery should be used only where the contributor has appropriate rights.
