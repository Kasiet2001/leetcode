def minOperations(nums):
    operations = 0
    flipped = False
    for num in nums:
        if not flipped and num == 0:
            operations += 1
            flipped = True
        elif flipped and num:
            operations += 1
            flipped = False
    return operations
print(minOperations([0,1,1,0,1]))



