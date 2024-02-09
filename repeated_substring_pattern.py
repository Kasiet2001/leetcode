def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            pattern = s[:i] * (n // i)
            if pattern == s:
                return True
    return False
print(repeatedSubstringPattern("abcabcabcabc"))
