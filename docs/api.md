# API and Integrations

## Current API status

There is no API client or backend in this repository. The static page does not send requests to an application service.

| UI area | Current behaviour |
| --- | --- |
| Search field | Visual input only; no search submission or filtering |
| Account and lists | Static text; no identity provider |
| Cart | Static link and icon; no cart state or persistence |
| Product/category links | Placeholder anchors |
| Hero carousel | Local browser-only image selection |
| Product rails | Browser-only horizontal scrolling |

## External resources

The HTML imports a stylesheet and font/icon resources from external hosts and uses remote hero/banner imagery. These are static resource requests, not application APIs.

## Future backend work

A real commerce application would require explicit API contracts for catalog retrieval, identity, cart operations, inventory, order management, and payment provider integration. Authorization, validation, pricing integrity, idempotency, auditability, and privacy must be designed server-side. Never put secret keys or payment credentials into browser JavaScript.
