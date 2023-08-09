from  collections import defaultdict
def findReplaceString(s, indices, sources, targets):
    d = {indices[i]: [sources[i], targets[i]] for i in range(len(indices))}
    n, ans = 0, ''
    while n < len(s):
        if n in d and d[n][0] == s[n: len(d[n][0]) + n]:
            ans += d[n][1]
            n += len(d[n][0])
        else:
            ans += s[n]
            n += 1
    return ans
print(findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))