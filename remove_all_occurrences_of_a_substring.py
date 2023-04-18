def removeOccurrences(s, part):
    while part in s:
        s = s.replace(part, '', 1)
    return s
print(removeOccurrences("aabababa", "aba"))