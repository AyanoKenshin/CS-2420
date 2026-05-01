class Node:
    
    def __init__(self, item, left, right):
        self.item = item
        self.L = left
        self.R = right


class Bag:
    
    def __init__(self):
        self.root = None

    def Size(self):
        return self.SizeR(self.root)
    
    def SizeR(self, c):
        if c is None:
            return 0
        return self.SizeR(c.L) + 1 + self.SizeR(c.R)

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

    def Insert(self, item):
        if self.Exists(item):
            return False
        n = Node(item, None, None)
        self.root = self.InsertR(n, self.root)
        return True

    def InsertR(self, n, c):
        if c is None:
            return n
        elif n.item < c.item:
            c.L = self.InsertR(n, c.L)
        else:
            c.R = self.InsertR(n, c.R)
        return c

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

    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.root = self.DeleteR(item, self.root)
        return True

    def DeleteR(self, item, c):
        if item < c.item:
            c.L = self.DeleteR(item, c.L)
        elif c.item < item:
            c.R = self.DeleteR(item, c.R)
        else:
            if c.L is None and c.R is None:
                return None
            elif c.L is None:
                return c.R
            elif c.R is None:
                return c.L
            else:
                pred = c.L
                while pred.R is not None:
                    pred = pred.R
                c.item = pred.item
                c.L = self.DeleteR(pred.item, c.L)
        return c

    def __iter__(self):
        yield from self.IterR(self.root)

    def IterR(self, c):
        if c is not None:
            yield from self.IterR(c.L)
            yield c.item
            yield from self.IterR(c.R)