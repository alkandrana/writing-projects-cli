import argparse

from batch_post.sync import parse_sync
from file.projects import parse_book


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    parse_sync(subparsers)
    parse_book(subparsers)
    args = parser.parse_args()
    args.func(args)
