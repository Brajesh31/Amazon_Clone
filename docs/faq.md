# ❓ Frequently Asked Questions

## Is this an official Amazon website?

No. This is an independent educational storefront prototype inspired by common marketplace interface patterns. It is not affiliated with, sponsored by, or endorsed by Amazon.

## Can visitors buy products?

No. Product cards, search, account labels, cart presentation, and navigation labels are visual examples. There is no working product detail route, cart state, checkout, payment processing, inventory, or order management.

## Why do some product images appear broken?

The HTML references local files under `imgs/`, but the tracked repository does not contain that directory. A clean clone therefore cannot load those local files. The unique paths are listed in [Asset Inventory](ASSET-INVENTORY.md).

## Can I simply download the original images using the filenames?

No. Opaque filenames and publicly accessible URLs do not grant redistribution rights. Use original or appropriately licensed replacements, record the rights basis, and update the asset inventory.

## Why is there no package.json?

The current application uses browser-native HTML, CSS, and JavaScript. It has no frontend framework or build step, so no npm package installation is needed. Node.js is used for the built-in test runner.

## How do I run the project?

From the repository root, run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/`.

## Why should I not open index.html directly?

The project relies on relative file references. A local HTTP server more closely matches static hosting and makes it easier to inspect resource requests and path resolution.

## Does the project use an API or database?

No. Product content is hard-coded in the HTML. The application does not call an application API or persist user data.

## How do the product rails move?

They use native horizontal overflow. The JavaScript additionally translates vertical-dominant wheel movement into horizontal scrolling when the rail can move. At the rail boundary, normal page scrolling is allowed.

## Does the carousel autoplay?

No. It changes slides only when a visitor activates the previous or next button.

## How do I run tests?

```bash
node --check amazone.js
node --test tests/*.test.js
python scripts/check_html.py
```

The JavaScript tests use Node's built-in test runner. The Python script checks basic HTML structure and local file references.

## Are the displayed prices live?

No. They are static illustrative text in the HTML and are not connected to a price service or inventory.

## Can I deploy it to static hosting?

Yes. Publish the repository root as a static site. There is no build command. Verify relative paths and external resources on the actual deployed URL.

## Can I use the images and logos?

Check the rights and licence for every image, logo, font, and icon independently. Public availability does not mean redistribution is permitted.

## What would be required to make it a real store?

A separate design and implementation would be needed for product data, accounts, authorization, cart persistence, server-side pricing, inventory, orders, payments, privacy, security, monitoring, and operations. This is not a small visual enhancement.

## Where should I report a security issue?

Follow [SECURITY.md](../SECURITY.md). Do not publish exploitable details or secrets in a public issue.
