import json
import sys
from pathlib import Path

from file.search import find_file


def get_book_details(code):
    title = input("Enter a name or title for the new book: ")
    series = input("Enter the series title for the new book (optional): ")
    goal = input("Enter your wordcount goal for the new book (100000): ")

    goal = int(goal or 100000)

    book = {
        "code": code,
        "title": title,
        "series": series if series else "N/A",
        "goal": goal,
    }
    return book


def create_book_structure(args):
    book_json = get_book_details(args.code)
    home_dir = find_file(args.world)
    if not home_dir or not home_dir.exists():
        print("Project directory could not be found.")
        sys.exit(1)
    else:
        scenes_home = Path(home_dir) / "books" / args.code.upper() / "manuscript" / "scenes"
        scenes_home.mkdir(parents=True, exist_ok=True)
        doc_file = home_dir / "books" / args.code.upper() / "novel.json"
        with open(doc_file, "w") as f:
            json.dump(book_json, f)
    print(f"Novel details printed to {doc_file}: {book_json}")

def parse_create_book(book_subparsers):
    create_parser = book_subparsers.add_parser("create")
    create_parser.add_argument("--code", "-c", required=True, help="Identifier for the new book, used as the folder name.")
    create_parser.add_argument("--world", "-w", required=True,
        help="The world or series name in which to creat the new book; should reflect the name of the parent directory.")
    create_parser.set_defaults(func=create_book_structure)
