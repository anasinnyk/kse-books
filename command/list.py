class ListCommand:
    def __init__(self, args, db):
        self.args = args
        self.db = db

    def execute(self):
        for record in self.db.list():
            print(" ".join(record))
