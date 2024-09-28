from collections import deque
class MyCircularDeque:
    def __init__(self, k: int):
        self.q = deque([])
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.q) + 1 <= self.k:
            self.q.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) + 1 <= self.k:
            self.q.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.q) > 0:
            self.q.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.q) > 0:
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.q) > 0:
            return self.q[0]
        return -1

    def getRear(self) -> int:
        if len(self.q) > 0:
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k