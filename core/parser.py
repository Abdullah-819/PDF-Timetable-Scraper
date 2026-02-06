from core.constants import DAYS, SLOTS
from utils.regex_patterns import TEACHER_PATTERN, VENUE_PATTERN


def parse_timetable(tables: list, target_section: str) -> dict:
    timetable = {day: [] for day in DAYS}

    for table in tables:
        if len(table) < 3:
            continue

        target_row = None
        for row in table:
            if row and row[0] and target_section in row[0]:
                target_row = row
                break

        if not target_row:
            continue

        day = DAYS[len([d for d in timetable.values() if d])]
        header = table[1]

        for col_index, slot in enumerate(SLOTS, start=1):
            if col_index >= len(target_row):
                continue

            if "Break" in header[col_index]:
                continue

            cell = target_row[col_index].strip()
            if not cell:
                continue

            teacher = None
            venue = None

            teacher_match = TEACHER_PATTERN.search(cell)
            venue_match = VENUE_PATTERN.search(cell)

            if teacher_match:
                teacher = teacher_match.group(0)

            if venue_match:
                venue = venue_match.group(0)

            subject = cell

            if teacher:
                subject = subject.replace(teacher, "").strip()

            if venue:
                subject = subject.replace(venue, "").strip()

            subject = subject.replace("(1 hr)", "").strip()

            timetable[day].append({
                "slot": slot,
                "time": SLOTS[slot],
                "subject": subject,
                "teacher": teacher,
                "venue": venue
            })

    return timetable
