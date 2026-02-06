# 📄 PDF Timetable Scraper

A **robust, deterministic Python utility** for extracting **structured class timetables** from noisy, non-tabular university PDF files.

This project is designed for **personal academic use**, focusing on **accuracy, proof-based parsing, and offline execution**.

---

## 🎯 Purpose

University timetable PDFs are usually:

- ❌ Not real tables  
- ❌ Full of broken words and spacing  
- ❌ Mixing multiple sections together  
- ❌ Missing explicit OFF-day markers  

Simple regex or table extractors **do not work reliably**.

This project solves the problem using **state-based parsing** and **exact section matching**.

---

## ✅ What This Scraper Extracts

For a given section/batch identifier, for example:
FA24-BCS-4-E


The scraper extracts the following fields:

- **DAY**
- **SLOT** (1–5)
- **TIME**
- **SUBJECT**
- **TEACHER**
- **VENUE**

### 💤 OFF Day Rule

If **all fields are absent for a specific day**, that day is **automatically considered OFF**.

- No guessing  
- No assumptions  
- No false positives  

---

## 🧠 Core Design Principles

- Deterministic parsing (not heuristic-based)
- Day-boundary detection
- Slot–time normalization
- Exact section proof-of-presence
- Default OFF-day inference
- Fully offline & private execution
- Minimal dependencies

---

## 📁 Project Structure



PDF-Timetable-Scraper/
│
├── data/
│ └── timetable.pdf
│
├── output/
│ └── FA24-BCS-4-E.json
│
├── core/
│ ├── extractor.py
│ ├── normalizer.py
│ ├── parser.py
│ ├── matcher.py
│ └── constants.py
│
├── utils/
│ ├── regex_patterns.py
│ └── helpers.py
│
├── cli.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE


---

## 📤 Example Output

```json
{
  "section": "FA24-BCS-4-E",
  "days": {
    "Monday": [
      {
        "slot": 1,
        "time": "8:30 - 9:55",
        "subject": "Information Security",
        "teacher": "Ms. Azka Riaz",
        "venue": "C2.4"
      }
    ],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
  }
}


An empty array ([]) means the day is OFF.

🚀 Installation

Clone or create the repository locally

Place your timetable PDF in the data/ directory

Install dependencies:

pip install -r requirements.txt

▶️ Usage (CLI)

Run the scraper by providing a section code:

python cli.py FA24-BCS-4-E


The output will be generated in:

output/FA24-BCS-4-E.json

📦 Dependencies

Minimal and stable:

pdfplumber


No OCR

No cloud APIs

No uploads

No tracking

🔐 Privacy & Scope

Fully offline execution

No network calls

No data collection

Intended strictly for personal academic use

Not designed for bulk scraping or public deployment

⚠️ Limitations

Tailored to specific timetable PDF layouts

Major layout changes may require parser adjustments

Does not support scanned/image-only PDFs

🛠 Possible Extensions

Semester-wise aggregation

CSV / Excel export

REST API wrapper for internal tools

Timetable clash detection

Integration with dashboards or portals

📌 Disclaimer

This project parses text-based PDFs only.
Scanned or image-based PDFs are not supported.

Built with precision, not shortcuts.
