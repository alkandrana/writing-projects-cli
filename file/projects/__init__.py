from new_project import parse_create_book


def parse_book(subparsers):
    book_parser = subparsers.add_parser("book")
    book_subparsers = book_parser.add_subparsers(dest="sub2command")
    parse_create_book(book_subparsers)
