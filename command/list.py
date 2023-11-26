class ListCommand:
    def __init__(self, args):
        self.args = args

    def execute(self):
        with open("books.txt", "r") as f:
            for line in f:
                id, name, author, year = line.strip().split("|")
                print(f"{id} {name} {author} {year}")
