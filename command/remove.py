class RemoveCommand:
    def __init__(self, args, db):
        self.args = args
        self.db = db

    def execute(self):
        is_removed = self.db.remove_by_id(self.args.id)

        print(
            "removed item {}".format(
                self.args.id) if is_removed else "item not found"
        )
