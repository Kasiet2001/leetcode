def prefixCount(words, pref):
    n = len(pref)
    ans = 0
    for w in words:
        if len(w) >= n and w[:n] == pref:
            ans += 1
    return ans
print(prefixCount(["leetcode","win","loops","success"], "code"))