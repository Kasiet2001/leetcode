from collections import Counter
def minSteps(s, t):
    s = Counter(s)
    t = Counter(t)
    n = s - t + (t - s)
    return sum(n.values())
print(minSteps("leetcode", "coats"))
