import streamlit as st
import os
from groq import Groq
import random
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


def main():
    st.title("Chat with GROQ")
    st.write("This is a simple chatbot that uses GROQ API to generate responses.")

    st.sidebar.title("Select a conversation model")
    model = st.sidebar.selectbox("Choose a Model", ["Mixtral-8x7b-32768", "llama2-70b-4096"])

    conversational_memory_length = st.sidebar.slider("Memory Length", 1, 10, 5)

    memory = ConversationBufferMemory(k=conversational_memory_length)

    user_input = st.text_area("Ask a question.. ")
    submit_button = st.button("Submit")

    # Session state variables
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({"input": message['human']}, {"output": message['AI']})

    groq_chat = ChatGroq(api_key=groq_api_key, model_name=model)

    conversation = ConversationChain(memory=memory, llm=groq_chat)

    if submit_button:
        response = conversation(user_input)
        message = {"human": user_input, "AI": response['response']}
        st.session_state.chat_history.append(message)
        st.write("Chatbot: ", response['response'])


if __name__ == "__main__":
    main()


