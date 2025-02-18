def smallestNumber(pattern):
    stack = []
    result = ''
    n = len(pattern)
    for i in range(n + 1):
        stack.append(i + 1)
        if n == i or pattern[i] == 'I':
            while stack:
                result += str(stack.pop())
    return result
print(smallestNumber("IIIDIDDD"))