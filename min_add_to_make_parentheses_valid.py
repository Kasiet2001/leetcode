def minAddToMakeValid(s):
    r = 0
    l = 0
    for i in s:
        if r == 0 and i == ')':
            l += 1
        else:
            if i == '(':
                r += 1
            else:
                r -= 1
    return l + r

print(minAddToMakeValid("()))(("))