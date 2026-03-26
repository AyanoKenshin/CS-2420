class Node:
    def __init__(self, item):
        self.item = item
        self.L = None
        self.R = None


class Bag:

    def __init__(self):
        self.root = None

    def Insert(self, item):
        if self.root is None:
            self.root = Node(item)
            return True
        return self.InsertR(item, self.root)

    def InsertR(self, item, c):
        if item == c.item:
            return False
        elif item < c.item:
            if c.L is None:
                c.L = Node(item)
                return True
            return self.InsertR(item, c.L)
        else:
            if c.R is None:
                c.R = Node(item)
                return True
            return self.InsertR(item, c.R)

    def Exists(self, item):
        return self.ExistsR(item, self.root)

    def ExistsR(self, item, c):
        if c is None:
            return False
        elif item == c.item:
            return True
        elif item < c.item:
            return self.ExistsR(item, c.L)
        else:
            return self.ExistsR(item, c.R)

    def Retrieve(self, item):
        return self.RetrieveR(item, self.root)

    def RetrieveR(self, item, c):
        if c is None:
            return None
        elif item == c.item:
            return c.item
        elif item < c.item:
            return self.RetrieveR(item, c.L)
        else:
            return self.RetrieveR(item, c.R)

    def Size(self):
        return self.SizeR(self.root)

    def SizeR(self, c):
        if c is None:
            return 0
        return self.SizeR(c.L) + 1 + self.SizeR(c.R)

    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.root = self.DeleteR(item, self.root)
        return True

    def DeleteR(self, item, c):
        if item < c.item:
            c.L = self.DeleteR(item, c.L)
        elif item > c.item:
            c.R = self.DeleteR(item, c.R)
        else:
            if c.L is None and c.R is None:
                return None
            elif c.L is None:
                return c.R
            elif c.R is None:
                return c.L
            else:
                p = c.L
                while p.R is not None:
                    p = p.R
                c.item = p.item
                c.L = self.DeleteR(p.item, c.L)
        return c

    def __iter__(self):
        yield from self.IterR(self.root)

    def IterR(self, c):
        if c is not None:
            yield from self.IterR(c.L)
            yield c.item
            yield from self.IterR(c.R)