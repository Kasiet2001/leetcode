def findSubstring(s, words):
    from collections import Counter
    ans = []
    wlen = len(words[0])
    l = len(words) * wlen
    for p in range(wlen):
        i = p
        dic = Counter(words)
        for j in range(i, len(s) + 1 - wlen, wlen):
            w = s[j: j + wlen]
            dic[w] -= 1
            while dic[w] < 0:
                dic[s[i: i + wlen]] += 1
                i += wlen
            if i + l == j + wlen:
                ans.append(i)
    return ans
print(findSubstring("ababababab", ["ababa","babab"]))