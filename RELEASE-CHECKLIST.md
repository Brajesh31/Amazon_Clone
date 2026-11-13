# Release Checklist

## Source and validation

- [ ] Review changes and confirm no credentials or private data are included.
- [ ] Run `node --check amazone.js`.
- [ ] Run `node --test tests/*.test.js`.
- [ ] Run `python scripts/check_html.py`.
- [ ] Confirm GitHub Actions is green for the release commit.
- [ ] Manually check carousel, product rails, responsive layouts, keyboard focus, and browser console.

## Assets and content

- [ ] Review each local and external asset reference.
- [ ] Verify usage rights and keep a record of asset licences.
- [ ] Resolve or explicitly document missing local image paths.
- [ ] Confirm non-affiliation wording remains visible and accurate.
- [ ] Verify product prices and promotional copy are clearly illustrative.

## Deployment

- [ ] Publish the repository root as a static site.
- [ ] Confirm relative paths work at the deployed base path.
- [ ] Serve the site over HTTPS.
- [ ] Review third-party resource hosts and hosting security headers.
- [ ] Do not represent the prototype as a functioning commerce platform.
