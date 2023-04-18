def isSubsequence(s, t):
    if len(s) > len(t):
        return False
    ind = 0
    for i in range(len(t)):
        if ind <= len(s) - 1:
            if s[ind] == t[i]:
                ind += 1
    return len(s) == ind
print(isSubsequence("b", "abc"))