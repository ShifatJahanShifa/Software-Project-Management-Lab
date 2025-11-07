def generate_prompt(question: str) -> str:
    """
    Constructs the base prompt for the chatbot.
    """
    prompt = f"""
    Provide clear, concise, and useful answers to the question.

    Question: {question}
    Answer:
    """
    return prompt
