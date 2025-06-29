import sqlite3
from contextlib import contextmanager

DATABASE = "posts.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@contextmanager
def db_cursor():
    conn = get_db_connection()
    try:
        yield conn.cursor()
        conn.commit()
    finally:
        conn.close()

def init_db():
    with db_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id INTEGER NOT NULL,
                source_channel_id INTEGER NOT NULL,
                scheduled_time DATETIME,
                status TEXT DEFAULT 'pending'
            )
        """)