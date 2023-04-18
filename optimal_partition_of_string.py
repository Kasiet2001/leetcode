def partitionString(s):
    t = 1
    p = ''
    for c in s:
        if c in p:
            t += 1
            p = ''
        p += c
    return t
print(partitionString("ssssss"))