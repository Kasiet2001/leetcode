def getEncryptedString(s, k):
    n = len(s)
    ans = ''
    for i in range(n):
        ans += s[(i + k) % n]
    return ans