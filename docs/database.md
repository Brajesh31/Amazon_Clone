# Database

The current project has no database and no persistence layer.

It does not store users, product inventory, prices, cart contents, searches, addresses, payment details, or order history. Product content is hard-coded in `index.html`.

A future backend should define a reviewed data model, migrations, access control, input validation, backup/restore, and retention requirements. Browser code must not connect directly to a privileged database or contain database credentials.
