def minimumChairs(s):
    ans = float('-inf')
    p = 0
    for i in s:
        if i == 'E':
            p += 1
        else:
            p -= 1
        ans = max(ans, p)
    return ans