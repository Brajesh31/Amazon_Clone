# 🚢 Release and Deployment Readiness Checklist

Use this checklist before publishing a tagged release or deploying a reviewed revision of the static storefront. It is intentionally explicit about evidence and known limitations.

## 1. Scope and release identity

- [ ] Confirm the intended commit and branch.
- [ ] Review the complete diff, including generated or binary files.
- [ ] Confirm the release description matches implemented behaviour.
- [ ] Confirm the project is still accurately described as a static educational prototype.
- [ ] Confirm no placeholder UI is described as a real search, account, cart, checkout, or payment feature.
- [ ] Update `CHANGELOG.md` with actual changes and date.

## 2. Source integrity

- [ ] Confirm `index.html`, `amazone.css`, and `amazone.js` exist.
- [ ] Confirm script selectors still match the page markup.
- [ ] Confirm no unrelated source files or assets were removed.
- [ ] Confirm there are no accidental credentials, tokens, or personal data.
- [ ] Confirm all changed files have a clear purpose.
- [ ] Confirm documentation matches the implementation.

## 3. Automated validation

Run from the repository root:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
python scripts/check_docs.py
```

- [ ] JavaScript syntax validation passes.
- [ ] Every JavaScript test passes.
- [ ] HTML structure validation passes.
- [ ] Every missing-reference warning is reviewed and classified.
- [ ] Documentation checks pass in GitHub Actions.
- [ ] Main CI workflow passes for the release commit.

A warning about missing local images is not evidence that those files exist. Resolve the issue or explicitly retain it as a known release limitation.

## 4. Browser verification

- [ ] Serve the site from the repository root.
- [ ] Confirm stylesheet and script load successfully.
- [ ] Test previous and next carousel controls.
- [ ] Test wrap-around from first to last and last to first slide.
- [ ] Test vertical wheel movement over each product rail.
- [ ] Test native horizontal trackpad movement.
- [ ] Confirm page scrolling works at rail boundaries.
- [ ] Inspect browser console and network failures.
- [ ] Review desktop, tablet, and mobile widths.
- [ ] Test keyboard focus and control activation.
- [ ] Review image alternative text and visible labels.
- [ ] Test 200% zoom and narrow viewport reflow.

## 5. Asset and content review

- [ ] Verify all local assets exist at their referenced paths.
- [ ] Verify each distributed image/font/icon has a documented licence or permission.
- [ ] Remove or replace unapproved third-party assets.
- [ ] Check remote resources over HTTPS.
- [ ] Confirm external resources have appropriate fallbacks where practical.
- [ ] Ensure product names, prices, and discounts are clearly illustrative unless verified data is implemented.
- [ ] Keep the non-affiliation statement visible and accurate.

## 6. Documentation and governance

- [ ] Update README and documentation hub.
- [ ] Update project tree if paths changed.
- [ ] Update architecture and workflow diagrams if behaviour changed.
- [ ] Update API/database status if integrations were added.
- [ ] Update accessibility and security notes.
- [ ] Update troubleshooting and FAQ entries for new known issues.
- [ ] Confirm issue forms and pull request template remain accurate.
- [ ] Confirm the licence file is present and unchanged unless a deliberate legal decision was made.

## 7. Static hosting verification

- [ ] Publish the correct repository root.
- [ ] Confirm the deployed document root and relative asset paths.
- [ ] Confirm HTTPS is enabled.
- [ ] Check the deployed page on its actual domain and base path.
- [ ] Review cache behaviour for HTML and static assets.
- [ ] Inventory required external hosts before setting a Content Security Policy.
- [ ] Confirm no backend secrets or unnecessary environment variables are configured.

## 8. Final release decision

- [ ] Record the commit SHA and deployment target.
- [ ] Record any known limitations and why they are accepted.
- [ ] Do not claim production commerce readiness.
- [ ] Do not claim accessibility or security certification without a corresponding audit.
- [ ] Publish release notes that distinguish completed work from future scope.
