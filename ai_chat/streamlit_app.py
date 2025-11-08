import numpy as np
import streamlit as st
import os
import sys
import django

# Add the parent (project) directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Tell Django where settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

django.setup()

from chatbot import Chatbot

st.set_page_config(page_title='AI Chatbot')

user = None
if 'history' not in st.session_state:
    user = f'User{np.random.randint(1000, 9999)}'
    st.session_state.history = []
if 'previous_chat' not in st.session_state:
    st.session_state.previous_chat = []

# Creating a sidebar
with st.sidebar:
    st.title('Chat Sessions')

    if st.button('New Chat'):
        if st.session_state.history not in st.session_state.previous_chat:
            st.session_state.previous_chat.append(st.session_state.history.copy())
        st.session_state.history = []

    
    st.markdown('---------')

    st.title('**Previous Chats**')

    # Display previous chats
    for i, chat in enumerate(st.session_state.previous_chat):
        # j = np.random.randint(1000,9999)
        if len(chat) > 0:
            chat_title = chat[0][1][:30] + '...' if len(chat[0][1])>30 else chat[0][1]
            if st.button(chat_title, key=f'chat{i}'):
                st.session_state.history = chat

st.title('Chat With ME!')

bot = Chatbot(user)

user_input = st.chat_input('Type your input here...')

if user_input:
    st.session_state.history.append(('User', user_input))

    reply = bot.chatbot(user_input)
    st.session_state.history.append(('Bot', reply))

# Display the convo
for sender, msg in st.session_state.history:
    if sender != 'Bot':
        st.chat_message(sender).markdown(msg)
    
    else:
        st.chat_message(sender).markdown(msg)
