# mcp/mcp_server.py

from pathlib import Path
from .resources_loader import load_json_file

class MCPServer:
    """
    MCPServer
    ---------
    - Loads local resource JSON files.
    - Provides simple query endpoints.
    """

    def __init__(self, data_dir: str = "data"):
        base = Path(data_dir)
        self.shelters = load_json_file(base / "shelters.json")
        self.food_banks = load_json_file(base / "food_banks.json")
        self.crisis_lines = load_json_file(base / "crisis_lines.json")
        self.legal_clinics = load_json_file(base / "legal_clinics.json")
        self.community_centers = load_json_file(base / "community_centers.json")

    def get_resources(self, crisis_type: str) -> dict:
        mapping = {
            "housing": {
                "shelters": self.shelters,
                "crisis_lines": self.crisis_lines,
                "community_centers": self.community_centers,
            },
            "food": {
                "food_banks": self.food_banks,
                "community_centers": self.community_centers,
            },
            "mental_health": {
                "crisis_lines": self.crisis_lines,
                "community_centers": self.community_centers,
            },
        }
        return mapping.get(crisis_type, {"community_centers": self.community_centers})
