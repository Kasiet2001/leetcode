def evaluate(s, knowledge):
    d = {k: v for k, v in knowledge}
    n = s.split('(')
    ans = ''
    for i in n:
        if ')' in i:
            if i[:i.index(')')] in d:
                ans += d[i[:i.index(')')]] + i[i.index(')') + 1:]
            else:
                ans += '?'
        else:
            ans += i
    return ans
print(evaluate("(a)(a)(a)aaa", [["a","yes"]]))