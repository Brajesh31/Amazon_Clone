# 🚀 Static Deployment Guide

## 1. Deployment model

The current repository is a static website. The deployable runtime consists of the HTML document, CSS stylesheet, JavaScript file, and any approved local assets. There is no build command, server-side application, database, or runtime environment configuration.

A static host can publish the repository root directly. Deployment does not add missing functionality such as accounts, search, cart persistence, checkout, payments, inventory, or order management.

## 2. Pre-deployment requirements

Before publishing:
- Review the [README](../README.md) and [Release Checklist](../RELEASE-CHECKLIST.md).
- Confirm the target commit and intended public content.
- Run all automated checks.
- Resolve or explicitly disclose missing local assets.
- Verify asset usage rights.
- Review external resource hosts.
- Check that no secrets or private data are committed.
- Confirm the non-affiliation statement remains accurate.

## 3. Build and artifact expectations

There is no bundler or compilation step. The site is served from the source directory.

Expected core files:
- `index.html`
- `amazone.css`
- `amazone.js`

Supporting local images should be added only after rights are confirmed. Do not invent a `dist/` directory or build output that the project does not generate.

## 4. Validate before deployment

Run from the repository root:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Review all warnings. The current HTML refers to 31 unique local image paths under `imgs/`, but that directory is absent from the tracked repository. A green JavaScript test run does not resolve these image requests.

## 5. Hosting configuration

When configuring a static host:
1. Select the repository and intended branch.
2. Set the publish/document root to the repository root.
3. Do not configure a build command unless a future change introduces a build system.
4. Do not configure a server runtime or database for the current project.
5. Enable HTTPS.
6. Confirm the root document is `index.html`.
7. Confirm the actual deployed URL and nested base path.
8. Test CSS, JS, and local asset URLs on the deployed domain.

## 6. Relative path behaviour

The HTML references styles and scripts using relative paths such as `./amazone.css` and `./amazone.js`. Image paths use `imgs/...`.

If the site is hosted at the domain root, these resolve relative to that location. If hosted under a nested route, confirm the browser's resolved URLs. Do not assume a root-relative path and a document-relative path behave identically.

## 7. HTTPS, headers, and resource policy

The hosting provider controls HTTP response headers. Review:
- HTTPS redirect and certificate.
- Content type for HTML, CSS, JS, and images.
- Cache policy for HTML versus static assets.
- Content Security Policy based on the exact external hosts actually used.
- Referrer policy and other security headers appropriate to the deployment.
- Error page behaviour and correct document root.

Do not deploy a guessed Content Security Policy with wildcard permissions or a policy that blocks required assets without testing.

## 8. Post-deployment smoke test

- [ ] Open the public URL in a private/incognito window.
- [ ] Confirm the page returns successfully.
- [ ] Inspect console and network errors.
- [ ] Confirm stylesheet and script load.
- [ ] Test carousel controls and wrap-around.
- [ ] Test product rail scrolling.
- [ ] Review responsive layout.
- [ ] Verify images and external resources.
- [ ] Check HTTPS and redirect behaviour.
- [ ] Confirm no placeholder action is presented as a real purchase capability.

## 9. Rollback

For a static site, rollback normally means redeploying a previously reviewed Git commit. Record the affected commit, deployment time, observed failure, and selected rollback revision. Verify the previous revision after rollback.

## 10. Production-readiness boundary

A public static deployment is not a production e-commerce service. Do not accept real orders, collect payment data, or collect customer account information through this prototype.
