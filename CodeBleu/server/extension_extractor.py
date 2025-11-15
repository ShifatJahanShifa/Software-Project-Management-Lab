import os

EXT_LANG_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp"
}

def get_language_from_extension(filename: str) -> str:
    _, ext = os.path.splitext(filename)
    return EXT_LANG_MAP.get(ext.lower(), "txt")  