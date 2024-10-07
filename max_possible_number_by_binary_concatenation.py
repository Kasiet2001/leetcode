def maxGoodNumber(nums):
    nums = [bin(num)[2:] for num in nums]
    nums.sort(key=lambda x: x * 10, reverse=True)
    res = ''.join(nums)
    return int(res, 2)
print(maxGoodNumber([1,2,3]))