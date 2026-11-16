# 🔐 Security Policy

## 1. Project security scope

Amazon Clone is a static educational storefront prototype. Its current implementation consists of HTML, CSS, and browser-side JavaScript. It does not provide a backend, account system, authentication, cart persistence, checkout, payment processing, inventory management, order processing, or a customer database.

This repository must not be used to collect real customer credentials, addresses, payment information, or other sensitive personal data. Deploying the static page does not make it a secure commerce platform.

## 2. Supported project state

Security fixes should target the current default branch, `main`. The project has no formal long-term support branches or production service-level agreement. Contributors should identify the affected commit and browser/runtime context when reporting a defect.

## 3. Reporting a vulnerability

Please do not publish exploitable vulnerability details, secrets, personal data, or a working attack payload in a public issue.

Use GitHub private vulnerability reporting for this repository if it is enabled. Otherwise contact the repository owner through the contact method available on [@brajesh31](https://github.com/brajesh31).

A useful report includes:
- A concise description of the suspected weakness.
- Affected file, line, URL, or commit.
- Preconditions and safe reproduction steps.
- The realistic impact on this static application.
- Any suggested mitigation.
- Whether the issue is already publicly known.

Do not include real passwords, API tokens, payment data, or personal records in the report.

## 4. Current security boundaries

| Area | Current implementation | Security interpretation |
|---|---|---|
| Authentication | Not implemented | No user identity or session is established |
| Authorization | Not implemented | No protected server resource exists |
| Search input | Visual input only | No query is submitted to an application service |
| Cart | Static icon/link | No trusted cart or order state exists |
| Payments | Not implemented | No card data or payment credentials should be entered |
| Database | Not present | No persistent customer or product records are stored |
| External resources | Remote image, font, and icon URLs | Availability, content, and privacy depend on external hosts |
| Local images | Referenced directory is absent | Missing assets are a reliability and content-integrity issue |
| Hosting headers | Not configured in source | HTTPS and response headers must be configured by the hosting platform |

## 5. Secure contribution rules

- Never commit secrets, API keys, passwords, private keys, access tokens, or production credentials.
- Do not place secret values in HTML, CSS, or browser JavaScript.
- Treat all browser input as untrusted if it is processed in a future feature.
- Avoid unsafe HTML injection APIs for untrusted values.
- Do not use client-side calculations as authority for prices, discounts, inventory, or payment status.
- Do not add a database credential to a public `.env.example`.
- Use HTTPS for remote resources.
- Review third-party resources and their privacy implications.
- Confirm licence and permission before redistributing assets.
- Keep CI permissions to the minimum required for each workflow.
- Avoid adding telemetry, analytics, or session replay without a defined purpose and privacy review.

## 6. If the project gains backend capabilities

A real commerce service would need a separate threat model and security design. At minimum, assess:
- Authentication, session lifecycle, and account recovery.
- Server-side authorization on every protected operation.
- Input validation and output encoding.
- CSRF, XSS, injection, request forgery, and abuse protections as applicable.
- Rate limiting and account/payment abuse controls.
- Server-authoritative prices, discounts, taxes, and inventory.
- Payment provider tokenization and webhook signature verification.
- Idempotency and safe retry behaviour for transactions.
- Secrets management and rotation.
- Audit logging that avoids sensitive payloads.
- Data minimization, retention, deletion, and backup controls.
- Dependency, deployment, monitoring, and incident response processes.

These controls are not implemented by this repository today.

## 7. Disclosure and remediation

The maintainer will assess the report, determine whether it affects the current code, and decide on a correction or documented non-issue. Please allow a reasonable opportunity to investigate before public disclosure. No fixed response-time guarantee is offered for this educational project.

## 8. Further guidance

See [Security Review](docs/SECURITY-REVIEW.md), [Data Flow](docs/data-flow.md), [Deployment](docs/deployment.md), and [Troubleshooting](docs/troubleshooting.md) for related technical context.
