import argparse
import uuid

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
if args.command == "add":
    with open("books.txt", "a") as f:
        id = uuid.uuid4()
        f.write(f"{id}|{args.name}|{args.author}|{args.year}\n")
        print(f"New book added with ID: {id}")

elif args.command == "list":
    with open("books.txt", "r") as f:
        for line in f:
            id, name, author, year = line.strip().split("|")
            print(f"{id} {name} {author} {year}")

elif args.command == "describe":
    with open("books.txt", "r") as f:
        for line in f:
            id, name, author, year = line.strip().split("|")
            if id == args.id:
                print(f"{id} {name} {author} {year}")
                break
        else:
            print("Book not found")
            exit(1)
else:
    print("unknown command")
    exit(1)
