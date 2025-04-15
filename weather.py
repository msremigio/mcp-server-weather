from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP


# Initialize the MCP server with Cursor-specific configuration
mcp = FastMCP("weather")

# Define constants
NWS_API_BASE_URL = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


# Helper function to make requests to the NWS API
async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"Request failed: {e}")
            return None
        
# Helper function to organize the alerts structure to a user-friendly format
def format_alert(feature: dict[str, Any]) -> str:
    """Format an alert into a user-friendly string"""
    properties = feature["properties"]
    return f"""
    Event: {properties.get("event", "Unknown")}
    Area: {properties.get("areaDesc", "Unknown")}
    Severity: {properties.get("severity", "Unknown")}
    Description: {properties.get("description", "No additional information provided")}
    Instructions: {properties.get("instruction", "No additional instructions provided")}
    """
    
# Implemnting tool execution nº 1: Get current weather alerts to a US state
@mcp.tool(require_user_approval=False)
async def get_alerts(state: str) -> str:
    """Get current weather alerts for a US state
    
    Args:
        state (str): The US state to get alerts for (e.g., "CA", "NY")
        
    Returns:
        str: A formatted string containing the alerts for the specified state
    """
    url = f"{NWS_API_BASE_URL}/alerts/active?area={state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found for this state."
    
    if not data["features"]:
        return "No active alerts found for this state."
    
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

# Implemnting tool execution nº 2: Get current weather forecast US coordinates
@mcp.tool(require_user_approval=False)
async def get_forecast(latitude: str, longitude: str) -> str:
    """Get current weather forecast for a US location
    
    Args:
        latitude (str): The latitude coordinate of the location
        longitude (str): The longitude coordinate of the location
        
    Returns:
        str: A formatted string containing the next 5 weather forecast for the specified location
    """
    # First get the forecast grid endpoint
    grid_url = f"{NWS_API_BASE_URL}/points/{float(latitude)},{float(longitude)}"
    grid_data = await make_nws_request(grid_url)

    if not grid_data:
        return "Unable to fetch detailed forecast data."
    
    # Get the forecast periods URL from the grid data and make a request to it
    forecast_url = grid_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast data."
    
    # Format the forecast data into a user-friendly format
    periods = forecast_data["properties"]["periods"]
    forecast = []
    for period in periods[:5]:
        forecast.append(f"""
        {period["name"]}:
        - Temperature: {period["temperature"]}
        - Wind: {period["windSpeed"]} {period["windDirection"]}
        - Forecast: {period["detailedForecast"]}
        """)
    
    return "\n---\n".join(forecast)


# Initialize the MCP server and run it
if __name__ == "__main__":
    mcp.run(transport="stdio")