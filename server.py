"""
MCP Server Template - Server Entry Point

Based on MCP Python SDK 2.0 (MCPServer + ServerMiddleware)
"""

import os
import uvicorn
from mcp.server.mcpserver import MCPServer

from middleware import ApiKeyMiddleware
from tools import register_all_tools
import config


# ============================================================
# Create MCP Server
# ============================================================
mcp = MCPServer(
    name="MCP Server Template",
    instructions="""You are an AI assistant that helps users interact with backend systems through MCP tools.

Core Rules:
1. Do not mention API keys, authentication, or other technical details - just provide the results
2. Use the available tools to help users accomplish their tasks
3. Ask for clarification when user requests are unclear

Tool Usage Guide:
- Use the appropriate tool based on user requests
- All parameters are optional unless explicitly marked as required
- When parameters are not provided, the system will use defaults or ask for clarification""",
    middleware=[ApiKeyMiddleware()],
)

# ============================================================
# Register All Tools
# ============================================================
register_all_tools(mcp)


# ============================================================
# Start Server
# ============================================================
if __name__ == "__main__":
    port = config.PORT
    config.logger.info("MCP Server starting...")
    config.logger.info(f"MCP endpoint: http://localhost:{port}/mcp")
    config.logger.info(f"Backend API: {config.API_BASE_URL}")

    app = mcp.streamable_http_app(stateless_http=True)
    uvicorn.run(app, host="0.0.0.0", port=port)