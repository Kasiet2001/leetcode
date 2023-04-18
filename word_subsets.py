def wordSubsets(words1, words2):
    from collections import Counter
    ans = Counter()
    for w2 in words2:
        ans |= Counter(w2)
    return [w1 for w1 in words1 if not ans - Counter(w1)]
print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ['oo']))
