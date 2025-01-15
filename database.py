import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute("""
            CREATE TABLE IF NOT EXISTS complaints(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                complaint TEXT
            )
            """)

    def save_complaint(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO complaints (name, age, complaint)
                VALUES (?, ?, ?)
            """,
                (data["name"], data["age"], data["complaint"])
            )


# conn = sqlite3.connect("db.sqlite")
# cursor = conn.cursor()
# with sqlite3.connect("db.sqlite") as conn:
#     cursor = conn.cursor()
#     conn.execute("""
#     CREATE TABLE IF NOT EXISTS complaints(
       
#     )
#     """)