def getGoodIndices(variables, target):
    ans = []
    for i, (a, b, c, m) in enumerate(variables):
        n = ((a ** b % 10) ** c) % m
        if n == target:
            ans.append(i)
    return ans
print(getGoodIndices([[39,3,1000,1000]], 17))