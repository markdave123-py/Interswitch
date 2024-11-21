import sqlite3


def connect_to_db(db_path):

    return sqlite3.connect(db_path)

def create_table_if_not_exists(db_path):

    conn = connect_to_db(db_path)
    cursor = conn.cursor()

    # SQL to create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weekend_metrics (
        month TEXT PRIMARY KEY,
        sat_mean_trip_count REAL,
        sat_mean_fare_per_trip REAL,
        sat_mean_duration_per_trip REAL,
        sun_mean_trip_count REAL,
        sun_mean_fare_per_trip REAL,
        sun_mean_duration_per_trip REAL
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()




def insert_metrics(db_path, metrics):

    conn = create_table_if_not_exists(db_path)

    conn = connect_to_db(db_path)
    cursor = conn.cursor()

    query = """
        INSERT OR REPLACE INTO weekend_metrics (
            month,
            sat_mean_trip_count, sat_mean_fare_per_trip, sat_mean_duration_per_trip,
            sun_mean_trip_count, sun_mean_fare_per_trip, sun_mean_duration_per_trip
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(query, metrics)
    conn.commit()
    conn.close()
