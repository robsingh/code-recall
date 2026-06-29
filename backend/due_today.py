from database import initialize_db
from datetime import datetime
import sqlite3


def show_due_today():
    initialize_db()

    with sqlite3.connect('recall.db') as conn:
        cursor = conn.cursor()
        current_date = datetime.now().isoformat(sep=' ', timespec='seconds')
        cursor.execute("""
                       SELECT title, solution, current_stage, next_review_date
                       FROM problems
                       WHERE next_review_date <= ?
                       """, (current_date,))
        records = cursor.fetchall()

        cursor.execute("""
                       SELECT COUNT(*)
                       FROM problems
                       """)
        count = cursor.fetchone()[0]
        return count, records
        
if __name__ == "__main__":
    show_due_today()

