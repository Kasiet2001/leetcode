def divideString(s: str, k: int, fill: str):
    if k == 1:
        return [i for i in s]
    s = s + (fill * (k - 1))
    d = []
    while len(s) >= k:
        d.append(s[:k])
        s = s.replace(s[:k], '')
    return d
print(divideString("hjefcvizjkecrioqhywe", 1, 'x'))