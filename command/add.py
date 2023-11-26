class AddCommand:
    def __init__(self, args, db):
        self.db = db
        self.args = args

    def execute(self):
        self.db.add([self.args.name, self.args.author, self.args.year])
        print(f"New book added with ID: {id}")
