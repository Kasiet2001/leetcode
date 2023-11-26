def beautifulSubstrings(s, k):
    n = len(s)
    ans = 0
    vowels = 'a, e, i, o, u'
    for i in range(n):
        v = 0
        c = 0
        for j in range(i, n):
            if s[j] in vowels:
                v += 1
            else:
                c += 1
            if v == c and (v * c) % k == 0:
                ans += 1
    return ans
print(beautifulSubstrings("baeyh", 2))

