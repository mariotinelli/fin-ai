---
paths:
  - 'resources/js/**/*.tsx'
---

# Js

## Keep component styling in Tailwind utilities
Use Tailwind utilities in the owning React components for component-specific layout, spacing, sizing, responsive behavior, and visual states. Reserve app.css for framework imports, theme tokens, dark-mode configuration, and shared base styles; prefer component-local solutions over adding page- or layout-specific global selectors.
