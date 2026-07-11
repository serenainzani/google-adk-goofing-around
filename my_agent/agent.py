from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """Return time for specified city"""
    return {
        "status": "success",
        "city": city,
        "time": "10:30AM"
    }

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='root_agent',
    description='A helpful assistant that tells the time for a given city.',
    instruction='You tell the time in cities, using the `get_current_time` tool for this purpose.',
    tools=[get_current_time]
)
