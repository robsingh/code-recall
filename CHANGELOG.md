## Issues Encountered & Resolutions

### 1. Duplicate problem entries
- Issue: re-running add_problem.py inserted the same title multiple times.
- Fix: added UNIQUE constraint on title, switched to INSERT OR IGNORE, checked ```cursor.rowcount``` to detect skipped inserts.

### 2. ```datetime``` deprecation warning in sqlite3
- Issue: passing a raw datetime object to sqlite3 triggered a deprecation warning (this was initial coded in py3.7 :P)
- Fix: explicitly converted to string with .isoformat() before storing

### 3. Mixing data-fetching with presentation (separation of concerns)
- Issue: show_due_today() and mark_reviewed() originally printed output directly, making them unusable by the Flask API layer.
- Fix: refactored both to return data only; CLI (main.py) and API (app.py) each handle their own presentation

### 4.  Inconsistent return types causing fragile caller code
- Issue: mark_reviewed() returned False on failure but a tuple on success, forcing callers to use isinstance() checks.
- Fix: standardized to always return a dictionary ({"success": bool, ...}), removing the need for type-checking in callers.

### 5. Malformed markdown file crashing the parser
- Issue: .md files missing a ## Solution section caused IndexError on .split()
- Fix: added a check for required section headers before splitting; main.py validates the parser's return type before unpacking