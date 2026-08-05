"""
MCP Server Template - Tools Module
"""

from tools.example import register_example_tools


def register_all_tools(mcp):
    """Register all tools to MCP server

    Args:
        mcp: MCPServer instance
    """
    register_example_tools(mcp)