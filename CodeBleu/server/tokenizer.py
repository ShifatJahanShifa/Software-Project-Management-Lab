import re


def custom_tokenizer(code):
    """
    Custom tokenizer function - customize this as needed
    This is a placeholder for your custom implementation
    """
    code = re.sub(r"//.*?$|/\*.*?\*/", "", code, flags=re.MULTILINE | re.DOTALL)
    tokens = re.findall(r"\b\w+\b|[{}();,\[\].]|[+\-*/=<>!&|]", code)
    tokens = [token.strip() for token in tokens if token.strip()]

    return tokens


def safe_tokenizer(code: str):
    # Split by word characters or single symbols, ignore empty tokens
    tokens = re.findall(r"\w+|[^\w\s]", code)
    return [t for t in tokens if t.strip()]
