from django.test import TestCase

# from base.base_api_testcase import BaseAPITestCase
from ai_chat.chatbot import Chatbot

# Create your tests here.
class TestChatbot(TestCase):
    def setUp(self):
        self.bot = Chatbot('User001')

    def test_chatbot_response(self):
        response = self.bot.chatbot('Hey, how you doing?')
        self.assertIsNotNone(response)
