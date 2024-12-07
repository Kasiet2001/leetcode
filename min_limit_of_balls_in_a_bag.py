from math import ceil
def minimumSize(nums, maxOperations):

    def is_possible(max_balls_in_bag, nums, maxOperations):
        total_operations = 0
        for num in nums:
            operations = ceil(num / max_balls_in_bag) - 1
            total_operations += operations
            if total_operations > maxOperations:
                return False
        return True

    left = 1
    right = max(nums)
    while left < right:
        middle = (left + right) // 2
        if is_possible(middle, nums, maxOperations):
            right = middle
        else:
            left = middle + 1
    return left
print(minimumSize([2,4,8,2], 4))
