from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

def get_wikipedia_tool():
    wiki_api = WikipediaAPIWrapper()
    return WikipediaQueryRun(api_wrapper=wiki_api)
