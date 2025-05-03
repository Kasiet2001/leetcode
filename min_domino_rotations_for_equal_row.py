def minDominoRotations(tops, bottoms):
    n = len(tops)
    count1 = [0] * (n + 1)
    count2 = [0] * (n + 1)
    ans1 = [0] * (n + 1)
    ans2 = [0] * (n + 1)
    for i in range(n):
        count1[tops[i] - 1] += 1
        count2[bottoms[i] - 1] += 1
        if count1[i] == n or count2[i] == n:
            return 0
        ans1[tops[i] - 1] += 1
        ans2[bottoms[i] - 1] += 1
        if tops[i] != bottoms[i]:
            ans1[bottoms[i] - 1] += 1
            ans2[tops[i] - 1] += 1
    result = float('inf')
    for i in range(n + 1):
        if ans1[i] == n:
            result = min(result, ans1[i] - count1[i])
        if ans2[i] == n:
            result = min(result, ans2[i] - count2[i])
    return -1 if result == float('inf') else result
print(minDominoRotations([1,2,3,4,6], [6,6,6,6,5]))