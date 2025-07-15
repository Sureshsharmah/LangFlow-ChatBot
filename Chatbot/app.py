import streamlit as st
from langgraph_agent import build_agent_executor

st.set_page_config(page_title="🧠 Groq Chatbot", page_icon="🧠")
st.title("🧠 Groq Chatbot (Gemma + Tools + Memory)")

if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = build_agent_executor()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if user_input and st.session_state.agent_executor:
    with st.spinner("Thinking..."):
        result = st.session_state.agent_executor.invoke({"input": user_input})
        output = result.get("output", "Sorry, I didn't get that.")
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", output))

if st.session_state.chat_history:
    st.subheader("🕒 Chat History")
    for sender, msg in st.session_state.chat_history:
        with st.chat_message("user" if sender == "You" else "assistant"):
            st.markdown(f"**{sender}:** {msg}")

st.sidebar.title("Options")
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.agent_executor = build_agent_executor()
    st.rerun()
