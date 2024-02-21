def maxJump(stones):
    ans = stones[1]
    for i in range(2, len(stones)):
        ans = max(ans, stones[i] - stones[i - 2])
    return ans
print(maxJump([0,2,5,6,7]))