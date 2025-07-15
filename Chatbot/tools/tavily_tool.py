import os
from dotenv import load_dotenv
from langchain.tools.tavily_search import TavilySearchResults

load_dotenv()

def get_tavily_tool():
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
    return TavilySearchResults()
