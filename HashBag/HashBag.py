class Bag:

    def __init__(self, table_size=1009):
        self.table_size = table_size
        self.table = []
        for i in range(self.table_size):
            self.table.append([])
        self.count = 0

    def _hash(self, item):
        total = 0
        for ch in item.ssn:
            if ch != '-':
                total += ord(ch)
        return total % self.table_size

    def Insert(self, item):
        index = self._hash(item)
        bucket = self.table[index]

        for existing in bucket:
            if existing == item:
                return False

        bucket.append(item)
        self.count += 1
        return True

    def Exists(self, item):
        index = self._hash(item)
        bucket = self.table[index]

        for existing in bucket:
            if existing == item:
                return True

        return False

    def Retrieve(self, item):
        index = self._hash(item)
        bucket = self.table[index]

        for existing in bucket:
            if existing == item:
                return existing

        return None

    def Size(self):
        return self.count

    def Delete(self, item):
        index = self._hash(item)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i] == item:
                del bucket[i]
                self.count -= 1
                return True

        return False

    def __iter__(self):
        for bucket in self.table:
            for item in bucket:
                yield item