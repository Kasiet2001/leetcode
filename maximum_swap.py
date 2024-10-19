def maximumSwap(num):
    stack = []
    num = list(str(num))
    for i in range(len(num)):
        while stack and num[stack[-1]] < num[i]:
            stack.pop()
        stack.append(i)
    large = small = None
    for i in range(len(stack)):
        if i != stack[i] and not large and not small:
            large = stack[i]
            small = i
        elif large and num[large] == num[stack[i]]:
            large = stack[i]
    if large != None:
        num[small], num[large] = num[large], num[small]
    return int(''.join(num))
print(maximumSwap(2736))