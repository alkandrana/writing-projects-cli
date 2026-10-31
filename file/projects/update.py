import json
import sys
from pathlib import Path

from file.search import get_book_path


def load_json(path: str | Path):
    if Path(path).exists():
        with open(path, 'r') as f:
            data = json.load(f)
        return data
    else:
        print("File could not be found.")
        sys.exit(1)


def update_local_goal(value, book):
    print(f"Locating novel.json for {book}...")
    path = get_book_path(book) / "novel.json"
    book_details = load_json(path)
    book_details['goal'] = value
    with open(path, 'w') as f:
        json.dump(book_details, f)
    print(f"Updated goal in {path}: {book_details}")

