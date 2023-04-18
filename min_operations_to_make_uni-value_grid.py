def minOperations(grid, x):
    n = []
    for i in range(len(grid)):
        n.extend(grid[i])
    n.sort()
    ans = 0
    m = n[len(n) // 2]
    for i in n:
        if i % x:
            return -1
        ans += abs(i - m)
    return ans // x
print(minOperations([[1,5],[2,3]], 1))