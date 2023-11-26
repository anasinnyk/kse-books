import uuid


class AddCommand:
    def __init__(self, args):
        self.args = args

    def execute(self):
        with open("books.txt", "a") as f:
            id = uuid.uuid4()
            f.write(
                f"{id}|{self.args.name}|{self.args.author}|{self.args.year}\n")
            print(f"New book added with ID: {id}")
