class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.reverse()
        i = self.items.pop()
        self.items.reverse()
        return i

    def peek(self, index):
        return self.items(index-1)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
