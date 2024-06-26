﻿# Groq-Chatbot
  This project implements a simple chatbot using the GROQ API for response generation and Streamlit for the user interface. The chatbot allows users to converse with it by asking questions or     
  providing input, and it responds accordingly based on the selected conversation model.

### Features
  * Users can select a conversation model from a dropdown menu.
  * Adjustable memory length to control the conversational context.
  * Users can input questions or messages to the chatbot.
  * Chat history is displayed in the interface.

### Setup
  1. Clone the repository:
     `git clone https://github.com/your_username/chatbot-groq-streamlit.git
cd chatbot-groq-streamlit`
  2. Install dependencies:
     `pip install -r requirements.txt`
  3. Set up environment variables:
     * Create a `.env` file in the project directory.
     * Add your GROQ API key to the `.env` file:
       `GROQ_API_KEY=your_groq_api_key`
  4. Run the Streamlit app:
     `streamlit run app.py`

### How to Use
  * Choose a conversation model from the sidebar.
  * Adjust the memory length slider according to preference.
  * Input your question or message in the text area.
  * Click the "Submit" button to interact with the chatbot.
  * The chatbot's response will be displayed below the input area.
  * Chat history will be shown in the interface.

### Deployed Link
  [GroqGPT](https://groq-chatbot-techbot505.streamlit.app/)
