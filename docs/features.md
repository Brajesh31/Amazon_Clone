# ✨ Feature Reference and Behaviour Specification

## 1. Reading this document

This reference separates actual browser behaviour from elements that are only visual. Status terms mean:

- **Implemented:** behaviour exists in the tracked source.
- **Presentation-only:** the UI is visible but does not perform the apparent application action.
- **Not implemented:** there is no current implementation.
- **Proposed:** a possible future enhancement, not a delivered feature.

## 2. Implemented browser interactions

### 2.1 Hero image carousel

**Source files:** `index.html`, `amazone.js`, `amazone.css`.

The hero section contains a list of promotional images and two native buttons. The JavaScript stores an active index, initially displays the first image, and binds the controls to increment or decrement the index.

| Behaviour | Status | Notes |
|---|---|---|
| Initial first slide selection | Implemented | Runs when at least one slide exists |
| Previous slide | Implemented | Moves one position backward |
| Next slide | Implemented | Moves one position forward |
| Wrap-around | Implemented | Uses modulo against slide count |
| Inactive slide visibility | Implemented | Non-active slides are hidden |
| `aria-hidden` update | Implemented | Applied when the element supports `setAttribute` |
| Autoplay | Not implemented | No timer or automatic transition |
| Touch/swipe | Not implemented | No pointer gesture handler |
| Pagination indicators | Not implemented | No dots or slide counter |
| Pause/resume | Not applicable | No autoplay |

The script guards against a missing or empty slide collection and against absent controls.

### 2.2 Product rail scrolling

**Source file:** `amazone.js`.

The product rows use CSS horizontal overflow. Each row is queried and receives its own wheel handler.

When vertical wheel movement dominates horizontal movement:
1. The handler calculates the maximum horizontal scroll.
2. It calculates a candidate position using `scrollLeft + deltaY`.
3. It clamps the position to the valid range.
4. If the rail can move, the handler prevents the default wheel action and updates `scrollLeft`.
5. If the rail cannot move, it leaves normal page scrolling available.

Native horizontal trackpad input is not intercepted by this handler.

### 2.3 Responsive layout

**Source file:** `amazone.css`.

The stylesheet uses media queries at 900px, 600px, and 380px. These adjust navigation wrapping, category card widths, margins, product section spacing, and footer layout.

The presence of breakpoints does not prove the layout is usable at every viewport. Manual review is still required, especially while local image files are missing.

## 3. Presentation-only areas

| UI area | Visible content | Missing behaviour |
|---|---|---|
| Brand/header | Logo image and root link | No brand-owned route or identity service |
| Delivery location | Static location copy | No address selection or geolocation |
| Search | Search input and icon | No submit, index, filtering, or results |
| Language | EN label and icons | No locale selector or translation |
| Account | Sign-in and account labels | No authentication or account management |
| Orders | Static label | No order history |
| Cart | Icon and label | No item state, quantity, persistence, or checkout |
| Category cards | Image, heading, placeholder link | No category route or filtering |
| Product rails | Product images | No detail view or purchase action |
| Deal cards | Static prices and discounts | No live pricing, offer validation, or stock status |

## 4. Static content model

Product names, prices, discount labels, and category headings are authored directly in HTML. There is no structured catalog file, API response, content management system, or remote product feed.

The displayed prices and discount values must be treated as illustrative text. They are not authoritative offers.

## 5. External visual dependencies

The page references remote hero images, a logo, icons, and font styles. These are loaded by the browser and may be unavailable or changed independently. Local product/category images are referenced under `imgs/`, but the directory is missing from the tracked repository.

See [Asset Inventory](ASSET-INVENTORY.md).

## 6. Interaction acceptance criteria

### Carousel

- [ ] First slide appears after startup.
- [ ] Next and previous controls select the expected slide.
- [ ] Navigation wraps in both directions.
- [ ] Inactive slides are not visually presented as active.
- [ ] Controls remain keyboard operable and have accessible names.

### Product rails

- [ ] Native horizontal scrolling works.
- [ ] Vertical wheel movement scrolls the rail when it can move.
- [ ] The wheel event is not unnecessarily prevented.
- [ ] Page scrolling remains available at both boundaries.
- [ ] Multiple rails work independently.

### Responsive presentation

- [ ] Navigation remains usable at mobile widths.
- [ ] Category cards reflow without overlap.
- [ ] Product rails remain horizontally discoverable.
- [ ] Footer content remains readable.
- [ ] Zoom and text scaling do not hide important controls.

## 7. Future feature rule

New search, cart, account, or purchase interactions must have a defined user problem, state model, empty/error behaviour, accessibility plan, tests, and clear data trust boundary. Do not add a visual control and call the feature complete without its expected behaviour.
