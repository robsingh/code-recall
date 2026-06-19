import argparse
import sys
from add_problem import adding_problem
from due_today import show_due_today
from review import mark_reviewed
from parser import parse_problem_file

def handle_add(args):
    result = parse_problem_file(args.filepath)
    if isinstance(result, tuple):
        title, problem, solution = result
        adding_problem(title, problem, solution)
    else:
        print("Check the .md again!")


def handle_due(args):
    count, records = show_due_today()
    if count == 0:
        print("There are no entries in the table!")
    elif not records:
        print("No problems are due today, go to gym!")
    else:
        print("─" * 40)
        print(f"\n📚 {len(records)} problem(s) due for review today!\n")
        for record in records:
            print(f"Title            : {record[0]}")
            print(f"Solution         : {record[1]}")
            print(f"Current Stage    : {record[2]}")
            print(f"Next Review Date : {record[3]}")
        print("─" * 40)


def handle_review(args):
    result = mark_reviewed(args.title)
    if result["success"]:
        print(f"'{args.title}' marked as reviewed! Next review on {result['next_review_date']}.")
    else:
        print(f"'{args.title}' not found!")

parser = argparse.ArgumentParser(description="Code Recall - Spaced Repetition for Coders")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
add_parser.add_argument('filepath', help="Enter the filepath")
add_parser.set_defaults(func=handle_add)

due_parser = subparsers.add_parser('due')
due_parser.set_defaults(func=handle_due)

review_parser = subparsers.add_parser('review')
review_parser.add_argument('title', help="Enter the title")
review_parser.set_defaults(func=handle_review)

args = parser.parse_args()

if not hasattr(args, 'func'):
    parser.print_help()
    sys.exit(1)
else:
    args.func(args)