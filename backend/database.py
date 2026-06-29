import sqlite3

def initialize_db():
    with sqlite3.connect('recall.db') as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS problems (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title VARCHAR UNIQUE,
                           problem VARCHAR,
                           solution VARCHAR,
                           notes VARCHAR,
                           created_at TEXT,
                           current_stage INTEGER,
                           next_review_date TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           problem_id INTEGER,reviewed_at TEXT,
                           FOREIGN KEY (problem_id) REFERENCES problems(id))''')
            

if __name__ == "__main__":
    initialize_db()


