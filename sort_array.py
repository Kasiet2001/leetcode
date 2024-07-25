from random import randint
def sortArray(nums):
    def partition(left, right):
        if left >= right:
            return

        pivot = nums[randint(left, right)]
        l, r, current = left - 1, right + 1, left
        while current < r:
            if nums[current] < pivot:
                l += 1
                nums[l], nums[current] = nums[current], nums[l]
                current += 1
            elif nums[current] > pivot:
                r -= 1
                nums[r], nums[current] = nums[current], nums[r]
            else:
                current += 1
        partition(left, l)
        partition(r, right)
    partition(0, len(nums) - 1)
    return nums
print(sortArray([5,2,3,1]))


