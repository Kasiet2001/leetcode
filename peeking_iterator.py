class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.curr = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.curr

    def next(self):
        value = self.curr
        self.curr = self.iterator.next() if self.iterator.hasNext() else None
        return value

    def hasNext(self):
        return self.curr != None