def isValid(s):
    while 'abc' in s:
        s = s.replace('abc', '')
    return len(s) == 0
print(isValid("abccba"))