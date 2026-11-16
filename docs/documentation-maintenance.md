# 📝 Documentation Maintenance Standard

## 1. Purpose

Documentation is part of the project's contributor interface. It must explain the actual code, provide useful procedures, and make limitations visible. Length alone is not quality: a long document that repeats generic statements or invents functionality is harmful.

## 2. Required update triggers

Review and update documentation whenever a change affects:
- User-visible page content or interaction.
- HTML structure, selectors, landmarks, or accessible names.
- CSS layout, breakpoints, typography, or overflow behaviour.
- JavaScript state or event handling.
- Tests, test commands, or CI workflows.
- Local asset paths, remote resources, or asset rights.
- Setup, deployment, hosting, or environment requirements.
- Security or privacy boundaries.
- Known limitations or future scope.
- Repository structure, filenames, or links.

## 3. Project-specific depth standard

A useful technical document should include the sections that fit its purpose:

1. **Purpose:** what the document covers.
2. **Current state:** what exists in the tracked repository.
3. **Implementation detail:** relevant files, selectors, commands, or behaviour.
4. **Workflow:** ordered steps or a diagram when useful.
5. **Edge cases:** failure modes and boundary conditions.
6. **Validation:** how a contributor can check the claims.
7. **Limitations:** what is not covered.
8. **Related references:** links to relevant project documents.

Do not force every section into a short metadata file or a source code file. Use detail where it improves understanding.

## 4. Documentation quality checklist

- [ ] Claims are supported by current source or repeatable behaviour.
- [ ] Implemented capabilities are separated from presentation-only UI.
- [ ] Future ideas are clearly marked as proposed.
- [ ] Commands are tested or accurately described.
- [ ] Relative links point to tracked files.
- [ ] Mermaid diagrams represent existing components.
- [ ] Project structure matches the current tree.
- [ ] Asset and licence statements are evidence-based.
- [ ] No secrets, tokens, or personal data are included.
- [ ] New pages are linked from the documentation hub.
- [ ] Related documents are updated when their assumptions change.

## 5. Status terminology

Use these labels consistently:

- **Implemented:** present in the current source and testable.
- **Partially implemented:** some behaviour exists, but a defined part remains incomplete.
- **Presentation-only:** visible UI without the expected application operation.
- **Not implemented:** no implementation exists.
- **Proposed:** future direction without a delivery commitment.
- **Known limitation:** a current constraint or defect.

## 6. Diagrams and tables

Use diagrams to explain relationships, decisions, or sequences that are difficult to understand in prose. Keep diagram nodes aligned with actual files and runtime components. Do not include a database, API, payment provider, or authentication service in a current-state diagram unless it exists in the source.

Tables should compare meaningful facts, not repeat paragraphs in another format.

## 7. Screenshots and images

Only include screenshots captured from the actual running project. Do not fabricate UI previews or use unrelated stock images as if they represented the application. Record screenshot context and update it after material UI changes. For project assets, maintain source and rights information.

## 8. Maintenance procedure

When a change is ready:
1. Identify affected documentation.
2. Update technical descriptions and diagrams.
3. Verify paths and commands.
4. Check the documentation hub and README.
5. Run the documentation workflow.
6. Review the diff for stale or contradictory statements.
7. Record material changes in the changelog.

## 9. Review cadence

Documentation should be reviewed with the implementation change and during release preparation. External asset assumptions and rights should be checked whenever an asset is added or replaced.
