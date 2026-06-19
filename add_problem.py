'''This script will handle one job: adding a new problem to the database.'''
from database import initialize_db
from datetime import datetime, timedelta
import sqlite3
from config import STAGE_INTERVALS


def adding_problem(title, problem, solution):
    initialize_db()
    current_stage = 0
    current_date = datetime.now().isoformat(sep=' ', timespec='seconds')
    next_review_date = (datetime.now().date()+timedelta(days=STAGE_INTERVALS[0])).isoformat()
    
    with sqlite3.connect('recall.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
                "INSERT OR IGNORE INTO problems(title, problem, solution, notes, created_at, current_stage, next_review_date) VALUES (?,?,?,?,?,?,?)",
                (title, problem, solution, None, current_date, current_stage, next_review_date)
            )
        if cursor.rowcount == 0:
            print(f" '{title}' already exists in your recall list.")
        else:
            print(f"'{title}' added successfully on {current_date}!")
