# Architecture

Amazon Clone is a single-page static site. `index.html` owns the content structure, `amazone.css` owns presentation, and `amazone.js` adds two client-side behaviors: hero-image selection and horizontal product scrolling.

There is no build pipeline, server, database, API, state store, or authentication layer. Images are a mixture of local paths and remote CDN URLs. The page should be served from the repository root so relative paths remain valid.
