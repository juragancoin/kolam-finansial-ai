from openai import OpenAI
import streamlit as st

client = OpenAI(
api_key=st.secrets["OPENAI_API_KEY"]
)

def ask_ai(system_prompt, user_question):

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.4,
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_question
        }
    ]
)

return response.choices[0].message.content
