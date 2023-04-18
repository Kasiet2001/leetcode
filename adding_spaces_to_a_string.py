def addSpaces(s, spaces):
    spaces = set(spaces)
    l = len(s)
    res = ''
    for i in range(l):
        if i in spaces:
            res += ' ' + s[i]
        else:
            res += s[i]
    return res
print(addSpaces("icodeinpython", [1,5,7,9]))