from math import gcd
def minOperations(nums, numsDivide):
    d = 0
    for i in numsDivide:
        d = gcd(d, i)
    nums.sort()
    for i in range(len(nums)):
        if d % nums[i] == 0:
            return i
    return -1
print(minOperations([3,2,6,2,35,5,35,2,5,8,7,3,4], [105,70,70,175,105,105,105]))