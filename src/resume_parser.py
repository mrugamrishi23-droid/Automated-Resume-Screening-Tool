from pathlib import Path
from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path):
    """Extract text from PDF, DOCX, or TXT resume files."""
    path = Path(file_path)
    extension = path.suffix.lower()

    if extension == ".pdf":
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if extension == ".docx":
        document = Document(str(path))
        paragraphs = [p.text for p in document.paragraphs]
        table_text = [
            " ".join(cell.text for cell in row.cells)
            for table in document.tables for row in table.rows
        ]
        return "\n".join(paragraphs + table_text)

    if extension == ".txt":
        return path.read_text(encoding="utf-8", errors="ignore")

    raise ValueError(f"Unsupported file type: {extension}")
