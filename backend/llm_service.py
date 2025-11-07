import os

import google.generativeai as genai
from dotenv import load_dotenv
from prompts import generate_prompt

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")


def generate_answer(question: str) -> str:
    try:
        prompt = generate_prompt(question)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM Error: {e}"
