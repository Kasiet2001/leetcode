def countGoodSubstrings(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] != s[i + 1]:
            if s[i + 1] != s[i + 2]:
                if s[i] != s[i + 2]:
                    count += 1
    return count