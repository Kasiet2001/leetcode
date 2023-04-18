def removeStars(s):
    res = []
    for i in s:
        if i != '*':
            res.append(i)
        else:
            res.pop()
    return ''.join(res)
print(removeStars("leet**cod*e"))