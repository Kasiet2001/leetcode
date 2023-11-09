def countHomogenous(s):
    mod = 10 ** 9 + 7
    ans = 0
    prev = 'A'
    length = 0
    for i in s:
        if i != prev:
            ans += length * (length + 1) / 2
            length = 1
        else:
            length += 1
        prev = i
    ans += length * (length + 1) / 2
    return ans % mod
print(countHomogenous("abbcccaa"))
