def areOccurrencesEqual(s):
    from collections import Counter
    n = Counter(s)
    return len(set(n.values())) == 1
print(areOccurrencesEqual("abacbc"))