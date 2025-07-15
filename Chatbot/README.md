# 🧠 Groq Tool-Enhanced Chatbot with LangChain, LangGraph, and Streamlit

This is an intelligent chatbot built with **LangChain**, **LangGraph**, **Streamlit**, and **Groq's `gemma-7b-it` model**.  
It uses real-time tools like **Wikipedia** and **Tavily** to answer questions and maintains chat memory for a more natural conversation flow.

---

## 🚀 Features

- ✅ Fast, low-latency responses using **Groq's `gemma-7b-it`**
- 🔧 Tool-based reasoning with **Wikipedia** and **Tavily Search**
- 🧠 Maintains chat memory using `ConversationBufferMemory`
- 💬 Clean and interactive frontend via **Streamlit**
- 🧼 Chat clearing option in the sidebar

---

## 🗂️ Project Structure

```
tool_chatbot/
├── app.py                      # Streamlit frontend
├── langgraph_agent.py         # Agent logic + memory setup
├── groq_llm.py                # Groq model loader
├── tools/
│   ├── wikipedia_tool.py      # Wikipedia tool config
│   └── tavily_tool.py         # Tavily tool config
├── .env                       # API keys (not committed)
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

- 🔑 Get Groq API key: https://console.groq.com
- 🔑 Get Tavily API key: https://app.tavily.com

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sureshsharmah/LangFlow-ChatBot
cd tool_chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the chatbot

```bash
streamlit run app.py
```
