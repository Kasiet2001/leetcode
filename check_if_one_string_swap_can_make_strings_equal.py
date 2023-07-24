def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True
    elif sorted(s1) != sorted(s2):
        return False
    n = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            n += 1
        if n == 2:
            return True
    return False
print(areAlmostEqual("kelb", "kelb",))