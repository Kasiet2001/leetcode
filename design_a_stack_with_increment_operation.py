class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.arr = []
    def push(self, x: int) -> None:
        if len(self.arr) + 1 <= self.maxSize:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) > 0:
            return self.arr.pop()
        return -1
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val
