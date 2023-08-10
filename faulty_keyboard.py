def finalString(s):
    res = []
    for i in s:
        if i == 'i':
            res.reverse()
        else:
            res += i
    return ''.join(res)
print(finalString("string"))