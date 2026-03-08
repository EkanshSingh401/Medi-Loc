from pathlib import Path

from pipeline import load_events
from storage import create_tables, get_connection, insert_events, summarize_events


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "sample_medication_events.csv"
    db_path = project_root / "mediloc.db"

    events = load_events(csv_path)

    conn = get_connection(db_path)
    create_tables(conn)
    insert_events(conn, events)

    summary = summarize_events(conn)

    print(f"Processed {len(events)} medication events.")
    print("Event summary:")
    for event_type, count in summary:
        print(f"  {event_type}: {count}")

    conn.close()


if __name__ == "__main__":
    main()
