def countPalindromicSubsequence(s):
    ans = 0
    unique = set(s)
    for i in unique:
        start = s.find(i)
        end = s.rfind(i)
        if start < end:
            ans += len(set(s[start + 1: end]))
    return ans
print(countPalindromicSubsequence("aabca"))