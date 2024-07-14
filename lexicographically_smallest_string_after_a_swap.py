def getSmallestString(s):
    ans = []
    for i in range(len(s)):
        if ans:
            if int(ans[-1]) % 2 == int(s[i]) % 2 and ans[-1] > s[i]:
                last = ans[-1]
                ans[-1] = s[i]
                ans.append(last)
                return ''.join(ans) + s[i + 1:]
            else:
                ans.append(s[i])
        else:
            ans.append(s[i])
    return s
print(getSmallestString("001"))
