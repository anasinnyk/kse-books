import uuid


class DBFile:
    def __init__(self, filename):
        self._afp = open(filename, "a")
        self._rfp = open(filename, "r")
        self._separator = "|"

    def find_by_id(self, id):
        for records in self.list():
            if records[0] == id:
                return records
        return None

    def add(self, data):
        id = uuid.uuid4()
        data.insert(0, id)
        self._afp.write(self._separator.join([str(f) for f in data]) + "\n")

    def list(self):
        return [l.split(self._separator) for l in self._rfp.readlines()]

    def __del__(self):
        self._afp.close()
        self._rfp.close()
