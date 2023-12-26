class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = sum(nums)
        self.l = len(nums)

    def sumRange(self, left: int, right: int) -> int:
        sl = sr = 0
        for i in range(left):
            sl += self.nums[i]
        for j in range(right + 1, self.l):
            sr += self.nums[j]
        return self.s - sl - sr