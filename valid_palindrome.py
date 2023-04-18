def isPalindrome(s):
    s = ''.join([i.lower() for i in s if i.isdigit() or i.isalpha()])
    return s == s[::-1]
print(isPalindrome("0a"))