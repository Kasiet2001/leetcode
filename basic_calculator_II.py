def calculate(s):
    s += '+'
    stack, curr = [], 0
    op = '+'
    for i in s:
        if i.isdigit():
            curr = (curr * 10) + int(i)
        elif i == ' ':
            continue
        else:
            if op == '+':
                stack.append(curr)
            elif op == '-':
                stack.append(-curr)
            elif op == '*':
                stack.append(stack.pop() * curr)
            elif op == '/':
                stack.append(int(stack.pop() / curr))
            curr = 0
            op = i
    return sum(stack)
print(calculate("3+2*2"))
