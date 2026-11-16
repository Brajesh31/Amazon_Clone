# ⚠️ Known Limitations and Technical Boundaries

## 1. Purpose

This document is a transparent record of the current prototype's boundaries. It distinguishes missing functionality from defects in functionality that does exist. Update it whenever the source changes.

## 2. Functional limitations

| Area | Current state | Practical consequence |
|---|---|---|
| Search | Visual input only | Visitors cannot submit a query or filter products |
| Account | Static sign-in/account labels | No identity, session, or account data |
| Orders | Static label | No order history or status |
| Cart | Static icon/link | No item state, quantity, persistence, or checkout |
| Product details | No product detail route | Cards do not open a complete product view |
| Categories | Non-interactive labels | No category route or filtered catalogue |
| Pricing | Static HTML text | Values are illustrative and not live |
| Inventory | Not implemented | No stock or availability information |
| Checkout | Not implemented | No purchase workflow |
| Payments | Not implemented | No transaction processing |
| Customer service | Static navigation label | No support workflow |

## 3. Architecture and data limitations

- No application API or backend.
- No database or persistent data store.
- No authentication or authorization.
- No server-side validation.
- No trusted price, discount, or inventory authority.
- No application logging, telemetry, or health endpoint.
- No user session or customer record.
- No package manifest, bundler, or framework runtime.

These are scope boundaries, not evidence that the corresponding systems are partially operational.

## 4. Asset limitations

The HTML references 31 unique local image paths under `imgs/`, but the tracked repository does not contain that directory. The resulting product/category image slots are unresolved in a clean checkout.

The page also depends on remote hero, logo, icon, and font resources. These can fail or change independently. Usage rights must be reviewed separately for each asset.

See [Asset Inventory](ASSET-INVENTORY.md).

## 5. Accessibility limitations

- Many images have empty alternative text and need context-sensitive review.
- Some visible controls are placeholders rather than functional actions.
- The carousel has native controls and updates `aria-hidden`, but it has not been demonstrated to meet a complete accessible carousel pattern.
- Contrast, reading order, zoom, and reflow require manual testing.
- Product rail discoverability for keyboard and assistive technology users needs review.

See [Accessibility Notes](ACCESSIBILITY.md) and [Accessibility Test Plan](accessibility-test-plan.md).

## 6. Security boundaries

The page does not process credentials or payments. That reduces the current application attack surface but does not remove risks from external resources, untrusted future DOM updates, asset licensing, or misleading commerce claims.

Hosting response headers are not defined by the source repository and must be reviewed at deployment time.

See [Security Review](SECURITY-REVIEW.md) and [Security Policy](../SECURITY.md).

## 7. Testing limitations

The JavaScript test suite uses a mock DOM. It verifies selected logic paths but cannot prove browser layout, actual device input, network availability, or screen-reader behaviour. No browser automation or visual regression suite is currently configured.

## 8. Claims that must not be made

Until the corresponding systems exist and are independently validated, do not claim:
- Production readiness.
- Secure checkout or payment processing.
- User account or order support.
- Live inventory or real product search.
- Persistent carts.
- Payment compliance.
- Formal accessibility or security certification.

## 9. How to close a limitation

A limitation is resolved only when:
1. The required implementation is committed.
2. Relevant tests and manual checks are performed.
3. Documentation is updated.
4. The limitation is removed or revised with evidence.
5. Any remaining constraints are stated clearly.
