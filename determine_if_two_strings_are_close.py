def closeStrings(word1, word2):
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False
    d1 = dict()
    d2 = dict()
    for i in range(len(word1)):
        d1[word1[i]] = d1.get(word1[i], 0) + 1
        d2[word2[i]] = d2.get(word2[i], 0) + 1
    return sorted(d1.values()) == sorted(d2.values())
print(closeStrings("abc", "bca"))