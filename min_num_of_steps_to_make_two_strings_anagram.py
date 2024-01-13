from collections import Counter
def minSteps(s, t):
    '''freq = [0] * 26
    for c in range(len(s)):
        freq[ord(s[c]) - ord('a')] += 1
        freq[ord(t[c]) - ord('a')] -= 1
    ans = 0
    for i in range(26):
        if freq[i] > 0:
            ans += freq[i]
    return ans'''

    return sum((Counter(t) - Counter(s)).values())

print(minSteps("leetcode", "practice"))