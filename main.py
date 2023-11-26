import argparse

import command.factory as factory

parser = argparse.ArgumentParser(description="Manage books")

command_parser = parser.add_subparsers(title="command", dest="command")

add_parser = command_parser.add_parser("add", help="add a book")
list_parser = command_parser.add_parser("list", help="list all books")
describe_parser = command_parser.add_parser("describe", help="describe a book")

add_parser.add_argument("--name", "-n", help="name of the book")
add_parser.add_argument("--author", "-a", help="author of the book")
add_parser.add_argument("--year", "-y", type=int, help="year of the book")

describe_parser.add_argument("id", help="id of the book")

args = parser.parse_args()
factory.create(args).execute()
