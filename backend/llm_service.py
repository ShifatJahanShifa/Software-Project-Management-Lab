import logging
import os

import google.generativeai as genai
from dotenv import load_dotenv
from mistralai import Mistral

from constants import MODEL
from extension_finder import detect_extension
from prompts import generate_prompt
from utils.code_cleaner import clean_code

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    logger.error(
        "MISTRAL_API_KEY not found in environment variables. Please check your .env file."
    )
else:
    logger.info("MISTRAL_API_KEY loaded successfully")

client = Mistral(api_key=api_key)


def generate_answer(question: str) -> str:
    try:
        if not api_key:
            return "Error: MISTRAL_API_KEY is not configured. Please create a .env file with your API key."

        prompt = generate_prompt(question)
        response = client.chat.complete(
            model=MODEL, messages=[{"role": "user", "content": prompt}]
        )
        code = response.choices[0].message.content
        extension = detect_extension(code, question)
        cleaned_code = clean_code(code)
        return cleaned_code, extension
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error generating answer: {error_msg}")

        if "API_KEY" in error_msg or "api key" in error_msg.lower():
            return f"API Key Error: {error_msg}. Please check your MISTRAL_API_KEY in the .env file."
        elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
            return (
                f"Quota/Limit Error: {error_msg}. Please check your API usage limits."
            )
        else:
            return f"Error: {error_msg}. Please try again later."
