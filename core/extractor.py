import pdfplumber
from core.normalizer import normalize_text


def extract_pdf_lines(pdf_path: str) -> list[str]:
    all_lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            normalized_lines = normalize_text(text)
            all_lines.extend(normalized_lines)

    return all_lines
