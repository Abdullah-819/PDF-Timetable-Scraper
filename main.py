import json
from core.extractor import extract_pdf_tables
from core.parser import parse_timetable


PDF_PATH = "data/timetable.pdf"


def run(section_code: str):
    tables = extract_pdf_tables(PDF_PATH)
    timetable = parse_timetable(tables, section_code)

    output = {
        "section": section_code,
        "days": timetable
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    run("FA24-BCS-4-E")
