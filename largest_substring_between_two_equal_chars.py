def maxLengthBetweenEqualCharacters(s):
    first_occ = dict()
    n = len(s)
    ans = -1
    for i in range(n):
        if s[i] in first_occ:
            ans = max(ans, i - first_occ[s[i]] - 1)
        else:
            first_occ[s[i]] = i
    return ans
print(maxLengthBetweenEqualCharacters("cbzxy"))