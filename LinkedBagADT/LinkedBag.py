class Node:
    
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Bag:
    
    def __init__(self):
        self.head = None

    def Size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def Exists(self, item):
        current = self.head
        while current is not None:
            if item == current.item:
                return True
            current = current.next
        return False

    def Insert(self, item):
        if not self.Exists(item):
            new_node = Node(item, self.head)
            self.head = new_node
            return True
        return False

    def Retrieve(self, item):
        current = self.head
        while current is not None:
            if item == current.item:
                return current.item
            current = current.next
        return None

    def Delete(self, item):
        previous = None
        current = self.head
        while current is not None:
            if item == current.item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.item
            current = current.next