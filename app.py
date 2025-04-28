import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template
template = """
Answer the questions below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""

# Load your model
model = Ollama(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit App
st.set_page_config(page_title="AI Psychologist", page_icon="🧠")

st.title("🧠 Welcome to your AI Psychologist!")

# Initialize conversation context
if "context" not in st.session_state:
    st.session_state.context = ""

# User input
user_input = st.text_input("What's on your mind?", key="user_input")

if st.button("Ask"):
    if user_input:
        with st.spinner('Thinking...'):
            result = chain.invoke({"context": st.session_state.context, "question": user_input})
            st.success(result)
            
            # Update the conversation history
            st.session_state.context += f"User: {user_input}\nAssistant: {result}\n"

# Option to reset conversation
if st.button("Reset Conversation"):
    st.session_state.context = ""
    st.success("Conversation reset!")
