# 🛠️ Maintenance and Operations Guide

## 1. Maintenance scope

The current application is static. Operational work is therefore focused on source integrity, static hosting, external resource availability, asset integrity, and automated checks rather than server administration.

## 2. Local validation routine

Run after editing HTML, CSS, JavaScript, tests, or local asset references:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Also serve the page and inspect it in a browser:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

## 3. Change review checklist

- [ ] Confirm only intended files changed.
- [ ] Confirm no existing assets or project files were removed unintentionally.
- [ ] Check all local image and stylesheet/script paths.
- [ ] Confirm external resources still load.
- [ ] Run JavaScript syntax validation.
- [ ] Run the Node.js tests.
- [ ] Run the HTML checker.
- [ ] Review desktop and mobile layouts.
- [ ] Check keyboard focus and accessible names.
- [ ] Check browser console errors.
- [ ] Update relevant docs and the changelog.

## 4. External resource maintenance

External images, icons, and fonts can be unavailable or changed independently. If replacing an external resource:

1. Identify the page elements that depend on it.
2. Verify that the replacement can legally be used.
3. Prefer stable, documented resource locations.
4. Test loading and layout when the resource fails.
5. Update [Asset Inventory](ASSET-INVENTORY.md).

## 5. Release process

Use the repository's [Release Checklist](../RELEASE-CHECKLIST.md). Do not publish a release with known broken image references without explicitly documenting that limitation.

## 6. Backup and recovery

The canonical source of truth is the Git repository. Use normal Git history and repository backup practices. Since the current project does not hold user or transaction data, database backup and payment recovery procedures do not apply.

## 7. Incident response

For a static-site problem:

1. Record the affected URL, browser, device, and approximate time.
2. Capture console and network errors without exposing private data.
3. Identify whether the failure is in repository content, hosting configuration, or an external asset host.
4. Reproduce locally using the same commit.
5. Fix and test the smallest relevant change.
6. Document any unresolved issue in the repository.

Security concerns should follow [SECURITY.md](../SECURITY.md).
