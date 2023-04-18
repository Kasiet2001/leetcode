def minRemoveToMakeValid(s):
    n = []
    l = list(s)
    for i in range(len(s)):
        if s[i] == '(':
            n.append(i)
        elif s[i] == ')':
            if len(n) != 0:
                n.pop()
            else:
                l[i] = ''
    for i in n:
        l[i] = ''
    return ''.join(l)
print(minRemoveToMakeValid("a)b(c)d"))
