def longestSemiRepetitiveSubstring(s):
    ans = 0
    n = [1]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            n.append(1)
        else:
            n[-1] += 1
    for j in range(1, len(n)):
        ans = max(ans, n[j] + n[j - 1])
    return n[0] if len(n) == 1 else ans
print(longestSemiRepetitiveSubstring("5494"))