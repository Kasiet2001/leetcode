def compress(chars):
    if len(chars) == 1:
        return 1
    res = 0
    a = b = 0
    s = ''
    while b < len(chars):
        if chars[a] == chars[b]:
            b += 1
            res += 1
        elif chars[a] != chars[b]:
            if res == 1:
                s += chars[a]
            else:
                s += chars[a] + str(res)
            a = b
            res = 0
    if res == 1:
        s += chars[a]
    else:
        s += chars[a] + str(res)
    chars[:] = [i for i in s]
    return len(chars)
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))