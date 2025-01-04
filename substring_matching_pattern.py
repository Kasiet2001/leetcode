def hasMatch(s, p):
    p = p.split('*')
    if len(p) == 2 and ''.join(p) in s:
        return True
    idx = 0
    n = 0
    i = 0
    while i < len(s) and idx < len(p):
        m = len(p[idx])
        if s[i: i + m] == p[idx]:
            n += 1
            idx += 1
            i += m
        else:
            i += 1
        if n == len(p):
            return True
    return False
print(hasMatch("xks", "*s"))