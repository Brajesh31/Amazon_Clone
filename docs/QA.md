# Quality Checks and Known Gaps

## Manual smoke test
1. Start a local server from the repository root.
2. Confirm the page loads without JavaScript errors.
3. Use both hero carousel controls.
4. Scroll each product rail with the mouse wheel.
5. Check narrow and wide viewport layouts.
6. Navigate with the keyboard and inspect focus visibility.
7. Verify remote assets and all local image paths.

## Known repository gap
The current Git tree does not include an `imgs/` directory, but the page references local `imgs/...` assets. This is a known broken-asset condition until those image files are supplied. Do not fabricate replacement assets or claim the page is visually complete.

## Automated checks
GitHub Actions checks that the three entry files exist and that `amazone.js` parses with Node.js. These checks do not validate visual rendering, remote image availability, accessibility, or product behavior.
