# 🧰 Troubleshooting Guide

## 1. Start with a reproducible environment

Run the static server from the repository root:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`. Record the browser, version, operating system, commit, and exact steps before investigating an issue.

## 2. Page loads without styling

**Check:**
- The server is running from the repository root.
- `amazone.css` exists beside `index.html`.
- The browser network panel shows a successful request for `./amazone.css`.
- The browser console does not report a stylesheet parsing error.

The HTML uses a relative stylesheet path. Hosting the document under a nested route can change how that path resolves.

## 3. Carousel controls do not change the image

**Check:**
- `amazone.js` loads successfully.
- The document contains `.header-slider ul img`.
- The previous and next buttons use `.control_prev` and `.control_next`.
- The browser console contains no script exception.
- The slide collection is not empty.

The script intentionally tolerates missing controls and empty slide collections. If there are no slides, there is nothing to display.

## 4. Product or category images are broken

The current tracked repository does not include the `imgs/` directory referenced by the page. This is a known repository issue.

**Resolution:**
1. Review [Asset Inventory](ASSET-INVENTORY.md).
2. Source an original or permissively licensed replacement.
3. Record the rights basis.
4. Add the asset under a stable local path.
5. Update the HTML and inventory.
6. Run `python scripts/check_html.py`.
7. Verify rendering in a browser.

Do not download images based solely on retailer-style filenames.

## 5. Remote hero images, fonts, or icons fail

Remote resources depend on third-party hosts. Check:
- Network connectivity.
- HTTPS and certificate errors.
- Browser extensions or content blockers.
- The request URL and response status.
- Whether the provider has changed or removed the resource.

A remote asset failure does not necessarily indicate a JavaScript bug. Consider a licensed local replacement if the resource is essential.

## 6. Product rails do not move horizontally

The rails use native horizontal overflow. Native horizontal trackpad movement should remain available. The JavaScript additionally translates vertical-dominant wheel movement when the rail has room to move.

If no movement occurs:
- Confirm the pointer is over the rail.
- Confirm the rail's content is wider than its visible area.
- Check whether the rail is already at its left or right boundary.
- Inspect the element's computed `overflow-x`, `scrollWidth`, and `clientWidth`.
- Confirm the wheel listener was attached.

At either boundary, normal page scrolling is deliberately not blocked.

## 7. Site works locally but fails after deployment

Check the document root and deployment base path. Relative paths such as `./amazone.css`, `./amazone.js`, and `imgs/...` resolve relative to the document location. Hosting under a nested path can therefore produce different URLs.

Inspect the deployed network panel and compare the requested paths with the actual published files.

## 8. Automated tests fail

Run:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

Use Node.js 20 or newer and Python 3. Read the first failing assertion and reproduce it before changing the test. Do not remove an assertion merely to make CI green.

## 9. HTML checker reports missing references

The checker reports missing local files. The missing `imgs/` references are known and should remain visible until resolved. A warning is not the same as a repaired asset.

## 10. Reporting an issue

Include the exact command, browser, commit, steps, expected result, actual result, and sanitized evidence. Do not include tokens, personal data, or private information. See [SUPPORT.md](../SUPPORT.md).
