# Django + Streamlit LLM Chatbot App

## Project Overview
A simple yet powerful chatbot application built using Django, Streamlit, and LLM APIs.  
This project lets users chat with an AI model, view past conversations, and start new ones—similar to ChatGPT’s interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
  - [Chat Interface (Streamlit)](#1-chat-interface-streamlit)
  - [Backend (Django)](#2-backend-django)
  - [Session Storage](#3-session-storage)
- [Installation & Setup](#installation--setup)
  - [Clone the Repository](#1-clone-the-repository)
  - [Create and Activate Virtual Environment](#2-create-and-activate-virtual-environment)
  - [Run Django Server](#3-run-the-django-server)
  - [Run Streamlit App](#4-run-the-streamlit-chat-app)

---

## Key Features

### 1) Chat Interface (Streamlit)
- Minimal, clean UI  
- Chat messages displayed like ChatGPT  
- Sidebar with:
  - New Chat button  
  - Previous chats list  
- Automatically stores each conversation  
- Switch between chats instantly  
- Fully interactive Streamlit frontend  

### 2) Backend (Django)
- Designed to store & manage chat sessions  
- API endpoint to generate LLM responses  
- Extensible for OpenAI, HuggingFace, Llama, etc.

### 3) Session Storage
Uses `st.session_state` to track:
- Current conversation  
- Previous chat history  
- User IDs  

---

## Installation & Setup

### 1) Clone the Repository

```bash
git clone https://github.com/Kaushikc4/django-llm-chatbot-app.git
cd django-llm-chatbot-app
```

### 2) Create and Activate Virtual Environment

```bash
python3 -m venv venv
```

#### Linux/Mac:
```bash
source venv/bin/activate
```

#### Windows:
```bash
venv\Scripts\activate
```

### 3) Run the Django Server

```bash
python manage.py runserver
```

### 4) Run the Streamlit Chat App

```bash
streamlit run ai_chat/streamlit_app.py
```
