def reverseParentheses(s):
    stack = []
    curr_str = ''
    for ch in s:
        if ch.isalpha():
            curr_str += ch
        else:
            stack.append(curr_str)
            curr_str = ''
            if ch == ')':
                stack.append(curr_str)
                curr_str = ''
                while stack and stack[-1] != '(':
                    curr_str = stack.pop() + curr_str
                stack.pop()
                stack.append(curr_str[::-1])
                curr_str = ''
            else:
                stack.append(ch)
    return ''.join(stack) + curr_str if curr_str else ''.join(stack)
print(reverseParentheses("a(bcdefghijkl(mno)p)q"))

