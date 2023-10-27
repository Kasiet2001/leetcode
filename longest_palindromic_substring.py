def longestPalindrome(s):
    ans = s[0]
    for i in range(len(s)):
        curr = s[i]
        for j in range(i + 1, len(s)):
            curr += s[j]
            if curr == curr[::-1] and len(curr) > len(ans):
                ans = curr
    return ans