from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        self.data = []
        self.index_map = defaultdict(list)
        self.count_map = defaultdict(int)

    def insert(self, val: int) -> bool:
        self.data.append(val)
        self.index_map[val].append(len(self.data) - 1)
        self.count_map[val] += 1
        return self.count_map[val] == 1

    def remove(self, val: int) -> bool:
        if not self.count_map[val]:
            return False

        last_elem = self.data[-1]
        val_index = self.index_map[val].pop()

        if val_index != len(self.data) - 1:
            self.index_map[last_elem].remove(len(self.data) - 1)
            self.index_map[last_elem].append(val_index)
            self.data[val_index] = last_elem

        self.data.pop()
        self.count_map[val] -= 1

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
