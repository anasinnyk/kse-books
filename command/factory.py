from command.add import AddCommand
from command.describe import DescribeCommand
from command.list import ListCommand


def create(args):
    if args.command == "add":
        return AddCommand(args)
    elif args.command == "describe":
        return DescribeCommand(args)
    elif args.command == "list":
        return ListCommand(args)
    else:
        print("unknown command")
        exit(1)
