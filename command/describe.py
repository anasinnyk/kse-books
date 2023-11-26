class DescribeCommand:
    def __init__(self, args, db):
        self.args = args
        self.db = db

    def execute(self):
        book = self.db.find_by_id(self.args.id)
        if not book:
            print("Book not found")
            exit(1)
        id, name, author, year = book
        print(f"{id} {name} {author} {year}")
