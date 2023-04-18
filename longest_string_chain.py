def longestStrChain(words):
    d = {}
    ans = 1
    for i in sorted(words, key=len):
        d[i] = 1
        for j in range(len(i)):
            n = i[:j] + i[j + 1:]
            if n in d:
                d[i] = max(d[i], d[n] + 1)
                ans = max(d[i], ans)
    return ans
print(longestStrChain(["a","b","ba","bca","bda","bdca"]))