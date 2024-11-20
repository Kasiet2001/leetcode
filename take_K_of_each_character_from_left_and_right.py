def takeCharacters(s, k):
    freq = [0, 0, 0]
    for c in s:
        freq[ord(c) - ord('a')] += 1
    if min(freq) < k:
        return -1
    res = float('inf')
    l = 0
    for r in range(len(s)):
        freq[ord(s[r]) - ord('a')] -= 1
        while min(freq) < k:
            freq[ord(s[l]) - ord('a')] += 1
            l += 1
        res = min(res, len(s) - (r - l + 1))
    return res
print(takeCharacters("aabaaaacaabc", 2))
