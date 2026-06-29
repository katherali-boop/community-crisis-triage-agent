# mcp/resources_loader.py

import json
from pathlib import Path

def load_json_file(path: Path) -> list:
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
