def replaceDigits(s):
    ans = list(s)
    for i in range(1, len(s), 2):
        ans[i] = chr(ord(ans[i - 1]) + int(ans[i]))
    return ''.join(ans)
print(replaceDigits("a1c1e1"))