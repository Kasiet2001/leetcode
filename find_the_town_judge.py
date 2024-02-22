def findJudge(n, trust):
    ans = [0] * (n + 1)
    for a, b in trust:
        ans[a] -= 1
        ans[b] += 1
    for i in range(len(ans)):
        if ans[i] == n - 1:
            return i
    return -1
print(findJudge(2, [[1,2]]))
