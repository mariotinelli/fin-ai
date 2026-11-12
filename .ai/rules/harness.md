---
paths:
  - 'docs/harness/**/capture-fixture.php'
  - 'docs/harness/**/planning.md'
---

# Harness

## Keep keyboard focus targets reachable
Exercise focus with real keyboard navigation along known targets and assert the resulting active element and visible focus where required. Choose a path that keeps focus inside the document, or explicitly re-establish focus before using :focus as a keyboard input target.

## Check both Pint and Rector before PHP handoff
Before handing off PHP changes, run both Pint and Rector in check mode with the project configuration; report success only after both pass. If sandbox restrictions prevent execution, explicitly include both pending checks in the approved host verification handoff.
