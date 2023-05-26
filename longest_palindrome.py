from collections import Counter
def longestPalindrome(s):
    ans = 0
    mid = 0
    d = Counter(s)
    for i in d.values():
        if i % 2 == 1:
            mid += 1
            ans += i - 1
        else:
            ans += i
    return ans if mid == 0 else ans + 1
print(longestPalindrome('a'))