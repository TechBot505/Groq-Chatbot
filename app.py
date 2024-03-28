import streamlit as st
import os
from groq import Groq
import random
from langchain.chains import ConrsationalChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


def main():
    pass


if __name__ == "__main__":
    main()


