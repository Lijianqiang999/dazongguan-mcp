"""
MCP Server Template - Authentication Middleware
"""

from mcp.server.context import ServerRequestContext
import config


class ApiKeyMiddleware:
    """Extract X-Api-Key from HTTP request headers"""

    async def __call__(self, ctx: ServerRequestContext, call_next):
        request = ctx.request
        if request and hasattr(request, 'headers'):
            key = request.headers.get("x-api-key", "")
            config._current_api_key = key
        return await call_next(ctx)