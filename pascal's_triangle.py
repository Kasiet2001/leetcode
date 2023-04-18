def generate(numRows):
    t = [[1], [1, 1]]
    if numRows < 3:
        return t[:numRows]
    while numRows - 2:
        n = 0
        r = [1]
        for i in range(len(t[-1]) - 1):
            r.append(t[-1][n] + t[-1][n + 1])
            n += 1
        r.append(1)
        t.append(r)
        numRows -= 1
    return t
print(generate(5))