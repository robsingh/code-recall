# Code Recall

Ever solve a coding problem, move on, and forget how you did it a month later? 
**Code Recall** fixes that — a spaced repetition CLI tool that reminds you to revisit problems you've already solved, before you forget them.


## What is this?
A command-line tool (with a Flask API layer) that tracks coding problems you've solved and schedules them for review using a spaced repetition algorithm — the same principle behind tools like Anki.


## Why I built this?
I dedicate one hour every morning to coding practice. The problem: I'd solve something, move on, and have no system to revisit it later — so the learning didn't stick. Code Recall is my answer to that. It logs every problem I solve and tells me exactly when to review it again, based on the spacing effect.


## Setup

### Requirements
Python 3.13.7

### Installation
```bash
git clone 
cd code_recall
pip install python-frontmatter flask
python app.py   # runs the Flask API on http://127.0.0.1:5000
```

## Usage

### CLI

```bash
python main.py add         # add a new problem from a .md file
python main.py due         # list problems due for review today
python main.py review ""   # mark a problem as reviewed
```

Run `python main.py -h` for full help.


### Adding a problem

Problems are added via a markdown file — see [`two_sum.md`](/code_recall/two_sum.md) for the expected format. Include a `title`, `notes`, a `## Problem` section, and a `## Solution` section. The parser reads this file and inserts it into the database.


### Checking due problems

```bash
python main.py due
```
Queries every problem where `next_review_date` is today or earlier.


### Marking a problem as reviewed

```bash
python main.py review "Two Sum"
```

Looks up the problem by title, logs the review timestamp, advances it to the next stage, and recalculates `next_review_date`.


## Spaced Repetition Schedule
Repetition Schedule is as follows:

| Stage  | Days until next review         | 
|--------|--------------------------------|
|   0    |       7                        |
|   1    |       28                       |
|   2    |       60                       |
|   3    |       180 (capped)             |


A problem is first due for review 7 days after it's added. Each successful review advances it to the next stage and a longer interval, capping at 180 days.


# Project Structure
code_recall/
├── config.py       — stage intervals, single source of truth
├── database.py     — schema, constraints, initialization
├── add_problem.py  — insert with duplicate protection
├── due_today.py    — query due problems
├── review.py       — spaced repetition logic
├── parser.py       — markdown file parser
├── main.py         — CLI entry point
├── app.py          - Flask API entry point
├── two_sum.md      — markdown file for adding a problem (example file)


## API Routes

| Method | Route                          | Description            |
|--------|--------------------------------|------------------------|
| POST   | `/problems`                    | Add a new problem      |
| GET    | `/problems/due`                | Get due problems       |
| PUT    | `/problems/<title>/review`     | Mark a problem reviewed|


# Roadmap
- [x] CLI tool with spaced repetition logic
- [x] Flask API wrapping core functions (see routes below)
- [ ] React frontend
- [ ] Rebuild in Go


## Issues Encountered & Resolutions

See [CHANGELOG.md](/code_recall/CHANGELOG.md) for a breakdown of bugs hit during development and how they were resolved.

