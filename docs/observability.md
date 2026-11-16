# 🔎 Diagnostics and Observability

## Current status

The project has no application telemetry, structured logging service, error-reporting SDK, server metrics, or backend health endpoint. It runs as a static page in the visitor's browser.

Diagnostics currently rely on:

- Browser developer tools.
- Network panel for failed image, stylesheet, and font requests.
- Console output for JavaScript runtime errors.
- Node.js test output for automated behaviour checks.
- Python checker output for local HTML references.
- GitHub Actions job results for CI status.

## Troubleshooting sequence

1. Record the commit and browser version.
2. Reproduce with the static server from the repository root.
3. Inspect the console for script errors.
4. Inspect the network panel for missing local files or failed third-party requests.
5. Run the automated checks.
6. Compare behaviour against the current tests and documentation.
7. Record any unresolved issue with steps to reproduce.

## Privacy

Do not add analytics or session replay by default. Any future telemetry should have a defined purpose, data minimization, retention policy, disclosure, and appropriate consent/legal review. Never collect passwords, payment data, or sensitive user input for debugging.

## Future option

A browser error-reporting service may be considered only when there is a deployed application and a clear operational need. The static prototype does not currently justify that dependency.
