def findNumbers(nums):
    return sum([1 for i in nums if len(str(i)) % 2 == 0])
print(findNumbers([555,901,482,1771]))