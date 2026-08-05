# DaZongGuan - MCP Server Template

> A template for building MCP (Model Context Protocol) servers with Python. This template provides a solid foundation for creating AI-powered assistants that connect to your backend systems.

## Features

- 🔌 **MCP Protocol Support** - Built on MCP Python SDK 2.0
- 🔐 **ApiKey Authentication** - Secure API key-based authentication via HTTP headers
- 🛠️ **Modular Tools** - Easy-to-extend tool system
- 📝 **Comprehensive Logging** - Built-in logging with rotation
- 🚀 **Production Ready** - Includes middleware, error handling, and configuration management

## Quick Start

### Prerequisites

- Python 3.10+
- MCP Python SDK >= 2.0.0

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-server-template.git
cd mcp-server-template

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

### Configuration

Edit `.env` file with your settings:

```env
# Backend API Configuration
API_BASE_URL=http://your-api-server:port

# Server Configuration
PORT=8001

# Logging
LOG_LEVEL=INFO
```

### Start Server

```bash
python server.py
```

The server runs at `http://localhost:8001` by default, with the MCP endpoint at `http://localhost:8001/mcp`.

## Project Structure

```
mcp-server-template/
├── server.py          # MCP server entry point
├── config.py          # Configuration and logging
├── middleware.py       # Authentication middleware
├── constants.py       # Constants definition
├── utils.py           # Utility functions
├── tools/             # Tools module directory
│   ├── __init__.py    # Tools module initialization
│   ├── example.py     # Example tools
│   └── ...            # Add your tools here
├── docs/              # Documentation
│   ├── README.md      # This file
│   └── API.md         # API documentation
├── .env.example       # Environment variables template
├── requirements.txt   # Python dependencies
└── LICENSE            # MIT License
```

## Usage

### Configure MCP Client

Add the MCP configuration to your AI client:

```json
{
  "mcpServers": {
    "your-server-name": {
      "url": "http://localhost:8001/mcp",
      "headers": {
        "X-Api-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

### Creating Tools

Create new tools in the `tools/` directory:

```python
# tools/your_tool.py

from utils import call_api, check_response

def register_your_tools(mcp):
    """Register your tools to MCP server"""

    @mcp.tool()
    async def your_tool_name(param1: str = "", param2: int = 0) -> str:
        """Tool description for AI to understand when to use it.

        Args:
            param1: Description of param1
            param2: Description of param2

        Returns:
            Description of return value
        """
        # Call your backend API
        res = await call_api("/api/your-endpoint", body={
            "param1": param1,
            "param2": param2
        })

        # Check response
        ok, result = check_response(res, "your action")
        if not ok:
            return f"❌ {result}"

        # Process and return result
        return f"✅ Success: {result}"
```

Register your tools in `tools/__init__.py`:

```python
from tools.your_tool import register_your_tools

def register_all_tools(mcp):
    """Register all tools to MCP server"""
    register_your_tools(mcp)
```

### Creating Resources

Resources provide read-only data to AI:

```python
@mcp.resource("your-server://resource-name")
async def get_resource():
    """Resource description"""
    return {"key": "value"}
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `API_BASE_URL` | Backend API base URL | `http://localhost:8000` |
| `PORT` | Server port | `8001` |
| `LOG_LEVEL` | Logging level | `INFO` |

## Tech Stack

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official MCP Python SDK (>= 2.0.0)
- [httpx](https://www.python-httpx.org/) - Async HTTP client
- [uvicorn](https://www.uvicorn.org/) - ASGI server

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/) - The protocol specification
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - The Python implementation