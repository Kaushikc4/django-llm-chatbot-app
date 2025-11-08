import openai
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatSession, Message
import os

# Create your views here.

def chat(request):
    if request.method == 'POST':
        
        user_input = request.POST.get('user_id')
        session_id = request.POST.get('session_id')

        # Create or get a chat session
        session, _ = ChatSession.objects.get_or_create(id=session_id or None, default={'User', 'Guest'})

        # Save User Message
        Message.objects.create(session=session, sender='User', message=user_input)

        # Send message to openai
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [{'role': 'User', 'content': 'user_input'}]
        )

        bot_reply = response['choices'][0]['message']['content']
        
        # Save Bot Message
        Message.objects.create(session=session, sender='bot', message=bot_reply)

        return JsonResponse({'reply': bot_reply, 'session_id': session.id})

    return render(request, 'chat.html')

def streamlit_chatbot(request):
    return render(request, 'streamlit_embed.html')
