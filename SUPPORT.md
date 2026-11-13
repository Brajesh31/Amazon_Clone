# Support

## Before opening an issue

1. Read the [README](README.md), [FAQ](docs/faq.md), and [Troubleshooting](docs/troubleshooting.md).
2. Serve the page from the repository root.
3. Run `node --check amazone.js`, `node --test tests/*.test.js`, and `python scripts/check_html.py`.
4. Check the browser console and network panel.

## Include in a bug report

- Browser and version.
- Operating system.
- Local server command and deployment path, if relevant.
- Expected behaviour and actual behaviour.
- Reproduction steps and sanitised console output.
- Screenshot for visual issues, without private information.

## Known limitation

The current repository does not track the `imgs/` directory referenced by the HTML. See [Asset inventory](docs/ASSET-INVENTORY.md). Report additional broken paths separately from this documented existing gap.
