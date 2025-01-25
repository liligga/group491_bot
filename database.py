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
            conn.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                year INTEGER,
                author TEXT,
                price INTEGER,
                cover TEXT
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

    def save_book(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO books (name, year, author, price, cover)
                VALUES (?, ?, ?, ?, ?)
            """,
                (data["name"], data["year"], data["author"], data["price"], data["cover"])
            )
            # conn.execute(    как не делать
            #     f"""INSERT INTO books (name, year, author, price)
            #      VALUES ({data['name']}, {data['year']}, {data['author']}, {data['price']})"""
            # )

    def get_all_books(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = conn.execute("SELECT * FROM books")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]