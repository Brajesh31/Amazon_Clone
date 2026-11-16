# 📦 Installation and Local Preview

## 1. What installation means for this project

Amazon Clone is a static HTML/CSS/JavaScript project. There is no dependency installation step, package manager manifest, framework setup, or build process. The files can be served directly by a static HTTP server.

You need a modern browser to view the page. Python 3 is used in the examples below to serve the files. Node.js 20 or newer is used for JavaScript tests.

## 2. Clone the repository

```bash
git clone https://github.com/Brajesh31/Amazon_Clone.git
cd Amazon_Clone
```

If you already have the repository, change into the local repository directory and confirm that you are on the intended branch before making edits.

## 3. Start the local server

From the repository root:

```bash
python -m http.server 8000
```

Open the following address in a browser:

```text
http://localhost:8000/
```

Stop the server with Ctrl+C in the terminal.

### Why serve over HTTP?

The page uses relative paths for its stylesheet, JavaScript, and local images. Serving from the repository root more closely matches a static deployment and makes network requests inspectable. Opening `index.html` through a `file://` URL can behave differently and should not be used as the only validation method.

## 4. Alternative static servers

Any static server can be used if it serves the repository root and preserves relative paths. Do not introduce a build tool merely to serve static files.

## 5. Validate the source

### JavaScript syntax and tests

With Node.js 20 or newer:

```bash
node --check amazone.js
node --test tests/*.test.js
```

### HTML and local asset references

With Python 3:

```bash
python scripts/check_html.py
```

The checker verifies required entry files, basic HTML structure, title presence, duplicate IDs, and local file references. It currently reports missing local image references as warnings because the repository does not track the referenced `imgs/` directory.

## 6. Environment variables

The current static site does not read environment variables and does not require secrets. The `.env.example` file is informational. Never place real API keys, passwords, tokens, or database credentials in public browser code or committed example files.

## 7. Common setup problems

| Symptom | Likely reason | Next step |
|---|---|---|
| Page cannot connect | Server is not running or port differs | Check terminal output and URL |
| Styles are missing | Server root or relative path is incorrect | Serve from repository root |
| JavaScript does not run | Script path or browser console error | Inspect network and console |
| Product images are broken | Referenced `imgs/` directory is absent | Review asset inventory |
| Tests command fails | Node.js missing or too old | Install a supported Node.js version |
| Python checker fails | Python missing or source structure invalid | Review the command output |

## 8. Related guides

- [Development Guide](development.md)
- [Testing Strategy](testing-strategy.md)
- [Troubleshooting](troubleshooting.md)
- [Deployment](deployment.md)
- [Asset Inventory](ASSET-INVENTORY.md)
