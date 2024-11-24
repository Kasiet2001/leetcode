def isPossibleToRearrange(s, t, k):
    if len(s) % k != 0:
        return False
    m = len(s) // k
    freq1 = {}
    freq2 = []
    for i in range(0, len(s) - m + 1, m):
        freq1[s[i: i + m]] = freq1.get(s[i: i + m], 0) + 1
        freq2.extend([t[i: i + m]])
    for n in freq2:
        if n not in freq1 or freq1[n] == 0:
            return False
        freq1[n] -= 1
    return True
print(isPossibleToRearrange("aabbcc", "bbaacc", 3))