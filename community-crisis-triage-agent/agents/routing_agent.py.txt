# agents/routing_agent.py

from mcp.mcp_server import MCPServer
from skills.resource_matching import match_resources

class RoutingAgent:
    """
    RoutingAgent
    ------------
    - Queries MCP for local resources.
    - Matches crisis type to services.
    - Builds an action plan.
    """

    def __init__(self, mcp_server: MCPServer | None = None):
        self.mcp = mcp_server or MCPServer()

    def route(self, crisis_info: dict) -> dict:
        resources = self.mcp.get_resources(crisis_info.get("crisis_type", "unknown"))
        plan = match_resources(crisis_info, resources)
        return {
            "resources": resources,
            "action_plan": plan,
        }
