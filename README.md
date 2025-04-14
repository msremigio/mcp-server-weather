# Initialize MCP Server using Cursor IDE

### mcp.json

```json
{
  "mcpServers": {
    "mcp_weather": {
      "command": "uv",
      "args": [
        "--directory",
        "path_to_your_project_directory",
        "run",
        "weather.py"
      ]
    }
  }
}

