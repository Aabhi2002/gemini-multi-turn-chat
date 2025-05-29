import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Ask user for temperature setting
try:
    temp_input = input("Enter temperature (0.0 - 1.0, default is 0.7): ").strip()
    temperature = float(temp_input) if temp_input else 0.7
except ValueError:
    print("Invalid input. Using default temperature = 0.7")
    temperature = 0.7

# Initialize Gemini model with user-defined temperature
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": temperature
    }
)

# Start a chat session
chat = model.start_chat()

# Console loop for unlimited turns
print("\n🔵 Gemini Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}\n")
