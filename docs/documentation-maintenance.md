# 📝 Documentation Maintenance Standard

## Why this exists

Documentation is part of the project's interface to contributors. It must describe the repository as it exists, clearly identify gaps, and avoid implying functionality that is not present.

## Required update triggers

Update relevant docs when a change affects:

- A user-visible feature or interaction.
- HTML structure, CSS layout, or JavaScript selectors.
- Setup commands or supported tooling.
- Test behaviour or validation commands.
- External asset sources or local image inventory.
- Accessibility or security assumptions.
- Deployment and release procedures.
- Known limitations or planned scope.

## Documentation review checklist

- [ ] Claims are supported by source code or repeatable behaviour.
- [ ] Implemented capabilities are distinguished from proposals.
- [ ] Commands work from the repository root.
- [ ] Relative links resolve to tracked files.
- [ ] Mermaid diagrams reflect actual components.
- [ ] Project tree matches the current branch.
- [ ] External URLs are intentional and not presented as guaranteed.
- [ ] No credentials, tokens, or private data are included.
- [ ] No unlicensed imagery or third-party content is added.
- [ ] The documentation index links to new material.

## Writing guidance

Prefer concrete explanations, tables, examples, and diagrams where they improve understanding. Avoid filler, unverified metrics, generic claims about production readiness, and placeholder sections that provide no guidance.

## Scope labels

Use these distinctions consistently:

- **Implemented:** visible in tracked source and testable.
- **Partially implemented:** some behaviour exists but important requirements remain incomplete.
- **Not implemented:** no implementation exists in the current source.
- **Proposed:** a possible future direction without a delivery commitment.

## Review cadence

Review the documentation when functionality changes and during release preparation. Recheck external resource assumptions and asset rights whenever an asset is added or replaced.
