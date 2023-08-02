import sqlite3

class MemoryDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY,
                title TEXT,
                identifier TEXT,
                date TEXT,
                people_involved TEXT,
                memory_triggers TEXT,
                summary TEXT
            )
        """)

    def insert_memory(self, title, identifier, date, people_involved, memory_triggers, summary):
        self.cursor.execute("""
            INSERT INTO memories (title, identifier, date, people_involved, memory_triggers, summary)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, identifier, date, people_involved, memory_triggers, summary))
        self.conn.commit()

    def fetch_memory(self, identifier):
        self.cursor.execute("SELECT * FROM memories WHERE identifier=?", (identifier,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()
