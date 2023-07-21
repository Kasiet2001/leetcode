def oddString(words):
    n = len(words)
    res = []
    for i in words:
        k = []
        for j in range(1, len(i)):
            k.append(ord(i[j]) - ord(i[j - 1]))
        res.append(k)
    for m in range(n):
        if res.count(res[m]) == 1:
            return words[m]
    return ''
print(oddString(["adc","wzy","abc"]))