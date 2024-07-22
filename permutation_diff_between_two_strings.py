def findPermutationDifference(s, t):
    t_idx = dict()
    for i in range(len(t)):
        t_idx[t[i]] = i
    ans = 0
    for i, ch in enumerate(s):
        ans += abs(i - t_idx[ch])
    return ans
print(findPermutationDifference("abcde", "edbac"))