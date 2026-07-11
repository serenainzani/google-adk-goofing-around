import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "edinburgh":
        return {
            "status": "success",
            "report": (
                "The weather in Edinburgh is cloudy"
                "with a temperature of 15°C."
            )
        }
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, weather information for '{city}' is not available."
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == 'edinburgh' or city.lower() == 'london':
        tz = ZoneInfo("Europe/London")
        now = datetime.datetime.now(tz)
        now_formatted = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")

        return {
            "status": "success",
            "message": f"The time is {now_formatted} in {city}"
        }
    else: 
        return {
            "status": "error",
            "error_message": f"Sorry, I cannot retrieve the time for {city}"
        }
    
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-3.1-flash-lite",
    description="A helpful assistant that returns the time and weather for a given city.",
    instruction="You are a helpful agent who can answer user questions about the time and weather for a given city, using the get_weather and get_current_time tools.",
    tools=[get_weather, get_current_time]
)