#!/usr/bin/env python3
"""Strip Jupyter widget metadata + outputs from .ipynb files.

Anything using `tqdm.notebook` (pooch downloads, scanpy progress bars in a
Jupyter kernel) emits widget output blobs whose UUIDs regenerate on every
execution. Stripping them keeps committed notebooks small and produces
clean PR diffs that reflect real source changes only.

Usage: strip_widget_metadata.py <notebook> [<notebook> ...]
Exits 0 if no changes, 1 if files were modified (so pre-commit reports the
fix the way other auto-fixers do).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WIDGET_MIME = "application/vnd.jupyter.widget-view+json"


def strip(path: Path) -> bool:
    nb = json.loads(path.read_text())
    changed = False

    if "widgets" in nb.get("metadata", {}):
        nb["metadata"].pop("widgets")
        changed = True

    for cell in nb.get("cells", []):
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if WIDGET_MIME in data:
                data.pop(WIDGET_MIME)
                changed = True

    if changed:
        path.write_text(json.dumps(nb, indent=1) + "\n")
    return changed


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: strip_widget_metadata.py <notebook> [<notebook> ...]", file=sys.stderr)
        return 2
    any_changed = False
    for arg in sys.argv[1:]:
        if strip(Path(arg)):
            print(f"stripped widgets: {arg}")
            any_changed = True
    return 1 if any_changed else 0


if __name__ == "__main__":
    sys.exit(main())
