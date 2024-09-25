def sumPrefixScores(words):
    hashMap = dict()
    for w in words:
        for i in range(1, len(w) + 1):
            hashMap[w[:i]] = hashMap.get(w[:i], 0) + 1
    ans = [0] * len(words)
    for i in range(len(words)):
        for j in range(1, len(words[i]) + 1):
            if words[i][:j] in hashMap:
                ans[i] += hashMap[words[i][:j]]
    return ans
print(sumPrefixScores(["abcd"]))