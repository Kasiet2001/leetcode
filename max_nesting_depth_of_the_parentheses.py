def maxDepth(s):
    opening = 0
    ans = 0
    for ch in s:
        if ch == '(':
            opening += 1
        elif ch == ')':
            ans = max(ans, opening)
            opening -= 1
    return ans
print(maxDepth("(1)+((2))+(((3)))"))