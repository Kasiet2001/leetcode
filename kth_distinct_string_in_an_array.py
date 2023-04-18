def kthDistinct(arr, k):
    from collections import Counter
    s = Counter(arr)
    c = []
    for j, v in s.items():
        if v == 1:
            c.append(j)
    return c[k - 1] if len(c) >= k else ''
print(kthDistinct(["d","b","c","b","c","a"], 2))