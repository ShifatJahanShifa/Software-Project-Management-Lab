import re


def remove_python_comments(code: str) -> str:
    code = re.sub(r"#.*", "", code)
    code = re.sub(r'(""".*?""")|(\'\'\'.*?\'\'\')', "", code, flags=re.DOTALL)
    return code.strip()


def remove_c_style_comments(code: str) -> str:
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    code = re.sub(r"//.*", "", code)
    return code.strip()


def remove_comments(code: str, language: str) -> str:
    language = language.lower()
    if language in ["python"]:
        return remove_python_comments(code)
    elif language in ["c", "cpp", "java", "javascript", "typescript"]:
        return remove_c_style_comments(code)
    else:
        return code
