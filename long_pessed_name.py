def isLongPressedName(name, typed):
    i = 0
    j = 0
    n = len(name)
    t = len(typed)
    while j < t:
        if i < n and typed[j] == name[i]:
            i += 1
        elif j == 0 or typed[j] != typed[j - 1]:
            return False
        j += 1
    return i == n
print(isLongPressedName("alex", "aaleex"))