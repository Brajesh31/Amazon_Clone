# Security Policy

## Project scope

Amazon Clone is a static educational storefront prototype. It does not implement accounts, cart persistence, checkout, payments, order management, or a backend service. It must not be used to collect customer data or presented as a production commerce platform.

## Safe development

- Do not place API keys, tokens, payment details, or other secrets in HTML, CSS, JavaScript, or public environment files.
- Do not trust client-side values for prices, inventory, identity, or payment state if a backend is introduced.
- Audit third-party image, font, and icon resources.
- Use only assets with documented permission or a suitable licence.
- Keep external resources on HTTPS and configure hosting security headers deliberately.
- Do not include private information in issue reports, tests, screenshots, or logs.

## Reporting

Do not publish sensitive details in a public issue. Report suspected vulnerabilities privately through the repository owner's GitHub profile contact method or GitHub private vulnerability reporting if available. Include affected paths, impact, safe reproduction steps, and a suggested mitigation.
