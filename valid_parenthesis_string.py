def checkValidString(s):
    stack = []
    asterisk = []
    for idx, char in enumerate(s):
        if char == '(':
            stack.append(idx)
        elif char == '*':
            asterisk.append(idx)
        else:
            if stack:
                stack.pop()
            elif asterisk:
                asterisk.pop()
            else:
                return False
    while stack and asterisk:
        if stack[-1] > asterisk[-1]:
            return False
        stack.pop()
        asterisk.pop()
    return len(stack) == 0
print(checkValidString("(*)(()"))