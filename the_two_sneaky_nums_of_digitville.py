def getSneakyNumbers(nums):
    ans = []
    seen = set()
    for x in nums:
        if x in seen:
            ans.append(x)
        else:
            seen.add(x)
    return ans
print(getSneakyNumbers([0,3,2,1,3,2]))