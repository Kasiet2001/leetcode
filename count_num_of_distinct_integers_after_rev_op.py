def countDistinctIntegers(nums):
    return len(set([int(str(i)[::-1]) for i in nums] + nums))
print(countDistinctIntegers([2,2,2]))