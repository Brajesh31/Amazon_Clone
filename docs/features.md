# ✨ Feature Reference

This document separates implemented behaviour from presentation-only elements.

## 1. Implemented browser interactions

### 1.1 Hero image carousel

**Location:** `index.html`, `amazone.js`, `amazone.css`

The hero area contains image elements and two buttons. JavaScript tracks one active slide and displays only that slide. Previous and next controls wrap around the available slide collection.

| Behaviour | Status |
|---|---|
| Initial first slide selection | Implemented |
| Previous slide | Implemented |
| Next slide | Implemented |
| Wrap at start and end | Implemented |
| `aria-hidden` update on slides | Implemented |
| Autoplay | Not implemented |
| Swipe/touch gesture | Not implemented |
| Slide indicators | Not implemented |

### 1.2 Product rail scrolling

**Location:** `amazone.js`

The product collections use horizontal overflow. The script optionally maps vertical wheel movement onto horizontal scrolling when vertical movement dominates. It clamps the scroll position to the rail's boundaries and does not trap page scrolling when the rail cannot move.

### 1.3 Responsive layout

**Location:** `amazone.css`

Media queries adjust the navigation, category card layout, margins, product sections, and footer for tablet and mobile widths. The CSS defines breakpoints at 900px, 600px, and 380px.

Responsive behaviour should still be manually reviewed in real browsers, especially because missing image assets affect card height and visual balance.

## 2. Presentation-only areas

| UI area | What appears | What is not implemented |
|---|---|---|
| Brand/header link | Logo image and root link | Brand-owned navigation destination |
| Delivery location | Static location copy | Geolocation or address selection |
| Search | Search input and icon | Query submission, index, filtering, results |
| Language | EN label and icons | Language selection or translation |
| Account | Sign-in copy | Authentication or account management |
| Orders | Static label | Order history |
| Cart | Icon and label | Cart state, quantity, persistence, checkout |
| Category cards | Image, heading, placeholder link | Category routes and filtered catalog |
| Product rails | Product images | Product detail views or purchase actions |
| Deal cards | Static price and discount text | Live pricing, offer validation, inventory |

## 3. Content model

Product card titles, prices, discount labels, and category labels are authored directly in HTML. There is no structured catalog data file or remote product feed.

## 4. External assets

The page uses third-party image, logo, icon, and font resources. The page does not bundle all visual resources locally. See [Asset Inventory](ASSET-INVENTORY.md) for the missing local image references and rights considerations.

## 5. Feature acceptance checklist

- [ ] Carousel starts on the first available slide.
- [ ] Previous and next controls wrap correctly.
- [ ] Inactive carousel slides are hidden from the visual presentation.
- [ ] Product rails support horizontal native scrolling.
- [ ] Vertical wheel movement scrolls a rail where possible.
- [ ] Page scrolling remains possible at rail boundaries.
- [ ] Layout remains readable at mobile and desktop widths.
- [ ] Placeholder controls are not described as working commerce features.
