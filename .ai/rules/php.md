---
paths:
  - '**/*.php'
---

# Php

## Check both Pint and Rector before PHP handoff
Before handing off PHP changes, run both Pint and Rector in check mode with the project configuration; report success only after both pass. If sandbox restrictions prevent execution, explicitly include both pending checks in the approved host verification handoff.
