# 🧪 Testing Strategy

## 1. Scope

The test strategy covers the existing browser-side JavaScript and HTML reference validation. It does not imply that a production commerce workflow exists.

## 2. Current automated layers

| Layer | Tool | Purpose |
|---|---|---|
| JavaScript syntax | Node.js `--check` | Catch parse errors |
| Behaviour tests | Node.js built-in test runner | Verify carousel and product rail behaviour |
| HTML/reference validation | `scripts/check_html.py` | Inspect HTML structure and local asset references |
| CI | GitHub Actions | Run repeatable checks for repository changes |

## 3. Behaviour cases

### Carousel

- Initialization selects the first slide.
- Next and previous controls update visibility.
- Navigation wraps across both ends.
- Missing slides or controls do not cause an exception.
- Inactive slides receive the expected `aria-hidden` value.
- Click handling avoids unintended default anchor behaviour where supported.

### Product rails

- Vertical wheel movement updates horizontal position when movement is possible.
- Horizontal trackpad movement is not intercepted.
- The next scroll position is clamped to the available range.
- Page scrolling is not trapped at either rail boundary.
- Multiple product rails are handled independently.

## 4. Commands

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

## 5. Manual browser test plan

- [ ] Open the site through a local HTTP server.
- [ ] Test carousel controls using mouse and keyboard.
- [ ] Confirm active slide visibility and focus behaviour.
- [ ] Test horizontal rails with a mouse wheel and a trackpad.
- [ ] Test at rail start and end boundaries.
- [ ] Check responsive layout at narrow, medium, and wide widths.
- [ ] Inspect image load failures and external resource errors.
- [ ] Review accessibility tree and keyboard focus.
- [ ] Check the browser console.

## 6. Test data and environment

The current test suite uses a lightweight mock DOM/environment and no external test packages. The page itself should be served from the repository root for manual checks. No credentials, database, or API service are required.

## 7. Gaps

No dedicated real-browser end-to-end automation or visual regression suite is present in the current repository. Add one only when its maintenance value justifies the dependency and runtime.
