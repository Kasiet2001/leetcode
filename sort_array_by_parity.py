def sortArrayByParity(nums):
    sorted = []
    for i in nums:
        if i % 2 == 0:
            sorted.insert(0, i)
        else:
            sorted.append(i)
    return sorted
print(sortArrayByParity([0]))