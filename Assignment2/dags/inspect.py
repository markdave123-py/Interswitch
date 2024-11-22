import sqlite3
from utils.config import get_config


def inspect_db():
    db_path = get_config("DB_PATH")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)

    cursor.execute("SELECT * FROM weekend_metrics;")
    rows = cursor.fetchall()
    print("Data in weekend_metrics:")
    for row in rows:
        print(row)

    conn.close()
