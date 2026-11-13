# Quality Assurance

## Automated checks

Run all project checks from the repository root:

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

The GitHub Actions workflow executes these commands on pushes and pull requests to `main`.

## JavaScript behaviour covered

The Node.js test suite verifies:

- First hero slide is visible after script startup.
- Next and previous controls select the expected slide.
- Carousel navigation wraps at both ends.
- Anchor navigation is prevented when carousel controls are activated.
- Vertical wheel movement scrolls a product rail horizontally.
- Native horizontal wheel movement is not intercepted.
- Wheel input at the end of a product rail does not trap page scrolling.
- Multiple rails receive independent event handlers.
- Missing slides or controls do not crash the script.

## Manual browser checklist

- [ ] Open the page from a local HTTP server.
- [ ] Confirm the stylesheet and JavaScript load.
- [ ] Use next and previous carousel controls.
- [ ] Use product rails with a vertical mouse wheel and horizontal trackpad input.
- [ ] Confirm page scrolling still works at product-rail boundaries.
- [ ] Check the page at narrow, medium, and wide viewports.
- [ ] Navigate controls with a keyboard and inspect visible focus.
- [ ] Check the browser console.
- [ ] Verify local image references after adding licensed assets.
- [ ] Verify external image, font, and icon requests.

## Known visual QA blocker

The current source tree omits the `imgs/` directory even though the HTML contains many references to it. Automated checks report those unresolved references as warnings, and visual review must account for the broken-image slots.
