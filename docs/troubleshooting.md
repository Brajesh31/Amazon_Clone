# Troubleshooting

## Page opens without styles

Confirm the server is running from the repository root and that `amazone.css` is present. The HTML references it as `./amazone.css`.

## Carousel controls do not work

Confirm `amazone.js` loads and inspect the browser console. Verify the page contains `.header-slider ul img`, `.control_prev`, and `.control_next`. The script safely handles an empty carousel or missing controls, but no slides means there is nothing to display.

## Product/category images are broken

The HTML references the `imgs/` directory, which is absent from the tracked repository. Review [Asset inventory](ASSET-INVENTORY.md). Add only assets you have permission to use, preserving the expected relative paths, or update the markup to reference approved alternatives.

## Remote hero images or icons fail

Check network access, HTTPS, browser extensions, content blockers, and third-party host availability. Remote providers may remove or change files without notice.

## Horizontal product rails do not move

Use the vertical mouse wheel over a product rail. A vertical wheel gesture is translated into horizontal movement when the rail can move. Native horizontal wheel input remains available. At either end, normal page scrolling is not blocked.

## Site works locally but fails after deployment

Serve the repository root as the document root and check the deployment base path. Paths beginning with `./` or `imgs/` are relative to the current document location. Hosting under a nested route may require a matching base path.

## Tests fail

Use Node.js 20 or newer and run:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

The Python HTML checker may report missing image paths as warnings. Those warnings reflect known absent files, not a test harness failure.
