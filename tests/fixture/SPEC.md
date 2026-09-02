# Settings update contract

`apply_settings(path, patch)` updates a JSON settings file.

- Preserve every unspecified key, including keys nested below a patched object.
- A failed write must leave the previous settings file readable and unchanged.
- Return the complete persisted settings object.
