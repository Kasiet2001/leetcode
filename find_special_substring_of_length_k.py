def hasSpecialSubstring(s, k):
    n = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            n += 1
        else:
            if n == k:
                return True
    return n == k
print(hasSpecialSubstring("a", 1))