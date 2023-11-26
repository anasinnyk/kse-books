from command.add import AddCommand
from command.describe import DescribeCommand
from command.list import ListCommand


def create(args, db):
    if args.command == "add":
        return AddCommand(args, db)
    elif args.command == "describe":
        return DescribeCommand(args, db)
    elif args.command == "list":
        return ListCommand(args, db)
    else:
        print("unknown command")
        exit(1)
