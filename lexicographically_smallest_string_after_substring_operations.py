def smallestString(s):
    ans = ''
    changes = 0
    for i in range(len(s)):
        if s[i] != 'a':
            ans += chr(ord(s[i]) - 1)
            changes += 1
        elif changes > 0 and s[i] == 'a':
            return ans + s[i:]
        else:
            ans += s[i]
    return ans if changes else ans[:-1] + 'z'
print(smallestString("a"))