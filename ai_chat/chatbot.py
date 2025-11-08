import arrow
import openai
from openai import OpenAI
import os
import subprocess

from ai_chat.models import ChatSession, Message

class Chatbot:
    def __init__(self, user=None, model='gemma:2b'):
        self.user = user
        self.model = model

    def chatbot(self, prompt):
        try:
            if self.user == None:
                session = ChatSession.objects.last()
            else:
                session = ChatSession.objects.create(
                    user = self.user
                )

            Message.objects.create(
                session = session,
                sender = session.user,
                message = prompt,
                timestamp = arrow.now('Asia/Kolkata').naive
            )

            result =  subprocess.run(
                ['ollama', 'run', self.model],
                input=prompt,
                text=True,
                capture_output=True,
                check=True
            )

            Message.objects.create(
                session = session,
                sender = 'Bot',
                message = result.stdout.strip(),
                timestamp = arrow.now('Asia/Kolkata').naive
            )
            return result.stdout.strip()
        except Exception as e:
            return f'Error {e}'
