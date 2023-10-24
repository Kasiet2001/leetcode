def getWordsInLongestSubsequence(n, words, groups):
    ans = [words[0]]
    for i in range(1, n):
        if groups[i] != groups[i - 1]:
            ans.append(words[i])
    return ans
print(getWordsInLongestSubsequence(4, ["a","b","c","d"], [1,0,1,1]))