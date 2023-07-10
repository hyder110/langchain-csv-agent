import streamlit as st 
import os
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType

def main():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    st.set_page_config(page_title="Ask Your CSV 📉")
    st .header("Ask Your CSV 📉")

    user_csv=st.file_uploader("Upload your CSV",type="csv")

    if user_csv is not None:
        user_input=st.text_input("Ask a question about your CSV: ")

        llms=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo-16k',openai_api_key=OPENAI_API_KEY)
        csv_path = user_csv.name
        agent=create_csv_agent(llms,csv_path,verbose=True)

        if user_input is not None and user_input !="":
            response=agent.run(user_input)

            st.write(response)

if __name__ == "__main__":
    main()