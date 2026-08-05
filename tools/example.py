"""
MCP Server Template - Example Tools

This file contains example tools to help you get started.
Replace these with your actual tools.
"""

from utils import call_api, check_response, format_list


def register_example_tools(mcp):
    """Register example tools to MCP server

    Args:
        mcp: MCPServer instance
    """

    @mcp.tool()
    async def search_items(
        keyword: str = "",
        category: str = "",
        limit: int = 10,
    ) -> str:
        """Search items in the system.

        Use this tool when:
        - User wants to search for items
        - User wants to filter items by keyword or category
        - All parameters are optional

        Args:
            keyword: Search keyword, supports fuzzy matching
            category: Category filter
            limit: Maximum number of results to return (default: 10)

        Returns:
            Formatted list of matching items
        """
        body = {}
        if keyword:
            body["keyword"] = keyword
        if category:
            body["category"] = category
        body["limit"] = limit

        res = await call_api("/api/items/search", body)
        ok, result = check_response(res, "search")
        if not ok:
            return f"❌ {result}"

        items = result.get("items") or []
        count = result.get("count", 0)

        if not items:
            return "No items found."

        lines = [f"Found {count} items (showing {len(items)}):\n"]
        for item in items:
            lines.append(f"【{item.get('id', '')}】{item.get('name', '')}")
            lines.append(f"  Category: {item.get('category', '')}")
            lines.append(f"  Status: {item.get('status', '')}")
            lines.append(f"  Created: {item.get('created_at', '')}")
            lines.append("")

        return "\n".join(lines)

    @mcp.tool()
    async def get_item_detail(item_id: int) -> str:
        """Get detailed information about a specific item.

        Use this tool when:
        - User wants to see full details of an item
        - User needs to see all fields of an item
        - item_id is obtained from search_items results

        Args:
            item_id: The unique identifier of the item (integer)

        Returns:
            Detailed item information
        """
        res = await call_api("/api/items/detail", params={"id": item_id})
        ok, result = check_response(res, "query")
        if not ok:
            return f"❌ {result}"

        item = result.get("item") or {}

        if not item:
            return f"❌ Item {item_id} not found."

        lines = []
        lines.append(f"【{item.get('id', '')}】{item.get('name', '')}")
        lines.append(f"  Category: {item.get('category', '')}")
        lines.append(f"  Status: {item.get('status', '')}")
        lines.append(f"  Description: {item.get('description', '')}")
        lines.append(f"  Created: {item.get('created_at', '')}")
        lines.append(f"  Updated: {item.get('updated_at', '')}")

        # Add more fields as needed
        if item.get("tags"):
            lines.append(f"  Tags: {', '.join(item['tags'])}")

        return "\n".join(lines)

    @mcp.tool()
    async def create_item(
        name: str = "",
        category: str = "",
        description: str = "",
    ) -> str:
        """Create a new item in the system.

        Use this tool when:
        - User wants to create a new item
        - User says "create", "add", or "new item"

        Args:
            name: Item name (required)
            category: Item category (required)
            description: Item description (optional)

        Returns:
            Creation result with the new item ID
        """
        # Validate required parameters
        errors = []
        if not name:
            errors.append("name (item name) is required")
        if not category:
            errors.append("category (item category) is required")

        if errors:
            return "❌ Parameter errors:\n" + "\n".join([f"- {e}" for e in errors])

        body = {
            "name": name,
            "category": category,
        }
        if description:
            body["description"] = description

        res = await call_api("/api/items/create", body)
        ok, result = check_response(res, "create")
        if not ok:
            return f"❌ {result}"

        item_id = result.get("id", "")

        return f"✅ Item created successfully!\nItem ID: {item_id}\nName: {name}"

    @mcp.tool()
    async def update_item(
        item_id: int = 0,
        name: str = "",
        category: str = "",
        description: str = "",
        status: str = "",
    ) -> str:
        """Update an existing item.

        Use this tool when:
        - User wants to modify an item
        - User says "update", "edit", or "modify item"
        - item_id is obtained from search_items or get_item_detail results

        Args:
            item_id: The unique identifier of the item (required)
            name: New item name (optional)
            category: New item category (optional)
            description: New item description (optional)
            status: New item status (optional)

        Returns:
            Update result
        """
        # Validate required parameters
        if not item_id or item_id == 0:
            return "❌ Parameter error:\n- item_id (item ID) is required"

        body = {"id": item_id}
        if name:
            body["name"] = name
        if category:
            body["category"] = category
        if description:
            body["description"] = description
        if status:
            body["status"] = status

        res = await call_api("/api/items/update", body)
        ok, result = check_response(res, "update")
        if not ok:
            return f"❌ {result}"

        return f"✅ Item updated successfully!\nItem ID: {item_id}"

    @mcp.tool()
    async def delete_item(item_id: int = 0) -> str:
        """Delete an item from the system.

        Use this tool when:
        - User wants to delete an item
        - User says "delete", "remove", or "drop item"
        - item_id is obtained from search_items or get_item_detail results

        Args:
            item_id: The unique identifier of the item (required)

        Returns:
            Deletion result
        """
        # Validate required parameters
        if not item_id or item_id == 0:
            return "❌ Parameter error:\n- item_id (item ID) is required"

        res = await call_api("/api/items/delete", body={"id": item_id})
        ok, result = check_response(res, "delete")
        if not ok:
            return f"❌ {result}"

        return f"✅ Item deleted successfully!\nItem ID: {item_id}"