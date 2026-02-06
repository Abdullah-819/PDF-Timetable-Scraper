from core.extractor import extract_pdf_lines

lines = extract_pdf_lines("data/timetable.pdf")

print("Total lines:", len(lines))
print("First 40 lines:")
for l in lines[:40]:
    print(l)
