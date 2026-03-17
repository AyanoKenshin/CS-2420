class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node


class Bag:

    def __init__(self):
        self.head = None
        self.size = 0

    def Insert(self, item):
        if self.Exists(item):
            return False
        self.head = Node(item, self.head)
        self.size += 1
        return True

    def Exists(self, item):
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    def Size(self):
        return self.size

    def Delete(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.item == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def Retrieve(self, item):
        current = self.head
        while current is not None:
            if current.item == item:
                return current.item
            current = current.next
        return None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.item
            current = current.next