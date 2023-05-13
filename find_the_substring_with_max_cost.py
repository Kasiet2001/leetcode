def maximumCostSubstring(s, chars, vals):
    ans = 0
    n = 0
    d = {chars[i]: vals[i] for i in range(len(chars))}
    for i in range(len(s)):
        if s[i] in chars:
            if n >= 0:
                n += d[s[i]]
            else:
                n = d[s[i]]
        else:
            if n >= 0:
                n += ord(s[i]) - 96
            else:
                n = ord(s[i]) - 96
        ans = max(ans, n)
    return ans
print(maximumCostSubstring("adaa","d",[-1000]))