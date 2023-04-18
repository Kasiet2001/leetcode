def divideArray(nums):
    total = 0
    if len(nums) % 2 == 0:
        for i in set(nums):
            if nums.count(i) % 2 == 0:
                total += 1
        return len(set(nums)) == total
    return False
print(divideArray([1,2,3,4]))