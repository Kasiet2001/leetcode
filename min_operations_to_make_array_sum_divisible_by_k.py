def minOperations(nums, k):
    return sum(nums) % k
print(minOperations([3,9,7], 5))