class SmallestInfiniteSet:
    def __init__(self):
        self.nums = list(range(1, 1001))

    def popSmallest(self) -> int:
        self.nums.sort()
        n = self.nums.pop(0)
        return n

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.append(num)