"""Read historical investigation evidence without inheriting its obsolete budgets."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ralph_runtime import RuntimeFailure


def read_history(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("original"), dict) or data["original"].get("status") != "failed" or data.get("used") is not True:
        raise RuntimeFailure("invalid investigation history; preserve evidence and inspect before resuming")
    return data
