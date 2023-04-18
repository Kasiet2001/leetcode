def smallerNumbersThanCurrent(nums):
    m = []
    for i in nums:
        s = 0
        for j in nums:
            if i > j:
                s += 1
        m.append(s)
    return m
print(smallerNumbersThanCurrent([7,7,7,7]))