def generate_prompt(question: str) -> str:
    """
    Constructs the base prompt for the chatbot.
    """
    prompt = f"""
    Provide only the code. (NO PREAMBLE)

    Question: {question}
    Answer:
    """
    return prompt
