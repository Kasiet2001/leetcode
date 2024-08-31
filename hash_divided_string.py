def stringHash(s, k):
    ans = []
    ch = 0
    curr_substr = 0
    for i in range(len(s)):
        ch += 1
        curr_substr += ord(s[i]) - 97
        if ch == k:
            ans.append(chr((curr_substr % 26) + 97))
            curr_substr = 0
            ch = 0
    return ''.join(ans)
print(stringHash("mxz", 3))