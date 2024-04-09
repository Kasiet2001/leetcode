def getSmallestString(s, k):
    ans = ''
    for i in s:
        back = ord(i) - ord('a')
        front = ord('z') - ord(i) + 1
        diff = min(back, front)
        if k >= diff:
            k -= diff
            ans += 'a'
        else:
            n = ord(i) - k
            ans += chr(n)
            k = 0
    return ans
print(getSmallestString("xaxcd", 4))