from collections import defaultdict
def maximumNumberOfStringPairs(words):
    ans = 0
    d = defaultdict(int)
    for i in words:
        d[i] += 1
    for k, v in d.items():
        d[k] -= 1
        if k[::-1] in d and d[k[::-1]] > 0:
            ans += 1
            d[k[::-1]] -=1
    return ans
print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))