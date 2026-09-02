import json
from pathlib import Path


def apply_settings(path: Path, patch: dict) -> dict:
    current = json.loads(path.read_text(encoding="utf-8"))
    current.update(patch)
    path.write_text(json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8")
    return current
