def beautifulIndices(s, a, b, k):
    ans = set()
    a_occur = []
    b_occur = []
    n = len(s)
    for idx in range(n):
        if idx + len(a) <= n and s[idx: idx + len(a)] == a:
            a_occur.append(idx)
        if idx + len(b) <= n and s[idx: idx + len(b)] == b:
            b_occur.append(idx)
    i = len(a_occur) - 1
    j = len(b_occur) - 1
    while i >= 0 and j >= 0:
        if abs(b_occur[j] - a_occur[i]) > k and a_occur[i] < b_occur[j]:
            j -= 1
        elif abs(b_occur[j] - a_occur[i]) <= k:
            ans.add(a_occur[i])
            i -= 1
        else:
            i -= 1
    return sorted(ans)
print(beautifulIndices("rinzbrrr", "nzb", "r", 2))


