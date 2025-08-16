# MCP Weather Server

A Model Context Protocol (MCP) server that provides real-time weather alerts and forecasts for locations across the United States. Built with FastMCP and powered by the National Weather Service (NWS) API.

## Author

Matheus Remigio  
Contact: matheus.remido@gmail.com

## 🌟 Features

- **Weather Alerts**: Get current weather alerts for any US state
- **Weather Forecasts**: Retrieve detailed 5-day weather forecasts for specific coordinates
- **Real-time Data**: Powered by the official National Weather Service API
- **MCP Integration**: Seamlessly integrates with MCP-compatible clients and AI assistants
- **Async Support**: Built with async/await for optimal performance
- **Error Handling**: Robust error handling with graceful fallbacks

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- MCP-compatible client (like Cursor IDE)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/msremigio/mcp-server-weather.git
   cd mcp_weather
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment**
   ```bash
   uv shell
   ```

### Running the Server

```bash
uv run weather.py
```

The server will start and listen for MCP protocol messages via stdio transport.

## 🔧 Configuration

### MCP Client Configuration

Add the following to your MCP client configuration (e.g., `mcp.json`):

```json
{
  "mcpServers": {
    "mcp_weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/mcp_weather/project",
        "run",
        "weather.py"
      ]
    }
  }
}
```

**Note**: Update the `--directory` path to match your actual project location.

## 📚 API Reference

### Available Tools

#### 1. Get Weather Alerts (`get_alerts`)

Retrieves current weather alerts for a specific US state.

**Parameters:**
- `state` (str): Two-letter state abbreviation (e.g., "CA", "NY", "TX")

**Returns:**
- Formatted string containing all active alerts for the specified state

**Example Response:**
```
Event: Severe Thunderstorm Warning
Area: Northern California
Severity: Severe
Description: Severe thunderstorms capable of producing large hail and damaging winds
Instructions: Move to an interior room on the lowest floor of a building

---

Event: Flash Flood Watch
Area: Southern California
Severity: Moderate
Description: Heavy rainfall may cause flash flooding
Instructions: Monitor weather conditions and be prepared to take action
```

#### 2. Get Weather Forecast (`get_forecast`)

Retrieves a 5-day weather forecast for specific coordinates.

**Parameters:**
- `latitude` (str): Latitude coordinate (decimal degrees)
- `longitude` (str): Longitude coordinate (decimal degrees)

**Returns:**
- Formatted string containing the next 5 forecast periods

**Example Response:**
```
Tonight:
- Temperature: 45°F
- Wind: 5 mph NW
- Forecast: Clear skies with light winds

---

Tomorrow:
- Temperature: 72°F
- Wind: 10 mph SW
- Forecast: Sunny and warm with increasing clouds in the afternoon
```

## 🏗️ Project Structure

```
mcp_weather/
├── weather.py          # Main MCP server implementation
├── main.py             # Simple entry point (placeholder)
├── pyproject.toml      # Project configuration and dependencies
├── mcp.json           # MCP client configuration template
├── README.md          # This file
├── uv.lock            # Dependency lock file
├── .python-version    # Python version specification
└── .venv/             # Virtual environment directory
```

## 🔌 Dependencies

- **httpx**: Modern async HTTP client for API requests
- **mcp**: Model Context Protocol implementation
- **FastMCP**: FastMCP framework for building MCP servers

## 🌐 Data Source

This project uses the [National Weather Service (NWS) API](https://www.weather.gov/documentation/services-web-api), which provides:

- Real-time weather alerts and warnings
- Detailed weather forecasts
- Geographic point data
- Free and reliable weather information

## 🛠️ Development

### Adding New Tools

To add new weather-related tools:

1. Create a new async function in `weather.py`
2. Decorate it with `@mcp.tool()`
3. Add proper type hints and docstrings
4. Implement the tool logic using the existing helper functions

### Testing

```bash
# Run the server in development mode
uv run weather.py

# Test with MCP client tools
# The server will respond to MCP protocol messages
```

## 📝 Error Handling

The server includes comprehensive error handling:

- HTTP request failures
- API response validation
- Network timeouts (30-second limit)
- Graceful fallbacks for missing data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License.

## 🙏 Acknowledgments

- [National Weather Service](https://www.weather.gov/) for providing the weather data API
- [MCP Project](https://modelcontextprotocol.io/) for the protocol specification
- [FastMCP](https://github.com/microsoft/mcp) for the server framework

## 📞 Support

For issues, questions, or contributions:

- Open an issue on GitHub
- Check the MCP documentation
- Review the National Weather Service API documentation

---

**Note**: This server requires an active internet connection to fetch weather data from the NWS API.

