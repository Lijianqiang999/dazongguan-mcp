# API Documentation

This document describes the available tools and resources in this MCP server.

## Tools

### search_items

Search items in the system.

**Parameters:**
- `keyword` (string, optional): Search keyword, supports fuzzy matching
- `category` (string, optional): Category filter
- `limit` (integer, optional): Maximum number of results to return (default: 10)

**Returns:**
Formatted list of matching items with ID, name, category, status, and creation time.

**Example Usage:**
```
User: Search for items containing "report"
AI: Found 5 items (showing 5):
    【1】Monthly Report
      Category: Documents
      Status: Active
      Created: 2024-01-15
    ...
```

---

### get_item_detail

Get detailed information about a specific item.

**Parameters:**
- `item_id` (integer, required): The unique identifier of the item

**Returns:**
Detailed item information including all fields.

**Example Usage:**
```
User: Show details for item 123
AI: 【123】Monthly Report
      Category: Documents
      Status: Active
      Description: Monthly financial report
      Created: 2024-01-15
      Updated: 2024-01-20
      Tags: finance, monthly
```

---

### create_item

Create a new item in the system.

**Parameters:**
- `name` (string, required): Item name
- `category` (string, required): Item category
- `description` (string, optional): Item description

**Returns:**
Creation result with the new item ID.

**Example Usage:**
```
User: Create a new item named "Quarterly Report" in category "Documents"
AI: ✅ Item created successfully!
    Item ID: 456
    Name: Quarterly Report
```

---

### update_item

Update an existing item.

**Parameters:**
- `item_id` (integer, required): The unique identifier of the item
- `name` (string, optional): New item name
- `category` (string, optional): New item category
- `description` (string, optional): New item description
- `status` (string, optional): New item status

**Returns:**
Update result.

**Example Usage:**
```
User: Update item 123 status to "Completed"
AI: ✅ Item updated successfully!
    Item ID: 123
```

---

### delete_item

Delete an item from the system.

**Parameters:**
- `item_id` (integer, required): The unique identifier of the item

**Returns:**
Deletion result.

**Example Usage:**
```
User: Delete item 123
AI: ✅ Item deleted successfully!
    Item ID: 123
```

---

## Resources

### dazongguan://items

Get a list of all items in the system.

**Returns:**
- `items`: Array of item objects
- `count`: Total number of items

Each item object contains:
- `id`: Unique identifier
- `name`: Item name
- `category`: Item category
- `status`: Item status
- `created_at`: Creation timestamp

---

## Authentication

All API calls require authentication via the `X-Api-Key` header. The API key is configured in your MCP client configuration.

```json
{
  "mcpServers": {
    "your-server": {
      "url": "http://localhost:8001/mcp",
      "headers": {
        "X-Api-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

## Error Handling

All tools return error messages in the following format:
```
❌ Error: [error message]
```

Common errors:
- Authentication failed: API key is invalid or expired
- Parameter validation: Required parameters are missing
- Backend API errors: Issues with the backend service