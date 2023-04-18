def removeDuplicates(s):
    res = []
    for i in s:
        if res == [] or res[-1] != i:
            res.append(i)
        else:
            res.pop()
    return ''.join(res)
print(removeDuplicates("abbaca"))