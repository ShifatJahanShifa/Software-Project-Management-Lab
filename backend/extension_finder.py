import re

EXT_MAP = {
    "python": "py",
    "py": "py",
    "javascript": "js",
    "js": "js",
    "typescript": "ts",
    "ts": "ts",
    "java": "java",
    "c": "c",
    "c++": "cpp",
    "cpp": "cpp",
    "go": "go",
    "rust": "rs",
    "rs": "rs",
    "html": "html",
    "json": "json",
    "bash": "sh",
    "sh": "sh",
}


LANG_ALIASES = {
    "python": ["python", "py"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript", "ts"],
    "java": ["java"],
    "c": ["c"],
    "cpp": ["cpp", "c++"],
    "go": ["go"],
    "rust": ["rust", "rs"],
    "html": ["html", "htm"],
    "json": ["json"],
    "bash": ["sh", "bash", "shell"],
}


def language_mentions(question: str, language: str) -> bool:
    """
    Check if the user question mentions a language or any of its aliases.
    """
    question = question.lower()
    aliases = LANG_ALIASES.get(language.lower(), [language.lower()])

    # Build regex: \b(alias1|alias2|...)\b
    pattern = r"\b(" + "|".join(re.escape(a) for a in aliases) + r")\b"

    return re.search(pattern, question) is not None


def detect_extension(code: str, question: str) -> str:
    lines = code.strip().split("\n")

    if not lines:
        return "txt"

    first_line = lines[0].strip()
    if first_line.startswith("```"):
        lang = first_line[3:].strip()
        return EXT_MAP.get(lang, "txt")
    else:
        if language_mentions(question=question, language="python"):
            return EXT_MAP["python"]
        elif language_mentions(question=question, language="javascript"):
            return EXT_MAP["javascript"]
        elif language_mentions(question=question, language="typescript"):
            return EXT_MAP["typescript"]
        elif language_mentions(question=question, language="java"):
            return EXT_MAP["java"]
        elif language_mentions(question=question, language="c"):
            return EXT_MAP["c"]
        elif language_mentions(question=question, language="cpp"):
            return EXT_MAP["cpp"]
        elif language_mentions(question=question, language="go"):
            return EXT_MAP["go"]
        elif language_mentions(question=question, language="html"):
            return EXT_MAP["html"]
        elif language_mentions(question=question, language="rust"):
            return EXT_MAP["rust"]
        elif language_mentions(question=question, language="json"):
            return EXT_MAP["json"]
        elif language_mentions(question=question, language="bash"):
            return EXT_MAP["bash"]
        else:
            return "txt"
