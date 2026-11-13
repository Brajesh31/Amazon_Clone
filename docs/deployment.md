# Deployment

## Hosting model

The current project is a static website. Publish the repository's HTML, CSS, JavaScript, and any approved local assets to a static hosting provider. There is no build command.

## Deployment checklist

1. Run `node --check amazone.js`.
2. Run `node --test tests/*.test.js`.
3. Run `python scripts/check_html.py` and review every missing-reference warning.
4. Supply licensed replacements for the currently absent `imgs/` assets, or update the markup to remove those references.
5. Verify external image, font, and icon URLs and confirm their usage terms.
6. Test the final site at the provider's actual path and domain.
7. Confirm that relative asset paths work under the configured base path.
8. Check the browser console, mobile layout, keyboard navigation, and image loading.

## Hosting notes

- Serve the repository root as the site's document root.
- No environment variables, backend secrets, database, or server runtime are currently required.
- Use HTTPS.
- Consider a restrictive Content Security Policy after inventorying the exact third-party hosts needed for scripts, fonts, styles, and images.
- Configure sensible caching for static assets while preserving the ability to update the HTML.

## Production scope warning

This repository is a frontend prototype. Deploying it does not create a functioning online store. Authentication, cart persistence, checkout, payment processing, order management, and inventory are not implemented.
