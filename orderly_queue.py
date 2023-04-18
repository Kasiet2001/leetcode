def orderlyQueue(s, k):
    if k > 1:
        return ''.join(sorted(s))
    ans = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        ans = min(ans, s)
    return ans
print(orderlyQueue("tk", 1))