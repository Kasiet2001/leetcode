def averageValue(nums):
    n = [i for i in nums if i % 2 == 0 and i % 3 == 0]
    return sum(n) // len(n) if len(n) > 0 else 0
print(averageValue([1,2,4,7,10]))