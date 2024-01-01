from collections import defaultdict
import random
class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.index_map = defaultdict(list)
        for i in range(len(self.nums)):
            self.index_map[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_map[target])