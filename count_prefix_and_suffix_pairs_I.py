def countPrefixSuffixPairs(words):
    ans = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                ans += 1
    return ans
print(countPrefixSuffixPairs(["abab","ab"]))