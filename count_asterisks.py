def countAsterisks(s):
    ans = 0
    n = 0
    for i in s:
        if n == 0 and i == '*':
            ans += 1
        elif i == '|':
            n += 1
            if n == 2:
                n = 0
    return ans
print(countAsterisks("yo|uar|e**|b|e***au|tifu|l"))