# 🔌 API and Integration Status

## 1. Current status

There is no application API client, server endpoint, backend service, or remote product data integration in this repository. The static page is rendered by the browser from repository files and remote visual resources.

This is an explicit architectural boundary, not an undocumented missing package.

## 2. UI capability map

| UI element | Current behaviour | Network/application API |
|---|---|---|
| Search field | Accepts text in the browser | None |
| Account and lists | Displays static labels | None |
| Orders | Displays static label | None |
| Cart | Displays icon and static link | None |
| Product/category links | Placeholder anchors | None |
| Hero carousel | Changes local slide visibility | None |
| Product rails | Changes browser element scroll position | None |
| Fonts/icons/images | Browser requests remote static resources | Static resource requests only |

A remote image request is not an application API. It does not provide product catalogue, user, cart, or order functionality.

## 3. Current data ownership

The HTML document is the source of truth for the visible product/category text and illustrative prices. The browser does not retrieve an authoritative catalogue, validate availability, or persist user choices.

There are no API keys, service credentials, authentication tokens, or environment variables required by the current application.

## 4. Proposed API domains for a future system

If the project is deliberately expanded into a real application, requirements may include the following domains. These are conceptual areas only, not current endpoints.

| Domain | Possible responsibility | Required trust boundary |
|---|---|---|
| Catalog | Product descriptions, categories, media | Server-controlled product records |
| Search | Query processing and result ranking | Input validation and abuse controls |
| Identity | Sign-in, session, account recovery | Secure authentication and authorization |
| Cart | Cart items and quantities | Server-side ownership and validation |
| Pricing | Prices, discounts, tax, totals | Server-authoritative calculations |
| Inventory | Stock and reservation state | Consistency and concurrency control |
| Orders | Order creation and lifecycle | Idempotency and authorization |
| Payments | Provider token and payment status | Provider integration and server verification |

## 5. API contract requirements

Before implementing any endpoint, define:
- Business purpose and owning service.
- Request and response schemas.
- Required and optional fields.
- Authentication and authorization rules.
- Validation and error response format.
- Rate limits and abuse controls.
- Idempotency for retryable operations.
- Logging and sensitive-data redaction.
- Versioning and backward compatibility.
- Automated tests and operational monitoring.

## 6. Security requirements

Never put secret keys, database credentials, payment secrets, or privileged access tokens in browser JavaScript or public HTML. Client-side validation improves usability but does not establish trust. The server must independently validate every security-sensitive operation.

## 7. Related documentation

See [Architecture](architecture.md), [Data Flow](data-flow.md), [Database](database.md), [Security Review](SECURITY-REVIEW.md), and [Future Scope](future-scope.md).
