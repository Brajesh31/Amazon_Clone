# 🛠️ Maintenance and Operations Guide

## 1. Operational model

The current application is a static site. Maintenance focuses on source integrity, browser compatibility, static hosting, external resource availability, asset rights, and repeatable automated checks. Server administration, database maintenance, and payment operations are outside the current project scope.

## 2. Routine validation

After changing HTML, CSS, JavaScript, tests, or local asset references, run:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Then serve the page:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/` and inspect the browser console and network panel.

## 3. Change review checklist

- [ ] Confirm the working branch and base commit.
- [ ] Review the complete diff.
- [ ] Confirm no useful files or assets were removed unintentionally.
- [ ] Check local image, stylesheet, and script references.
- [ ] Verify remote resource URLs are still intentional.
- [ ] Run JavaScript syntax validation.
- [ ] Run all Node.js tests.
- [ ] Run the Python HTML checker.
- [ ] Review desktop and mobile layouts.
- [ ] Check keyboard focus, accessible names, and reading order.
- [ ] Inspect console and network errors.
- [ ] Update the changelog and relevant documentation.

## 4. Asset maintenance

When adding or replacing a visual asset:
1. Identify every UI element that uses it.
2. Verify the file can be redistributed publicly.
3. Record the original source and licence or permission.
4. Use a predictable local path.
5. Review dimensions, compression, crop, and aspect ratio.
6. Write meaningful alternative text or confirm the image is decorative.
7. Update [Asset Inventory](ASSET-INVENTORY.md).
8. Run the HTML checker and inspect the page.

Do not download images based only on opaque retailer-style filenames.

## 5. External resource maintenance

Remote images, fonts, and icons can be unavailable or modified without a repository commit. If replacing one:
- Document the affected element.
- Review the provider and usage terms.
- Prefer stable HTTPS resource URLs.
- Consider a local licensed alternative.
- Check layout when the request fails.
- Update the asset inventory and security review.

## 6. CI maintenance

The main CI workflow validates required files, JavaScript syntax, behaviour tests, and HTML/local references. The documentation workflow checks basic documentation structure. Review workflow permissions and action versions periodically.

Do not add write permissions to a workflow unless it has a documented requirement. Do not make CI green by hiding meaningful validation failures.

## 7. Static deployment operations

Use the repository root as the static document root. Confirm HTTPS, correct content types, relative asset paths, cache policy, and hosting response headers. The deployment provider controls those settings.

See [Deployment](deployment.md).

## 8. Backup and recovery

Git history is the canonical source of truth for the repository. Use repository backup and access-control practices appropriate to the owner. The current static project does not hold customer or transaction data, so database backup and payment recovery procedures do not apply.

## 9. Incident handling

For a reported static-site failure:
1. Record the public URL, commit, browser, device, and time.
2. Capture sanitized console and network errors.
3. Determine whether the issue is in source, deployment configuration, or an external host.
4. Reproduce locally using the same commit.
5. Make the smallest appropriate correction.
6. Run automated and manual checks.
7. Document the cause and remaining risk.

For security concerns, follow [SECURITY.md](../SECURITY.md).

## 10. Maintenance cadence

Review dependencies and GitHub Actions periodically, check external resources during release preparation, and update docs whenever implementation behaviour changes. Do not create a recurring operational process that the static project does not need.
