def minimumOperationsToMakeKPeriodic(word, k):
    freq = dict()
    n = len(word)
    for i in range(0, n, k):
        w = word[i: i + k]
        freq[w] = freq.get(w, 0) + 1
    m = max(freq.values())
    ans = n // k - m
    return ans
print(minimumOperationsToMakeKPeriodic("leetcoleet", 2))
