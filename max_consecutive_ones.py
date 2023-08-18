def findMaxConsecutiveOnes(nums):
    ans = 0
    ones = 0
    for i in nums:
        if i == 1:
            ones += 1
            if ones > ans:
                ans = ones
        else:
            ones = 0
    return ans
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))