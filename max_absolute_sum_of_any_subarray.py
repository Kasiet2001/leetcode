def maxAbsoluteSum(nums):
    max_sum = min_sum = 0
    curr1 = curr2 = 0
    for n in nums:
        if curr1 + n <= 0:
            curr1 = 0
        else:
            curr1 += n
            max_sum = max(max_sum, curr1)
        if curr2 + n >= 0:
            curr2 = 0
        else:
            curr2 += n
            min_sum = min(min_sum, curr2)
    return max(max_sum, abs(min_sum))
print(maxAbsoluteSum([1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1]))

