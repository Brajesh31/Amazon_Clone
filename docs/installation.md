# Installation and Local Preview

## Requirements

No npm or Python package installation is required. Use a modern browser and optionally Python 3 to serve the page locally.

## Start the site

From the repository root:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/>.

If Python is unavailable, use any static file server that serves the repository root without rewriting the asset paths.

## Validate the project

With Node.js 20 or newer:

```bash
node --check amazone.js
node --test tests/*.test.js
```

With Python 3:

```bash
python scripts/check_html.py
```

The checker reports missing local images as warnings. There is no tracked `imgs/` directory in the current repository tree, so those image slots remain unresolved until licensed assets are supplied.

## No environment variables

The current static site reads no environment variables and does not need secrets. `.env.example` exists as a reminder not to place future credentials in browser code.
