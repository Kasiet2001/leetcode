def isSubsequence(s, t):
    ind_s = ind_t = 0
    while ind_s < len(s) and ind_t < len(t):
        if s[ind_s] == t[ind_t]:
            ind_s += 1
        ind_t += 1
    return ind_s == len(s)
print(isSubsequence("b", "abc"))