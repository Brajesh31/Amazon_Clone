# Troubleshooting

## Local images are missing

Run the server from the repository root and verify that the `imgs/` directory exists with the filenames referenced in `index.html`. Relative paths are case-sensitive on many hosts.

## The carousel does not move

Check the browser console and confirm that `.header-slider ul img`, `.control_prev`, and `.control_next` exist. The current script expects at least one hero image.

## Remote images or icons do not load

Check network connectivity, HTTPS access, CDN availability, and browser extensions. Remote assets may be blocked by policy or changed by their providers.

## Product rails do not scroll

Use the mouse wheel over a `.products` region. The script prevents the default wheel behavior for those regions and translates vertical wheel movement to horizontal scrolling.
