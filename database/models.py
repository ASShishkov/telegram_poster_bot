from database.db import db_cursor

def add_post(message_id, source_channel_id, scheduled_time=None):
    with db_cursor() as cursor:
        cursor.execute(
            "INSERT INTO posts (message_id, source_channel_id, scheduled_time) VALUES (?, ?, ?)",
            (message_id, source_channel_id, scheduled_time)
        )

def get_pending_posts():
    with db_cursor() as cursor:
        cursor.execute("SELECT * FROM posts WHERE status = 'pending'")
        return cursor.fetchall()