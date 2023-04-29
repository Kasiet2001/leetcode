def isIsomorphic(s, t):
    n = set(zip(s, t))
    return len(set(s)) == len(set(t)) == len(n)
print(isIsomorphic("egg", "add"))