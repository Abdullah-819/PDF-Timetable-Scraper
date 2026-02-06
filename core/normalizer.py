import re

def normalize_text(raw_text: str) -> list[str]:
    lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
    result = []

    buffer = ""

    for line in lines:
        if len(line) <= 3 and re.fullmatch(r"[A-Za-z ]+", line):
            buffer += line.replace(" ", "")
            continue

        if buffer:
            result.append(buffer)
            buffer = ""

        line = re.sub(r"\s{2,}", " ", line)
        result.append(line)

    if buffer:
        result.append(buffer)

    cleaned = []
    for line in result:
        line = re.sub(r"FehmUlQuran|FehmUlQur an|FehmUl Qur an", "Fehm Ul Quran", line)
        cleaned.append(line.strip())

    return cleaned
