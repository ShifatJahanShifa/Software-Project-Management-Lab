def clean_code(code: str) -> str:
    lines = code.strip().split("\n")

    if not lines:
        return ""

    length = len(lines)
    length -= 1
    new_lines = lines[1:length]
    cleaned_code = "\n".join(new_lines)

    return cleaned_code
