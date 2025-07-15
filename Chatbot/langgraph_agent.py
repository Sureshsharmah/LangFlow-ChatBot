from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

from groq_llm import get_llm
from tools.wikipedia_tool import get_wikipedia_tool
from tools.tavily_tool import get_tavily_tool

def build_agent_executor():
    tools = [get_wikipedia_tool(), get_tavily_tool()]
    llm = get_llm()

    prompt = PromptTemplate.from_template("""
You are an intelligent AI assistant that answers questions using tools.

You must use the following format:

Question: {input}  
Thought: your reasoning  
Action: the action to take, one of [{tool_names}]  
Action Input: the input to the action  
Observation: the result of the action  
... (repeat Thought/Action/Action Input/Observation as needed)  
Thought: I now know the answer  
Final Answer: the final answer to the original question

⚠️ Never write 'Action: None'. If no tool is needed, just say:
Final Answer: <your answer>

Available tools:  
{tools}

Chat History:
{chat_history}

Begin!

Question: {input}
{agent_scratchpad}
""")

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        memory=memory
    )

    return executor
