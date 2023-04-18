def backspaceCompare(s, t):
    n = ''
    m = ''
    for i in s:
        if i != '#':
            n += i
        else:
            n = n[:-1]
    for j in t:
        if j != '#':
            m += j
        else:
            m = m[:-1]
    return True if n == m else False
print(backspaceCompare("a#c","b"))