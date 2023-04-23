def licenseKeyFormatting(s, k):
    s = ''.join(s.split('-'))
    s = s[::-1]
    ans = ''
    n = ''
    for i in range(len(s)):
        n += s[i]
        if len(n) == k:
            ans += n + '-'
            n = ''
    ans += n
    return ans[::-1].upper().lstrip('-')
print(licenseKeyFormatting("5F3Z-2e-9-w", 4))