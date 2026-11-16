# 🔐 Security Review and Threat Boundaries

## 1. Review purpose

This is a repository-level review of the current static frontend. It is not a penetration test, threat-model certification, compliance assessment, or guarantee that deployment infrastructure is secure.

The review distinguishes risks that exist in the current code from controls that would only become relevant if the project later gains a backend.

## 2. System boundary

Current components:
- A browser-loaded HTML document.
- A local stylesheet.
- A browser-side JavaScript file.
- Local image paths, currently unresolved in the tracked tree.
- Remote images, fonts, and icon resources.

Not present:
- Application API.
- Authentication or session service.
- Database.
- Cart or order service.
- Payment provider integration.
- User profile or customer record storage.

## 3. Threat and control matrix

| Area | Current observation | Risk / consequence | Recommended control |
|---|---|---|---|
| Secrets | No application credentials required | Future developers may mistakenly commit secrets | Keep secrets out of client code and public examples |
| Third-party resources | Multiple remote hosts are used | Availability, content, tracking, and policy changes are outside project control | Inventory hosts, review necessity, prefer stable HTTPS resources |
| Local assets | 31 unique local paths are unresolved | Broken rendering and potential unsafe asset substitution | Add reviewed, licensed assets and validate references |
| Search field | Input is not processed | No current search injection path through an app API | If implemented, validate input and encode output |
| Placeholder links | Some controls are presentation-only | Users may mistake non-functional UI for a real action | Use accurate labels and only expose real actions as controls |
| Product prices | Static strings in HTML | Values are not authoritative and can be edited by a visitor | Never use browser values as transaction authority |
| Identity | No authentication | No identity assurance or access control | Add a separate identity design before user data exists |
| Payments | No payment flow | No transaction security exists | Use a reputable provider and server-side verification in a future system |
| Database | No database | No current database exposure | Do not introduce browser-side privileged database access |
| Hosting | No hosting policy in source | Headers and TLS depend on deployment configuration | Configure HTTPS and response headers at the host |
| Dependencies | No npm runtime dependency graph | Third-party CSS/font resources remain external dependencies | Review external providers and update policy |
| CI | Workflows run repository checks | Overbroad workflow permissions could expose repository write access | Keep permissions minimal and pin/review actions |

## 4. External resource considerations

The page loads third-party visual resources. Before deployment, review:
- Whether each resource is necessary.
- Whether it is served over HTTPS.
- Whether the provider's usage terms permit the intended use.
- Whether the request exposes visitor network metadata to the provider.
- Whether the page remains usable when the host is unavailable.
- Whether a local approved asset is a better option.

A Content Security Policy should be designed from a verified resource inventory. Do not paste a generic policy that blocks required resources or grants broad wildcards.

## 5. Browser-side code rules

If new functionality processes user-controlled content:
- Treat input as untrusted.
- Prefer safe DOM APIs such as `textContent` for text.
- Avoid concatenating untrusted strings into HTML.
- Validate data at the boundary where it enters the application.
- Keep client-side checks for user experience, not security authority.
- Do not expose privileged tokens or credentials.

## 6. Future commerce security requirements

A real commerce application would require a separate threat model covering:
- Identity proofing and account recovery.
- Session security and authorization.
- Product and inventory integrity.
- Server-side price and discount calculation.
- Cart and order consistency.
- Payment tokenization and provider webhook verification.
- Idempotency and duplicate transaction prevention.
- Abuse, bot, and rate-limit controls.
- Privacy, retention, and deletion.
- Secure secrets storage and rotation.
- Audit logs, monitoring, backups, and incident response.

None of these services is currently implemented.

## 7. Security review checklist for changes

- [ ] No secrets or personal data are committed.
- [ ] External resources are necessary and use HTTPS.
- [ ] New assets have documented rights.
- [ ] User-controlled strings are handled safely.
- [ ] No unsafe HTML injection is introduced.
- [ ] No client-side value is treated as trusted transaction data.
- [ ] Workflow permissions are minimal.
- [ ] Documentation accurately describes security boundaries.
- [ ] Any new integration has a documented threat and privacy review.

## 8. Reporting

Use [SECURITY.md](../SECURITY.md) for private vulnerability reporting. Avoid public disclosure of exploitable details or sensitive values.
