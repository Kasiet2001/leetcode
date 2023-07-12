def largeGroupPositions(s):
    ans = []
    start = 0
    s += '1'
    for i, ch in enumerate(s):
        if s[start] != ch:
            if i - start >= 3:
                ans.append([start, i - 1])
            start = i
    return ans
print(largeGroupPositions("abbxxxxzzy"))

