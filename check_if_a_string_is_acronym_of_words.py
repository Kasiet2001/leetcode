def isAcronym(words, s):
    if len(words) != len(s):
        return False
    n = ''
    for i in words:
        n += i[0]
    return n == s
print(isAcronym(["alice","bob","charlie"], "abc"))