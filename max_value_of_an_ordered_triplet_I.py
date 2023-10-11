def maximumTripletValue(nums):
    ans = 0
    maximum = 0
    max_diff = 0
    for i in nums:
        ans = max(ans, max_diff * i)
        max_diff = max(max_diff, maximum - i)
        maximum = max(maximum, i)
    return ans
print(maximumTripletValue([12,6,1,2,7]))