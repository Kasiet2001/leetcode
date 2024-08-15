def decodeString(s):
    stack = []
    for i in s:
        if i != ']':
            stack.append(i)
        else:
            curr_str = ''
            while stack[-1] != '[':
                curr_str = stack.pop() + curr_str
            stack.pop()

            curr_num = ''
            while stack and stack[-1].isdigit():
                curr_num = stack.pop() + curr_num
            curr_str *= int(curr_num)
            stack.append(curr_str)
    return ''.join(stack)
print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
