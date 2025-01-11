from collections import Counter
def canConstruct(s, k):
    if len(s) < k:
        return False
    odd = 0
    freq = Counter(s)
    for key, v in freq.items():
        if v % 2 == 1:
            odd += 1
    return odd <= k
print(canConstruct("true", 4))