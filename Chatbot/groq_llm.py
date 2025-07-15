import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    return ChatGroq(
        model_name="gemma2-9b-it",  
        api_key=os.getenv("GROQ_API_KEY")
    )
