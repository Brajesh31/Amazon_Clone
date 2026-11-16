# 🛍️ Project Overview

## 1. Project identity

**Amazon Clone** is an independent, Amazon-inspired static storefront prototype. It uses a single HTML document, a CSS stylesheet, and browser-native JavaScript to demonstrate selected marketplace interface patterns.

It is an educational frontend project. It is not affiliated with, sponsored by, or endorsed by Amazon, and it is not a functioning online store.

## 2. Problem statement

Frontend learners often need to practise several related interface skills in one coherent example: navigation, promotional content, category cards, product collections, responsive layout, and small interactive behaviours. A static storefront provides a practical setting for those skills without requiring an API, database, build pipeline, or framework.

The challenge is to keep the example clear and testable while avoiding the false impression that a visually complete marketplace layout implements the business systems behind real commerce.

## 3. Project objectives

- Demonstrate a structured marketplace-style page using HTML5.
- Use CSS for layout, typography, visual hierarchy, and responsive breakpoints.
- Implement a small hero carousel with browser-native JavaScript.
- Support horizontal product browsing with native overflow and wheel interaction.
- Keep the runtime dependency-light.
- Provide tests and validation scripts for the implemented behaviour.
- Document missing resources and unimplemented controls accurately.

## 4. Proposed solution and file roles

| Resource | Role |
|---|---|
| `index.html` | Navigation, hero area, category cards, product rails, deal cards, and footer |
| `amazone.css` | Global styling, layout, card presentation, rail overflow, and responsive rules |
| `amazone.js` | Carousel slide selection and vertical-wheel-to-horizontal-rail behaviour |
| `tests/amazone.test.js` | Mock-DOM tests for the JavaScript interactions |
| `scripts/check_html.py` | Basic HTML structure and local-reference validation |
| `.github/workflows/ci.yml` | Automated syntax, test, and HTML validation |

## 5. Implemented capabilities

- Marketplace-style top navigation and secondary navigation presentation.
- Five-image hero carousel with previous and next controls.
- Static category and promotional cards.
- Horizontally scrollable product collections.
- Vertical wheel translation for product rails when movement is possible.
- Responsive CSS adjustments at 900px, 600px, and 380px.
- Dependency-free JavaScript behaviour tests.
- Basic HTML and local-reference checker.

## 6. Explicit non-goals

The current implementation does not provide:
- Product search or filtering.
- User registration, sign-in, or sessions.
- Functional cart or wishlist state.
- Product detail pages or working product links.
- Checkout, payments, tax, shipping, or refunds.
- Inventory, order management, or customer service workflows.
- Application APIs, database persistence, or server-side validation.

The presence of a search field or cart icon is not evidence that the corresponding system exists.

## 7. Technology profile

| Layer | Technology | Purpose |
|---|---|---|
| Content | HTML5 | Page structure |
| Presentation | CSS3 | Layout and responsive styling |
| Interaction | Vanilla JavaScript | Carousel and product rails |
| Tests | Node.js built-in test runner | Behaviour regression checks |
| HTML validation | Python standard library | Structure and path checks |
| Preview | Python HTTP server or equivalent | Local static serving |

There is no package manifest, frontend framework, bundler, or runtime backend.

## 8. Repository health and known issues

The repository includes tests, CI, contribution and security guidance, issue templates, accessibility notes, and technical documentation.

A material visual issue remains: `index.html` references 31 unique local image paths under `imgs/`, but the tracked repository does not contain that directory. Those local image requests cannot resolve in a clean checkout. Remote hero, logo, icon, and font resources also depend on third-party hosts.

## 9. Intended audience

- Students and frontend learners.
- Contributors practising HTML, CSS, and vanilla JavaScript.
- Reviewers assessing a small browser-only project.
- Developers studying lightweight static prototypes and testable DOM behaviour.

## 10. Success criteria

The project is successful as a learning prototype when its documented interactions work, the page is understandable and responsive, its assets have clear rights, its controls are not misleading, and its tests provide useful regression coverage. It does not need a backend to meet that educational goal.

## 11. Identity and asset rights

The project is independent. Any third-party logo, retailer image, font, or icon must be reviewed under its own licence or permission terms. The repository's software licence does not automatically grant rights to external brand assets.
