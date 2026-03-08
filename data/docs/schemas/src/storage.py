import sqlite3
from pathlib import Path


def get_connection(db_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(db_path)


def create_tables(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS medication_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT NOT NULL,
            medication TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            event_type TEXT NOT NULL,
            device_id TEXT NOT NULL
        )
        """
    )

    conn.commit()


def insert_event(conn: sqlite3.Connection, event: dict) -> None:
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO medication_events
        (patient_id, medication, timestamp, event_type, device_id)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            event["patient_id"],
            event["medication"],
            event["timestamp"],
            event["event_type"],
            event["device_id"],
        ),
    )

    conn.commit()


def insert_events(conn: sqlite3.Connection, events: list[dict]) -> None:
    for event in events:
        insert_event(conn, event)


def summarize_events(conn: sqlite3.Connection) -> list[tuple]:
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT event_type, COUNT(*)
        FROM medication_events
        GROUP BY event_type
        ORDER BY event_type
        """
    )

    return cursor.fetchall()
