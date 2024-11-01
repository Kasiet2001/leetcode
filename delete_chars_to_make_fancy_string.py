def makeFancyString(s):
    ans = ''
    curr = 0
    for i in range(len(s)):
        if ans and ans[-1] == s[i]:
            curr += 1
            if curr <= 2:
                ans += s[i]
        else:
            curr = 1
            ans += s[i]
    return ans
print(makeFancyString("aaabaaaa"))

