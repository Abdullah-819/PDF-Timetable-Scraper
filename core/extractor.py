import pdfplumber


def extract_pdf_tables(pdf_path: str) -> list[list[list[str]]]:
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables({
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
                "intersection_tolerance": 5
            })

            for table in tables:
                cleaned_table = []
                for row in table:
                    if not row:
                        continue
                    cleaned_row = [
                        cell.strip().replace("\n", " ") if cell else ""
                        for cell in row
                    ]
                    cleaned_table.append(cleaned_row)

                if cleaned_table:
                    all_tables.append(cleaned_table)

    return all_tables
