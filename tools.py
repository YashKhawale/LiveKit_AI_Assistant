import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
    context: RunContext,  # type: ignore
    city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3"
        )
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error fetching weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}."

    
@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        response = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Search results for '{query}': {response}")
        return response
    except Exception as e:
        logging.error(f"Error searching web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."
    
