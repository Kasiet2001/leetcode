from collections import defaultdict
def maxSubstrings(word):
    seen = defaultdict(int)
    ans = 0
    for i, ch in enumerate(word):
        if ch in seen and i - seen[ch] >= 3:
            ans += 1
            seen = defaultdict(int)
        elif ch not in seen:
            seen[ch] = i
    return ans
print(maxSubstrings("abcdeafdef"))