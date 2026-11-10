import csv
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

FILES = {
    "research": "research.csv",
    "projects": "projects.csv",
    "news": "news.csv",
    "journals": "journals.csv",
    "conferences": "conferences.csv",
    "patentsGranted": "patents_granted.csv",
    "patentsFiled": "patents_filed.csv",
    "currentPeople": "current_people.csv",
    "alumni": "alumni.csv",
    "studentProjects": "student_projects.csv",
    "activities": "activities.csv",
    "awards": "awards.csv",
}

def _convert_value(value: str) -> Any:
    value = (value or "").strip()
    if value == "":
        return ""
    # Keep years numeric where possible for existing frontend display/sorting.
    if value.isdigit():
        try:
            return int(value)
        except ValueError:
            pass
    return value

def read_csv(name: str) -> list[dict]:
    filename = FILES.get(name)
    if not filename:
        raise KeyError(name)
    path = DATA_DIR / filename
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    result = []
    for row in rows:
        item = {
            key: (int(value) if key == "year" and (value or "").strip().isdigit()
                  else (value or "").strip())
            for key, value in row.items()
        }
        # Fields used as arrays by the existing frontend.
        if name == "research":
            item["tags"] = [part.strip() for part in item.get("tags", "").split(";") if part.strip()]
        elif name == "activities":
            item["items"] = [part.strip() for part in item.get("items", "").split(" || ") if part.strip()]
        elif name == "studentProjects":
            item = item.get("item", "")
        result.append(item)
    return result

def read_all() -> dict:
    # CSVs are read from disk on every request: no process restart or cache flush needed.
    return {key: read_csv(key) for key in FILES}
