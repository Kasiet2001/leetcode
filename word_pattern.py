def wordPattern(pattern, s):
    s = s.split()
    pattern = list(pattern)
    d = {}
    if len(set(pattern)) != len(set(s)):
        return False
    elif len(pattern) != len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in d:
            d[pattern[i]] = s[i]
        elif d[pattern[i]] != s[i]:
            return False
    return True
print(wordPattern("abba", "dog cat cat fish"))