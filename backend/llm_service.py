import os
import logging

import google.generativeai as genai
from dotenv import load_dotenv
from prompts import generate_prompt

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    logger.error("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
else:
    logger.info("GEMINI_API_KEY loaded successfully")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-pro")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def generate_answer(question: str) -> str:
    try:
        if not api_key:
            return "Error: GEMINI_API_KEY is not configured. Please create a .env file with your API key."
        
        prompt = generate_prompt(question)
        messages.append({"role": "user", "content": prompt})
        conversation_prompt = ""
        for msg in messages:
            role = msg["role"].capitalize()
            conversation_prompt += f"{role}: {msg['content']}\n"
        response = model.generate_content(conversation_prompt)
        messages.append({"role": "assistant", "content": response.text})
        return response.text
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error generating answer: {error_msg}")
       
        if "API_KEY" in error_msg or "api key" in error_msg.lower():
            return f"API Key Error: {error_msg}. Please check your GEMINI_API_KEY in the .env file."
        elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
            return f"Quota/Limit Error: {error_msg}. Please check your API usage limits."
        else:
            return f"Error: {error_msg}. Please try again later."
