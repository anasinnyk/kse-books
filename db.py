import os
import uuid


class DBFile:
    def __init__(self, filename):
        self._fp = open(filename, "r+" if os.path.exists(filename) else "w+")
        self._separator = "|"

    def find_by_id(self, id):
        for records in self.list():
            if records[0] == id:
                return records
        return None

    def remove_by_id(self, id):
        if self.find_by_id(id) is None:
            return False
        else:
            self.save([r for r in self.list() if r[0] != id])
            return True

    def save(self, data):
        self._fp.seek(0)
        self._fp.truncate()
        for line in data:
            self._fp.write(self._separator.join([str(f) for f in line]) + "\n")

    def add(self, data):
        self._fp.seek(0, os.SEEK_END)
        id = uuid.uuid4()
        data.insert(0, id)
        self._fp.write(self._separator.join([str(f) for f in data]) + "\n")

    def list(self):
        self._fp.seek(0)
        return [l.strip("\n").split(self._separator) for l in self._fp.readlines()]

    def __del__(self):
        self._fp.close()
