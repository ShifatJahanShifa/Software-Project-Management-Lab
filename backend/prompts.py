def generate_prompt(question: str) -> str:
    """
    Constructs the base prompt for the chatbot.
    """
    prompt = f"""
    You are an intelligent, polite, and helpful assistant.
    Always provide clear, concise, and useful answers to the questions.

    Question: {question}
    Answer:
    """
    return prompt
