---
paths:
  - 'resources/js/**/*.tsx'
---

# Js

## Keep component styling in Tailwind utilities
Use Tailwind utilities in the owning React components for component-specific layout, spacing, sizing, responsive behavior, and visual states. Reserve app.css for framework imports, theme tokens, dark-mode configuration, and shared base styles; prefer component-local solutions over adding page- or layout-specific global selectors.

## Reuse shared UI through focused components
Reuse existing components before duplicating UI. Extract repeated markup, visual structure, or behavior with a clear shared responsibility into focused components with small typed props and composable children; keep page-specific logic in its owner.
