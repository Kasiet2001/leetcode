def parseBoolExpr(expression):
    def parse_or(s, b):
        n = b.pop()
        while b[-1] != '(':
            n2 = b.pop()
            n = n or n2
        b.pop()
        return n
    def parse_and(s, b):
        n = b.pop()
        while b[-1] != '(':
            n2 = b.pop()
            n = n and n2
        b.pop()
        return n
    def parse_not(a, b):
        n = b.pop()
        b.pop()
        return not n
    bools = []
    signs = []
    for ch in expression:
        if ch == ')':
            s = signs.pop()
            if s == '|':
                bools.append(parse_or(s, bools))
            elif s == '&':
                bools.append(parse_and(s, bools))
            elif s == '!':
                bools.append(parse_not(s, bools))
        elif ch == 'f':
            bools.append(False)
        elif ch == 't':
            bools.append(True)
        elif ch == '(':
            bools.append(ch)
        elif ch in ('!', '&', '|'):
            signs.append(ch)
    return bools[0] == True
print(parseBoolExpr("!(&(f,t))"))

