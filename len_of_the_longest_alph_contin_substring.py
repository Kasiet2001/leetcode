def longestContinuousSubstring(s):
    ans = [1 for _ in range(len(s))]
    for i in range(1, len(s)):
        if ord(s[i]) == ord(s[i - 1]) + 1:
            ans[i] = ans[i - 1] + 1
    return max(ans)
print(longestContinuousSubstring("abcdacaba"))