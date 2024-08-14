Moai AI Chat



Overview
Moai AI Chat is a hands-on project aimed at learning how to build AI multimedia chat application. This project is all about integrating different AI models to handle audio, images, and PDFs in a single chat interface.

Using Whisper AI for audio, LLaVA for image processing, and Chroma DB for PDFs come together in a chat application.


Getting Started

To get started with Moai AI Chat, clone the repository and follow these simple steps:

Create a Virtual Environment: I am using Python 3.10.12 currently

Upgrade pip: pip install --upgrade pip

Install Requirements: pip install -r requirements.txt

Setting Up Local Models: Download the models you want to implement. Here is the llava model I used for image chat (ggml-model-q5_k.gguf and mmproj-model-f16.gguf). And the quantized mistral model form TheBloke (mistral-7b-instruct-v0.1.Q5_K_M.gguf).

Customize config file: Check the config file and change accordingly to the models you downloaded.

Enter commands in terminal:

python3 database_operations.py This will initialize the sqlite database for the chat sessions.
streamlit run app.py