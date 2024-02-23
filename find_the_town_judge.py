def findJudge(n, trust):
    if n == 1:
        return n
    ans = [0] * (n + 1)
    for a, b in trust:
        ans[a] -= 1
        ans[b] += 1
    for i in range(len(ans)):
        if ans[i] == n - 1:
            return i
    return -1
print(findJudge(4, [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]))
