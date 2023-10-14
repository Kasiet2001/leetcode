def separateDigits(nums):
    ans = []
    for i in nums:
        ans.extend([int(j) for j in str(i)])
    return ans
print(separateDigits([13,25,83,77]))