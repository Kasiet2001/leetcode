def arraySign(nums):
    neg = 0
    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            neg += 1
    return 1 if neg % 2 == 0 else -1
print(arraySign([-1,1,-1,1,-1]))