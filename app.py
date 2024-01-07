import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage

from llms import llms
from agent import ask_agent

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        AIMessage(content="Hi! I'm Veritone Copilot. How can I help you?")
    ]

dialogue_area = st.empty()
# input_area = st.empty()

# with input_area.container():
user_input = st.chat_input("Say something.")

with dialogue_area.container():
    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        bot_response = ask_agent(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=bot_response))
    for message in st.session_state.messages:
        if message.type == 'human':
            st_message = st.chat_message(
                message.type
            )
        else:
            st_message = st.chat_message(
                message.type,
                avatar='https://talent.wendy.ai/assets/wendy_avatar.f53354a1.svg'
            )
        st_message.write(message.content)