# Contributing to MCP Server Template

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the [Issues](https://github.com/yourusername/mcp-server-template/issues) section
2. If not, create a new issue with:
   - A clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)

### Submitting Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/mcp-server-template.git
   cd mcp-server-template
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the coding style of the existing code
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   # Run the server
   python server.py

   # Test your tools with an MCP client
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Add a description of your changes

## Coding Guidelines

### Python Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use type hints for function parameters and return values
- Write docstrings for all functions and classes
- Keep functions focused and small

### Adding New Tools

When adding new tools:

1. Create a new file in `tools/` directory (e.g., `tools/your_tool.py`)
2. Define a registration function:
   ```python
   def register_your_tools(mcp):
       @mcp.tool()
       async def your_tool(param: str = "") -> str:
           """Tool description for AI"""
           # Implementation
           return "Result"
   ```
3. Register in `tools/__init__.py`:
   ```python
   from tools.your_tool import register_your_tools

   def register_all_tools(mcp):
       register_your_tools(mcp)
   ```
4. Update documentation in `docs/API.md`

### Documentation

- Update README.md if you add new features
- Add API documentation for new tools
- Include examples in docstrings

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Contact the maintainers

Thank you for contributing!