from collections import defaultdict
def canConvertString(s, t, k):
    if len(s) != len(t):
        return False
    d = defaultdict(int)
    for i in range(len(s)):
        if s[i] != t[i]:
            if ord(t[i]) > ord(s[i]):
                diff = ord(t[i]) - ord(s[i])
            else:
                diff = 26 - ord(s[i]) + ord(t[i])
            n = d[diff] * 26 + diff
            if n > k:
                return False
            d[diff] += 1
    return True
print(canConvertString("aab", "bbb", 27))