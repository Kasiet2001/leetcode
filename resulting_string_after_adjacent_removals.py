def resultingString(s):
    stack = []
    def are_consecutive(c1, c2):
        return abs(ord(c1) - ord(c2)) == 1 or (c1 == 'a' and c2 == 'z') or (c1 == 'z' and c2 == 'a')

    for char in s:
        if stack and are_consecutive(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
print(resultingString("adcb"))
