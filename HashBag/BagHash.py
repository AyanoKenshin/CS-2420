class Bag:

    def __init__(self):
        self.size = 0
        startingCapacity = 100
        self.capacity = startingCapacity
        while self.IsPrime(self.capacity) == False:
            self.capacity += 1
        self.table = [None] * self.capacity

    def Hash(self, item):
        digits = item.ssn.replace("-", "")
        return int(digits)

    def Exists(self, item):
        key = self.Hash(item)
        index = key % self.capacity
        while True:
            if self.table[index] is None:
                return False
            if self.table[index] is not False and self.table[index] == item:
                return True
            index = (index + 1) % self.capacity

    def Insert(self, item):
        if self.Exists(item):
            return False

        if self.size * 2 >= self.capacity:
            self.Resize()

        key = self.Hash(item)
        index = key % self.capacity

        while self.table[index] is not None and self.table[index] is not False:
            index = (index + 1) % self.capacity

        self.table[index] = item
        self.size += 1
        return True

    def Delete(self, item):
        if not self.Exists(item):
            return False

        key = self.Hash(item)
        index = key % self.capacity

        while True:
            if self.table[index] is not False and self.table[index] == item:
                self.table[index] = False
                self.size -= 1
                return True
            index = (index + 1) % self.capacity

    def Retrieve(self, item):
        key = self.Hash(item)
        index = key % self.capacity

        while True:
            if self.table[index] is None:
                return None
            if self.table[index] is not False and self.table[index] == item:
                return self.table[index]
            index = (index + 1) % self.capacity

    def Size(self):
        return self.size

    def Capacity(self):
        return self.capacity

    def Resize(self):
        oldTable = self.table
        self.capacity = self.capacity * 2
        while self.IsPrime(self.capacity) == False:
            self.capacity += 1
        self.table = [None] * self.capacity
        self.size = 0

        for item in oldTable:
            if item is not None and item is not False:
                self.Insert(item)

    def __iter__(self):
        for item in self.table:
            if item is not None and item is not False:
                yield item

    def IsPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True