def scoreOfParentheses(s):
    stack = [0]
    for i in s:
        if i == '(':
            stack.append(0)
        else:
            n = stack.pop()
            stack[-1] += max(2 * n, 1)
    return stack[-1]
print(scoreOfParentheses("(())"))