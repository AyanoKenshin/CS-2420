class Bag:

    def __init__(self):
        self.L = []

    def Insert(self, item):
        if self.Exists(item):
            return False
        self.L.append(item)
        return True

    def Exists(self, item):
        for i in range(len(self.L)):
            if self.L[i] == item:
                return True
        return False

    def Size(self):
        return len(self.L)

    def Delete(self, item):
        for i in range(len(self.L)):
            if self.L[i] == item:
                self.L[i] = self.L[-1]
                self.L.pop()
                return True
        return False

    def Retrieve(self, item):
        for i in range(len(self.L)):
            if self.L[i] == item:
                return self.L[i]
        return None

    def __iter__(self):
        for x in self.L:
            yield x