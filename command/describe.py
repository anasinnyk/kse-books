class DescribeCommand:
    def __init__(self, args):
        self.args = args

    def execute(self):
        with open("books.txt", "r") as f:
            for line in f:
                id, name, author, year = line.strip().split("|")
                if id == self.args.id:
                    print(f"{id} {name} {author} {year}")
                    break
            else:
                print("Book not found")
                exit(1)
