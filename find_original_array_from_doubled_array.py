def findOriginalArray(changed):
    from collections import Counter
    c = Counter(changed)
    zeros, m = divmod(c[0], 2)
    if m:
        return []
    ans = [0] * zeros
    for n in sorted(c.keys()):
        if c[n] > c[2 * n]:
            return []
        c[2 * n] -= c[n]
        ans.extend([n] * c[n])
    return ans
print(findOriginalArray([1, 2, 3, 4, 6, 8]))
