from django.urls import path
from . import views

urlpatterns = [
    # path('', views.chat, name='chat'),
    path('', views.streamlit_chatbot, name='streamlit.chatbot')
]