def canBeEqual(s1, s2):
    if s1 == s2:
        return True
    if s1 == s2[2] + s2[1] + s2[0] + s2[3]:
        return True
    elif s1 == s2[0] + s2[3] + s2[2] + s2[1]:
        return True
    elif s1 == s2[2] + s2[3] + s2[0] + s2[1]:
        return True
    return False
print(canBeEqual("abcd", "cdab"))