from collections import defaultdict
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.ind_map = defaultdict(SortedList)
        self.occupied = {}

    def change(self, index: int, number: int) -> None:
        if index in self.occupied:
            old = self.occupied[index]
            self.ind_map[old].discard(index)
            if not self.ind_map[old]:
                del self.ind_map[old]
        self.ind_map[number].add(index)
        self.occupied[index] = number

    def find(self, number: int) -> int:
        if number in self.ind_map:
            return self.ind_map[number][0]
        return -1