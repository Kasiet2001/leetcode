def getMaximumXor(nums, maximumBit):
    xor = 0
    for n in nums:
        xor ^= n
    mask = (1 << maximumBit) - 1
    ans =[]
    for n in reversed(nums):
        ans.append(xor ^ mask)
        xor ^= n
    return ans
print(getMaximumXor([0,1,1,3], 2))