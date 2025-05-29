# Gemini Multi-Turn Chat

A simple interactive chatbot using the Google Gemini API that maintains conversation context across multiple turns. This project demonstrates how to create a context-aware chat application that remembers previous interactions.

## What the Script Does

This script creates an interactive chatbot that:
- Maintains conversation history across multiple turns
- Allows users to have natural, context-aware conversations
- Configures the model's creativity level through temperature settings
- Provides a simple console interface for interaction
- Preserves context between messages for coherent conversations

## Features

- Interactive console-based chat interface
- Context preservation across multiple conversation turns
- Configurable temperature parameter for response creativity
- Unlimited conversation turns
- Simple and clean implementation

## Setup and Dependencies

1. Clone this repository:
```bash
git clone https://github.com/Aabhi2002/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## How to Run

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies using pip
3. Set up your Gemini API key in the `.env` file
4. Run the script:
```bash
python gemini_chat.py
```

## Usage Instructions

- When prompted, enter a temperature value between 0.0 and 1.0 (default is 0.7)
  - Lower values (e.g., 0.2) make responses more focused and deterministic
  - Higher values (e.g., 0.8) make responses more creative and varied
- Type your messages and press Enter to chat
- Type 'exit' or 'quit' to end the conversation

## Requirements

- Python 3.7+
- google-generativeai
- python-dotenv
- Google Gemini API key

## Note

Make sure to keep your API key secure and never commit it to version control. The `.env` file is already included in `.gitignore` for security. 