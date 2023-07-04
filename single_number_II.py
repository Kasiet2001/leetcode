def singleNumber(nums):
    ones = 0
    twos = 0

    for num in nums:
        ones ^= (num & ~twos)
        twos ^= (num & ~ones)

    return ones
print(singleNumber([2,2,3,2]))