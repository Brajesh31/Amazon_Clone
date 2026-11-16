# ⚠️ Known Limitations and Technical Boundaries

This list records observed or explicitly documented limitations. It should be revised when source behaviour changes.

## 1. Functional limitations

- Search is a visual input only.
- Account and list labels are static.
- Cart is not stateful and has no persistence.
- Product/category links are placeholders.
- No product details or purchase action exists.
- No checkout, payment, order management, or refund process exists.
- Product text and promotional values are hard-coded in the HTML.

## 2. Data and infrastructure limitations

- No application API or backend.
- No database or persistence layer.
- No authentication or authorization.
- No server-side validation.
- No inventory or price authority.
- No monitoring or application logging layer.
- No application environment configuration is required by the current static implementation.

## 3. Asset limitations

- The HTML references 31 unique local image paths under `imgs/`.
- The tracked repository does not contain an `imgs/` directory.
- Remote hero, logo, icon, and font URLs may be unavailable, altered, or subject to independent usage terms.
- Image rights have not been established merely by the presence of a URL in the markup.

See [Asset Inventory](ASSET-INVENTORY.md).

## 4. Accessibility limitations to review

- Several images currently use empty alternative text. Verify whether each is decorative or informative before changing it.
- Some navigation and content regions are presentation-oriented rather than fully functional controls.
- The carousel has button labels and slide `aria-hidden` updates, but a full screen-reader announcement and reduced-motion strategy are not documented as implemented.
- Colour contrast and zoom/reflow behaviour require manual browser testing.

See [Accessibility](ACCESSIBILITY.md).

## 5. Security boundaries

The static page does not process credentials or payments. That reduces the current attack surface but does not remove risks from external resources, unsafe future DOM updates, third-party assets, or misleading claims that imply real transactions.

See [Security](SECURITY-REVIEW.md) and [SECURITY.md](../SECURITY.md).

## 6. What must not be claimed

Do not claim production readiness, secure checkout, account support, payment compliance, live inventory, real product search, persistent carts, or operational e-commerce capabilities until those systems are actually implemented and independently validated.
