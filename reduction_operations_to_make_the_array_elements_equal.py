from collections import Counter
def reductionOperations(nums):
    ans = 0
    nums.sort(reverse=True)
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            ans += i + 1
    return ans
print(reductionOperations([1,1,2,2,3]))
