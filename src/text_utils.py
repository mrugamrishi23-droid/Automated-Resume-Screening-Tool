import re
from pathlib import Path

def clean_text(text):
    """Normalize text while preserving useful words, numbers, and symbols."""
    text = text.lower()
    text = re.sub(r"[\r\t]", " ", text)
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def load_required_skills(path):
    """Read one skill per line; ignore blank lines and comments."""
    path = Path(path)
    return [
        line.strip().lower()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
