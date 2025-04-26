from collections import Counter
def findCommonResponse(responses):
    res = []
    for r in responses:
        s = set(r)
        res.extend(s)
    m = Counter(res)
    maxAppear = max(m.values())
    ans = 'z' * 1000
    for w, v in m.items():
        if v == maxAppear and ans > w:
            ans = w
    return ans
print(findCommonResponse([["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]))
