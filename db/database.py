import sqlite3
import os

DB_PATH = os.path.join("data", "documents.db")

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the documents table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        path TEXT,
        thumbnail_path TEXT,
        tags TEXT,
        description TEXT,
        upload_date TEXT,
        lecture_date TEXT,
        total_pages INTEGER
        )
    """
    )
    conn.commit()
    print("Database initialized successfully.")
    conn.close()