def clean_code(code: str) -> str:
    lines = code.strip().split("\n")

    if not lines:
        return None

    length = len(lines)
    length -= 1
    new_lines = lines[1:length]
    cleaned_code = "\n".join(new_lines)
    print(cleaned_code)
    return cleaned_code
