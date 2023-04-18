def findContentChildren(g, s):
    g.sort()
    s.sort()
    ch = 0
    c = 0
    ans = 0
    while ch < len(g) and c < len(s):
        if g[ch] <= s[c]:
            ans += 1
            ch += 1
        c += 1
    return ans
print(findContentChildren([1,2,4], [1,2,3,3]))