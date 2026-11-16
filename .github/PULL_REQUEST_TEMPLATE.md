# 🔀 Pull Request

Thank you for contributing. Keep the change focused and describe its observable effect.

## 1. Summary

Explain the problem, why it matters, and what this pull request changes.

## 2. Change category

- [ ] Bug fix
- [ ] Frontend interaction
- [ ] Visual or responsive improvement
- [ ] Accessibility improvement
- [ ] Documentation
- [ ] Tests or CI
- [ ] Asset replacement
- [ ] Maintenance or configuration

## 3. Implementation details

Describe the main files changed, important decisions, and trade-offs. Mention whether the change affects HTML selectors, CSS breakpoints, JavaScript state, or external resources.

## 4. Behaviour and scope

- [ ] The change is implemented, not only represented by placeholder UI.
- [ ] Any future or incomplete capability is clearly identified.
- [ ] No unrequested backend, database, or framework was introduced.
- [ ] Existing useful files and assets were preserved.

## 5. Validation performed

- [ ] `node --check amazone.js`
- [ ] `node --test tests/*.test.js`
- [ ] `python scripts/check_html.py`
- [ ] `python scripts/check_docs.py` (when documentation changes)
- [ ] Served the site from the repository root.
- [ ] Tested carousel controls and wrap-around where relevant.
- [ ] Tested product rail scrolling and boundaries where relevant.
- [ ] Reviewed narrow and wide viewport layouts.
- [ ] Checked keyboard focus and accessible names.
- [ ] Inspected browser console and network errors.
- [ ] Confirmed GitHub Actions results.

Only mark checks that were actually performed.

## 6. Assets and external resources

List new or changed images, fonts, icons, and external hosts. Include source, licence/permission, attribution requirements, and alternative-text decisions.

## 7. Documentation

- [ ] README updated where needed.
- [ ] Documentation hub and project tree updated where needed.
- [ ] Architecture/workflow diagrams updated where behaviour changed.
- [ ] Asset inventory updated where media changed.
- [ ] Security/accessibility notes updated where relevant.
- [ ] Changelog updated for material changes.

## 8. Screenshots or evidence

For visual changes, include screenshots captured from the actual running project. Do not fabricate previews. Remove personal or sensitive information.

## 9. Known limitations and follow-up

List unresolved defects, test gaps, and follow-up work. Include the known missing local image references if the change does not resolve them.

## 10. Reviewer notes

Highlight the areas that need careful review, including risky assumptions or compatibility concerns.
