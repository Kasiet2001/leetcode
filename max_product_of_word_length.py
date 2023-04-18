def maxProduct(words):
    ans = 0
    words = list(set(words))
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            l = 0
            for ch in words[i]:
                if ch not in words[j]:
                    l = len(words[i]) * len(words[j])
                else:
                    l = 0
                    break
            ans = max(ans, l)
    return ans
print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))