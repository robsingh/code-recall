import sqlite3
from database import initialize_db
from config import STAGE_INTERVALS
from datetime import datetime, timedelta

def mark_reviewed(title):
    initialize_db()
    
    with sqlite3.connect('recall.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, current_stage
                       FROM problems
                       WHERE title = ?
                       """, (title,))
        
        records = cursor.fetchone()
        if not records:
            return {"success": False}
        
        problem_id = records[0]
        current_stage = records[1]
        new_stage = min(current_stage + 1,3)
        days = STAGE_INTERVALS[new_stage]
        next_review_date = (datetime.now().date() + timedelta(days=days)).isoformat()
        current_date = datetime.now().isoformat(sep=' ', timespec='seconds')

        cursor.execute("""
                       INSERT INTO reviews (problem_id, reviewed_at)
                       VALUES (?,?)
                       """, (problem_id, current_date))
        
        cursor.execute("""
                       UPDATE problems
                       SET current_stage = ?, next_review_date = ?
                       WHERE title = ?
                       """,(new_stage, next_review_date, title))
        return {"success": True, "new_stage": new_stage, "next_review_date": next_review_date}
         

if __name__ == "__main__":
    mark_reviewed(title='Two Sum')