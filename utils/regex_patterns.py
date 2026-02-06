import re

SECTION_PATTERN = re.compile(
    r'\b[A-Z]{2}\d{2}-[A-Z]{3}-\d-[A-Z]\b'
)

SECTION_WITH_STRENGTH_PATTERN = re.compile(
    r'\b([A-Z]{2}\d{2}-[A-Z]{3}-\d-[A-Z])\s*\(\d+\)\b'
)

TIME_PATTERN = re.compile(
    r'\b\d{1,2}:\d{2}\s*-\s*\d{1,2}:\d{2}\b'
)

SLOT_PATTERN = re.compile(
    r'^[1-5]$'
)

TEACHER_PATTERN = re.compile(
    r'\b(Mr\.|Ms\.|Mrs\.|Dr\.|Engr\.)\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+'
)

VENUE_PATTERN = re.compile(
    r'\b(CL?ab-\d+|[A-Z]\d(?:\.\d)?|B\d+|D\d+|W\d+|A\d\.\d|Physics Lab|Networking Lab|DLD Lab)\b'
)
