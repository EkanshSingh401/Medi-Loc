import csv
from datetime import datetime
from pathlib import Path

VALID_EVENT_TYPES = {"taken", "missed", "late"}


def load_events(csv_path: Path) -> list[dict]:
    events = []

    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            event = validate_and_transform(row)
            events.append(event)

    return events


def validate_and_transform(row: dict) -> dict:
    required_fields = ["patient_id", "medication", "timestamp", "event_type", "device_id"]

    for field in required_fields:
        if field not in row or not row[field].strip():
            raise ValueError(f"Missing required field: {field}")

    event_type = row["event_type"].strip().lower()
    if event_type not in VALID_EVENT_TYPES:
        raise ValueError(f"Invalid event_type: {event_type}")

    try:
        parsed_timestamp = datetime.fromisoformat(row["timestamp"].strip())
    except ValueError as exc:
        raise ValueError(f"Invalid timestamp format: {row['timestamp']}") from exc

    return {
        "patient_id": row["patient_id"].strip(),
        "medication": row["medication"].strip(),
        "timestamp": parsed_timestamp.isoformat(),
        "event_type": event_type,
        "device_id": row["device_id"].strip(),
    }
