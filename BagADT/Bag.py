class Bag:
    
    def __init__(self):
        self.L = []

    def Size(self):
        return len(self.L)

    def Exists(self, item):
        for i in self.L:
            if item == i:
                return True
        return False

    def Insert(self, item):
        if self.Exists(item):
            return False
        self.L.append(item)
        return True

    def Retrieve(self, item):
        for i in self.L:
            if item == i:
                return i
        return None

    def Delete(self, item):
        for i in range(len(self.L)):
            if item == self.L[i]:
                self.L[i] = self.L[-1]
                self.L.pop()
                return True
        return False

    def __iter__(self):
        for i in self.L:
            yield i