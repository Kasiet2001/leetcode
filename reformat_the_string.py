def reformat(s):
    x = [i for i in s if i.isalpha()]
    y = [i for i in s if i.isdigit()]
    if len(y) > len(x):
        x, y = y, x
    if len(x) - len(y) > 1:
        return ''
    ans = []
    while x:
        ans.append(x.pop())
        if y:
            ans.append(y.pop())
    return ''.join(ans)[::-1]
print(reformat("a0b1c2"))
